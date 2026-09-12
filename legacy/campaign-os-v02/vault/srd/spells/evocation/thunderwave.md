---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [nature, arcane, combat]
summary: "5e SRD spell text for Thunderwave."
subtype: evocation
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 5f91be60-4d85-4bc7-926b-d8ab88ea5dd8
---

# Thunderwave

**Level:** 1 — Evocation ([[bard|Bard]], [[druid|Druid]], [[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** Self

**Components:** V, S

**Duration:** Instantaneous

You unleash a wave of thunderous energy. Each creature in a 15-foot Cube originating from you makes a [[constitution|Constitution]] saving throw. On a failed save, a creature takes 2d8 Thunder damage and is pushed 10 feet away from you. On a successful save, a creature takes half as much damage only.

In addition, unsecured objects that are entirely within the Cube are pushed 10 feet away from you, and a thunderous boom is audible within 300 feet.

**_Using a Higher-Level Spell Slot._** The damage increases by 1d8 for each spell slot level above 1.

## Simulation Data

```spell
name: Thunderwave
level: 1
school: evocation
classes: [Bard, Druid, Sorcerer, Wizard]
desc: "Each creature in a 15-foot Cube originating from you makes a Constitution saving throw."
sim:
  save: { ability: con }
  half_on_save: true
  damage: [{ dice: "2d8", type: thunder }]
  targets: { area: true, radius: 15 }
  scaling:
    per_slot_above: { damage_dice: "1d8" }
  notes: "The forced 10-foot push on a failed save isn't modeled (no forced-movement primitive)."
```
