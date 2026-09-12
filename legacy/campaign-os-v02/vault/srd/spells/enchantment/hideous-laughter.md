---
type: spell
status: srd
publish: false
aliases: ["Tasha's Hideous Laughter"]
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, intrigue]
summary: "5e SRD spell text for Hideous Laughter."
subtype: enchantment
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 02578b32-be97-4a69-bc0a-f87392a1b74f
---

# Hideous Laughter

**Level:** 1 — Enchantment ([[bard|Bard]], [[warlock|Warlock]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** 30 feet

**Components:** V, S, M (a tart and a feather)

**Duration:** Concentration, up to 1 minute

One creature of your choice that you can see within range makes a [[wisdom|Wisdom]] saving throw. On a failed save, it has the [[prone|Prone]] and [[incapacitated|Incapacitated]] conditions for the duration. During that time, it laughs uncontrollably if it's capable of laughter, and it can't end the [[prone|Prone]] condition on itself.

At the end of each of its turns and each time it takes damage, it makes another Wisdom saving throw. The target has Advantage on the save if the save is triggered by damage. On a successful save, the spell ends.

**_Using a Higher-Level Spell Slot._** You can target one additional creature for each spell slot level above 1.

## Simulation Data

```spell
name: Hideous Laughter
level: 1
school: enchantment
classes: [Bard, Warlock, Wizard]
desc: "One creature makes a Wisdom saving throw. On a failed save, it has the Prone and Incapacitated conditions for the duration."
sim:
  save: { ability: wis }
  effects: [{ effect: incapacitated_prone, save_ends: { save: wis, timing: end_of_turn, also_on_damage: true } }]
  targets: { area: false, count: 1 }
  range: 30
  concentration: true
```
