#!/usr/bin/env python3
"""Check the documentation in content/: Open Knowledge Format conformance, frontmatter, and links.

Errors fail; warnings are reported. `--strict` makes warnings fail too.

    E1  frontmatter is missing or not parseable YAML            (OKF v0.2 §11, criterion 1)
    E2  `type:` is empty, or not an artifact type in schema.yml   (OKF v0.2 §11, criterion 2)
    E3  index.md anywhere, or a log.md that breaks §9's structure (OKF v0.2 §3.1, §9, criterion 3)
    E4  `title:` or `description:` is missing, or the description spans several lines
    E5  a relative link or image points at nothing
    E6  `sources:` is malformed: not a list of mappings, an entry with no `resource` or `id`, a
        duplicate id, a resource that does not exist, or a footnote label that is no source id
                                                                   (OKF v0.2 §5.1, §6.2)
    E7  `generated:` or `verified:` is malformed: not a mapping or list of mappings, an actor outside
        the convention, or a datetime without an explicit UTC offset  (OKF v0.2 §5.2, §7)
    E8  `tags:` is not a list of lowercase-kebab strings            (OKF v0.2 §4.1)
    W1  the page's first `# Heading` does not match its `title:`
    W2  a .puml diagram that no page embeds or links
    W3  an artifact with no `sources:` or no `generated:`, where its type requires them
"""

from __future__ import annotations

import re
import sys
from datetime import date

import yaml

from okflib import CONTENT, FOOTNOTE_REF_RE, OKF_ACTOR_RE, ROOT, Page, okf_datetime, resolve_resource

SCHEMA = (yaml.safe_load((ROOT / "schema.yml").read_text(encoding="utf-8")) or {})["types"]
TAG_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

errors: list[str] = []
warnings: list[str] = []


def report(bucket: list[str], path, line: int, code: str, message: str) -> None:
    bucket.append(f"  {path.relative_to(ROOT)}:{line}: [{code}] {message}")


def check_log(page: Page) -> None:
    """OKF v0.2 §9: newest-first `## YYYY-MM-DD` groups holding flat list entries."""
    lines = page.prose().splitlines()
    dates = []
    for i, line in enumerate(lines):
        if line.startswith("## "):
            value = line[3:].strip()
            try:
                parsed = date.fromisoformat(value)
            except ValueError:
                parsed = None
            if not parsed or parsed.isoformat() != value:
                report(errors, page.path, page.line_of(0) + i, "E3", "log.md date headings must be exactly YYYY-MM-DD")
                continue
            dates.append((i, parsed))
    if not dates:
        report(errors, page.path, 1, "E3", "log.md needs at least one YYYY-MM-DD date heading")
        return
    if any(later >= earlier for (_, earlier), (_, later) in zip(dates, dates[1:])):
        report(errors, page.path, 1, "E3", "log.md date headings must be newest first, one per date")
    for n, (start, _) in enumerate(dates):
        end = dates[n + 1][0] if n + 1 < len(dates) else len(lines)
        group = [(start + 1 + k, l) for k, l in enumerate(lines[start + 1:end]) if l.strip()]
        if not group or not group[0][1].startswith("- "):
            report(errors, page.path, page.line_of(0) + start, "E3", "each log date group must begin with a list entry")
        for k, l in group:
            if not (l.startswith("- ") or l.startswith(("  ", "\t"))):
                report(errors, page.path, page.line_of(0) + k, "E3", "log date groups may hold only list items")


def check_trust(page: Page) -> None:
    generated = page.get("generated")
    if generated is not None:
        if not isinstance(generated, dict):
            report(errors, page.path, 1, "E7", "generated: must be a mapping with `by` and `at`")
        else:
            if not OKF_ACTOR_RE.fullmatch(str(generated.get("by") or "")):
                report(errors, page.path, 1, "E7", "generated.by must be `producer/version`, `human:<id>` or `process:<id>`")
            if not okf_datetime(generated.get("at")):
                report(errors, page.path, 1, "E7", "generated.at must be an ISO 8601 datetime with an explicit UTC offset")
    if page.get("verified") is not None:
        events = page.verified_events()
        if not isinstance(events, list):
            report(errors, page.path, 1, "E7", "verified: must be a mapping or a list of mappings")
            return
        for event in events:
            if not isinstance(event, dict):
                report(errors, page.path, 1, "E7", "verified: every event must be a mapping with `by` and `at`")
                continue
            if not OKF_ACTOR_RE.fullmatch(str(event.get("by") or "")):
                report(errors, page.path, 1, "E7", "verified.by must be `human:<id>`, `process:<id>` or `producer/version`")
            if not okf_datetime(event.get("at")):
                report(errors, page.path, 1, "E7", "verified.at must be an ISO 8601 datetime with an explicit UTC offset")


def check_sources(page: Page) -> None:
    raw = page.get("sources")
    if raw is None:
        entries = []
    elif not isinstance(raw, list):
        report(errors, page.path, 1, "E6", "sources: must be a list of mappings")
        return
    else:
        entries = raw
    ids = []
    for entry in entries:
        if not isinstance(entry, dict):
            report(errors, page.path, 1, "E6", f"sources: '{entry}' is not a mapping — write `- id: …` / `resource: …`")
            continue
        resource = str(entry.get("resource") or "").strip()
        ident = str(entry.get("id") or "").strip()
        if not resource:
            report(errors, page.path, 1, "E6", "sources: an entry has no `resource` — OKF requires one per entry")
        else:
            target = resolve_resource(page, resource)
            if target is not None and not target.exists():
                report(errors, page.path, 1, "E6", f"sources: {resource} does not exist")
        if not ident:
            report(errors, page.path, 1, "E6", f"sources: {resource or 'an entry'} has no `id` — footnotes cite sources by id")
        elif ident in ids:
            report(errors, page.path, 1, "E6", f"sources: id '{ident}' is used twice")
        ids.append(ident)
    prose = page.prose()
    for m in FOOTNOTE_REF_RE.finditer(prose):
        if m.group(1) not in ids:
            report(errors, page.path, page.line_of(m.start()), "E6", f"footnote [^{m.group(1)}] names no id in sources:")


def main() -> int:
    strict = "--strict" in sys.argv[1:]
    paths = sorted(CONTENT.rglob("*.md"))
    referenced = set()

    for path in paths:
        page = Page(path)
        if path.name == "index.md":
            report(errors, path, 1, "E3", "index.md is reserved by the Open Knowledge Format — a folder's page is _index.md")
        if page.error:
            report(errors, path, 1, "E1", f"{page.error} — every file in the bundle needs a `---` YAML block")
            continue
        if path.name == "log.md":
            if path.parent != CONTENT:
                report(errors, path, 1, "E3", "the only log.md is content/log.md, generated by `make generate`")
            check_log(page)

        kind = str(page.get("type") or "").strip()
        if not kind:
            report(errors, path, 1, "E2", "no `type:` — the Open Knowledge Format requires one on every file")
        elif kind not in SCHEMA:
            report(errors, path, 1, "E2", f"type '{kind}' is not declared in schema.yml ({', '.join(sorted(SCHEMA))})")

        for key in ("title", "description"):
            if not str(page.get(key) or "").strip():
                report(errors, path, 1, "E4", f"no `{key}:`")
        if "\n" in str(page.get("description") or "").strip():
            report(errors, path, 1, "E4", "description spans several lines — keep it to one sentence")

        tags = page.get("tags")
        if tags is not None and (not isinstance(tags, list) or not all(isinstance(t, str) and TAG_RE.fullmatch(t) for t in tags)):
            report(errors, path, 1, "E8", "tags: must be a list of lowercase-kebab strings, e.g. [account, r1-walking-skeleton]")

        check_sources(page)
        check_trust(page)

        spec = SCHEMA.get(kind) or {}
        for key in spec.get("requires", []):
            if page.get(key) is None:
                report(warnings, path, 1, "W3", f"a `{kind}` should carry `{key}:` — see AGENTS.md")

        heading = re.search(r"^# (.+)$", page.prose(), re.MULTILINE)
        if path.name not in ("_index.md", "log.md") and heading and page.get("title") and heading.group(1).strip() != str(page.get("title")).strip():
            report(warnings, path, page.line_of(heading.start()), "W1", f"`# {heading.group(1).strip()}` does not match title: '{page.get('title')}'")

        for line, target in page.links():
            resolved = (path.parent / target.split("#")[0]).resolve()
            referenced.add(resolved)
            if not resolved.exists():
                report(errors, path, line, "E5", f"{target} does not exist")

    for diagram in sorted(CONTENT.rglob("*.puml")):
        if diagram.resolve() not in referenced:
            report(warnings, diagram, 1, "W2", "no page embeds or links this diagram")

    for line in errors + warnings:
        print(line)
    print(f"lint: {len(errors)} error(s), {len(warnings)} warning(s) — {len(paths)} files")
    return 1 if errors or (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
