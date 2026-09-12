---
type: monster
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat, horror]
summary: "CR 2 shape-shifting monstrosity with adhesive grapple and acid attacks."
tier: supporting
source: "raw/2026-07/12_MonstersA-Z.md"
source_url: ""
subtype: srd
statblock: inline
name: "Mimic"
found_at:
- "[[shelfworks|Shelfworks]]"
- "[[the-drowned-maw|The Drowned Maw]]"
uid: 921ca172-2df2-4909-ba89-dc6452d320a5
---

# Mimic

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Mimic"
size: Medium
type: monstrosity
alignment: "Neutral"
ac: 12
hp: 58
hit_dice: "9d8 + 18"
speed: "20 ft."
stats: [17, 12, 15, 5, 13, 8]
damage_immunities: "Acid"
condition_immunities: "Prone"
senses: "darkvision 60 ft.; Passive Perception 11"
cr: 2
traits:
  - name: "Adhesive (Object Form Only)"
    desc: "The mimic adheres to anything that touches it. A Huge or smaller creature adhered to the mimic has the Grappled condition (escape DC 13). Ability checks made to escape this grapple have Disadvantage."
actions:
  - name: "Bite"
    desc: "*Melee Attack Roll:* +5 (with Advantage if the target is Grappled by the mimic), reach 5 ft. 7 (1d8 + 3) Piercing damage—or 12 (2d8 + 3) Piercing damage if the target is Grappled by the mimic—plus 4 (1d8) Acid damage."
  - name: "Pseudopod"
    desc: "*Melee Attack Roll:* +5, reach 5 ft. 7 (1d8 + 3) Bludgeoning damage plus 4 (1d8) Acid damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 13). Ability checks made to escape this grapple have Disadvantage."
bonus_actions:
  - name: "Shape-Shift"
    desc: "The mimic shape-shifts to resemble a Medium or Small object while retaining its game statistics, or it returns to its true blob form. Any equipment it is wearing or carrying isn't transformed."
```
