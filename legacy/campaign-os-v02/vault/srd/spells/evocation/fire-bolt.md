---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, combat]
summary: "5e SRD spell text for Fire Bolt."
subtype: evocation
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 1f03d375-a0de-4ad9-a5f9-00687f005028
---

# Fire Bolt

**Level:** Cantrip — Evocation ([[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** 120 feet

**Components:** V, S

**Duration:** Instantaneous

You hurl a mote of fire at a creature or an object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 Fire damage. A flammable object hit by this spell starts burning if it isn't being worn or carried.

**_Cantrip Upgrade._** The damage increases by 1d10 when you reach levels 5 (2d10), 11 (3d10), and 17 (4d10).

## Simulation Data

```spell
name: Fire Bolt
level: 0
school: evocation
classes: [Sorcerer, Wizard]
desc: "You hurl a mote of fire at a creature or an object within range."
sim:
  id: fire_bolt
  attack_type: ranged_spell
  range: 120
  damage: [{ dice: "1d10", type: fire }]
  cantrip_scaling:
    5: { damage: [{ dice: "2d10", type: fire }] }
    11: { damage: [{ dice: "3d10", type: fire }] }
    17: { damage: [{ dice: "4d10", type: fire }] }
```
