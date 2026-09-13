---
title: "ATM"
type: entity
description: "Represents a physical ATM terminal deployed at a specific location."
weight: 1
tags: [atm]
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

# ATM

Represents a physical ATM terminal deployed at a specific location. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| atmId           | String   | Unique identifier of the ATM        |
| location        | String   | Physical address of the ATM         |
| status          | Enum     | ONLINE, OFFLINE, OUT_OF_SERVICE     |
