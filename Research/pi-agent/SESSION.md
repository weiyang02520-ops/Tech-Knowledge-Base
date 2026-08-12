# Agent Session

Use When:
- designing conversation persistence, restore, fork or branch
- separating runtime state from durable history

## Three Different Objects

[Repo-confirmed] `Agent` is the in-memory turn engine. `AgentSession` is the application-facing lifecycle and policy coordinator. `SessionManager` is the durable append-only log/tree. `AgentSessionRuntime` replaces the active session object when the user changes session identity.

## Durable Data Model

[Repo-confirmed] A session file is JSONL. The header contains format version (currently 3), session id, timestamp, cwd and optional `parentSession`. Every subsequent entry has `id`, `parentId`, timestamp and a discriminated type:

- `message`: user, assistant or tool result
- `model_change`, `thinking_level_change`
- `compaction`, `branch_summary`
- extension `custom` state (excluded from LLM context)
- extension `custom_message` (included after conversion)
- `label` and `session_info`

[Repo-confirmed] Entries are append-only. `leafId` selects the active path. Branching moves the in-memory leaf pointer; later entries create a new child without deleting the abandoned branch.

## Where State Lives

| State | Owner |
| --- | --- |
| current transcript, system prompt, model, tools, thinking, streaming flags | `Agent.state` |
| session id/file/cwd, full entry tree, active leaf | `SessionManager` |
| retry, compaction, queue-display, extension and bash orchestration | `AgentSession` |
| resource discovery and base prompt inputs | `ResourceLoader` + `AgentSession` |
| new/switch/fork/import replacement | `AgentSessionRuntime` |

[Repo-confirmed] System prompt and tool definitions are rebuilt from current resources; they are not stored as ordinary session messages. Model and thinking changes are stored, and restore scans the selected branch for the effective values.

## Persistence Lifecycle

[Repo-confirmed] `AgentSession` subscribes to `Agent` and appends user, assistant and tool-result messages on `message_end`. A new persisted file is delayed until an assistant message exists, avoiding empty/abandoned session clutter. Thereafter entries append one JSON line at a time.

[Repo-confirmed] `SessionManager.open()` loads, migrates and indexes a file. `continueRecent()` selects the most recent session. `createAgentSession()` rebuilds the compaction-aware context and restores model/thinking where available.

## Resume, Branch, Fork and Clone

[Repo-confirmed] In-session tree navigation changes the selected leaf and optionally appends a branch summary. `createBranchedSession()` materializes one path into a new file. `forkFrom()` copies all source entries into a new file/cwd with a new header referencing `parentSession`. `AgentSessionRuntime.fork()` and `switchSession()` run before/after extension lifecycle gates and recreate cwd-bound services.

[Inference] Pi distinguishes branching history from creating a new session identity. This is a strong model for editor UX: “edit from here” should not necessarily create a new project conversation file, while “clone session” should.

## Recovery Boundary

[Repo-confirmed] Compaction never deletes JSONL history. `buildContextEntries()` projects only the latest compaction summary, kept messages and post-compaction entries into the model context. Full earlier history remains inspectable and branchable.

[Inference] Append-only files trade compact storage and transactional databases for transparency, portability and post-crash inspectability. Concurrent multi-process writers are not the intended model; session replacement is coordinated in one host process.

