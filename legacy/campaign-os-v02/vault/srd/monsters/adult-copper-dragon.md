---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "Huge dragon (CR 14) with acid breath, a slowing cone attack, and psychic Giggling Magic spellcasting."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Adult Copper Dragon"
found_at:
- "[[redwind-isles|Redwind Isles]]"
- "[[outer-reach|Outer Reach]]"
uid: 4a06e1b2-69e5-4c11-b3e7-7c49f34a5b5b
---

# Adult Copper Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult Copper Dragon"
size: Huge
type: dragon
alignment: "Chaotic Good"
ac: 18
hp: 184
hit_dice: "16d12 + 80"
speed: "40 ft., Climb 40 ft., Fly 80 ft."
stats: [23, 12, 21, 18, 15, 18]
saves:
  - dex: 6
  - wis: 7
damage_immunities: "Acid"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 22"
languages: "Common, Draconic"
cr: 14
traits:
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks. It can replace one attack with a use of (A) Slowing Breath or (B) Spellcasting to cast *Mind Spike* (level 4 version)."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +11, reach 10 ft. 17 (2d10 + 6) Slashing damage plus 4 (1d8) Acid damage."
  - name: "Acid Breath (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 18, each creature in an 60-foot-long, 5-foot-wide Line. *Failure:* 54 (12d8) Acid damage. *Success:* Half damage."
  - name: "Slowing Breath"
    desc: "*Constitution Saving Throw*: DC 18, each creature in a 60-foot Cone. *Failure:* The target can't take Reactions; its Speed is halved; and it can take either an action or a Bonus Action on its turn, not both. This effect lasts until the end of its next turn."
  - name: "Spellcasting"
    desc: "The dragon casts one of the following spells, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 17): - **At Will:** *Detect Magic*, *Mind Spike*, *Minor Illusion*, *Shapechange* - **1e/Day Each:** *Greater Restoration*, *Major Image*"
legendary_actions:
  - name: "Giggling Magic"
    desc: "*Charisma Saving Throw*: DC 17, one creature the dragon can see within 90 feet. *Failure:* 24 (7d6) Psychic damage. Until the end of its next turn, the target rolls 1d6 whenever it makes an ability check or attack roll and subtracts the number rolled from the D20 Test. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Mind Jolt"
    desc: "The dragon uses Spellcasting to cast *Mind Spike* (level 4 version). The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
```
