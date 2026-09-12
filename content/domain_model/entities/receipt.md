---
title: "Receipt"
type: entity
description: "Represents a printed or digital receipt issued after a transaction."
weight: 8
tags: [receipt]
sources:
  - id: domain-model
    resource: /domain_model/domainModel.md
  - id: cr-1-3
    resource: /sources/cr_1_3.md
generated:
  by: jarvis/1.0
  at: 2026-09-12T21:29:07Z
---

# Receipt

> [!NOTE] v1.3 – Added 2026-09-12
> Receipt has its own page, split out of the [Domain Model](../domainModel.md).

Represents a printed or digital receipt issued after a transaction. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| receiptId       | String   | Unique receipt identifier           |
| printedAt       | DateTime | When the receipt was generated      |
| content         | String   | Formatted receipt text              |
