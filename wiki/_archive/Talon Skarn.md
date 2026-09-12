---
type: npc
campaign: shattered-sea
status: alive
role: rival
location: Midchain
faction: Countless
visibility: dm
tags: [npc, countless, schism]
summary: Countless peregrine apprentice and CR 13 flying skirmisher; his stoop-and-chain combat kit supports the Rule of Two rivalry with Talon Vantyrus.
---
# Talon Skarn

![[attachments/shattered-sea/character-references/talon-skarn-reference-sheet.jpg|Talon Skarn character reference sheet]]

````col
```col-md
flexGrow=2
===
## At a Glance

| **Role**      | Countless apprentice and CR `13` flying skirmisher                    |
| ------------- | ---------------------------------------------------------------------- |
| **Nature**    | Living expression of the [[Rule of Two]]                               |
| **Home**      | Midchain                                                               |
| **Wants**     | To kill [[Talon Vantyrus]] under Countless doctrine                    |
| **Arrival**   | Enters only when the party physically reaches Midchain                |
| **Fight**     | Pursues the current job; he does not stay for a duel to `0` hit points |
| **Kit**       | Katana, two sai, and two kusarigama                                    |
| **Signature** | A `30-foot` stoop, `20-foot` chain reach, and forced movement           |
| **Weakness**  | No damage resistances; ground him, deny the stoop lane, and spread out |

> **DM thesis:** Skarn is Vantyrus's standing threat made flesh. He is trying to kill his master because the [[Rule of Two]] demands it, not because he has abandoned Countless.
```

```col-md
flexGrow=1
===
> [!narration] Talon Skarn
> A broad peregrine aarakocra stands about five feet tall, heavy wings lifted behind a dark robe. Pale chest feathers climb into a black-and-cream face; red-orange crown feathers flare above steady amber-gold eyes and a yellow beak tipped in black. The robe hangs in dark layers over wrapped ankles and bare talons, with patterned trim catching along the collar and down the front.
>
> Cloth wraps and loose metal chains cover his forearms. One hand holds a long straight sword, the other a curved hook-blade on a dangling chain. When he shifts his grip, the chain links click once and settle against the wraps.
```
````

## Running Talon Skarn

````col
```col-md
flexGrow=1
===
### Opening

Wings lift and chains click. If Skarn has a `30-foot` straight-down lane, open with **Peregrine Dive**. Otherwise, use **Kusarigama** to set the distance.

### Default turn

Use **Stunning Strike** once on his turn. Follow with **Kusarigama** to pull a target clear of its partner, or **Sai** to blunt the watcher's next attack.

### Legendary actions

After another creature's turn, use **Chain Snap** to reopen a pull, **Crossing Sai** to punish a watcher, or **Wingbeat Step** to change the lane. Use each option at most once before Skarn's next turn.

### Stoop lane

**Peregrine Dive** needs `30 feet` of straight-down movement. Use it from a roof-break, terrace, or open sky. A tight aisle under leaves is chain work, not a stoop.
```

```col-md
flexGrow=1
===
### If pressured

Use **Step of the Falcon** to Disengage, **Wingbeat Step** to change the lane, and **Deflect Attack** on the first solid hit. At `97` hit points or fewer, finish the current job if he can; otherwise, leave.

### Target priority

Take the object if one is at stake. Otherwise, attack the creature blocking the job, then the carrier, then anyone between Skarn and it. He cuts gear before throats.

### Counterplay

Ground him with Grapple or Restrain, or deny a `30-foot` straight-down lane. Beat the **Constitution save — `DC 18`** to avoid **Stunning Strike**. His AC is `19` and he has no damage resistances. Spread out against **Kusarigama Tempest**, deny clean pulls, or make him spend movement.

### Kusarigama Tempest

Use **Kusarigama Tempest** when two or more creatures are inside its `20-foot` Emanation and a pull or **Prone** condition changes the fight. On a failed save, choose pull or **Prone** for each creature; on a success, deal damage only.
```
````

### Difficulty knobs

- **Easier.** Remove **Legendary Resistance** and start **Kusarigama Tempest** uncharged.
- **Harder.** Start him in the air with a stoop lane without raising his AC.

# Combat

> **Encounter rule:** Use this block whenever [[Talon Skarn]] fights. His win condition is the current job, not a duel to 0 hit points. On [[Session-11-09-Theft-on-the-Watch]], that job is the [[Fate Spinner]] and a break down the star-cut.

## Statblock

```statblock
layout: Basic 5e Layout
dice: true
columns: 2
forceColumns: true
name: Talon Skarn
size: Medium
type: humanoid
subtype: aarakocra
alignment: lawful neutral
ac: 19
hp: 195
hit_dice: "23d8 + 92"
speed: "50 ft., fly 90 ft."
stats: [14, 22, 18, 12, 20, 14]
saves:
  - Dex: +11
  - Con: +9
  - Wis: +10
skillsaves:
  - Acrobatics: +16
  - Insight: +10
  - Perception: +10
  - Stealth: +11
senses: "passive Perception 20"
languages: "Auran, Common"
cr: 13
traits:
  - name: Evasion
    desc: "When Talon is subjected to an effect that allows him to make a Dexterity saving throw to take only half damage, he instead takes no damage on a successful save and half damage on a failed save. He can't use this trait while Incapacitated."
  - name: Legendary Resistance (3/Day)
    desc: "If Talon fails a saving throw, he can choose to succeed instead."
  - name: Skyhunter
    desc: "Opportunity Attacks against Talon have Disadvantage while he is flying."
  - name: Peregrine Dive
    desc: "If Talon flies at least 30 feet downward in a straight line immediately before hitting a creature with his Katana, the attack deals an extra 13 (3d8) Slashing damage, and the target must succeed on a DC 18 Strength saving throw or have the Prone condition. Talon can deal this extra damage only once per turn."
  - name: Stunning Strike (1/Turn)
    desc: "Immediately after Talon hits a creature with a melee attack during his turn, he can force it to make a DC 18 Constitution saving throw. On a failed save, the creature has the Stunned condition until the start of Talon's next turn. On a successful save, its Speed is halved until then, and the next attack roll made against it before then has Advantage."
actions:
  - name: Multiattack
    desc: "Talon makes three attacks, using Katana, Kusarigama, or Sai in any combination."
  - name: Katana
    desc: "Melee Attack Roll: +11, reach 5 ft., one target. Hit: 17 (2d10 + 6) Slashing damage."
  - name: Kusarigama
    desc: "Melee Attack Roll: +11, reach 20 ft., one target. Hit: 15 (2d8 + 6) Slashing damage. If the target is Large or smaller, Talon can pull it up to 10 feet toward himself."
  - name: Sai
    desc: "Melee Attack Roll: +11, reach 5 ft., one target. Hit: 13 (2d6 + 6) Piercing damage, and the target has Disadvantage on the next attack roll it makes before the start of Talon's next turn."
  - name: Kusarigama Tempest (Recharge 5-6)
    desc: "Talon whirls both chained sickles around himself. Each creature of his choice in a 20-foot Emanation must make a DC 19 Dexterity saving throw. Failure: 27 (6d8) Slashing damage, and Talon either pulls the creature up to 15 feet toward himself or gives it the Prone condition. Success: Half damage only."
bonus_actions:
  - name: Step of the Falcon
    desc: "Talon takes the Dash or Disengage action."
reactions:
  - name: Deflect Attack
    desc: "Trigger: Talon is hit by an attack roll. Response: Talon reduces the attack's damage to himself by 18 (2d10 + 7). If this reduces the damage to 0, Talon can immediately move up to 10 feet without provoking Opportunity Attacks."
legendary_actions:
  - name: ""
    desc: "Legendary Action Uses: 3. Immediately after another creature's turn, Talon can expend one use to take one of the following actions. He regains all expended uses at the start of his turn."
  - name: Chain Snap
    desc: "Talon makes one Kusarigama attack. He can't use Chain Snap again until the start of his next turn."
  - name: Crossing Sai
    desc: "Talon makes one Sai attack. He can't use Crossing Sai again until the start of his next turn."
  - name: Wingbeat Step
    desc: "Talon moves up to half his Speed without provoking Opportunity Attacks. He can't use Wingbeat Step again until the start of his next turn."
```

## Alt Art

![[attachments/shattered-sea/portraits/talon-skarn-portrait.jpg|Talon Skarn portrait]]
![[artifacts/tokens/talon-skarn-token.png|Talon Skarn FoundryVTT token]]
