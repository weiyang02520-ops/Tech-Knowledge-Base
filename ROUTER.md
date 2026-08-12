# KB Router

A shared, Markdown-first technical knowledge base is available at this directory. Use it only when the current task is likely to benefit from an existing open-source solution, reusable capability, architecture pattern, or prior technology comparison.

Query the KB before designing a non-trivial feature or system, selecting or integrating a framework, comparing technical approaches, or implementing general capabilities such as agents, RAG, MCP, networking, browsers, automation, databases, bots, or developer tools. If relevance is uncertain, allow one lightweight `search` and stop when it finds no high-relevance result.

Do not query for typos, prose polishing, formatting, simple renames, clearly localized bugs, small changes with an already specified implementation, explanations answerable from the current code, or unrelated ordinary tasks.

Use progressive retrieval:

1. `python tools/kb.py search "<capability>"` (maximum 3 candidates).
2. Read only the suggested `show` or `reuse` result.
3. Use `architecture` only when module boundaries are needed.
4. Inspect `source/` only when public analysis is insufficient and the recorded commit is relevant.

Soft retrieval budget: under 1,000 tokens for an ordinary lookup and under 2,500 for a typical technical task. Never preload the KB, read unrelated projects for safety, or repeat the same retrieval in one task unless the requirement changes or a deeper layer is justified.

