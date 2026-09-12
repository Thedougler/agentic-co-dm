---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane, undead]
summary: "5e SRD spell text for False Life."
subtype: necromancy
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: d75445a6-1b5c-4cb9-a901-2dd62eb93971
---

# False Life

**Level:** 1 — Necromancy ([[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** Self

**Components:** V, S, M (a drop of alcohol)

**Duration:** Instantaneous

You gain 2d4 + 4 Temporary Hit Points.

**_Using a Higher-Level Spell Slot._** You gain 5 additional Temporary Hit Points for each spell slot level above 1.

## Simulation Data

```spell
name: False Life
level: 1
school: necromancy
classes: [Sorcerer, Wizard]
desc: "You gain 2d4 + 4 Temporary Hit Points."
sim:
  temp_hp: { amount: 9 }
  notes: "amount is the average roll of 2d4+4 (9) — the temp_hp modifier takes a flat number, not a dice expression."
```
