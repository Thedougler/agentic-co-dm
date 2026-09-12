---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The questions every content type asks the DM before drafting, asked in one message, plus what the interview never invents for itself."
created: "2026-08-03"
updated: "2026-08-15"
tags: [craft]
uid: 5dedf7cb-9fa7-4972-877d-81275fef653e
---

# Draft — Shared Interview

Ask every uncovered question below in a single message, never serially
(`.claude/skills/composing-beats/references/runtime-surface.md` § Prep-entity floor) -> a guide that asks one question
per turn burns the DM's turns.

A per-type guide lists its own extra questions and asks them in the same
message as these.

## The questions every type asks

- **Which PC, and how?** Ask per the PC-Connection Requirement
  (`vault/refs/vault/_common/hard-rules.md`).
- **Where does it sit in the wiki?** The location, region, faction, or
  parent entity this attaches to, so the page's frontmatter and wikilinks
  resolve.
- **Is it table-bound?** Could the party conceivably interact with this
  **this session or the next**? Yes → `prep_depth: planned` and the page
  earns spoken siblings, linked entities, and a run-guide line. No →
  `prep_depth: initial`.
- **Does it want a visual aid?** Only for a named, party-relevant entity,
  and only once the page's own review gate passes.

## What the interview never invents

Race, species, role, subtype, tier, rarity, and the PC connection are all
DM answers -> ask for them rather than supplying a default. A default
silently becomes canon the moment the page is written.

An answer the DM has already given in this conversation is answered -> do
not re-ask it.
