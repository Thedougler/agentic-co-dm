---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 13 huge amphibious giant with lightning sword and thunderbolt; casts Control Weather."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Storm Giant"
found_at:
- "[[outer-reach|Outer Reach]]"
- "[[central-strait|Central Strait]]"
uid: 383a8ef2-c597-40ec-8631-3780e119758c
---

# Storm Giant

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Storm Giant"
size: Huge
type: giant
alignment: "Chaotic Good"
ac: 16
hp: 230
hit_dice: "20d12 + 100"
speed: "50 ft., Fly 25 ft. (hover), Swim 50 ft."
stats: [29, 14, 20, 16, 20, 18]
saves:
  - str: 14
  - con: 10
  - wis: 10
  - cha: 9
damage_resistances: "Cold"
damage_immunities: "Lightning, Thunder"
senses: "darkvision 120 ft., truesight 30 ft.; Passive Perception 20"
languages: "Common, Giant"
cr: 13
traits:
  - name: "Amphibious"
    desc: "The giant can breathe air and water."
actions:
  - name: "Multiattack"
    desc: "The giant makes two attacks, using Storm Sword or Thunderbolt in any combination."
  - name: "Storm Sword"
    desc: "*Melee Attack Roll:* +14, reach 10 ft. 23 (4d6 + 9) Slashing damage plus 13 (3d8) Lightning damage."
  - name: "Thunderbolt"
    desc: "*Ranged Attack Roll:* +14, range 500 ft. 22 (2d12 + 9) Lightning damage, and the target has the Blinded and Deafened conditions until the start of the giant's next turn."
  - name: "Lightning Storm (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 18, each creature in a 10-foot-radius, 40-foot-high Cylinder [Area of Effect]|XPHB|Cylinder originating from a point the giant can see within 500 feet. *Failure:* 55 (10d10) Lightning damage. *Success:* Half damage."
  - name: "Spellcasting"
    desc: "The giant casts one of the following spells, requiring no Material components and using Wisdom as the spellcasting ability (spell save DC 18): - **At Will:** *Detect Magic*, *Light* - **1/Day Each:** *Control Weather*"
```
