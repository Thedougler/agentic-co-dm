---
type: pc-abilities
status: canon
publish: false
aliases: []
summary: "Delmar's traits, features, actions, and feats transcribed from his character sheet."
created: 2026-07-30
updated: 2026-08-08
tags: [stealth]
pc: "delmar-fisk"
pc_level: 5
last_synced: "2026-07-26"
uid: a6ae8d29-8f48-404d-90b1-d150ceeb022f
---

# Delmar Atticus Fisk — Abilities

Built from the player's character sheet. One section per action-economy
slot so a table runner can transclude exactly the one they need mid-round
(`![[delmar-fisk-abilities#Reactions]]`) — an ability that costs an Action
goes under Actions and is named, not repeated, anywhere else.

Everything [[delmar-fisk|Delmar Atticus Fisk]] can do, sorted by what it
costs to do it. He has no spells; his [[rogue|Rogue]] class grants none.

## Traits

Species and background traits (always-on, free to activate).

| Trait | Source | Effect |
|---|---|---|
| Variant Human traits | Species | Extra language, extra skill, bonus feat (spent on Lucky) |

## Features

Class and subclass features that are not themselves an Action, Bonus
Action, or Reaction. These include passives, resource grants, and rest recoveries.

| Feature | Source | Effect | Uses | Recovery |
|---|---|---|---|---|
| Core Rogue Traits | [[rogue\|Rogue]] | Save proficiencies, Expertise (2 skills), Sneak Attack, Thieves' Cant, Weapon Mastery | at will | - |
| Rakish Audacity | [[rogue-swashbuckler\|Swashbuckler]] | Adds CHA mod to initiative; Sneak Attack usable without Advantage if within 5 ft of the target and no other creature within 5 ft of him | at will | - |
| Fancy Footwork | [[rogue-swashbuckler\|Swashbuckler]] | During his turn, a creature he melee-attacks can't make Opportunity Attacks against him for the rest of that turn | at will | - |
| Weapon Mastery | Rogue | [[musket\|Musket]] = Slow (reduce target's Speed 10 ft. on hit, once). [[rapier\|Rapier]] = Vex (Advantage on next attack vs. that target before end of his next turn) `[verify]` neither weapon has its own line in the Actions table below | at will | - |
| Uncanny Dodge | Rogue | Reaction: halve the damage of one attack that hits him. See Reactions | - | - |

## Actions

| Action | To-Hit / DC | Damage / Effect | Uses | Notes |
|---|---|---|---|---|
| Blunderbuss (Exandria) | +8 | 2d8+5 Piercing | at will | [[delmars-blunderbuss\|Delmar's Blunderbuss]]; Firearms, Reload, Misfire, Range 15/60 |
| [[dagger\|Dagger]] (×2) | +8 | 1d4+5 Piercing | at will | Simple, Finesse, Light, Thrown, Nick, Range 20/60 |
| [[pistol\|Pistol]] (×4) | +5 `[verify]` | 1d10+5 Piercing | at will | Martial, Ammunition, Firearms, Range 30/90, Loading (some); 3 lower than the Blunderbuss/Dagger lines' +8 despite sharing DEX +5 + bonus +3. Transcribed as printed, not silently corrected |
| Sneak Attack | - | +3d6 on-hit, once per turn | at will | With a finesse/ranged weapon given Advantage, or (Rakish Audacity) simply while solo next to the target |
| Cunning Strike | - | Forgo Sneak Attack dice for a rider. See the mechanic blocks below | at will | Withdraw option (1d6 dice cost: move up to half Speed, no Opportunity Attacks) has no save |

> [!mechanic]
> **Cunning Strike (Poison).** Forgo 1d6 of Sneak Attack dice: target makes a CON save (DC 16) or becomes [[poisoned|Poisoned]] for 1 minute, repeating the save at the end of each of its turns.

> [!mechanic]
> **Cunning Strike (Trip).** Forgo 1d6 of Sneak Attack dice: target makes a DEX save (DC 16) or falls [[prone|Prone]].

## Bonus Actions

| Bonus Action | Trigger / Cost | Effect | Uses | Recovery |
|---|---|---|---|---|
| Cunning Action | - | Dash, Disengage, or Hide | at will | - |
| Steady Aim | - | Advantage on next attack roll this turn if he hasn't moved; Speed drops to 0 until end of turn | at will | - |

## Reactions

| Reaction | Trigger | Effect | Uses | Recovery |
|---|---|---|---|---|
| Uncanny Dodge | An attacker he can see hits him with an attack roll | Halve the attack's damage against him (round down) | at will | - |
| Firearm Specialist reroll | Misfire on a firearm attack | Reroll the misfire | 1 | Short Rest |

## Feats

| Feat | Source | Effect |
|---|---|---|
| Lucky | Variant Human bonus feat | 3 Luck Points. Spend 1 to grant self Advantage on a d20 Test, or impose Disadvantage on an attack roll against him. Recharges on a Long Rest |
| Tavern Brawler | - | Enhanced Unarmed Strike (1d4 + STR bludgeoning), reroll a 1 on an Unarmed Strike damage die, mastery with improvised weapons, Push 5 ft. on an Unarmed Strike hit |
| Firearm Specialist | - | Firearms training; the misfire reroll and bonus-action reload above are its Reaction/Action-economy expressions |

[[ability-score-improvement|Ability Score Improvement]] from the Sailor background (+2 DEX/+1 CHA) is the
source of the DEX 20 / CHA 15 spread instead of a flat +2. See
[[delmar-fisk-stats]].
