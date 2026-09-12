---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The settlement district query addendum, escalation cases, and a full worked settlement + district example on Aberholt in the current template shape."
created: "2026-08-03"
updated: "2026-08-07"
tags: [maritime]
uid: b386f47f-de4a-49c6-b91c-5d96d29d77c3
---

# Draft — Location, Settlement Subtype, Worked Example

Read this from `vault/refs/vault/location/references/settlement.md` for the
district query addendum, the Degrade-by-asking escalation cases, and a
full worked example of the settlement + district output that guide's §
Output structure produces.

## Standard queries (district addendum)

`vault/refs/vault/_common/queries.md` already covers the settlement
name itself. Once a district is warranted
(`vault/refs/vault/location/references/settlement.md` § Districts), run the same two commands
again for its name before instantiating its page:

```bash
grep -ril "<district name>" vault/ vault/campaigns/shattered-sea/pcs/ 2>/dev/null
grep -rl --include=transcript.md -i "<district name>" vault/episodes/ 2>/dev/null
```

A hit before the district page exists means the name collides with
something established — pick a different district name or ask the DM.
Empty output is informative: nothing established, name and invent freely.

## Degrade by asking

- Unclear whether a locale earns its own district page or is just color
  in the settlement's own body → ask "does anything happen here, or is it
  just a landmark?" rather than defaulting either way.
- No real government/trade/culture/defense fact offered for an OPTIONAL
  section → leave the heading deleted; don't invent detail to fill it.
- A settlement's compass neighbour is unclear → widen the search past its
  `within:` region's edge (`vault/refs/vault/location/references/placement.md`)
  rather than guessing or writing "open water."

## Worked example (fixture — placeholder names, not real campaign content)

User: "build me a settlement — I need a smugglers' port for a level 4
party."

Interview: name `Aberholt` (Welsh *aber-* = river mouth, fits a port);
setting = coastal river-mouth; `within:` a region page (fixture:
`[[example-coastal-region]]`); compass neighbours resolved from that
region's own Geography. Cultural root: human river-trade dialect. The
haze off the fish-smoking sheds is why the smuggling economy survives
here — nobody can see across their own street past midday, so the
guild's watch relies on toll-posts, not sightlines. That's the concrete
fact the read-aloud and Government/Trade sections below draw from — it
never needed a formal Theme field to do that work.

Standard queries for `Aberholt` and its one district → no hits, clean to
create. District resolution: the working tideline holds enough of its
own detail (its own notable NPC, its own draw) to earn a page —
**Smokehouse Wharf**. The Guildhall street, by contrast, has nothing
beyond color and stays a subheading on the settlement page itself.

```markdown
---
type: location
status: pending
publish: false
title: ""
aliases: ["Aberholt"]
summary: "A haze-shrouded river-mouth port whose fish-smoke economy hides a smuggling trade."
created: "2026-07-30"
updated: "2026-07-30"
tags: [maritime]
tier: supporting
subtype: settlement
within: "[[example-coastal-region]]"
north_of: "[[riverbend]]"
east_of: "[[seal-rocks]]"
south_of: "[[kingfisher-point]]"
west_of: "[[deadman-cove]]"
geography: [coastal, river-mouth]
campaigns: []
reference_image: ""
---

# Aberholt

> [!read-aloud]
> Smoke holds at head height over the tideline, and every street below
> the bluff smells of curing fish before you see a single shed. Cargo
> sleds rattle across plank walkways somewhere off in the haze — moving
> fast, going somewhere in particular. Up the one switchback street, the
> Guildhall's clean stonework stands clear of it all, watching.

## At a Glance

| Field | Detail |
|---|---|
| Type | Settlement |
| Within | [[example-coastal-region]] |
| Ruled By | The Harbormaster's Guild |
| Population | ~2,000 |
| Known For | Fish-smoke haze thick enough to hide a handoff |

## Geography

**Extent.** About a mile and a half of waterfront by half a mile inland,
a wedge narrowing upriver to the one street that leaves town.

**Topography.** The tideline is the low point and the Guildhall bluff the
high one, some 90 ft. above it, climbed by a single switchback street.
Everything below the bluff is mudflat and boardwalk, and the boards go
under at spring tide. The smoke off the curing sheds holds at head height
in still weather, so anyone on the flats sees perhaps thirty feet; from
the bluff the whole harbour is legible. Three ways in: the river road,
the harbour itself, and the tide-crossing to Seal Rocks, which closes
twice a day.

## Government

The Harbormaster's Guild rules by charter, seated in the Guildhall.
Three elders hold the deciding votes on anything the Guild sanctions —
right now, that includes who gets safe-harbor papers.

## Trade

The declared economy is fish-curing and river freight; the real money
moves through the same sheds after dark. The haze isn't decorative — it's
the reason the smuggling trade survives here at all.

## Districts

| District | Detail |
|---|---|
| [[aberholt-smokehouse-wharf]] | The working tideline, sheds and cargo runs, smoke thick enough to hide a handoff |

## Notable NPCs

- [[elder-voss|Elder Voss]] — Harbormaster's Guild elder, one of the three
  deciding votes. Covers for a debt he doesn't know the size of.

```

```markdown
---
type: location
status: pending
publish: false
title: ""
aliases: ["Smokehouse Wharf"]
summary: "Aberholt's working tideline district — smoking sheds, plank walkways, and cargo traffic thick enough to hide a handoff."
created: "2026-07-30"
updated: "2026-07-30"
tags: [maritime]
tier: supporting
subtype: settlement
within: "[[aberholt]]"
north_of: "[[aberholt-guildhall]]"
east_of: "[[aberholt-guildhall]]"
south_of: "[[seal-rocks]]"
west_of: "[[deadman-cove]]"
geography: [coastal]
campaigns: []
reference_image: ""
---

# Aberholt: Smokehouse Wharf

> [!read-aloud]
> Rows of smoking sheds stand on pilings, joined by plank walkways slick
> with tide-scum. Past ten feet in most weather, the haze swallows
> everything — you hear the cargo sleds on the boards before you see
> them.

## At a Glance

| Field | Detail |
|---|---|
| Type | Settlement (district) |
| Within | [[aberholt]] |
| Ruled By | The Harbormaster's Guild (via [[aberholt]]) |
| Population | ~600 (dockworkers, curers) |
| Known For | Cargo traffic no one outside it can actually see |

## Geography

**Extent.** The tideline itself, a few hundred feet of pilings and
walkway between the waterline and the base of the Guildhall bluff.

**Topography.** Flat, planked, and slick — every walkway tide-scummed,
sightlines cut to ten feet or less whenever the sheds are running.

## Notable NPCs

None beyond [[elder-voss|Elder Voss]], who is cited on [[aberholt]]
rather than restated here.

```
