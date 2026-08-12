# Call Chains

Use When:
- tracing a concrete runtime lifecycle or debugging an integration

## Normal Chat and Tool Call

```text
CLI/RPC/SDK -> AgentSession.prompt
 -> input hook -> skill/template -> auth -> before_agent_start
 -> _runAgentPrompt -> Agent.prompt -> runAgentLoop -> runLoop
 -> streamAssistantResponse -> ModelRuntime.streamSimple -> Provider.streamSimple
 -> AssistantMessageEventStream -> message_end
 -> toolCall blocks -> validate -> hook -> execute -> hook
 -> ToolResultMessage -> next streamAssistantResponse
 -> final AssistantMessage -> agent_end -> post-run retry/compaction check -> settled
```

## Streaming

```text
provider start/delta/done
 -> streamAssistantResponse mutates partial
 -> Agent.processEvents
 -> AgentSession extension event
 -> SDK listener / TUI / JSON / RPC output
 -> message_end only then SessionManager.appendMessage
```

## Compaction

```text
agent_end or pre-prompt -> _checkCompaction
 -> prepareCompaction(current branch, settings)
 -> session_before_compact
 -> compact -> serialize -> summary provider stream
 -> SessionManager.appendCompaction
 -> buildSessionContext -> Agent.state.messages replacement
 -> session_compact + compaction_end
 -> Agent.continue once only for recovery/queued work
```

## Restore / Fork / Branch

```text
SessionManager.open/continueRecent
 -> parse/migrate/index JSONL -> buildSessionContext
 -> createAgentSession restores messages/model/thinking

tree navigation -> collect abandoned entries -> optional branch summary
 -> move leaf / append branch_summary -> rebuild Agent messages

AgentSessionRuntime.fork/switch/new
 -> session_before_* -> shutdown old -> create cwd-bound services/session
 -> rebind UI/listeners -> session_start(reason)
```

## Extension Load

```text
DefaultResourceLoader.reload
 -> discover global/project/package/CLI extension paths
 -> jiti.import -> await factory(ExtensionAPI)
 -> collect handlers/tools/providers/commands
 -> createAgentSessionServices flushes provider registrations
 -> AgentSession builds ExtensionRunner and dynamic tool/prompt state
 -> session_start
```

