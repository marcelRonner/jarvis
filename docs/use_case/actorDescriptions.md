# Actor Descriptions – ATM System

## Overview

This page provides a detailed description and system access profile for every actor that appears in the [Use-Case Diagram](useCaseDiagram.md) and the [Business Process](../business_process/businessProcess.md).

---

## Actors

| Actor | Type | Description | System Access |
|-------|------|-------------|---------------|
| **Customer** | Primary | A bank customer who holds one or more Account at a Bank and possesses a physical Card. The Customer initiates every ATM interaction by inserting a Card and authenticating with a PIN. Corresponds to 🟦 Customer in the Business Process. | Physical access to the ATM terminal (card slot, keypad, screen, cash tray, receipt slot). No direct access to the Bank Backend or any internal system component. All actions are mediated through the ATM user interface. |
| **ATM System** | System | The ATM hardware and software that mediates between the Customer and the Bank Backend. It reads Card data, manages Session lifecycle, drives the CashDispenser and CashCassette, prints Receipt, and enforces local validations. Corresponds to 🟨 ATM System in the Business Process. | Full control over local peripherals (card reader, keypad, screen, CashDispenser, receipt printer). Authenticated network connection to the Bank Backend API. Read/write access to Session and local AuditLog. No direct access to Account or Transaction records — all financial operations are delegated to the Bank Backend. |
| **Bank Backend** | Supporting | The centralised banking system operated by the Bank. It validates Card and PIN credentials, authorises and processes Transaction (withdrawal, transfer, balance inquiry), manages Account balances, and writes AuditLog entries. Corresponds to 🟩 Bank Backend in the Business Process. | Full read/write access to Account, Transaction, Card, and AuditLog records. Receives requests exclusively from authenticated ATM System connections. No direct interaction with the Customer. |
