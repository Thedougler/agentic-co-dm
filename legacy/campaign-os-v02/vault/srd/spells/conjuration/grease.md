---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "5e SRD spell text for Grease."
subtype: conjuration
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 334f5ebb-470e-45dc-b99f-deeb27832e50
---

# Grease

**Level:** 1 — Conjuration ([[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** 60 feet

**Components:** V, S, M (a bit of pork rind or butter)

**Duration:** 1 minute

Nonflammable grease covers the ground in a 10 foot square centered on a point within range and turns it into Difficult Terrain for the duration.

When the grease appears, each creature standing in its area must succeed on a [[dexterity|Dexterity]] saving throw or have the [[prone|Prone]] condition. A creature that enters the area or ends its turn there must also succeed on that save or fall [[prone|Prone]].

## Simulation Data

```spell
name: Grease
level: 1
school: conjuration
classes: [Sorcerer, Wizard]
desc: "Each creature standing in the area must succeed on a Dexterity saving throw or fall Prone."
sim:
  save: { ability: dex }
  effects: [{ effect: prone }]
  targets: { area: true, radius: 5 }
  range: 60
  notes: "Only the on-cast save is modeled; the repeat save for entering/ending a turn in the area isn't."
```
