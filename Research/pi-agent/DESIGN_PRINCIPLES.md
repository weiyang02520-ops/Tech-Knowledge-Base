# Design Principles and Minimal Core

Use When:
- evaluating whether an agent architecture is over-designed
- choosing which capabilities belong in core or extensions

## Why the Core Is Small

[Repo-confirmed] `pi-agent-core` contains a stateful `Agent`, uniform message/tool types and a loop. Session files, compaction, coding tools, resource discovery, TUI and providers live outside it. `[Inference]` The core is small because its invariant is narrow: repeatedly ask a model, execute declared tools and emit ordered events.

[Docs-confirmed] Pi intentionally does not ship built-in multi-agent orchestration, memory database, workflow engine, browser, vector database or GUI. Examples/extensions can implement subagents and specialized behavior; external interfaces can build GUIs.

## Benefits and Costs

- `[Inference]` Benefits: provider/UI reuse, mockability, small conceptual kernel, replaceable policy, no forced database or workflow semantics.
- `[Inference]` Costs: important product behavior accumulates in `AgentSession` and extensions; integrations must choose policy; full-permission local extensions widen risk; users can assemble inconsistent systems.

## Extensibility Philosophy

[Repo-confirmed] Dynamic system prompts, context transforms, tools, providers, commands, UI and session gates are host-level extension points. Skills use progressive disclosure rather than runtime code. Packages distribute both.

[Inference] Pi prefers mechanisms over domain policy. AI Novel Studio should invert that priority where safety and authorship state matter: keep domain transitions (DRAFT → REVIEWING → READY), canonical facts, revision guards and Writer persistence in core; make optional context sources/exporters/providers extensible.

## Over-design Judgment

[Inference] AI Novel Studio is not over-designed in its M5 Writer path: Chief → validated TaskCard → deterministic ContextBudget → prose-only Writer → non-canonical partial → guarded draft is domain decomposition, not agent-framework ceremony. The general Chief `AgentSession` is underpowered for persistent chat, but adding multi-agent scheduling, generic plugins, vector memory and RPC before the GUI/use cases would be over-design.

