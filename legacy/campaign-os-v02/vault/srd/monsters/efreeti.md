---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "CR 11 fire elemental with regeneration, high AC, fire immunity, and potential Wish spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Efreeti"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
uid: 1cf5178d-076a-44b7-b6a4-515f17cac7e8
---

# Efreeti

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Efreeti"
size: Large
type: elemental
alignment: "Neutral"
ac: 17
hp: 212
hit_dice: "17d10 + 119"
speed: "40 ft., Fly 60 ft. (hover)"
stats: [22, 12, 24, 16, 15, 19]
saves:
  - wis: 6
  - cha: 8
damage_immunities: "Fire"
senses: "darkvision 120 ft.; Passive Perception 12"
languages: "Primordial (Ignan)"
cr: 11
traits:
  - name: "Elemental Restoration"
    desc: "If the efreeti dies outside the Elemental Plane of Fire, its body dissolves into ash, and it gains a new body in 1d4 days, reviving with all its Hit Points somewhere on the Plane of Fire."
  - name: "Magic Resistance"
    desc: "The efreeti has Advantage on saving throws against spells and other magical effects."
  - name: "Wishes"
    desc: "The efreeti has a 30 percent chance of knowing the *Wish* spell. If the efreeti knows it, the efreeti can cast it only on behalf of a non-genie creature who communicates a wish in a way the efreeti can understand. If the efreeti casts the spell for the creature, the efreeti suffers none of the spell's stress. Once the efreeti has cast it three times, the efreeti can't do so again for 365 days."
actions:
  - name: "Multiattack"
    desc: "The efreeti makes three attacks, using Heated Blade or Hurl Flame in any combination."
  - name: "Heated Blade"
    desc: "*Melee Attack Roll:* +10, reach 5 ft. 13 (2d6 + 6) Slashing damage plus 13 (2d12) Fire damage."
  - name: "Hurl Flame"
    desc: "*Ranged Attack Roll:* +8, range 120 ft. 24 (7d6) Fire damage."
  - name: "Spellcasting"
    desc: "The efreeti casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 16): - **At Will:** *Detect Magic*, *Elementalism* - **1e/Day Each:** *Gaseous Form*, *Invisibility*, *Major Image*, *Plane Shift*, *Tongues*, *Wall of Fire*"
```
