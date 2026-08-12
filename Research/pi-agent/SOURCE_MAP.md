# Source Map

Use When:
- locating the pinned implementation without repeating repository-wide search
- verifying a conclusion at function/class level

All paths are relative to the Pi repository at `2e4d239…` unless marked Novel.

| Topic | File | Class / function | Purpose |
| --- | --- | --- | --- |
| Agent state | `packages/agent/src/agent.ts` | `Agent`, `runWithLifecycle`, `processEvents` | transcript, queues, abort, event reduction |
| Loop | `packages/agent/src/agent-loop.ts` | `runLoop`, `streamAssistantResponse`, `executeToolCalls` | model/tool iteration |
| Contracts | `packages/agent/src/types.ts` | `AgentTool`, `AgentContext`, `AgentEvent` | provider-neutral runtime types |
| Message/model | `packages/ai/src/types.ts` | `Message`, `Context`, `Model`, stream events | normalized provider boundary |
| Validation | `packages/ai/src/utils/validation.ts` | `validateToolArguments` | schema conversion/checking |
| Provider registry | `packages/ai/src/models.ts` | `Provider`, `Models`, `createProvider` | auth + dispatch + catalogs |
| Retry/overflow | `packages/ai/src/utils/retry.ts`, `overflow.ts`, `provider-retry.ts` | classifiers/retry loops | transient vs overflow policy |
| SDK factory | `packages/coding-agent/src/core/sdk.ts` | `createAgentSession` | compose runtime/session/resources |
| Host session | `.../core/agent-session.ts` | `AgentSession`, `prompt`, `_handlePostAgentRun` | persistence, hooks, retry, compaction |
| Session replacement | `.../core/agent-session-runtime.ts` | `AgentSessionRuntime` | new/switch/fork/import lifecycle |
| Durable session | `.../core/session-manager.ts` | `SessionManager`, `buildSessionContext` | JSONL append-only tree/projection |
| Compaction | `.../core/compaction/compaction.ts` | `prepareCompaction`, `compact`, `findCutPoint` | summary boundary and generation |
| Branch summary | `.../core/compaction/branch-summarization.ts` | collect/prepare/generate | preserve abandoned branch context |
| Tools | `.../core/tools/index.ts`, `bash.ts`, `read.ts`, `edit.ts`, `write.ts` | create definitions/tools | coding operations and progress |
| Extensions | `.../core/extensions/loader.ts`, `runner.ts`, `types.ts` | loader, `ExtensionRunner`, API/events | plugin lifecycle |
| Skills | `.../core/skills.ts` | `loadSkills`, `formatSkillsForPrompt` | discovery/progressive disclosure |
| Resources | `.../core/resource-loader.ts` | `DefaultResourceLoader` | settings/packages/context/prompts |
| Models | `.../core/model-runtime.ts`, `provider-composer.ts` | `ModelRuntime` | built-in/config/extension composition |
| CLI | `packages/coding-agent/src/main.ts` | `main`, `createRuntime` | cwd/trust/session/mode bootstrap |
| RPC | `.../modes/rpc/rpc-mode.ts`, `rpc-types.ts` | `runRpcMode`, `RpcCommand` | JSONL subprocess protocol |
| Official docs | `packages/coding-agent/docs/{sdk,rpc,sessions,session-format,compaction,extensions,skills,security,providers,settings}.md` | — | supported user contract |
| Novel role/runtime | `agents/types.py`, `definitions.py`, `runtime.py` | `AgentDef`, `AgentSession`, `run_agent` | in-memory Chief loop |
| Novel tools | `tools/types.py`, `registry.py`, `read_tools.py`, `write_tools.py` | `ToolRegistry` | allowlist, batch preflight, domain tools |
| Novel providers | `llm/provider.py`, `openai_compatible.py`, `types.py` | `BaseProvider` | OpenAI-compatible normalization |
| Novel Writer | `core/write_workflow.py`, `agents/planner.py`, `agents/writer.py` | `WriteWorkflow` | TaskCard/context/prose orchestration |
| Novel context | `core/context.py`, `context_budget.py` | `plan_context` | deterministic source selection |
| Novel durability | `core/generation.py`, `ai_draft.py`, `history.py`, `mutation.py` | workspaces/guards/snapshots | long generation and safe writes |

