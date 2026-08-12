# Publication Audit

## Verdict

**Content readiness:** Ready for public review and repository publication, including the Phase 2 lightweight retrieval layer.

**Open-source readiness:** Not complete until the owner selects and adds the final license. Without a `LICENSE` file, others do not receive a standard permission grant for the original knowledge-base content.

**Git safety of local sources:** Pass. All five `source/` directories are ignored by `Tech-Knowledge-Base/.gitignore` through `**/source/` and were independently verified with `git check-ignore` and `git status --ignored`.

## Audit Scope

- Audit date: 2026-08-09
- Public files checked: 54
- Public Markdown files checked: 50
- Public Markdown lines at audit: 2,190
- Upstream repositories: 5 shallow clones pinned in their `META.md`
- Upstream projects installed or executed: No
- Remote repository created or pushed: No

## Required File Check

Pass. The repository contains all required global documents, five project metadata/summary/reuse/status sets, two architecture maps, five templates, the Skills comparison, `ROUTER.md`, the cross-platform Python CLI, four adapters and automated Router/CLI tests. No expected project document is missing.

## Source Exclusion Check

Pass for Git publication.

```text
**/source/
```

Git reports each local source directory as ignored:

- `Network/fanqiang/source/`
- `AI-Agent/prime-agent/source/`
- `AI-Engineering/addyosmani-agent-skills/source/`
- `AI-Engineering/mattpocock-skills/source/`
- `Browser/ladybird/source/`

**Residual operational warning:** `.gitignore` protects Git staging and push. It does not remove source from a manual ZIP, cloud-sync folder or drag-and-drop upload. Use Git-based publication or explicitly exclude `source/` when making archives.

## Provenance and Copyright Check

Pass with one documented residual risk.

- Every project records upstream repository, branch, analyzed commit, date and license status.
- `ATTRIBUTION.md` identifies all five third-party projects.
- Public documents contain independent summaries, analysis, architecture maps and recommendations rather than copied upstream README or source sections.
- Third-party source and binary assets are not part of the public Git content.
- `fanqiang` has no identified repository-wide standard license. This is recorded as `Unknown`; its source and assets must remain excluded. Independent factual analysis and links may be published, but a legal review is prudent if future revisions add quotations, screenshots or copied configuration.

## License Check

Blocked by owner decision, intentionally.

- No final knowledge-base license has been selected.
- Recommended content choices are `CC BY 4.0` or `CC BY-SA 4.0`.
- If substantive scripts are added later, MIT or Apache-2.0 can be applied separately to code.
- Upstream licenses do not determine the license for original analysis and do not permit relicensing upstream material.

See `LICENSE-RECOMMENDATION.md`. Do not add a final `LICENSE` without owner confirmation.

## Sensitive Information Check

Pass for the public document set.

- No API-key assignment, password assignment, token assignment, common private-key header, GitHub token pattern or OpenAI-style secret pattern was found.
- No local absolute source path is used as required knowledge.
- Public adapters use `<KB_ROOT>` or `%USERPROFILE%` rather than publishing the tested user's absolute home path. Exact machine paths and backup names remain in ignored `.local/INSTALLATION_REPORT.md`.
- Public documents mention credentials only as security concepts or redaction rules.
- Upstream repositories were not included in the public scan because they are excluded from publication; their contents must not be copied into the public tree.

## Link and Structure Check

Pass.

- Broken relative Markdown links: 0
- Missing required project files: 0
- Missing required `META.md` fields: 0
- Exact duplicated prose blocks of 100 or more normalized characters: 0
- Project navigation is available by catalog, tags, summary, reuse guide, architecture and status.

External websites remain dynamic. Repository URLs were reachable during analysis, but external download, service, proxy and product links are never treated as permanently verified.

## Staleness Check

Pass with explicit revalidation requirements.

- Every analysis is bound to a commit and date.
- `STATUS.md` separates current evidence from recommendations and defines revalidation triggers.
- `fanqiang` marks old and dynamic material rather than presenting every tutorial as current.
- Ladybird is identified as pre-alpha; its partly aspirational process document is not treated as complete implementation fact.
- Both Skills repositories are identified as new and fast-changing.

## Cross-AI Compatibility Check

Pass.

- Core knowledge uses ordinary Markdown, YAML front matter, relative links, tables and text diagrams.
- The CLI uses Python 3.10+ standard library only; no Codex SDK, Claude API, application connector, embedding service or private plugin is required.
- Tool-specific adapters contain only short entry behavior, never knowledge content.
- Codex 0.144.5 and Claude Code 2.1.224 were installed through verified persistent instruction files after backups. Trae CN 3.3.86, TRAE SOLO CN 0.1.7 and WorkBuddy 5.0.2 were detected, but their stable file-level rule mechanisms were not verified, so no guessed configuration was written and manual setup instructions were produced.

## Phase 2 Retrieval Check

Pass.

- Router acceptance: 20/20 correct decisions, 0 false triggers, 0 misses.
- Automated suite: 14/14 tests passed on Python 3.14.4.
- Commands verified: `search`, `show`, `reuse`, `architecture`, `path`, `status`, plus Router simulation and the Windows wrapper.
- Search returns at most three candidates, provides match reasons and a next command, and says source dive is not needed yet.
- Bilingual aliases were verified for background/long-running tasks, subagents and system/network proxy.
- Unknown projects, empty capabilities and unavailable architecture documents produce human-readable errors without tracebacks.
- No-match search stops retrieval instead of scanning unrelated projects.
- Optional local logging records normalized keywords rather than full prompts and is ignored by Git.

At audit time, all public Markdown contained approximately 86,519 characters. A representative search returned 234 characters; search plus a relevant reuse section returned 506 characters, about 0.6% of the full Markdown character volume. Exact model tokenization varies, but this indicates roughly 99% less retrieved context than preloading the knowledge base. The installed always-on adapter rule is 565 characters in its portable form.

## Scale Check

Pass for 100+ projects with a known maintenance threshold.

- One project per directory limits merge conflict and cognitive load.
- Fixed templates keep records comparable.
- Categories remain shallow; tags and comparisons handle cross-domain discovery.
- `source/` remains local and does not inflate the public repository.
- Markdown remains usable without a database, server or build step.

At roughly 50-100 projects, measure search misses, false matches and command latency. SQLite FTS becomes worthwhile only when Markdown scanning is measurably slow or keyword ranking degrades. Consider MCP only when multiple tools cannot reliably invoke the local CLI. Consider embeddings/RAG only after aliases and FTS demonstrably fail on a substantially larger collection. Markdown must remain the authoritative readable source.

## Publication Blockers

1. Select and add the final license.
2. When publication is authorized, initialize or create the dedicated GitHub repository and verify the staged file list contains no `source/` paths.

No remote repository, push or release was created during this work.

## Recommended Pre-push Gate

```powershell
git status --short
git check-ignore -v -- */*/source/README.md
git ls-files | rg '(^|/)source/'
```

The final command must produce no output. Review the complete staged diff before the first push.
