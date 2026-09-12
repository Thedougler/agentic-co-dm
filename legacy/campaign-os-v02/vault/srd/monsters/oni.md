---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 7 fiend with regeneration, necrotic claws, psychic rays, and shapeshifting magic."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[doldrums|Doldrums]]"
- "[[crown-islands|Crown Islands]]"
statblock: inline
name: "Oni"
uid: 572d18f7-3a1c-4001-94f8-0e82872613c8
---

# Oni

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Oni"
size: Large
type: fiend
alignment: "Lawful Evil"
ac: 17
hp: 119
hit_dice: "14d10 + 42"
speed: "30 ft., Fly 30 ft. (hover)"
stats: [19, 11, 16, 14, 12, 15]
saves:
  - dex: 3
  - con: 6
  - wis: 4
  - cha: 5
damage_resistances: "Cold"
senses: "darkvision 60 ft.; Passive Perception 14"
languages: "Common, Giant"
cr: 7
traits:
  - name: "Regeneration"
    desc: "The oni regains 10 Hit Points at the start of each of its turns if it has at least 1 Hit Point."
actions:
  - name: "Multiattack"
    desc: "The oni makes two Claw or Nightmare Ray attacks. It can replace one attack with a use of Spellcasting."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +7, reach 10 ft. 10 (1d12 + 4) Slashing damage plus 9 (2d8) Necrotic damage."
  - name: "Nightmare Ray"
    desc: "*Ranged Attack Roll:* +5, range 60 ft. 9 (2d6 + 2) Psychic damage, and the target has the Frightened condition until the start of the oni's next turn."
  - name: "Shape-Shift"
    desc: "The oni shape-shifts into a Small or Medium Humanoid or a Large Giant, or it returns to its true form. Other than its size, its game statistics are the same in each form. Any equipment it is wearing or carrying isn't transformed."
  - name: "Spellcasting"
    desc: "The oni casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 13): - **At Will:** - **1e/Day Each:** *Charm Person*, *Darkness*, *Gaseous Form*, *Sleep*"
bonus_actions:
  - name: "Invisibility"
    desc: "The oni casts *Invisibility* on itself, requiring no spell components and using the same spellcasting ability as Spellcasting."
```
