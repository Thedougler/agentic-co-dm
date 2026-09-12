---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Region subtype specifics for the location guide — the OPTIONAL Government/Trade/Culture/Defenses/Hazards/Ecology sections, when a settlement or island earns its own page, and the wilderness-travel layer for a travelled-through region."
created: "2026-08-03"
updated: "2026-08-07"
tags: [survival, travel]
uid: 22a6356f-a121-4fe7-a6c4-61ee5618638f
---

# Draft — Location, Region Subtype

A district is `subtype: settlement` nested `within:` a larger settlement,
never its own subtype — a building *within* a settlement is `building`,
not `district`. This file covers `subtype: region`, including an island
(this same subtype, nested `within:` a larger region or the sea itself).

## Optional sections

`## Government`, `## Trade`, `## Culture`, `## Defenses`, `## Hazards`,
`## Ecology` are each OPTIONAL on
`vault/_templates/_campaigns/_location/_location_region.md` — keep only the
ones a real decision has actually been made for; delete the rest outright
rather than filling them with generic filler. `## At a Glance`, `##
Geography`, and `## Routes & Access` are never omitted — every region has
a Controlled By and an Access, every physical place occupies space
relative to its neighbours, and every region has some way a party gets
into, across, and out of it.

## Settlements and landmarks

A settlement or sub-region inside this region earns its own page and a
row in `## Settlements` when it's somewhere the party can stand and a
local power runs — same standard as any other settlement page
(`vault/refs/vault/location/references/settlement.md`). A locale with no governing structure of
its own (a ruin, a reef, a named stretch of water) is a `## Landmarks` row
instead, still its own page only if it has real content beyond a name.
Where `## Map` is kept, each row's marker exists there and each marker's
row exists here — a mismatch is the defect that pairing exists to catch.

## Wilderness-travel layer

Still a single page, not a phase-gated pipeline — but when the interview
reveals the party *travels through* this region rather than just arriving
at a fixed point (a road, a stretch of wilds, a crossing between two known
places), the `## Routes & Access` section carries that weight directly:
cite `vault/refs/vault/location/references/wilderness-travel-and-exploration.md` (Character
Roles — Trailhand, Scout, Quartermaster — and Group Stealth) and
`vault/refs/gameplay-toolbox.md` § Travel Pace (the terrain/pace/DC
table) rather than restating either table on the page. Landmarks along the
route double as secrets-and-clues delivery points
(`vault/refs/vault/location/references/wilderness-travel-and-exploration.md` § Creating the
Wilderness) — give each one worth stopping at its own row in `##
Landmarks`. A region with no journey through it — a single self-contained
locale — skips this and follows the normal
`vault/refs/vault/location/references/output.md` § Output structure like any
other subtype.
