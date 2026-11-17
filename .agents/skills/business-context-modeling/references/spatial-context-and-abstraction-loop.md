# Spatial context and abstraction loop

This reference governs the **reusable modeling behavior of the Skill**, not a particular project's example. It is part of the authoring contract for a work-level System Context and its descendant Business Contexts. It extends (does not replace) `modeling-rules.md`, `multi-view-modeling.md`, and the Mermaid authoring conventions.

## Why these Views exist

The reader should be able to understand a work's purpose and value relations **from the position and semantic icons of its elements**, without decoding a forest of arrowheads. These Views are instruments for discussion and revision, not documentation of a predetermined process.

**System Context** answers "What is the whole work for, and who is involved?" **Business Context** answers "In one meaningful scene, who or what supplies value and inputs, what Business transforms them, and who or what receives value and outputs?" **Business Flow** answers temporal order, decisions, returns, and task ownership. Do not let the latter questions leak into the first diagram.

## First View: a deliberately sparse System Context

1. Name the **whole work** in the reader's language and use one central `b_` Business anchor. For a work-modeling task, do **not** quietly replace that anchor with the software product being developed.
2. Reuse the **agreed purpose sentence** as one `p_` rounded note **visually above and to the right of the central Business**. It represents the goal that all the participants orient toward, not a new data object, another task, or a destination node in a sequential process. Preserve the user's intent; never reduce a desired lived/business state to a delivery method or one-time handover.
3. Include only the major participating `a_` Actors and genuinely relevant `x_` External Systems. Distinguish responsibility/participation from organizational affiliation; one participant can be both a provider and recipient in reality. Choose a *primary* value role for this View without duplicating the same actor to force symmetry.
4. Use semantic **Z-index / SIPO reading order**: **provider/executor Actors and External Systems on the left → the whole Business at center → recipients/beneficiaries on the right**, with the purpose above-right. No `i_` Information, phase list, implementation tools, or handoff matrix in this first View. The detailed inputs/outputs belong to the next View.
5. Relationships are few, meaningful, and predominantly `---`; use one `-.-` from the central Business to the purpose note. **Do not draw normal value direction with arrows**. If a system is not evidenced or named, do not invent one to make the diagram look complete.
6. Keep the exact icon family and styles selected in `.fde/config.json`: one canonical icon per semantic role (Actor, Business, Information, External System, Decision), 28×28 icon canvas, 14px labels, light relation line. Never substitute boxed default Mermaid nodes for semantic icons in the name of speed.
7. The source order should declare left-side elements, then central `b_`, then `p_` **before** right-side participants, and finally relations. This is a *layout hint*, **not proof** of placement. Render/preview and inspect; if the note appears below or to the left, mark the visual acceptance **not passed** and adjust meaningful layout choices. Never fake relations or insert invisible nodes solely to move it.

**System Context acceptance gate**: the first glance identifies *the work*, *the purpose at upper-right*, *who supplies/executes*, and *who benefits/receives*. If not, simplify; do not compensate with a paragraph, phase table, extra notes, or edge labels. Actual operational scope can be explained in short adjacent prose without packing it into the picture.

## Next View: Business Context as spatial SIPO

For a chosen Business Use Case / coherent scene, make the value roles legible **in space**:

| Zone | Elements and meaning |
| --- | --- |
| Far left | `a_` / `x_` providers, executors, source systems (value supplied) |
| Inner left | `i_` inputs: real information used, checked, or updated |
| Center | `b_` Business activities with meaningful outcomes (not a list of procedural steps); preserve a readable sibling backbone |
| Right | `a_` / `x_` value recipients and `i_` outputs/results (relative order follows actual relationships, not a rigid recipe) |
| Upper right of the relevant Business | `p_` purpose / outcome note **when needed** to make the collective goal explicit |

- **Position denotes value role**; `---` denotes participation or meaningful association. A line is not a workflow arrow. Avoid edge labels, arrowheads, decorative grouping, and duplicated identities when positional semantics already suffice.
- Ground each participant relation in what is provided, done, decided, received, or used; ground each Information relation in the Business Story and Information × Business matrix. Maintain one stable Information vocabulary across parent/child Views.
- If a participant materially both supplies and receives, keep one identity and choose the primary role in this scene. Discuss feedback/loops in the Flow or in a focused Context; do not draw two copies of the participant.
- A `--> ` exception is allowed **only** for direction whose meaning cannot be inferred from position, with a written reason and the explicit checker option. Do not use arrows to make a value-chain look more like a process.
- A multi-Business Context is a relationship projection, **not phase order**. A phase is a useful navigation index, but is not automatically a Business or its child.

## The concrete → abstraction → concrete loop

Do **not** start with an elegant but ungrounded 4–6 box taxonomy. Begin with what actually happens in **one concrete case**. Avoid replacing named work with generic labels that lose meaning.

1. **Get concrete**: describe one job/scene in people's vocabulary; identify Who, Why, Input, Business transformation, Output, recipients, systems, and unknowns. Gather as many *real, meaningful* candidates as needed for one provisional canvas. A first draft is allowed to be dense; classify observations vs assumptions.
2. **Sketch one whole scene**: use the spatial SIPO contract and a lightweight relationship model/matrix. Check that each depicted element is traceable to the described work, not borrowed from a previous sample. Do not use a template's node/edge counts as the model's required cardinality.
3. **Read it aloud as work**: can a participant explain the value and each relationship at this level without tracing crossings or reciting a method? Check the rendered graph. High Business-element × relation density, crossing lines, mixed responsibility boundaries, or a story that cannot be told at a glance are signals for **reconsidering grain**—not merely aesthetic defects to hide.
4. **Cut at a real scene change**: split when the actors/systems, Information, value provider/recipient, responsibility, or outcome change materially. Try grouping elements that together express one useful Business outcome. If the group has a coherent input, transformation, output and responsibility, name that **parent Business**. If a candidate has no meaningful boundary, leave it within its scene. Never divide automatically at a fixed node count or at every phase.
5. **Retain both levels and trace**: the parent Context shows its peer Businesses and their relation; a selected Business opens a child Detailed Context / Business Use Case (relations) or a Business Flow (sequence, decision, task, rework). Preserve stable IDs, parent/expanded-node links, and the ability to return from child to parent. A phase can still index this structure without being equated to it.
6. **Return upward**: when a child reveals a role, missing information, different outcome, or a false boundary, correct the parent and master elements, then propagate to affected sibling Views. Never treat a beautiful diagram as evidence of semantic correctness.

**Stop splitting** when the remaining scene tells a coherent value story, not when the picture reaches a prescribed node count. **Stop expanding** when the current question can be answered; do not manufacture tasks to fill a hierarchy.

## Failure patterns that must block a claimed finished model

- The whole-work System Context contains phase sequences, request/design/test output lists, implementation detail, or several separate context notes instead of the principal purpose.
- The purpose exists only in adjacent prose, or renders away from the **upper-right** of the central Business.
- The key Actors/Systems are on arbitrary sides and positional SIPO meaning cannot be read without arrow directions.
- Default boxed flowchart nodes replace semantic icons or mix icon sets across Views.
- Context is a line of process steps connected by `-->`; arrowheads carry ordinary input/output direction.
- Business Context is just a phase index, or its input/output Information has no grounded relationship to Businesses.
- The scene is obviously unreadable but is force-laid out, shrunk, or reduced to a generic chain instead of reconsidering meaningful boundaries.
- A child View changes the meaning of an Actor/Information/Business and leaves the parent stale.
- A specific synthetic example or screenshot is presented as proof that the **Skill** itself now works across real conversations.

## Checks and evidence

1. Run the icon/context and semantic checkers, including the **System Context profile** for a first View (when available), but recognize that source order cannot prove on-screen coordinates.
2. **Visual gate**: inspect the actual Mermaid render, preferably at iPad reading width: central Business, provider left, recipient right, purpose above-right; icons and labels intact; arrows restrained. Record what was or wasn't verified, rather than claiming success from source checks alone.
3. **Conversation regression**: without copying any completed example, try at least two *different* kinds of work descriptions. For each, elicit a sparse whole-work Context, then a concrete Business Context, observe complexity, justify one split (or explicitly decline it), expand a child, and propagate one correction back to the parent. Check that the resulting source is useable and privately stored for confidential scenarios.
4. The acceptance output must identify **what was validated**, **what remains tentative**, and **what a reader still cannot infer**. A public example page is neither required nor sufficient for this Skill improvement.
