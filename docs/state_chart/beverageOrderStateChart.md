# State Chart – BeverageOrder

## Overview

This state chart describes the lifecycle of the `BeverageOrder` entity defined in the [Domain Model](../domain_model/domainModel.md). State transitions are backed by activities in the [Order Coffee use case](../use_case/order_coffee/orderCoffee.md). The [Use-Case Diagram](../use_case/useCaseDiagram.md) provides the full functional context.

---

## Diagram

![State Chart – BeverageOrder](../assets/img/beverageOrderStateChart.svg)

---

## States

| State | Description |
|-------|-------------|
| `PENDING` | The `BeverageOrder` has been created; dispensing is in progress. |
| `COMPLETED` | The Espresso was successfully dispensed. |
| `FAILED` | The `CoffeeMachine` was unavailable; nothing was dispensed. |

---

## Transition Traceability

| Transition | Trigger Activity | Use Case | Activity Diagram Step |
|------------|-----------------|----------|-----------------------|
| `[*] → PENDING` | "ATM creates BeverageOrder (status = PENDING)" | [Order Coffee](../use_case/order_coffee/orderCoffee.md) | `:ATM creates BeverageOrder\n(status = PENDING);` |
| `PENDING → COMPLETED` | "ATM updates BeverageOrder (status = COMPLETED)" | [Order Coffee](../use_case/order_coffee/orderCoffee.md) | `:ATM updates BeverageOrder\n(status = COMPLETED);` |
| `PENDING → FAILED` | "ATM updates BeverageOrder (status = FAILED)" | [Order Coffee](../use_case/order_coffee/orderCoffee.md) | `:ATM updates BeverageOrder\n(status = FAILED);` |

---

## States Not Covered

None. All three `BeverageOrder` states are backed by activities in the Order Coffee use case activity diagram.
