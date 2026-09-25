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
tier: supporting
created: 2026-09-13T03:04:18Z
updated: 2026-09-13
type: npc
reveal: revealed
campaign: shattered-sea
visibility: dm
status: alive
role: "Hound of Tyr"
location: "[[blackrule]]"
faction: "[[dravosi-crown]]"
relationships:
  - target: "[[khlysty-the-flock]]"
    type: related_to
  - target: "[[dravosi-crown]]"
    type: related_to
  - target: "[[tyr]]"
    type: related_to
  - target: "[[shepherd-grigori]]"
    type: related_to
  - target: "[[blackrule]]"
    type: related_to
---
# Aleksander Malone

````col
```col-md
flexGrow=2
===
## At a Glance

| **Role**   | Rival; Hound of [[tyr]] |
| ---------- | ------------------------ |
| **Nature** | Reserved Crown hunter who treats confirmed heresy as righteous judgment. |
| **Home**   | [[blackrule]], a chapterhouse cut into volcanic terrace-rock in the southern [[Midchain]] |
| **Wants**  | To hunt confirmed [[khlysty-the-flock|Flock]] infiltration and deliver judgment. |
| **Leverage** | The Crown reserves him for confirmed heresy, and his release at [[sarns-landing]] changed Crown policy. |
| **Limit**  | He is a hunter, not a negotiator; the Crown's formal confirmation rule is the leash on his violence. |

> **DM thesis:** Aleksander is a patient, righteous Crown weapon whose grim joy becomes visible only when someone gives him a confirmed heretic to judge.
```

```col-md
flexGrow=1
===
> [!narration] Aleksander Malone
> Tall and spare, a High Elf in a Crown-service coat that has been through worse than tailoring can hide. The wool carries salt and something older. Seams gone pale at the shoulders, patched at the elbows with leather that matches nothing else on him. His hands are steady and unused to stillness, resting open at his sides the way a man's do when he expects to need them.
>
> Before he speaks again, fingers touch his lips. Quick as a blessing. His eyes have already finished with whoever he is looking at.
```
````

## Running Aleksander Malone

````col
```col-md
flexGrow=1
===
### First meeting

When heresy is confirmed, Malone arrives as a Crown hunter, not a negotiator. He trains at [[blackrule]] and leaves only when confirmation reaches him. On [[hcs-ordinance]], he hunted [[shepherd-grigori]] while the cutter stood under merchant cover.

> *Malone*: “The Crown has confirmed the heresy.”
```

```col-md
flexGrow=1
===
### When posture changes

Malone treats violence as righteous judgment and takes grim joy in it rather than reluctance. He was once loosed in public at [[sarns-landing]]; the result was ugly enough that Crown policy now requires formal confirmation before he is released. The Crown once assigned him a handler, and that handler did not survive contact.

He remains calm while assessing a confirmed target. Threaten [[shepherd-grigori]] or another protected Heir-like asset and something old and cold surfaces; he has waited long enough to remember how to move without haste.
```
````

## Voice

Malone speaks in clipped, formal sentences with the finality of a judgment. He avoids negotiation and names heresy as a settled category once the Crown confirms it.

**The ask:** *“State your name and your allegiance.”*

**The refusal:** *“There is nothing to negotiate.”*

**Under pressure:** *“The Crown confirmed the heresy. Judgment follows.”*

## Connections

| Connection | Meaning |
| ---------- | ------- |
| [[dravosi-crown]] | Employer and leash; the Crown reserves him for confirmed Flock infiltration. |
| [[tyr]] | Patron named on the scales at [[blackrule]]. |
| [[khlysty-the-flock]] | Hunt target pattern. |
| [[shepherd-grigori]] | Target he hunted aboard [[hcs-ordinance]]. |
| [[corbin-knighton]] | Recent boarding companion aboard the cutter. |
| [[blackrule]] | Chapterhouse he chose in the southern [[Midchain]]. |
| [[sarns-landing]] | Public release that changed Crown policy. |
| Ashglass, Hollow Choir, and Corrigan's Rest | Named places the source says do not overlap [[blackrule]]; no owner page is currently filed for Hollow Choir. |
**Combat.**

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

