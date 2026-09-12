---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "CR 2 undead with stench aura and paralytic claw attack."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Ghast"
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[the-drowned-maw|The Drowned Maw]]"
uid: 16e51320-ef89-46dc-97d3-c032bee2dcf3
---

# Ghast

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ghast"
size: Medium
type: undead
alignment: "Chaotic Evil"
ac: 13
hp: 36
hit_dice: "8d8"
speed: "30 ft."
stats: [16, 17, 10, 11, 10, 8]
saves:
  - wis: 2
damage_resistances: "Necrotic"
damage_immunities: "Poison"
condition_immunities: "Charmed, Exhaustion, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Common"
cr: 2
traits:
  - name: "Stench"
    desc: "*Constitution Saving Throw*: DC 10, any creature that starts its turn in a 5-foot Emanation originating from the ghast. *Failure:* The target has the Poisoned condition until the start of its next turn. *Success:* The target is immune to this ghast's Stench for 24 hours."
actions:
  - name: "Bite"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 7 (1d8 + 3) Piercing damage plus 9 (2d8) Necrotic damage."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 10 (2d6 + 3) Slashing damage. If the target is a non-Undead creature, it is subjected to the following effect. *Constitution Saving Throw*: DC 10. *Failure:* The target has the Paralyzed condition until the end of its next turn."
```
