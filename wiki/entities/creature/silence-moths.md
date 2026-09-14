---
title: "Silence Moths"
aliases:
  - Silence Moths
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "campaign-os:silence-moths.md"
  - "/workspace/midchain-ingest/group-a/monsters/Silence Moths.md"
summary: "CR 8 silent moth swarm that muffles sound and fills mouths; fire drives it off the trees."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T20:00:00Z
updated: 2026-09-13
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: "controller"
cr: "8"
relationships:
  - target: "[[Aruhe]]"
    type: related_to
---
# Silence Moths

## Statblock

````col
```col-md
flexGrow=2
===
> [!narration] Narration
> Thumb-sized, colorless moths drift at dusk and dawn in a cloud the size of a sail. Ahead of the swarm the jungle goes quiet, then the cloud fills a mouth.
```

```col-md
```statblock
layout: Basic 5e Layout
name: "Silence Moths"
size: Huge
type: swarm of Tiny monstrosities
alignment: unaligned
ac: 13
hp: 105
hit_dice: "14d12 + 14"
speed: "0 ft., fly 40 ft. (hover)"
stats: [3, 16, 12, 1, 10, 1]
damage_resistances: "bludgeoning, piercing, slashing"
condition_immunities: "charmed, frightened, grappled, paralyzed, petrified, prone, restrained, stunned"
senses: "blindsight 30 ft. (blind beyond this radius), passive Perception 10"
languages: "—"
cr: 8
traits:
  - name: "Silence Aura"
    desc: "The swarm generates a 30-foot-radius sphere of magical silence centered on itself. No sound can be created within or pass through the area. Casting a spell that requires a verbal component is impossible within the area."
  - name: "Swarm"
    desc: "The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening large enough for a Tiny insect. The swarm can't regain hit points or gain temporary hit points."
  - name: "Suffocating Cloud"
    desc: "A creature that starts its turn in the swarm's space must succeed on a DC 14 Constitution saving throw or begin suffocating as moths fill its nose and mouth. A suffocating creature can hold its breath for a number of rounds equal to its Constitution modifier (minimum 1 round) before it drops to 0 hit points. Removing itself from the swarm's space ends the effect."
actions:
  - name: "Engulf"
    desc: "Melee Weapon Attack: +6 to hit, reach 0 ft., one target in the swarm's space. Hit: 21 (6d6) piercing damage, or 10 (3d6) piercing damage if the swarm has half its hit points or fewer."
```
```
````

## Behavior

- **Habitat.** Rot and Grove approaches at dusk and dawn. Fire drives them off; they will not leave the trees.
- **Behavior.** Cloud advances with silence ahead, then fills mouths.
- **Diet.** Source is silent beyond smothering living prey in the swarm.
- **Social Structure.** Swarm.

## Tactics

- **Signs.** Jungle goes quiet; sail-sized colorless cloud.
- **Instincts.** Fill a mouth; stay among trees.
- **Tactics.** Advance under Silence Aura; Engulf creatures in the swarm's space; Suffocating Cloud on those who start turns inside.
- **Weaknesses.** Fire drives them off; they will not follow anyone out of the trees.
- **Aftermath.** Quiet resumes as the cloud breaks or burns away.
