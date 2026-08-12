# Testing Strategy

Use When:
- designing test seams for runtime, persistence, providers or plugins
- deciding whether a module boundary is justified by testability

[Repo-confirmed] At the pinned commit the monorepo contains approximately 131 `pi-ai`, 23 `pi-agent-core`, 222 `pi-coding-agent`, 32 TUI, and additional protocol/client/server test files. This is a source-tree count, not a claim that tests were executed.

## Layers

- `[Repo-confirmed]` `pi-ai`: provider payload/stream conversion, auth, abort, token/usage, context overflow, cross-provider handoff and mocks.
- `[Repo-confirmed]` `pi-agent-core`: loop order, tool calls, steering/follow-up, events, failure/abort and harness/session conformance.
- `[Repo-confirmed]` `pi-coding-agent`: `AgentSession` prompt/queue/retry/compaction, session JSONL/tree/migrations, tool implementations, extension runner/discovery, skills, SDK, RPC and regression fixtures.
- `[Repo-confirmed]` Integration tests use fake streams/providers and JSONL fixtures; selected subprocess tests cover RPC framing and lifecycle.

## Test-driven Boundaries

[Inference] The injectable `streamFn`, `AgentTool.execute`, `SessionManager`, `ResourceLoader`, `ModelRuntime` and extension runner are explicit seams that let the loop be tested without real networks, TUI or disk. Pure functions such as `buildSessionContext`, `findCutPoint`, schema validation and provider transforms carry the highest deterministic coverage value.

[Inference] `AgentSession`'s breadth creates combinatorial tests, visible in many targeted regression files. AI Novel Studio should keep its existing narrower `BaseProvider`, `ToolRegistry`, context planner and workflow services independently fakeable, while adding contract tests before introducing any plugin/RPC boundary.

## Research QA

[Repo-confirmed] This research performed static review only. Fifteen critical findings were rechecked against pinned source during the second pass: package direction, loop entry, provider boundary, tool validation, parallel ordering, truncated-call refusal, message persistence, JSONL tree, compaction trigger, cut rules, summary re-entry, history retention, extension isolation, skill disclosure and file/shell authority.

