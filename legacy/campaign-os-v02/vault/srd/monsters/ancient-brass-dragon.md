---
type: monster
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 20 Gargantuan Chaotic Good dragon with Fire Breath, Sleep Breath, and spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[redwind-isles|Redwind Isles]]"
- "[[ashwall-islands|Ashwall Islands]]"
statblock: inline
name: "Ancient Brass Dragon"
uid: 779b9719-aba6-4ba1-aa74-6ba751e5d2aa
---

# Ancient Brass Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ancient Brass Dragon"
size: Gargantuan
type: dragon
alignment: "Chaotic Good"
ac: 20
hp: 332
hit_dice: "19d20 + 133"
speed: "40 ft., Burrow 40 ft., Fly 80 ft."
stats: [27, 10, 25, 16, 15, 22]
saves:
  - dex: 6
  - wis: 8
damage_immunities: "Fire"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 24"
languages: "Common, Draconic"
cr: 20
traits:
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of (A) Sleep Breath or (B) Spellcasting to cast *Scorching Ray* (level 3 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +14, reach 15 ft. 19 (2d10 + 8) Slashing damage plus 7 (2d6) Fire damage."
  - name: "Fire Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 21, each creature in a 90-foot-long, 5-foot-wide Line. *Failure:* 58 (13d8) Fire damage. *Success:* Half damage."
  - name: "Sleep Breath"
    desc: "*Constitution Saving Throw*: DC 21, each creature in a 90-foot Cone. *Failure:* The target has the Incapacitated condition until the end of its next turn, at which point it repeats the save. *Second Failure* The target has the Unconscious condition for 10 minutes. This effect ends for the target if it takes damage or a creature within 5 feet of it takes an action to wake it."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 20): - **At Will:** *Detect Magic*, *Minor Illusion*, *Scorching Ray*, *Shapechange*, *Speak with Animals* - **1e/Day Each:** *Control Weather*, *Detect Thoughts*"
legendary_actions:
  - name: "Blazing Light"
    desc: "The dragon uses Spellcasting to cast *Scorching Ray* (level 3 version)."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
  - name: "Scorching Sands"
    desc: "*Dexterity Saving Throw*: DC 20, one creature the dragon can see within 120 feet. *Failure:* 36 (8d8) Fire damage, and the target's Speed is halved until the end of its next turn. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
```
