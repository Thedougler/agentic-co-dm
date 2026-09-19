---
title: "Aruhe - Grinning Ape"
aliases:
  - Aruhe - Grinning Ape
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "campaign-os:grinning-apes.md"
  - "/workspace/midchain-ingest/group-a/monsters/Grinning Ape.md"
summary: "CR 6 Aruhe bruiser ape from living-stock ecology."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.42
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T20:00:00Z
updated: 2026-09-13T20:00:00Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: aruhe
role: "bruiser"
cr: "6"
relationships:
  - target: "[[Aruhe]]"
    type: related_to
---
# Aruhe - Grinning Ape

## Statblock

````col
```col-md
flexGrow=2
===
> [!narration] Narration
> Gorilla-sized, dark-furred apes sit in the terrace canopy in groups of three and five. Their faces are locked in a rictus that never changes; they do not groom or call. Stones come first, then the group drops as one on whatever moved below.
```

```col-md
```statblock
layout: Basic 5e Layout
name: "Grinning Ape"
size: Large
type: monstrosity
alignment: unaligned
ac: "14 (natural armor)"
hp: 95
hit_dice: "10d10 + 40"
speed: "40 ft., climb 40 ft."
stats: [18, 16, 18, 5, 14, 4]
skillsaves:
  - Athletics: +7
  - Stealth: +6
senses: "darkvision 60 ft., passive Perception 12"
languages: "—"
cr: 6
traits:
  - name: "Canopy Prowler"
    desc: "The grinning ape has advantage on Dexterity (Stealth) checks made in forested or jungle terrain while among trees."
  - name: "Pack Ambush"
    desc: "If the grinning ape hits a creature that hasn't taken a turn yet in combat, the attack deals an extra 7 (2d6) damage."
actions:
  - name: "Multiattack"
    desc: "The grinning ape makes two attacks: one with its Bite and one with its Fist."
  - name: "Bite"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 13 (2d8 + 4) piercing damage."
  - name: "Fist"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (2d6 + 4) bludgeoning damage."
  - name: "Rock"
    desc: "Ranged Weapon Attack: +7 to hit, range 30/60 ft., one target. Hit: 15 (2d10 + 4) bludgeoning damage."
```
```
````

## Behavior

- **Habitat.** [[old-gardens]] terraces. Groups of three to five.
- **Behavior.** Silent canopy sitters; stones first, then a group drop.
- **Diet.** Whatever moved below the terrace canopy.
- **Social Structure.** Groups of three to five. No grooming or calls.

## Tactics

- **Signs.** Rictus grins never change. Stones fall from above without a warning call.
- **Instincts.** Ambush from canopy as a group.
- **Tactics.** Rock from canopy, then drop together. Use Pack Ambush on creatures that have not acted.
- **Weaknesses.** Source is silent beyond ordinary combat answers.
- **Aftermath.** Disturbed terrace canopy and scattered stones.
