---
title: "Domain Model – ATM System"
linkTitle: "Domain Model"
type: domain-model
description: "The domain model of the ATM system at a glance: its class diagram, and a link to each business entity."
weight: 1
tags: [atm, bank, customer, account, card, session, transaction, receipt, cash-dispenser, cash-cassette, audit-log]
sources:
  - id: cr-1-3
    resource: /sources/cr_1_3.md
generated:
  by: jarvis/1.0
  at: 2026-09-13T09:54:02Z
verified:
  - by: human:owner
    at: 2026-09-13T09:23:45Z
  - by: human:owner
    at: 2026-09-13T10:11:37Z
---

# Domain Model – ATM System

## Overview

This domain model describes the core business entities and their relationships for an IT system that realizes an Automated Teller Machine (ATM).

---

## Class Diagram

![Domain Model – ATM System](domainModel.puml)

---

## Classes

- [ATM](entities/atm.md)
- [Bank](entities/bank.md)
- [Customer](entities/customer.md)
- [Account](entities/account.md)
- [Card](entities/card.md)
- [Session](entities/session.md)
- [Transaction](entities/transaction.md)
- [Receipt](entities/receipt.md)
- [CashDispenser](entities/cashDispenser.md)
- [CashCassette](entities/cashCassette.md)
- [AuditLog](entities/auditLog.md)
