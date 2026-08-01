---
applyTo: "docs/use_case/**"
---

# Use-Case Diagram Conventions

## Files to produce
- `useCaseDiagram.puml` — PlantUML use-case diagram
- `useCaseDiagram.md` — Markdown documentation describing actors, use cases, and relationships

## Markdown structure
```
# Use-Case Diagram – {System Name}
## Overview          → One paragraph + link to business process
## Diagram           → Embedded image referencing the generated SVG or the .puml file
## Actors            → Table: Actor | Type (Primary / Supporting) | Description
## Use Cases         → One H3 section per use case with a brief description
                       and traceability back to business process steps
## Relationships     → Table: Relationship | Type (include / extend) | Description
```

## Actor conventions
- Every actor must originate from the business process — do not invent actors
- Classify actors as **Primary** (initiates the interaction) or **Supporting** (provides a service)
- Use the same actor names as in the business process legend (e.g. "Customer", "Bank Backend")
- Actors table columns: `Actor | Type | Description`
- Description must reference the business process role (e.g. "see 🟦 Customer in the Business Process")

## Use-case conventions
- Each use case represents a **user goal** — not an individual process step or system action
- Derive use cases from the **transaction branches** in the business process (e.g. one use case per branch at the "Select transaction type" decision)
- Naming: **verb-first**, 2–3 words, present tense (e.g. "Withdraw Cash", not "Cash Withdrawal" or "The customer withdraws cash")
- Each use case gets an H3 heading (`### Use Case Name`) with:
  - One sentence describing the goal
  - A **traceability reference** to the corresponding business process steps using the step numbering (e.g. "Corresponds to **Business Process steps 4a.1 – 4a.6**")
- Use cases separated by blank lines (no `---` rules — those are for domain model classes)

## Relationship conventions
- **`<<include>>`** — use for mandatory sub-flows that are shared across multiple use cases (e.g. authentication). The arrow points **from** the base use case **to** the included use case.
- **`<<extend>>`** — use for optional behaviour that may or may not occur (e.g. printing a receipt). The arrow points **from** the base use case **to** the extending use case.
- Do **not** use `<<include>>` / `<<extend>>` for one-off steps that belong inside a single use case
- Relationships table columns: `Relationship | Type | Description`
- Every relationship in the `.puml` file must have a matching row in the Markdown table

## PlantUML conventions
- Use `@startuml` / `@enduml`, `left to right direction`, `skinparam actorStyle awesome`
- The `@startuml` name must equal the file basename (`@startuml useCaseDiagram`) — the rendered SVG is named after it
- System boundary: `rectangle "System Name" { … }`
- Primary actors on the **left**, supporting actors on the **right**
- Use `usecase "Name" as UC_Alias` for readable aliases
- Actors connect to use cases with `--` (solid lines), relationships use `..>` (dashed arrows)
- Keep the diagram **flat** — no nested rectangles or packages inside the system boundary
- Use cases represent the **goal** an actor wants to achieve, not individual process steps

## Detailed Use-Case Description Conventions

Each use case from the use-case diagram gets its own **subfolder** under `use_case/` (e.g. `use_case/withdraw_cash/`). Folder names use **snake_case**.

Never leave an empty use-case folder behind — either complete it or remove it.

### Files to produce per use case
- `{useCaseName}.md` — Markdown description (camelCase file name)
- `{useCaseName}.puml` — PlantUML activity diagram (camelCase file name)

### Markdown structure
```
# Use Case – {Use Case Name}
## Overview          → One paragraph + links to use-case diagram and business process
## Preconditions     → Bullet list of conditions that must be true before the use case starts
## Postconditions    → Grouped by outcome (Success / Failure variants) as bullet lists
## Description       → One paragraph narrative of the flow using domain model entity names
## Activity Diagram  → Embedded image referencing the .puml file
```

### Content rules
- **Preconditions** and **Postconditions** must reference domain model entities and their attributes/states (e.g. "Session with status `ACTIVE`")
- **Description** is a plain-English walkthrough — do not duplicate the activity diagram step-by-step; summarise the intent
- Every use case must include a **traceability reference** to the corresponding business process step numbers
- Use `---` horizontal rules to separate major sections

### PlantUML activity diagram conventions
- Use `@startuml` / `@enduml`, `!theme plain`
- The `@startuml` name must equal the file basename (`@startuml withdrawCash`) — the rendered SVG is named after it
- Title: `title Activity Diagram – {Use Case Name}`
- Use `:action;` for activities, `if (...) then (...)` / `else (...)` for decisions
- Use `while (...) is (...)` / `endwhile (...)` for loops
- Use `stop` for every terminal path (success and failure)
- Reference domain model entity names in action labels (e.g. "Bank Backend debits Account")
- Keep labels concise — max 2 lines using `\n`

Activity labels are the **traceability join key** for state charts and user stories. State-chart traceability tables quote these strings verbatim, so changing a label means updating every artifact that quotes it.
