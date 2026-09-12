---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [horror, mystery]
summary: "CR 2 aberration with confusing gibbering aura and lethal bite."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Gibbering Mouther"
found_at:
- "[[midchain-east|Midchain East]]"
- "[[doldrums|Doldrums]]"
uid: 64814a71-c02c-4728-b560-5a9d149d2691
---

# Gibbering Mouther

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Gibbering Mouther"
size: Medium
type: aberration
alignment: "Chaotic Neutral"
ac: 9
hp: 52
hit_dice: "7d8 + 21"
speed: "20 ft., Swim 20 ft."
stats: [10, 8, 16, 3, 10, 6]
damage_immunities: "Prone"
senses: "darkvision 60 ft.; Passive Perception 10"
cr: 2
traits:
  - name: "Aberrant Ground"
    desc: "The ground in a 10-foot Emanation originating from the mouther is Difficult Terrain."
  - name: "Gibbering"
    desc: "The mouther babbles incoherently while it doesn't have the Incapacitated condition. *Wisdom Saving Throw*: DC 10, any creature that starts its turn within 20 feet of the mouther while it is babbling. *Failure:* The target rolls 1d8 to determine what it does during the current turn: - **1-4**: The target does nothing. - **5-6**: The target takes no action or Bonus Action and uses all its movement to move in a random direction. - **7-8**: The target makes a melee attack against a randomly determined creature within its reach or does nothing if it can't make such an attack."
actions:
  - name: "Bite"
    desc: "*Melee Attack Roll:* +2, reach 5 ft. 7 (2d6) Piercing damage. If the target is a Medium or smaller creature, it has the Prone condition. The target dies if it is reduced to 0 Hit Points by this attack. Its body is then absorbed into the mouther, leaving only equipment behind."
  - name: "Blinding Spittle (Recharge 5-6)"
    desc: "*Dexterity Saving Throw*: DC 10, each creature in a 10-foot-radius Sphere [Area of Effect]|XPHB|Sphere centered on a point within 30 feet. *Failure:* 7 (2d6) Radiant damage, and the target has the Blinded condition until the end of the mouther's next turn."
```
