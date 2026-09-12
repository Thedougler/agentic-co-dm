---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, combat]
summary: "5e SRD spell text for Scorching Ray."
subtype: evocation
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 96e18693-2624-4ced-9e74-7aa9d3cad807
---

# Scorching Ray

**Level:** 2 — Evocation ([[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** 120 feet

**Components:** V, S

**Duration:** Instantaneous

You hurl three fiery rays. You can hurl them at one target within range or at several. Make a ranged spell attack for each ray. On a hit, the target takes 2d6 Fire damage.

**_Using a Higher-Level Spell Slot._** You create one additional ray for each spell slot level above 2.

## Simulation Data

```spell
name: Scorching Ray
level: 2
school: evocation
classes: [Sorcerer, Wizard]
desc: "You hurl three fiery rays, one ranged spell attack per ray."
sim:
  attack_type: ranged_spell
  range: 120
  attack_count: 3
  damage: [{ dice: "2d6", type: fire }]
  scaling:
    per_slot_above: { attack_count: 1 }
```
