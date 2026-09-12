---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "A Medium Neutral Evil wight (CR 3) that drains life with necrotic weapons and can raise slain Humanoids as zombies."
found_at:
- "[[doldrums|Doldrums]]"
- "[[the-drowned-maw|The Drowned Maw]]"
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Wight"
uid: af317629-5ef2-42c0-ade0-f82e226b2112
---

# Wight

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Wight"
size: Medium
type: undead
alignment: "Neutral Evil"
ac: 14
hp: 82
hit_dice: "11d8 + 33"
speed: "30 ft."
stats: [15, 14, 16, 10, 13, 15]
damage_resistances: "Necrotic"
damage_immunities: "Poison"
condition_immunities: "Exhaustion, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 13"
languages: "Common plus one other language"
cr: 3
traits:
  - name: "Sunlight Sensitivity"
    desc: "While in sunlight, the wight has Disadvantage on ability checks and attack rolls."
actions:
  - name: "Multiattack"
    desc: "The wight makes two attacks, using Necrotic Sword or Necrotic Bow in any combination. It can replace one attack with a use of Life Drain."
  - name: "Necrotic Sword"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. 6 (1d8 + 2) Slashing damage plus 4 (1d8) Necrotic damage."
  - name: "Necrotic Bow"
    desc: "*Ranged Attack Roll:* +4, range 150/600 ft. 6 (1d8 + 2) Piercing damage plus 4 (1d8) Necrotic damage."
  - name: "Life Drain"
    desc: "*Constitution Saving Throw*: DC 13, one creature within 5 feet. *Failure:* 6 (1d8 + 2) Necrotic damage, and the target's Hit Point maximum decreases by an amount equal to the damage taken. A Humanoid slain by this attack rises 24 hours later as a Zombie under the wight's control, unless the Humanoid is restored to life or its body is destroyed. The wight can have no more than twelve zombies under its control at a time."
```
