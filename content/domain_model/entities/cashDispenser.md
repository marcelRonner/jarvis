---
title: "CashDispenser"
type: entity
description: "Represents the cash-dispensing hardware unit inside an ATM."
weight: 9
tags: [cash-dispenser, atm]
sources:
  - id: domain-model
    resource: /domain_model/domainModel.md
  - id: cr-1-3
    resource: /sources/cr_1_3.md
generated:
  by: jarvis/1.0
  at: 2026-09-12T21:29:07Z
---

# CashDispenser

> [!NOTE] v1.3 – Added 2026-09-12
> CashDispenser has its own page, split out of the [Domain Model](../domainModel.md).

Represents the cash-dispensing hardware unit inside an ATM. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute          | Type     | Description                          |
|--------------------|----------|--------------------------------------|
| dispenserId        | String   | Unique dispenser identifier         |
| totalCashAvailable | Decimal  | Total cash remaining in the unit    |
| lastRefillDate     | DateTime | Date of last cash refill            |
