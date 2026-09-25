---
title: "Aruhe - Thornback"
aliases:
  - Aruhe - Thornback
  - Thornbacks
category: entities
tags: [shattered-sea, aruhe, creature]
sources:
  - "/workspace/midchain-ingest/group-a/monsters/Thornback.md"
  - "campaign-os:thornbacks.md"
summary: "CR 7 blight-corrupted thorned bruiser that roots the Quiet floor and drives off other beasts."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
tier: supporting
created: 2026-09-13T20:00:00Z
updated: 2026-09-18T06:52:43Z
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

> [!narration] Narration
> Boar and porcupine with the off-switch gone: javelin quills on shoulder and rump, tusks grown through the skull and out again. Solitary animals root the Quiet floor and shove trails other beasts use afterward. Spent spines litter the path and regrow in hours.

## Statblock

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

## Behavior


- **Habitat.** [[the-quiet]] floor. It avoids other thornbacks because two in one stretch fight each other first.
- **Behavior.** The Blight fused boar aggression with a porcupine's defensive arsenal and removed the off switch. It roots through the jungle floor and shoves trails open. Shed quills regrow within hours.
- **Diet.** Rooting-floor forage and whatever the charge catches.
- **Social Structure.** Solitary. Two in one stretch fight each other first.

## Tactics


- **Signs.** Javelin quills, tusks through skull, spent spines on trails.
- **Instincts.** Charge, gore, and quill. It claims a stretch alone.
- **Tactics.** It opens with a charge into Gore, then follows with Quill Lash. It uses Spine Volley when prey clusters.
- **Weaknesses.** Reach and formation counter it. Do not stand in the cone.
- **Aftermath.** Trails shoved open and littered with spent spines.
