---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "Huge giant (CR 9) with hovering flight, Thunderous Mace melee, Thundercloud ranged attack, and extensive spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Cloud Giant"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[outer-reach|Outer Reach]]"
uid: c79da8d1-0939-4299-85fe-a84efaf0648b
---

# Cloud Giant

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Cloud Giant"
size: Huge
type: giant
alignment: "Neutral"
ac: 14
hp: 200
hit_dice: "16d12 + 96"
speed: "40 ft., Fly 20 ft. (hover)"
stats: [27, 10, 22, 12, 16, 16]
saves:
  - con: 10
  - wis: 7
senses: "Passive Perception 21"
languages: "Common, Giant"
cr: 9
actions:
  - name: "Multiattack"
    desc: "The giant makes two attacks, using Thunderous Mace or Thundercloud in any combination. It can replace one attack with a use of Spellcasting to cast *Fog Cloud*."
  - name: "Thunderous Mace"
    desc: "*Melee Attack Roll:* +12, reach 10 ft. 21 (3d8 + 8) Bludgeoning damage plus 7 (2d6) Thunder damage."
  - name: "Thundercloud"
    desc: "*Ranged Attack Roll:* +12, range 240 ft. 18 (3d6 + 8) Thunder damage, and the target has the Incapacitated condition until the end of its next turn."
  - name: "Spellcasting"
    desc: "The giant casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 15): - **At Will:** *Detect Magic*, *Fog Cloud*, *Light* - **1e/Day Each:** *Control Weather*, *Gaseous Form*, *Telekinesis*"
bonus_actions:
  - name: "Misty Step"
    desc: "The giant casts the *Misty Step* spell, using the same spellcasting ability as Spellcasting."
```
