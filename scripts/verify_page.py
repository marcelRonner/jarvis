#!/usr/bin/env python3
"""Record that a person read an artifact and approved it: append an OKF `verified` event.

**Run by the user, never by Jarvis.** `verified:` is the one signal in the documentation that
separates "approved by a person" from "written by an agent", and AGENTS.md forbids Jarvis from
writing it. The change-request protocol ends with the user approving the change; this command is
how that approval is recorded, without hand-typing YAML that is easy to get subtly wrong.

Usage:
    make verify PAGES="content/use_case/withdraw_cash/withdrawCash.md content/sources/cr_1_3.md" [WHO=owner]

Each page gets `{ by: human:<WHO>, at: <now, UTC> }` appended to its `verified:` list — the list is
created if absent, a bare single mapping becomes a list first, and earlier approvals are kept.
`human:` is how an OKF consumer tells a person's approval from a machine's (§5.3, §7).

`generated:` is left alone: approving an artifact is not changing it (OKF v0.2 §5.2).
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone

import yaml

from okflib import CONTENT, FRONTMATTER_RE, ROOT, utc_now, verified_events

VERIFIED_BLOCK_RE = re.compile(r"^verified:.*\n(?:(?:[ \t]+|- ).*\n)*", re.M)
WHO_RE = re.compile(r"[^\s:]+")


def _scalar(value) -> str:
    if isinstance(value, datetime):
        return value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if value.tzinfo else value.isoformat()
    return str(value)


def add_verification(text: str, who: str, at: datetime) -> str:
    """Return `text` with one more verification event; the body and every other key untouched."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("page has no frontmatter to record a verification in")
    meta = yaml.safe_load(match.group(1)) or {}
    events = verified_events(meta if isinstance(meta, dict) else {})
    if not isinstance(events, list) or not all(isinstance(e, dict) for e in events):
        raise ValueError("existing `verified:` is malformed — fix it by hand first, so nothing is lost")
    events = events + [{"by": f"human:{who}", "at": at}]
    lines = ["verified:"]
    for event in events:
        for i, (key, value) in enumerate(event.items()):
            lines.append(f"  {'- ' if i == 0 else '  '}{key}: {_scalar(value)}")
    block = "\n".join(lines) + "\n"
    frontmatter = match.group(1) + "\n"
    if VERIFIED_BLOCK_RE.search(frontmatter):
        frontmatter = VERIFIED_BLOCK_RE.sub(lambda _: block, frontmatter, count=1)
    else:
        frontmatter += block
    return text[: match.start(1)] + frontmatter.rstrip("\n") + text[match.end(1):]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pages", nargs="+", help="artifacts to mark approved, under content/")
    parser.add_argument("--who", default="owner", help="the id after `human:` (default: owner)")
    args = parser.parse_args()
    if not WHO_RE.fullmatch(args.who):
        print(f"verify: '{args.who}' cannot be an actor id — no spaces or colons", file=sys.stderr)
        return 1
    at, failed = utc_now(), 0
    for name in args.pages:
        path = (ROOT / name).resolve()
        if not path.is_file() or CONTENT.resolve() not in path.parents or path.suffix != ".md":
            print(f"verify: {name} is not a Markdown file under content/", file=sys.stderr)
            failed += 1
            continue
        try:
            path.write_text(add_verification(path.read_text(encoding="utf-8"), args.who, at), encoding="utf-8")
        except ValueError as exc:
            print(f"verify: {name}: {exc}", file=sys.stderr)
            failed += 1
            continue
        print(f"verify: human:{args.who} approved {path.relative_to(ROOT)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
