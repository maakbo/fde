# Synthetic Discovery Intake

This fixture is intentionally synthetic. It tests the Discovery facilitation mechanism and is not a claim about a real company.

## Field story

A system-development team receives requests from a business department and turns them into requirements and specifications.

The business department often explains what they want in documents and meetings. Project leads and designers review the material, ask follow-up questions, and rewrite it into requirements.

In this synthetic case:

- reviewers repeatedly search several documents for the same business terms;
- experienced designers notice contradictions that newer members often miss;
- some contradictions are discovered only after basic design has started;
- final decisions still need a human because business intent is contextual;
- documents are stored in an internal environment and cannot be sent to an unrestricted external service.

The team is interested in AI, but has not decided what should be automated.

## Expected Discovery behavior

The Skill should not jump directly to "build an AI agent."

It should:

1. make the current work visible;
2. reconsider unnecessary or duplicated checking;
3. identify late contradiction discovery / repeated cross-document checking as candidate bottlenecks;
4. compare process simplification, deterministic checks, information-structure improvements, AI assistance, and human review;
5. treat security constraints as part of feasibility and risk;
6. keep final contextual judgment human unless evidence supports a different boundary;
7. produce a Definition handoff for one first target;
8. preserve unknowns such as actual frequency, time cost, error rate, and document sensitivity classification.
