---
name: definition-facilitation
description: Turn a selected Discovery target into a reviewable Definition: scope, observable behavior, quality expectations, constraints, assumptions, acceptance criteria, and unresolved responsibility boundaries before solution design.
---

# Definition Facilitation

Use this Skill after Discovery has selected a business target, or when a user already knows what work should change but needs to define it well enough for people and implementation agents to discuss consistently.

Definition answers **what must be true**. It does not prematurely decide prompts, models, RAG, MCP, APIs, agent topology, or implementation architecture.

## Core contract

- Start from the Discovery Brief when one exists. Preserve its evidence, assumptions, unknowns, exclusions, and intended outcome.
- If no Discovery Brief exists, accept an equivalent field description; do not force the user backward if the target and rationale are already clear.
- Use business-context-modeling when actors, activities, information, systems, decisions, exceptions, or handoffs are still too vague to define behavior.
- Preserve the user's business language before introducing technical terms.
- Separate requirement from solution idea. Record useful solution ideas as later Design questions rather than silently converting them into requirements.
- Separate Evidence, Assumption, Constraint, and Unknown.
- Express acceptance criteria as observable outcomes or examples wherever possible.
- Do not invent numeric SLOs, accuracy thresholds, legal rules, data classifications, or authority boundaries.
- Keep human / AI / RPA / System responsibility as a boundary to define, not an excuse to design the solution early.

## Workflow

### 1. Re-establish the Definition boundary

State:

- selected target;
- intended business outcome;
- in-scope work;
- explicitly out-of-scope work;
- actors affected;
- upstream input and downstream use;
- evidence inherited from Discovery;
- unresolved questions that can change the boundary.

If the selected target is still ambiguous, narrow it before writing requirements.

### 2. Make the work observable

Describe the target as behavior rather than document names or implementation components.

Capture:

- trigger / starting situation;
- input information;
- major business decisions;
- normal path;
- meaningful exceptions;
- output / changed state;
- who uses or confirms the result.

Use concrete examples when tacit judgment appears. Ask what an experienced person notices, compares, rejects, escalates, or treats as exceptional.

### 3. Define functional requirements

For each required behavior, state what the future work or mechanism must enable.

Prefer forms such as:

- detect / present / compare / record / route / prevent / allow;
- actor + observable behavior + relevant condition.

Avoid implementation prescriptions such as "use vector DB" or "call an LLM" unless they are genuine constraints.

### 4. Define non-functional requirements

Only include qualities that matter to the field case, such as:

- timeliness;
- correctness / quality;
- repeatability;
- explainability / traceability;
- availability;
- security / privacy;
- operability;
- cost;
- maintainability;
- accessibility.

If a target value is unknown, record the quality dimension and how it should be measured rather than inventing a number.

### 5. Separate constraints and assumptions

**Constraint**: a condition the solution must obey.

Examples: approved environment only, mandatory human approval, existing system interface, regulation, data residency.

**Assumption**: something currently believed true that Definition depends on and should be verified.

Examples: documents are machine-readable, identifiers are stable, reviewers can access the same source.

Do not mix the two.

### 6. Surface responsibility boundaries

For each important decision or action, identify what must be decided before Design:

- who may propose;
- who may decide;
- who may execute;
- who must review;
- what may be automated;
- what must remain human-controlled;
- what requires specialist approval.

Do not choose an agent architecture here. Capture the unresolved boundary and evidence needed to settle it.

### 7. Write acceptance criteria

Acceptance criteria should let a field team judge whether the defined change is good enough to enter Design / PoC.

Use observable scenarios:

- Given a representative input or situation,
- When the defined behavior occurs,
- Then a person can observe a specific result.

Include important failure / exception cases.

Mark criteria whose threshold is still TBD. A TBD threshold is better than an invented number.

### 8. Handoff to Design

Definition is ready enough when the team can review:

- scope and exclusions;
- current / desired behavior;
- functional requirements;
- relevant quality dimensions;
- constraints and assumptions;
- representative decisions and exceptions;
- acceptance criteria;
- unresolved human / automation responsibility boundaries;
- Design questions that should not be answered in Definition.

## Output contract

Create a compact Definition Brief using templates/definition-brief.md.

Keep it reviewable by field participants. The brief is a shared decision surface, not a specification dump.

## Field-use loop

Discovery target -> observable work -> requirements -> constraints / assumptions -> responsibility boundaries -> acceptance criteria -> Design questions -> field review -> revise

After field review, capture:

- wording that field participants interpreted differently;
- missing decisions or exceptions;
- requirements that were actually solution ideas;
- acceptance criteria nobody could judge;
- constraints discovered too late;
- responsibility boundaries that caused disagreement.

Use that evidence to refine Definition before moving deeper into Design.
