---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Full Player-Known/DM-only mapping onto the location template — read-aloud opening, At a Glance, the OPTIONAL body sections, Toy Chest, On Display, Notable NPCs, and per-subtype additions."
created: "2026-08-03"
updated: "2026-08-10"
tags: [exploration]
uid: fbfe1821-139c-4c81-95b2-ccfb5d35c16c
---

# Draft — Location Output Structure

Content flows top-to-bottom in the template's own heading order — read-
aloud opening, `## At a Glance` (governed-area and dungeon subtypes) or
`## Structure` (site subtypes), `## Geography`, whichever OPTIONAL
sections apply, then `## Loot` / `## Notable NPCs`. Every
Notable NPC resolves to a wikilink or spawns a pending stub, never
plain-text prose (`vault/refs/vault/location/references/npcs.md`).

The Player-Known/DM-Only distinction below is a *drafting* lens (what the
table can learn through play vs. what only the DM sees), not a separate
page structure — same convention `.claude/skills/draft-content/references/npc.md` and
`.claude/skills/draft-content/references/monster.md` use. It maps onto the template's own
headings rather than needing headings of its own.

**Player-Known material** — the table's experience of the place, the
page's own `status: pending` frontmatter is the provenance marker
(page-level only, no inline tag; `transcript-ingest` flips it to `canon`
once the party actually arrives):

- **Read-aloud opening** as a `[!read-aloud]` callout (hand the
  sentence-level work to `dnd5e-scene-narration`'s two-draft protocol).
  **Full mode** (3–5 sentences) for first impressions, **lite mode** (2–3
  sentences) for revisits or minor spaces. Short on ideas before
  drafting? Name the location, then name three fantastic aspects for it
  (`.claude/skills/composing-beats/references/runtime-surface.md` § Develop
  Fantastic Locations — e.g. "Blazing beam of light shining to the
  heavens," "Moat of molten rock") as raw material for
  `dnd5e-scene-narration`'s draft, not a competing method.
- **Notable sub-location read-alouds** — for any secondary space worth
  its own beat (a building's notable room, a region's landmark —
  anything short of a full dungeon room key), add an `### <Sub-location
  Name>` subheading with its own `[!read-aloud]` callout, lite mode by
  default.

**DM-only material** — everything that runs the location but hasn't
reached the table yet, filled into the template's own headings after the
Player-Known material and before `## Notable NPCs`:

- **`## At a Glance`** (settlement, region, dungeon) — the two-column
  table the template specifies: subtype-appropriate fields (Ruled By/
  Population for settlement, Controlled By/Access for region, Danger for
  dungeon), each a one-clause Detail, every page-naming value a wikilink.
  Site subtypes (building, plane, shop) have no `## At a Glance` — their
  `## Structure` heading carries the equivalent detail as prose instead.
- **`## Geography`** — Extent and Topography per the template's own spec;
  compass neighbours live in frontmatter, not here
  (`vault/refs/vault/location/references/placement.md`).
- **Government / Trade / Culture / Defenses / Hazards /
  [[ecology|Ecology]]** —
  settlement- and region-specific OPTIONAL sections, each keeping only a
  real, decided fact; `vault/refs/vault/location/references/settlement.md` and
  `vault/refs/vault/location/references/region.md` own the keep/delete
  judgment for each.
- **Toy Chest** — the table from `.claude/skills/draft-content/references/location.md` §
  Toy Chest (`vault/refs/vault/location/references/toy.md` for vocabulary and
  examples), placed as free prose after `## At a Glance`/`## Structure`
  — it has no heading of its own on the template.
- **Location quality checklist** — before finalizing, check the location
  against `vault/refs/vault/location/references/tips.md`'s six-item checklist
  (elaborated in `.claude/skills/composing-beats/references/composition.md` § Locations):
  one defining trait, familiar, functional, fantastic, moves the story
  forward, has personality, envisioned in three dimensions. Cited, not
  restated — read either file rather than treating this bullet as the
  full rubric.
- **Notable sub-location DM notes** — the matching `### <Sub-location
  Name>` subheading for each one introduced under Player-Known: what
  it's for, its own mini Toy Chest row if it's independently active, any
  mechanics in parentheses.
- **[[dungeon|Dungeon]] subtype only** — the room content splits at room granularity,
  per `vault/refs/vault/location/references/dungeon.md` § Output structure
  (the authoritative spec for this): each Room's read-aloud half lands as
  an `### Room N — Name` subheading in the Player-Known material; the DM
  half — Access, General Features, Map Key, per-room mechanics/secrets,
  Three Clue Audit, Treasure Summary, Running This Dungeon — sits as
  `###` subheadings in the DM-only material, where the publish-time strip
  swallows that whole range. The callout *type* marks voice; which half
  it sits in marks publish eligibility.
- **[[settlement|Settlement]] or region subtype, including a district or island** —
  `vault/refs/vault/location/references/settlement.md` and
  `vault/refs/vault/location/references/region.md` § Output structure are the
  authoritative mapping, including when a district/sub-region/landmark
  earns its own page versus a subheading on the parent.
- **[[shop|Shop]] subtype only** —
  `## Shopkeeper`'s transclusion, the mandatory `## On Display`
  read-aloud box and curated item list (with the read-layer commands
  that pick the items), and `## Inventory`'s Base embed are all
  specified in `vault/refs/vault/location/references/shop.md`, the
  authoritative mapping for this subtype.

**`## Notable NPCs`** — wikilinks only, resolved or stubbed per
`vault/refs/vault/location/references/npcs.md`.

**`## Session Log`** — starts empty. `transcript-ingest`'s territory
(`vault/refs/runbook-wiki.md` § Who writes what): once the party
actually visits, `transcript-ingest` appends
`- [[sNN-slug]] — one line of what happened`. Don't pre-fill it, and
never retroactively edit an entry — a contradicting later session gets a
`CONTRADICTION:` block instead (`vault/refs/runbook-wiki.md` rule 6).
