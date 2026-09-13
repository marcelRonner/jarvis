---
title: "Session"
type: entity
description: "Represents an active interaction between a customer and an ATM."
weight: 6
tags: [session, atm]
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

# Session

> [!NOTE] v1.3 – Added 2026-09-12
> Session has its own page, split out of the [Domain Model](../domainModel.md).

Represents an active interaction between a customer and an ATM. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| sessionId       | String   | Unique session identifier           |
| startTime       | DateTime | When the session started            |
| endTime         | DateTime | When the session ended              |
| status          | Enum     | ACTIVE, COMPLETED, TIMED_OUT        |
