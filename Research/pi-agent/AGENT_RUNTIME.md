# Agent Runtime

Use When:
- implementing or debugging an LLM tool loop
- deciding what belongs in `Agent`, `AgentSession`, and the provider layer

## Exact Turn Path

[Repo-confirmed]

```text
AgentSession.prompt(text)
  input hook -> skill/template expansion -> model/auth preflight
  -> extension before_agent_start -> AgentSession._runAgentPrompt(messages)
  -> Agent.prompt(messages)
  -> Agent.runWithLifecycle(AbortController)
  -> runAgentLoop(prompts, AgentContext snapshot, AgentLoopConfig)
  -> runLoop()
       streamAssistantResponse()
         transformContext -> convertToLlm -> Context{systemPrompt,messages,tools}
         -> streamFunction(model, context, options)
         -> provider AssistantMessageEventStream
       find toolCall blocks
       -> executeToolCalls(sequential or parallel)
          find tool -> prepareArguments -> validateToolArguments
          -> beforeToolCall -> tool.execute(signal,onUpdate) -> afterToolCall
          -> ToolResultMessage
       push tool results into current context
       -> next model turn while tool calls/steering remain
  -> message_end listener persists messages
  -> AgentSession._handlePostAgentRun()
       retry or compact and Agent.continue() when needed
  -> agent_settled
```

## Inputs, Outputs and State

| Step | Input | Output / state |
| --- | --- | --- |
| `AgentSession.prompt` | text, images, source, queue behavior | `AgentMessage[]`; per-turn prompt override |
| `Agent.prompt` | one/batch `AgentMessage` | mutates active transcript through events |
| `runAgentLoop` | prompt messages + snapshot + config + signal | newly emitted `AgentMessage[]` |
| `streamAssistantResponse` | `AgentContext` | final normalized `AssistantMessage` plus deltas |
| `executeToolCalls` | assistant tool calls | ordered `ToolResultMessage[]`, termination flag |
| `AgentSession` listener | `AgentEvent` | JSONL entries, extension events, retry/compaction bookkeeping |

[Repo-confirmed] Provider-specific conversion happens only at `streamFunction`/`pi-ai`; the low-level loop sees the uniform `AssistantMessage` content blocks and `StopReason`.

## Loop Semantics

[Repo-confirmed] The inner loop continues for tool calls and steering messages; the outer loop drains follow-ups only after the agent would otherwise stop. Queue mode is `all` or `one-at-a-time`.

[Repo-confirmed] A message containing any tool marked `executionMode: "sequential"` makes the whole batch sequential; otherwise the configured default is parallel. Parallel results are awaited together but emitted back to the model in original call order.

[Repo-confirmed] A response stopped by `length` never executes its tool calls because their salvaged arguments may be silently truncated. Pi synthesizes error tool results and lets the model reissue them.

[Repo-confirmed] Tool failures are data, not loop crashes: missing tools, invalid arguments, thrown execution errors and hook failures become `isError: true` tool results. A runtime/provider exception becomes a terminal assistant message with `stopReason: error` or `aborted`.

## Design Rationale

[Inference] The event-driven reducer allows the same loop to feed persistence, TUI, JSON, RPC and tests without UI imports. Snapshotting context at run start avoids casual shared-array mutation; `prepareNextTurn` deliberately refreshes model, tools and system prompt between tool rounds so extensions can change runtime configuration mid-turn.

