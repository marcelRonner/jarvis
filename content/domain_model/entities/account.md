---
title: "Account"
type: entity
description: "Represents a bank account owned by a customer."
weight: 4
tags: [account]
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

# Account

> [!NOTE] v1.3 – Added 2026-09-12
> Account has its own page, split out of the [Domain Model](../domainModel.md).

Represents a bank account owned by a customer. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| accountNumber   | String   | Unique account number               |
| accountType     | Enum     | CHECKING, SAVINGS                   |
| balance         | Decimal  | Current account balance             |
| currency        | String   | Currency code (e.g. CHF, EUR)       |
| dailyLimit      | Decimal  | Maximum daily withdrawal amount     |
