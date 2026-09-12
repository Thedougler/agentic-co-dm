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
subtype: building           # building | plane | dungeon | settlement | region | shop — a district is `settlement`, an island is `region`, nested `within:` its parent
within: "[[campaigns/<campaign>/locations/<parent-slug>]]"
north_of: ""                 # quoted wikilink, nearest place at this location's own scale to the north — never empty, never "open water"/"none"
east_of: ""                   # quoted wikilink, nearest place to the east — same rule
south_of: ""                  # quoted wikilink, nearest place to the south — same rule
west_of: ""                    # quoted wikilink, nearest place to the west — same rule
geography: []                # terrain tags, at least one
campaigns: []                 # OPTIONAL
reference_image: ""           # OPTIONAL
owner_skill: ".claude/skills/draft-content/references/location.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: c69466f8-31d5-498a-a7a6-5ccc4bf0d538
---

# <Name>

![[<slug>-narration-appearance]]

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## Structure

The interior, what a party sees crossing the threshold and moving
through it. Compass neighbours live in the `north_of`/`east_of`/
`south_of`/`west_of` frontmatter fields, not here — all four are
mandatory, every place has something in every direction, and "open
water"/"none" is never an acceptable value. Placement judgment is in
`vault/refs/vault/location/references/placement.md`.

## Atmosphere

OPTIONAL — keep when the place has a distinct feel worth naming beyond
what the read-aloud box already covers; delete otherwise.

## Loot

OPTIONAL — keep when at least one `type: secret, subtype: cache` page's `within:` resolves
here; delete otherwise.

![[<loot-slug>]]

## Notable NPCs

OPTIONAL — only when real, sourced NPCs are found here.

Who can the party find here? Each one resolves to a wikilink or a spawned
stub, never plain-text prose.

