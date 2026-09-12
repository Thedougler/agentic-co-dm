---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Drafting guide for vault/campaigns/shattered-sea/lore/ rumour pages — unverified in-world gossip the party can hear, spread, and investigate, with a DM-known truth value."
created: "2026-08-07"
updated: "2026-08-07"
tags: [survival]
uid: cee35f35-6f16-495f-8aef-d127727c17ae
---

# Draft — Rumour

Unverified in-world gossip the party can hear, spread, and investigate,
with a DM-known truth value. Its craft home is the GM-craft rumour-table
tradition (Roleplaying Tips' rumour-table columns, The Alexandrian's
hexcrawl rumour tables: a draw, a live question, a distortable
true/false/partially-true value) — the lore type's `spell`/`species`/
`background`/`puzzle`-style exception to narrative-wiki grounding
(ADR-0040), adapted into a per-entity page instead of a rolled table.

`draft-moment` queries these pages while grounding a moment and folds a hit
in as an overheard line whenever the party would recognize its subject —
no open objective required (`vault/refs/npc-guidance.md` §4). A one-line
piece of colour with nothing to investigate isn't a rumour page: it
belongs in the run guide's `## What They Overhear`, or in Living World
Detail when it's a change rather than talk.

## Template

`vault/_templates/_campaigns/_lore/_lore_rumour.md` — copy it, never
retype it from memory (`type: lore, subtype: rumour` — fixed, the rumour
fork of the lore type). Fixed headings, in order: `## The Rumour`,
`## Truth Value`, `## Spread`, `## Investigating It`.

## Boundary vs the lore hub

A rumour carries a live **Truth Value** the party can investigate and
change their belief about — that live question is what makes it a
rumour, not a settled fact. Once confirmed true or false at the table
with nothing left to investigate, the underlying fact moves to its own
`.claude/skills/draft-content/references/lore.md` page (or the NPC/faction/location page
it actually belongs to); this page stays as the record of how it was
heard and spread. Any other lore subtype — cosmology, history,
pantheons, cultures, legends, prophecies — is the hub's, not this leaf's.

## Read first — before writing anything

Same shared gate the hub already runs: read `.claude/skills/composing-beats/references/runtime-surface.md`
and `vault/refs/vault/_common/hard-rules.md`, then run
`vault/refs/vault/_common/queries.md`'s stub check for the rumour name.

`DR1: <three files read, stub-check output pasted>`.

## Hard rules — this type only

- **Confirm a live question.** Instantiating a page -> confirm it's
  genuinely unverified gossip with a live question (§ Boundary vs the
  lore hub), not a settled fact or another page type's own history.
- **Quote only what's spoken.** `## The Rumour` -> a `> [!read-aloud]`
  callout only when the rumour is delivered as a direct quote at the
  table; otherwise plain prose.
- **State the truth value.** `## Truth Value` -> `**True**`, `**False**`,
  or `**Partially true:**` followed by exactly what's real and what's
  distorted or invented in the retelling — the DM-only ground truth an
  investigation check resolves toward.
- **Name the spread.** `## Spread` -> name who repeats it and where, and
  state whether it mutates on retelling (and how) or stays fixed.
- **Tier the check.** `## Investigating It` -> a `[!check] <Skill> —
  <Label>` callout (`callouts` skill, references/check.md), tiered
  Success/Failure. Success moves the party toward the Truth Value;
  failure costs something (time, a wrong lead, the source clams up)
  rather than nothing happening.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- What's the rumour, verbatim as the party would hear it repeated?
- Confirm it's genuinely unverified gossip with a live question, not a
  settled fact — is there something to investigate?
- What's actually true — `**True**`, `**False**`, or `**Partially
  true**`?
- Who repeats it, and where does it circulate — does it mutate on
  retelling?
- What does pressing further on it (a skill check) reveal on success and
  cost on failure?

Sparking a rumour when the DM doesn't have one yet:
`vault/refs/vault/lore/references/rumour-content.md`.

## Before you ship

- Lifecycle: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Then: `vault/refs/vault/_common/checklist.md`
