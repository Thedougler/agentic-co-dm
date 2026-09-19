# Combat

> **Encounter rule:** Select Captain Reeves's statblock based on his tactical position and crew support. Damage to his body alone never changes forms. His position shifts when the party separates him from his crew or when he activates the cursed blade as a final act of desperation.

## Deck Lord Form

**Use when:** Reeves commands from the quarterdeck, bridge, or captain's quarters with access to crew and crew reinforcements. He has room to maneuver and allies within shouting distance.

```statblock
layout: Basic 5e Layout
name: "Captain Darius Reeves (Deck Lord)"
size: Medium
type: humanoid
alignment: "chaotic neutral"
ac: 17
hp: 110
hit_dice: "13d8 + 52"
speed: "30 ft."
stats: [18, 16, 18, 15, 14, 17]
saves:
  - dexterity: 6
  - constitution: 7
  - charisma: 6
skillsaves:
  - acrobatics: 6
  - deception: 6
  - insight: 4
  - perception: 4
  - persuasion: 6
damage_resistances: "none"
condition_immunities: "none"
senses: "passive Perception 14"
languages: "Common, Thieves' Cant"
cr: "6"
traits:
  - name: "Fleet Tactics"
    desc: "As a bonus action, Reeves can command up to three allied creatures he can see within 60 feet that can hear him. One of them can use its reaction immediately to move up to half its speed or take the Dodge action."
  - name: "Parry"
    desc: "Reeves adds 4 to his AC against one weapon attack within reach, provided he can see the attacker and is holding his scimitar."
  - name: "Cunning Action"
    desc: "On each of his turns, Reeves can use a bonus action to take the Dash, Disengage, or Hide action."
actions:
  - name: "Multiattack"
    desc: "Reeves makes two Scimitar attacks or two Pistol attacks, or uses Command Crew twice."
  - name: "Scimitar"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) slashing damage. If the target is a creature, Reeves can push it up to 5 feet away as a bonus effect."
  - name: "Pistol"
    desc: "Ranged Weapon Attack: +6 to hit, range 30/90 ft., one target. Hit: 7 (1d8 + 3) piercing damage."
  - name: "Command Crew"
    desc: "Reeves targets one creature he can see within 30 feet that can hear him. The creature must succeed on a DC 14 Wisdom saving throw or use its reaction immediately to move up to its speed toward a target Reeves designates, or to make one weapon attack against that target."
reactions:
  - name: "Quick Counter"
    desc: "When a creature hits Reeves with a melee attack, he can use his reaction to make one Scimitar attack against that creature."
```

---

## Cornered Captain Form

**Use when:** Reeves is isolated below decks, trapped in a narrow space, separated from his crew, or forced into direct combat without reinforcements. His crew cannot hear his commands or is too distant to respond. His desperation increases his personal ferocity.

```statblock
layout: Basic 5e Layout
name: "Captain Darius Reeves (Cornered)"
size: Medium
type: humanoid
alignment: "chaotic neutral"
ac: 18
hp: 88
hit_dice: "16d8 + 16"
speed: "30 ft."
stats: [19, 17, 13, 14, 13, 16]
saves:
  - strength: 7
  - dexterity: 6
  - charisma: 6
skillsaves:
  - acrobatics: 6
  - athletics: 7
  - deception: 5
  - insight: 3
  - perception: 3
  - persuasion: 5
damage_resistances: "none"
condition_immunities: "none"
senses: "passive Perception 13"
languages: "Common, Thieves' Cant"
cr: "5"
traits:
  - name: "Desperate Fervor"
    desc: "When Reeves hits a creature with a melee attack, he can choose to gain temporary hit points equal to 3. He can use this trait a number of times equal to his Constitution modifier (2), regaining all uses at the end of a long rest."
  - name: "Parry"
    desc: "Reeves adds 4 to his AC against one weapon attack within reach, provided he can see the attacker and is holding his scimitar."
  - name: "Cunning Action"
    desc: "On each of his turns, Reeves can use a bonus action to take the Dash, Disengage, or Hide action. However, he grants opportunity attacks if he uses Disengage since the space is cramped."
actions:
  - name: "Multiattack"
    desc: "Reeves makes two Scimitar attacks or two Pistol attacks."
  - name: "Scimitar"
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 11 (1d8 + 7) slashing damage. If the target is a creature, Reeves can push it up to 5 feet away."
  - name: "Pistol"
    desc: "Ranged Weapon Attack: +6 to hit, range 30/90 ft., one target. Hit: 8 (1d8 + 4) piercing damage."
  - name: "Desperate Thrust (Recharge 5-6)"
    desc: "Reeves makes a Scimitar attack with advantage. If this attack hits, the target takes an additional 5 (1d10) slashing damage."
reactions:
  - name: "Quick Counter"
    desc: "When a creature hits Reeves with a melee attack, he can use his reaction to make one Scimitar attack against that creature."
```

---

## Cursed Blade Form

**Use when:** Reeves draws the cursed blade as a final act—facing near-certain death, betrayed by crew, or making his last stand with nothing left to lose. This form represents his willingness to damn himself rather than surrender.

```statblock
layout: Basic 5e Layout
name: "Captain Darius Reeves (Cursed Blade)"
size: Medium
type: humanoid
alignment: "chaotic neutral"
ac: 16
hp: 66
hit_dice: "12d8 + 12"
speed: "30 ft."
stats: [20, 18, 12, 13, 12, 15]
saves:
  - strength: 8
  - dexterity: 7
  - charisma: 5
skillsaves:
  - acrobatics: 7
  - athletics: 8
  - deception: 4
  - perception: 3
  - persuasion: 4
damage_resistances: "necrotic"
condition_immunities: "none"
senses: "passive Perception 13"
languages: "Common, Thieves' Cant"
cr: "4"
traits:
  - name: "Cursed Pact"
    desc: "Reeves wields Blacktide, a cursed cutlass. His attacks with it deal an additional 3 (1d6) necrotic damage. When Reeves reduces a creature to 0 hit points with Blacktide, he gains 10 temporary hit points."
  - name: "Reckless Attack"
    desc: "At the start of his turn, Reeves can choose to attack recklessly. Until the start of his next turn, attack rolls against him have advantage, and his attack rolls with Blacktide have advantage."
  - name: "Final Stand"
    desc: "When Reeves is reduced to 33 hit points or fewer, his speed increases by 10 feet and he gains advantage on Strength saving throws."
actions:
  - name: "Multiattack"
    desc: "Reeves makes two Blacktide attacks, or uses Vicious Slash once and makes one Blacktide attack."
  - name: "Blacktide (Cursed Cutlass)"
    desc: "Melee Weapon Attack: +8 to hit, reach 5 ft., one target. Hit: 12 (1d8 + 8) slashing damage plus 3 (1d6) necrotic damage."
  - name: "Vicious Slash (Recharge 5-6)"
    desc: "Reeves makes a melee attack with Blacktide against each creature within 5 feet of him. He makes a separate attack roll for each target."
reactions:
  - name: "Cursed Riposte"
    desc: "When a creature hits Reeves with a melee attack while wielding Blacktide, he can use his reaction to make one Blacktide attack against that creature. If this attack hits, the target takes the attack's damage and must succeed on a DC 15 Wisdom saving throw or take 3 (1d6) psychic damage as the curse whispers doubts."
```

---

## Running Reeves

### Deck Lord Tactics

**Opening position and tell:** Reeves stands in the highest position available—quarterdeck, bridge, or captain's quarters—with a commanding view. His crew clusters nearby, awaiting orders. When combat begins, his immediate action is to position his crew and maintain control of space through commands, not personal combat.

**First round choices:** Reeves uses **Fleet Tactics** to move crew into advantageous positions—blocking chokepoints, flanking party members, or creating difficult terrain. He makes one Scimitar attack and one **Command Crew** order, reserving **Parry** for incoming threats. His crew's presence is the real danger; Reeves himself is a support piece.

**If pressured into personal combat:** Reeves shifts his scimitar use from positioning (pushing enemies) to damage, using **Cunning Action** to kite around obstacles. He employs **Quick Counter** to punish incoming attacks and maintains **Parry** against the party's strongest melee fighter. If the party closes on him effectively, he withdraws toward reinforcements or crew members who can shield him.

**If separated from crew:** This triggers the **Cornered Captain** form. Reeves notices immediately that his commands have no effect and his advantage has evaporated.

### Cornered Captain Tactics

**Position and tell:** Reeves is alone—trapped below decks, in a narrow corridor, or otherwise unable to receive or direct crew assistance. His voice carries no authority here. His bearing changes from commanding presence to cornered predator; his movements become aggressive and territorial.

**Default choice:** Without crew to buffer him, Reeves leans into personal offense. He uses **Desperate Fervor** to heal himself mid-fight, extracting resources from each hit. His **Parry** becomes more reactive, focused on survival. He avoids open ground, using the cramped environment to stay close and prevent ranged attacks from dealing damage safely.

**If the party gains an overwhelming advantage (majority of his HP gone):** Reeves recognizes the situation is untenable. He attempts to break line toward an escape route or shouted for reinforcements. If he can neither escape nor be reinforced, he pulls **Blacktide** and transitions to the **Cursed Blade** form as a final gambit.

**Counterplay:** The party can drive Reeves into isolation through positioning, blocking crew reinforcements, or using Hold Person and similar conditions. Once isolated and damaged, he becomes beatable. The real threat is preventing the party from isolating him in the first place.

### Cursed Blade Tactics

**The moment of desperation:** Reeves draws **Blacktide** with visible reluctance and rage. His eyes change; something older and hungrier speaks through him. He is no longer fighting to escape or win—he is fighting to take as many enemies with him as possible before the curse consumes him entirely. His **Reckless Attack** is the ultimate tell: he no longer cares if he gets hit.

**First turn:** Reeves uses **Reckless Attack** and makes two **Blacktide** attacks, accepting the incoming advantage against him. His +8 to hit and 1d8 + 8 + 1d6 per hit make him immediately dangerous. **Final Stand** kicks in if he drops below 33 HP—his speed increases, and he becomes harder to control.

**Middle rounds:** Reeves alternates between **Vicious Slash** (on recharge) to pressure multiple enemies and double **Blacktide** attacks when recharge is unavailable. Every kill with the sword heals him via **Cursed Pact**, creating a dangerous snowball if he can land killing blows. **Cursed Riposte** on his reactions converts incoming hits into offensive opportunities.

**Failure state:** If Reeves drops to 0 HP while wielding Blacktide, the curse does not release him—it pulls him deeper. **DM note:** Depending on the campaign, Reeves might be consumed by the curse and become a different monster entirely, reform as a cursed undead, or simply die, taking the weapon's corruption with him. Define this before combat begins.

**Counterplay:** The party can:
- **Disarm him:** Force a Save against losing Blacktide, removing his healing mechanism.
- **Use area control:** **Reckless Attack** only gives advantage on his attacks; spells and abilities that trigger saves or create difficult terrain still work.
- **Target the weapon:** Blacktide itself is a legitimate target (AC 16, 10 HP). Destroying it breaks **Cursed Pact** and leaves Reeves without healing.
- **Separate or control:** Hold Person, Banishment, or similar effects remove him from the fight temporarily, giving the party a breather.

### Encounter Integration

Reeves operates best with crew support and favorable positioning. The encounter design should allow the party to earn separation and isolation through clever tactics rather than raw stats. A victory where the party forces Reeves from Deck Lord → Cornered Captain → defeat feels earned. A victory that transitions to Cursed Blade (near-TPK scenario where Reeves activates his true form) becomes climactic and memorable.

**Transition tells:** Make the shift between forms obvious to the party:
- Loss of crew influence / crew being silenced or separated triggers **Cornered Captain** visibly.
- Drawing **Blacktide** is an unmistakable crossing of the line—Reeves speaks different dialogue, stands differently, his curse becomes visible (voice changes, shadow wrong, necrotic aura).

**Resources and crew:** Running Reeves with 4-6 crew members (use standard pirate or bandit stat blocks, lower CR) makes the Deck Lord encounter a proper medium difficulty. Without crew, Cornered Captain becomes a 1v4 or 1v5 where the party's numbers matter. Cursed Blade should be a last resort only—if reached, it's a climactic solo duel that ends the encounter decisively.
