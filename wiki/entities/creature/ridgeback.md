---
title: Ridgeback
category: entities
tags: [shattered-sea, creature]
sources:
  - "elemental-plane-of-water.md"
  - "synthesis/party-combat-profile.md"
summary: Blind aquatic ambusher from the Maw fissure; its telegraphed ridge charge knocks prey prone before it bites.
provenance:
  extracted: 0.65
  inferred: 0.35
  ambiguous: 0.0
invention: true
tier: supporting
created: 2026-09-13T21:05:00Z
updated: 2026-09-27
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
relationships:
  - target: "[[elemental-plane-of-water]]"
    type: related_to
  - target: "[[drowned-maw]]"
    type: related_to
region: ""
role: ambusher
cr: 7
---
# Ridgeback

````col
```col-md
flexGrow=2
===
## At a Glance

Ridgeback is a blind aquatic ambusher from the [[drowned-maw|Drowned Maw]] fissure. It exposes a rising dorsal ridge before its charge, giving the party a visible chance to scatter or take cover.

- **Habitat.** The fissure at [[drowned-maw|Drowned Maw]] and the surrounding waters.
- **Role.** Ambusher that knocks one target prone, then follows with a bite.
- **Origin.** The second named entity drawn through the [[elemental-plane-of-water|Elemental Plane of Water]] fissure, documented in Clyde's Bestiary.
```

```col-md
flexGrow=1
===
> [!narration] Ridgeback
> Flat-black skin rolls through the water like wet stone, with no eyes anywhere on its blunt head. A hard ridge runs from its skull down its back. It turns toward the smallest splash, then rises until the ridge cuts the surface and the water pulls into a straight wake behind it.
``` 
````

## Statblock

The source establishes Ridgeback's flat-black skin, eyeless head, blindsight, and water breathing. The combat chassis below is the authored table version for a Hard threat to the four level-5 PCs in the party combat profile.

```statblock
layout: Basic 5e Layout
name: "Ridgeback"
size: Large
type: elemental
alignment: unaligned
ac: "16 (natural armor)"
hp: 142
hit_dice: "15d10 + 60"
speed: "30 ft., swim 60 ft."
stats: [20, 14, 18, 4, 14, 8]
saves:
  - Strength: +8
  - Constitution: +7
skillsaves:
  - Perception: +5
  - Stealth: +5
senses: "Blindsight 60 ft., passive Perception 15"
languages: "—"
cr: "7"
traits:
  - name: "Water Breathing"
    desc: "The Ridgeback can breathe underwater."
  - name: "Submerged Ambusher"
    desc: "While underwater, the Ridgeback has Advantage on Dexterity (Stealth) checks made to hide among rock, wreckage, or other cover."
actions:
  - name: "Multiattack"
    desc: "The Ridgeback makes one Bite attack and one Tail attack."
  - name: "Bite"
    desc: "Melee Attack Roll: +8, reach 5 ft. Hit: 16 (2d10 + 5) Piercing damage."
  - name: "Tail"
    desc: "Melee Attack Roll: +8, reach 10 ft. Hit: 14 (2d8 + 5) Bludgeoning damage."
  - name: "Ridge Charge (Recharge 5–6)"
    desc: "The Ridgeback swims up to its Swim Speed in a straight line. When it enters a creature's space, that creature must make a DC 16 Dexterity saving throw. Failure: 18 (4d8) Bludgeoning damage, and the target has the Prone condition. Success: Half damage only. The Ridgeback cannot use Ridge Charge if it cannot move at least 20 feet."
```

## Tactics

- **Opening.** The Ridgeback hides underwater, rises behind cover, and uses Ridge Charge against an isolated creature or the character nearest the water.
- **Signature.** The dorsal ridge rises and the water draws into a straight wake before Ridge Charge. The party can scatter, move behind solid cover, or ready movement away from the line. If the charge lands, the Ridgeback follows with Multiattack against the prone target.
- **Weaknesses.** It cannot use Ridge Charge without a straight 20-foot lane. Bright open water and solid cover deny its Stealth advantage, and open air forces it to use its walking speed.
- **Morale.** It retreats into the fissure when reduced to 29 hit points or fewer. It does not fight to the death unless cornered away from water.

> [!narration] In action
> The ridge rises through the black water and a narrow wake draws tight behind it. The creature surges along that wake, its blunt head vanishing beneath the surface before its full weight breaks through where you stood.

## Behavior

- **Habits.** Ridgeback waits motionless in dark water and turns toward splashes, disturbed silt, and hull vibrations.
- **Diet.** No source establishes its diet. Use the creature's attacks and ambush behavior without adding a diet claim.
- **Group.** No source establishes whether Ridgeback is solitary or social. The named entity is treated as a solitary encounter unless another page says otherwise.
- **Body.** Ridgeback has flat-black skin, no eyes, blindsight, and water breathing. Its dorsal ridge is the visible tell for Ridge Charge.
- **Signs.** A straight wake, disturbed silt, scrape marks on submerged rock, and a sudden absence of ordinary water movement precede Ridge Charge.
- **Aftermath.** A charge leaves a clean lane through silt and loose wreckage, while the bitten target's blood draws a dark cloud through the water.

## Secrets

Ridgeback is not an unrelated sea predator. It is the second of at least three entities drawn through the [[drowned-maw|Drowned Maw]] fissure from the [[elemental-plane-of-water|Elemental Plane of Water]], alongside [[Leviathan]] and [[Krakling]]. The flat-black, eyeless hide and blindsight are the evidence that links them.

## Connections

- [[drowned-maw|Drowned Maw]] — the fissure through which Ridgeback crossed.
- [[elemental-plane-of-water|Elemental Plane of Water]] — Ridgeback's source plane.
- [[algernon-reginald-clyde|Algernon Reginald Clyde]] — author of Clyde's Bestiary, which documents Ridgeback.
