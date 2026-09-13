---
title: "Card"
type: entity
description: "Represents a physical debit or credit card linked to an account."
weight: 5
tags: [card]
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
  - by: human:owner
    at: 2026-09-13T10:11:37Z
---

# Card

Represents a physical debit or credit card linked to an account. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| cardNumber      | String   | Unique card number                  |
| cardType        | Enum     | DEBIT, CREDIT                       |
| expirationDate  | Date     | Card expiry date                    |
| pin             | String   | Encrypted PIN                       |
| isBlocked       | Boolean  | Whether the card is blocked         |
