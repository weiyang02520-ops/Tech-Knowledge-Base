# Overall Architecture

Use When:
- deciding package/module boundaries for an agent product
- separating UI, session persistence, tool loop and provider adapters

## Monorepo Boundary

[Repo-confirmed] Root `package.json` declares workspaces under `packages/*`. The research-relevant published packages at the pinned commit are:

| Package | Responsibility | Depends inward on |
| --- | --- | --- |
| `@earendil-works/pi-ai` | unified messages, models, provider auth, streaming adapters, usage | provider SDKs and telemetry only |
| `@earendil-works/pi-agent-core` | stateful `Agent`, low-level loop, tool execution, event protocol | `pi-ai` |
| `@earendil-works/pi-coding-agent` | coding tools, `AgentSession`, JSONL session tree, compaction, resources, extensions, CLI/TUI/JSON/RPC modes | `pi-agent-core`, `pi-ai`, `pi-tui` |
| `pi-protocol`, `pi-client`, `pi-server` | experimental transport-neutral remote sessions | protocol/client/server layers |
| `pi-tui` | terminal rendering and input | no agent-policy ownership |

[Inference] The dependency direction is the key design, not the number of packages: provider normalization does not know sessions; the loop does not know coding files; the coding host composes them.

## Runtime Composition

```text
CLI main.ts
  -> choose cwd/session + resolve project trust
  -> createAgentSessionServices()
       SettingsManager + ModelRuntime + DefaultResourceLoader
  -> createAgentSessionFromServices()
       createAgentSession()
         Agent(pi-agent-core)
         AgentSession(pi-coding-agent)
         SessionManager(JSONL/tree)
  -> createAgentSessionRuntime()
       owns replacing the active session on new/resume/fork/import
  -> InteractiveMode | print/json | RPC
```

[Repo-confirmed] `main.ts` resolves the target session cwd before loading cwd-bound settings, extensions and models. This prevents resuming a session from accidentally retaining the startup directory's runtime services.

## Core Versus Host

[Repo-confirmed] `Agent` owns `systemPrompt`, `model`, `thinkingLevel`, `tools`, `messages`, streaming state, pending tool call IDs, message queues and an active abort controller. It does not persist files, discover skills, build a coding prompt, or implement compaction.

[Repo-confirmed] `AgentSession` adds persistence listeners, input/template/skill expansion, dynamic system-prompt and tool rebuilding, extension hooks, model selection, auto retry, auto/manual compaction, bash messages, statistics and tree navigation.

[Repo-confirmed] `AgentSessionRuntime` sits one layer higher and replaces the active `AgentSession` across new-session, switch/resume, fork/clone and import. UI subscribers are session-specific and must rebind after replacement.

## Prompt Templates, Configuration and CLI

[Repo-confirmed] `DefaultResourceLoader` discovers context files, extensions, skills, prompt templates and themes. `SettingsManager` merges global and project settings, while project trust decides whether protected project resources may load. `AgentSession.prompt()` expands `/skill:name` and prompt templates before constructing the user message.

[Docs-confirmed] Interactive, print, JSON and RPC are modes over the same session/runtime layer. `[Inference]` This is genuine core/UI decoupling even though the interactive TUI remains feature-richer than headless modes.

## Architectural Trade-off

[Inference] Pi optimizes for a small reusable loop and a highly extensible local host. This yields excellent test seams and embedding options, but `AgentSession` has grown into a 3,000+ line coordinator. Its package architecture is cleaner than its largest application-service class; future adopters should copy the boundaries, not the class size.

