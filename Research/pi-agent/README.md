# Pi Coding Agent 深度架构研究

Use When:
- 需要定位 Pi 的 Agent Runtime、Session、Compaction、Tools、Extensions、Skills、Provider 或 SDK/RPC 设计
- 评估 AI Novel Studio 的会话、上下文、插件和多角色架构

## Research Metadata

| Field | Value |
| --- | --- |
| Project | Pi coding agent / pi monorepo |
| Official repository | https://github.com/badlogic/pi-mono （GitHub 页面现重定向至 earendil-works/pi） |
| Research commit SHA | `2e4d23959485279aa2da1a45103de2ea22d46395` |
| Research date | 2026-08-12 |
| Analysis type | Static source and official-doc analysis |
| Execution | Upstream code not executed; only `git ls-remote`, shallow clone and text inspection |
| License | MIT, copyright Mario Zechner |
| Primary language | TypeScript; Node.js >= 22.19 |
| AI Novel Studio snapshot | `877c6edf09b29628fa4cfa7dac757d0dbba1ffed` plus explicitly identified uncommitted workspace changes |

## Evidence Labels

- `[Repo-confirmed]`: the pinned source or tests directly establish the claim.
- `[Docs-confirmed]`: official Pi documentation states the claim; source was not required or not fully traced.
- `[Inference]`: an architectural judgment derived from the pinned implementation. It is not presented as upstream intent.

All unlabelled tables in this directory are source maps or summaries of adjacent labelled findings.

## Executive Conclusion

[Repo-confirmed] Pi is not one monolithic `AgentSession`. Its reusable center is a layered composition: `pi-ai` normalizes provider messages and streams; `pi-agent-core` owns mutable agent state and the tool loop; `pi-coding-agent` adds persisted tree sessions, compaction, resources, extensions, CLI modes and SDK factories. `AgentSession` is an application service around `Agent`, not the fundamental loop itself.

[Inference] The most reusable lesson for AI Novel Studio is not “copy Pi.” It is to preserve the current domain workflow while separating three concepts now partly conflated: a provider-neutral turn runtime, a persisted conversation/session log, and domain workflows such as Chief → TaskCard → Writer → Draft. Shared Runtime + immutable `AgentDef`-like role definitions is sufficient for Chief/Writer/Reviewer; a general multi-agent framework is not yet justified.

[Repo-confirmed] Pi's session format is append-only JSONL with parent-linked entries. Compaction changes the active projection, not the historical log. That is substantially more recoverable than destructive message trimming. `[Inference]` AI Novel Studio should adopt the principle when persistent chat arrives, but should not use conversation compaction as a substitute for its existing deterministic Writer `ContextBudgetPlan`.

[Repo-confirmed] Pi deliberately has no built-in sandbox. Project trust gates loading project resources, while tools and extensions retain the process user's filesystem and shell authority. `[Inference]` This is inappropriate as the default safety model for a novel editor, whose constrained project store, revision guards, snapshots and role-specific tool allowlists are stronger product boundaries.

## Navigation

| Question | Read |
| --- | --- |
| Packages, boundaries, minimal core | [ARCHITECTURE.md](ARCHITECTURE.md), [DESIGN_PRINCIPLES.md](DESIGN_PRINCIPLES.md) |
| Exact user → model → tool loop | [AGENT_RUNTIME.md](AGENT_RUNTIME.md), [CALL_CHAINS.md](CALL_CHAINS.md) |
| Session state, JSONL, resume/fork/tree | [SESSION.md](SESSION.md) |
| Context projection and budgets | [CONTEXT_MANAGEMENT.md](CONTEXT_MANAGEMENT.md) |
| Trigger, cut point, summary, recovery | [CONTEXT_COMPACTION.md](CONTEXT_COMPACTION.md) |
| Tool schema, execution, safety | [TOOL_SYSTEM.md](TOOL_SYSTEM.md) |
| Models, auth, providers | [PROVIDER_LAYER.md](PROVIDER_LAYER.md) |
| Stream protocols and UI delivery | [STREAMING.md](STREAMING.md) |
| Hooks and plugin surface | [EXTENSIONS.md](EXTENSIONS.md) |
| Progressive-disclosure skills | [SKILLS.md](SKILLS.md) |
| Embedding and subprocess control | [SDK_RPC.md](SDK_RPC.md) |
| Errors, retry, abort | [ERROR_RECOVERY.md](ERROR_RECOVERY.md) |
| Tests and seams | [TESTING.md](TESTING.md) |
| Fast source lookup | [SOURCE_MAP.md](SOURCE_MAP.md) |
| Pi vs AI Novel Studio | [AI_NOVEL_STUDIO_COMPARISON.md](AI_NOVEL_STUDIO_COMPARISON.md) |
| Adoption decisions | [AI_NOVEL_STUDIO_LESSONS.md](AI_NOVEL_STUDIO_LESSONS.md) |

## Coverage Checklist

The research covers: overall architecture; runtime; session; model/provider; message model; tool system and loop; streaming; context and compaction; persistence, resume, fork and branch; extensions; skills; prompt templates; events/hooks; SDK; RPC; CLI; errors; cancellation; retry; usage; configuration; security; file/shell safety; testing; package boundaries; extensibility and minimal-core philosophy. Small modules are routed to the relevant focused file rather than omitted.

