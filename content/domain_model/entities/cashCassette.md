---
title: "CashCassette"
type: entity
description: "Represents a single cassette holding banknotes of a specific denomination."
weight: 10
tags: [cash-cassette]
sources:
  - id: domain-model
    resource: /domain_model/domainModel.md
  - id: cr-1-3
    resource: /sources/cr_1_3.md
generated:
  by: jarvis/1.0
  at: 2026-09-12T21:29:07Z
---

# CashCassette

> [!NOTE] v1.3 – Added 2026-09-12
> CashCassette has its own page, split out of the [Domain Model](../domainModel.md).

Represents a single cassette holding banknotes of a specific denomination. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| cassetteId      | String   | Unique cassette identifier          |
| denomination    | Decimal  | Banknote value (e.g. 10, 20, 100)  |
| quantity        | Integer  | Number of banknotes in the cassette |
