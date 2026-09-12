---
type: monster
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, nature]
summary: "CR 5 large elemental that burrows through earth, doubles damage to objects, and attacks with slams and throws."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Earth Elemental"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
uid: 3450c6e0-5347-4b73-b250-253fe597a77a
---

# Earth Elemental

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Earth Elemental"
size: Large
type: elemental
alignment: "Neutral"
ac: 17
hp: 147
hit_dice: "14d10 + 70"
speed: "30 ft., Burrow 30 ft."
stats: [20, 8, 20, 5, 10, 5]
damage_vulnerabilities: "Thunder"
damage_immunities: "Poison"
condition_immunities: "Exhaustion, Paralyzed, Petrified, Poisoned, Unconscious"
senses: "darkvision 60 ft., tremorsense 60 ft.; Passive Perception 10"
languages: "Primordial (Terran)"
cr: 5
traits:
  - name: "Earth Glide"
    desc: "The elemental can burrow through nonmagical, unworked earth and stone. While doing so, the elemental doesn't disturb the material it moves through."
  - name: "Siege Monster"
    desc: "The elemental deals double damage to objects and structures."
actions:
  - name: "Multiattack"
    desc: "The elemental makes two attacks, using Slam or Rock Launch in any combination."
  - name: "Slam"
    desc: "*Melee Attack Roll:* +8, reach 10 ft. 14 (2d8 + 5) Bludgeoning damage."
  - name: "Rock Launch"
    desc: "*Ranged Attack Roll:* +8, range 60 ft. 8 (1d6 + 5) Bludgeoning damage. If the target is a Large or smaller creature, it has the Prone condition."
```
