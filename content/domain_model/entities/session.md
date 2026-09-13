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
  at: 2026-09-13T09:54:02Z
verified:
  - by: human:owner
    at: 2026-09-13T09:23:45Z
---

# Session

Represents an active interaction between a customer and an ATM. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| sessionId       | String   | Unique session identifier           |
| startTime       | DateTime | When the session started            |
| endTime         | DateTime | When the session ended              |
| status          | Enum     | ACTIVE, COMPLETED, TIMED_OUT        |
