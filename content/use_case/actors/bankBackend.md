---
title: "Bank Backend"
type: actor
description: "The centralised banking system operated by the Bank."
weight: 3
tags: [bank, customer, account, card, transaction, audit-log]
sources:
  - id: business-process
    resource: /business_process/businessProcess.md
  - id: cr-1-3
    resource: /sources/cr_1_3.md
generated:
  by: jarvis/1.0
  at: 2026-09-12T21:29:07Z
---

# Bank Backend

> [!NOTE] v1.3 – Added 2026-09-12
> Bank Backend has its own page, split out of the [Actor Descriptions](../actorDescriptions.md).

**Type:** Supporting

## Description

The centralised banking system operated by the Bank. It validates Card and PIN credentials, authorises and processes Transaction (withdrawal, transfer, balance inquiry), manages Account balances, and writes AuditLog entries. Corresponds to 🟩 Bank Backend in the Business Process.

## System Access

Full read/write access to Account, Transaction, Card, and AuditLog records. Receives requests exclusively from authenticated ATM System connections. No direct interaction with the Customer.
