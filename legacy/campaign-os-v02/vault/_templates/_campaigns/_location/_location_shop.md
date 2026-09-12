---
type: location
status: draft
publish: false
title: ""                 # OPTIONAL — display title if it differs from the H1
aliases: []
summary: ""                 # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
tier: supporting           # core | supporting | peripheral
subtype: shop
within: "[[campaigns/<campaign>/locations/<parent-slug>]]"
shopkeeper: "[[<slug>]]"
north_of: ""                 # quoted wikilink, nearest place at this location's own scale to the north — never empty, never "open water"/"none"
east_of: ""                   # quoted wikilink, nearest place to the east — same rule
south_of: ""                  # quoted wikilink, nearest place to the south — same rule
west_of: ""                    # quoted wikilink, nearest place to the west — same rule
geography: []                # terrain tags, at least one
campaigns: []                 # OPTIONAL
reference_image: ""           # OPTIONAL
owner_skill: ".claude/skills/draft-content/references/location.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 53c64b23-5ce9-4184-b206-621ee004daac
---

# <Name>

![[<slug>-narration-appearance]]

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## Structure

The interior, room by room where it matters (counter, back room, cellar):
what a party sees crossing the threshold and moving through it. Compass
neighbours live in the `north_of`/`east_of`/`south_of`/`west_of`
frontmatter fields, not here — all four are mandatory, every place has
something in every direction, and "open water"/"none" is never an
acceptable value. Placement judgment is in
`vault/refs/vault/location/references/placement.md`.

## Atmosphere

What it feels like to be a customer here — sound, smell, light, the
shopkeeper's manner, the regulars. Short: this is color, not mechanics.

## Shopkeeper

The `shopkeeper:` frontmatter key is the wikilink source of truth; this
heading transcludes that same page, full-page — no NPC prose here, no
partial copy.

![[<shopkeeper-slug>]]

## On Display

![[<slug>-narration-on-display]]

<One bullet per item, 6-10 items, ordered as the box shows them:
`* [[<item-slug>|<Item Name>]] - <value, gp> - <one clause, what it does
or what it is>`. Ranked on usefulness to this party between its current
level and three levels on first — the gap in their gear, the consumable
they burned through, the counter to what is hunting them — and on
thematic and narrative fit second, which chooses between equally useful
candidates and never promotes a useless one. Three quarters usable
tonight, the remaining quarter a tier above them, priced out of reach,
there to be saved for. Every entry is a real `type: item` page with
`value:` set and `found_at:` linking here, or it does not go on the
list.>

## Inventory

Embeds the campaign's shared shop-inventory Base, which filters live to
items whose `found_at:` links to this page — the full standing stock, of
which `## On Display` is the curated shortlist. No per-shop Base file
needed.

![[shop-inventory.base]]

## Loot

OPTIONAL — keep when at least one `type: secret, subtype: cache` page's `within:` resolves
here (a hidden cache distinct from the shop's own for-sale Inventory);
delete otherwise.

![[<loot-slug>]]

## Notable NPCs

OPTIONAL — only when real, sourced content fills it beyond the
shopkeeper.

Who else can the party find here?

