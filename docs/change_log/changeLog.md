# Change Log – ATM System

## How to Read This Log

Each version section lists **every artifact that was created or changed**, with a direct link and a short description of what happened, followed by a *Change request & decisions* block recording the request that produced it. Inline admonitions for a given version are removed after **two subsequent versions** (cleanup rule).

**Version marker legend:**

| Marker | Meaning |
|---|---|
| 🟢 `new` | Artifact or element added in this version |
| 🟡 `changed` | Existing artifact or element modified |
| 🔴 `deprecated` | Artifact or element scheduled for removal |
| ⚫ `removed` | Artifact or element deleted |

---

## v1.3 – Documentation Toolchain (2026-08-01)

Restructures how the authoring conventions are delivered to AI agents and adds an automated consistency check. No specification content changed — the ATM system itself is unaffected.

| Artifact | Status | Description |
|---|---|---|
| [Home](../index.md) | 🟡 changed | Added the *How the artifacts interlink* section: dependency chain, join keys, and impact rules; corrected the story count from 15 to 16 |
| `.github/copilot-instructions.md` | 🟡 changed | Reduced from 408 to ~85 lines — persona, protocol, and cross-cutting rules only; artifact conventions moved out |
| `.github/instructions/*.instructions.md` | 🟢 new | Six path-scoped convention files (domain model, business process, use case, state chart, epics, change log). The previous stacked `applyTo:` blocks in a single file were inert; they now load only when the matching folder is edited |
| `.github/prompts/lint-docs.prompt.md` | 🟢 new | `/lint-docs` semantic review: terminology drift, contradictions, coverage gaps, stale claims |
| `scripts/lint_docs.py` | 🟢 new | Seven mechanical checks (L1–L7) covering nav coverage, link integrity, diagram naming, reachability, story-map coverage, activity-label traceability, empty folders |
| `scripts/build_landing.py` | 🟢 new | Generates the instructions embedded in `index.html` from the real instruction files, so the landing page cannot drift from what the agent reads |
| `Makefile` | 🟡 changed | `PUML_FILES` now discovers every `.puml` under `docs/` instead of a hand-maintained list; added `lint`, `landing`, `build`, and `clean` targets |
| `.github/workflows/deploy-docs.yml` | 🟡 changed | Calls `make diagrams` instead of ten hardcoded commands, runs `make lint`, and builds with `--strict` |
| All `.puml` files | 🟡 changed | `@startuml` names normalised to the file basename so the generated SVG name is derivable |
| Generated diagrams (`assets/img/*.svg`) | 🟡 changed | All SVGs regenerated under camelCase names matching their `.puml` source |
| [UC: Print Receipt](../use_case/print_receipt/printReceipt.md), [US-5.1](../epics/user_stories/us_5_1.md), [US-5.3](../epics/user_stories/us_5_3.md), [Epics & Story Map](../epics/epics.md) | 🟡 changed | Added the v1.2 `!!! note` / `!!! warning` admonitions that the convention required but no page carried |
| `docs/assets/css/version-markers.css` | ⚫ removed | The `attr_list`, Mermaid `classDef`, and PlantUML stereotype marker mechanisms were never applied in any artifact; MkDocs admonitions are now the single version-marking notation |
| `docs/use_case/authenticate_qr/`, `docs/use_case/withdraw_foreign_currency/` | ⚫ removed | Empty placeholder folders from abandoned work |

<details><summary>Change request &amp; decisions</summary>

**Requested:** "This repo contains in the docs folder a system documentation that should always be kept up to date with any change that is proposed against it. How the different assets interlink is kept in the copilot-instructions.md — I am wondering now if this is an efficient setup and if this could be optimized. I was looking at this article and was wondering if things could be optimized: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"

**Clarified:**
- Q: Which AI tools drive this repo? → A: GitHub Copilot in VS Code, plus students reading the repo as course material. No `AGENTS.md` / `CLAUDE.md` needed.
- Q: How mechanical should enforcement become? → A: Layered — a deterministic script in CI plus a separate semantic lint prompt.

**Decided:** Measured against the referenced LLM-wiki pattern, the setup already had the wiki (`docs/`), the schema (`copilot-instructions.md`), an index, a log, and a strong *ingest* operation. Two gaps were closed:

1. *Schema delivery.* The seven stacked `applyTo:` blocks only work in `.github/instructions/*.instructions.md` files, which did not exist — so the whole 20 KB file loaded on every request and the path-scoping did nothing. Split into six real scoped files.
2. *The missing lint operation.* Nothing verified the Self-Maintenance Checklist, and drift had accumulated (a `Makefile` entry for a nonexistent file, missing SVGs, PascalCase/camelCase diagram mismatches serving stale images, a wrong story count). Added `make lint`.

Rejected: automating the Makefile↔workflow sync — the duplication was removed instead, by globbing `.puml` files and having CI call the same target. Rejected: keeping the three unused version-marker notations — one applied notation beats three documented ones.

</details>

---

<!--
  A v2.0 "Order Coffee" release previously sat here. It was rolled back on 2026-08-01 so the
  repository can be used in class to demonstrate a change request end to end, starting from a
  clean v1.3 baseline. The full release is preserved in git history at commit ca299e8.
-->

---

## v1.2 – Account Balance on Receipt (2026-03-02)

Every printed Receipt now includes the current Account `balance` so the Customer always knows their remaining funds after a Transaction.

| Artifact | Status | Description |
|---|---|---|
| [UC: Print Receipt](../use_case/print_receipt/printReceipt.md) | 🟡 changed | Postconditions and description updated to mandate Account `balance` on every Receipt |
| [UC: Print Receipt (PlantUML)](../use_case/print_receipt/printReceipt.puml) | 🟡 changed | Activity diagram updated with "ATM retrieves current Account balance" step |
| [Epics & Story Map](../epics/epics.md) | 🟡 changed | US-5.3 added to R2 – Core Transactions |
| [US-5.1](../epics/user_stories/us_5_1.md) | 🟡 changed | Conversation and confirmation updated to reference Account `balance` on Receipt |
| [US-5.3](../epics/user_stories/us_5_3.md) | 🟢 new | "Show Account Balance on Receipt" — MUST/Basic, R2 Core Transactions |

---

## v1.1 – Eject Card Before Cash Dispensing (2026-02-22)

Card is now ejected before cash is dispensed in the withdrawal path, preventing Customers from forgetting their Card. The Session remains `ACTIVE` after Card ejection. Non-withdrawal paths are unchanged.

| Artifact | Status | Description |
|---|---|---|
| [Business Process](../business_process/businessProcess.md) | 🟡 changed | Inserted step 4a.6 "Eject Card" before cash dispensing; renumbered dispensing to 4a.7; step 5.5 now conditional ("Eject Card if not already ejected") |
| [UC Diagram](../use_case/useCaseDiagram.md) | 🟡 changed | Withdraw Cash description updated (BP steps 4a.1–4a.7), added Card ejection mention |
| [UC: Withdraw Cash](../use_case/withdraw_cash/withdrawCash.md) | 🟡 changed | Postconditions, description, and activity diagram updated with Card ejection step |
| [UC: Withdraw Cash (PlantUML)](../use_case/withdraw_cash/withdrawCash.puml) | 🟡 changed | Added "ATM ejects Card" action before "ATM dispenses cash" |
| [Epics & Story Map](../epics/epics.md) | 🟡 changed | Epic 2 BP steps updated to 4a.1–4a.7; US-2.6 added to R1 Walking Skeleton |
| [US-2.1](../epics/user_stories/us_2_1.md) | 🟡 changed | Happy-path conversation and confirmation updated to include Card ejection step |
| [US-2.6](../epics/user_stories/us_2_6.md) | 🟢 new | "Eject Card Before Cash Dispensing" — MUST/Basic, R1 Walking Skeleton |

---

## v1.0 – Initial Release (2026-02-22)

Baseline version establishing all core artifacts for the ATM system.

| Artifact | Status | Description |
|---|---|---|
| [Domain Model](../domain_model/domainModel.md) | 🟢 new | 11 entities: ATM, Bank, Customer, Account, Card, Session, Transaction, Receipt, CashDispenser, CashCassette, AuditLog |
| [Domain Model (PlantUML)](../domain_model/domainModel.puml) | 🟢 new | Class diagram mirroring the Markdown domain model |
| [Business Process](../business_process/businessProcess.md) | 🟢 new | End-to-end ATM interaction flow (steps 1.1 – 5.5) with Mermaid flowchart |
| [Use-Case Diagram](../use_case/useCaseDiagram.md) | 🟢 new | 5 use cases: Authenticate, Withdraw Cash, Check Balance, Transfer Funds, Print Receipt |
| [Use-Case Diagram (PlantUML)](../use_case/useCaseDiagram.puml) | 🟢 new | PlantUML use-case diagram |
| [Actor Descriptions](../use_case/actorDescriptions.md) | 🟢 new | Customer, ATM System, Bank Backend — profiles and system access |
| [UC: Authenticate](../use_case/authenticate/authenticate.md) | 🟢 new | Detailed use case with activity diagram (BP steps 1.1 – 3.1) |
| [UC: Withdraw Cash](../use_case/withdraw_cash/withdrawCash.md) | 🟢 new | Detailed use case with activity diagram (BP steps 4a.1 – 4a.6) |
| [UC: Check Balance](../use_case/check_balance/checkBalance.md) | 🟢 new | Detailed use case with activity diagram (BP step 4b.1) |
| [UC: Transfer Funds](../use_case/transfer_funds/transferFunds.md) | 🟢 new | Detailed use case with activity diagram (BP steps 4c.1 – 4c.3) |
| [UC: Print Receipt](../use_case/print_receipt/printReceipt.md) | 🟢 new | Detailed use case with activity diagram (BP steps 5.2 – 5.3) |
| [State Chart: Transaction](../state_chart/transactionStateChart.md) | 🟢 new | PENDING → COMPLETED / FAILED lifecycle, traced to use case activities |
| [Epics & Story Map](../epics/epics.md) | 🟢 new | 5 epics, 14 user stories across 3 release slices |
| [User Stories](../epics/user_stories/us_1_1.md) (×14) | 🟢 new | 3C format (Card–Conversation–Confirmation) with KANO classification |
