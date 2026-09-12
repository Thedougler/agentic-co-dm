---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror, stealth]
summary: "A CR 1/2 undead wraith that drains Strength and thrives in darkness, but weakens in sunlight and radiant damage."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[doldrums|Doldrums]]"
- "[[the-drowned-maw|The Drowned Maw]]"
statblock: inline
name: "Shadow"
uid: 95da06d5-9f5f-4dfd-93c2-8141dd5f7cfb
---

# Shadow

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Shadow"
size: Medium
type: undead
alignment: "Chaotic Evil"
ac: 12
hp: 27
hit_dice: "5d8 + 5"
speed: "40 ft."
stats: [6, 14, 13, 6, 10, 8]
damage_resistances: "Acid, Cold, Fire, Lightning, Thunder"
damage_vulnerabilities: "Radiant"
damage_immunities: "Necrotic, Poison"
condition_immunities: "Exhaustion, Frightened, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious"
senses: "darkvision 60 ft.; Passive Perception 10"
cr: "1/2"
traits:
  - name: "Amorphous"
    desc: "The shadow can move through a space as narrow as 1 inch without expending extra movement to do so."
  - name: "Sunlight Weakness"
    desc: "While in sunlight, the shadow has Disadvantage on D20 Test."
actions:
  - name: "Draining Swipe"
    desc: "*Melee Attack Roll:* +4, reach 5 ft. 5 (1d6 + 2) Necrotic damage, and the target's Strength score decreases by 1d4. The target dies if this reduces that score to 0. If a Humanoid is slain by this attack, a Shadow rises from the corpse 1d4 hours later."
bonus_actions:
  - name: "Shadow Stealth"
    desc: "While in Dim Light or darkness, the shadow takes the Hide action."
```
