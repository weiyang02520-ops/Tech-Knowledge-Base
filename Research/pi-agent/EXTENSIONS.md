# Extensions

Use When:
- designing hooks, plugins, dynamic tools/providers or custom UI
- assessing plugin isolation and failure behavior

## Loading and Lifecycle

[Repo-confirmed] Extensions are `.ts`/`.js` factories loaded through `jiti` from global/project directories, explicit paths or Pi packages. Discovery checks direct files and one-level directories with `index` or manifest entries. Async factories are awaited before session startup.

[Repo-confirmed] Factories receive `ExtensionAPI`. They may register event handlers, tools, commands, shortcuts, flags, message/entry renderers, Markdown transforms and providers; send messages; persist custom entries; execute commands; change active tools/model/thinking; and use a shared event bus.

[Repo-confirmed] Hooks cover project trust, resource discovery, session start/switch/fork/compact/tree/shutdown, input, context, provider request/headers/response, agent/turn/message/tool lifecycle, model/thinking selection and user bash.

## Mutation Surface

[Repo-confirmed] Extensions can add/override tools, alter per-turn system prompts, transform messages/context, block or modify tool calls/results, add commands/TUI, persist state and register providers. Tool registration after startup refreshes the current registry immediately.

## Isolation and Errors

[Repo-confirmed] Extensions are not isolated: they execute in-process with full user permissions. Loading errors are collected as diagnostics. Most event-handler exceptions are caught, reported to error listeners and iteration continues; tool hooks can deliberately block/fail execution. A stale-runtime guard invalidates captured contexts after session replacement/reload.

[Inference] One broken handler usually does not crash the agent, but arbitrary extension code can still block the event loop, mutate external state or terminate the process. API breadth is high and stability cost follows; Pi mitigates lifecycle misuse more than security risk.

## Recommendation for AI Novel Studio

[Inference] Use this as a Post-MVP plugin reference, not an immediate implementation. Start with typed domain extension points (context source, exporter, provider adapter, review rule) and explicit permissions. Do not expose raw session internals, arbitrary shell execution or UI replacement in the first plugin API.

