# Business Process – ATM Cash Withdrawal & Services

## Overview

This business process describes the end-to-end flow of a customer interacting with an ATM, from card insertion and authentication through transaction execution (withdrawal, balance inquiry, or transfer) to session completion. It references the entities defined in the [Domain Model](../domain_model/domainModel.md).

---

## Process Diagram

**Legend:** 🟦 Customer &nbsp; 🟨 ATM System &nbsp; 🟩 Bank Backend &nbsp; 🟥 Decision

```mermaid
flowchart TD
    classDef customer fill:#DBEAFE,stroke:#2563EB,color:#1E3A5F
    classDef atm fill:#FEF9C3,stroke:#CA8A04,color:#713F12
    classDef bank fill:#DCFCE7,stroke:#16A34A,color:#14532D
    classDef decision fill:#FEE2E2,stroke:#DC2626,color:#7F1D1D

    Start(("Start")) --> InsertCard["1.1 Insert Card into ATM"]:::customer
    InsertCard --> ReadCard["1.2 Read Card data"]:::atm
    ReadCard --> ValidateCard{"1.3 Card valid\nand not blocked?"}:::decision

    ValidateCard -->|No| RetainCard["1.4 Retain Card\nDisplay error"]:::atm
    RetainCard --> EndFail(("End"))

    ValidateCard -->|Yes| EnterPIN["2.1 Enter PIN"]:::customer
    EnterPIN --> AuthPIN["2.2 Validate PIN\nagainst Bank records"]:::bank

    AuthPIN -->|Invalid| AttemptsLeft{"2.3 Attempts\nremaining?"}:::decision
    AttemptsLeft -->|Yes| EnterPIN
    AttemptsLeft -->|No| BlockCard["2.4 Block Card\nRetain Card"]:::atm
    BlockCard --> EndFail

    AuthPIN -->|Valid| CreateSession["3.1 Create Session"]:::atm
    CreateSession --> SelectAction{"3.2 Select\ntransaction type"}:::customer

    SelectAction -->|Withdrawal| EnterAmount["4a.1 Enter\nwithdrawal amount"]:::customer
    SelectAction -->|Balance Inquiry| ShowBalance["4b.1 Retrieve balance\nDisplay on screen"]:::atm
    SelectAction -->|Transfer| SelectTarget["4c.1 Select\ntarget Account"]:::customer

    EnterAmount --> CheckLimit{"4a.2 Amount within\ndaily limit?"}:::decision
    CheckLimit -->|No| EnterAmount
    CheckLimit -->|Yes| CheckFunds{"4a.3 Sufficient\nbalance?"}:::decision
    CheckFunds -->|No| InsufficientFunds["4a.3a Display\ninsufficient funds"]:::atm
    InsufficientFunds --> SelectAction

    CheckFunds -->|Yes| CheckCash{"4a.4 CashDispenser\nhas sufficient cash?"}:::decision
    CheckCash -->|No| NoCash["4a.4a Display ATM\nout of cash"]:::atm
    NoCash --> SelectAction

    CheckCash -->|Yes| CreateTx["4a.5 Create Transaction\nDebit Account"]:::bank
    CreateTx --> EjectCardW["4a.6 Eject Card"]:::atm
    EjectCardW --> DispenseCash["4a.7 Dispense cash\nUpdate CashCassettes"]:::atm
    DispenseCash --> LogTx["5.1 Write AuditLog entry"]:::bank

    ShowBalance --> LogTx

    SelectTarget --> EnterTransferAmt["4c.2 Enter\ntransfer amount"]:::customer
    EnterTransferAmt --> ExecuteTransfer["4c.3 Create Transaction\nDebit source, credit target"]:::bank
    ExecuteTransfer --> LogTx

    LogTx --> ReceiptChoice{"5.2 Print Receipt?"}:::customer
    ReceiptChoice -->|Yes| PrintReceipt["5.3 Generate and\nprint Receipt"]:::atm
    PrintReceipt --> AnotherTx{"5.4 Another\ntransaction?"}:::customer
    ReceiptChoice -->|No| AnotherTx

    AnotherTx -->|Yes| SelectAction
    AnotherTx -->|No| EndSession["5.5 Close Session\nEject Card if not\nalready ejected"]:::atm
    EndSession --> EndOK(("End"))
```
