---
type: npc
status: pending
publish: false
aliases: []
created: "2026-08-06"
updated: "2026-08-10"
tags: [faith, war, recurring]
summary: "Aleksander Malone, the Dravosi Crown's heresy-only reserve, has already decided to kill Shepherd Grigori himself, Crown confirmation or not."
owner_skill: ".claude/skills/draft-content/references/npc.md"
subtype: recurring
location: "[[blackrule|Blackrule]]"
role: [villain, recurring]
has_active_front: true
campaigns: [Shattered Sea]
reference_image: ""
voice_id: ""
voice: ""
voice_actor: ""
uid: ddf2cf78-b624-493e-a38f-6b54c81fa1b2
---

# Aleksander Malone

**Wants:** to kill [[shepherd-grigori|Shepherd Grigori]]. The Shepherd's healings read to him exactly as the shepherd of mercy he answered at [[sarns-landing|Sarn's Landing]]. He means to deliver the same judgment, and he will enjoy it.

![[aleksander-malone-narration-appearance]]

## Stats & Combat

```statblock
layout: Basic 5e Layout
name: Aleksander Malone
size: Medium
type: humanoid (elf)
alignment: lawful neutral
ac: "18 (half plate, blessed)"
hp: 195
hit_dice: "26d8 + 78"
speed: "30 ft."
stats: [20, 14, 16, 12, 20, 13]
saves:
  - Con: +7
  - Wis: +9
skillsaves:
  - Insight: +9
  - Perception: +9
  - Religion: +5
  - Stealth: +6
condition_immunities: "charmed, frightened"
senses: "passive Perception 19"
languages: "Common, Elvish"
cr: 14
traits:
  - name: "Regeneration"
    desc: "[HB] Malone regains 20 hit points at the start of his turn. If Malone takes necrotic damage, this trait doesn't function at the start of his next turn. Malone dies only if he starts his turn with 0 hit points and doesn't regenerate."
  - name: "Heretic's Bane"
    desc: "[HB] Malone has advantage on saving throws against spells and abilities used by fiends and undead. When he hits a fiend or undead with a weapon attack, the attack deals an extra 4 (1d8) radiant damage."
  - name: "Sneak Attack (1/Turn)"
    desc: "[RAW] Malone deals an extra 7 (2d6) damage when he hits a target with a weapon attack and has advantage on the attack roll, or when another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and Malone doesn't have disadvantage on the attack roll."
  - name: "Spellcasting"
    desc: "[RAW] Malone is a 7th-level spellcaster. His spellcasting ability is Wisdom (spell save DC 17, +9 to hit with spell attacks). He has the following cleric spells prepared.\n\nAt will: *Guidance*, *Sacred Flame* (3d8), *Thaumaturgy*\n\n2/Day each: *Bless*, *Command*, *Hold Person*\n\n1/Day each: *Dispel Magic*, *Banishment*"
actions:
  - name: "Multiattack"
    desc: "Malone makes three attacks: any combination of blessed longsword and blessed bayonet attacks."
  - name: "Blessed Longsword"
    desc: "Melee Weapon Attack: +9 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage plus 9 (2d8) radiant damage."
  - name: "Blessed Bayonet"
    desc: "Ranged Weapon Attack: +9 to hit, range 20/60 ft., one target. Hit: 7 (1d4 + 5) piercing damage plus 9 (2d8) radiant damage."
  - name: "Bayonet Barrage (Recharge 5–6)"
    desc: "[HB] Malone hurls a fan of blessed bayonets in a 30-foot cone. Each creature in that area must make a DC 17 Dexterity saving throw, taking 28 (8d6) radiant damage on a failed save, or half as much damage on a successful one."
bonus_actions:
  - name: "Action Surge (1/Short Rest)"
    desc: "[RAW] Malone can take one additional action on his turn, in addition to his regular action and a possible bonus action."
  - name: "Spiritual Weapon (2/Day)"
    desc: "[RAW] Malone conjures a spectral mace within 60 feet. For 1 minute, as a bonus action on each of his turns, he can move the weapon up to 20 feet and make a melee spell attack (+9 to hit) against a creature within 5 feet of it, dealing 14 (2d8 + 5) force damage on a hit."
  - name: "Channel Divinity: Rebuke the Unclean (1/Short Rest)"
    desc: "[HB] Each fiend and undead within 30 feet of Malone must succeed on a DC 17 Wisdom saving throw or be turned for 1 minute. A turned creature must spend its turns moving as far away from Malone as possible and cannot take reactions. It can only Dash or try to escape effects preventing movement. A fiend or undead of CR 2 or lower that fails is destroyed instead."
reactions:
  - name: "Guided Judgment (2/Short Rest)"
    desc: "[HB] Immediately after missing with an attack roll, Malone can reroll the die and must use the new roll."
  - name: "Withdraw by Judgment (1/Day)"
    desc: "[HB] **Trigger:** Malone is reduced below 49 hit points (one-quarter of his maximum). **Effect:** Malone can teleport up to 30 feet to an unoccupied space he can see, without provoking opportunity attacks, and does not return to the fight this encounter."
```

A CR 14 exorcist hybrid. Regenerates 20/turn, shuts off only on necrotic. The party must solve that problem or he simply will not die.

Below a quarter HP he withdraws to [[blackrule|Blackrule]] and does not return this fight. He hunts again on his own authority, whenever he chooses. Bayonet Barrage covers the approach. Blessed attacks close the kill. Against fiends and undead, every swing bites deeper. [[banishment|*Banishment*]] is his opener against any fiend. Guided Judgment fires twice. High AC alone will not stall him. Once per combat he speaks free of turn cost: *"[[tyr|Tyr]] weighs the guilty and I am his warhammer."*

## Voice

Hard Irish Catholic zealot. Tyr's law weaponized as operational language. Threat delivery. He quotes divine precepts as targeting data. Every sentence carries the cadence of a life spent reading one law and finding every answer in it. Fingers touch his lips before speaking, quick as a blessing.

He pronounces. He does not ask. He does not soften or doubt or negotiate. Grim joy, absolute conviction. He enjoys the work because the work is righteous.

> *"[[tyr|Tyr]] weighs the guilty and I am his warhammer. His seal is on every warrant I carry. Sin has mass, and yours has pulled something to your door that is worse than me. Confess now and the scales tip to mercy. Refuse and I break you with a rod of iron. Be wise. Kneel before his court finds you standing. This can be over with one swing of my sword."*

## Relationships

- [[dravosi-crown|Dravosi Crown]]: held in reserve for confirmed heresy, a lesson the Crown learned at Sarn's Landing when his zealotry finished the job and kept going. The Crown tried assigning a handler. The handler did not survive contact. Nobody signs his orders once the leash slips. *"Their dog needs a long leash, and a handler will only get bit."*
- [[blackrule|Blackrule]]: the chapterhouse he chose himself, carved into volcanic terrace-rock in the [[midchain-south|Southern Midchain]]. Genuine disdain for civilized excess, not exile. He calls it home when he is there at all. *"Tyr's court needs no walls. The guilty find me wherever I pray."*
- [[shepherd-grigori|Shepherd Grigori]]: the undead [[hierarch|Hierarch]] Malone is already hunting. He fears killing someone he was wrong about more than he fears failing to act. *"Confess and I will be swift,"* he tells every suspect, and thanks the guilty for their honesty afterward.
- [[tyr|Tyr]]: the god he serves without a flicker of doubt. His oath, older than Blackrule: *"Tyr grants mercy to those who confess. I grant the rest to him."*
- [[sarns-landing|Sarn's Landing]]: the incident that got him leashed. He executed the shepherd within the hour, then executed fourteen confessing villagers. He believed the rest innocent. The Crown learned the cost of pointing him at something.

## Goals & Fronts

### Front: The Hound of God

**Lifecycle:** active
**Aim:** find [[shepherd-grigori|Grigori]] and kill him, the same judgment he delivered at [[sarns-landing|Sarn's Landing]], on his own authority and without waiting for Crown confirmation.
**Approach:** prays audibly and reads the crowd for who flinches at [[tyr|Tyr]]'s name. Offers confession before the blade as a mercy, then kills without hesitation once a suspect confesses or refuses. *"I will break them with a rod of iron."*
**Off-screen move if unopposed:** works Grigori's known trail (the noble courts he has healed in) backward one household at a time, closing distance with grim certainty. Each household confirms a piece. He states what he has learned aloud, as fact, not as question.
**Trigger conditions:**

- Each court, servant, or noble household Malone tracks down that confirms a Grigori visit advances the hunt.
**Clock:** 4 segments (fast-moving), filled: 0
**Consequence at fill:** Malone reaches Grigori and kills him. The crew learns of it after, if they learn of it at all.
**Possible outcomes (2-3):** the crew reaches Grigori first and the confrontation plays on their terms. The crew's path crosses Malone's mid-hunt, for or against each other depending on what he reads in them. Or Malone corners Grigori alone off-screen.
**PC connection:** [[perrin-black-jaw|Perrin Black-Jaw]] failed the Arcana check identifying Grigori's necrotic magic in Session 03 and holds a lead into the same trail Malone is already walking.
**Quest link:** none yet.
