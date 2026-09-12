---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [faith, nature]
summary: "5e SRD spell text for Magic Weapon."
subtype: transmutation
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 7dbbcab7-4362-435c-a2d3-4c5d3bf5e4df
---

# Magic Weapon

**Level:** 2 — Transmutation ([[paladin|Paladin]], [[ranger|Ranger]], [[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Bonus Action

**Range:** Touch

**Components:** V, S

**Duration:** 1 hour

You touch a nonmagical weapon. Until the spell ends, that weapon becomes a magic weapon with a +1 bonus to attack rolls and damage rolls. The spell ends early if you cast it again.

**_Using a Higher-Level Spell Slot._** The bonus increases to +2 with a level 3–5 spell slot. The bonus increases to +3 with a level 6+ spell slot.

## Simulation Data

```spell
name: Magic Weapon
level: 2
school: transmutation
classes: [Paladin, Ranger, Sorcerer, Wizard]
desc: "A nonmagical weapon you touch becomes a magic weapon with a +1 bonus to attack rolls and damage rolls."
sim:
  modifier: { kind: flat_to_hit, value: 1 }
  notes: "Only the +1 attack-roll bonus is modeled — the single-modifier compile path can't also carry the matching +1 damage bonus, and the upcast +2/+3 tiers aren't modeled."
```
