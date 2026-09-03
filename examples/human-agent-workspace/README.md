# Human–Agent Workspace

This example shows one way to separate human judgment, conversational sense-making, repository
work, and public reuse without making the human carry every agent-to-agent message.

- **maakbo**: the human decision maker.
- **matti**: the ChatGPT-side thought partner who clarifies intent and reviews meaning.
- **kubox**: the Codex-side repository operator who works within the agreed intent.

## Views

1. [Architecture Overview](architecture-overview.md) — the private control plane and public reuse
   surface.
2. [Handoff and Review Flow](handoff-review-flow.md) — the request, independent review, response,
   and human-decision loop.

The pages show only the reusable architecture. Private decisions and operational history remain in
the private repository.
