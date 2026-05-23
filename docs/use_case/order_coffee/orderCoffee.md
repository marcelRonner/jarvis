# Use Case – Order Coffee

## Overview

This use case describes how a Customer requests and receives a complimentary Espresso from the ATM's CoffeeMachine during an active Session. It is derived from the [Use-Case Diagram](../useCaseDiagram.md) and corresponds to **Business Process steps 4d.1 – 4d.3**. The [Business Process](../../business_process/businessProcess.md) provides the end-to-end context.

---

## Preconditions

- A `Session` with `status = ACTIVE` exists for the authenticated Customer.
- The `ATM` has a connected `CoffeeMachine`.

---

## Postconditions

**Success**

- A `BeverageOrder` with `beverageType = ESPRESSO` and `status = COMPLETED` is created and linked to the `Session`.
- The `CoffeeMachine` decrements its `beansRemaining` count by 1.
- An `AuditLog` entry is written for the dispensing event.

**Failure – CoffeeMachine unavailable**

- No `BeverageOrder` is created.
- The ATM displays an "out of service" message and returns the Customer to the transaction selection screen.

---

## Description

After successful authentication the Customer selects "Coffee" from the transaction menu. The ATM checks the `CoffeeMachine` status. If the machine is `ONLINE` and `beansRemaining > 0`, the ATM creates a `BeverageOrder` (status `PENDING`), instructs the `CoffeeMachine` to dispense an Espresso, and on completion updates the `BeverageOrder` to `COMPLETED`. An `AuditLog` entry is written. If the `CoffeeMachine` is `OFFLINE` or `OUT_OF_STOCK`, no order is created and the Customer is informed.

Corresponds to **Business Process steps 4d.1 – 4d.3**.

---

## Activity Diagram

![Activity Diagram – Order Coffee](../../assets/img/orderCoffee.svg)
