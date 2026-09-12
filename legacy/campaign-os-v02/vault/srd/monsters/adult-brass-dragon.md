---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "Huge dragon (CR 13) with fire immunity, breath weapon, spellcasting, and legendary resistance."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Adult Brass Dragon"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
uid: 262e5351-3e82-4b69-8f2b-5ee709cf8358
---

# Adult Brass Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult Brass Dragon"
size: Huge
type: dragon
alignment: "Chaotic Good"
ac: 18
hp: 172
hit_dice: "15d12 + 75"
speed: "40 ft., Burrow 30 ft., Fly 80 ft."
stats: [23, 10, 21, 14, 13, 17]
saves:
  - dex: 5
  - wis: 6
damage_immunities: "Fire"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 21"
languages: "Common, Draconic"
cr: 13
traits:
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of (A) Sleep Breath or (B) Spellcasting to cast *Scorching Ray*."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +11, reach 10 ft. 17 (2d10 + 6) Slashing damage plus 4 (1d8) Fire damage."
  - name: "Fire Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 18, each creature in a 60-foot-long, 5-foot-wide Line. *Failure:* 45 (10d8) Fire damage. *Success:* Half damage."
  - name: "Sleep Breath"
    desc: "*Constitution Saving Throw*: DC 18, each creature in a 60-foot Cone. *Failure:* The target has the Incapacitated condition until the end of its next turn, at which point it repeats the save. *Second Failure* The target has the Unconscious condition for 10 minutes. This effect ends for the target if it takes damage or a creature within 5 feet of it takes an action to wake it."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 16): - **At Will:** *Detect Magic*, *Minor Illusion*, *Scorching Ray*, *Shapechange*, *Speak with Animals* - **1e/Day Each:** *Detect Thoughts*, *Control Weather*"
legendary_actions:
  - name: "Blazing Light"
    desc: "The dragon uses Spellcasting to cast *Scorching Ray*."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
  - name: "Scorching Sands"
    desc: "*Dexterity Saving Throw*: DC 16, one creature the dragon can see within 120 feet. *Failure:* 27 (6d8) Fire damage, and the target's Speed is halved until the end of its next turn. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
```
