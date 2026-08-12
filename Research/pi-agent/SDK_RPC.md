# SDK and RPC

Use When:
- embedding the agent in desktop/web apps or exposing it to non-TypeScript clients
- deciding whether UI and agent core are genuinely decoupled

## SDK

[Repo-confirmed] `createAgentSession(options)` is the in-process entry. It composes `ModelRuntime`, `SettingsManager`, `SessionManager`, `ResourceLoader`, selected/custom tools, extensions and `Agent`; it restores messages/model/thinking from an existing manager and returns `{session, extensionsResult, modelFallbackMessage}`.

[Repo-confirmed] Callers can use in-memory, new persisted, recent, or explicit-file `SessionManager`s; inject models, tool lists, custom tools and resource loaders; subscribe to events; prompt/steer/follow up; compact; abort; change model/thinking; inspect messages and dispose.

[Repo-confirmed] `createAgentSessionServices()` separates cwd-bound settings/models/resources from session creation. `AgentSessionRuntime` owns replacing the live session for new, switch/resume, fork/clone and import. This is the layer used by built-in interactive, print and RPC modes.

## RPC

[Repo-confirmed] RPC is newline-delimited JSON over stdin/stdout. Commands cover prompt/queues/abort, session replacement and tree reads, models/thinking, compaction/retry, bash, statistics/export and command discovery. Events stream asynchronously. Extension UI requests have request IDs and matching input responses.

[Docs-confirmed] Node/TypeScript hosts should prefer the SDK; RPC is intended for subprocess isolation/language boundaries. The RPC process still has Pi's host permissions—it is a process boundary, not a security sandbox.

## GUI Value

[Inference] Pi demonstrates that one agent core can serve CLI, desktop, web or messaging adapters. For AI Novel Studio, define a stable application service/event interface now; use direct Python calls for the first GUI. Add local RPC only when a separate frontend process or another language actually needs it. Copy session-replacement semantics and asynchronous accepted-command/event separation, not the entire Pi protocol.

