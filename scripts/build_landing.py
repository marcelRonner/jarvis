#!/usr/bin/env python3
"""Regenerate the embedded Markdown block in index.html from the instruction files.

index.html is a standalone landing page that renders the Jarvis instructions client-side.
It keeps its own copy of the Markdown so the page stays static with no network fetch — but
a hand-maintained copy drifts. This script rebuilds that copy from the real source files,
so the landing page can never disagree with what the agent actually reads.

Usage:
    python3 scripts/build_landing.py            # rewrite the block
    python3 scripts/build_landing.py --check    # exit 1 if out of date (used by `make lint`)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LANDING = REPO / "index.html"
CORE = REPO / ".github" / "copilot-instructions.md"
INSTRUCTIONS = REPO / ".github" / "instructions"

# The generated region inside index.html.
BLOCK_RE = re.compile(
    r'(<script id="raw-md" type="text/markdown">\n).*?(\n\s*</script>)',
    re.DOTALL,
)

ORDER = [
    "domain-model",
    "business-process",
    "use-case",
    "state-chart",
    "epics",
    "change-log",
]


def instruction_files() -> list[Path]:
    found = {p.stem.removesuffix(".instructions"): p for p in INSTRUCTIONS.glob("*.instructions.md")}
    ordered = [found.pop(name) for name in ORDER if name in found]
    ordered.extend(found[name] for name in sorted(found))  # any newly added artifact type
    return ordered


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (applyTo glob, body) for an .instructions.md file."""
    match = re.match(r"---\n(.*?)\n---\n(.*)", text, re.DOTALL)
    if not match:
        return "", text
    glob = re.search(r'applyTo:\s*"?([^"\n]+)"?', match.group(1))
    return (glob.group(1).strip() if glob else ""), match.group(2).lstrip("\n")


def render() -> str:
    parts = [CORE.read_text(encoding="utf-8").rstrip()]
    for path in instruction_files():
        glob, body = split_frontmatter(path.read_text(encoding="utf-8"))
        parts.append(
            "---\n\n"
            f"*`.github/instructions/{path.name}` — applies to `{glob}`*\n\n"
            f"{body.rstrip()}"
        )
    return "\n\n".join(parts)


def main() -> int:
    check = "--check" in sys.argv
    html = LANDING.read_text(encoding="utf-8")
    content = render()

    if "</script>" in content:
        sys.exit("build_landing: instruction text contains </script>; refusing to embed")

    if not BLOCK_RE.search(html):
        sys.exit('build_landing: could not find the <script id="raw-md"> block in index.html')

    updated = BLOCK_RE.sub(lambda m: m.group(1) + content + m.group(2), html)

    if updated == html:
        print("build_landing: index.html is up to date")
        return 0
    if check:
        print("build_landing: index.html is STALE — run `make landing`", file=sys.stderr)
        return 1

    LANDING.write_text(updated, encoding="utf-8")
    print(f"build_landing: index.html updated ({len(content.splitlines())} lines embedded)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
