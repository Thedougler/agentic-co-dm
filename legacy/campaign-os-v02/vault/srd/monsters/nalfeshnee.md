---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 13 large demon with demonic restoration, teleportation, and horror nimbus."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Nalfeshnee"
found_at:
- "[[sorrowbell|Sorrowbell]]"
- "[[kalowe|Kalowe]]"
uid: 0c9a3616-a1a7-4bd8-85f3-c1c477a0580b
---

# Nalfeshnee

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Nalfeshnee"
size: Large
type: fiend
alignment: "Chaotic Evil"
ac: 18
hp: 184
hit_dice: "16d10 + 96"
speed: "20 ft., Fly 30 ft."
stats: [21, 10, 22, 19, 12, 15]
saves:
  - con: 11
  - int: 9
  - wis: 6
  - cha: 7
damage_resistances: "Cold, Fire, Lightning"
damage_immunities: "Poison"
condition_immunities: "Frightened, Poisoned"
senses: "truesight 120 ft.; Passive Perception 11"
languages: "Abyssal; telepathy 120 ft."
cr: 13
traits:
  - name: "Demonic Restoration"
    desc: "If the nalfeshnee dies outside the Abyss, its body dissolves into ichor, and it gains a new body instantly, reviving with all its Hit Points somewhere in the Abyss."
  - name: "Magic Resistance"
    desc: "The nalfeshnee has Advantage on saving throws against spells and other magical effects."
actions:
  - name: "Multiattack"
    desc: "The nalfeshnee makes three Rend attacks."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +10, reach 10 ft. 16 (2d10 + 5) Slashing damage plus 11 (2d10) Force damage."
  - name: "Teleport"
    desc: "The nalfeshnee teleports up to 120 feet to an unoccupied space it can see."
bonus_actions:
  - name: "Horror Nimbus (Recharge 5-6)"
    desc: "*Wisdom Saving Throw*: DC 15, each creature in a 15-foot Emanation originating from the nalfeshnee. *Failure:* 28 (8d6) Psychic damage, and the target has the Frightened condition for 1 minute, until it takes damage, or until it ends its turn with the nalfeshnee out of line of sight. *Success:* The target is immune to this nalfeshnee's Horror Nimbus for 24 hours."
```
