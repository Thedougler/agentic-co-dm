---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
found_at:
- "[[outer-reach|Outer Reach]]"
- "[[ashwall-islands|Ashwall Islands]]"
tags: [combat]
summary: "Gargantuan ancient white dragon (CR 20) with cold breath, freezing burst effects, and ice-walking abilities."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Ancient White Dragon"
uid: bb7577a5-cf18-45dd-88ae-173978dd4cff
---

# Ancient White Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Ancient White Dragon"
size: Gargantuan
type: dragon
alignment: "Chaotic Evil"
ac: 20
hp: 333
hit_dice: "18d20 + 144"
speed: "40 ft., Burrow 40 ft., Fly 80 ft., Swim 40 ft."
stats: [26, 10, 26, 10, 13, 18]
saves:
  - dex: 6
  - wis: 7
damage_immunities: "Cold"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 23"
languages: "Common, Draconic"
cr: 20
traits:
  - name: "Ice Walk"
    desc: "The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, Difficult Terrain composed of ice or snow doesn't cost it extra movement."
  - name: "Legendary Resistance (4/Day, or 5/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +14, reach 15 ft. 17 (2d8 + 8) Slashing damage plus 7 (2d6) Cold damage."
  - name: "Cold Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 22, each creature in a 90-foot Cone. *Failure:* 63 (14d8) Cold damage. *Success:* Half damage."
legendary_actions:
  - name: "Freezing Burst"
    desc: "*Constitution Saving Throw*: DC 20, each creature in a 30-foot-radius Sphere [Area of Effect]|XPHB|Sphere centered on a point the dragon can see within 120 feet. *Failure:* 14 (4d6) Cold damage, and the target's Speed is 0 until the end of the target's next turn. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
  - name: "Frightful Presence"
    desc: "The dragon casts *Fear*, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 18). The dragon can't take this action again until the start of its next turn."
```
