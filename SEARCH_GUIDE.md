# Search Guide

## Fast Path

```text
Need -> ROUTER -> kb search -> kb show/reuse -> architecture only if needed -> source only if justified
```

## Recommended Search Order

1. Run `python tools/kb.py search "<capability>"`; accept at most three candidates.
2. Follow its suggested `reuse` command, or use `show` for the 30-second judgment.
3. Run `architecture` only for module boundaries and data flow.
4. Run `status` before relying on dynamic facts; stale or unknown facts may need online verification.
5. Run `path` and inspect `source/` only when the recorded analysis is insufficient.
6. Stop after the first search when there is no high-relevance result.

## Command-line Examples

```powershell
python tools/kb.py search "heartbeat scheduler persistent goal"
python tools/kb.py search "system proxy"
python tools/kb.py reuse prime-agent "long-running agent"
```

The CLI reads the existing Markdown at invocation time. It creates no separately maintained index, database, embedding, server or knowledge graph.

Python 3.10 or newer is required. Optional local usage logging is off by default. Set `KB_USAGE_LOG=1` to append only timestamp, tool name, normalized capability keywords, matched projects and deepening state to ignored `.local/kb-usage.log`; full prompts, secrets and private code are never logged.

## Search Interpretation

- A tag match is a navigation hint, not proof that the upstream project is suitable.
- `STATUS.md` records freshness and confidence; dynamic facts may require current online verification.
- `META.md` identifies the exact commit analyzed.
- Recommendations are scoped to the documented scenario and should not be treated as upstream claims.

## When No Match Exists

Record the missing capability before external research. If a new project is found, compare it with existing entries before adding it. Building from scratch is allowed when existing options are outdated, unsafe, overbuilt, license-incompatible, or mismatched to the required scope.
