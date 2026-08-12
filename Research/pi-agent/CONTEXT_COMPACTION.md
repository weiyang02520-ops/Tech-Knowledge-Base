# Context Compaction

Use When:
- implementing context overflow recovery or conversation summarization
- auditing what survives compaction and whether history is recoverable

## Trigger

[Repo-confirmed] Automatic threshold compaction runs when `contextTokens > contextWindow - reserveTokens`; defaults are `reserveTokens=16384` and `keepRecentTokens=20000`. Manual `/compact` bypasses the threshold. Context-overflow errors, silent successful overflow by usage, and certain underfilled `length` stops trigger a bounded compact-and-retry recovery.

[Repo-confirmed] Threshold compaction does not retry a completed answer. Recoverable overflow/truncation removes the failed assistant from in-memory context, compacts, then continues once. A second overflow recovery is refused.

## Preparation and Cut Point

[Repo-confirmed] `prepareCompaction()` operates on the current branch. It starts at the previous compaction's kept boundary, estimates the actual projected pre-compaction context, walks backward until `keepRecentTokens`, and cuts only at user, assistant, bash, custom or summary messages—not tool results.

[Repo-confirmed] Normal cuts preserve complete recent turns. If one turn exceeds the retention budget, Pi cuts inside it at an assistant boundary, separately summarizes the early turn prefix, and retains the suffix. Tool results stay paired with their initiating assistant call in the kept segment.

## Summary Input and Output

[Repo-confirmed] Messages to summarize are converted to LLM messages and serialized as labelled transcript text. Tool result text is truncated to 2,000 characters for the summarization request. Previous summary and accumulated read/modified file lists are folded into the next summary.

[Repo-confirmed] Output is a structured checkpoint (goal, constraints, progress, decisions, next steps, critical context and file lists). The persisted `CompactionEntry` contains `summary`, `firstKeptEntryId`, `tokensBefore`, optional usage/details and whether an extension supplied it.

## Re-entry and Recovery

[Repo-confirmed] After append, `buildSessionContext()` produces: current system prompt + compaction-summary custom message + messages beginning at `firstKeptEntryId` + post-compaction messages. The summary is therefore re-entered on every later model call until superseded.

[Repo-confirmed] Original entries remain in JSONL and can be inspected or selected in the session tree. The model context is lossy; durable history is not. Extensions may cancel compaction or supply a custom result through `session_before_compact`.

## Evaluation

- `[Inference]` Strengths: bounded context, one-step overflow recovery, non-destructive history, recent-work continuity, extensible summary policy.
- `[Inference]` Weaknesses: LLM summary drift, heuristic cut/token estimates, large single-turn complexity, summary calls add cost and failure modes.
- `[Inference]` Long-term risk: repeated summaries can privilege recent coding state over older user intent. Domain products should persist structured facts separately and treat compaction as conversational continuity only.
- `[Inference]` AI Novel Studio timing: introduce after persistent multi-turn chat exists and real sessions approach model limits—likely M7—not as an M6 Reviewer prerequisite.

