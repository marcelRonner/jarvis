---
title: "Bank"
type: entity
description: "Represents a financial institution that owns or operates ATMs and manages customer accounts."
weight: 2
tags: [bank]
sources:
  - id: domain-model
    resource: /domain_model/domainModel.md
  - id: cr-1-3
    resource: /sources/cr_1_3.md
generated:
  by: jarvis/1.0
  at: 2026-09-12T21:29:07Z
---

# Bank

> [!NOTE] v1.3 – Added 2026-09-12
> Bank has its own page, split out of the [Domain Model](../domainModel.md).

Represents a financial institution that owns or operates ATMs and manages customer accounts. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| bankCode        | String   | Unique bank identification code     |
| name            | String   | Name of the bank                    |
| swiftCode       | String   | SWIFT/BIC code for interbank comm.  |
