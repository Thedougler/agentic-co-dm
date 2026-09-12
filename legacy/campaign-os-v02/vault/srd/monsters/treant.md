---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [nature]
summary: "Huge CR 9 plant (138 HP, AC 16) resisting physical damage, vulnerable to fire, with slams, bark attacks, and tree animation."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Treant"
found_at:
- "[[midchain-west|Midchain West]]"
- "[[verdant-teeth|Verdant Teeth]]"
uid: ef565cc6-636c-4c8c-9f1d-9de19ddcd68a
---

# Treant

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Treant"
size: Huge
type: plant
alignment: "Chaotic Good"
ac: 16
hp: 138
hit_dice: "12d12 + 60"
speed: "30 ft."
stats: [23, 8, 21, 12, 16, 12]
damage_resistances: "Bludgeoning, Piercing"
damage_vulnerabilities: "Fire"
senses: "Passive Perception 13"
languages: "Common, Druidic, Elvish, Sylvan"
cr: 9
traits:
  - name: "Siege Monster"
    desc: "The treant deals double damage to objects and structures."
actions:
  - name: "Multiattack"
    desc: "The treant makes two Slam attacks."
  - name: "Slam"
    desc: "*Melee Attack Roll:* +10, reach 5 ft. 16 (3d6 + 6) Bludgeoning damage."
  - name: "Hail of Bark"
    desc: "*Ranged Attack Roll:* +10, range 180 ft. 28 (4d10 + 6) Piercing damage."
  - name: "Animate Trees (1/Day)"
    desc: "The treant magically animates up to two trees it can see within 60 feet of itself. Each tree uses the Treant stat block, except it has Intelligence and Charisma scores of 1, it can't speak, and it lacks this action. The tree takes its turn immediately after the treant on the same Initiative count, and it obeys the treant. A tree remains animate for 1 day or until it dies, the treant dies, or it is more than 120 feet from the treant. The tree then takes root if possible."
```
