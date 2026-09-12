---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 8 demonic fiend with stench aura, magic resistance, and regeneration."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Hezrou"
found_at:
- "[[sorrowbell|Sorrowbell]]"
- "[[crown-islands|Crown Islands]]"
uid: 8e8003ed-a5bc-42c0-a07e-04571325e9a6
---

# Hezrou

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Hezrou"
size: Large
type: fiend
alignment: "Chaotic Evil"
ac: 18
hp: 157
hit_dice: "15d10 + 75"
speed: "30 ft."
stats: [19, 17, 20, 5, 12, 13]
saves:
  - str: 7
  - con: 8
  - wis: 4
damage_resistances: "Cold, Fire, Lightning"
damage_immunities: "Poison"
condition_immunities: "Poisoned"
senses: "darkvision 120 ft.; Passive Perception 11"
languages: "Abyssal; telepathy 120 ft."
cr: 8
traits:
  - name: "Demonic Restoration"
    desc: "If the hezrou dies outside the Abyss, its body dissolves into ichor, and it gains a new body instantly, reviving with all its Hit Points somewhere in the Abyss."
  - name: "Magic Resistance"
    desc: "The hezrou has Advantage on saving throws against spells and other magical effects."
  - name: "Stench"
    desc: "*Constitution Saving Throw*: DC 16, any creature that starts its turn in a 10-foot Emanation originating from the hezrou. *Failure:* The target has the Poisoned condition until the start of its next turn."
actions:
  - name: "Multiattack"
    desc: "The hezrou makes three Rend attacks."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 6 (1d4 + 4) Slashing damage plus 9 (2d8) Poison damage."
bonus_actions:
  - name: "Leap"
    desc: "The hezrou jumps up to 30 feet by spending 10 feet of movement."
```
