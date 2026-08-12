# AI Novel Studio Lessons

Use When:
- prioritizing M6, M7 and Post-MVP architecture work
- deciding what to adopt, defer or reject from Pi

# Executive Conclusion

[Inference] If redesigning AI Novel Studio today after studying Pi, keep its domain safety and Writer pipeline, but introduce a small shared turn runtime contract, immutable role definitions, explicit session/application events and a future append-only chat session store. Do not add a generic multi-agent framework, full-permission plugin system, shell tool or generic compaction inside the Writer path.

# What Pi Does Better

[Repo-confirmed] Pi has clearer runtime layering; non-destructive persisted session trees; complete resume/fork/branch semantics; cooperative cancellation; tool/model streaming events; provider capability normalization; bounded overflow recovery; progressive skill disclosure; and SDK/RPC surfaces used by multiple UIs.

# What AI Novel Studio Already Does Well

[Repo-confirmed] Novel has safer project boundaries, strict role allowlists, batch mutation preflight, optimistic revision guards, snapshots/undo, canonical/derived data separation, deterministic Writer context selection, validated TaskCards, prose-only Writer isolation, durable partial generation and guarded draft state. These are product invariants and should not be diluted by a generic agent framework.

# Adopt Now

## 1. Shared Turn Runtime Contract

- Pi current: `[Repo-confirmed]` `Agent` accepts provider-neutral messages/tools and emits ordered lifecycle events.
- Novel current: Chief uses `run_agent`; Writer and Chief planner bypass that loop through separate provider calls.
- Difference: no common request/result/event/cancel vocabulary across the three roles.
- Benefit: GUI, usage, logging and cancellation integrate once without forcing identical workflows.
- Cost: small interfaces/adapters; no behavior rewrite required.
- Risk: over-generalizing Writer into a tool loop. Keep Writer as a specialized execution strategy.
- Recommended stage: Now, as contracts only; implementation can remain incremental.

## 2. Immutable Role Definition + Per-run State

- Pi current: runtime separates `Agent` state from tool/model contracts, though host settings remain dynamic.
- Novel current: `AgentDef` is a mutable dataclass; `m4_chief_agent_def()` mutates a returned instance.
- Difference: definition and session policy can blur.
- Benefit: prevents role/tool leakage; makes tests and future Reviewer safer.
- Cost: frozen dataclass and builder changes.
- Risk: minimal migration friction.
- Recommended stage: Now / before M6.

## 3. Stable Application Events

- Pi current: start/update/end/settled, tool, compaction and queue events feed TUI/SDK/RPC.
- Novel current: CLI callbacks expose Writer stage/text deltas; Chief returns a final structured result.
- Difference: no common GUI-facing event stream.
- Benefit: future GUI can render progress without importing CLI behavior.
- Cost: event dataclasses and adapters.
- Risk: premature exhaustive event taxonomy. Start with run/stage/text/tool/error/settled.
- Recommended stage: Now, alongside GUI boundary.

# Adopt in M6

## 4. Shared Runtime + AgentDef for Chief / Writer / Reviewer

- Pi current: one runtime can host different prompts/tools without a built-in multi-agent scheduler.
- Novel current: Chief plans; Writer generates; future Reviewer owns only DRAFT → REVIEWING → READY.
- Difference: roles are orchestrated by `WriteWorkflow`, not independent collaborating agents.
- Benefit: common lifecycle and policy while preserving deterministic workflow ownership.
- Cost: Reviewer adapter and shared cancellation/usage plumbing.
- Risk: turning Reviewer into an autonomous peer that can bypass state transitions.
- Recommended stage: M6; workflow remains the sole orchestrator.

## 5. Explicit Model Capabilities

- Pi current: model metadata includes context, output, reasoning, modalities and compatibility.
- Novel current: configuration mainly exposes model, max context and `tool_calls`.
- Difference: role selection cannot reason about structured output, streaming, images or reasoning.
- Benefit: safer fallback and validation for Reviewer/Writer.
- Cost: capability dataclass and configuration validation.
- Risk: inaccurate user-supplied metadata.
- Recommended stage: M6 only for capabilities actually consumed.

# Adopt in M7

## 6. Append-only Persistent Chat Session

- Pi current: JSONL header + parent-linked entries, model/thinking changes and compaction entries; active context is a projection.
- Novel current: chat messages are in memory and truncated at 40 messages.
- Difference: process exit loses chat; destructive trim loses earlier context.
- Benefit: resume, audit, crash recovery and future GUI continuity.
- Cost: versioned format, migrations, list/open semantics and privacy controls.
- Risk: confusing project mutation history with conversation history; store separately.
- Recommended stage: M7 when persistent chat becomes a product requirement.

## 7. Conversational Compaction

- Pi current: threshold/overflow summary with recent-turn retention and full historical log.
- Novel current: count-based trim; Writer uses deterministic context budget instead.
- Difference: no semantic continuity for long chat.
- Benefit: long Chief/Reviewer conversations remain usable.
- Cost: summary prompt, usage, failure/retry and evaluation tests.
- Risk: hallucinated/omitted intent; never promote summary into canonical novel facts.
- Recommended stage: M7 after session persistence and real telemetry show need.

## 8. Knowledge-base Progressive Disclosure

- Pi current: only skill metadata is always present; full instructions load by model choice or explicit command.
- Novel current: Tech-Knowledge-Base already has `kb.py search/reuse` and focused Markdown.
- Difference: KB retrieval is not integrated into role context.
- Benefit: low token cost and targeted architecture knowledge.
- Cost: router adapter and `Use When` metadata hygiene.
- Risk: model skips retrieval or retrieves stale guidance.
- Recommended stage: M7 for engineering agents; for in-product novel knowledge, use deterministic domain retrieval instead.

# Adopt Post-MVP

## 9. Typed Plugin Architecture

- Pi current: broad executable extensions can modify nearly every runtime layer.
- Novel current: no plugin API.
- Difference: Pi optimizes local developer extensibility; Novel protects author data.
- Benefit: exporters, context sources, providers and review rules become installable.
- Cost: versioning, permissions, discovery, diagnostics and compatibility tests.
- Risk: arbitrary code and unstable internals.
- Recommended stage: Post-MVP; begin with narrow typed capabilities and explicit trust.

## 10. Local RPC

- Pi current: SDK for in-process TypeScript; JSONL RPC for subprocess/language boundaries.
- Novel current: Python core and CLI; future GUI unspecified.
- Difference: no stable process protocol.
- Benefit: web/desktop/QQ adapters can share one long-lived core.
- Cost: protocol versioning, async events, shutdown and reconnect.
- Risk: unnecessary distributed-state complexity for a Python GUI.
- Recommended stage: Post-MVP, only if frontend becomes a separate process/language.

# Do Not Adopt

- `[Inference]` General multi-agent framework now: Chief/Writer/Reviewer need shared runtime contracts and an explicit workflow, not autonomous routing, delegation or agent-to-agent chat.
- `[Inference]` Full-permission shell/file tools: Novel's safe project store and domain mutations are superior for author data.
- `[Inference]` Pi extension API wholesale: too broad and unisolated for the product's trust boundary.
- `[Inference]` Generic compaction for Writer inputs: preserve deterministic `ContextBudgetPlan` and structured facts.
- `[Inference]` Provider breadth for its own sake: add adapters only for user demand and distinct API semantics.
- `[Inference]` Vector DB/memory database in core: structured project files and provenance remain authoritative; retrieval can be added as a derived index.

# Architecture Risks Found in AI Novel Studio

1. `[Repo-confirmed]` `_trim_session()` uses message count and can remove middle tool context without a durable audit log.
2. `[Inference]` Separate Chief/Planner/Writer call paths will duplicate cancellation, events, usage and retry policy unless unified at the contract level.
3. `[Inference]` A future GUI could couple directly to CLI functions unless an application-service API is declared first.
4. `[Inference]` Mutable `AgentDef` and loosely typed `Any` context/registry fields reduce static guarantees around Reviewer authorization.
5. `[Repo-confirmed]` Context-too-long Writer fallback shrinks every selected item by 0.65, which may truncate critical rules/outline after the first carefully prioritized plan; a second priority-aware replan would be safer.
6. `[Inference]` Partial file append and metadata update are individually durable but not one atomic transaction; recovery tests must cover mismatched sidecar/body states.

# Final Recommended Architecture

```text
GUI / CLI / future adapters
  -> ApplicationSession service + typed events/cancellation
      -> ConversationStore (M7, append-only; separate from project history)
      -> Shared TurnRuntime contracts
          -> Chief strategy (tool loop)
          -> Writer strategy (TaskCard + ContextBudget + prose stream)
          -> Reviewer strategy (review-only tools + state gate)
      -> Workflow orchestrator owns role order and state transitions
      -> Domain core owns ProjectStore, revisions, snapshots, drafts and facts
      -> ProviderRegistry (capabilities added only as needed)
```

# Direct Answers

1. AgentSession should evolve toward Pi's separation of engine/session/store, but retain Novel domain services.
2. Chief/Writer/Reviewer do not need a multi-agent framework.
3. Shared Runtime contracts + immutable AgentDef/role strategy + explicit workflow are enough.
4. Compaction belongs after persistent chat and measured context pressure, likely M7.
5. Pi's append-only persistence/projection idea is worth adopting; its exact coding-centric entry types are not.
6. Extensions are a Post-MVP reference, with narrower permissions and typed capabilities.
7. Pi Skills fit Tech-Knowledge-Base progressive disclosure; use the router and 1–3 focused files.
8. SDK-style application services matter for the GUI now; RPC matters only across a real process/language boundary.
9. Current M5 domain architecture is not over-designed; adding generic agent/plugin/distributed machinery now would be.
10. M0–M5 already align on UI-independent core, provider abstraction, structured messages, explicit tools, bounded loops, error normalization, streaming and context budgeting.

# If Redesigning Today

[Inference] I would change: persistent-session boundaries, immutable role specs, common events/cancellation, explicit model capabilities and priority-aware context retry. I would keep: local files as canonical truth, safe paths, no shell, role allowlists, TaskCard planning, deterministic Writer context, provenance, revision guards, snapshots, partial generation and workflow-owned state transitions.

