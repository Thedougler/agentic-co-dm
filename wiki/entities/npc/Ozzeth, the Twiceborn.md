---
title: "Ozzeth, the Twiceborn"
category: entities
tags: ["shattered-sea", "npc", "combat"]
sources:
  - "campaign-os:ozzeth-the-twiceborn.md"
created: 2026-09-13
updated: 2026-09-13
type: npc
lifecycle: proposed
lifecycle_changed: "2026-09-13"
reveal: unrevealed
campaign: shattered-sea
visibility: dm
summary: "A Grung mage branded Twiceborn by Gold caste, guards Magazine Delta in the sewers with control spells and dominates foes."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
base_confidence: 0.55
tier: supporting
---
# Ozzeth, the Twiceborn

**Wants:** to keep [[Simone]]'s unsealed color-rite stable from a distance, the one secret his own Twiceborn brand couldn't take from him, while Gold caste's reputation-work keeps him too disgraced to ever ask for open help.

> [!narration] Narration
> A wiry Grung crouches at the tide line inside Magazine Delta, mottled green-and-grey hide slick with sewer damp, eyes fixed on the vent above for movement. His hands are never still when he casts (red climbs one palm as blue drains from the other), the stalled Gold-caste rite still trying, uselessly, to finish what it started years ago.


*Ozzeth*: "Hold still. This won't take long. Not for you."

"Twiceborn" is not a name Ozzeth chose. It's Gold caste's own official term of censure, the brand stamped on a Grung caught mid-shift with an unsealed, incomplete color change. He and Simone Tabarnack, both power-hungry, independently found the same suppressed rite Gold caste keeps for reordering *someone else's* caste: a governance and punishment tool, never built to run on its own holder. Turned inward, it doesn't finish. His hands shifting red and blue mid-cast is that rite still stuck, permanently, mid-transfer. Gold couldn't move against him openly without admitting the rite exists and works, so the punishment went sideways, through reputation instead of force. With no standing of his own to resist it, "the mage-abomination" stuck outright, immediate and unchallenged. See [[Grung clans|Grung Clans]] for the caste-color mechanism this rests on.

Ozzeth found the rite first and went further with it than Simone ever managed alone, and he spent years keeping hers stable even after his own brand cost him everything that secret should have protected. He casts [[Sending]] freely, on his own schedule instead of hers, so no watcher can predict the timing, and checks in with her often. She looks up to him for the maintenance nobody else in her garrison ever suspected existed.

| Field | Value |
|---|---|
| Primary goal | Keep [[Simone]]'s unsealed color-rite from collapsing, at any distance. |
| Consistent method | Checks in by [[Sending]], timed to his own schedule instead of hers, so no watcher learns the pattern. |
| Active problem | His own miscarried rite marked him "mage-abomination," so any help he offers has to travel through Sending, never his own name. |
| Performance hooks | The silent professional who never explains himself + a casting hand that visibly bleeds color, red climbing one palm as blue drains the other. |
| Link of relevance | [[Jean-Claude Tabarnack]]: Ozzeth's death at his hands in Session 06 is what finally leaves Simone's rite unmaintained. |

> [!mechanic]
> **Ozzeth's Ossketh — incomplete arcane transmutation, background process.** The self-cast color-sealing rite never finished; it has been running unstably on his body for years (visible as the red-and-blue color shift in his hands during spellcasting). [[Detect Magic]] near Ozzeth: "Arcane transmutation — like a spell caught mid-execution, still running." His spellcasting is standard Arcane ([[Intelligence]], wizard tradition) and is separate from the Ossketh. The unstable Ossketh is a background process — [[Counterspell]] cannot target it.

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: Ozzeth, the Twiceborn
size: Small
type: humanoid
subtype: grung
campaign: shattered-sea
alignment: lawful evil
ac: 16
ac_class: mage armour (chromatic ward)
hp: 130
hit_dice: 20d6 + 60
speed: "25 ft., climb 25 ft., swim 30 ft."
stats: [8, 16, 16, 20, 14, 16]
saves:
  - constitution: 6
  - intelligence: 8
  - wisdom: 5
skillsaves:
  - arcana: 8
  - deception: 6
  - insight: 5
  - stealth: 6
damage_immunities: "poison"
condition_immunities: "poisoned"
senses: "passive Perception 15"
languages: "Grung, Common, Deep Speech"
cr: 8
traits:
  - name: Twiceborn Will
    desc: "Ozzeth has advantage on Constitution saving throws to maintain concentration, and advantage on saving throws against being charmed or frightened. A being whose own body has broken the caste order does not bend easily to anyone else's."
  - name: Chromatic Anomaly
    desc: "Ozzeth's skin runs blue and red at once, the colours shifting as he moves. He is never surprised while he can see, and a creature that tries to read his caste, rank, or intent by sight (an Insight check to gauge him) has disadvantage — the signal he broadcasts is a contradiction. Purely diegetic; it grants no combat bonus beyond this."
  - name: Standing Leap
    desc: "Ozzeth's long jump is 25 feet and his high jump is 15 feet, with or without a running start."
  - name: Toxic Skin
    desc: "A creature that touches Ozzeth or hits him with a melee attack while within 5 feet, or that grapples him, must succeed on a DC 14 Constitution saving throw or take 5 (2d4) poison damage and be poisoned until the start of its next turn."
  - name: Spellcasting
    desc: "Ozzeth is a 9th-level spellcaster. His spellcasting ability is Intelligence (spell save DC 16, +8 to hit with spell attacks). He casts with no verbal components — his conjuring is scent, gesture, and colour. Cantrips (at will): mind sliver, minor illusion, poison spray, message. 1st level (4 slots): shield, charm person, disguise self, silent image. 2nd level (3 slots): hold person, misty step, mirror image. 3rd level (3 slots): fireball, fear, hypnotic pattern. 4th level (3 slots): greater invisibility, dimension door, phantasmal killer. 5th level (1 slot): dominate person."
  - name: "Legendary Resistance (2/Day)"
    desc: "If Ozzeth fails a saving throw, he can choose to succeed instead."
actions:
  - name: Multiattack
    desc: "Ozzeth casts one cantrip and makes one Venom Lash attack."
  - name: Venom Lash
    desc: "Melee Weapon Attack (tongue): +6 to hit, reach 10 ft., one target. Hit: 5 (1d4 + 3) piercing damage, and the target must succeed on a DC 14 Constitution saving throw or take 7 (2d6) poison damage. Ozzeth can pull a target of Medium size or smaller 5 feet toward him on a hit."
  - name: Poison Spray (Cantrip)
    desc: "One creature within 10 feet must succeed on a DC 16 Constitution saving throw or take 11 (2d10) poison damage. (Grung venom, wept as a needle-fine mist.)"
bonus_actions:
  - name: Misty Step (2nd-Level Slot)
    desc: "Ozzeth teleports up to 30 feet to an unoccupied space he can see."
reactions:
  - name: Shield (1st-Level Slot)
    desc: "When hit by an attack or targeted by magic missile, Ozzeth gains a +5 bonus to AC until the start of his next turn, including against the triggering attack, and takes no damage from magic missile."
legendary_actions:
  - name: Weeping Cantrip
    desc: "Ozzeth casts a cantrip (typically poison spray or mind sliver)."
  - name: Slip the Skin
    desc: "Ozzeth moves up to his speed without provoking opportunity attacks. He may climb or enter water as part of this move."
  - name: Pull the Thread (Costs 2 Actions)
    desc: "Ozzeth targets one creature charmed, frightened, or dominated by him that he can see within 60 feet. That creature immediately uses its reaction to move up to its speed and make one weapon attack against a target of Ozzeth's choice."
```

A small grung mage whose chromatic ward and 130 hit points of spellcasting prowess once stood watch at [[Verdant Teeth]] and [[Orak]] before he took up his post in Magazine Delta.

Guards **Room T2 (Magazine Delta)** with [[Purple-Caste Zealot]] in [[Calveno Sewer Magazines]] (Session 06 roster, reworked 2026-07-03). He left mobile work, and a drunk mage, blind monk, and mage-abomination took the remaining slots. He swims 30 ft. and casts control spells well; the Zealot is a walking bomb, so watch the barrels.

Ozzeth casts with no speech, and [[Silence]] won't stop him (that trick won't work here). The Purple-Caste Zealot draws all fire, freeing him up to use *dominate person* and other control magic. [[Dominate Person]] is best, used once per fight at the right moment.

## Connections

- [[Purple-Caste Zealot]]: escort, guards Room T2/Magazine Delta alongside him
- [[Vashu the Weeping Veil|Vashu, the Weeping Veil]]: fellow guardian, Room T1/Magazine Gamma
- [[Bazzoth, the Steeped]]: fellow guardian, Room 5/Magazine Beta
- [[Ozvok, the Vermillion Distiller]]: related [[Grung]] alchemist figure
- [[Solange Barret]]: red-caste warlock, Room 8
- [[Grung clans|Grung Clans]]: faction
- [[Calveno Sewer Magazines]]: guards Room T2/Magazine Delta of this dungeon
- [[Simone Tabarnack]]: found the color-sealing rite
  independently, then became her mentor, keeping her own unsealed rite
  stable for years; his death here leaves it unmaintained

## Session Log

**Session 06** (`vault/episodes/006/`): fought in the Primary Chamber, warding [[Solange Barret|Solange]]'s spell as his hands shifted red and blue. He cast Dominate Person at [[Delmar Fisk]], but Delmar saved (roll 19, plus [[Jean-Claude Tabarnack|Jean-Claude]]'s help for 20) and shook it off.

Mid-fight, stood by Solange. Placed a hand on her shoulder and said “you can do this.” Cast [[Misty Step]] and [[Greater Invisibility]] to keep her safe. She kept casting her spell.

Killed later in the same fight. Delmar shot his arm. Jean-Claude cast [[Hunter's Mark]] and finished him with a bow (17 to hit, 13 damage). His last act: grabbed Solange's shoulder and said “do it now” before he fell.
