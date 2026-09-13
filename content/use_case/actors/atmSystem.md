---
title: "ATM System"
type: actor
description: "The ATM hardware and software that mediates between the Customer and the Bank Backend."
weight: 2
tags: [atm, bank, customer, account, card, session, transaction, receipt, cash-dispenser, cash-cassette, audit-log]
sources:
  - id: business-process
    resource: /business_process/businessProcess.md
  - id: cr-1-3
    resource: /sources/cr_1_3.md
generated:
  by: jarvis/1.0
  at: 2026-09-12T21:29:07Z
---

# ATM System

> [!NOTE] v1.3 – Added 2026-09-12
> ATM System has its own page, split out of the [Actor Descriptions](../actorDescriptions.md).

**Type:** System

## Description

The ATM hardware and software that mediates between the Customer and the Bank Backend. It reads Card data, manages Session lifecycle, drives the CashDispenser and CashCassette, prints Receipt, and enforces local validations. Corresponds to 🟨 ATM System in the Business Process.

## System Access

Full control over local peripherals (card reader, keypad, screen, CashDispenser, receipt printer). Authenticated network connection to the Bank Backend API. Read/write access to Session and local AuditLog. No direct access to Account or Transaction records — all financial operations are delegated to the Bank Backend.
