---
type: monster
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 17 Gargantuan dragon turtle with Fire breath, powerful multiattack, and massive durability."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Dragon Turtle"
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[outer-reach|Outer Reach]]"
uid: bf8fb592-eff6-497a-829b-e568e8729200
---

# Dragon Turtle

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Dragon Turtle"
size: Gargantuan
type: dragon
alignment: "Neutral"
ac: 20
hp: 356
hit_dice: "23d20 + 115"
speed: "20 ft., Swim 50 ft."
stats: [25, 10, 20, 10, 12, 12]
saves:
  - con: 11
  - wis: 7
damage_resistances: "Fire"
senses: "darkvision 120 ft.; Passive Perception 11"
languages: "Draconic, Primordial (Aquan)"
cr: 17
traits:
  - name: "Amphibious"
    desc: "The dragon can breathe air and water."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Bite attacks. It can replace one attack with a Tail attack."
  - name: "Bite"
    desc: "*Melee Attack Roll:* +13, reach 15 ft. 23 (3d10 + 7) Piercing damage plus 7 (2d6) Fire damage. Being underwater doesn't grant Resistance to this Fire damage."
  - name: "Tail"
    desc: "*Melee Attack Roll:* +13, reach 15 ft. 18 (2d10 + 7) Bludgeoning damage. If the target is a Huge or smaller creature, it has the Prone condition."
  - name: "Steam Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 19, each creature in a 60-foot Cone. *Failure:* 56 (16d6) Fire damage. *Success:* Half damage. *Failure or Success*: Being underwater doesn't grant Resistance to this Fire damage."
```
