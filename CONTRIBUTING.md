# Contributing

## Admission Rules

A project should be added only when it offers a meaningful reusable implementation, architecture pattern, comparison anchor, or historical lesson. Search existing projects first. If a candidate substantially overlaps an existing entry, create or update a comparison before adding it.

## Addition Workflow

1. Check `CATALOG.md`, `TAGS.md`, and `Comparisons/` for overlap.
2. Shallow-clone the upstream repository into its local `source/` directory.
3. Record upstream URL, branch, commit, date, license, languages, and important directories in `META.md`.
4. Analyze README/docs, directory tree, configuration, entry points, core modules, then only necessary representative source.
5. Write `SUMMARY.md`, `REUSE_GUIDE.md`, and `STATUS.md`; add `ARCHITECTURE.md` for complex systems.
6. Update `CATALOG.md`, `TAGS.md`, and `ATTRIBUTION.md`.
7. Check links, unsupported claims, sensitive data, copied third-party material, and publication readiness.

## Writing Rules

- Distinguish `Fact`, `Analysis`, and `Recommendation`.
- Attach a source path or upstream documentation link to important technical facts.
- Use `Unknown` or `Needs Verification` when evidence is insufficient.
- Do not copy large portions of upstream README files, documentation, or source code.
- Keep the 30-second assessment short and decision-oriented.
- Explain both what should not be rebuilt and what remains reasonable to implement independently.

## Status Reviews

Status is commit- and date-specific. Revalidate projects when their analyzed commit changes materially, the upstream becomes archived, its license changes, a security-sensitive recommendation ages, or a major replacement becomes established.

