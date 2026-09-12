---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, intrigue]
summary: "CR 6 Small humanoid spellcaster with Arcane Burst and protective magic reactions."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Mage"
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[central-strait|Central Strait]]"
uid: 4fd81c3d-7ffa-4ad2-8652-50fad49bbc44
---

# Mage

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Mage"
size: Small
type: humanoid
alignment: "Neutral"
ac: 15
hp: 81
hit_dice: "18d8"
speed: "30 ft."
stats: [9, 14, 11, 17, 12, 11]
saves:
  - int: 6
  - wis: 4
senses: "Passive Perception 14"
languages: "Common and any three languages"
cr: 6
actions:
  - name: "Multiattack"
    desc: "The mage makes three Arcane Burst attacks."
  - name: "Arcane Burst"
    desc: "*Melee or Ranged Attack Roll:* +6, reach 5 ft. or range 120 ft. 16 (3d8 + 3) Force damage."
  - name: "Spellcasting"
    desc: "The mage casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 14): - **At Will:** *Detect Magic*, *Light*, *Mage Armor*, *Mage Hand*, *Prestidigitation* - **2e/Day Each:** *Fireball*, *Invisibility* - **1e/Day Each:** *Cone of Cold*, *Fly*"
bonus_actions:
  - name: "Misty Step (3/Day)"
    desc: "The mage casts *Misty Step*, using the same spellcasting ability as Spellcasting."
reactions:
  - name: "Protective Magic (3/Day)"
    desc: "The mage casts *Counterspell* or *Shield* in response to the spell's trigger, using the same spellcasting ability as Spellcasting."
```
