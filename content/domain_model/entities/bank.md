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
  at: 2026-09-13T09:54:02Z
verified:
  - by: human:owner
    at: 2026-09-13T09:23:45Z
---

# Bank

Represents a financial institution that owns or operates ATMs and manages customer accounts. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| bankCode        | String   | Unique bank identification code     |
| name            | String   | Name of the bank                    |
| swiftCode       | String   | SWIFT/BIC code for interbank comm.  |
