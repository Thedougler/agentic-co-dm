---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, intrigue]
summary: "CR 6 humanoid duelist who fights with Rapier or Pistol and can Charm a nearby foe."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[midchain-west|Midchain West]]"
- "[[crown-islands|Crown Islands]]"
statblock: inline
name: "Pirate Captain"
uid: e8495ff1-1b20-4d1a-b6b7-8e5ca3e76be0
---

# Pirate Captain

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Pirate Captain"
size: Small
type: humanoid
alignment: "Neutral"
ac: 17
hp: 84
hit_dice: "13d8 + 26"
speed: "30 ft."
stats: [10, 18, 14, 10, 14, 17]
saves:
  - str: 3
  - dex: 7
  - wis: 5
  - cha: 6
senses: "Passive Perception 15"
languages: "Common plus one other language"
cr: 6
actions:
  - name: "Multiattack"
    desc: "The pirate makes three attacks, using Rapier or Pistol in any combination."
  - name: "Rapier"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 13 (2d8 + 4) Piercing damage, and the pirate has Advantage on the next attack roll it makes before the end of this turn."
  - name: "Pistol"
    desc: "*Ranged Attack Roll:* +7, range 30/90 ft. 15 (2d10 + 4) Piercing damage."
bonus_actions:
  - name: "Captain's Charm"
    desc: "*Wisdom Saving Throw*: DC 14, one creature the pirate can see within 30 feet. *Failure:* The target has the Charmed condition until the start of the pirate's next turn."
```
