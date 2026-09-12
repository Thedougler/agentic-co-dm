---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "5e SRD spell text for Hex."
subtype: enchantment
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: b6dc612c-652b-4a89-87aa-deb338c1218b
---

# Hex

**Level:** 1 — Enchantment ([[warlock|Warlock]])

**Casting Time:** Bonus Action

**Range:** 90 feet

**Components:** V, S, M (the petrified eye of a newt)

**Duration:** Concentration, up to 1 hour

You place a curse on a creature that you can see within range. Until the spell ends, you deal an extra 1d6 Necrotic damage to the target whenever you hit it with an attack roll. Also, choose one ability when you cast the spell. The target has Disadvantage on ability checks made with the chosen ability.

If the target drops to 0 Hit Points before this spell ends, you can take a Bonus Action on a later turn to curse a new creature.

**_Using a Higher-Level Spell Slot._** Your Concentration can last longer with a spell slot of level 2 (up to 4 hours), 3–4 (up to 8 hours), or 5+ (24 hours).

## Simulation Data

```spell
name: Hex
level: 1
school: enchantment
classes: [Warlock]
desc: "You deal an extra 1d6 Necrotic damage to the target whenever you hit it with an attack roll."
sim:
  modifier: { kind: extra_damage, dice: "1d6" }
  action_cost: bonus
  concentration: true
  range: 90
  notes: "The disadvantage-on-one-ability-check rider and re-cursing on a kill aren't modeled."
```
