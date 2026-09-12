---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "CR 1/4 small elemental with blurred form and death burst; steam breath reduces movement."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Steam Mephit"
found_at:
- "[[ashwall-islands|Ashwall Islands]]"
- "[[midchain-south|Midchain South]]"
uid: 7b047f16-f07f-46fc-b8ba-3ac19127c156
---

# Steam Mephit

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Steam Mephit"
size: Small
type: elemental
alignment: "Neutral Evil"
ac: 10
hp: 17
hit_dice: "5d6"
speed: "30 ft., Fly 30 ft."
stats: [5, 11, 10, 11, 10, 12]
damage_immunities: "Fire, Poison"
condition_immunities: "Exhaustion, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 10"
languages: "Primordial (Aquan, Ignan)"
cr: "1/4"
traits:
  - name: "Blurred Form"
    desc: "Attack rolls against the mephit are made with Disadvantage unless the mephit has the Incapacitated condition."
  - name: "Death Burst"
    desc: "The mephit explodes when it dies. *Dexterity Saving Throw*: DC 10, each creature in a 5-foot Emanation originating from the mephit. *Failure:* 5 (2d4) Fire damage. *Success:* Half damage."
actions:
  - name: "Claw"
    desc: "*Melee Attack Roll:* +2, reach 5 ft. 2 (1d4) Slashing damage plus 2 (1d4) Fire damage."
  - name: "Steam Breath (Recharge 6)"
    desc: "*Constitution Saving Throw*: DC 10, each creature in a 15-foot Cone. *Failure:* 5 (2d4) Fire damage, and the target's Speed decreases by 10 feet until the end of the mephit's next turn. *Success:* Half damage only. *Failure or Success*: Being underwater doesn't grant Resistance to this Fire damage."
```
