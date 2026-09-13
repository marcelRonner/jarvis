"""Reading the documentation the way an Open Knowledge Format consumer does.

Shared by the checks (lint_docs.py), the owner's verification command (verify_page.py) and the
consumer acceptance tests. Kept deliberately forgiving: a reader that rejects a concept for an
unknown type, an extra key or a missing optional field would break OKF v0.2 §11 — rejecting such
things is the linter's decision, as producer policy, never the reader's.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.DOTALL)
FENCE_RE = re.compile(r"^```.*?^```", re.DOTALL | re.MULTILINE)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]\s]+)\](?!:)")

# OKF v0.2 §5: every timestamp is an ISO 8601 datetime with an explicit UTC offset.
OKF_DATETIME_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})$")
# OKF v0.2 §7: `<producer>/<version>`, `human:<id>` or `process:<id>`.
OKF_ACTOR_RE = re.compile(r"(?:human|process):[^\s:]+|[^\s/:]+/[^\s/]+")


class Page:
    """One Markdown file: its frontmatter as a mapping, and its body."""

    def __init__(self, path: Path):
        self.path = path
        self.text = path.read_text(encoding="utf-8")
        self.error: str | None = None
        self.meta: dict = {}
        self.body = self.text
        self.body_offset = 0
        match = FRONTMATTER_RE.match(self.text)
        if not match:
            self.error = "missing frontmatter"
            return
        self.body, self.body_offset = match.group(2), match.start(2)
        try:
            meta = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as exc:
            self.error = f"frontmatter is not valid YAML: {str(exc).splitlines()[0]}"
            return
        if not isinstance(meta, dict):
            self.error = "frontmatter is not a mapping"
            return
        self.meta = meta

    def get(self, key, default=None):
        return self.meta.get(key, default)

    def prose(self) -> str:
        """The body with fenced code blanked out, line numbers kept."""
        return FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), self.body)

    def line_of(self, body_index: int) -> int:
        return self.text.count("\n", 0, self.body_offset + body_index) + 1

    def links(self) -> list[tuple[int, str]]:
        """Relative link and image targets, with line numbers."""
        out = []
        prose = self.prose()
        for m in LINK_RE.finditer(prose):
            target = m.group(1)
            if re.match(r"^[a-z][a-z0-9+.-]*:|^#|^//", target, re.I):
                continue
            out.append((self.line_of(m.start()), target))
        return out

    def sources(self) -> list:
        """`sources` as a list, whatever shape it was written in."""
        listed = self.get("sources")
        if listed is None:
            return []
        return [listed] if isinstance(listed, dict) else listed

    def verified_events(self):
        return verified_events(self.meta)


def verified_events(meta: dict):
    """`verified` as a list of events. A bare mapping is one event — OKF v0.2 §5.2, a consumer MUST.

    A value that is neither a mapping nor a list comes back unchanged, so a validator can report it.
    """
    verified = meta.get("verified")
    if verified is None:
        return []
    return [verified] if isinstance(verified, dict) else verified


def okf_datetime(value) -> datetime | None:
    """An OKF timestamp as an aware datetime, or None. YAML may already have parsed it."""
    if isinstance(value, datetime):
        return value if value.tzinfo else None
    text = str(value or "")
    if not OKF_DATETIME_RE.fullmatch(text):
        return None
    return datetime.fromisoformat(text.replace("Z", "+00:00"))


def resolve_resource(page: Page, resource: str) -> Path | None:
    """Where a path-valued field points, per OKF v0.2 §6.2: `/…` from the bundle root, else relative."""
    if re.match(r"^[a-z][a-z0-9+.-]*:", resource, re.I):
        return None  # an absolute URL; nothing local to check
    if resource.startswith("/"):
        return (CONTENT / resource.lstrip("/")).resolve()
    return (page.path.parent / resource).resolve()


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)
