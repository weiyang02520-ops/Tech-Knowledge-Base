---
project_name: "Prime Agent"
upstream_repository: "PrimeIntellect-ai/prime-agent"
github_url: "https://github.com/PrimeIntellect-ai/prime-agent"
author_or_organization: "Prime Intellect and contributors"
default_branch: "main"
analyzed_commit: "a18809e00ea30638584d87b3afea7285a9d7296c"
analysis_date: "2026-08-09"
license: "MIT"
main_languages: ["TypeScript", "Python", "JavaScript", "Shell"]
main_technologies: ["Node.js", "TypeScript", "IPython", "daemon", "JSONL", "RLM", "TUI", "RPC", "Agent Skills"]
project_status: "Active, fast-moving, pre-1.0"
tags: ["agent", "long-running-agent", "subagent", "daemon", "heartbeat", "scheduler", "persistent-goal", "context-compaction", "context-persistence", "autonomous-mode", "skills", "session-resume"]
possible_reuse_areas: ["agent lifecycle", "persistent sessions", "subagent orchestration", "scheduled prompts", "goal continuation", "context compaction", "client-runtime separation"]
---

# Metadata

## Documentation Location

- Project overview: `source/README.md`
- Main documentation: `source/packages/coding-agent/docs/`
- Architecture overview: `source/packages/coding-agent/docs/architecture.md`
- Long-running behavior: `source/packages/coding-agent/docs/long-running-agents.md`
- RLM model: `source/packages/coding-agent/docs/rlm.md`

## Important Directories

| Directory | Responsibility |
| --- | --- |
| `packages/coding-agent/` | Main CLI/TUI modes, sessions, daemon, RLM host, skills and persistence. |
| `packages/agent/` | Agent abstraction and model loop foundation. |
| `packages/ai/` | Model providers, model registry and AI transport concerns. |
| `packages/tui/` | Terminal UI primitives. |
| `prime-agent-runtime/` | Python RLM harness and model-facing skill helpers. |
| `scripts/` | Build, release and installer support; not executed in this analysis. |

## Repository Size at Analysis

- Package version in root manifest: `0.7.1`
- Tracked files: 1,134
- Local shallow-clone size: approximately 27 MB including Git metadata
- Worktree state after clone: clean

## Analysis Scope

Read the overview, architecture, long-running-agent and RLM documentation; inspected workspace manifests, package boundaries, daemon/core file map, bundled skill names and representative runtime entry points. No installer, runtime, test, daemon, Python kernel, script or model request was executed.

## Verification Notes

**Fact:** The repository is MIT licensed, actively changing, and below version 1.0 at the analyzed commit.

**Analysis:** Documentation and code organization strongly support the described architecture, but rapid releases mean exact APIs and file paths should be revalidated before direct integration.

