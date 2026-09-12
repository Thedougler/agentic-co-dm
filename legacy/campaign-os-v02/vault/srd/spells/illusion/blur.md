---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, stealth]
summary: "5e SRD spell text for Blur."
subtype: illusion
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 44c697c2-c6f6-4450-9fb2-321fcfb125a2
---

# Blur

**Level:** 2 — Illusion ([[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** Self

**Components:** V

**Duration:** Concentration, up to 1 minute

Your body becomes blurred. For the duration, any creature has Disadvantage on attack rolls against you. An attacker is immune to this effect if it perceives you with Blindsight or Truesight.

## Simulation Data

```spell
name: Blur
level: 2
school: illusion
classes: [Sorcerer, Wizard]
desc: "Any creature has Disadvantage on attack rolls against you for the duration."
sim:
  modifier: { kind: impose_disadvantage_on_enemy }
  concentration: true
  notes: "The Blindsight/Truesight immunity exception isn't modeled (no perception-type-conditional primitive)."
```
