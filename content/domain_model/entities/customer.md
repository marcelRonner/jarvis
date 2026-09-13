---
title: "Customer"
type: entity
description: "Represents an individual who holds one or more accounts at a bank."
weight: 3
tags: [customer]
sources:
  - id: domain-model
    resource: /domain_model/domainModel.md
  - id: cr-1-3
    resource: /sources/cr_1_3.md
generated:
  by: jarvis/1.0
  at: 2026-09-12T21:29:07Z
---

# Customer

> [!NOTE] v1.3 – Added 2026-09-12
> Customer has its own page, split out of the [Domain Model](../domainModel.md).

Represents an individual who holds one or more accounts at a bank. Part of the [Domain Model](../domainModel.md).

## Attributes

| Attribute       | Type     | Description                          |
|-----------------|----------|--------------------------------------|
| customerId      | String   | Unique identifier of the customer   |
| firstName       | String   | First name                          |
| lastName        | String   | Last name                           |
| dateOfBirth     | Date     | Date of birth                       |
