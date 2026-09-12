---
name: llm-wiki
description: >-
  The knowledge-base pattern layer of a Campaign OS repo (vault/ present). Use when the user
  says "LLM wiki"/"Karpathy wiki", asks why the system "compiles instead of retrieves", asks
  what `tier:`/`summary:`/the retrieval ladder mean, or asks which skill ingests/queries/lints
  wiki content. Not for a specific fact lookup (llm-wiki-query) or whole-system architecture
  (campaign-os).
---

# llm-wiki

Campaign OS is a domain specialization of Andrej Karpathy's **LLM Wiki**
pattern: *compile, don't retrieve*. Knowledge is distilled **once** — at
INGEST time — into maintained `vault/` pages (including `vault/campaigns/shattered-sea/pcs/`) and kept current,
never recalled from chat memory (drifts) nor re-derived from raw transcripts
per query (RAG). One grep hits pre-synthesized, canon-tiered content. The full
theory — source/credit, the chat-memory/RAG/compile comparison, layer mapping,
`tier:`/`summary:` mechanics, provenance, what was deliberately declined —
lives in [`references/pattern.md`](references/pattern.md).

## The retrieval-primitive ladder (single source of truth — every read-side skill follows this)

**Use the cheapest primitive that answers the question; escalate only when it
can't.** Law L1 ("grep, don't remember") made mechanical — and the operational
spine of the `llm-wiki-query` skill.

| Need | Primitive | Cost |
|---|---|---|
| Does a page exist? Its type/status/tags? | grep the `^---` frontmatter block | **cheapest** |
| 1-sentence preview | Read the page's `summary:` field (W89 lints it present on every page) | **cheap** |
| A specific fact or section | `grep -A<n> -B<n> "<term>" <file>` — matched lines + context only | **medium** |
| Whole-page content | `Read <file>` | **expensive — last resort** |
| Relationships across pages | grep `\[\[.*\]\]` across a type dir, or walk wikilinks | case-by-case |

A 500-line page opened to read 15 lines is 485 lines of wasted budget.

## Router — which skill owns the operation

Never perform these inline; each verb has exactly one owner (diffuse
authorship is failure mode #6):

| You are about to... | Owner |
|---|---|
| Ingest a non-transcript source (book, doc, legacy export) | `llm-wiki-ingest` |
| Ingest a session transcript | `transcript-label`, then `transcript-ingest` |
| Find or answer anything from the wiki | `llm-wiki-query` (off-thread lookup: `wiki-researcher` agent) |
| Bulk health/lint sweep (W1–W27) | `llm-wiki-lint` |
| Audit, normalize, or extend the tag vocabulary — or resolve a W13/W27 finding | `tag-taxonomy` |
| Resolve a contradiction or duplicate-page merge | `canon-review` (evidence-settled contradictions close autonomously same turn; merges + genuine splits are human-gated) |
| Report pipeline status — un-ingested sessions, missing `summary:`/`tier:`, `tier: core` promotion candidates | `llm-wiki-status` |
| Package a token-bounded canon slice for a consumer (briefing pack, subagent input) | `llm-wiki-context-pack` |
| Research real-world material on the web and file it for prep | `llm-wiki-research` (files via `find-guidelines` / prep skills) |
| Author a page of an existing type | the type's `<type>-prep` skill (`.claude/rules/skills.md` § Directory scoping) |
| Create a content type with no template | `content-type-scaffold` |
| Session loop, publishing, hooks/levers, whole-system architecture | `campaign-os` |

Structural equivalents, for anyone arriving from a generic LLM-wiki mental
model: the operation log is `git log` — never a standing log file (a stale
ledger reads as settled fact); there is no raw/rebuild verb — canon is
promoted in place (`status: pending` → `canon`) and git is the history.

## References

| Question | Read |
|---|---|
| Why compile-don't-retrieve; layer mapping; `tier:`/`summary:` mechanics; provenance; declined mechanisms; six-laws mapping | [`references/pattern.md`](references/pattern.md) |
