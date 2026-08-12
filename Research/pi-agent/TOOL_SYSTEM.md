# Tool System

Use When:
- designing schemas, dispatch, progress streaming, cancellation or tool safety
- comparing open local-agent tools with domain-constrained tools

## Contract and Registry

[Repo-confirmed] `AgentTool` extends the `pi-ai` tool schema (`name`, description, TypeBox parameters) with label, async `execute(toolCallId, params, signal, onUpdate)`, optional argument preparation and sequential/parallel mode. A final result carries text/image content, arbitrary details, optional usage, newly added tool names and an optional termination hint.

[Repo-confirmed] Default active coding tools are `read`, `bash`, `edit`, `write`. Additional built-ins `grep`, `find`, `ls` exist and can be selected. `AgentSession` merges built-ins, SDK custom tools and extension tools into a dynamic map; extension registration refreshes tools immediately.

## Dispatch

[Repo-confirmed] `prepareToolCall()` finds the active tool, applies compatibility argument preparation, clones/coerces/validates arguments using TypeBox/JSON Schema, then runs the `beforeToolCall` hook. A block produces an error result without execution.

[Repo-confirmed] `execute()` is awaited and receives the active `AbortSignal`. `onUpdate` emits `tool_execution_update`; updates after promise settlement are ignored. Thrown errors become error results. `afterToolCall` may patch content/details/usage/error state. Results become `ToolResultMessage` with the original call id/name and are fed to the next model call.

[Repo-confirmed] Tool batches can run concurrently. A batch terminates the agent only when every finalized result requests termination. Output truncation utilities and temp-file spill keep shell output bounded.

## Safety Boundary

[Repo-confirmed] Built-in path resolution accepts relative or absolute paths and expands home paths. It does not confine access to cwd. Bash spawns the configured shell in cwd, inherits process authority, supports optional timeout and kills the process tree on abort.

[Docs-confirmed] Pi has no built-in sandbox. Project trust gates automatic loading of local settings/extensions/skills; it does not restrict model-requested tool actions. OS containers, VMs or policy-controlled execution are the recommended isolation boundary.

[Inference] This is a deliberate coding-agent trade: general power with honest trust semantics. AI Novel Studio should retain `ProjectStore.safe_path`, role tool allowlists, revision hashes, mutation snapshots and no general shell tool. Its current registry also preflights a complete batch and forbids unsafe read/write mixing; that domain policy is stronger than Pi's default.

## Malformed Calls and Cancellation

[Repo-confirmed] Unknown tool, schema failure, blocked hook and tool exception are returned to the model as repairable tool errors. A `length`-truncated assistant message causes every contained tool call to fail without execution. Abort propagates to tools, providers and retry sleeps; tools must cooperate with the signal.

