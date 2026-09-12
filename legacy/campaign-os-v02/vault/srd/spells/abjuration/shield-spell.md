---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "5e SRD spell text for Shield."
subtype: abjuration
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 3b8574c2-c0ba-4c81-8f89-83dfad596a33
---

# Shield

**Level:** 1 — Abjuration ([[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Reaction, which you take when you are hit by an attack roll or targeted by the _[[magic-missile|Magic Missile]]_ spell

**Range:** Self

**Components:** V, S

**Duration:** 1 round

An imperceptible barrier of magical force protects you. Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, and you take no damage from _[[magic-missile|Magic Missile]]_.

## Simulation Data

```spell
name: Shield
level: 1
school: abjuration
classes: [Sorcerer, Wizard]
desc: "You have a +5 bonus to AC, including against the triggering attack, until the start of your next turn."
sim:
  modifier: { kind: reaction_ac_bonus, bonus: 5 }
  action_cost: reaction
  notes: "Magic Missile immunity isn't modeled (no spell-name-conditional immunity primitive)."
```
