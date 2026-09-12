---
type: monster
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 1/4 small fiend immune to poison with damaging claws and a poisoning fetid cloud aura."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Dretch"
found_at:
- "[[sorrowbell|Sorrowbell]]"
- "[[kalowe|Kalowe]]"
uid: 9d904f75-2cef-4ff3-853c-87c193d102a0
---

# Dretch

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Dretch"
size: Small
type: fiend
alignment: "Chaotic Evil"
ac: 11
hp: 18
hit_dice: "4d6 + 4"
speed: "20 ft."
stats: [12, 11, 12, 5, 8, 3]
damage_resistances: "Cold, Fire, Lightning"
damage_immunities: "Poison"
condition_immunities: "Poisoned"
senses: "darkvision 60 ft.; Passive Perception 9"
languages: "Abyssal; telepathy 60 ft. (works only with creatures that understand Abyssal)"
cr: "1/4"
actions:
  - name: "Rend"
    desc: "*Melee Attack Roll:* +3, reach 5 ft. 4 (1d6 + 1) Slashing damage."
  - name: "Fetid Cloud (1/Day)"
    desc: "*Constitution Saving Throw*: DC 11, each creature in a 10-foot Emanation originating from the dretch. *Failure:* The target has the Poisoned condition until the end of its next turn. While Poisoned, the creature can take either an action or a Bonus Action on its turn, not both, and it can't take Reactions."
```
