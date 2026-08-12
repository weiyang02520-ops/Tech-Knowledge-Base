---
project_name: "Agent Skills"
upstream_repository: "addyosmani/agent-skills"
github_url: "https://github.com/addyosmani/agent-skills"
author_or_organization: "Addy Osmani and contributors"
default_branch: "main"
analyzed_commit: "7676817c12a1317454ae3898a0c5c1eacf5dd3d5"
analysis_date: "2026-08-09"
license: "MIT"
main_languages: ["Markdown", "JavaScript", "Shell", "Python"]
main_technologies: ["Agent Skills", "Claude plugins", "Codex plugins", "slash commands", "AI coding agents", "evaluation fixtures"]
project_status: "Active"
tags: ["spec", "planning", "incremental-development", "tdd", "debugging", "code-review", "security", "api-design", "frontend", "context-engineering", "git-workflow", "ci-cd", "documentation", "deployment"]
possible_reuse_areas: ["software lifecycle workflow", "verification gates", "agent context design", "cross-tool skill packaging", "review checklists"]
---

# Metadata

## Documentation Location

- Overview and lifecycle map: `source/README.md`
- Skills: `source/skills/*/SKILL.md`
- Shared checklists: `source/references/`
- Cross-tool setup: `source/docs/`
- Commands and personas: `source/commands/`, `source/agents/`
- Evaluations: `source/evals/`

## Important Directories

| Directory | Role |
| --- | --- |
| `skills/` | 24 workflow skills in a flat, discoverable namespace. |
| `references/` | Shared Definition of Done, testing, security, performance, accessibility and orchestration checklists. |
| `commands/` | Lifecycle slash-command entry points. |
| `agents/` | Review personas such as reviewer, tester and security auditor. |
| `docs/` | Adoption and tool-specific setup. |
| `.claude*`, `.codex-plugin`, `.gemini`, `.opencode` | Packaging adapters; not the core knowledge source. |

## Repository Size at Analysis

- Skills found: 24
- Tracked files: 184
- Local shallow-clone size: approximately 1.2 MB including Git metadata
- Worktree state after clone: clean

## Analysis Scope

Read the lifecycle overview and representative skills for routing, specification, planning, TDD, debugging, review and context engineering; inspected the complete skill inventory and tool adapters. No installer, hook, command, evaluation or script was executed.

## Verification Notes

**Fact:** The repository is MIT licensed and explicitly supports multiple AI coding tools. Some individual skills reference shared files outside their own directories; upstream documents this per-skill portability gap.

**Recommendation:** Extract workflows and evidence gates as ordinary engineering guidance. Do not assume that installing all 24 skills is necessary or that every tool supports the same invocation semantics.

