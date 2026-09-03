# Multi-view business modeling

Use a model set when one diagram can no longer answer every useful question at
one abstraction level, or when the complexity itself is worth observing.

## Model and View

A **Model** is the maintained meaning: purpose, desired outcomes, Business
activities, participants, Information, systems, flows, implementation choices,
and their relationships. It may include prose, inventories, decisions, and
uncertainty in the authoring workspace.

A **View** selects only the part needed to answer one reader question at one
boundary, state, and abstraction level. Purpose / Outcome, System Context,
Business Map, Business Context, and Business Flow are different Views of a
larger Model. Do not put every level into one diagram or publish the entire
authoring workspace as one model note.

Keep the Why-to-How trace described in `business-story-and-5w2h.md`. The trace
is bidirectional: descend to concretize, and revise an upper Model when a lower
View reveals a wrong purpose, boundary, activity, or responsibility.

## Business Map and Business Flow

A Business Map answers which peer capabilities or Business areas constitute a
larger Business. Use relationship lines; their placement does not express
time. A Business Flow answers what happens next, where decisions occur, and
where work returns. Keep these as separate Views even when they share names.

Master element maps are a parallel canonical layer, not another abstraction
rung: actor, external-system, and information views hold same-type identities
and relationships. Context and overview views select those IDs and record the
links in the model-set index. If a detail changes the meaning of an element,
revise the master first, then propagate the canonical label and ID to consumers.

## The three-rung context ladder

The following is a reusable path, not a requirement to create three diagrams
every time. Add only the rungs that help the current discussion.

| Rung | Artifact | Center and scope | Relationship meaning |
| --- | --- | --- | --- |
| 1 | Overall context | The title-level business area or outcome as one `b_` anchor, with major actor subjects around it | `---` means the overall business relationship; no sequence |
| 2 | Use-case / scene context | One scene where responsibility, system boundary, information handoff, or value recipient changes; one outcome-sized `b_` activity plus selected master elements | left = provider, center = Business, right = recipient; `---` by default; arrow only when direction itself cannot be expressed by placement |
| 3 | Business flow | One selected use-case activity decomposed into actions, decisions, and essential rework | `-->` means order; use the flow Skill |

The first rung's `b_` node is a title anchor for the business area or outcome,
not a small task. The second rung is the business-centered discussion surface:
it selects canonical `a_`, `x_`, and `i_` nodes rather than inventing local
identities. The third rung is deliberately not a context diagram; it answers
what happens next inside the selected scene.

### Choosing and splitting a scene

Choose a use-case context when one of these changes the reading:

- who provides, owns, or receives the value;
- which external system crosses the boundary;
- which information is created, changed, or handed off; or
- where responsibility moves between participants.

If one scene becomes crowded, first preserve it as a complexity observation,
then split it into sibling use-case contexts by scene, question, or relationship
kind. Do not shrink labels or hide elements solely to fit Mermaid. Each sibling
keeps the same overall parent and its own focused question.

## View roles

| View | Purpose | Typical level |
| --- | --- | --- |
| Complexity observation | Preserve the full same-level backbone for discussion | Activity or capability |
| Overall context | Name the whole business area and its major actor subjects | Rung 1 |
| Use-case context | Explain one changing scene around a business outcome | Rung 2 |
| Overview flow | Show high-level handoffs or order across several views | One level above children, only when order is the question |
| Business flow | Explain order, decisions, or rework inside one use-case activity | Rung 3 |

Observation and overview are different. Observation preserves complexity at the
current level; an overall or higher overview deliberately summarizes it.

Move upward one rung at a time:

| Child | Parent overview |
| --- | --- |
| Operation or task | Activity or outcome unit |
| Activity or use-case scene | Capability or business area |
| Capability or business area | Purpose or value concept |

Do not add another overview at the same level merely to reduce node count.

## Concrete to abstract

1. Preserve the candidate inventory and useful dense observation view.
2. Group details that share an outcome, responsibility, or boundary.
3. Name each group as one next-higher concept.
4. Choose relationship or handoff semantics and assign stable IDs.
5. Record which detailed views and concrete nodes each overview node summarizes.

Do not group items merely because Mermaid placed them near each other.

## Abstract to concrete

1. Select one overall or higher-overview node whose meaning needs discussion.
2. State a narrower scene question and boundary.
3. Expand it into one use-case context, selecting canonical master IDs.
4. Add a business flow only when internal order or decisions matter.
5. Link every child to its parent diagram and exact parent node ID.

## Bidirectional trace

For every view, record rung/level, role, parent and expanded node ID, children,
one-sentence focus, selected master IDs, and status. A use-case context expands
exactly one overall node; a business flow expands exactly one use-case activity.
Keep the observation view while it remains meaningful evidence. Revise upward
when detail changes a shared concept or master identity; descend when an
overview hides a disputed distinction.

## Round-trip loop

1. Start at the overall context and choose one scene that needs detail.
2. Expand that node into a use-case context and reconcile its actor, system,
   and information selections with the masters.
3. Add a business flow only for the selected activity's internal order.
4. Bring discoveries back upward: update the master or parent overview when the
   meaning, boundary, or value recipient changes.
5. If the detail reveals another distinct scene, add a sibling context and keep
   both children linked to the same parent. If several siblings change the
   overall reading, add one higher overview rung.
