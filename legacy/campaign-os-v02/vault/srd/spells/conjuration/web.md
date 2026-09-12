---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [arcane]
summary: "5e SRD spell text for Web."
subtype: conjuration
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: 20aa71c6-3ca5-4116-af4f-d5f54cc0e4fe
---

# Web

**Level:** 2 — Conjuration ([[sorcerer|Sorcerer]], [[wizard|Wizard]])

**Casting Time:** Action

**Range:** 60 feet

**Components:** V, S, M (a bit of spiderweb)

**Duration:** Concentration, up to 1 hour

You conjure a mass of sticky webbing at a point within range. The webs fill a 20-foot Cube there for the duration. The webs are Difficult Terrain, and the area within them is Lightly Obscured.

If the webs aren't anchored between two solid masses (such as walls or trees) or layered across a floor, wall, or ceiling, the web collapses on itself, and the spell ends at the start of your next turn. Webs layered over a flat surface have a depth of 5 feet.

The first time a creature enters the webs on a turn or starts its turn there, it must succeed on a [[dexterity|Dexterity]] saving throw or have the [[restrained|Restrained]] condition while in the webs or until it breaks free.

A creature Restrained by the webs can take an action to make a [[strength|Strength]] (Athletics) check against your spell save DC. If it succeeds, it is no longer Restrained.

The webs are flammable. Any 5-foot Cube of webs exposed to fire burns away in 1 round, dealing 2d4 Fire damage to any creature that starts its turn in the fire.

## Simulation Data

```spell
name: Web
level: 2
school: conjuration
classes: [Sorcerer, Wizard]
desc: "A creature entering the webs must succeed on a Dexterity saving throw or become Restrained."
sim:
  save: { ability: dex }
  effects: [{ effect: restrained, save_ends: { save: str, timing: end_of_turn } }]
  targets: { area: true, radius: 20 }
  range: 60
  concentration: true
  notes: "The real escape is a Strength (Athletics) check on the creature's own action, not a repeat saving throw — approximated here as a str save_ends. The fire-vulnerability rider isn't modeled."
```
