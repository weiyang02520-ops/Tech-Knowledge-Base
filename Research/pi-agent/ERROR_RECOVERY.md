# Error, Retry and Cancellation

Use When:
- defining provider/tool failure policy, Ctrl+C semantics or overflow recovery
- auditing whether errors remain observable and safe

| Failure | Pi behavior |
| --- | --- |
| Provider/transport transient | `[Repo-confirmed]` normalized error assistant message; outer session retry classifies 429/5xx/network/stream failures and uses bounded exponential backoff |
| SDK/provider internal retry | `[Repo-confirmed]` 408/409/429/5xx and transport errors may retry with server delay or jittered exponential delay; sleep is abortable and long requested delays are capped |
| Quota/billing | `[Repo-confirmed]` patterns explicitly exclude these from retry |
| Context overflow | `[Repo-confirmed]` excluded from generic retry; compact and continue at most once |
| Malformed/unknown tool call | `[Repo-confirmed]` error `ToolResultMessage`; model can repair |
| Tool exception | `[Repo-confirmed]` caught and returned with `isError=true`; loop continues |
| Truncated tool arguments | `[Repo-confirmed]` none execute; synthetic error results request reissue |
| Ctrl+C/abort | `[Repo-confirmed]` abort retry, signal provider/tools, wait for idle; TUI signal layer may escalate shutdown |
| Stream disconnect | `[Repo-confirmed]` normalized provider error; transient text patterns can retry; a finalized partial/error remains observable |
| Timeout/rate limit | `[Repo-confirmed]` provider-level and session-level bounded retry settings; cancellation interrupts backoff |
| Compaction failure | `[Repo-confirmed]` emits `compaction_end` with error and does not corrupt/delete history |
| Extension handler error | `[Repo-confirmed]` diagnostic/error event; ordinary hook iteration continues |

[Repo-confirmed] `Agent.runWithLifecycle()` converts uncaught failures to a synthetic assistant message with empty content, provider/model metadata, zero usage and `stopReason` error/aborted. Event listeners are awaited; idle is reached only after final listeners settle.

[Inference] Pi has two retry layers (provider request and agent-turn retry). This improves resilience but can multiply attempts, latency and cost; settings and events are necessary for visibility. AI Novel Studio should keep provider retry metadata but implement one explicit orchestration budget before adding automatic turn replay, especially for mutations or long Writer generations.

[Inference] AI Novel Studio's Writer behavior is domain-appropriate: no-output provider failure is hard; partial-output failure preserves a resumable non-canonical file; only complete/truncated validated output can enter the canonical AI draft through revision and snapshot guards.

