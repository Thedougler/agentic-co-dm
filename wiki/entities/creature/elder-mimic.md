---
title: "Elder Mimic"
aliases:
  - Elder Mimic
category: entities
tags: [shattered-sea, creature]
sources: ["the-unplotted.md"]
summary: "Doctrine source for The Unplotted. It learns to become the shelter they choose instead of a chest."
provenance:
  extracted: 1.0
  inferred: 0.0
  ambiguous: 0.0
base_confidence: 0.37
lifecycle: accepted
lifecycle_changed: "2026-09-18"
tier: supporting
created: 2026-09-13T22:00:00Z
updated: 2026-09-18
type: creature
reveal: unrevealed
campaign: shattered-sea
visibility: dm
---
# Elder Mimic

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: "Elder Mimic"
size: Medium
type: monstrosity
alignment: Neutral
ac: 12
hp: 58
hit_dice: "9d8 + 18"
speed: "30 ft."
stats: [17, 12, 15, 5, 16, 8]
skillsaves:
  - Stealth: +5
  - Insight: +5
damage_immunities: "acid"
condition_immunities: "prone"
senses: "darkvision 60 ft.; passive Perception 13"
languages: "—"
cr: 2
traits:
  - name: "Adhesive (Object Form Only)"
    desc: "The mimic adheres to anything that touches it. A Huge or smaller creature adhered to the mimic has the Grappled condition (escape DC 13). Ability checks made to escape this grapple have Disadvantage."
  - name: "Perfect False Appearance"
    desc: "While motionless in object form, the mimic is indistinguishable from a harmless, exceptionally well-made version of the object it resembles. If a creature casts Identify on it in this form, the spell reports the object it appears to be, reveals that object's properties, and does not reveal the mimic's nature; any magical effects associated with the apparent object function normally. It has Advantage on Stealth checks made to remain unnoticed in this form."
  - name: "Unbreathing"
    desc: "The mimic doesn't need to breathe."
  - name: "Practiced Escape"
    desc: "The mimic doesn't provoke opportunity attacks when it moves away from a creature it has damaged this turn."
actions:
  - name: "Bite"
    desc: "Melee Weapon Attack: +5 to hit (with advantage if the target is grappled by the mimic), reach 5 ft., one target. Hit: 7 (1d8 + 3) piercing damage plus 4 (1d8) acid damage, or 12 (2d8 + 3) piercing damage plus 4 (1d8) acid damage if the target is grappled by the mimic."
  - name: "Pseudopod"
    desc: "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 7 (1d8 + 3) bludgeoning damage plus 4 (1d8) acid damage. If the target is a Large or smaller creature, it is grappled (escape DC 13) with disadvantage on the check."
bonus_actions:
  - name: "Shape-Shift"
    desc: "The mimic shape-shifts to resemble a Medium or Small object while retaining its game statistics, or it returns to its true blob form. Any equipment it is wearing or carrying isn't transformed."
```

**Wants:** to stay undiscovered indefinitely and get relocated to better, safer ground through someone else's labor. [[delmar-fisk]] claimed it as a consolation prize during the *[[Uncertainty]]*'s break-room refit at [[La Vasca]] and catalogued it as the [[Fleet Commanders Chair]]. It is now trapped aboard a ship at sea with no city's worth of replacement objects left to vanish into.
**Morale:** it never presses a fight it doesn't need to win. It bites once, then Shape-Shifts away to reform elsewhere and breaks line of sight through the nearest hatch or doorway. If cornered with nowhere left to reshape into, it fights for real instead.

> [!narration] Narration
> The captain's chair beat everyone else to the break room. High-backed, deep red leather worn soft at the arms, its legs turned from wood too dark and heavy for a chair this size.
>
> It smells of pipe smoke and old oil, and the leather at the armrest gives a fraction more than good leather should.


## Description

A mimic old and clever enough to have learned that furniture stays in service longer than chests. Sailors tell the standard mimic stories: it wants to look like treasure and hates fire, so crews check every chest before opening it. Nobody tells that story about a chair, and there's no folk warning for this one, because nobody's had reason to write it yet.

## Ecology

Most mimics don't live long enough to grow clever. The first sword swung at an unattended chest cuts down anything young that resembles treasure. Mimics that endure learn the lesson early and permanently: stop being a chest. This one picked furniture instead, patient enough to sit unclaimed for decades wherever nobody thinks to search, feeding on scraps and vermin between the rare meals that come to it. Age sharpened its judgment more than its hunger. A disguise that has fooled a hundred taverns' worth of drunks and dockhands knows which room to sit in and which move gets it carried somewhere better.

It did not work the lesson out on its own. It learned the doctrine from an [[island mimic]], one of its own kind grown past any disguise smaller than a coastline, and then it left. Every patient decade since has been a thing running, and it has never once been back inside sight of that coast.

## Toy Chest

| Verb | Unstable Condition | Consequence | Link of Relevance |
|---|---|---|---|
| Touch it (sit in it, grab it, search it) | It's undetected, still in object form | Its Adhesive trait leaves the toucher **Grappled** and stuck fast, and its Bite then attacks with **Advantage** against them | No direct link. |
| Watch the armrest before it acts | It's about to be touched, or about to bite | The leather gives slightly more than good leather should the instant before something happens. A sharp-eyed PC can read this tell. | No direct link. |
| Grab it and throw it (a Tavern Brawler habit) | It gets kept instead of thrown | The chair has a plan for whoever keeps it. Adhesive leaves them stuck the instant they mean to use it | [[delmar-fisk]] |
| Corner it with every exit covered | It has nowhere left to reshape into | It abandons the chase and fights for real instead of shape-shifting away | No direct link. |

## Prepped Reveals

The chair waits for someone to touch it, then bites once and disappears before anyone can pin it down. Left unhunted, it keeps feeding on whatever's aboard. Ration sacks turn up torn, rope ends turn up bitten, and sooner or later a crew member wakes with a bite mark and no memory of what did it. It isn't trying to kill anyone aboard, but it doesn't need to try hard to hurt one. That gives the crew of the *[[Uncertainty]]* a reason to run it down that has nothing to do with Delmar's pride.
