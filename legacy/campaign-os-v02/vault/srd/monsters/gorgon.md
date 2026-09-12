---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "CR 5 construct with petrifying breath and gore attack."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Gorgon"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[shelfworks|Shelfworks]]"
uid: ca020873-3d64-4037-9efc-8d2e403fcd33
---

# Gorgon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Gorgon"
size: Large
type: construct
alignment: "Unaligned"
ac: 19
hp: 114
hit_dice: "12d10 + 48"
speed: "40 ft."
stats: [20, 11, 18, 2, 12, 7]
damage_immunities: "Exhaustion, Petrified"
senses: "darkvision 60 ft.; Passive Perception 17"
cr: 5
actions:
  - name: "Gore"
    desc: "*Melee Attack Roll:* +8, reach 5 ft. 18 (2d12 + 5) Piercing damage. If the target is a Large or smaller creature and the gorgon moved 20+ feet straight toward it immediately before the hit, the target has the Prone condition."
  - name: "Petrifying Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 15, each creature in a 30-foot Cone. *First Failure* The target has the Restrained condition and repeats the save at the end of its next turn if it is still Restrained, ending the effect on itself on a success. *Second Failure* The target has the Petrified condition instead of the Restrained condition."
bonus_actions:
  - name: "Trample"
    desc: "*Dexterity Saving Throw*: DC 16, one creature within 5 feet that has the Prone condition. *Failure:* 16 (2d10 + 5) Bludgeoning damage. *Success:* Half damage."
```
