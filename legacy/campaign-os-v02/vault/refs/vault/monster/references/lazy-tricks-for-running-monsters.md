---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [combat]
summary: "Quick-math monster statistics by CR, ten reusable monster features, a dice-average lookup table, and other fast tricks for running monsters at the table."
tier: supporting
source: "raw/2026-07/05 - Lazy Tricks for Running Monsters.md"
source_url: ""
uid: af4575c5-0172-409e-a5fe-547d39008fb3
---

# Lazy Tricks for Running Monsters (5e Monster Builder)

Tricks and tips for more easily preparing and running monsters during play. These are called "lazy tricks" not because they're about cheating or doing less work overall, but because they're meant to let you quickly accomplish things when your game is in progress and you don't have a lot of extra time.

## Quick Monster Statistics

An even quicker set of monster statistics than the "Building a Quick Monster" guidelines (a source elsewhere in this document that this page does not itself contain).

First, choose a challenge rating for the monster, based on its perceived power in the encounter. When needed, compare the monster to existing monsters to find a suitable challenge rating. Then use the following guidelines to craft its baseline statistics:

* Armor Class = 12 + 1/2 CR
* Hit points = (15 × CR) + 15
* Proficient saving throws and skills = 4 + 1/2 CR
* Nonproficient saving throws and abilities = −2 to +2, based on the monster's story
* Attack bonus = 4 + 1/2 CR
* DC for saving throws = 12 + 1/2 CR
* Total damage per round = (7 × CR) + 5

Start the monster out with one attack, then add one additional attack at CR 2, CR 7, CR 11, and CR 15. Split the total damage noted above across all attacks.

With a solid set of combat statistics at hand, use narrative descriptions to make the monster unique, interesting, and evocative.

## Ten Useful Monster Features

Give any custom monster impactful features and attacks that make sense for their place in the game. When a monster feature deals damage, choose a damage type appropriate to the creature's physiology, theme, or story. A creature channeling magical power might deal acid, cold, fire, lightning, force, poison, psychic, necrotic, radiant, or thunder damage. A creature making use of spines, spikes, or projectiles might deal bludgeoning, piercing, or slashing damage.

**Damaging Blast.** This creature has one or more single-target ranged attacks using the attack bonus and damage calculated above, and which deal damage of an appropriate type.

**Damage Reflection.** Whenever a creature within 5 feet of this creature hits them with a melee attack, the attacker takes damage in return of a type appropriate to the creature. The damage dealt is equal to half the damage of one of this creature's attacks. If you give a creature this feature, give them one less attack than normal.

**[[misty-step|Misty Step]].** As a bonus action, this creature can teleport up to 30 feet to an unoccupied space they can see.

**Knockdown.** When this creature hits a target with a melee attack, the target must succeed on a [[strength|Strength]] saving throw or be knocked prone.

**Restraining Grab.** When this creature hits a target with a melee attack, the target is grappled (escape DC based on this creature's Strength or [[dexterity|Dexterity]] modifier). While grappled, the target is restrained.

**Damaging Burst.** As an action, this creature can create a burst of energy, magic, spines, or some other effect in a 10-foot-radius sphere, either around themself or at a point within 120 feet. Each creature in that area must make a Dexterity, [[constitution|Constitution]], or [[wisdom|Wisdom]] saving throw (your choice, based on the type of burst). On a failure, a target takes damage of an appropriate type equal to half this creature's total damage per round. On a success, a target takes half as much damage.

**Cunning Action.** On each of their turns, this creature can use a bonus action to take the Dash, Disengage, or Hide action.

**Damaging Aura.** Each creature who starts their turn within 10 feet of this creature takes damage of a type appropriate to the creature. The damage dealt is equal to half the damage of one of this creature's attacks. If you give a creature this feature, give them one less attack than normal.

**Energy Weapons.** The creature's weapon attacks deal extra damage of an appropriate type. You can add this damage on top of the creature's regular damage output to give them a combat boost, or you can replace some of the creature's normal weapon damage with this energy damage.

**Damage Transference.** When this creature takes damage, they can transfer half or all of that damage (your choice) to a willing creature within 30 or 60 feet of them. This feature is particularly good for boss monsters.

## Using Averages

By default, 5e monster stat blocks calculate the average damage for any attack's dice expression, as with "13 (2d8 + 4) bludgeoning damage" for an ogre's [[greatclub|Greatclub]] attack. Using average damage for a monster's attacks is one of the best ways to speed up combat.

Sometimes, though, you need to roll damage for effects that aren't in a stat block. When you do, use the following table to quickly look up the average value of various dice equations. Find the number of dice in the leftmost column, then go across to the appropriate die type. You can add up averages to get an average value for higher numbers of dice — for example, adding the average of 2d10 and 6d10 to get the average of 8d10. Use this approach to find the average for rolling more than twelve dice, so that if you need an average for 24d10, you can simply look at the 12d10 average and double it.

| # of dice | d4 | d6 | d8 | d10 | d12 |
| --------- | -- | -- | -- | --- | --- |
| 1         | 2  | 3  | 4  | 5   | 6   |
| 2         | 5  | 7  | 9  | 11  | 13  |
| 3         | 7  | 10 | 13 | 16  | 19  |
| 4         | 10 | 14 | 18 | 22  | 26  |
| 5         | 12 | 17 | 22 | 27  | 32  |
| 6         | 15 | 21 | 27 | 33  | 39  |
| 7         | 17 | 24 | 31 | 38  | 45  |
| 8         | 20 | 28 | 36 | 44  | 52  |
| 9         | 22 | 31 | 40 | 49  | 58  |
| 10        | 25 | 35 | 45 | 55  | 65  |
| 11        | 27 | 38 | 49 | 60  | 71  |
| 12        | 30 | 42 | 54 | 66  | 78  |

You can also compute averages for dice expressions with simple equations you can keep in your head. The average of two dice is the maximum value of one of those dice + 1, so that the average of 2d12 is 13. Then double that number for multiples of two, so that the average of 2d8 is 9, the average of 4d8 is 18, and so forth. Likewise, the average of a single die is half the size of the die, so add that number to a two-dice average to get odd numbers. For example, the average of 4d6 is 14, so the average of 5d6 is 17. (The average of one die is actually half the size of the die plus 0.5, which is why the average of two dice is the maximum value of the die + 1.)

## Other Lazy Monster Tricks

Once you're in the middle of an encounter, make use of a number of other quick tricks to make running monsters easier, with more flexibility and greater speed. Try any of the following options at your table, and make use of any trick that helps your game:

* Use passive monster initiative (vault/refs/quick-tricks-for-lazier-5e-games.md § Passive Monster Initiative). Even faster? Just have all monsters act on initiative count 12.
* Turn the HP, damage, and attack-count dials on the fly to speed a fight up or slow it down, and pull the number-of-monsters dial (fleeing, reinforcing, or breaking on a controller's death) for the same reason (vault/refs/vault/monster/references/difficulty-dials.md).
* Include creatures designed to eat "save or suck" attacks such as *banishment* or *polymorph*.
