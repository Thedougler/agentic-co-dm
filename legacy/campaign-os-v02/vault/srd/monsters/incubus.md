---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "Medium fiend caster with psychic touch, dream spells, and shape-shift to Succubus (CR 4)."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Incubus"
found_at:
- "[[sorrowbell|Sorrowbell]]"
- "[[kalowe|Kalowe]]"
uid: b07df696-fb1e-4a82-a22e-3dcccb72881d
---

# Incubus

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Incubus"
size: Medium
type: fiend
alignment: "Neutral Evil"
ac: 15
hp: 66
hit_dice: "12d8 + 12"
speed: "30 ft., Fly 60 ft."
stats: [8, 17, 13, 15, 12, 20]
damage_resistances: "Cold, Fire, Poison, Psychic"
senses: "darkvision 60 ft.; Passive Perception 15"
languages: "Abyssal, Common, Infernal; telepathy 60 ft."
cr: 4
traits:
  - name: "Succubus Form"
    desc: "When the incubus finishes a Long Rest, it can shape-shift into a Succubus, using that stat block instead of this one. Any equipment it's wearing or carrying isn't transformed."
actions:
  - name: "Multiattack"
    desc: "The incubus makes two Restless Touch attacks."
  - name: "Restless Touch"
    desc: "*Melee Attack Roll:* +7, reach 5 ft. 15 (3d6 + 5) Psychic damage, and the target is cursed for 24 hours or until the incubus dies. Until the curse ends, the target gains no benefit from finishing Short Rests."
  - name: "Spellcasting"
    desc: "The incubus casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 15): - **At Will:** *Disguise Self*, *Etherealness* - **1e/Day Each:** *Dream*, *Hypnotic Pattern*"
bonus_actions:
  - name: "Nightmare (Recharge 6)"
    desc: "*Wisdom Saving Throw*: DC 15, one creature the incubus can see within 60 feet. *Failure:* If the target has 20 Hit Points or fewer, it has the Unconscious condition for 1 hour, until it takes damage, or until a creature within 5 feet of it takes an action to wake it. Otherwise, the target takes 18 (4d8) Psychic damage."
```
