---
title: Aleksander Malone
aliases:
  - Aleksander Malone
category: entities
tags: [shattered-sea, npc]
sources:
  - "campaign-os:aleksander-malone-narration-appearance.md"
  - "Khlysty - the Flock.md"
  - "legacy: /Users/nick/shattered-sea/wiki/shattered-sea/kill-the-shepherd/npc.aleksander-malone.md"
  - "aleksander-malone.md"
summary: "Hound of Tyr reserved by the Crown for confirmed Flock infiltration; CR 14 elf hunter with a blessed fight sheet."
provenance:
  extracted: 0.95
  inferred: 0.05
  ambiguous: 0.0
base_confidence: 0.50
lifecycle: proposed
lifecycle_changed: "2026-09-13"
tier: supporting
created: 2026-09-13T03:04:18Z
updated: 2026-09-13
type: npc
reveal: unrevealed
campaign: shattered-sea
visibility: dm
status: alive
role: "Hound of Tyr"
faction: "[[dravosi-crown]]"
relationships:
  - target: "[[khlysty-the-flock]]"
    type: related_to
  - target: "[[dravosi-crown]]"
    type: related_to
  - target: "[[Tyr]]"
    type: related_to
  - target: "[[shepherd-grigori]]"
    type: related_to
  - target: "[[Blackrule]]"
    type: related_to
---
# Aleksander Malone

## Who and want

[[aleksander-malone]] is the [[dravosi-crown]]'s Hound of [[Tyr]]. The Crown reserves him for confirmed [[khlysty-the-flock]] infiltration. He trains at [[Blackrule]] and leaves only when heresy is confirmed. Word of confirmed heresy reaches him and he goes on his own judgment; the Crown once assigned a handler, and that handler did not survive contact. Crown talk names him a dog that needs a long leash. He was aboard [[hcs-ordinance]] under [[corbin-knighton]] while hunting [[shepherd-grigori]]. His signature line is: "May God have mercy on my enemies, for they shall have none from me."

## Look

Source is silent beyond half plate and blessed weapons on the fight sheet. Medium elf humanoid; half plate AC 18; blessed longsword and bayonets.

## First minutes and posture

When heresy is confirmed, Malone arrives as a Crown hunter, not a negotiator. He treats the violence as righteous judgment and takes grim joy in it rather than reluctance. At [[sarns-landing]] he was once loosed in public; the result was ugly enough that Crown policy now requires formal heresy confirmation before he is released. On [[hcs-ordinance]], he hunted Grigori while the cutter stood under merchant cover.

## Named ties

- [[dravosi-crown]] — employer and leash.
- [[Tyr]] — scales cut into the altar stone at [[Blackrule]].
- [[khlysty-the-flock]] / [[shepherd-grigori]] — the hunt target pattern.
- [[corbin-knighton]] / [[hcs-ordinance]] — recent boarding companion.
- [[Blackrule]] — chapterhouse he chose himself, cut into volcanic terrace-rock in the southern [[Midchain]], from disdain for civilized excess rather than exile.
- [[sarns-landing]] — public release that changed Crown policy.
- [[Ashglass]], [[hollow-choir]], and [[corrigans-rest]] — named places the source says do not overlap [[Blackrule]].

## Combat

CR 14. Regeneration 20, Heretic's Bane against fiends and undead, Sneak Attack, 7th-level Wisdom spellcasting (DC 17), Multiattack with blessed longsword and bayonet, Bayonet Barrage cone, Action Surge, Spiritual Weapon, Rebuke the Unclean, Guided Judgment, and Withdraw by Judgment when reduced below 49 hit points. A later idea note asks for no invented supernatural resilience; the live sheet is kept. ^[ambiguous]

```statblock
layout: Basic 5e Layout
name: "Aleksander Malone"
size: Medium
type: humanoid (elf)
alignment: "Lawful Neutral"
ac: "18 (half plate, blessed)"
hp: 195
hit_dice: "26d8 + 78"
speed: "30 ft."
stats: [20, 14, 16, 12, 20, 13]
saves:
  - con: 7
  - wis: 9
skillsaves:
  - insight: 9
  - perception: 9
  - religion: 5
  - stealth: 6
condition_immunities: "Charmed, Frightened"
senses: "Passive Perception 19"
languages: "Common, Elvish"
cr: 14
traits:
  - name: "Regeneration"
    desc: "Malone regains 20 hit points at the start of his turn. If Malone takes necrotic damage, this trait doesn't function at the start of his next turn. Malone dies only if he starts his turn with 0 hit points and doesn't regenerate."
  - name: "Heretic's Bane"
    desc: "Malone has advantage on saving throws against spells and abilities used by fiends and undead. When he hits a fiend or undead with a weapon attack, the attack deals an extra 4 (1d8) radiant damage."
  - name: "Sneak Attack (1/Turn)"
    desc: "Malone deals an extra 7 (2d6) damage when he hits a target with a weapon attack and has advantage on the attack roll, or when another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and Malone doesn't have disadvantage on the attack roll."
  - name: "Spellcasting"
    desc: "Malone is a 7th-level spellcaster. His spellcasting ability is Wisdom (spell save DC 17, +9 to hit with spell attacks). At will: Guidance, Sacred Flame (3d8), Thaumaturgy. 2/day each: Bless, Command, Hold Person. 1/day each: Dispel Magic, Banishment."
actions:
  - name: "Multiattack"
    desc: "Malone makes three attacks: any combination of blessed longsword and blessed bayonet attacks."
  - name: "Blessed Longsword"
    desc: "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage plus 9 (2d8) radiant damage."
  - name: "Blessed Bayonet"
    desc: "Ranged Weapon Attack: +9 to hit, range 20/60 ft., one target. Hit: 7 (1d4 + 5) piercing damage plus 9 (2d8) radiant damage."
  - name: "Bayonet Barrage (Recharge 5–6)"
    desc: "Malone hurls a fan of blessed bayonets in a 30-foot cone. Each creature in that area must make a DC 17 Dexterity saving throw, taking 28 (8d6) radiant damage on a failed save, or half as much damage on a successful one."
bonus_actions:
  - name: "Action Surge (1/Short Rest)"
    desc: "Malone can take one additional action on his turn, in addition to his regular action and a possible bonus action."
  - name: "Spiritual Weapon (2/Day)"
    desc: "Malone conjures a spectral mace within 60 feet. For 1 minute, as a bonus action on each of his turns, he can move the weapon up to 20 feet and make a melee spell attack (+9 to hit) against a creature within 5 feet of it, dealing 14 (2d8 + 5) force damage on a hit."
  - name: "Channel Divinity: Rebuke the Unclean (1/Short Rest)"
    desc: "Each fiend and undead within 30 feet of Malone must succeed on a DC 17 Wisdom saving throw or be turned for 1 minute. A turned creature must spend its turns moving as far away from Malone as possible and cannot take reactions. It can only Dash or try to escape effects preventing movement. A fiend or undead of CR 2 or lower that fails is destroyed instead."
reactions:
  - name: "Guided Judgment (2/Short Rest)"
    desc: "Immediately after missing with an attack roll, Malone can reroll the die and must use the new roll."
  - name: "Withdraw by Judgment (1/Day)"
    desc: "When Malone is reduced below 49 hit points, he can teleport up to 30 feet to an unoccupied space he can see without provoking opportunity attacks, and does not return to the fight this encounter."
```

## Connections

- [[dravosi-crown]]
- [[khlysty-the-flock]]
- [[shepherd-grigori]]
- [[Tyr]]
- [[Blackrule]]
- [[hcs-ordinance]]
- [[corbin-knighton]]

## Narration

> [!narration]
> *Tall and spare, a High Elf in a Crown-service coat that has been through worse than tailoring can hide. The wool carries salt and something older. Seams gone pale at the shoulders, patched at the elbows with leather that matches nothing else on him. His hands are steady and unused to stillness, resting open at his sides the way a man's do when he expects to need them.*
>
> *Before he speaks again, fingers touch his lips. Quick as a blessing. His eyes have already finished with whoever he is looking at.*
