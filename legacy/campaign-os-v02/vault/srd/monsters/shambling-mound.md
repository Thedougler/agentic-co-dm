---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [nature]
summary: "A CR 5 plant creature that absorbs lightning to heal and uses charged tendrils to pull and engulf foes."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[verdant-teeth|Verdant Teeth]]"
- "[[midchain-south|Midchain South]]"
statblock: inline
name: "Shambling Mound"
uid: 8de23148-9a20-4802-b4e2-b6b484dde838
---

# Shambling Mound

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Shambling Mound"
size: Large
type: plant
alignment: "Unaligned"
ac: 15
hp: 110
hit_dice: "13d10 + 39"
speed: "30 ft., Swim 20 ft."
stats: [18, 8, 16, 5, 10, 5]
damage_resistances: "Cold, Fire"
damage_immunities: "Lightning"
condition_immunities: "Deafened, Exhaustion"
senses: "blindsight 60 ft.; Passive Perception 10"
cr: 5
traits:
  - name: "Lightning Absorption"
    desc: "Whenever the shambling mound is subjected to Lightning damage, it regains a number of Hit Points equal to the Lightning damage dealt."
actions:
  - name: "Multiattack"
    desc: "The shambling mound makes three Charged Tendril attacks. It can replace one attack with a use of Engulf."
  - name: "Charged Tendril"
    desc: "*Melee Attack Roll:* +7, reach 10 ft. 7 (1d6 + 4) Bludgeoning damage plus 5 (2d4) Lightning damage. If the target is a Medium or smaller creature, the shambling mound pulls the target 5 feet straight toward itself."
  - name: "Engulf"
    desc: "*Strength Saving Throw*: DC 15, one Medium or smaller creature within 5 feet. *Failure:* The target is pulled into the shambling mound's space and has the Grappled condition (escape DC 14). Until the grapple ends, the target has the Blinded and Restrained conditions, and it takes 10 (3d6) Lightning damage at the start of each of its turns. When the shambling mound moves, the Grappled target moves with it, costing it no extra movement. The shambling mound can have only one creature Grappled by this action at a time."
```
