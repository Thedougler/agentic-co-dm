---
title: "Aruhe - Thornback"
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "/workspace/midchain-ingest/group-a/monsters/Thornback.md"
summary: "CR 7 thorned bruiser from living-stock ecology."
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
cr: "7"
relationships:
  - target: "[[Aruhe]]"
    type: related_to
---
# Aruhe - Thornback

## Statblock

````col
```col-md
flexGrow=2
===
> [!narration] Narration
> Boar and porcupine with the off-switch gone: javelin quills on shoulder and rump, tusks grown through the skull and out again. Solitary animals root the Quiet floor and shove trails other beasts use afterward. Spent spines litter the path and regrow in hours.
```

```col-md
```statblock
layout: Basic 5e Layout
name: "Thornback"
size: Large
type: monstrosity
alignment: unaligned
ac: "16 (natural armor, quills)"
hp: 114
hit_dice: "12d10 + 48"
speed: "40 ft."
stats: [20, 10, 18, 3, 12, 5]
senses: "passive Perception 11"
languages: "—"
cr: 7
traits:
  - name: "Quill Defense"
    desc: "A creature that hits the thornback with a melee attack while within 5 feet of it takes 5 (2d4) piercing damage."
  - name: "Charge"
    desc: "If the thornback moves at least 20 feet straight toward a target and then hits it with a Gore attack on the same turn, the target takes an extra 9 (2d8) piercing damage. If the target is a creature, it must succeed on a DC 16 Strength saving throw or be knocked prone."
actions:
  - name: "Multiattack"
    desc: "The thornback makes two attacks: one with its Gore and one with its Quill Lash."
  - name: "Gore"
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 18 (3d8 + 5) piercing damage."
  - name: "Quill Lash"
    desc: "Melee Weapon Attack: +8 to hit, reach 10 ft., one target. Hit: 12 (2d6 + 5) piercing damage."
  - name: "Spine Volley (Recharge 5-6)"
    desc: "The thornback flings a spray of quills in a 15-foot cone. Each creature in the area must make a DC 15 Dexterity saving throw, taking 21 (6d6) piercing damage on a failed save, or half as much damage on a successful one."
```
```
````

## Behavior

- **Habitat.** [[Aruhe - Quiet Forest]] floor. Solitary — two fight each other first.
- **Behavior.** Roots and shoves trails other animals later use; quills shed and regrow in hours.
- **Diet.** Rooting Quiet floor forage and whatever the charge catches.
- **Social Structure.** Solitary; two in one stretch fight each other first.

## Tactics

- **Signs.** Javelin quills, tusks through skull, spent spines on trails.
- **Instincts.** Charge, gore, and quill; claim a stretch alone.
- **Tactics.** Charge into Gore; Quill Lash; Spine Volley when clustered prey allows.
- **Weaknesses.** Reach and formation answers; do not stand in the cone.
- **Aftermath.** Trails shoved open and littered with spent spines.
