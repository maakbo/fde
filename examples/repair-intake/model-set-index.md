# Repair service model set

## Purpose

Connect the repair-intake boundary discussion to the wider repair service without flattening capability, activity, and task details into one diagram.

## View map

| View | Role | Level | Parent / expanded node | Child views | Focus | Status |
| --- | --- | --- | --- | --- | --- | --- |
| [overview](overview.mmd) | overview flow | capability / business area | — | [context](context.mmd) | High-level handoff from intake to repair and return | working hypothesis |
| [context](context.mmd) | focused context | business activity | `overview.mmd / b_manage_intake` | [flow](flow.mmd) | Actors, information, and outside service around intake | working hypothesis |
| [flow](flow.mmd) | focused flow | task | `context.mmd / b_receive_request` | — | Completeness decision and missing-detail rework | working hypothesis |

## Abstract to concrete

- `b_manage_intake` expands into the customer, repair request, intake record, scheduling service, and `b_receive_request` activity.
- `b_receive_request` expands into receiving, checking completeness, requesting details, and booking.

## Concrete to abstract

- The intake details group under `b_manage_intake` because they share the outcome of producing a repair request ready for execution.
- If the detail shows that booking allocates repair capacity rather than merely completing intake, revise the overview boundary between `b_manage_intake` and `b_repair_item`.

## Open modeling question

Does booking complete intake, or begin repair execution?
