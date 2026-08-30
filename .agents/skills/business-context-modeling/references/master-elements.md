# Master element maps

Master maps are the canonical semantic layer for the three non-activity element
types that recur across business context views:

| Master view | Nodes | Main question |
| --- | --- | --- |
| Actor map | `a_` | Who provides, receives, owns, or is related to value? |
| External-system map | `x_` | Which systems cooperate, integrate, or depend on one another? |
| Information model | `i_` | Which business objects are associated, derived, or held together? |

They are maps, not process diagrams. A master map may connect nodes of the same
type. A business context remains business-centered: every foundation-context
edge still joins one `b_` activity and one non-business element.

## Canonical identity

- Give each element a stable `prefix_lower_snake_case` ID. The ID is the
  identity; a visible label may be refined without silently creating a second
  element.
- Keep the canonical label, icon URL, size, and class in the master map.
- Reuse the exact ID and node definition when a context view selects an
  element. Do not create a synonym only because the local diagram has a
  different wording.
- Keep aliases, source wording, confidence, and unresolved classification in
  the Markdown companion, not in the Mermaid node label.
- If two names represent different abstraction levels, states, owners, or
  responsibilities, assign distinct IDs and explain the distinction.

Mermaid has no native import for another Markdown diagram. “Reference” means
copying the canonical node identity and recording the link explicitly:

```markdown
## Master references

| Master | ID | Canonical label | Use in this view |
| --- | --- | --- | --- |
| `actor-master.md` | `a_customer` | Customer | receives the outcome |
| `information-master.md` | `i_repair_request` | Repair request | input |
```

Keep one selected ID per row. The reference checker verifies that every
selected `a_`, `x_`, or `i_` node has a row, that the master path and canonical
label match the supplied map, and that no unselected ID is smuggled into the
trace table. The path is resolved from the context file; a same-named file in a
different directory is not an equivalent master.

The model-set index is a navigation and trace aid, not a second semantic
registry. The Mermaid node in the master remains the source for its canonical
identity.

## Relationship semantics

Use unlabelled lines so the diagrams remain quick to edit and redraw by hand.
State the meaning in the `Reading` sentence below the diagram.

| Master | `---` means | `-->` means | Do not imply |
| --- | --- | --- | --- |
| Actor | peer, affiliation, or association | parent-to-child, accountability, or ownership | a work sequence |
| External system | related or cooperating systems | integration or dependency direction | a business activity |
| Information | conceptual association | derivation, containment, or another explicitly directional relation | a detailed data schema |

The directed edge in a master map is a structural relation, not the value-flow
or process arrow used by a context or flow view. Use it only when direction
changes the discussion. Keep relationship labels out of the icon diagram; put
cardinality, evidence, and uncertainty in companion prose or a small table.

## Master-first loop

1. Extract the user's actual nouns and verbs from conversation or source
   material. Keep candidates and source wording before normalizing labels.
2. Reconcile each actor, system, and information candidate with the existing
   master maps: reuse, add, merge only with evidence, or mark unresolved.
3. Update the affected master map before composing a context view when the
   candidate set or same-type relationships are part of the question.
4. Build the business context by selecting master IDs around one `b_` activity.
   Copy the canonical node lines and add a `## Master references` table.
5. If the context reveals a missing or incorrect same-type relationship, move
   back up and revise the master. If it reveals a meaningful distinction,
   create a focused child view and trace it back to the master ID.
6. Record master views alongside overview, observation, focused context, and
   flow views in the model-set index.

Do not force a master node merely because a familiar role, product, or data
object is common elsewhere. Keep `unresolved` candidates visible until the
boundary and responsibility are clear.

## Master map checks

- One master file contains one kind only: actors, external systems, or
  information.
- Do not place `b_` activities in a master map.
- Use the same thin Lucide profile as the public context convention:
  `a_` uses `user.svg` at `38 x 38`, `x_` uses `server.svg` at `32 x 32`, and
  `i_` uses `file.svg` at `32 x 32`.
- Keep one short reading sentence, fixed-size icon nodes, and ordinary
  `---` lines unless a structural direction is material.
- A map may be larger than seven nodes when that density is intentional. Run
  the checker with `--allow-complexity` and preserve the observation rather
  than deleting candidates to fit the canvas.
- If several candidates are known but their same-type relationship is not yet
  evidenced, keep them as disconnected nodes and run the checker with
  `--allow-sparse`. Do not invent an edge merely to satisfy a visual or lint
  requirement. Record the missing evidence in the reading sentence or an
  unresolved question. `--allow-sparse` and `--allow-complexity` can be used
  together.

Use the companion checker with the matching kind:

```bash
python3 .agents/skills/business-context-modeling/scripts/check_master_map.py \
  path/to/actor-master.md --kind actor --strict
python3 .agents/skills/business-context-modeling/scripts/check_master_map.py \
  path/to/system-master.md --kind system --strict
python3 .agents/skills/business-context-modeling/scripts/check_master_map.py \
  path/to/information-master.md --kind information --strict

# Verify that selected context nodes still match the canonical masters.
python3 .agents/skills/business-context-modeling/scripts/check_master_references.py \
  path/to/context.md \
  --actor path/to/actor-master.md \
  --system path/to/system-master.md \
  --information path/to/information-master.md

# If a selected master intentionally contains disconnected candidates:
python3 .agents/skills/business-context-modeling/scripts/check_master_references.py \
  path/to/context.md --actor path/to/actor-master.md --allow-sparse
```
