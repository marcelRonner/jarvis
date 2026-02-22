# Change Log – ATM System

## How to Read This Log

Each version section lists **every artifact that was created or changed**, with a direct link and a short description of what happened. Inline admonitions and diagram tags for a given version are removed after **two subsequent versions** (cleanup rule).

**Version marker legend:**

| Marker | Meaning |
|---|---|
| 🟢 `new` | Artifact or element added in this version |
| 🟡 `changed` | Existing artifact or element modified |
| 🔴 `deprecated` | Artifact or element scheduled for removal |
| ⚫ `removed` | Artifact or element deleted |

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
