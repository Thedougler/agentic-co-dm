---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "A CR 1 incorporeal undead that drains maximum hit points and fears sunlight and radiant damage."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Specter"
found_at:
- "[[the-drowned-maw|The Drowned Maw]]"
- "[[midchain-east|Midchain East]]"
uid: d3ef0660-bd0a-4a6b-a7ed-bcee7ecdb66f
---

# Specter

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Specter"
size: Medium
type: undead
alignment: "Chaotic Evil"
ac: 12
hp: 22
hit_dice: "5d8"
speed: "30 ft., Fly 50 ft. (hover)"
stats: [1, 14, 11, 10, 10, 11]
damage_resistances: "Acid, Bludgeoning, Cold, Fire, Lightning, Piercing, Slashing, Thunder"
damage_immunities: "Necrotic, Poison"
condition_immunities: "Charmed, Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Understands Common plus one other language but can't speak"
cr: 1
traits:
  - name: "Incorporeal Movement"
    desc: "The specter can move through other creatures and objects as if they were Difficult Terrain. It takes 5 (1d10) Force damage if it ends its turn inside an object."
  - name: "Sunlight Sensitivity"
    desc: "While in sunlight, the specter has Disadvantage on ability checks and attack rolls."
actions:
  - name: "Life Drain"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. 7 (2d6) Necrotic damage. If the target is a creature, its Hit Point maximum decreases by an amount equal to the damage taken."
```
