---
applyTo: "docs/state_chart/**"
---

# State Chart Conventions

## When to create a state chart
- Only for domain model entities that have an **Enum status/state** attribute
- Only include state transitions that are **backed by activities** in use case descriptions
- If a domain model state has no use case activity triggering it, document it in a "States Not Covered" section

## Files to produce
- One `.puml` state diagram per entity (e.g. `transactionStateChart.puml`)
- One `.md` documentation page per state chart (e.g. `transactionStateChart.md`)
- File names: `{entityName}StateChart` in **camelCase**

## Markdown structure
```
# State Chart – {Entity Name}
## Overview          → One paragraph + links to domain model and use-case diagram
## Diagram           → Embedded image referencing the .puml file
## States            → Table: State | Description
## Transition Traceability → Table: Transition | Trigger Activity | Use Case | Activity Diagram Step
## States Not Covered → List domain model states with no use case backing
```

## Content rules
- Every row in the **Transition Traceability** table must reference a specific `:action;` label from a use case activity diagram
- The quoted activity string must appear **verbatim** in the referenced `.puml` — `make lint` (check L6) enforces this
- Use case activities that trigger state transitions must use the exact pattern:
  - Creation: `"Bank Backend creates {Entity} (status = {STATE})"`
  - Update: `"Bank Backend updates {Entity} (status = {STATE})"`
- If a use case activity does not explicitly show the state transition, update the use case activity diagram first
- Link to each referenced use case in the traceability table

## PlantUML conventions
- Use `@startuml` / `@enduml`, `!theme plain`, `skinparam stateFontStyle bold`
- The `@startuml` name must equal the file basename (`@startuml transactionStateChart`) — the rendered SVG is named after it
- Title: `title State Chart – {Entity Name}`
- Use `[*] -->` for the initial transition
- State descriptions: `state {STATE} : short description`
- Transition labels must match the trigger activity text from the use case diagrams
- Keep transition labels concise — max 2 lines using `\n`
