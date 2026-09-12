---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [faith]
summary: "A CR 11 celestial guardian with powerful psychic roar, extensive magical knowledge, and inscrutability."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Sphinx of Lore"
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[outer-reach|Outer Reach]]"
uid: 8c2034b6-b95e-4d58-9b9c-f314641c043c
---

# Sphinx of Lore

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Sphinx of Lore"
size: Large
type: celestial
alignment: "Lawful Neutral"
ac: 17
hp: 170
hit_dice: "20d10 + 60"
speed: "40 ft., Fly 60 ft."
stats: [18, 15, 16, 18, 18, 18]
damage_resistances: "Necrotic, Radiant"
damage_immunities: "Psychic"
condition_immunities: "Charmed, Frightened"
senses: "truesight 120 ft.; Passive Perception 18"
languages: "Celestial, Common"
cr: 11
traits:
  - name: "Inscrutable"
    desc: "No magic can observe the sphinx remotely or detect its thoughts without its permission. Wisdom (Insight) checks made to ascertain its intentions or sincerity are made with Disadvantage."
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the sphinx fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The sphinx makes three Claw attacks."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +8, reach 5 ft. 14 (3d6 + 4) Slashing damage."
  - name: "Mind-Rending Roar (Recharge 5-6)"
    desc: "*Wisdom Saving Throw*: DC 16, each enemy in a 300-foot Emanation originating from the sphinx. *Failure:* 35 (10d6) Psychic damage, and the target has the Incapacitated condition until the start of the sphinx's next turn."
  - name: "Spellcasting"
    desc: "The sphinx casts one of the following spells, requiring no Material components and using Intelligence as the spellcasting ability (spell save DC 16): - **At Will:** *Detect Magic*, *Identify*, *Mage Hand*, *Minor Illusion*, *Prestidigitation* - **1e/Day Each:** *Dispel Magic*, *Legend Lore*, *Locate Object*, *Plane Shift*, *Remove Curse*, *Tongues*"
legendary_actions:
  - name: "Arcane Prowl"
    desc: "The sphinx can teleport up to 30 feet to an unoccupied space it can see, and it makes one Claw attack."
  - name: "Weight of Years"
    desc: "*Constitution Saving Throw*: DC 16, one creature the sphinx can see within 120 feet. *Failure:* The target gains 1 Exhaustion level. While the target has any Exhaustion levels, it appears 3d10 years older. *Failure or Success*: The sphinx can't take this action again until the start of its next turn."
```
