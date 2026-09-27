---
title: "Cave Bats"
aliases:
  - Cave Bats
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "/workspace/midchain-ingest/group-a/monsters/Cave Bats.md"
summary: "Three- to four-foot-winged cave bats that leave skylights at dusk. Guano feeds the caves, and mass flight warns of Blackrail country."
provenance:
  extracted: 0.85
  inferred: 0.15
  ambiguous: 0.0
invention: true
tier: supporting
created: 2026-09-13T19:58:00Z
updated: 2026-09-27
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: ecology
cr: "1/8"
relationships:
  - target: "[[Blackrail]]"
    type: related_to
  - target: "[[lava-tubes]]"
    type: related_to
---
# Cave Bats

````col
```col-md
flexGrow=2
===
## At a Glance

Cave bats are the cave country's clock and alarm: they leave at dusk, they feed over the canopy, and when the whole colony leaves at once the party knows something is moving deeper in.

- **Habitat.** Skylights, wells, and [[lava-tubes]] across [[aruhe]]'s cave country.
- **Treasure.** Guano, which is what the cave floor eats, and the first thing a party sees below a roost.
```
````

```col-md
flexGrow=1
===
> [!narration] Cave Bats
> A cave bat's body is the size of a boot, with three to four feet of wing stretched over long fingers. The wings are grey-brown and thin enough to show the bones against the light, and the face is mostly ears, folded flat at rest and opening as the bat leans into a turn. Below the roost the stone runs white and stinking with guano, and at dusk the bats pour out of the cave mouths in a stream that turns the air over the canopy solid with wings.
```

## Statblock

```statblock
layout: Basic 5e Layout
name: "Cave Bat"
size: Small
type: beast
alignment: unaligned
ac: "13"
hp: 5
hit_dice: "2d6 - 2"
speed: "10 ft., fly 40 ft."
stats: [4, 15, 9, 2, 12, 4]
senses: "Blindsight 60 ft., Darkvision 60 ft., Passive Perception 13"
languages: "—"
cr: "1/8"
traits:
  - name: "Echolocation"
    desc: "The bat can't use its Blindsight while it has the Deafened condition."
  - name: "Keen Hearing"
    desc: "The bat has Advantage on Wisdom (Perception) checks that rely on hearing."
actions:
  - name: "Bite"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 4 (1d4 + 2) Piercing damage."
```

```statblock
layout: Basic 5e Layout
name: "Cave Bat Roost"
size: Medium
type: "swarm of Small beasts"
alignment: unaligned
ac: "13"
hp: 27
hit_dice: "6d8"
speed: "5 ft., fly 40 ft. (hover)"
stats: [4, 15, 9, 2, 12, 4]
damage_resistances: "Bludgeoning, Piercing, Slashing"
condition_immunities: "Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained, Stunned"
senses: "Blindsight 60 ft., Passive Perception 13"
languages: "—"
cr: "1"
traits:
  - name: "Echolocation"
    desc: "The swarm can't use its Blindsight while it has the Deafened condition."
  - name: "Swarm"
    desc: "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Small bat. The swarm can't regain Hit Points or gain Temporary Hit Points."
actions:
  - name: "Bite"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 7 (2d6) Piercing damage, or 3 (1d6) Piercing damage if the swarm has half its Hit Points or fewer."
```

**Tactics.** A roost fights only when something blunders into it. The bats empty the cave mouth in a mass and the swarm closes on the closest warm body, biting and then re-forming around it; a swarm that is bloodied scatters into the dark and re-forms at the far end of the passage. Loud noise, fire, and a light held steady at the cave mouth keep them at the roof, and a Deafened swarm loses its blindsight and fights blind. Below half its Hit Points the roost breaks and streams out of the skylight instead of holding, which is the moment the party can leave.

**Tracks and signs.** Guano caked white below a skylight or well; dusk exits in a line over the canopy; a roost that empties in daylight means something moved deeper in, and the deeper thing is often [[Blackrail]] country. A colony leaving during the day is the earliest warning a party gets that someone is down in the tubes with them.

**Secret.** The bats are not the danger the cave's reputation is built on. They are the cave's alarm: a roost holds still through a person walking past and empties at a [[Blackrail]], which is why experienced cave crews watch the roost rather than the floor. A party that learns to read the roost gets a warning system; a party that kills the colony loses it.

**Connections.** [[lava-tubes]] are the passages the bats roost in, and their guano is what feeds the cave floor. [[Blackrail]] presence is what drives a daylight exit.
