---
type: monster
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 21 Gargantuan Chaotic Good dragon with Acid Breath, Slowing Breath, and spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
statblock: inline
name: "Ancient Copper Dragon"
uid: 5611d558-0a56-46f5-9254-c40a44d8352c
---

# Ancient Copper Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ancient Copper Dragon"
size: Gargantuan
type: dragon
alignment: "Chaotic Good"
ac: 21
hp: 367
hit_dice: "21d20 + 147"
speed: "40 ft., Climb 40 ft., Fly 80 ft."
stats: [27, 12, 25, 20, 17, 22]
saves:
  - dex: 8
  - wis: 10
damage_immunities: "Acid"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 27"
languages: "Common, Draconic"
cr: 21
traits:
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of (A) Slowing Breath or (B) Spellcasting to cast *Mind Spike* (level 5 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +15, reach 15 ft. 19 (2d10 + 8) Slashing damage plus 9 (2d8) Acid damage."
  - name: "Acid Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 22, each creature in an 90-foot-long, 10-foot-wide Line. *Failure:* 63 (14d8) Acid damage. *Success:* Half damage."
  - name: "Slowing Breath"
    desc: "*Constitution Saving Throw*: DC 22, each creature in a 90-foot Cone. *Failure:* The target can't take Reactions; its Speed is halved; and it can take either an action or a Bonus Action on its turn, not both. This effect lasts until the end of its next turn."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 21): - **At Will:** *Detect Magic*, *Mind Spike*, *Minor Illusion*, *Shapechange* - **1e/Day Each:** *Greater Restoration*, *Major Image*, *Project Image*"
legendary_actions:
  - name: "Giggling Magic"
    desc: "*Charisma Saving Throw*: DC 21, one creature the dragon can see within 120 feet. *Failure:* 31 (9d6) Psychic damage. Until the end of its next turn, the target rolls 1d8 whenever it makes an ability check or attack roll and subtracts the number rolled from the D20 Test. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Mind Jolt"
    desc: "The dragon uses Spellcasting to cast *Mind Spike* (level 5 version). The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
