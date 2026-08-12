# Pi vs AI Novel Studio

Use When:
- comparing the two architectures item by item
- checking whether Pi's coding-agent choices fit a novel-writing product

## Snapshot Caveat

[Repo-confirmed] Pi is pinned to `2e4d239…`. AI Novel Studio is inspected at committed SHA `877c6edf…` plus visible uncommitted M5 hardening changes in `context_budget.py`, generation/workflow/writer and tests. Claims about those changes refer to the workspace snapshot, not the clean commit alone.

| Area | Pi | AI Novel Studio | Judgment |
| --- | --- | --- | --- |
| Agent Runtime | generic async event loop, normalized tool/message protocol | small synchronous Chief tool loop plus separate Writer workflow | Novel should unify interfaces, not erase specialized workflow |
| AgentDef | runtime tools/state are mutable; extensions can change them | explicit `AgentDef` id/prompt/tool allowlist/round limit/model role | Novel's role definition is clearer domain policy |
| Session | `Agent` + `AgentSession` + `SessionManager` + replacement runtime | in-memory `AgentSession` with `messages` and 40-message trim | Pi is much more mature for chat lifecycle |
| Tool Registry | dynamic built-ins/custom/extensions; TypeBox; async/progress/cancel | explicit registry, strict small schema, per-role allowlist, whole-batch preflight | Novel is safer; Pi is more general |
| Provider | multi-provider/model/auth/capability registry | one OpenAI-compatible implementation behind `BaseProvider` | keep current until a distinct API family is needed |
| Streaming | normalized model and tool event streams | Provider chunks; Writer streams; Chief loop calls `chat()` | adopt shared events incrementally |
| Context | active session projection + transforms | deterministic domain source collection and priority budget | complementary, not substitutes |
| ContextBudget | usage/model window plus compaction thresholds | explicit rendered budget with output reserve, safety margin and source manifest | Novel is stronger for prose generation |
| Compaction | LLM summary + recent messages; persisted boundary | none; chat destructively trims by message count | persistent chat eventually needs Pi-like projection |
| History | append-only JSONL tree retains all conversational entries | project `.history` snapshots/undo for content mutations | both are correct for different histories |
| Extensions | executable full-permission hooks/tools/UI/provider API | none/general plugin API absent | defer; start typed and constrained |
| Skills | name/description/location always visible; full text on demand | KB router is external; prompts are static files | progressive disclosure is a strong fit for KB |
| CLI/Core | interactive/print/JSON/RPC share runtime | core has no UI dependency; CLI adapters call services | both align; Novel lacks stable app-service event contract |
| Error handling | tool errors as messages; provider retry/overflow policy | stable ProviderError codes; safe tool errors; workflow guards | Novel safety is strong; retry policy is narrower |
| Cancellation | AbortSignal across provider/tool/summary/retry | Ctrl+C/stream exception; durable Writer partial | Pi general cancellation stronger; Novel Writer recovery stronger |
| Long generation | chat message persistence, tool progress | append-only `.partial.md` + sidecar + cross-process resume + guarded finalize | Novel should keep its design |

## Key Structural Difference

[Inference] Pi centers an open-ended conversation; durable state is the conversation tree. AI Novel Studio centers a canonical novel project; durable state is structured domain files and guarded draft transitions. Therefore Pi's `AgentSession` should inspire the chat/control plane, while Novel's `WriteWorkflow` remains the domain data plane.

## M0–M5 Alignment

[Repo-confirmed] Current Novel choices already aligned with Pi principles include: provider-neutral internal message types; UI-independent core; explicit tool schemas and registry; per-agent tool selection; bounded tool rounds/calls; error normalization; stream chunks; model configuration; and event-like structured results.

[Inference] Novel goes beyond Pi's defaults in relevant areas: project-relative safe paths, no shell, optimistic revision checks, snapshots/undo, whole-batch mutation preflight, provenance hashes, and non-canonical crash-resilient Writer partials.

## Gaps Found

- `[Repo-confirmed]` Chat sessions are not persisted and `_trim_session()` deletes context by count without preserving tool-call grouping semantics beyond head/tail slicing.
- `[Repo-confirmed]` Chief runtime is synchronous and cannot expose incremental provider/tool events or cooperative cancellation.
- `[Inference]` `AgentDef` is mutable after construction; immutable role specs plus per-session runtime state would reduce accidental leakage.
- `[Inference]` Provider capability is largely a `tool_calls` boolean; future reasoning/image/JSON/schema/context capabilities need explicit metadata.
- `[Inference]` There is no stable GUI-facing session/application service or event protocol yet.

