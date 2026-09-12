---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [undead, horror]
summary: "CR 3 small undead with curse-delivering rotting fist and frightening gaze."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Mummy"
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[the-drowned-maw|The Drowned Maw]]"
uid: 6880effd-2ba8-4c2b-869e-f5721ac18196
---

# Mummy

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Mummy"
size: Small
type: undead
alignment: "Lawful Evil"
ac: 11
hp: 58
hit_dice: "9d8 + 18"
speed: "20 ft."
stats: [16, 8, 15, 6, 12, 12]
saves:
  - wis: 3
damage_vulnerabilities: "Fire"
damage_immunities: "Necrotic, Poison"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Poisoned"
senses: "darkvision 60 ft.; Passive Perception 11"
languages: "Common plus two other languages"
cr: 3
actions:
  - name: "Multiattack"
    desc: "The mummy makes two Rotting Fist attacks and uses Dreadful Glare."
  - name: "Rotting Fist"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 8 (1d10 + 3) Bludgeoning damage plus 10 (3d6) Necrotic damage. If the target is a creature, it is cursed. While cursed, the target can't regain Hit Points, its Hit Point maximum doesn't return to normal when finishing a Long Rest, and its Hit Point maximum decreases by 10 (3d6) every 24 hours that elapse. A creature dies and turns to dust if reduced to 0 Hit Points by this attack."
  - name: "Dreadful Glare"
    desc: "*Wisdom Saving Throw*: DC 11, one creature the mummy can see within 60 feet. *Failure:* The target has the Frightened condition until the end of the mummy's next turn. *Success:* The target is immune to this mummy's Dreadful Glare for 24 hours."
```
