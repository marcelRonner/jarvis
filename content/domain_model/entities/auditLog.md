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
  at: 2026-09-12T21:29:07Z
verified:
  - by: human:owner
    at: 2026-09-13T09:23:45Z
---

# AuditLog

> [!NOTE] v1.3 – Added 2026-09-12
> AuditLog has its own page, split out of the [Domain Model](../domainModel.md).

Represents a record of system events for security and compliance purposes. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| logId           | String   | Unique log entry identifier         |
| eventType       | String   | Type of event logged                |
| timestamp       | DateTime | When the event occurred             |
| detail          | String   | Descriptive detail of the event     |
