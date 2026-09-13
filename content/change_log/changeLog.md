---
title: "Change Log – ATM System"
linkTitle: "Change Log"
type: change-log
description: "Version history of the ATM system documentation, listing every artifact created or changed in each version."
weight: 1
sources:
  - id: cr-1-3
    resource: /sources/cr_1_3.md
  - id: cr-1-4
    resource: /sources/cr_1_4.md
generated:
  by: jarvis/1.0
  at: 2026-09-13T07:22:06Z
---

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

## v1.4 – Explain the Repository to Each Audience (2026-09-13)

The documentation home page explains what this is and how the artifacts interlink, and links every other explanation of the repository. No functional change to the ATM system. See [CR-1.4](../sources/cr_1_4.md).

| Artifact | Status | Description |
|---|---|---|
| [Home](../_index.md) | 🟡 changed | New sections *What this is*, *How the artifacts interlink* and *Learn more*; user story count corrected to 16 |
| [Change Log](changeLog.md) | 🟡 changed | This entry |
| [Log](../log.md) | 🟡 changed | Regenerated with v1.4 |
| [CR-1.4](../sources/cr_1_4.md) | 🟢 new | The change request for this version |

---

## v1.3 – Open Knowledge Format Metadata and Concepts (2026-09-12)

Every artifact now records where it derives from, who produced it and which domain entities it concerns, as Open Knowledge Format frontmatter, and each domain entity and actor has its own page. No functional change to the ATM system. See [CR-1.3](../sources/cr_1_3.md).

| Artifact | Status | Description |
|---|---|---|
| [Domain Model – ATM System](../domain_model/domainModel.md) | 🟡 changed | Classes moved to one entity page each; frontmatter adds `sources`, `generated` and `tags` |
| [ATM](../domain_model/entities/atm.md) | 🟢 new | Entity page, split out of the Domain Model |
| [Bank](../domain_model/entities/bank.md) | 🟢 new | Entity page, split out of the Domain Model |
| [Customer](../domain_model/entities/customer.md) | 🟢 new | Entity page, split out of the Domain Model |
| [Account](../domain_model/entities/account.md) | 🟢 new | Entity page, split out of the Domain Model |
| [Card](../domain_model/entities/card.md) | 🟢 new | Entity page, split out of the Domain Model |
| [Session](../domain_model/entities/session.md) | 🟢 new | Entity page, split out of the Domain Model |
| [Transaction](../domain_model/entities/transaction.md) | 🟢 new | Entity page, split out of the Domain Model |
| [Receipt](../domain_model/entities/receipt.md) | 🟢 new | Entity page, split out of the Domain Model |
| [CashDispenser](../domain_model/entities/cashDispenser.md) | 🟢 new | Entity page, split out of the Domain Model |
| [CashCassette](../domain_model/entities/cashCassette.md) | 🟢 new | Entity page, split out of the Domain Model |
| [AuditLog](../domain_model/entities/auditLog.md) | 🟢 new | Entity page, split out of the Domain Model |
| [Business Process – ATM Cash Withdrawal & Services](../business_process/businessProcess.md) | 🟡 changed | Frontmatter adds `sources`, `generated` and `tags` |
| [Use-Case Diagram – ATM System](../use_case/useCaseDiagram.md) | 🟡 changed | Business Process traceability references cited with a footnote; frontmatter adds `sources`, `generated` and `tags` |
| [Actor Descriptions – ATM System](../use_case/actorDescriptions.md) | 🟡 changed | Actors moved to one page each; frontmatter adds `sources`, `generated` and `tags` |
| [Customer](../use_case/actors/customer.md) | 🟢 new | Actor page, split out of the Actor Descriptions |
| [ATM System](../use_case/actors/atmSystem.md) | 🟢 new | Actor page, split out of the Actor Descriptions |
| [Bank Backend](../use_case/actors/bankBackend.md) | 🟢 new | Actor page, split out of the Actor Descriptions |
| [Use Case – Authenticate (Card & PIN)](../use_case/authenticate/authenticate.md) | 🟡 changed | Business Process traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags` |
| [Use Case – Withdraw Cash](../use_case/withdraw_cash/withdrawCash.md) | 🟡 changed | Business Process traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags` |
| [Use Case – Check Balance](../use_case/check_balance/checkBalance.md) | 🟡 changed | Business Process traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags` |
| [Use Case – Transfer Funds](../use_case/transfer_funds/transferFunds.md) | 🟡 changed | Business Process traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags` |
| [Use Case – Print Receipt](../use_case/print_receipt/printReceipt.md) | 🟡 changed | Business Process traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags` |
| [State Chart – Transaction](../state_chart/transactionStateChart.md) | 🟡 changed | Transaction link points at the Transaction entity page; frontmatter adds `sources`, `generated` and `tags` |
| [Epics & Story Map – ATM System](../epics/epics.md) | 🟡 changed | Frontmatter adds `sources`, `generated` and `tags` |
| [US-1.1 – Insert Card and Validate](../epics/user_stories/us_1_1.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-1.2 – Enter PIN and Create Session](../epics/user_stories/us_1_2.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-1.3 – Retry PIN on Invalid Entry](../epics/user_stories/us_1_3.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-1.4 – Block Card After Failed PIN Attempts](../epics/user_stories/us_1_4.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-2.1 – Enter Amount and Receive Cash](../epics/user_stories/us_2_1.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-2.2 – Enforce Account Daily Limit](../epics/user_stories/us_2_2.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-2.3 – Verify Sufficient Account Balance](../epics/user_stories/us_2_3.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-2.4 – Check CashDispenser Availability](../epics/user_stories/us_2_4.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-2.5 – Handle Cash Dispensing Failure](../epics/user_stories/us_2_5.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-2.6 – Eject Card Before Cash Dispensing](../epics/user_stories/us_2_6.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-3.1 – View Account Balance](../epics/user_stories/us_3_1.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-4.1 – Select Target Account and Transfer Funds](../epics/user_stories/us_4_1.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-4.2 – Handle Transfer Processing Error](../epics/user_stories/us_4_2.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-5.1 – Print Receipt After Transaction](../epics/user_stories/us_5_1.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-5.2 – Decline Receipt Printing](../epics/user_stories/us_5_2.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [US-5.3 – Show Account Balance on Receipt](../epics/user_stories/us_5_3.md) | 🟡 changed | Activity diagram traceability reference cited with a footnote; frontmatter adds `sources`, `generated` and `tags`, including release and KANO tags |
| [Change Log – ATM System](../change_log/changeLog.md) | 🟡 changed | This entry; frontmatter adds `sources` and `generated` |
| [Log](../log.md) | 🟢 new | Every version, newest first, in Open Knowledge Format — generated from this change log |
| [Home](../_index.md) | 🟡 changed | Artifacts list links the entity pages, the actor pages, the sources and the log |
| [CR-1.3](../sources/cr_1_3.md) | 🟢 new | The change request for this version |

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
