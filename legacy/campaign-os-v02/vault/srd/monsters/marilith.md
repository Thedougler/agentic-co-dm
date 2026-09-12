---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 16 Large fiend with Demonic Restoration and six-weapon Multiattack."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Marilith"
found_at:
- "[[sorrowbell|Sorrowbell]]"
- "[[kalowe|Kalowe]]"
uid: 44aaf5ad-6803-46e1-ad4c-1c1321965499
---

# Marilith

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Marilith"
size: Large
type: fiend
alignment: "Chaotic Evil"
ac: 16
hp: 220
hit_dice: "21d10 + 105"
speed: "40 ft., Climb 40 ft."
stats: [18, 20, 20, 18, 16, 20]
saves:
  - str: 9
  - con: 10
  - wis: 8
  - cha: 10
damage_resistances: "Cold, Fire, Lightning"
damage_immunities: "Poison"
condition_immunities: "Poisoned"
senses: "truesight 120 ft.; Passive Perception 18"
languages: "Abyssal; telepathy 120 ft."
cr: 16
traits:
  - name: "Demonic Restoration"
    desc: "If the marilith dies outside the Abyss, its body dissolves into ichor, and it gains a new body instantly, reviving with all its Hit Points somewhere in the Abyss."
  - name: "Magic Resistance"
    desc: "The marilith has Advantage on saving throws against spells and other magical effects."
  - name: "Reactive"
    desc: "The marilith can take one Reaction on every turn of combat."
actions:
  - name: "Multiattack"
    desc: "The marilith makes six Pact Blade attacks and uses Constrict."
  - name: "Pact Blade"
    desc: "*Melee Attack Roll:* +10, reach 5 ft. 10 (1d10 + 5) Slashing damage plus 7 (2d6) Necrotic damage."
  - name: "Constrict"
    desc: "*Strength Saving Throw*: DC 17, one Medium or smaller creature the marilith can see within 5 feet. *Failure:* 15 (2d10 + 4) Bludgeoning damage. The target has the Grappled condition (escape DC 14), and it has the Restrained condition until the grapple ends."
bonus_actions:
  - name: "Teleport (Recharge 5-6)"
    desc: "The marilith teleports up to 120 feet to an unoccupied space it can see."
```
