---
applyTo: "docs/change_log/**"
---

# Change Log & Version Tracking Conventions

## Files to produce
- `changeLog.md` — Permanent, append-only change log (one section per version)

## Markdown structure
```
# Change Log – {System Name}
## How to Read This Log   → Explanation + version marker legend table
## v{X.Y} – {Title} ({Date}) → One section per version, newest on top when adding
```

## Version section rules
- Each version gets an H2 heading: `## v{X.Y} – {Title} ({YYYY-MM-DD})`
- Below the heading: one-sentence summary of the change
- **Artifact table** with columns: `Artifact | Status | Description`
- Status uses emoji markers: 🟢 `new` · 🟡 `changed` · 🔴 `deprecated` · ⚫ `removed`
- Every artifact that was touched **must** have a row — even if the change is minor
- Link every artifact to its file using relative paths

## Change request & decisions (MANDATORY)

The change log records *what* changed. This block records *why* — the raw input that produced it.
Without it the reasoning evaporates with the chat session and cannot be reconstructed later.

Every version section ends with:

```markdown
<details><summary>Change request &amp; decisions</summary>

**Requested:** the user's original request, verbatim

**Clarified:**
- Q: … → A: …

**Decided:** the approach taken, and any alternative that was considered and rejected (with the reason)

</details>
```

Fill this in from steps 1–3 of the Change-Request Protocol. Quote the request as the user
phrased it — do not paraphrase or tidy it up.

## Inline admonition markers
Use MkDocs admonitions inside affected `.md` files to flag changes:
```markdown
!!! note "v{X.Y} – Added {YYYY-MM-DD}"
    Brief description of what was added.

!!! warning "v{X.Y} – Changed {YYYY-MM-DD}"
    Brief description of what changed.

!!! danger "v{X.Y} – Deprecated {YYYY-MM-DD}"
    Brief description of what is deprecated and when it will be removed.
```

Place the admonition directly under the H1 of the affected page.

Admonitions are the **only** version-marking mechanism. Do not add PlantUML `<<vN-new>>`
stereotypes, Mermaid `classDef vNew/vChanged/vDeprecated` classes, or `attr_list` CSS
markers — those mechanisms were removed in v2.1 because three parallel notations for one
concept were never applied consistently.

## Cleanup rule
- Inline admonitions are **removed after 2 subsequent versions**
- Example: markers from v1.0 are removed when v3.0 is released
- The change log itself is **permanent** — never delete version sections

## Integration with Self-Maintenance Checklist
Whenever you create or modify **any** artifact, you **MUST** also add or update the corresponding entry in `change_log/changeLog.md`. This is an additional mandatory step on top of the existing Self-Maintenance Checklist.
