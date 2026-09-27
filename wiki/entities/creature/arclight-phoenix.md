---
title: Arclight Phoenix
aliases:
  - Arclight Phoenix
category: entities
tags: [shattered-sea, creature]
sources: ["ashwall-islands.md"]
summary: Storm-edge phoenix that hatches from lightning-opened eggs in Ashwall vents and flies west into the Galewall.
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
tier: supporting
created: 2026-09-13T20:40:00Z
updated: 2026-09-13T20:40:00Z
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
region: Ashwalls
role: storm hatch
relationships:
  - target: "[[Ashwalls]]"
    type: related_to
  - target: "[[galewall]]"
    type: related_to
cr: "5"
invention: true
---
# Arclight Phoenix

> [!narration] Arclight Phoenix
> A white bird of stormlight can show in the rigging. Lateral fire branches through ash and holds for a breath before it fades.

## At a Glance

Arclight Phoenixes are storm-edge elemental predators that hatch in the volcanic [[Ashwalls]] and fly west into the [[galewall]].

- **Habitat.** Warm volcanic vents and fissures in the [[Ashwalls]], especially along the storm edge.
- **Hatch sign.** Lateral lightning through ash opens an egg; a dead phoenix leaves its egg in the volcano.

## Statblock

```statblock
layout: Basic 5e Layout
name: "Arclight Phoenix"
size: Medium
type: elemental
alignment: unaligned
ac: 15
hp: 65
hit_dice: "10d8 + 20"
speed: "30 ft., fly 60 ft."
stats: [10, 18, 14, 8, 14, 12]
saves:
  - dexterity: 6
  - wisdom: 5
damage_resistances: "Lightning"
senses: "darkvision 60 ft., passive Perception 12"
languages: "—"
cr: "5"
traits:
  - name: "Storm Body"
    desc: "When a creature within 5 feet hits the phoenix with a melee attack, that creature takes 3 (1d6) Lightning damage."
actions:
  - name: "Multiattack"
    desc: "The phoenix makes two Talon attacks."
  - name: "Talon"
    desc: "Melee Attack Roll: +7, reach 5 ft. Hit: 8 (1d8 + 4) Slashing damage plus 3 (1d6) Lightning damage."
  - name: "Lateral Arc (Recharge 5–6)"
    desc: "The phoenix sends lightning through a 30-foot-long, 5-foot-wide Line. Each creature in the Line makes a DC 14 Dexterity Saving Throw. Failure: 18 (4d8) Lightning damage. Success: Half damage."
```

## Tactics

**Hunt.**

The phoenix opens with Lateral Arc when prey clusters, then closes on an isolated target with its talons. Its lateral fire branches visibly through the ash before the arc strikes. A creature that keeps its distance and spreads out denies the phoenix both its line and its melee retaliation. It flees into the storm when reduced to 16 Hit Points or fewer.

## Behavior

**Life.**

When an [[arclight-phoenix]] dies, its egg remains in the [[Ashwalls]] volcanoes. Lightning opens the egg. The bird emerges oriented toward the storm edge and flies west into the [[galewall]]. It does not return until it dies again in the weather.
