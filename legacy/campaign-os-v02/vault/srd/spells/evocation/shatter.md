---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, intrigue, combat]
summary: "5e SRD spell text for Shatter."
subtype: evocation
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 922a77ff-fea6-472f-8f80-d21e2fcb1815
---

# Shatter

**Level:** 2 — Evocation ([[bard|Bard]], [[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** 60 feet

**Components:** V, S, M (a chip of mica)

**Duration:** Instantaneous

A loud noise erupts from a point of your choice within range. Each creature in a 10-foot-radius Sphere centered there makes a [[constitution|Constitution]] saving throw, taking 3d8 Thunder damage on a failed save or half as much damage on a successful one. A Construct has Disadvantage on the save.

A nonmagical object that isn't being worn or carried also takes the damage if it's in the spell's area.

**_Using a Higher-Level Spell Slot._** The damage increases by 1d8 for each spell slot level above 2.

## Simulation Data

```spell
name: Shatter
level: 2
school: evocation
classes: [Bard, Sorcerer, Wizard]
desc: "Each creature in a 10-foot-radius Sphere makes a Constitution saving throw."
sim:
  save: { ability: con }
  half_on_save: true
  damage: [{ dice: "3d8", type: thunder }]
  targets: { area: true, radius: 10 }
  range: 60
  scaling:
    per_slot_above: { damage_dice: "1d8" }
  notes: "Construct disadvantage on the save isn't modeled (no target-type-conditional save primitive)."
```
