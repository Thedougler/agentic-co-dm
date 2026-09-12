---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 12 lawful evil fiend immune to fire and poison with magic rope that entangles and restores in the Nine Hells."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Erinyes"
found_at:
- "[[crown-islands|Crown Islands]]"
- "[[sunken-crown|Sunken Crown]]"
uid: 078985b6-0707-4bae-9e5b-08166390925f
---

# Erinyes

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Erinyes"
size: Medium
type: fiend
alignment: "Lawful Evil"
ac: 18
hp: 178
hit_dice: "21d8 + 84"
speed: "30 ft., Fly 60 ft."
stats: [18, 16, 18, 14, 14, 18]
saves:
  - dex: 7
  - con: 8
  - cha: 8
damage_resistances: "Cold"
damage_immunities: "Fire, Poison"
condition_immunities: "Poisoned"
senses: "truesight 120 ft.; Passive Perception 16"
languages: "Infernal; telepathy 120 ft."
cr: 12
traits:
  - name: "Diabolical Restoration"
    desc: "If the erinyes dies outside the Nine Hells, its body disappears in sulfurous smoke, and it gains a new body instantly, reviving with all its Hit Points somewhere in the Nine Hells."
  - name: "Magic Resistance"
    desc: "The erinyes has Advantage on saving throws against spells and other magical effects."
  - name: "Magic Rope"
    desc: "The erinyes has a magic rope. While bearing it, the erinyes can use the Entangling Rope action. The rope has AC 20, HP 90, and Immunity to Poison and Psychic damage. The rope turns to dust if reduced to 0 Hit Points, if it is 5+ feet away from the erinyes for 1 hour or more, or if the erinyes dies. If the rope is damaged or destroyed, the erinyes can fully restore it when finishing a Short Rest|XPHB|Short or Long Rest."
actions:
  - name: "Multiattack"
    desc: "The erinyes makes three Withering Sword attacks and can use Entangling Rope."
  - name: "Withering Sword"
    desc: "*Melee Attack Roll:* +8, reach 5 ft. 13 (2d8 + 4) Slashing damage plus 11 (2d10) Necrotic damage."
  - name: "Entangling Rope (Requires Magic Rope)"
    desc: "*Strength Saving Throw*: DC 16, one creature the erinyes can see within 120 feet. *Failure:* 14 (4d6) Force damage, and the target has the Restrained condition until the rope is destroyed, the erinyes uses a Bonus Action to release the target, or the erinyes uses Entangling Rope again."
```
