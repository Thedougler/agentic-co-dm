---
name: web-search
description: web-search — search-query formulation and source-evaluation craft for a Campaign OS repo (vault/ present). Use when the task is *how* to search — operator syntax, engine choice, query narrowing, source-reliability tiers. Not landing findings in canon (llm-wiki-research) or querying the wiki (llm-wiki-query).
---

# Web Search Skill

Formulates effective search queries, picks the right engine, and evaluates source reliability.
It does not execute searches or fetch results itself — pair it with `WebSearch`/`WebFetch`, or
with `llm-wiki-research` when the findings must land in canon.

## Workflow

1. **Clarify the need**: what to find, why, what's already been tried, and any constraint
   (time period, source type, language).
2. **Build the query** — start broad then narrow, try synonyms/variations, use question-based
   or source-specific framing. Pull operator syntax from
   `.claude/skills/web-search/references/search-craft.md` § Query Optimization.
3. **Pick the engine** — general web vs. a specialized engine (academic, code, data,
   AI-powered). See `.claude/skills/web-search/references/search-craft.md` § Specialized Search
   Engines.
4. **Evaluate results** with the CRAAP test (currency, relevance, authority, accuracy, purpose)
   and the source-reliability tiers in
   `.claude/skills/web-search/references/search-craft.md` § Source Evaluation.
5. **Synthesize** — cross-reference across sources; note gaps and follow-up queries.

Cannot execute real searches, access real-time results, or reach paywalled content — this
skill only shapes the query and grades what comes back.

## Reference

| Need | File |
|---|---|
| Search operators, query-formulation techniques | `.claude/skills/web-search/references/search-craft.md` § Query Optimization |
| Specialized search engines by domain | `.claude/skills/web-search/references/search-craft.md` § Specialized Search Engines |
| CRAAP test, source-reliability tiers | `.claude/skills/web-search/references/search-craft.md` § Source Evaluation |
| Strategy write-up template + worked examples | `.claude/skills/web-search/references/search-craft.md` § Output Format & Examples |
