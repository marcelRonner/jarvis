---
title: "AuditLog"
type: entity
description: "Represents a record of system events for security and compliance purposes."
weight: 11
tags: [audit-log]
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

# AuditLog

Represents a record of system events for security and compliance purposes. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| logId           | String   | Unique log entry identifier         |
| eventType       | String   | Type of event logged                |
| timestamp       | DateTime | When the event occurred             |
| detail          | String   | Descriptive detail of the event     |
