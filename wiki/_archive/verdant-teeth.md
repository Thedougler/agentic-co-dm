---
type: location
status: canon
publish: false
title: "The Verdant Teeth"
aliases:
- Verdant Teeth
summary: Five reef-fringed Grung-held islands in the middle of the Midchain, with dense rainforest interiors, strict trade protocols, and lethal boundaries.
created: 2026-07-30
updated: 2026-08-09
tags:
- exploration
tier: supporting
subtype: region
within: "[[midchain]]"
north_of: "[[midchain-north]]"
east_of: "[[midchain-east]]"
south_of: "[[midchain-south]]"
west_of: "[[midchain-west]]"
geography:
- archipelago
- reef
- rainforest
campaigns:
- Shattered Sea
reference_image: ""
owner_skill: ".claude/skills/draft-content/references/location.md"
uid: c0391549-f1bc-4628-81d1-cf3e074aff4a
---

# The Verdant Teeth

## Map

```leaflet
id: verdant-teeth
image: [[verdant-teeth-map]]
bounds:
  - [0, 0]
  - [1024, 1024]
height: 780px
width: 100%
lat: 512
long: 512
minZoom: -2
maxZoom: 2
zoomDelta: 0.125
defaultZoom: -0.125
unit: miles
scale: 12
marker:
  - default, 554, 280, [[veth|Veth]], Largest island, with a sanctioned trade beach of its own.
  - default, 774, 430, [[sorn|Sorn]], Interior agriculture behind one guarded beach.
  - default, 278, 400, [[dreth|Dreth]], Eastern island; lower and wetter.
  - default, 724, 760, [[karath|Karath]], Reef gaps answered with dart and arrow fire.
  - default, 304, 740, [[orak|Orak]], Linked to Dreth by shallow crossings.
```

Clustered islands sit two days south of [[kalowe|Kalowe]], where reef-fringed coasts rise into limestone ridges and rainforest swallows the high ground. From the water, they look like a single green wall broken by reefs and pale sand.

The [[grung-clans|Grung clans]] hold every island here. Every chart marks the interiors with the same warning: do not approach. Those who cross the tree line vanish. Locals treat this as fact, not rumour.

Coastal settlements across the Midchain now report raids from the Teeth direction. The [[chain-council|Chain Council]] has heard the complaints. For now, [[veth|Veth]]'s beach remains open for trade.

> [!read-aloud]
> Green humps break the horizon first, close enough together that the gaps between them read as open water until the current pulls your hull sideways toward one.
>
> No smoke, no roofline, nothing built where you can see it. Just limestone going up pale and steep under canopy that never breaks.
>
> One shoreline shows a strip of pale sand, cleared and worked, the only interruption in the green wall running the rest of the horizon.
>
> The reef hums under the hull before the swell changes.
>
> Somewhere past that green, five clans are watching you arrive. Only two of them will let you land.

```meta-bind
VIEW[{reference_image}][image(class(reference-image-view))]
```

## At a Glance

| Field | Detail |
|---|---|
| Type | [[grung\|Grung]]-held island cluster |
| Within | [[midchain\|The Midchain]] |
| Controlled By | [[grung-clans\|The Grung Clans]] |
| Access | Sanctioned contact at [[veth\|Veth]]'s west beach or [[sorn\|Sorn]]'s guarded beach; interiors forbidden |
| Known For | Strict trade protocols, poisonous boundaries, rainforest hazards, and worsening raids |

## Geography

**Extent:** roughly fifteen miles across the whole cluster, five islands within reef-broken sight of each other. Veth is the largest, Karath and Sorn run three to four miles across, and Dreth and Orak sit smaller, linked by shallow crossings.

**Topography:** limestone ridges rise straight out of reef-fringed water on every island, rainforest closing over the high ground within a few strides of any beach. No chart marks a path through the interior. The tree line is where every survey stops.

## Routes & Access

Each clan that holds an island runs its own sanctioned beach: [[veth|Veth]]'s west beach for the blue-caste intermediaries there, [[sorn|Sorn]]'s guarded landing for the Botukuri clan. Traders anchor offshore and wait while intermediaries come down to the waterline. The exchange is brief. Visitors stay on the shore and never speak directly to gold grung.

Reef gaps ring every island in the cluster, and the clans watch each one. A hull that noses into a gap off [[karath|Karath]] takes darts and arrows before anyone hails it. No pilot trade operates here, and no beach beyond Veth's and Sorn's exists to try.

Run the crossing per `vault/refs/vault/location/references/wilderness-travel-and-exploration.md` and `vault/refs/gameplay-toolbox.md` § Travel Pace.

## Hazards

The tree line is the hazard. Those who cross it vanish. Locals state this as fact, not rumour.

Below it sit the reef gaps, the toxin the clans coat their darts with, and rainforest interiors nobody outside the clans has mapped. A visitor who keeps to the sand at [[veth|Veth]] keeps the terms the clans set, and can withdraw whenever they choose. A visitor who steps past it has no terms at all.

## Settlements

| Place | Detail |
|---|---|
| [[veth\|Veth]] | Largest island, with its own sanctioned trade beach. |
| [[sorn\|Sorn]] | Interior agriculture behind guarded beach traffic. |
| [[karath\|Karath]] | Reef gaps draw dart and arrow fire before questions. |
| [[dreth\|Dreth]] | Eastern, lower, wetter, dangerous. |
| [[orak\|Orak]] | Eastern, lower, wetter; linked to [[dreth\|Dreth]] by shallow crossings. |

## Notable NPCs

- **[[jean-claude-tabarnack|Jean-Claude Tabarnack]]**: born on the Teeth. Fled the clans. The Grung hunt him.
- **[[simone-tabarnack|Simone Tabarnack]]**: leads Sorn's garrison. Supplies Grung toxin to the [[dravosi-crown|Dravosi Crown]].

## Hooks

- Raids traced back to the Teeth are increasing; the [[chain-council|Chain Council]] has heard the complaints but has no way in past the tree line.
- [[jean-claude-tabarnack|Jean-Claude Tabarnack]]'s flight from the Teeth remains a secret. It could surface at [[veth|Veth]]'s trade beach.
