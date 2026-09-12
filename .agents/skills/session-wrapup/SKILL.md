---
name: session-wrapup
description: >-
  Turn a completed campaign session into a durable, reviewable log and
  surgical canon updates under wiki/<slug>/sessions/. Use after play or
  after session-transcript-ingest has produced a bounded packet; do not use
  for session prep or live narration.
---

# Session wrap-up

## Work gate

Wrapup. Follow `docs/agents/work.md`. Show a chat proposal first. Write wiki pages only after DM accept (FR-019). Reject leaves no page. Load `wiki/AGENTS.md`, `copy-writer`, and `obsidian-markdown` on the post-accept write.

Invention is required when the wiki lacks the fact: flag it and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the DM has a chat proposal they can accept or reject; after accept, the filed page is inspectable Work.

Remap durable output to `wiki/`; templates live in `wiki/templates/`. Unused prep is not canon.

Turn what actually happened into the campaign's durable session record. This
skill complements `session-transcript-ingest`: when the source is a raw,
messy, or timestamped transcript, hand it to that skill first and consume its
bounded packet. Do not duplicate transcript cleanup or pass the full transcript
between specialists.

## Procedure

1. **Orient.** Use `./scripts/qmd` to retrieve the campaign hub, `hot.md`, the
   relevant session note, and any existing entities named in the notes. Confirm
   campaign and session identifiers; ask Nick/Co-DM rather than guessing a
   missing ID. Read `wiki/templates/Session log.md` before creating a log.
2. **Separate sources.** Read the play notes or the ingest packet and the
   session-prep note for comparison. Only play-supported events become canon.
   Keep unused prep, proposed actions, and unresolved audio separate from the
   durable record. Preserve Said/Resolved/Implied/Uncertain/Contradiction
   labels and short evidence spans when the ingest packet supplies them.
3. **Propose the session log.** Show the beats in chat, addressed to the DM: actual beats in order, player-safe `[!narration]`, secrets revealed, loose threads, rewards, next hooks. Do not put DM-only facts, DCs, or unearned names in narration. Do not turn silence into an event. Do not write the wiki yet.
4. **Propose surgical canon changes.** Name existing owner pages that play supports updating. For a genuinely new entity, propose a stub rather than inventing missing canon. Show contradictions to the DM.
5. **File after accept.** After DM accept, write the smallest file under `wiki/` (session log + accepted owner updates). Follow `wiki/templates/` and the AGENTS `type` enum. Do not create `campaigns/`, `pages/`, or `raw/` trees. If the DM rejects, write nothing.
6. **Hand off and finish.** Return a bounded receipt: log path, changed entity paths, unresolved contradictions, and any next-owner handoffs. Run `./scripts/after-write "skills: session wrap-up for <campaign>/<session>"` after writes. If the GM defers review, leave no silent canon write.

## Boundaries

- Session logs are durable; `wiki/templates/Session prep.md` remains disposable.
- `session-transcript-ingest` owns raw transcript/ASR cleanup and evidence
  packets; this skill owns the post-session log and approved surgical updates.
- Use `qmd-retrieval` for lookup and `obsidian-markdown` for every vault note
  write. Never paste WotC text or invent setting canon.

## Post-session ritual

Aim to capture the durable dump within 24 hours and keep the first pass to about
15 minutes: **who acted, what decisions landed, and which threads remain**. Then
update the vault bible surgically: improvised NPCs, places, loot, and other
lasting facts become typed atomic notes or updates on their existing owners. Keep
unused prep disposable, compare the short player recap when available, and hand
reviewed faction clocks or off-screen movement to `world-tick`. The session log
is the evidence spine; it is not a raw transcript.

> **Attribution and license.** Adapted from AntTheLimey/gm-apprentice's
> `session-wrapup` skill under **CC BY-SA 4.0**. Adapted for ai-co-dm by
> Nick Davenock, including path/schema remapping and local handoff rules.
> This adapted material remains available under **CC BY-SA 4.0**; see the
> vendor `LICENSE` and `ATTRIBUTION.md` for the license and attribution terms.

## Echo capture

In the durable log, retain the consequences of action **and inaction**: what the
party changed, what they left unattended, and which living faction or pressure
moved in response. Keep those echoes as evidence-backed threads for `world-tick`,
not as a retrofitted plot or hidden punishment.
