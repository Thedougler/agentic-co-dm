---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "CR 1/4 undead melee combatant with Undead Fortitude to reduce lethal damage."
found_at:
- "[[doldrums|Doldrums]]"
- "[[orak|Orak]]"
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Zombie"
uid: c8b5bb85-b254-4669-a258-e97f9ec4af6b
---

# Zombie

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Zombie"
size: Medium
type: undead
alignment: "Neutral Evil"
ac: 8
hp: 15
hit_dice: "2d8 + 6"
speed: "20 ft."
stats: [13, 6, 16, 3, 6, 5]
saves:
  - wis: 0
damage_immunities: "Poison"
condition_immunities: "Exhaustion, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 8"
languages: "Understands Common plus one other language but can't speak"
cr: "1/4"
traits:
  - name: "Undead Fortitude"
    desc: "If damage reduces the zombie to 0 Hit Points, it makes a Constitution saving throw (DC 5 plus the damage taken) unless the damage is Radiant or from a Critical Hit. On a successful save, the zombie drops to 1 Hit Point instead."
actions:
  - name: "Slam"
    desc: "*Melee Attack Roll:* +3, reach 5 ft. 5 (1d8 + 1) Bludgeoning damage."
```
