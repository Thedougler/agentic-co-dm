---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "CR 5 small undead with spider climb, claw grapple, and Constitution save-based necrotic bite."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Vampire Spawn"
found_at:
- "[[doldrums|Doldrums]]"
- "[[sunken-crown|Sunken Crown]]"
uid: 64433e46-c0a8-486b-b09a-db7c67d72dcb
---

# Vampire Spawn

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Vampire Spawn"
size: Small
type: undead
alignment: "Neutral Evil"
ac: 16
hp: 90
hit_dice: "12d8 + 36"
speed: "30 ft."
stats: [16, 16, 16, 11, 10, 12]
saves:
  - dex: 6
  - wis: 3
damage_resistances: "Necrotic"
senses: "darkvision 60 ft.; Passive Perception 13"
languages: "Common plus one other language"
cr: 5
traits:
  - name: "Spider Climb"
    desc: "The vampire can climb difficult surfaces, including along ceilings, without needing to make an ability check."
  - name: "Vampire Weakness"
    desc: "The vampire has these weaknesses: - **Forbiddance**: The vampire can't enter a residence without an invitation from an occupant. - **Running Water**: The vampire takes 20 Acid damage if it ends its turn in running water. - **Stake to the Heart**: The vampire is destroyed if a weapon that deals Piercing damage is driven into the vampire's heart while the vampire has the Incapacitated condition. - **Sunlight**: The vampire takes 20 Radiant damage if it starts its turn in sunlight. While in sunlight, it has Disadvantage on attack rolls and ability checks."
actions:
  - name: "Multiattack"
    desc: "The vampire makes two Claw attacks and uses Bite."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 8 (2d4 + 3) Slashing damage. If the target is a Medium or smaller creature, it has the Grappled condition (escape DC 13) from one of two claws."
  - name: "Bite"
    desc: "*Constitution Saving Throw*: DC 14, one creature within 5 feet that is willing or that has the Grappled, Incapacitated, or Restrained condition. *Failure:* 5 (1d4 + 3) Piercing damage plus 10 (3d6) Necrotic damage. The target's Hit Point maximum decreases by an amount equal to the Necrotic damage taken, and the vampire regains Hit Points equal to that amount."
bonus_actions:
  - name: "Deathless Agility"
    desc: "The vampire takes the Dash or Disengage action."
```
