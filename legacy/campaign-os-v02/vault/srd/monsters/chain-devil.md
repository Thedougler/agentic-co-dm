---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "Lawful Evil fiend with infernal chains, grappling, and magical resistance."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Chain Devil"
found_at:
- "[[calders-tooth|Calder's Tooth]]"
- "[[midchain-west|Midchain West]]"
uid: 7a3bef71-b7fc-4421-b4db-c1cea60ac405
---

# Chain Devil

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Chain Devil"
size: Medium
type: fiend
alignment: "Lawful Evil"
ac: 15
hp: 85
hit_dice: "10d8 + 40"
speed: "30 ft."
stats: [18, 15, 18, 11, 12, 14]
saves:
  - con: 7
  - wis: 4
damage_resistances: "Bludgeoning, Cold, Piercing, Slashing"
damage_immunities: "Fire, Poison"
condition_immunities: "Poisoned"
senses: "darkvision 120 ft. (unimpeded by magical darkness); Passive Perception 11"
languages: "Infernal; telepathy 120 ft."
cr: 8
traits:
  - name: "Diabolical Restoration"
    desc: "If the devil dies outside the Nine Hells, its body disappears in sulfurous smoke, and it gains a new body instantly, reviving with all its Hit Points somewhere in the Nine Hells."
  - name: "Magic Resistance"
    desc: "The devil has Advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "The devil makes two Chain attacks and uses Conjure Infernal Chain."
  - name: "Chain"
    desc: "*Melee Attack Roll:* +7, reach 10 ft. 11 (2d6 + 4) Slashing damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 14) from one of two chains, and it has the Restrained condition until the grapple ends."
  - name: "Conjure Infernal Chain"
    desc: "The devil conjures a fiery chain to bind a creature. *Dexterity Saving Throw*: DC 15, one creature the devil can see within 60 feet. *Failure:* 9 (2d4 + 4) Fire damage, and the target has the Restrained condition until the end of the devil's next turn, at which point the chain disappears. If the target is Large or smaller, the devil moves the target up to 30 feet straight toward itself. *Success:* The chain disappears."
```
