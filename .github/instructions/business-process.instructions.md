---
applyTo: "docs/business_process/**"
---

# Business Process Conventions

## Files to produce
- `businessProcess.md` — Markdown with embedded Mermaid diagram (no separate diagram files)

## Markdown structure
```
# Business Process – {Process Name}
## Overview          → One paragraph + link to domain model
## Process Diagram   → Legend + embedded Mermaid flowchart
```

## Mermaid diagram rules

**Layout:** Use `flowchart TD` (top-down). Never use `LR` for complex processes.

**Actors via color-coded classes** (not subgraphs — they render poorly):

| Actor / Role   | classDef Name | Fill      | Stroke    | Text Color |
|----------------|---------------|-----------|-----------|------------|
| Customer/User  | `customer`    | `#DBEAFE` | `#2563EB` | `#1E3A5F`  |
| System/ATM     | `atm`         | `#FEF9C3` | `#CA8A04` | `#713F12`  |
| Backend/Bank   | `bank`        | `#DCFCE7` | `#16A34A` | `#14532D`  |
| Decision       | `decision`    | `#FEE2E2` | `#DC2626` | `#7F1D1D`  |

Add a text legend above the diagram: `**Legend:** 🟦 Customer 🟨 ATM System 🟩 Bank Backend 🟥 Decision`

**Step numbering:** `{phase}.{step}` (e.g. `1.1`, `2.3`). Parallel branches: `4a.1`, `4b.1`. Alternate paths: `4a.3a`.

These step IDs are the **traceability join key** for use cases and epics — never renumber an existing step without updating every artifact that cites it.

**Node shapes:** Rectangles `["..."]` for actions, diamonds `{"..."}` for decisions, double circles `(("Start"))` / `(("End"))`.

**Node labels:** Max 2 lines, use `\n`. Describe WHAT, not WHO (color = actor). Reference domain model entity names.

**Edges:** `-->` for flow, `-->|label|` for conditions. Loop-backs to the originating decision node.

**General:** Include happy + error paths. All terminal paths end at `(("End"))`. Node IDs in camelCase.
