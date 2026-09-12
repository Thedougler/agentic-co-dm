---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [faith]
summary: "CR 10 celestial naga with poison damage, spittle attack, and healing spells."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Guardian Naga"
found_at:
- "[[sunken-crown|Sunken Crown]]"
- "[[crown-islands|Crown Islands]]"
uid: bd4b32ef-08ba-4f07-89e8-c3cf8914133c
---

# Guardian Naga

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Guardian Naga"
size: Large
type: celestial
alignment: "Lawful Good"
ac: 18
hp: 136
hit_dice: "16d10 + 48"
speed: "40 ft., Climb 40 ft., Swim 40 ft."
stats: [19, 18, 16, 16, 19, 18]
saves:
  - dex: 8
  - con: 7
  - int: 7
  - wis: 8
  - cha: 8
damage_immunities: "Poison"
condition_immunities: "Charmed, Paralyzed, Poisoned, Restrained"
senses: "darkvision 60 ft.; Passive Perception 14"
languages: "Celestial, Common"
cr: 10
traits:
  - name: "Celestial Restoration"
    desc: "If the naga dies, it returns to life in 1d6 days and regains all its Hit Points unless *Dispel Evil and Good* is cast on its remains."
actions:
  - name: "Multiattack"
    desc: "The naga makes two Bite attacks. It can replace any attack with a use of Poisonous Spittle."
  - name: "Bite"
    desc: "*Melee Attack Roll:* +8, reach 10 ft. 17 (2d12 + 4) Piercing damage plus 22 (4d10) Poison damage."
  - name: "Poisonous Spittle"
    desc: "*Constitution Saving Throw*: DC 16, one creature the naga can see within 60 feet. *Failure:* 31 (7d8) Poison damage, and the target has the Blinded condition until the start of the naga's next turn. *Success:* Half damage only."
  - name: "Spellcasting"
    desc: "The naga casts one of the following spells, requiring no Somatic or Material components and using Wisdom as the spellcasting ability (spell save DC 16): - **At Will:** *Thaumaturgy* - **1e/Day Each:** *Clairvoyance*, *Cure Wounds*, *Flame Strike*, *Geas*, *True Seeing*"
```
