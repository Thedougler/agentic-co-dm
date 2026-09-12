---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The within field's rules by subtype, compass-neighbour placement judgment, where location NPC stubs land, and how vault/campaigns/shattered-sea/locations/ is subdivided into region folders."
created: "2026-08-03"
updated: "2026-08-07"
tags: [survival]
uid: 1835c114-92ca-4188-b6a0-28e586f1331f
---

# Draft — Location Placement

## Within field

Every page also carries `within:` — required, like `subtype:`, never
omitted — a wikilink to the location page that contains it. Always
quoted, full vault-relative path, no alias: `within:
"[[crown-islands]]"`, never bare
`[[<slug>]]` — an unquoted wikilink value parses as a nested array, not a
string. Open field: no closed enum, since the target is another page name
not a fixed vocabulary.

A district's and a building's `within:` is the settlement (sometimes a
district, for a building) it sits inside. A settlement's is the
island/region it sits on; an island's is its region; a dungeon's is
whatever landmass or region it sits in/under. No containing location page
exists yet for any of these (or for `region` or `plane`) →
`within: "[[shattered-sea]]"`
(`vault/campaigns/shattered-sea/locations/shattered-sea.md` — the top-level region location
every other location ultimately sits inside; distinct from
`vault/campaigns/shattered-sea/campaign-overview.md`, which is the
`type: campaign` page, not a location). Every location's `within:` chain
terminates there, so the key is never blank; `vault/campaigns/shattered-sea/locations/shattered-sea.md`
itself sets `within:` to the campaign overview page.

## Compass neighbours

All four `north_of:`/`east_of:`/`south_of:`/`west_of:` frontmatter keys
are required on every location page, like `within:` — never empty, never
"open water"/"open sea"/"none", and always quoted the same way `within:`
is: `north_of: "[[al-fondale]]"`.
A place always has something in every direction; a bullet that names
nothing tells a DM nothing.

Each neighbour is the **nearest sibling at this location's own scale**,
in that compass direction: an island's neighbours are islands, a
building's are buildings on the same street, a region's are regions. Not
a nearby place of a different scale, and never a distance or travel time
— just the wikilink.

The neighbour is **never this page's own `within:` value.** A place sits
inside its parent, so the parent lies in no single direction from it and
names nothing a DM can steer toward. Reach past the parent to its
neighbour instead.

Where **no sibling exists** in a given direction — nothing else shares
this location's `within:` on that side — widen the search past the
parent's edge: name the nearest landmark of any type beyond it (an
island, a settlement, a region, a strait, a sea band — whatever the party
would actually raise if they kept going that way). An island along a
chain's northern edge usually takes the strait beyond it as its North;
the island below takes that first island. The parent location's own
Geography content is the reference for what lies outside each of its
edges.

## NPC stubs

NPC stubs this guide spawns follow `.claude/skills/draft-content/references/npc.md`'s
owned paths.

## Directory placement

`vault/campaigns/shattered-sea/locations/` is subdivided by region: a `region`/`plane` page
(and `vault/campaigns/shattered-sea/locations/shattered-sea.md` itself) lives directly in
`vault/campaigns/shattered-sea/locations/`; every other subtype's file lives at
`vault/campaigns/shattered-sea/locations/<region-slug>/<slug>.md`, where `<region-slug>` is the
nearest `subtype: region` ancestor found by walking its `within:` chain
(`.claude/skills/draft-content/references/location.md` § Template) — the same folder its
region ancestor's own page sits next to, not a folder nested inside that
page.
