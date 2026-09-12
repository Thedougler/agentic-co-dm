---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "CR 11 elemental servant capable of flight, weather control, and magical wishes."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Djinni"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
uid: e91d00d7-0a6d-4824-845d-04e24873464d
---

# Djinni

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Djinni"
size: Large
type: elemental
alignment: "Chaotic Good"
ac: 17
hp: 218
hit_dice: "19d10 + 114"
speed: "30 ft., Fly 90 ft. (hover)"
stats: [21, 15, 22, 15, 16, 20]
saves:
  - dex: 6
  - wis: 7
damage_immunities: "Lightning, Thunder"
senses: "darkvision 120 ft.; Passive Perception 13"
languages: "Primordial (Auran)"
cr: 11
traits:
  - name: "Elemental Restoration"
    desc: "If the djinni dies outside the Elemental Plane of Air, its body dissolves into mist, and it gains a new body in 1d4 days, reviving with all its Hit Points somewhere on the Plane of Air."
  - name: "Magic Resistance"
    desc: "The djinni has Advantage on saving throws against spells and other magical effects."
  - name: "Wishes"
    desc: "The djinni has a 30 percent chance of knowing the *Wish* spell. If the djinni knows it, the djinni can cast it only on behalf of a non-genie creature who communicates a wish in a way the djinni can understand. If the djinni casts the spell for the creature, the djinni suffers none of the spell's stress. Once the djinni has cast it three times, the djinni can't do so again for 365 days."
actions:
  - name: "Multiattack"
    desc: "The djinni makes three attacks, using Storm Blade or Storm Bolt in any combination."
  - name: "Storm Blade"
    desc: "*Melee Attack Roll:* +9, reach 5 feet. 12 (2d6 + 5) Slashing damage plus 7 (2d6) Lightning damage."
  - name: "Storm Bolt"
    desc: "*Ranged Attack Roll:* +9, range 120 feet. 13 (3d8) Thunder damage. If the target is a Large or smaller creature, it has the Prone condition."
  - name: "Create Whirlwind"
    desc: "The djinni conjures a whirlwind at a point it can see within 120 feet. The whirlwind fills a 20-foot-radius, 60-foot-high Cylinder [Area of Effect]|XPHB|Cylinder centered on that point. The whirlwind lasts until the djinni's Concentration on it ends. The djinni can move the whirlwind up to 20 feet at the start of each of its turns. Whenever the whirlwind enters a creature's space or a creature enters the whirlwind, that creature is subjected to the following effect. *Strength Saving Throw*: DC 17 (a creature makes this save only once per turn, and the djinni is unaffected). *Failure:* While in the whirlwind, the target has the Restrained condition and moves with the whirlwind. At the start of each of its turns, the Restrained target takes 21 (6d6) Thunder damage. At the end of each of its turns, the target repeats the save, ending the effect on itself on a success."
  - name: "Spellcasting"
    desc: "The djinni casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 17): - **At Will:** *Detect Evil and Good*, *Detect Magic* - **2e/Day Each:** *Create Food and Water*, *Tongues*, *Wind Walk* - **1e/Day Each:** *Creation*, *Gaseous Form*, *Invisibility*, *Major Image*, *Plane Shift*"
```
