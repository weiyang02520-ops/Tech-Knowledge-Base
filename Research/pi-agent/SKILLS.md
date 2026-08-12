# Skills

Use When:
- implementing on-demand knowledge/instruction loading
- deciding whether a capability should be code or declarative guidance

## Skill Versus Extension

[Repo-confirmed] A skill is Markdown instructions plus optional scripts/references/assets. It is discovered and disclosed to the model; it does not receive runtime hooks. An extension is executable in-process code with registration and lifecycle APIs. Skills guide model behavior; extensions alter host behavior.

## Discovery and Loading

[Repo-confirmed] Pi scans global, project, `.agents/skills`, packages, settings and CLI paths. Direct root Markdown and recursive `SKILL.md` rules vary by location. It parses frontmatter into `name`, `description`, file path, base directory, source metadata and `disable-model-invocation`.

[Repo-confirmed] Missing descriptions prevent loading; most naming/spec violations produce warnings. Name collisions keep the first discovered skill and emit diagnostics.

## Progressive Disclosure

[Repo-confirmed] The system prompt contains only visible skill name, description and location in XML, plus instructions to use `read` when a task matches. Full skill content is not automatically placed in context. `/skill:name` explicitly reads the file in the host and injects its body; normal invocation depends on the model matching the description and choosing `read`.

[Repo-confirmed] `disable-model-invocation: true` hides a skill from the model list while keeping explicit slash invocation. Relative references resolve against the skill directory.

## Tech-Knowledge-Base Decision

[Inference] Yes—the progressive-disclosure mechanism fits Tech-Knowledge-Base, but the unit should be a small router skill plus `Use When` metadata in focused documents, not one skill per research file and not wholesale injection. The router should return 1–3 relevant documents; the model reads those files on demand. This matches the present `kb.py search/reuse` design.

[Inference] Do not let descriptions alone become the authoritative taxonomy. Keep `CATALOG.md`/`TAGS.md` machine-readable enough for deterministic retrieval, use skills only as entry instructions, and never auto-load the entire Pi research for unrelated AI Novel Studio work.

