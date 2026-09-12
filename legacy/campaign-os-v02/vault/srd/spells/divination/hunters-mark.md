---
type: spell
status: srd
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [nature, mystery]
summary: "5e SRD spell text for Hunter's Mark."
subtype: divination
tier: supporting
source: "raw/2026-07/07_Spells.md"
source_url: ""
uid: ace72ded-0d89-4d65-9877-9c2e006e503d
---

# Hunter's Mark

**Level:** 1 — Divination ([[ranger|Ranger]])

**Casting Time:** Bonus Action

**Range:** 90 feet

**Components:** V

**Duration:** Concentration, up to 1 hour

You magically mark one creature you can see within range as your quarry. Until the spell ends, you deal an extra 1d6 Force damage to the target whenever you hit it with an attack roll. You also have Advantage on any [[wisdom|Wisdom]] (Perception or Survival) check you make to find it.

If the target drops to 0 Hit Points before this spell ends, you can take a Bonus Action to move the mark to a new creature you can see within range.

**_Using a Higher-Level Spell Slot._** Your Concentration can last longer with a spell slot of level 3–4 (up to 8 hours) or 5+ (up to 24 hours).

## Simulation Data

```spell
name: Hunter's Mark
level: 1
school: divination
classes: [Ranger]
desc: "You deal an extra 1d6 Force damage to the target whenever you hit it with an attack roll."
sim:
  modifier: { kind: extra_damage, dice: "1d6" }
  action_cost: bonus
  concentration: true
  range: 90
  notes: "The Perception/Survival advantage rider and re-marking on a kill aren't modeled."
```
