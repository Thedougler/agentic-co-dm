---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, faith]
summary: "CR 4 Large fiend with Corrupting Touch curse, spellcasting, and magical leap."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Lamia"
found_at:
- "[[kalowe|Kalowe]]"
- "[[la-cenere|La Cenere]]"
uid: a3f2eb8b-5b4b-4226-8fd3-9bd3d497374d
---

# Lamia

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Lamia"
size: Large
type: fiend
alignment: "Chaotic Evil"
ac: 13
hp: 97
hit_dice: "13d10 + 26"
speed: "40 ft."
stats: [16, 13, 15, 14, 15, 16]
senses: "darkvision 60 ft.; Passive Perception 12"
languages: "Abyssal, Common"
cr: 4
actions:
  - name: "Multiattack"
    desc: "The lamia makes two Claw attacks. It can replace one attack with a use of Corrupting Touch."
  - name: "Claw"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 7 (1d8 + 3) Slashing damage plus 7 (2d6) Psychic damage."
  - name: "Corrupting Touch"
    desc: "*Wisdom Saving Throw*: DC 13, one creature the lamia can see within 5 feet. *Failure:* 13 (3d8) Psychic damage, and the target is cursed for 1 hour. Until the curse ends, the target has the Charmed and Poisoned conditions."
  - name: "Spellcasting"
    desc: "The lamia casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 13): - **At Will:** *Disguise Self*, *Minor Illusion* - **1e/Day Each:** *Geas*, *Major Image*, *Scrying*"
bonus_actions:
  - name: "Leap"
    desc: "The lamia jumps up to 30 feet by spending 10 feet of movement."
```
