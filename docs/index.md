# ATM System Documentation

Welcome to the documentation for the **ATM example system**.

## Artifacts

- [**Domain Model**](domain_model/domainModel.md) — Core business entities and their relationships
- [**Business Process**](business_process/businessProcess.md) — End-to-end ATM interaction flow with embedded diagram
- [**Use-Case Diagram**](use_case/useCaseDiagram.md) — Actor–system interactions derived from the business process
  - [Actor Descriptions](use_case/actorDescriptions.md) — Detailed actor profiles and system access
  - [Authenticate](use_case/authenticate/authenticate.md) — Card & PIN authentication flow
  - [Withdraw Cash](use_case/withdraw_cash/withdrawCash.md) — Cash withdrawal flow
  - [Check Balance](use_case/check_balance/checkBalance.md) — Balance inquiry flow
  - [Transfer Funds](use_case/transfer_funds/transferFunds.md) — Fund transfer flow
  - [Print Receipt](use_case/print_receipt/printReceipt.md) — Optional receipt printing
- [**State Charts**](state_chart/transactionStateChart.md) — Entity lifecycle diagrams traced to use case activities
  - [Transaction](state_chart/transactionStateChart.md) — PENDING → COMPLETED / FAILED lifecycle
- [**Epics & Story Map**](epics/epics.md) — Work breakdown into epics with release-grouped user stories
  - [User Stories](epics/user_stories/us_1_1.md) — 14 stories in 3C format across 3 releases
- [**Change Log**](change_log/changeLog.md) — Version history with full artifact traceability