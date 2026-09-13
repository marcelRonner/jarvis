---
title: "Customer"
type: actor
description: "A bank customer who holds one or more Account at a Bank and possesses a physical Card."
weight: 1
tags: [atm, bank, customer, account, card]
sources:
  - id: business-process
    resource: /business_process/businessProcess.md
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

# Customer

**Type:** Primary

## Description

A bank customer who holds one or more Account at a Bank and possesses a physical Card. The Customer initiates every ATM interaction by inserting a Card and authenticating with a PIN. Corresponds to 🟦 Customer in the Business Process.

## System Access

Physical access to the ATM terminal (card slot, keypad, screen, cash tray, receipt slot). No direct access to the Bank Backend or any internal system component. All actions are mediated through the ATM user interface.
