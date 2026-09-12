---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [nature, intrigue, combat]
summary: "5e SRD spell text for Faerie Fire."
subtype: evocation
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: aed27082-6836-45c1-b04e-b680af974650
---

# Faerie Fire

**Level:** 1 — Evocation ([[bard|Bard]], [[druid|Druid]])

**Casting Time:** Action

**Range:** 60 feet

**Components:** V

**Duration:** Concentration, up to 1 minute

Objects in a 20-foot Cube within range are outlined in blue, green, or violet light (your choice). Each creature in the Cube is also outlined if it fails a [[dexterity|Dexterity]] saving throw. For the duration, objects and affected creatures shed Dim Light in a 10-foot radius and can't benefit from the [[invisible|Invisible]] condition.

Attack rolls against an affected creature or object have Advantage if the attacker can see it.

## Simulation Data

```spell
name: Faerie Fire
level: 1
school: evocation
classes: [Bard, Druid]
desc: "Each creature in the Cube is outlined in light if it fails a Dexterity saving throw."
sim:
  save: { ability: dex }
  effects: [{ effect: lit }]
  targets: { area: true, radius: 20 }
  range: 60
  concentration: true
```
