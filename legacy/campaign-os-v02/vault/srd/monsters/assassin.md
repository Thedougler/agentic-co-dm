---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, intrigue]
summary: "Agile humanoid with poison attacks, evasion, and cunning tactics."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[calders-tooth|Calder's Tooth]]"
- "[[midchain-west|Midchain West]]"
statblock: inline
name: "Assassin"
uid: 69bfcac0-0920-4e2a-9b83-631d28852cdc
---

# Assassin

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Assassin"
size: Small
type: humanoid
alignment: "Neutral"
ac: 16
hp: 97
hit_dice: "15d8 + 30"
speed: "30 ft."
stats: [11, 18, 14, 16, 11, 10]
saves:
  - dex: 7
  - int: 6
damage_resistances: "Poison"
senses: "Passive Perception 16"
languages: "Common, Thieves' cant"
cr: 8
traits:
  - name: "Evasion"
    desc: "If the assassin is subjected to an effect that allows it to make a Dexterity saving throw to take only half damage, the assassin instead takes no damage if it succeeds on the save and only half damage if it fails. It can't use this trait if it has the Incapacitated condition."
actions:
  - name: "Multiattack"
    desc: "The assassin makes three attacks, using Shortsword or Light Crossbow in any combination."
  - name: "Shortsword"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 7 (1d6 + 4) Piercing damage plus 17 (5d6) Poison damage, and the target has the Poisoned condition until the start of the assassin's next turn."
  - name: "Light Crossbow"
    desc: "*Ranged Attack Roll:* +7, range 80/320 ft. 8 (1d8 + 4) Piercing damage plus 21 (6d6) Poison damage."
bonus_actions:
  - name: "Cunning Action"
    desc: "The assassin takes the Dash, Disengage, or Hide action."
```
