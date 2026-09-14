---
name: session-recap
description: >
  Turn an approved session log or ingest packet into a player-facing recap without duplicating session-wrapup.
  Invoke for: "session recap", "process session notes", "update the wiki after session",
  "what changed this session", or "post-session recap". Consumes a bounded session log or ingest packet and produces only a recap plus optional highlights.
disable-model-invocation: true
---

> Sandbox rules are in AGENTS.md (always loaded). Use the vault procedures in AGENTS.md and the existing sibling skills.

## Work gate

Wrapup. Follow `docs/agents/work.md`. Show a chat proposal first. Write to `wiki/` only after DM accept (FR-019). Reject leaves no page. Ground claims in wiki pages and/or D&D 5e rules; cite `[[pages]]`. Recap is human prose. Unused prep is not canon. Players see nothing until accepted and presented.

## What this produces

A bounded player-facing rendering of a finished session log; it does not cascade world state.

## Inputs

One of:
- An approved session log under `wiki/journal/sessions/<campaign-slug>/<NN>/`
- A bounded evidence packet from `session-transcript-ingest` or
  `reconciling-session-evidence`
- A request like "process session 4" — locate the approved log after wrap-up

Raw notes, recordings, and transcripts must go through the ingest/reconciliation
path first; do not use them directly as recap input.

## Workflow

### 1. Read current state

Read in this order, stopping when you have enough:
1. `wiki/<campaign>/hot.md`
2. The most recent `wiki/journal/sessions/<campaign-slug>/<NN>/Session NN - Recap.md` — for continuity and tone
3. Active situation files in `wiki/<campaign>/fronts/` relevant to the session
4. Entity pages referenced in the notes (summary frontmatter first; full page only if needed)

### 2. Propose, then file after accept

Show the recap in chat. After DM accept, create `wiki/journal/sessions/<campaign-slug>/<NN>/Session NN - Recap.md` (same folder as that night’s plan/beats; never flat `wiki/journal/Session NN - Recap.md` or a `recaps/` tree) following the established pattern:
- Frontmatter: `type: recap`, `lifecycle: accepted`, campaign fields, `visibility: table`, and `tags: [session, recap]`
- Player-facing prose — what happened as the players experienced it
- Load `obsidian-markdown` for prose standards
- Wikilink every named entity on first mention

If the DM rejects, write nothing.

## Boundary with existing session skills

`session-transcript-ingest` owns raw transcript cleanup and evidence packets. `session-wrapup` owns the durable DM log, surgical canon updates, clocks, and entity filing. This skill consumes that finished log or approved packet and writes only the player-facing recap plus optional highlights; it does not update `hot.md`, fronts, entity pages, AGENTS.md, or canon.

## Finish

Run `./scripts/lint-obsidian-markdown` on the recap after any write.

## Post-session wiki spine

Run after `session-wrapup`, ideally within 24 hours. Keep the durable dump to
about 15 minutes: who acted, what decisions changed, and which threads remain
open. Compare the player recap with the approved log without promoting a
contradiction. The recap is only the short player-facing rendering; typed NPC,
place, loot, or other canon belongs to the owning notes, and faction clocks/world
tick belong to `world-tick`.
