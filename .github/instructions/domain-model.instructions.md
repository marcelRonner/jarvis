---
applyTo: "docs/domain_model/**"
---

# Domain Model Conventions

## Files to produce
- `domainModel.md` — Markdown domain model
- `domainModel.puml` — PlantUML class diagram (mirrors the Markdown exactly)

## Markdown structure
```
# Domain Model – {System Name}
## Overview          → One paragraph describing the system scope
## Classes           → One H3 section per class
## Relationships     → Compact notation + descriptive table
```

## Class conventions
- Each class gets an H3 heading (`### ClassName`) with a one-sentence description
- Attributes in a table: `Attribute | Type | Description`
- Supported types: `String`, `Integer`, `Decimal`, `Boolean`, `Date`, `DateTime`, `Enum`
- Enum values listed inline (e.g. `Enum {ONLINE, OFFLINE}`)
- Classes separated by `---` horizontal rules

## Relationships section
- Compact notation with multiplicities: `Bank "1" ---- "1..*" ATM : operates`
- Followed by a descriptive table: `Relationship | Description`

## PlantUML conventions
- Use `@startuml` / `@enduml`, `!theme plain`, `skinparam classAttributeIconSize 0`
- The `@startuml` name must equal the file basename (`@startuml domainModel`) — the rendered SVG is named after it
- All attributes with types inside `class` blocks
- Relationships: `Bank "1" -- "1..*" ATM : operates >`
