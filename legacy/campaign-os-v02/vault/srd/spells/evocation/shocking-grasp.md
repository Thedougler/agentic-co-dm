---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, combat]
summary: "5e SRD spell text for Shocking Grasp."
subtype: evocation
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: d24e789e-2608-47d0-862f-49d4fc13b4ab
---

# Shocking Grasp

**Level:** Cantrip — Evocation ([[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** Touch

**Components:** V, S

**Duration:** Instantaneous

Lightning springs from you to a creature that you try to touch. Make a melee spell attack against the target. On a hit, the target takes 1d8 Lightning damage, and it can't make Opportunity Attacks until the start of its next turn.

**_Cantrip Upgrade._** The damage increases by 1d8 when you reach levels 5 (2d8), 11 (3d8), and 17 (4d8).

## Simulation Data

```spell
name: Shocking Grasp
level: 0
school: evocation
classes: [Sorcerer, Wizard]
desc: "Lightning springs from you to a creature that you try to touch."
sim:
  attack_type: melee_spell
  reach: 5
  damage: [{ dice: "1d8", type: lightning }]
  cantrip_scaling:
    5: { damage: [{ dice: "2d8", type: lightning }] }
    11: { damage: [{ dice: "3d8", type: lightning }] }
    17: { damage: [{ dice: "4d8", type: lightning }] }
  notes: "Opportunity-attack denial on the target isn't modeled (no such primitive)."
```
