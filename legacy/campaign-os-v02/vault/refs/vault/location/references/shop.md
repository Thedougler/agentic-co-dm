---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Shop subtype guide: the Shopkeeper transclusion, the On Display read-aloud box and curated item list with its selection and no-repeat-in-town rules, and the Inventory Base embed."
created: "2026-08-10"
updated: "2026-08-10"
tags: [exploration]
uid: 734d62e5-e2e6-420e-8785-766405a63383
---

# Draft — Location, Shop Subtype

Read this when `.claude/skills/draft-content/references/location.md`'s interview settles on
`subtype: shop`. No deeper pipeline — one page, built from
`vault/_templates/_campaigns/_location/_location_shop.md` — but four
sections carry mechanics no other location has.

## `## Shopkeeper`

The `shopkeeper:` frontmatter key is the wikilink source of truth; the
heading transcludes that same page, full-page, never partial NPC prose.
No shopkeeper page yet → run `.claude/skills/draft-content/references/npc.md` to build one
first, then set `shopkeeper:` and the embed to it, and set the NPC's own
`location:` key back to this shop page (symmetric link both directions).

## `## On Display`

The curated shortlist the DM actually puts in front of *this* party,
sitting between `## Shopkeeper` and `## Inventory`'s full live stock. It
exists because a Base view of forty stocked items is a database, not a
scene: this section is what the shopkeeper has out where hands can reach
it, chosen for the party standing there tonight. Two parts, in order,
both required.

### 1. The read-aloud box

A `[!read-aloud]` box, **continuing mode** — the DM has already narrated
the party arriving and the shopkeeper greeting them, so this box carries
only the goods: what the shelves, cases, racks, and hooks show from where
the party stands. Theater of the mind, written to be performed
(`vault/refs/theater-of-the-mind-abbreviated.md`;
`dnd5e-scene-narration` writes the sentences, loaded while drafting,
never as an audit after). Its craft rules:

- **Show, never name.** An item reaches the table as shape, wear,
  material, sound, and the light on it — never as its title, never as
  its price, never as a game term. A player who wants the thing on the
  shelf finds out which bullet it is by asking for it.
- **No agency, no interiority.** Never narrate what the party does,
  notices, feels, or wants: no "you can't help but notice", no "your eye
  is drawn to", no "you decide to". State what is there; the pull comes
  from the object, not from an instruction to be pulled
  (`.claude/skills/composing-beats/references/audits.md`).
- **Two senses minimum, one of them not sight.** Oil, cold metal, the
  creak of a strop, the shut-since-spring smell of a case.
- **Seed the menu.** Every bullet below has its subject standing
  somewhere in these beats, with the aspirational entries visibly out of
  reach — cased, high on the wall, tagged with another buyer's name. A
  player cannot reach for what the box never put in the room.
- **Closing beat** follows the standard contract (`callouts`
  references/read-aloud.md § closing beat): the live element, the piece
  someone has to cross the floor to touch, never mood.

### 2. The list

A flat bullet list, 6–10 items, ordered as the box shows them, one line
each so the DM can scan it while the table talks:

`* [[<item-slug>|<Item Name>]] - <value, gp> - <one clause>`

Selection is the work here, not the prose, and it ranks on two things in
a fixed order.

**First, usefulness to this party between its current level and three
levels on.** What closes a gap in their gear, replaces the consumable
they burned through, or counters what is hunting them — now or by the
level they are about to reach. An item that does nothing for them across
that band does not make the list, however well it suits the shop.

**Second, thematic and narrative fit.** Between candidates that are
equally useful, take the one this shop would really have, that carries
its trade and its owner's history, and that a player can ask a question
about. Fit chooses among useful items; it never promotes a useless one.

Three quarters of the list is usable tonight and priced within reach,
and the remaining quarter sits a tier above them, priced out of reach, on
the page to be saved toward — that quarter is worth saving for precisely
because the next three levels are where it pays off. Every entry resolves to a real `type: item`
page carrying `value:` and a `found_at:` link back to this shop, so the
same item appears in `## Inventory` below; an item with no page gets one
(`.claude/skills/draft-content/references/item.md`) before it goes on the list.

### No item twice in one town

An item already on another shop's `## On Display` in the same settlement,
district, or region does not go on this one. Two shops a street apart
offering the same rapier tells the players the world has one rapier in
it; the whole point of the shortlist is that walking into the next shop
shows them something they have not seen. Check before writing the list —
every sibling shop under the same parent, not just the neighbours:

```bash
grep -rn '^\* \[\[' vault/campaigns/<slug>/locations/<folder>/*.md
```

`wiki links spread --to subtype=shop --from type=item` is the same
question asked from the item side: it names the shops each item is
*under*-represented at, so its suggestions are already variety-aware.

A staple that genuinely belongs in every shop of a trade — rope in every
chandlery — stays in `## Inventory`, where the Base carries it, and off
`## On Display`, which is the shortlist of what makes *this* shop worth
the walk.

### Picking the items

Never pick from memory — the read layer answers every one of these
questions (`vault/refs/runbook-commands.md` § Read layer; `wiki` is
`uv run --directory utils/wiki-cli wiki`), in order:

| Question | Command |
|---|---|
| What level is the party, and what hurts them? | Read `vault/campaigns/<slug>/pcs/combat-profile/party-combat-profile.md` — Effective CR Band and Weakness Map |
| What does this shop already stock? | `wiki links in <shop-page>` (`type: item` rows), or `wiki list --where type=item --where found_at~<shop-slug> --columns path,value,rarity` |
| What else fits this shop's trade? | `npm run search:content -- query "<what it deals in>"`, then `wiki list --where type=item --where rarity=<band> --columns path,value,rarity --sort value` |
| Which items are stocked nowhere yet? | `wiki links spread --to subtype=shop --from type=item` — its suggestions place a homeless item where it belongs |
| Is one shop hoarding the good stock? | `wiki links breakdown --to subtype=shop --from type=item` |

A search that comes back empty means the item page doesn't exist yet,
never that the world lacks the thing — a chandlery sells rope whether or
not the wiki has caught up. Write the missing item page, set its
`found_at:` to this shop, then list it.

## `## Inventory`

Embeds the campaign's shared
`vault/campaigns/<slug>/dashboards/shop-inventory.base`, which filters
live to items whose `found_at:` links to this page — no per-shop Base
file. Every item stocked here needs its own
`.claude/skills/draft-content/references/item.md` page with `found_at:` set to this shop
page and `value:` set; an item missing either key won't appear in the
view.
