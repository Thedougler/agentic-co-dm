---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "A Neutral weretiger (CR 4) that can shape-shift into a Large tiger-humanoid hybrid or Large tiger and curse Humanoids with its bite."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Weretiger"
found_at:
- "[[verdant-teeth|Verdant Teeth]]"
- "[[midchain-north|Midchain North]]"
uid: 4c1eb161-b0ad-46f5-8ab4-0e5bb4c35503
---

# Weretiger

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Weretiger"
size: Small
type: monstrosity
alignment: "Neutral"
ac: 12
hp: 120
hit_dice: "16d8 + 48"
speed: "30 ft., Alternate ? ft."
stats: [17, 15, 16, 10, 13, 11]
senses: "darkvision 60 ft.; Passive Perception 15"
languages: "Common (can't speak in tiger form)"
cr: 4
actions:
  - name: "Multiattack"
    desc: "The weretiger makes two attacks, using Scratch or Longbow in any combination. It can replace one attack with a Bite attack."
  - name: "Bite (Tiger or Hybrid Form Only)"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. *Constitution Saving Throw*: DC 13. *Failure:* The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Weretiger under the DM's control and has 10 Hit Points. *Success:* The target is immune to this weretiger's curse for 24 hours."
  - name: "Scratch"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 10 (2d6 + 3) Slashing damage."
  - name: "Longbow (Humanoid or Hybrid Form Only)"
    desc: "*Ranged Attack Roll:* +4, range 150/600 ft. 11 (2d8 + 2) Piercing damage."
bonus_actions:
  - name: "Prowl (Tiger or Hybrid Form Only)"
    desc: "The weretiger moves up to its Speed without provoking Opportunity Attacks. At the end of this movement, the weretiger can take the Hide action."
  - name: "Shape-Shift"
    desc: "The weretiger shape-shifts into a Large tiger-humanoid hybrid or a Large tiger, or it returns to its true humanoid form. Its game statistics, other than its size, are the same in each form. Any equipment it is wearing or carrying isn't transformed."
```
