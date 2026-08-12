---
project_name: "Skills for Real Engineers"
upstream_repository: "mattpocock/skills"
github_url: "https://github.com/mattpocock/skills"
author_or_organization: "Matt Pocock and contributors"
default_branch: "main"
analyzed_commit: "84fdeffd12f2ee307994d1eb6feb48173b6e0502"
analysis_date: "2026-08-09"
license: "MIT"
main_languages: ["Markdown", "Shell", "JavaScript"]
main_technologies: ["Agent Skills", "subagents", "issue trackers", "ADRs", "domain glossary", "TDD", "handoff documents"]
project_status: "Active, with stable and in-progress skill groups"
tags: ["grill-me", "requirements", "spec", "tickets", "tdd", "bug-diagnosis", "code-review", "architecture", "domain-modeling", "handoff", "research", "merge-conflict", "long-task-planning"]
possible_reuse_areas: ["requirements interrogation", "domain vocabulary", "test seams", "feedback-loop debugging", "two-axis review", "agent handoff", "agent-oriented writing"]
---

# Metadata

## Documentation Location

- Overview and inventory: `source/README.md`
- Engineering skills: `source/skills/engineering/`
- Productivity skills: `source/skills/productivity/`
- Miscellaneous setup skills: `source/skills/misc/`
- Explicitly unfinished work: `source/skills/in-progress/`

## Important Directories

| Directory | Role |
| --- | --- |
| `skills/engineering/` | Design, spec, tickets, TDD, debugging, review, architecture and delivery workflows. |
| `skills/productivity/` | Grilling, handoff, teaching, questionnaires and writing for agents. |
| `skills/misc/` | Specific setup and migration helpers. |
| `skills/in-progress/` | Work explicitly not presented as mature default material. |
| `scripts/` | Supporting scripts; not executed in this analysis. |

## Repository Size at Analysis

- `SKILL.md` files found: 35
- Tracked files: 151
- Local shallow-clone size: approximately 1.0 MB including Git metadata
- Worktree state after clone: clean

## Analysis Scope

Inspected the complete inventory and read representative skills covering grilling, spec synthesis, implementation, TDD, bug diagnosis, code review, domain modeling, research, handoff and agent-oriented writing. No Skill, script, hook, installer, issue-tracker write or subagent workflow was executed.

## Verification Notes

**Fact:** The repository is MIT licensed. Several workflows are deliberately user-invoked, some assume subagents or an issue tracker, and `skills/in-progress/` is explicitly separated.

**Recommendation:** Reuse the reasoning patterns selectively. Remove assumptions about commands, subagents, issue trackers and temporary handoff locations when adapting to a universal Markdown knowledge base.

