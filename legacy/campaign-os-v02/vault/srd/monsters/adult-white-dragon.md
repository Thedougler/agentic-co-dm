---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "CR 13 Chaotic Evil dragon with cold immunity, cold breath, and ice-walk mobility."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[redwind-isles|Redwind Isles]]"
statblock: inline
name: "Adult White Dragon"
uid: 31ef6614-5837-486e-90fa-d2cb8a86406c
---

# Adult White Dragon

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Adult White Dragon"
size: Huge
type: dragon
alignment: "Chaotic Evil"
ac: 18
hp: 200
hit_dice: "16d12 + 96"
speed: "40 ft., Burrow 30 ft., Fly 80 ft., Swim 40 ft."
stats: [22, 10, 22, 8, 12, 12]
saves:
  - dex: 5
  - wis: 6
damage_immunities: "Cold"
senses: "blindsight 60 ft., darkvision 120 ft.; Passive Perception 21"
languages: "Common, Draconic"
cr: 13
traits:
  - name: "Ice Walk"
    desc: "The dragon can move across and climb icy surfaces without needing to make an ability check. Additionally, Difficult Terrain composed of ice or snow doesn't cost it extra movement."
  - name: "Legendary Resistance (3/Day, or 4/Day in Lair)"
    desc: "If the dragon fails a saving throw, it can choose to succeed instead."
actions:
  - name: "Multiattack"
    desc: "The dragon makes three Rend attacks."
  - name: "Rend"
    desc: "*Melee Attack Roll:* +11, reach 10 ft. 13 (2d6 + 6) Slashing damage plus 4 (1d8) Cold damage."
  - name: "Cold Breath (Recharge 5-6)"
    desc: "*Constitution Saving Throw*: DC 19, each creature in a 60-foot Cone. *Failure:* 54 (12d8) Cold damage. *Success:* Half damage."
legendary_actions:
  - name: "Freezing Burst"
    desc: "*Constitution Saving Throw*: DC 14, each creature in a 30-foot-radius Sphere [Area of Effect]|XPHB|Sphere centered on a point the dragon can see within 120 feet. *Failure:* 7 (2d6) Cold damage, and the target's Speed is 0 until the end of the target's next turn. *Failure or Success*: The dragon can't take this action again until the start of its next turn."
  - name: "Pounce"
    desc: "The dragon moves up to half its Speed, and it makes one Rend attack."
  - name: "Frightful Presence"
    desc: "The dragon casts *Fear*, requiring no Material components and using Charisma as the spellcasting ability (spell save DC 14). The dragon can't take this action again until the start of its next turn."
```
