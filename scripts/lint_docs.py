#!/usr/bin/env python3
"""Check the documentation in content/: Open Knowledge Format conformance, frontmatter, and links.

Errors fail; warnings are reported. `--strict` makes warnings fail too.

    E1  frontmatter is missing or not parseable YAML          (OKF v0.2 §11, criterion 1)
    E2  `type:` is empty, or not an artifact type in schema.yml (OKF v0.2 §11, criterion 2)
    E3  a file is named index.md or log.md                    (OKF v0.2 §3.1 reserves both)
    E4  `title:` or `description:` is missing, or the description spans several lines
    E5  a relative link or image points at nothing
    W1  the page's first `# Heading` does not match its `title:`
    W2  a .puml diagram that no page embeds or links

The Open Knowledge Format asks three things of a bundle: parseable frontmatter on every file, a
non-empty type on every file, and reserved filenames that follow their structure. The first two are
E1 and E2. For the third, this documentation uses neither reserved name — Hugo's `_index.md` is a
section page, and the change log is changeLog.md — so E3 keeps it that way instead of validating a
structure nothing here should have.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
TYPES = set((yaml.safe_load((ROOT / "schema.yml").read_text(encoding="utf-8")) or {})["types"])

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.DOTALL)
FENCE_RE = re.compile(r"^```.*?^```", re.DOTALL | re.MULTILINE)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

errors: list[str] = []
warnings: list[str] = []


def report(bucket: list[str], path: Path, line: int, code: str, message: str) -> None:
    bucket.append(f"  {path.relative_to(ROOT)}:{line}: [{code}] {message}")


def lineno(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def main() -> int:
    strict = "--strict" in sys.argv[1:]
    pages = sorted(CONTENT.rglob("*.md"))
    referenced: set[Path] = set()

    for path in pages:
        text = path.read_text(encoding="utf-8")
        if path.name in ("index.md", "log.md"):
            report(errors, path, 1, "E3", f"{path.name} is reserved by the Open Knowledge Format — a folder's page is _index.md")

        match = FRONTMATTER_RE.match(text)
        if not match:
            report(errors, path, 1, "E1", "no frontmatter — every file in the bundle needs a `---` YAML block")
            continue
        try:
            meta = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as exc:
            report(errors, path, 1, "E1", f"frontmatter is not valid YAML: {exc}".splitlines()[0])
            continue
        if not isinstance(meta, dict):
            report(errors, path, 1, "E1", "frontmatter is not a mapping")
            continue

        kind = str(meta.get("type") or "").strip()
        if not kind:
            report(errors, path, 1, "E2", "no `type:` — the Open Knowledge Format requires one on every file")
        elif kind not in TYPES:
            report(errors, path, 1, "E2", f"type '{kind}' is not declared in schema.yml ({', '.join(sorted(TYPES))})")

        for key in ("title", "description"):
            if not str(meta.get(key) or "").strip():
                report(errors, path, 1, "E4", f"no `{key}:`")
        if "\n" in str(meta.get("description") or "").strip():
            report(errors, path, 1, "E4", "description spans several lines — keep it to one sentence")

        body_start = match.start(2)
        body = FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), match.group(2))
        heading = re.search(r"^# (.+)$", body, re.MULTILINE)
        if path.name != "_index.md" and heading and meta.get("title") and heading.group(1).strip() != str(meta["title"]).strip():
            report(warnings, path, lineno(text, body_start + heading.start()), "W1",
                   f"`# {heading.group(1).strip()}` does not match title: '{meta['title']}'")

        for m in LINK_RE.finditer(body):
            target = m.group(1)
            if re.match(r"^[a-z][a-z0-9+.-]*:|^#|^//", target, re.I):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            referenced.add(resolved)
            if not resolved.exists():
                report(errors, path, lineno(text, body_start + m.start()), "E5", f"{target} does not exist")

    for diagram in sorted(CONTENT.rglob("*.puml")):
        if diagram.resolve() not in referenced:
            report(warnings, diagram, 1, "W2", "no page embeds or links this diagram")

    for line in errors + warnings:
        print(line)
    print(f"lint: {len(errors)} error(s), {len(warnings)} warning(s) — {len(pages)} files")
    return 1 if errors or (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
