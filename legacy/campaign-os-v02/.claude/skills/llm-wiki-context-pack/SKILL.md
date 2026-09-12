---
name: llm-wiki-context-pack
description: Package a token-bounded, read-only slice of canon for a downstream consumer, in a Campaign OS repo (vault/ present). Use for a "briefing pack", "context pack", "everything relevant to X in one block", a named token budget, or a subagent dispatch needing canon input. Renders in-conversation only. Not llm-wiki-query or draft-run-guide.
---

# llm-wiki-context-pack

Read-only: the pack is a
rendered snapshot in the conversation (or a subagent prompt) — never a repo
file (an unowned derived file is ledger rot; re-render instead of reusing a
stale pack).

Turns "everything relevant to X, under N tokens" into a deterministic
selection over the retrieval-ladder rungs the wiki already maintains
(`summary:`, `tier:`) — instead of ad-hoc full-page reads and hand-rolled
budget math.

## Inputs

Topic (an entity, place, thread, or "the party's current situation"), and a
budget (default 8000 tokens, cap 50000). Token estimate: `chars / 4` —
the shared constant `llm-wiki-status`'s footprint check also uses.

## Steps

1. **Relevance pass — frontmatter only, no bodies.** Candidates
   score: topic matches title/`aliases:` frontmatter +5 ·
   shared tag +3 · topic term in `summary:` +2 · named in the topic page's
   own wikilinks +2. Unknown
   vocabulary → one `npm run search:content -- query "<topic>"` pass, +4 per
   semantic hit.
2. **Tier-aware selection.** Order candidates by score bucket, and within a
   bucket `tier: core` → `supporting` → `peripheral` (absent ⇒ supporting).
3. **Compress each selected page.** Always keep: title, `status:`, `tier:`,
   `summary:`. Body: strip frontmatter, `## Sources`-style footers, empty
   headings, and any fact already included from another page — replace the
   duplicate with `(see [[page]])`. Never rewrite a kept fact's wording.
4. **Fill to budget, greedily, in the order from step 2.** Running
   `chars/4` count; a page that would overflow gets its summary block only
   (title + `summary:` + status line); `peripheral` drops first. Track what
   was dropped.
5. **Render one block** with a header: topic · budget · actual estimate ·
   pages included (wikilinked) · pages dropped. `PACK: <topic> — <actual>/
   <budget> tokens, <n> pages, <m> dropped`.

## Craft packs

Topic `craft:<register>` selects from `vault/refs/stories/` instead of
canon: always include `vault/refs/stories/register.md`'s row matching
`<register>` in its "The two registers" table, all of
`vault/refs/stories/banned-patterns.md`, and the
`vault/refs/stories/influences.md` entries whose moves the shape plan
names. Budget default 6000 tokens. Skip steps 1-2 — inclusion is fixed by
the topic, not scored — and run steps 3-4 unchanged: compress each selected
section, then fill to budget greedily (influences.md entries drop first,
then banned-patterns.md, then register.md's row last). Render one block per
step 5; header reads
`PACK: craft:<register> — <actual>/<budget> tokens, <n> pages, <m> dropped`.

## Visibility

Default audience is the DM: pending pages and `## DM Only` content may be
included, each labeled (`(pending)`, `(DM only)`). Consumer is
player-facing (recap, anything a player reads) → strip every `## DM Only`
section and every `status: pending` page before scoring (L3 default-deny),
and say so in the header.

## Boundaries

- Never write the pack (or any page) to the repo — a consumer that needs a
  durable artifact routes to its owning skill (`draft-run-guide`,
  `recap-writer`).
- Never state a fact in the pack that isn't on a page read this run (L1);
  the pack cites by wikilink like any answer.
- Contradiction between two included pages → include both lines flagged
  `CONTRADICTION`, route `canon-review`; never pick silently.
