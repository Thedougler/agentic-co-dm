
# Draft — Threat

A danger advancing on its own timeline whether or not the party engages,
with no single organisation left to own it — or none at all. Done means
the DM can run the danger from `## Clock` alone.

Routes here: fronts, countdown clocks, escalating dangers, campaign
conflicts, and a villain's plan already in motion — each only once the
Faction-vs-Threat Boundary below sends it here. A conspiracy one
organisation runs is that faction's front; a conspiracy that outlives or
outgrows whoever started it is a threat.

## Template

`vault/_templates/_campaigns/_threat.md` — copy it. Headings fixed and in
order: `## Nature · ## Clock · ## Entangled Parties` (OPTIONAL — delete
outright if no real stakeholder fills it yet).

## Read first — all four, before writing anything

1. `.claude/skills/composing-beats/references/runtime-surface.md` — the prep craft floor.
2. `.claude/skills/composing-beats/references/audits.md` — PC agency, NPC independence.
3. `vault/refs/vault/_common/hard-rules.md` — shared rules; bind this type, never restated below.
4. `vault/refs/vault/_common/queries.md` — run the stub check now, paste the output.

`DF1: <four files read, stub-check output pasted>`.

## Hard rules — this type only

- **The Faction-vs-Threat Boundary.** A danger with one clear organisational
  owner advancing it stays on that faction's own `## Goals & Fronts`
  (`.claude/skills/draft-content/references/faction.md`) — never fork it onto a `threat` page
  too. A `threat` page exists only when the danger spans multiple factions
  or [[vault/refs/vault/location/references/npcs|NPCs]], outlives or
  outgrows whichever one started it, or has no organisational owner at all
  (a plague, a rising tide, a curse). One danger, one page — pick the owner
  test above before writing anything.
- **No Clock, No Threat.** A pressure with no independently advancing
  timeline isn't a threat — it's `lore` (a settled fact with no active
  hook) or flavor; write it there instead. Mirrors the Clock Decision Rule
  faction fronts already use.
- **`threat_status` Is Its Own Key.** Track the danger's operational state
  in `threat_status: active | dormant | resolved` only; don't duplicate it
  in `status` or prose — same discipline as `faction_status`.
- **Entangled, Not Owned.** `## Entangled Parties` names factions, NPCs, or
  locations caught up in the danger — never a substitute owner field. The
  moment one of them is genuinely running the clock, the Faction-vs-Threat
  Boundary applies and the front moves to their own page instead.

## Interview — this type only

Ask with `vault/refs/vault/_common/interview.md`'s shared questions:

- The concept — what concretely is this danger? None yet -> ask what it
  looks like rather than picking a visual for the DM
  ([[vault/refs/vault/campaign/references/degrade|Degrade By Asking]]).
- Does anything already own this danger's clock right now (the Faction-vs-
  Threat Boundary)? A clear single owner -> stop, this belongs on that
  page instead, not here.
- The Clock right now: Lifecycle, trigger conditions, segment count,
  consequence at fill — same fields the [[vault/refs/vault/faction/references/front|Front]] template asks.
- `threat_status` right now? Template default is `active`; correct if
  wrong.

## Before you ship

- [[vault/refs/vault/_common/lifecycle|Lifecycle]]: `vault/refs/vault/_common/lifecycle.md`
- Gaps: `vault/refs/vault/_common/degrade.md`
- [[vault/refs/vault/_common/handoffs|Handoffs]]: `vault/refs/vault/_common/handoffs.md`
- Boundaries: `vault/refs/vault/_common/out-of-scope.md`
- Common checklist: `vault/refs/vault/_common/checklist.md`
- Threat checklist: `vault/refs/vault/threat/references/checklist.md`

## Reference files

| File | Read when |
|---|---|
| `vault/refs/vault/faction/references/front.md` | Filling `## Clock` — full field definitions, lifecycle states, the quest-link rule |
| `vault/refs/vault/threat/references/checklist.md` | Threat-only checklist additions |
