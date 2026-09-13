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
  at: 2026-09-13T09:54:02Z
verified:
  - by: human:owner
    at: 2026-09-13T09:23:45Z
---

# CashCassette

Represents a single cassette holding banknotes of a specific denomination. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| cassetteId      | String   | Unique cassette identifier          |
| denomination    | Decimal  | Banknote value (e.g. 10, 20, 100)  |
| quantity        | Integer  | Number of banknotes in the cassette |
