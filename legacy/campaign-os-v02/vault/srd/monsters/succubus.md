---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 4 medium fiend with charm and draining kiss; shape-shifts to humanoid form."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Succubus"
found_at:
- "[[midchain-west|Midchain West]]"
- "[[crown-islands|Crown Islands]]"
uid: 9891db36-16d8-4098-a807-41e557e72adb
---

# Succubus

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Succubus"
size: Medium
type: fiend
alignment: "Neutral Evil"
ac: 15
hp: 71
hit_dice: "13d8 + 13"
speed: "30 ft., Fly 60 ft."
stats: [8, 17, 13, 15, 12, 20]
damage_resistances: "Cold, Fire, Poison, Psychic"
senses: "darkvision 60 ft.; Passive Perception 15"
languages: "Abyssal, Common, Infernal; telepathy 60 ft."
cr: 4
traits:
  - name: "Incubus Form"
    desc: "When the succubus finishes a Long Rest, it can shape-shift into an Incubus, using that stat block instead of this one."
actions:
  - name: "Multiattack"
    desc: "The succubus makes one Fiendish Touch attack and uses Charm or Draining Kiss."
  - name: "Fiendish Touch"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 16 (2d10 + 5) Psychic damage."
  - name: "Charm"
    desc: "The succubus casts *Dominate Person* (level 8 version), requiring no spell components and using Charisma as the spellcasting ability (spell save DC 15)."
  - name: "Draining Kiss"
    desc: "*Constitution Saving Throw*: DC 15, one creature Charmed by the succubus within 5 feet. *Failure:* 13 (3d8) Psychic damage. *Success:* Half damage. *Failure or Success*: The target's Hit Point maximum decreases by an amount equal to the damage taken."
bonus_actions:
  - name: "Shape-Shift"
    desc: "The succubus shape-shifts to resemble a Medium or Small Humanoid or back into its true form. Its game statistics are the same in each form, except its Fly Speed is available only in its true form. Any equipment it's wearing or carrying isn't transformed."
```
