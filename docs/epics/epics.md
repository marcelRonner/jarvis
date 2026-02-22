# Epics & Story Map – ATM System

## Overview

This page lists all epics required to build the ATM system. Each epic realises exactly one [Use Case](../use_case/useCaseDiagram.md) and uses the terminology defined in the [Domain Model](../domain_model/domainModel.md). User stories are grouped into horizontal release slices to form a **story map**: each row is a deliverable release, each column is an epic. Individual story details are in the [user_stories/](user_stories/) subfolder.

**KANO legend:** MUST / NEEDS = Basic quality · WANTS = Performance quality · WOULD LIKE = Attractive quality

---

## Story Map

| | Epic 1: Authenticate Card & PIN | Epic 2: Withdraw Cash | Epic 3: Check Balance | Epic 4: Transfer Funds | Epic 5: Print Receipt |
|---|---|---|---|---|---|
| **Use Case** | [Authenticate](../use_case/authenticate/authenticate.md) | [Withdraw Cash](../use_case/withdraw_cash/withdrawCash.md) | [Check Balance](../use_case/check_balance/checkBalance.md) | [Transfer Funds](../use_case/transfer_funds/transferFunds.md) | [Print Receipt](../use_case/print_receipt/printReceipt.md) |
| **Goal** | Validate Card and PIN so the ATM can create a Session | Dispense cash from the CashDispenser and debit the Customer Account | Retrieve and display the current Account balance | Debit the source Account and credit a target Account | Generate and print a Receipt for a completed Transaction |
| **Key Entity** | Card, Session | Transaction, Account, CashDispenser, CashCassette | Transaction, Account | Transaction, Account | Receipt, Transaction |
| **Actor** | Customer, Bank Backend | Customer, Bank Backend | Customer, Bank Backend | Customer, Bank Backend | Customer |
| **BP Steps** | 1.1 – 3.1 | 4a.1 – 4a.7 | 4b.1 | 4c.1 – 4c.3 | 5.2 – 5.3 |
| | | | | | |
| **R1 – Walking Skeleton** | [US-1.1](user_stories/us_1_1.md) Insert Card and Validate | [US-2.1](user_stories/us_2_1.md) Enter Amount and Receive Cash | [US-3.1](user_stories/us_3_1.md) View Account Balance | | |
| | | [US-2.6](user_stories/us_2_6.md) Eject Card Before Cash | | | |
| | [US-1.2](user_stories/us_1_2.md) Enter PIN and Create Session | | | | |
| **R2 – Core Transactions** | [US-1.3](user_stories/us_1_3.md) Retry PIN on Invalid Entry | [US-2.2](user_stories/us_2_2.md) Enforce Account Daily Limit | | [US-4.1](user_stories/us_4_1.md) Select Target Account and Transfer Funds | [US-5.1](user_stories/us_5_1.md) Print Receipt After Transaction |
| | | [US-2.3](user_stories/us_2_3.md) Verify Sufficient Account Balance | | | |
| **R3 – Robustness & Security** | [US-1.4](user_stories/us_1_4.md) Block Card After Failed PIN Attempts | [US-2.4](user_stories/us_2_4.md) Check CashDispenser Availability | | [US-4.2](user_stories/us_4_2.md) Handle Transfer Processing Error | [US-5.2](user_stories/us_5_2.md) Decline Receipt Printing |
| | | [US-2.5](user_stories/us_2_5.md) Handle Cash Dispensing Failure | | | |
