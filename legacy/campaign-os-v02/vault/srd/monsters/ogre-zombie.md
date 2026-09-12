---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "CR 2 undead ogre with Undead Fortitude, resistant to death and powerful slam."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[doldrums|Doldrums]]"
- "[[the-drowned-maw|The Drowned Maw]]"
statblock: inline
name: "Ogre Zombie"
uid: 4baf4695-2743-4dc0-8e27-dd8158ee3657
---

# Ogre Zombie

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ogre Zombie"
size: Large
type: undead
alignment: "Neutral Evil"
ac: 8
hp: 85
hit_dice: "9d10 + 36"
speed: "30 ft."
stats: [19, 6, 18, 3, 6, 5]
saves:
  - wis: 0
damage_immunities: "Poison"
condition_immunities: "Exhaustion, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 8"
languages: "Understands Common and Giant but can't speak"
cr: 2
traits:
  - name: "Undead Fortitude"
    desc: "If damage reduces the zombie to 0 Hit Points, it makes a Constitution saving throw (DC 5 plus the damage taken) unless the damage is Radiant or from a Critical Hit. On a successful save, the zombie drops to 1 Hit Point instead."
actions:
  - name: "Slam"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 13 (2d8 + 4) Bludgeoning damage."
```
