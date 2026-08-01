---
applyTo: "docs/epics/**"
---

# Epic & User Story Conventions

## Files to produce
- `epics.md` — Story map overview (epic columns × release rows)
- `user_stories/us_{epic}_{seq}.md` — One file per user story in a `user_stories/` subfolder

## Markdown structure — `epics.md`
```
# Epics & Story Map – {System Name}
## Overview          → One paragraph + links to use-case diagram and domain model
## Story Map         → Table: epic columns × release rows (see table rules below)
```

## Story Map table rules
- **One column per epic** — the epic title is the column header
- The first column is a label column (row headers)
- **Header rows** (above the release slices):
  - **Use Case** — link to the detailed use case description
  - **Goal** — one sentence using domain model entity names
  - **Key Entity** — comma-separated domain model entities
  - **Actor** — must match use-case diagram actors
  - **BP Steps** — business process step range
- **Release rows** (below the header, labelled `R{N} – {Release Name}`):
  - Each row represents a **deliverable release** that can span multiple epics
  - Cells contain `[US-{epic}.{seq}](user_stories/us_{epic}_{seq}.md) {title}` links
  - Stories in the **same row** across different epics form a coherent releasable slice
  - Order rows by priority: top = highest priority (walking skeleton / MVP), bottom = polish / delight
- Every story file must be linked from this table — `make lint` (check L5) enforces this

## Content rules for epics
- Each epic realises **exactly one** use case — no epic may span multiple use cases
- No use case may be split across multiple epics
- Epic naming: `Epic {N}: {Verb} {Object}` matching the use case name (e.g. "Epic 2: Withdraw Cash")
- All entity names must match the domain model exactly (singular, PascalCase)
- Wording in the Goal row must be action-oriented and reference the domain model entity that changes state

## User story conventions

### File naming
- `us_{epic}_{seq}.md` in the `user_stories/` subfolder (e.g. `us_2_3.md` = Epic 2, Story 3)
- Auto-numbered: `US-{epic}.{seq}` (e.g. `US-2.3`)

### 3C format (Card – Conversation – Confirmation)
Every user story file follows this structure:
```
# US-{epic}.{seq} – {Title}
## Card             → As a {Actor}, I {MUST|NEED|WANT|WOULD LIKE} {goal} so that {benefit}.
## Conversation     → Bullet list: context, domain references, activity diagram traceability, KANO classification
## Confirmation     → Given / When / Then acceptance criteria
```

### KANO model → adjective mapping
| KANO Category | Adjective | Meaning |
|---|---|---|
| Basic quality | **MUST** / **NEEDS** | Expected; absence causes dissatisfaction |
| Performance quality | **WANTS** | More is better; satisfaction proportional to fulfilment |
| Attractive quality | **WOULD LIKE** | Delighter; presence surprises positively, absence does not disappoint |

### Content rules for user stories
- Only use actors defined in `docs/use_case/actorDescriptions.md`, and link to it from the story with a relative path (`../../use_case/actorDescriptions.md`)
- The **Card** section is a single sentence following the template exactly
- The **Conversation** section must include:
  - A traceability reference to the corresponding activity in a use case activity diagram
  - The KANO classification with rationale
  - References to domain model entity names and attributes where relevant
- The **Confirmation** section uses Given / When / Then format
- Each acceptance criterion must be independently testable

### New story checklist
A new story is not done until it is (a) written in 3C format, (b) linked from the `epics.md` story map, and (c) added to the `mkdocs.yml` nav under User Stories.
