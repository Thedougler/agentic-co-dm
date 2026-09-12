---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Mapping ship content onto the template's headings, and when a Tier-3 vessel earns a multi-file family."
created: "2026-08-03"
updated: "2026-08-03"
tags: [maritime]
uid: 8f7d3d22-c1cb-45de-946a-df081f5f2fe2
---

# Output structure and multi-file ship families

## Output structure — mapped onto the ship template

`vault/_templates/_srd/_ship.md` is the sole authority on shape (`vault/_templates/CLAUDE.md`) — this
section maps content onto it, it doesn't restate it. The required H2s for `type: ship`
are fixed: `## Stats & Combat`, `## Crew`, `## Session Log` — nothing added, nothing
removed, this order (the Template Heading Lock). `## Connections` is optional (template carries it,
lint doesn't require it). No Player-Known/DM Only split — `publish:`/`status:` on the
page is the visibility gate (`.claude/skills/composing-beats/references/runtime-surface.md` §8); everything below is organized by
content function, not by who's allowed to know it.

**Above `## Stats & Combat`** — drafted ahead of the reveal, the page's own
`status: pending` frontmatter is the provenance marker (page-level only, no
inline tag; `transcript-ingest` flips it to `canon` once the table actually
sees this ship):

- **Flavor description** — 2-4 sentences, `[!read-aloud]` callout. Silhouette, build,
  one signature detail — checked against `vault/refs/vault/location/references/tips.md`'s six-point
  checklist (the Mobile-Location Check). No mechanical content here.
- **Stat line**, plain text immediately after: `*[Ship class] · Tier [N] · [home port
  or "unmoored"]*`.
- **Ship Toy table** (`.claude/skills/draft-content/references/ship.md` § Ship Toy) — the DM-facing fields, plus anything that
  helps the DM run the ship but hasn't reached the table yet: hidden cargo, true
  ownership, prepped reveals. A genuinely hidden fact stays inline in prose here, never
  partitioned into its own heading (`.claude/skills/composing-beats/references/runtime-surface.md` §8).

**`## Stats & Combat`** — a body table (Hull Points, Hull AC, Damage Threshold, Speed,
Cargo, Crew min/full, armament — adapt columns to what the vessel needs, per
`vault/refs/vault/ship/references/tiers-and-crew.md` § 2) plus any variant or magical enhancement,
each `[HB]`/`[RAW]`-labeled and bounded (the Bound And Label Every Effect rule). Never a combat encounter's
stat block or difficulty calibration — that's `encounter-prep`'s (the Player Character Boundary).

**`## Crew`** — named crew with roles (`vault/refs/vault/ship/references/tiers-and-crew.md` § 3); total
headcount for unnamed ordinary sailors. A named crew member who might recur — a rival
captain, a first mate with their own arc — hands off to the `npc` type
(`.claude/skills/draft-content/references/npc.md`) before this guide writes a line of dialogue for them;
a one-off name with no future stays inline as a bullet.

**`## Connections`** (optional) — owner, home-port faction, rival vessels,
writs/liens — durable non-crew relationships, wikilinked. Keeps `## Session Log`
purely session-appearance evidence, per `vault/_templates/_srd/_ship.md`'s `## Connections`
note.

**`## Session Log`** — starts empty. `transcript-ingest`'s territory: once the ship
actually appears at the table, `transcript-ingest` appends
`- [[sNN-slug]] — one line of what happened`.
Don't pre-fill it — leave it empty; `transcript-ingest` will populate it when the ship appears at the table.

## Multi-file ship families (the Tier-3 pattern)

Per the Multi-File Fork rule, only when its bar is met (the party's
home ship, or a major campaign vessel that genuinely needs more than one page): one
parent `ship` page `<ship-slug>.md` plus child `ship` pages
`<ship-slug>-<part-slug>.md`, children back-linking the parent — the same tree
convention `.claude/skills/draft-content/references/location.md`'s settlement subtype uses for a settlement and its
districts. Typical parts: `<ship-slug>-layout.md` (deck-by-deck room keys — key each deck
as a zone, `vault/refs/zone-based-combat.md`'s ~25ft abstraction, and name what's
physically in each one: rigging, hatches, cargo nets, gun mounts, anything a future
boarding fight could use as an interactive object, cover, or difficult terrain,
per `vault/refs/combat-encounter-checklist.md`'s categories — this guide states what's
there, `encounter-prep` decides how a fight uses it, the Player Character Boundary stays intact),
`<ship-slug>-manifest.md` (full crew roster beyond what the parent's `## Crew` table shows),
`<ship-slug>-owners-manual.md` (player-facing reference, if the party controls it).
Every child page still carries the fixed ship-template headings and still lints
individually — a child page is not exempt from the Template Heading Lock just because it's a
sub-file. The parent page's `## Stats & Combat` and `## Crew` stay the summary; a
child's version can go deeper without duplicating the summary verbatim (same
single-source-split discipline `.claude/skills/draft-content/references/location.md`'s settlement-subtype reference uses
between a settlement and its district pages).
