---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [faith]
summary: "CR 17 celestial sphinx with enchantment and control; frightens and paralyzes via roar, casts restoration and divination spells."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Sphinx of Valor"
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[outer-reach|Outer Reach]]"
uid: 945e7cf2-fbfc-4693-a7c2-7a252ac5d6d2
---

# Sphinx of Valor

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Sphinx of Valor"
size: Large
type: celestial
alignment: "Lawful Neutral"
ac: 17
hp: 199
hit_dice: "19d10 + 95"
speed: "40 ft., Fly 60 ft."
stats: [22, 10, 20, 16, 23, 18]
saves:
  - dex: 6
  - con: 11
  - int: 9
  - wis: 12
damage_resistances: "Necrotic, Radiant"
damage_immunities: "Psychic"
condition_immunities: "Charmed, Frightened"
senses: "truesight 120 ft.; Passive Perception 22"
languages: "Celestial, Common"
cr: 17
traits:
  - name: "Inscrutable"
    desc: "No magic can observe the sphinx remotely or detect its thoughts without its permission. Wisdom (Insight) checks made to ascertain its intentions or sincerity are made with Disadvantage."
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the sphinx fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The sphinx makes two Claw attacks and uses Roar."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +12, reach 5 ft. 20 (4d6 + 6) Slashing damage."
  - name: "Roar (3/Day)"
    desc: "The sphinx emits a magical roar. Whenever it roars, the roar has a different effect, as detailed below (the sequence resets when it takes a Long Rest): - **First Roar**: *Wisdom Saving Throw*: DC 20, each enemy in a 500-foot Emanation originating from the sphinx. *Failure:* The target has the Frightened condition for 1 minute. - **Second Roar**: *Wisdom Saving Throw*: DC 20, each enemy in a 500-foot Emanation originating from the sphinx. *Failure:* The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically. - **Third Roar**: *Constitution Saving Throw*: DC 20, each enemy in a 500-foot Emanation originating from the sphinx. *Failure:* 44 (8d10) Thunder damage, and the target has the Prone condition. *Success:* Half damage only."
  - name: "Spellcasting"
    desc: "The sphinx casts one of the following spells, requiring no Material components and using Wisdom as the spellcasting ability (spell save DC 20): - **At Will:** *Detect Evil and Good*, *Thaumaturgy* - **1e/Day Each:** *Detect Magic*, *Dispel Magic*, *Greater Restoration*, *Heroes' Feast*, *Zone of Truth*"
legendary_actions:
  - name: "Arcane Prowl"
    desc: "The sphinx can teleport up to 30 feet to an unoccupied space it can see, and it makes one Claw attack."
  - name: "Weight of Years"
    desc: "*Constitution Saving Throw*: DC 16, one creature the sphinx can see within 120 feet. *Failure:* The target gains 1 Exhaustion level. While the target has any Exhaustion levels, it appears 3d10 years older. *Failure or Success*: The sphinx can't take this action again until the start of its next turn."
```
