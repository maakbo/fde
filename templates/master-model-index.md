# Master model index

The three master diagrams are the canonical semantic layer. This file is only
the navigation and trace surface that connects them to business context views.

## Master views

| Master | Role | Canonical prefix | Source |
| --- | --- | --- | --- |
| Actor map | value participants, hierarchy, and peer relations | `a_` | [actor master](master-actor-map.md) |
| External-system map | integrations and system dependencies | `x_` | [system master](master-system-map.md) |
| Information model | conceptual information relationships | `i_` | [information master](master-information-model.md) |

## Context references

For every context view, record the selected master IDs and copy their canonical
node definitions. Mermaid does not import another diagram automatically.
The model-set may have an overall context and several use-case contexts; record
the exact IDs selected by each context, not only the first diagram in the set.

| Context view | Master | Selected IDs | Why selected |
| --- | --- | --- | --- |
| `context.md` | `master-actor-map.md` | `a_customer` | participant in the activity |
| `context.md` | `master-information-model.md` | `i_request` | input information |

## Reconciliation notes

Record new candidates, aliases, conflicts, and unresolved classifications here
only as a trace. The master Mermaid nodes remain the canonical identity.

- New or changed actor IDs:
- New or changed external-system IDs:
- New or changed information IDs:
- Context views that need to be revisited:
