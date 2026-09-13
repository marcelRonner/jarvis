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
  at: 2026-09-13T09:54:02Z
verified:
  - by: human:owner
    at: 2026-09-13T09:23:45Z
---

# Account

Represents a bank account owned by a customer. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| accountNumber   | String   | Unique account number               |
| accountType     | Enum     | CHECKING, SAVINGS                   |
| balance         | Decimal  | Current account balance             |
| currency        | String   | Currency code (e.g. CHF, EUR)       |
| dailyLimit      | Decimal  | Maximum daily withdrawal amount     |
