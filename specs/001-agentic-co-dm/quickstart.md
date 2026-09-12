# Quickstart: Agentic Co-DM

Proves the spec loop on this machine. Campaign of record stays in ai-co-dm; use a throwaway source in this vault. Do not invent campaign people the source does not name.

## Prerequisites

- This repo, branch `001-agentic-co-dm`
- Obsidian can open `wiki/`
- Host agent with `.agents/skills/` loaded
- Foundry + MCP only for story 3; skip Foundry if it is down and still run 1–2 and 4

## Story 1 — Wiki

1. Name one file in `wiki/_raw/` (a place, item, hazard, or creature sample) and approve ingest of that file only.
2. Run `wiki-ingest` on that named file only.
3. Open the page in Obsidian. Expect: the sample's section order and markdown still there (early-dev exception); links; source trace; readable prose (FR-018). Thin stubs only for names in that source. Telegram copy fails. No extra invented pages. A creature page stays linear (no `col`).
4. Ask the Co-DM a fact on that page. Expect: answer + `[[citation]]`.

## Story 2 — Work

1. In prep, ask for a new NPC the wiki does not have.
2. Expect a **chat proposal**, not a wiki page: marked invention, grounded in the ingested page and/or 5e rules.
3. Edit and accept. Expect a wiki page only then, `lifecycle: accepted`.
4. Reject a second proposal. Expect no wiki page and nothing presentable.
5. Confirm no agent is used as table runtime.

## Story 3 — Foundry

1. Stage the accepted NPC via `foundry-stage`.
2. Expect the Foundry actor matches accepted wording.
3. Attempt to stage the rejected proposal. Expect refusal (nothing to stage).

## Story 4 — Wrapup

1. Propose a session outcome that contradicts prep (the NPC died, or a promise was made). Do not write yet.
2. After accept, expect wiki pages matching play.
3. Ask the Co-DM the fact. Expect the post-session page, not the obsolete prep.

## Pass

SC-005: one sitting, one operator, full loop. Wiki pages remain human prose. No silent canon. No wiki write before DM approval (FR-019). No Co-DM during a fake "session" gap between prep and wrapup.
