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
subtype: region             # building | plane | dungeon | settlement | region | shop — an island is `region` nested `within:` a larger region or the open sea
within: "[[campaigns/<campaign>/locations/<parent-slug>]]"
north_of: ""                 # quoted wikilink, nearest place at this location's own scale to the north — never empty, never "open water"/"none"
east_of: ""                   # quoted wikilink, nearest place to the east — same rule
south_of: ""                  # quoted wikilink, nearest place to the south — same rule
west_of: ""                    # quoted wikilink, nearest place to the west — same rule
geography: []                # terrain tags, at least one
campaigns: []                 # OPTIONAL
reference_image: ""           # OPTIONAL
owner_skill: ".claude/skills/draft-content/references/location.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: ad67cfca-2a28-44ca-8a8a-f24aa877c1e9
---

# <Name>

## Map

OPTIONAL — keep this heading when a chart of this region has been drawn and
stored under `_assets/maps/`; delete it outright when none has. Never write
the heading over prose describing the region's shape: that prose belongs in
the opening paragraphs below, and a `## Map` with no `leaflet` block in it
is a heading pretending to be a chart. Where kept, it comes first on the
page, because the marker coordinates fix each child location's position
relative to its neighbours. Image generated per the `visual-aids` skill and
`vault/refs/art-style.md` § Maps, stored at `_assets/maps/<slug>-map.<ext>`,
one marker per `## Locations Within`/`## Landmarks` entry; region scale is
miles, not feet.

```leaflet
id: <unique-id>
image: [[_assets/maps/<slug>-map.<ext>]]
bounds:
  - [0, 0]
  - [<image height>, <image width>]
height: 780px
width: 100%
lat: <half the image height>
long: <half the image width>
minZoom: -2
maxZoom: 2
zoomDelta: 0.125
defaultZoom: -0.125
unit: miles
scale: 12
marker:
  - default, <lat>, <long>, [[<slug>|Display]], <one-line description>
```

Opening prose sits below: two or three short paragraphs on what this region
is, what it looks like from the water or the road, and who holds it.

![[<slug>-narration-appearance]]

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## At a Glance

A two-column `| Field | Detail |` table, one row each: Type, Within,
Controlled By, Access, Known For. Every value that names a page is a
wikilink. The Within row names this page's own `within:` and nothing
further up the chain. One clause per Detail.

## Geography

Every physical place occupies space relative to other places, so this
section is never omitted. **Extent** — one line fixing size and shape, in
miles once crossing it takes a day's travel or a sail, never mixed with
feet. **Topography** — elevation, footing, sight lines, ways in and out;
concrete and short. Compass neighbours live in the `north_of`/`east_of`/
`south_of`/`west_of` frontmatter fields, not here — all four are
mandatory, every place has something in every direction, and "open
water"/"none" is never an acceptable value. Placement judgment (nearest
sibling at this location's own scale, never `within:` itself, widen past
the parent's edge when nothing sits there) is in
`vault/refs/vault/location/references/placement.md`.

## Government

OPTIONAL — keep when this region has a real ruling structure spanning its
settlements; delete otherwise.

## Trade

OPTIONAL — keep when the region's economy (a trade route, a resource, a
blockade) matters to the story; delete otherwise.

## Culture

OPTIONAL — keep when a culture, faith, or custom spans the region rather
than belonging to one settlement in it; delete otherwise.

## Defenses

OPTIONAL — keep when a region-spanning military or defensive posture is
plot-relevant; delete otherwise.

## Routes & Access

How a party gets into this region, crosses it, and gets out — the lanes,
the channels, the season or tide that closes them, and who is watching.
Cite `vault/refs/vault/location/references/wilderness-travel-and-exploration.md` and
`vault/refs/gameplay-toolbox.md` § Travel Pace for running the
journey rather than restating either table on the page.

## Hazards

OPTIONAL — what can kill or strand a party here that is native to the
region rather than to one place in it — terrain, weather, predators,
political hazards that behave like terrain.

## Landmarks

OPTIONAL — keep when at least one page's `within:` resolves to this region
and has no page of its own worth a `## Settlements` row (a ruin, a reef, a
named stretch of water); delete otherwise. A two-column `| Landmark |
Detail |` table.

## Settlements

OPTIONAL — keep when at least one settlement- or region-shaped page's
`within:` resolves here; delete otherwise. A two-column `| Place | Detail |`
table, one row per child page, ordered as the map reads. Every row's Place
cell is a wikilink to a real page. Where `## Map` is kept, each row's
marker exists there and each marker's row exists here — a mismatch between
them is the defect this pairing exists to catch.

## Ecology

OPTIONAL — one to three paragraphs on what naturally lives here and why,
grounded in the terrain and climate already established above, thematic
archetypes only, never a literal monster checklist — the anchor a `type:
monster` page's `found_at:` frontmatter cites for its own thematic-fit
judgment call.

## Loot

OPTIONAL — keep when at least one `type: secret, subtype: cache` page's `within:` resolves
here; delete otherwise.

![[<loot-slug>]]

## Notable NPCs

OPTIONAL — only when real, sourced NPCs operate at region scale, not tied
to one place within it.

