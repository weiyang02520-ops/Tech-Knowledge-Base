# Context Management

Use When:
- budgeting model context or diagnosing overflow
- deciding whether deterministic selection and conversational compaction should coexist

[Repo-confirmed] `AgentContext` contains the current system prompt, `AgentMessage[]` and active tools. Before every LLM call the loop may run extension `context` transforms, then `convertToLlm()` removes host-only message types and normalizes images. Provider adapters receive only the uniform `Context`.

[Repo-confirmed] Durable history and active context are separate. `SessionManager.buildSessionContext()` walks the current leaf path, applies the latest compaction boundary, converts custom/summary entries and returns messages plus effective model/thinking settings.

[Repo-confirmed] `estimateContextTokens()` trusts the last valid assistant usage (`input + output + cacheRead + cacheWrite`) and adds heuristic estimates for trailing messages. Without usage it estimates every message; text is conservatively approximated and images count as a fixed character equivalent. Immediately after compaction, UI context usage is intentionally unknown until a new assistant response supplies post-compaction usage.

[Repo-confirmed] Context-window differences live on `Model.contextWindow`; output capacity lives on `Model.maxTokens`. Compaction threshold is calculated against the selected model each time, and overflow from an old model is ignored after switching providers/models.

[Inference] Pi manages conversational growth, not domain relevance. AI Novel Studio's `ContextBudgetPlan` selects chapter outlines, rules, characters, world and recent text by deterministic priority before a Writer call. The correct future design is two-stage: domain context selection first, persisted conversational projection/compaction second. Replacing the current plan with generic summarization would weaken provenance and reproducibility.

## System Prompt and Tools

[Repo-confirmed] The base system prompt is rebuilt from cwd, context files, visible skill metadata, selected tools, tool-specific snippets and appended prompts. `before_agent_start` may override it for one turn. `prepareNextTurnWithContext` refreshes prompt, tools, model and thinking between tool rounds, so dynamic tool registration is visible without restarting the session.

## Known Boundaries

[Inference] Heuristic token estimation is deliberately approximate; provider usage arrives only after a response, so preflight cannot be exact. A provider may silently truncate in ways Pi cannot identify. Compaction summaries are lossy and can accumulate semantic drift, while the append-only log preserves auditability but does not make the model remember omitted facts.

