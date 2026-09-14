---
title: "Soul Incarnate"
category: entities
tags: [shattered-sea, lore]
sources:
  - "/workspace/midchain-ingest/group-a/npcs/Sir Quackers the Fowl.md"
  - "campaign-os:soul-incarnate.md"
summary: "A signature the Fate Spinner can expose; Sir Quackers carries it without understanding what it means."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.35
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T19:50:00Z
updated: 2026-09-13
type: lore
reveal: unrevealed
campaign: shattered-sea
visibility: dm
kind: fact
truth: partial
scope: "Linked to ley-line phenomena at Yssenmoor"
---

# Soul Incarnate

## Stats & Combat

**Behavior states**

| State | Trigger | Behavior |
|---|---|---|
| **Observing** | Default, no Front trigger has fired | Never initiates contact, and does not act, respond, or reveal itself even under direct threat to anything but its own sealed body. It only records |
| **Engaged** | Something breaches its seal, or the [[Front]]'s trigger condition on [[Sentinels of the Eyrie]] fires | Breaks two centuries of pure observation and fights without restraint, using its full combat suite |

**Wants:** to keep [[Drowned Maw]]'s unbroken, uninterpreted record running past its own death. The current escalation breaks that pattern entirely.
**Morale:** it never flees. Bound to the sealed body beneath [[High Eyrie|the High Eyrie]], it simply stops fighting and returns to observation the moment the threat that forced it to act ends, dead intruder or resolved crisis alike.

> [!narration] Narration
> A figure hangs a foot off the stone where a body should stand, meridian lines burning faint gold along limbs that don't end cleanly at the skin, already facing you before you finish turning, patient as the two centuries it has spent this way. The stone floor holds only the dust of your own steps, and the seal keeps the air still enough to taste. Somewhere beneath your boots, wrapped and stone-dry, the body it left still lies where the order sealed it two hundred years ago. It has always only watched. What you do next is the first thing in a long while it hasn't already seen coming.


```statblock
layout: Basic 5e Layout
name: "Soul Incarnate"
size: Medium
type: undead
alignment: "True Neutral"
ac: 20
hp: 315
hit_dice: "42d8 + 126"
speed: "30 ft., fly 30 ft. (hover)"
stats: [11, 16, 16, 21, 14, 16]
saves:
  - dex: 10
  - con: 10
  - int: 12
  - wis: 9
damage_resistances: "Cold, Lightning"
damage_immunities: "Necrotic, Poison"
condition_immunities: "Charmed, Exhaustion, Frightened, Paralyzed, Poisoned"
senses: "truesight 120 ft.; Passive Perception 19"
languages: "All"
cr: 21
traits:
  - name: "Legendary Resistance (4/Day, or 5/Day within the High Eyrie)"
    desc: "If the Soul Incarnate fails a saving throw, it can choose to succeed instead."
  - name: "Ki-Form"
    desc: "The Soul Incarnate is incorporeal, its meridian-lined form unbound from the body it left behind; it can move through other creatures and objects as if they were difficult terrain, taking 5 (1d10) Force damage if it ends its turn inside an object."
  - name: "Sealed Vessel"
    desc: "If destroyed, the Soul Incarnate reforms in 1d10 days as long as its mummified body remains sealed within the High Eyrie's sea stack, reviving with all its Hit Points. The new ki-form appears in an unoccupied space within the seal."
actions:
  - name: "Multiattack"
    desc: "The Soul Incarnate makes three attacks, using Meridian Strike or Severing Palm in any combination."
  - name: "Meridian Strike"
    desc: "*Melee or Ranged Attack Roll:* +12, reach 5 ft. or range 120 ft. 31 (4d12 + 5) Force damage."
  - name: "Severing Palm"
    desc: "*Melee Attack Roll:* +12, reach 5 ft. 15 (3d6 + 5) Cold damage, and the target has the Paralyzed condition until the start of the Soul Incarnate's next turn."
  - name: "Recorded Discipline"
    desc: "The Soul Incarnate channels two centuries of undying focus in place of spellcasting, using Intelligence as its focusing ability (save DC 20): - **At Will:** *Detect Magic*, *Detect Thoughts*, *Dispel Magic*, *Fireball*, *Invisibility*, *Lightning Bolt*, *Mage Hand*, *Prestidigitation* - **2/Day Each:** *Animate Dead*, *Dimension Door*, *Plane Shift* - **1/Day Each:** *Chain Lightning*, *Finger of Death*, *Power Word Kill*, *Scrying*"
reactions:
  - name: "Protective Focus"
    desc: "The Soul Incarnate casts *Counterspell* or *Shield* in response to the spell's trigger, using the same focusing ability as Recorded Discipline."
legendary_actions:
  - name: "Flowing Step"
    desc: "The Soul Incarnate teleports up to 60 feet to an unoccupied space it can see, and each creature within 10 feet of the space it left takes 11 (2d10) Necrotic damage."
  - name: "Unbroken Record"
    desc: "*Constitution Saving Throw*: DC 20, each creature that isn't an Undead in a 20-foot Emanation originating from the Soul Incarnate. *Failure:* 31 (9d6) Necrotic damage. *Success:* Half damage. *Failure or Success*: The Soul Incarnate can't take this action again until the start of its next turn."
  - name: "Severed Doctrine"
    desc: "The Soul Incarnate casts *Fear*, using the same focusing ability as Recorded Discipline. The Soul Incarnate can't take this action again until the start of its next turn."
```

## Description

A monk who reached lichdom through years of meditation and then ritual desiccation, drinking a mummifying preparation while sealed underground in perfect stillness until the line between life and death gave out. The physical body mummifies and becomes the phylactery. What rises off it takes the shape of a ki-form, a hovering figure traced in glowing meridian lines, incorporeal and unbound by ordinary physical limits. The Soul Incarnate has led [[Sentinels of the Eyrie|the Sentinels of the Eyrie]] in secret for two centuries, guiding the order from beneath [[High Eyrie|the High Eyrie]] without ever once appearing before it.

## Ecology

The Soul Incarnate's body has not moved since the seal closed over it two centuries ago. Everything it knows of [[Drowned Maw]] and the waters past it toward [[Outer Reach]] comes through the same discipline that built it: record what you see, add nothing to it. It shares no lair with anything living, and asks nothing of the Sentinels who pray, drill, and copy ledgers directly over its resting place, unaware a mind still occupies the stone beneath them. The seal never breaks. Each prior escalation at the Maw has spiked and settled at a slightly higher baseline within the record it keeps, and the current one exceeds every prior entry, meeting it with attention instead of the passivity the order's whole doctrine assumes of it.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Bring it a complete, uninterpreted account of the current Maw crisis, delivered by someone trained in the order's own doctrine | The account comes from [[Crissdalynn Khinriss]], the one living Sentinel whose pilgrimage has drawn her closest to its attention | It weighs the account against two centuries of its own record and may share a fragment of that record in answer, the first exchange it has permitted since the seal closed | [[Crissdalynn Khinriss]] |
| Damage or expose the sealed, mummified body beneath [[High Eyrie|the High Eyrie]] | Someone breaches the seal itself, not merely the chamber around it | It abandons pure observation and intervenes directly for the first time in two centuries, an act the order's own founding claim cannot survive once anyone sees it happen | [[Sentinels of the Eyrie]], via the Soul Incarnate's Watch Front |
| Ask it directly what it has recorded of [[Auralis]] | The crew of the *[[Uncertainty]]* can already prove they know the Soul Incarnate exists as a conscious entity, not merely an old founding document | It confirms two centuries of surface observation have found no trace of Auralis at all, though both watch the Maw from opposite sides, each unaware of the other | [[Auralis]] |

## Prepped Reveals

The founding ledgers [[Master Kyzil]] calls "very old" have a conscious author who is still recording. The Soul Incarnate wrote the order's earliest entries itself and has kept the hand consistent across two centuries of copyists since.

> [!check] Investigation or Religion — Reading the Ledger Hand
> DC 20; anyone with access to the archive at [[High Eyrie|the High Eyrie]] may roll.
> **Success:** one hand never changes across two centuries of otherwise-shifting script, an anomaly no living scribe can explain.
> **Failure:** the archive reads as exactly what the order believes it to be, a long unbroken tradition with no single author.
