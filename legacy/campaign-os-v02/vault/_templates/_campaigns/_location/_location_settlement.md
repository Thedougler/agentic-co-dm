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
subtype: settlement        # building | plane | dungeon | settlement | region | shop — a district is `settlement` nested `within:` a larger settlement
within: "[[campaigns/<campaign>/locations/<parent-slug>]]"
north_of: ""                # quoted wikilink, nearest place at this location's own scale to the north — never empty, never "open water"/"none"
east_of: ""                  # quoted wikilink, nearest place to the east — same rule
south_of: ""                 # quoted wikilink, nearest place to the south — same rule
west_of: ""                   # quoted wikilink, nearest place to the west — same rule
geography: []               # terrain tags, at least one
campaigns: []                # OPTIONAL
reference_image: ""          # OPTIONAL
owner_skill: ".claude/skills/draft-content/references/location.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 0ada0260-8303-42a9-8280-ef2a338857aa
---

# <Name>

![[<slug>-narration-appearance]]

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## At a Glance

A two-column `| Field | Detail |` table, one row each: Type, Within,
Ruled By, Population, Known For. Every value that names a page is a
wikilink. The Within row names this page's own `within:` and nothing
further up the chain. One clause per Detail — this is the row a DM reads
mid-session.

## Geography

Every physical place occupies space relative to other places, so this
section is never omitted. **Extent** — one line fixing size and shape, in
feet where a party crosses it in a turn or two, never mixed with miles:
`roughly 400 ft. by 250 ft., a crescent open to the west`, not `large`.
**Topography** — two to four lines, in order: elevation, footing, sight
lines, ways in and out; the map a player builds in their head, concrete
and short. Compass neighbours live in the `north_of`/`east_of`/`south_of`/
`west_of` frontmatter fields, not here — all four are mandatory, every
place has something in every direction, and "open water"/"none" is never
an acceptable value. Placement judgment (nearest sibling at this
location's own scale, never `within:` itself, widen past the parent's
edge when nothing sits there) is in `vault/refs/vault/location/references/placement.md`.

## Government

OPTIONAL — keep when a real seat of power, law, or judiciary has been
decided; delete otherwise. Who rules, how, and what happens when someone
breaks the law here.

## Trade

OPTIONAL — keep when this settlement's economy matters to the story
(a trade hub, a smuggling port, a company town); delete otherwise.

## Culture

OPTIONAL — keep when a distinct custom, faith, or festival defines life
here; delete otherwise.

## Defenses

OPTIONAL — keep when the settlement's fortification or lack of one is
plot-relevant; delete otherwise.

## Districts

OPTIONAL — keep when at least one page's `within:` resolves to this
settlement; delete otherwise. A two-column `| District | Detail |` table,
one row per child page, Detail one clause. Every row's District cell is a
wikilink to a real page — a district with no page of its own is a
`### <Name>` sub-location subheading instead, never a bulleted name with
no target.

## Loot

OPTIONAL — keep when at least one `type: secret, subtype: cache` page's `within:` resolves
here; delete otherwise.

![[<loot-slug>]]

## Notable NPCs

OPTIONAL — only when real, sourced NPCs are found here.

Who can the party find here? Each one resolves to a wikilink or a spawned
stub, never plain-text prose.

