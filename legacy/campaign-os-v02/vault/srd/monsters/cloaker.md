---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, mystery]
summary: "Large aberration (CR 8) that attaches to blind prey, uses tail strikes, and frightens with Moan or Mirror Image."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Cloaker"
found_at:
- "[[midchain-east|Midchain East]]"
- "[[shelfworks|Shelfworks]]"
uid: 1da275d0-83ee-4248-a4c9-550fe3cdafde
---

# Cloaker

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Cloaker"
size: Large
type: aberration
alignment: "Chaotic Neutral"
ac: 14
hp: 91
hit_dice: "14d10 + 14"
speed: "10 ft., Fly 40 ft."
stats: [17, 15, 12, 13, 14, 7]
damage_immunities: "Frightened"
senses: "darkvision 120 ft.; Passive Perception 12"
languages: "Deep Speech, Undercommon"
cr: 8
traits:
  - name: "Light Sensitivity"
    desc: "While in Bright Light, the cloaker has Disadvantage on attack rolls."
actions:
  - name: "Multiattack"
    desc: "The cloaker makes one Attach attack and two Tail attacks."
  - name: "Attach"
    desc: "*Melee Attack Roll:* +6, reach 5 ft. 13 (3d6 + 3) Piercing damage. If the target is a Large or smaller creature, the cloaker attaches to it. While the cloaker is attached, the target has the Blinded condition, and the cloaker can't make Attach attacks against other targets. In addition, the cloaker halves the damage it takes (round down), and the target takes the same amount of damage. The cloaker can detach itself by spending 5 feet of movement. The target or a creature within 5 feet of it can take an action to try to detach the cloaker, doing so by succeeding on a DC 14 Strength (Athletics) check."
  - name: "Tail"
    desc: "*Melee Attack Roll:* +6, reach 10 ft. 8 (1d10 + 3) Slashing damage."
bonus_actions:
  - name: "Moan"
    desc: "*Wisdom Saving Throw*: DC 13, each creature in a 60-foot Emanation originating from the cloaker. *Failure:* The target has the Frightened condition until the end of the cloaker's next turn. *Success:* The target is immune to this cloaker's Moan for the next 24 hours."
  - name: "Phantasms (Recharge after a Short or Long Rest)"
    desc: "The cloaker casts the *Mirror Image* spell, requiring no spell components and using Wisdom as the spellcasting ability. The spell ends early if the cloaker starts or ends its turn in Bright Light."
```
