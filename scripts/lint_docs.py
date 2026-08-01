#!/usr/bin/env python3
"""Consistency checks for the ATM documentation set.

The conventions in `.github/instructions/` describe a strict traceability chain between
artifacts. Most of that chain is mechanically checkable, and anything mechanically
checkable should not depend on an agent (or an author) remembering it. This script is
the deterministic half of the "lint" operation; `.github/prompts/lint-docs.prompt.md`
covers the semantic half.

Checks:
    L1  Every docs/**/*.md page appears in the mkdocs.yml nav
    L2  Every relative Markdown link resolves to an existing file
    L3  Diagram naming is consistent: `@startuml <name>` == file basename, every
        referenced SVG has a producing .puml, and the SVG exists on disk
    L4  Every page is reachable by following links from docs/index.md
    L5  Every user story is linked from the epics story map, and any story count
        stated in docs/index.md matches reality
    L6  Every state-chart traceability row quotes an activity label that appears
        verbatim in the referenced use-case activity diagram
    L7  No empty directories under docs/

    L8 (`mkdocs build --strict`) is deliberately not run here — `make build` and the CI
    workflow run it as their own step, so running it here would build the site twice.

Usage:  python3 scripts/lint_docs.py            (from the repo root)
Exit:   0 = clean, 1 = findings
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("lint: PyYAML is required (pip install -r requirements.txt)")

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
MKDOCS = REPO / "mkdocs.yml"

# Markdown links and images: [text](target) / ![alt](target)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
# Fenced code blocks — links inside them are illustrative templates, not real links.
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)

findings: list[str] = []


def report(path: Path, line: int | None, check: str, message: str) -> None:
    loc = path.relative_to(REPO)
    findings.append(f"{loc}:{line or 1}: [{check}] {message}")


def md_files() -> list[Path]:
    return sorted(DOCS.rglob("*.md"))


def puml_files() -> list[Path]:
    return sorted(DOCS.rglob("*.puml"))


def strip_fences(text: str) -> str:
    """Blank out fenced code blocks, preserving line numbering."""
    return FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)


def links_in(path: Path) -> list[tuple[int, str]]:
    """Real (non-template, non-external) link targets with their line numbers."""
    out = []
    for lineno, line in enumerate(strip_fences(path.read_text(encoding="utf-8")).splitlines(), 1):
        for target in LINK_RE.findall(line):
            target = target.split()[0].strip()  # drop optional "title"
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if "{" in target:  # convention template such as us_{epic}_{seq}.md
                continue
            out.append((lineno, target))
    return out


def resolve(source: Path, target: str) -> Path:
    return (source.parent / target.split("#")[0]).resolve()


# --------------------------------------------------------------------------- L1
def load_nav_pages() -> set[Path]:
    class Loader(yaml.SafeLoader):
        pass

    # mkdocs.yml carries !!python/name: tags for superfences; ignore all unknown tags.
    Loader.add_multi_constructor("", lambda loader, suffix, node: None)

    config = yaml.load(MKDOCS.read_text(encoding="utf-8"), Loader=Loader)
    pages: set[Path] = set()

    def walk(node) -> None:
        if isinstance(node, str):
            pages.add((DOCS / node).resolve())
        elif isinstance(node, list):
            for item in node:
                walk(item)
        elif isinstance(node, dict):
            for value in node.values():
                walk(value)

    walk(config.get("nav") or [])
    return pages


def check_nav_coverage() -> None:
    nav = load_nav_pages()
    for page in md_files():
        if page.resolve() not in nav:
            report(page, None, "L1", "page is not listed in the mkdocs.yml nav")


# --------------------------------------------------------------------------- L2
def check_links() -> None:
    for page in md_files():
        for lineno, target in links_in(page):
            if target.endswith(".svg"):
                continue  # generated artifacts — L3 reports these with a more useful message
            resolved = resolve(page, target)
            if not resolved.exists():
                report(page, lineno, "L2", f"broken link -> {target}")


# --------------------------------------------------------------------------- L3
def check_diagrams() -> None:
    produced: dict[str, Path] = {}
    for puml in puml_files():
        first = puml.read_text(encoding="utf-8").splitlines()[0].strip()
        match = re.match(r"@startuml\s+(\S+)", first)
        if not match:
            report(puml, 1, "L3", "first line must be `@startuml <name>`")
            continue
        name = match.group(1)
        if name != puml.stem:
            report(
                puml, 1, "L3",
                f"`@startuml {name}` must equal the file basename `{puml.stem}` "
                f"(it names the generated SVG, so a mismatch silently serves a stale diagram)",
            )
        produced[name] = puml

    for page in md_files():
        for lineno, target in links_in(page):
            if not target.endswith(".svg"):
                continue
            stem = Path(target).stem
            if stem not in produced:
                report(page, lineno, "L3", f"{stem}.svg has no .puml that produces it")
            elif not resolve(page, target).exists():
                report(page, lineno, "L3", f"{stem}.svg is referenced but not generated yet (run `make diagrams`)")


# --------------------------------------------------------------------------- L4
def check_reachable() -> None:
    index = DOCS / "index.md"
    seen = {index.resolve()}
    queue = [index]
    while queue:
        page = queue.pop()
        for _, target in links_in(page):
            resolved = resolve(page, target)
            if resolved.suffix == ".md" and resolved.exists() and resolved not in seen:
                seen.add(resolved)
                queue.append(resolved)

    for page in md_files():
        if page.resolve() not in seen:
            report(page, None, "L4", "page is not reachable by following links from docs/index.md")


# --------------------------------------------------------------------------- L5
def check_stories() -> None:
    story_dir = DOCS / "epics" / "user_stories"
    stories = sorted(story_dir.glob("us_*.md"))
    epics = DOCS / "epics" / "epics.md"

    linked = {resolve(epics, t) for _, t in links_in(epics)}
    for story in stories:
        if story.resolve() not in linked:
            report(story, None, "L5", "story is not linked from the epics.md story map")

    index = DOCS / "index.md"
    for lineno, line in enumerate(index.read_text(encoding="utf-8").splitlines(), 1):
        match = re.search(r"(\d+)\s+stories", line)
        if match and int(match.group(1)) != len(stories):
            report(
                index, lineno, "L5",
                f"states {match.group(1)} stories but {len(stories)} exist in {story_dir.relative_to(REPO)}",
            )


# --------------------------------------------------------------------------- L6
def normalise(text: str) -> str:
    return " ".join(text.split())


def check_traceability() -> int:
    """Every quoted `:action;` label must exist verbatim in the referenced .puml.

    Returns the number of activity labels actually verified, so a state chart written
    without verbatim quotes cannot look 'checked' when nothing was checked.
    """
    verified = 0
    for page in sorted((DOCS / "state_chart").glob("*.md")):
        lines = page.read_text(encoding="utf-8").splitlines()
        in_table = False
        for lineno, line in enumerate(lines, 1):
            if line.startswith("## "):
                in_table = "Transition Traceability" in line
                continue
            if not in_table or not line.strip().startswith("|"):
                continue

            activities = [c for c in re.findall(r"`([^`]+)`", line) if c.startswith(":")]
            if not activities:
                continue

            targets = [t for _, t in links_in_line(page, line) if t.endswith(".md")]
            if not targets:
                report(page, lineno, "L6", "traceability row quotes an activity but links to no use case")
                continue

            puml = resolve(page, targets[0]).with_suffix(".puml")
            if not puml.exists():
                report(page, lineno, "L6", f"referenced use case has no activity diagram ({puml.name})")
                continue

            haystack = normalise(puml.read_text(encoding="utf-8"))
            for activity in activities:
                verified += 1
                if normalise(activity) not in haystack:
                    report(
                        page, lineno, "L6",
                        f"activity `{activity}` does not appear in {puml.relative_to(REPO)} — "
                        f"the state chart and the activity diagram have drifted apart",
                    )
    return verified


def links_in_line(source: Path, line: str) -> list[tuple[int, str]]:
    return [(0, t) for t in LINK_RE.findall(line) if not t.startswith(("http", "#"))]


# --------------------------------------------------------------------------- L7
def check_empty_dirs() -> None:
    for directory in sorted(DOCS.rglob("*")):
        if directory.is_dir() and not any(directory.iterdir()):
            report(directory, None, "L7", "empty directory — complete the artifact or remove the folder")


# --------------------------------------------------------------------------- main
def main() -> int:
    for check in (
        check_nav_coverage,
        check_links,
        check_diagrams,
        check_reachable,
        check_stories,
        check_empty_dirs,
    ):
        check()
    traced = check_traceability()

    if not findings:
        print(f"lint: OK — {len(md_files())} pages, {len(puml_files())} diagrams, no findings")
        if traced:
            print(f"lint: L6 verified {traced} traceability quote(s) against their activity diagrams")
        else:
            print(
                "lint: L6 verified 0 traceability quotes — no state chart quotes an activity\n"
                "      label verbatim yet, so this check currently proves nothing. See\n"
                "      .github/instructions/state-chart.instructions.md for the expected form."
            )
        return 0

    print(f"lint: {len(findings)} finding(s)\n")
    for finding in sorted(findings):
        print(f"  {finding}")
    print("\nSee .github/instructions/ for the conventions these checks enforce.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
