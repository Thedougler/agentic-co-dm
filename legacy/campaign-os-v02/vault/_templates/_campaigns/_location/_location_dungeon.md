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
subtype: dungeon
within: "[[campaigns/<campaign>/locations/<parent-slug>]]"
north_of: ""                 # quoted wikilink, nearest place at this location's own scale to the north — never empty, never "open water"/"none"
east_of: ""                   # quoted wikilink, nearest place to the east — same rule
south_of: ""                  # quoted wikilink, nearest place to the south — same rule
west_of: ""                    # quoted wikilink, nearest place to the west — same rule
geography: []                # terrain tags, at least one
campaigns: []                 # OPTIONAL
reference_image: ""           # OPTIONAL
owner_skill: ".claude/skills/draft-content/references/location.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: dc8ce24a-7653-4776-9531-d4222731ee15
---

# <Name>

![[<slug>-narration-appearance]]

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## At a Glance

A two-column `| Field | Detail |` table, one row each: Type, Within,
Controlled By, Danger, Known For. Every value that names a page is a
wikilink. One clause per Detail.

## Features

Architecture (what it's built of and by whom), Magical Features (any
standing effect that isn't one room's trap), Atmosphere (temperature,
air, sound, light) — as many of the three as are true here; drop what
isn't. Compass neighbours live in the `north_of`/`east_of`/`south_of`/
`west_of` frontmatter fields, not here — all four are mandatory, every
place has something in every direction, and "open water"/"none" is never
an acceptable value. Placement judgment (nearest sibling at this
location's own scale, never `within:` itself, widen past the parent's
edge when nothing sits there) is in `vault/refs/vault/location/references/placement.md`.

## Entrances & Exits

Every known way in and out, including the ones the party has to find.
One line each: where it lets out, what guards or seals it, whether it's
one-way.

## Levels

`###` subheadings, one per level (Room 1..N under each): each room's
a `![[<room-slug>-narration-appearance]]` embed in the player-facing half, its Dimensions/Features/Intent
block in the DM half. A Map Key (the Phase 3 artifact) precedes the first
level. Three Clue Audit only when a hidden conclusion exists. Treasure
Summary and Running This Dungeon (Chokepoint Test, Empty Room Test) close
the section.

## Loot

OPTIONAL — keep when at least one `type: secret, subtype: cache` page's `within:` resolves
here (a find substantial enough to reuse, revisit, or hand off — distinct
from a room-level Treasure Summary bullet); delete otherwise.

![[<loot-slug>]]

## Notable NPCs

OPTIONAL — only when real, sourced content fills it.

Who holds this site, and what are they doing when the party arrives?
Every occupant NPC carries a proactive objective that advances without
the party.

