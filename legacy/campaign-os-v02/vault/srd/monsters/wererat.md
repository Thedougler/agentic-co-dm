---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "A Small lawful evil wererat (CR 2) that can shape-shift into rat-humanoid hybrid or rat form and curse Humanoids with its bite."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Wererat"
found_at:
- "[[kalowe|Kalowe]]"
- "[[crown-islands|Crown Islands]]"
uid: 7fca2cf1-95bf-4fd3-a9b8-d8e8254584b2
---

# Wererat

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Wererat"
size: Small
type: monstrosity
alignment: "Lawful Evil"
ac: 13
hp: 60
hit_dice: "11d8 + 11"
speed: "30 ft., Climb 30 ft."
stats: [10, 16, 12, 11, 10, 8]
senses: "darkvision 60 ft.; Passive Perception 14"
languages: "Common (can't speak in rat form)"
cr: 2
actions:
  - name: "Multiattack"
    desc: "The wererat makes two attacks, using Scratch or Hand Crossbow in any combination. It can replace one attack with a Bite attack."
  - name: "Bite (Rat or Hybrid Form Only)"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 8 (2d4 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. *Constitution Saving Throw*: DC 11. *Failure:* The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Wererat under the DM's control and has 10 Hit Points. *Success:* The target is immune to this wererat's curse for 24 hours."
  - name: "Scratch"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 6 (1d6 + 3) Slashing damage."
  - name: "Hand Crossbow (Humanoid or Hybrid Form Only)"
    desc: "*Ranged Attack Roll:* +5, range 30/120 ft. 6 (1d6 + 3) Piercing damage."
bonus_actions:
  - name: "Shape-Shift"
    desc: "The wererat shape-shifts into a Medium rat-humanoid hybrid or a Small rat, or it returns to its true humanoid form. Its game statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed."
```
