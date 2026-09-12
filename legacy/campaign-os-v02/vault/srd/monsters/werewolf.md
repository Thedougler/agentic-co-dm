---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "A Chaotic Evil werewolf (CR 3) with Pack Tactics that can shape-shift into Large wolf-humanoid hybrid or Medium wolf and curse Humanoids."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Werewolf"
found_at:
- "[[midchain-west|Midchain West]]"
- "[[midchain-north|Midchain North]]"
uid: 58430a1a-232b-4360-8e16-cfc6e5133e13
---

# Werewolf

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Werewolf"
size: Small
type: monstrosity
alignment: "Chaotic Evil"
ac: 15
hp: 71
hit_dice: "11d8 + 22"
speed: "30 ft., Alternate ? ft."
stats: [16, 14, 14, 10, 11, 10]
senses: "darkvision 60 ft.; Passive Perception 14"
languages: "Common (can't speak in wolf form)"
cr: 3
traits:
  - name: "Pack Tactics"
    desc: "The werewolf has Advantage on an attack roll against a creature if at least one of the werewolf's allies is within 5 feet of the creature and the ally doesn't have the Incapacitated condition."
actions:
  - name: "Multiattack"
    desc: "The werewolf makes two attacks, using Scratch or Longbow in any combination. It can replace one attack with a Bite attack."
  - name: "Bite (Wolf or Hybrid Form Only)"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. *Constitution Saving Throw*: DC 12. *Failure:* The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Werewolf under the DM's control and has 10 Hit Points. *Success:* The target is immune to this werewolf's curse for 24 hours."
  - name: "Scratch"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 10 (2d6 + 3) Slashing damage."
  - name: "Longbow (Humanoid or Hybrid Form Only)"
    desc: "*Ranged Attack Roll:* +4, range 150/600 ft. 11 (2d8 + 2) Piercing damage."
bonus_actions:
  - name: "Shape-Shift"
    desc: "The werewolf shape-shifts into a Large wolf-humanoid hybrid or a Medium wolf, or it returns to its true humanoid form. Its game statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed."
```
