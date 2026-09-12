---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [faith]
summary: "5e SRD spell text for Bless."
subtype: enchantment
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: b2cf5482-495d-4b83-852b-71375e073551
---

# Bless

**Level:** 1 — Enchantment ([[cleric|Cleric]], [[paladin|Paladin]])

**Casting Time:** Action

**Range:** 30 feet

**Components:** V, S, M (a [[holy-symbol|Holy Symbol]] worth 5+ GP)

**Duration:** Concentration, up to 1 minute

You bless up to three creatures within range. Whenever a target makes an attack roll or a saving throw before the spell ends, the target adds 1d4 to the attack roll or save.

**_Using a Higher-Level Spell Slot._** You can target one additional creature for each spell slot level above 1.

## Simulation Data

```spell
name: Bless
level: 1
school: enchantment
classes: [Cleric, Paladin]
desc: "Whenever a target makes an attack roll or a saving throw, the target adds 1d4 to the roll."
sim:
  modifier: { kind: flat_to_hit, value: 2.5 }
  concentration: true
  range: 30
  notes: "The saving-throw bonus isn't modeled — only the attack-roll bonus (flat_to_hit)."
```
