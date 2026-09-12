---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, intrigue]
summary: "High-level spellcaster with magic resistance and arcane burst attacks."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[calders-tooth|Calder's Tooth]]"
statblock: inline
name: "Archmage"
uid: 1118eebb-7f65-4eaf-ab3f-5519fc93dd6f
---

# Archmage

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Archmage"
size: Small
type: humanoid
alignment: "Neutral"
ac: 17
hp: 170
hit_dice: "31d8 + 31"
speed: "30 ft."
stats: [10, 14, 12, 20, 15, 16]
saves:
  - int: 9
  - wis: 6
damage_immunities: "Psychic"
condition_immunities: "Charmed ((with Mind Blank))"
senses: "Passive Perception 16"
languages: "Common plus five other languages"
cr: 12
traits:
  - name: "Magic Resistance"
    desc: "The archmage has Advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "The archmage makes four Arcane Burst attacks."
  - name: "Arcane Burst"
    desc: "*Melee or Ranged Attack Roll:* +9, reach 5 ft. or range 150 ft. 27 (4d10 + 5) Force damage."
  - name: "Spellcasting"
    desc: "The archmage casts one of the following spells, using Intelligence as the spellcasting ability (spell save DC 17): - **At Will:** *Detect Magic*, *Detect Thoughts*, *Disguise Self*, *Invisibility*, *Light*, *Mage Armor*, *Mage Hand*, *Prestidigitation* - **2e/Day Each:** *Fly*, *Lightning Bolt* - **1e/Day Each:** *Cone of Cold*, *Mind Blank*, *Scrying*, *Teleport*"
bonus_actions:
  - name: "Misty Step (3/Day)"
    desc: "The mage casts *Misty Step*, using the same spellcasting ability as Spellcasting."
reactions:
  - name: "Protective Magic (3/Day)"
    desc: "The archmage casts *Counterspell* or *Shield* in response to the spell's trigger, using the same spellcasting ability as Spellcasting."
```
