---
title: "Bazzoth, the Steeped"
aliases:
  - Bazzoth, the Steeped
category: entities
tags: [shattered-sea, npc]
sources:
  - "campaign-os:bazzoth-the-steeped.md"
created: 2026-09-13
updated: 2026-09-13
type: npc
reveal: revealed
campaign: shattered-sea
visibility: dm
summary: "An old red-caste Grung alchemist and CR 6 magazine guardian in the Calveno Sewers, killed in Session 05."
provenance:
  extracted: 0.85
  inferred: 0.10
  ambiguous: 0.05
tier: supporting
---
# Bazzoth, the Steeped

# Bazzoth, the Steeped

An old red-caste Grung. Thick, heavyset, with a mottled brick-red hide and sagging throat. He wore a bone-plate apron over vials of reagent and carried a drinking gourd at all times.

He guarded **Room 5** in the [[Calveno Sewer Magazines]] dungeon, where two [[Grung]] laborers worked with him. Dead in Session 05, he used a Sump-Reek Bomb but still fell. His death destroyed the room's powder barrels; this was the second magazine down, after [[le-paludi]]'s Magazine Alpha fell first.

> [!mechanic]
> **Shed the Years** is a bonus-action rite. While active: +15 ft. speed, no opportunity attacks, +2 AC, advantage on Dex saves, and a third Envenomed Lash at +8 to hit. Any hit or a failed DC 15 Con save ends it. Steeped gives advantage against charm/fear and on Con saves. Toxic Secretion and Master of the Bench punish melee foes. Reeking Step (3/day) teleports him when hit. Sump-Reek Bomb (Recharge 5, 6) deals area damage: a 20-ft. poison cloud forcing saves each round.
> **Tradition and school:** Shed the Years — Arcane transmutation (concentration); Counterspell can target it, breaking concentration ends it; Detect Magic while active: "Arcane transmutation — the caster's body is burning through time it doesn't have left." Reeking Step — Arcane conjuration (teleportation); Counterspell can target each use. Sump-Reek Bomb — Arcane conjuration (area conjured poison cloud); no concentration.

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: Bazzoth, the Steeped
size: Small
type: humanoid
subtype: grung
campaign: shattered-sea
alignment: lawful evil
ac: 15
ac_class: bone-plate apron and bench-harness
hp: 132
hit_dice: 24d6 + 48
speed: "25 ft., climb 25 ft., swim 25 ft."
stats: [9, 14, 15, 18, 12, 15]
saves:
  - constitution: 5
  - intelligence: 7
skillsaves:
  - arcana: 7
  - medicine: 7
  - nature: 7
  - insight: 4
damage_immunities: "poison"
condition_immunities: "poisoned"
senses: "passive Perception 14"
languages: "Grung, Common"
cr: 6
traits:
  - name: Steeped
    desc: "Bazzoth is soused on the same reagent-spirits he distils, and it has pickled fear and doubt out of him. He has advantage on saving throws against being charmed or frightened, and on Constitution saving throws made to maintain concentration. A creature relying on scent to track or read him works at a disadvantage."
  - name: Toxic Secretion
    desc: "A creature that touches Bazzoth or hits him with a melee attack while within 5 feet, or that grapples him, must succeed on a DC 13 Constitution saving throw or take 5 (2d4) poison damage and be poisoned until the start of its next turn."
  - name: Standing Leap
    desc: "Bazzoth's long jump is 25 feet and his high jump is 15 feet, with or without a running start. He rarely bothers — until the rite is on him (see Shed the Years)."
  - name: Master of the Bench
    desc: "Bazzoth is never surprised while conscious, and is immune to the effects of his own concoctions. A creature that is poisoned has disadvantage on saving throws against his concoctions until the end of its next turn."
  - name: "Legendary Resistance (1/Day)"
    desc: "If Bazzoth fails a saving throw, he can choose to succeed instead. The old vintage does not go over on the first push — and the rite does not break on the first good hit."
actions:
  - name: Multiattack
    desc: "Bazzoth makes two attacks, using Hurled Flask or Envenomed Lash in any combination. While Shed the Years is active, he makes one additional Envenomed Lash attack."
  - name: Hurled Flask
    desc: "Ranged Weapon Attack: +6 to hit, range 30/90 ft., one target. Hit: 11 (2d8 + 2) acid damage. Bazzoth can deal poison damage instead of acid (his choice each throw), and the target has disadvantage on the next saving throw it makes against one of Bazzoth's concoctions before the end of Bazzoth's next turn."
  - name: Envenomed Lash
    desc: "Melee Weapon Attack: +6 to hit, reach 10 ft., one target. Hit: 9 (2d6 + 2) poison damage, and the target must succeed on a DC 15 Constitution saving throw or be poisoned until the end of its next turn. While Shed the Years is active, this attack is magical, is made at +8 to hit, and deals an extra 5 (1d10) force damage."
  - name: "Sump-Reek Bomb (Recharge 5–6)"
    desc: "Bazzoth hurls a sealed bone flask that bursts into a 20-foot-radius cloud centred on a point he can see within 60 feet. Each creature in that area makes a DC 15 Constitution saving throw, taking 21 (6d6) poison damage on a failure, or half as much on a success. A creature that fails is also poisoned and repeats the save at the end of each of its turns, ending the effect on a success. The cloud lingers and heavily obscures its area until the start of Bazzoth's next turn; a creature that enters it for the first time on a turn, or starts its turn there, is subjected to the save."
bonus_actions:
  - name: Clinging Ichor
    desc: "Bazzoth lobs a flask of sump-glue at a point he can see within 30 feet, coating a 10-foot-radius area that is difficult terrain until the start of his next turn. A creature in the area when it lands, or that enters it for the first time on a turn, must succeed on a DC 15 Strength saving throw or have its speed reduced to 0 until the end of its next turn. He cannot use this the same turn he invokes Shed the Years."
  - name: "Shed the Years"
    desc: "Bazzoth swigs from his gourd and speaks a red-caste rite over his own body, and decades unspool from it. He concentrates to maintain the rite (as if concentrating on a spell); it lasts up to 1 minute. While active: his walking speed increases by 15 feet and his movement no longer provokes opportunity attacks; he gains a +2 bonus to AC and has advantage on Dexterity saving throws; his melee attacks become magical, more accurate, and harder-hitting (see Envenomed Lash); and his Multiattack includes one additional Envenomed Lash. If his concentration is broken, the rite ends."
reactions:
  - name: "Reeking Step (3/Day)"
    desc: "When Bazzoth takes damage, or a creature ends its turn within 5 feet of him, he speaks a short rite and steps through a puff of stinging reek, teleporting to an unoccupied space he can see within 30 feet. This movement does not provoke opportunity attacks."
```

## Connections

- [[vashu-the-weeping-veil|Vashu, the Weeping Veil]]: fellow guardian.
- [[ozvok-the-vermillion-distiller]]: Grung alchemist.
- [[ozzeth-the-twiceborn]]: fellow guardian.
- [[grung-elite-warrior]]: combat reference.
- [[simone-tabarnack]]: related figure.
- [[grung-clans|Grung Clans]]: his faction.
- [[Calveno Sewer Magazines]]: his post.
- [[Grung]]: his people.

## Session Log

**Session 05.** He died in Room 5/Magazine Beta. His death disabled the powder barrels. See `vault/episodes/005/s05-recap.md`.
