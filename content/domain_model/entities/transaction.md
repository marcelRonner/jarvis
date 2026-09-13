---
title: "Transaction"
type: entity
description: "Represents a financial operation performed during a session."
weight: 7
tags: [transaction]
sources:
  - id: domain-model
    resource: /domain_model/domainModel.md
  - id: cr-1-3
    resource: /sources/cr_1_3.md
generated:
  by: jarvis/1.0
  at: 2026-09-12T21:29:07Z
verified:
  - by: human:owner
    at: 2026-09-13T09:23:45Z
---

# Transaction

> [!NOTE] v1.3 – Added 2026-09-12
> Transaction has its own page, split out of the [Domain Model](../domainModel.md).

Represents a financial operation performed during a session. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute        | Type     | Description                          |
|------------------|----------|--------------------------------------|
| transactionId    | String   | Unique transaction identifier       |
| transactionType  | Enum     | WITHDRAWAL, DEPOSIT, TRANSFER, BALANCE_INQUIRY |
| amount           | Decimal  | Transaction amount                  |
| currency         | String   | Currency code                       |
| timestamp        | DateTime | When the transaction was executed   |
| status           | Enum     | PENDING, COMPLETED, FAILED, REVERSED|
