---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Mapping item content onto the template's headings, and the cross-skill handoffs that touch a named NPC, location, or treasure slot."
created: "2026-08-03"
updated: "2026-08-08"
tags: [craft]
uid: 35c94ea0-c9a1-4a3d-bfd6-d769f03217e5
---

# Output structure and cross-skill handoffs

## Output structure — mapped onto the item template

`vault/_templates/_srd/_item.md` is the sole authority on shape — this section maps
content onto it. The required H2s for `type: item` are `## Mechanics` and
`## Provenance`, both OPTIONAL per the template's own stated conditions
(the Template Heading Lock). No Player-Known/DM Only split —
`publish:`/`status:` on the page is the visibility gate
(`.claude/skills/composing-beats/references/runtime-surface.md` §8); organize by content function below.

**Above `## Mechanics`**, drafted ahead of the reveal, the page's own
`status: pending` frontmatter is the provenance marker (page-level only, no
inline tag; `transcript-ingest` flips it to `canon` once the table actually
sees this item):

- **Flavor description** — 2-4 sentences, `[!read-aloud]` callout.
  Appearance, provenance-in-brief, feel in hand. No mechanical content — a
  player could hear this before picking the item up (the Prose Pass).
  Sharpen it with the Condition + Description + Origin method in
  `vault/refs/vault/item/references/flavor-generation.md`.
- **Stat line**, plain text immediately after — format in
  `vault/refs/vault/item/references/srd-conventions.md` § Stat line format.
- **Item Toy table** (`vault/refs/vault/item/references/toy.md`) — the
  DM-facing fields, plus anything that helps the DM run the item but hasn't
  reached the table yet: hidden mechanics not yet revealed, future draws,
  plain prose for anything that shouldn't leak before the item's reveal.

**`## Mechanics`** — every power the item has, each Bound And Label Every
Effect-compliant, edge cases named where they'd plausibly come up, closed
with a **Limitations** subsection stating what the item explicitly cannot
do.

**`## Provenance`** — the item's history: who made it, who owned it before
now, how it's arriving in the current arc, and its current holder.
Wikilink every NPC, location, or faction named here.

## Cross-skill handoffs

- **Sold by, or made by, a named NPC** — confirm that NPC's page exists via
  the stub check, routing an unbuilt one through `.claude/skills/draft-content/references/npc.md`
  first, then wikilink the item to their page in `## Provenance` and add a
  reciprocal link on the NPC's own `## Relationships` section.
- **Tied to a specific location** — confirm that location page exists, add
  a reciprocal wikilink there too.
- **Filling a treasure slot for an encounter or a dungeon room** — the
  calling guide hands over the slot's context (rarity ceiling, narrative
  reason); this guide delivers the complete item page, then hands back a
  wikilink for the caller to place inline.
- **Visual aid, once the DM Review Gate passes** — category Props (1:1
  square, object-focused); skip for items never described to players.
