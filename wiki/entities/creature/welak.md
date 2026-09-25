---
title: "Welak"
category: entities
tags: [shattered-sea, creature]
sources:
  - "campaign-os:whip-shark.md"
  - "/workspace/midchain-ingest/group-a/monsters/Welak.md"
summary: "CR 5 surface ambusher also called whip shark; follows salvage-pump vibration and hits hull or crew before a reload."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
tier: supporting
created: 2026-09-13T19:55:00Z
updated: 2026-09-13T19:55:00Z
type: creature
reveal: revealed
campaign: shattered-sea
visibility: dm
role: ambusher
cr: "5"
relationships:
  - target: "[[drowned-maw]]"
    type: related_to
  - target: "[[Uncertainty]]"
    type: related_to
region: ""
---
# Welak

> [!narration] Narration
> The first thing seen is the lower barb riding proud of the water. Then the hull takes it.

## Statblock

```statblock
layout: Basic 5e Layout
name: Welak / Whip Shark
size: Large
type: monstrosity
alignment: unaligned
ac: "15"
hp: 95
hit_dice: "10d10 + 40"
speed: 10 ft., swim 60 ft.
stats: [20, 16, 18, 3, 14, 5]
saves:
  - Str: +8
  - Con: +7
skillsaves:
  - Perception: +5
  - Stealth: +6
senses: "passive Perception 15"
languages: "—"
cr: 5
traits:
  - name: Vibration Hunter
    desc: "While in water, Welak knows the location of each moving vessel within 120 feet of it. It has Advantage on Wisdom (Perception) checks made to detect a vessel or its machinery, and it follows salvage-pump vibration more readily than blood."
  - name: Surface Ambush
    desc: "Once per turn, when Welak hits a creature while it is Hidden from that creature, the attack deals an extra 7 (2d6) damage."
actions:
  - name: Multiattack
    desc: "Welak makes one Bite attack and one Barb Hook attack."
  - name: Bite
    desc: "Melee Attack Roll: +8, reach 5 ft., one target. Hit: 18 (2d10 + 7) piercing damage."
  - name: Barb Hook
    desc: "Melee Attack Roll: +8, reach 10 ft., one target. Hit: 17 (2d8 + 8) piercing damage. If the target is a creature, it must succeed on a DC 15 Strength saving throw or be pulled up to 10 feet toward Welak and Grappled (escape DC 15). If the target is a vessel, its hull takes 4 extra piercing damage and the vessel's Speed is reduced by 10 feet until Welak moves."
```

## Behavior


- **Habitat.** [[drowned-maw]] waters and Shelfworks salvage approaches. A fed Welak rarely leaves the Maw. The specimen that struck the [[Uncertainty]] west of Calveno was an outlier.
- **Behavior.** Surfaces once, fast, and attacks wood before a crew can reload. Follows salvage-pump vibration more than blood.
- **Diet.** Ship-side prey and whatever the ambush yields; fed animals turn back toward the Maw.
- **Social Structure.** Source is silent on packs; run as a singular ambusher unless another source says otherwise.

## Tactics


- **Signs.** Lower barb riding high; pump vibration drawing approach.
- **Instincts.** Hit hull or exposed deck first; prefer vibration over blood scent.
- **Tactics.** Hidden surface pass with Barb Hook; Multiattack once revealed; retreat toward the Maw when fed.
- **Weaknesses.** Quiet or redirect the pump; move the vessel; Ready attacks for the surface pass; cut a lodged barb; force an open fight without the ambush angle.
- **Aftermath.** A retreat after feeding is a successful ecology outcome, not a failed combat.
