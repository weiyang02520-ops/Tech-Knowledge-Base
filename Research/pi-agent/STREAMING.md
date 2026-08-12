# Streaming

Use When:
- implementing incremental model/tool UI updates
- defining cancellation and subprocess event semantics

[Repo-confirmed] Provider adapters return an async `AssistantMessageEventStream`. Events are `start`, text/thinking/tool-call start-delta-end, and terminal `done` or `error`. Each delta carries a current partial assistant message; `result()` resolves to the final normalized message.

[Repo-confirmed] `streamAssistantResponse()` inserts the partial into the current context at `start`, replaces it on deltas, emits `message_update`, and replaces it with the final message at completion. Persistence happens only on `message_end`, so partial model text is not appended as multiple durable entries.

[Repo-confirmed] Tool execution has a parallel event stream: start, zero or more partial updates, end, then message start/end for the durable tool result. This separates UI progress from the model-visible final result.

[Repo-confirmed] `AgentSession.subscribe()` exposes the same lifecycle to SDK callers. RPC serializes events as JSONL on stdout while command acceptance is acknowledged separately; prompt failure after acceptance is reported through event/message flow, not a second response.

[Repo-confirmed] Abort uses one run-scoped controller. Provider requests, tool execution, compaction/branch summarization and retry sleeps have signals/controllers; `AgentSession.abort()` cancels retry and agent work then waits for settled state.

[Inference] The distinction among delta, final message and durable persistence is worth copying. AI Novel Studio already streams Writer prose into a crash-resilient non-canonical partial file, which is stronger for long-form generation than Pi's ordinary chat persistence. Its general Chief tool runtime is non-streaming; unify event vocabulary later, but preserve the Writer partial workspace.

