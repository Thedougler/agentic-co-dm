# Worked example

One monster taken through steps 1 to 8. Every name, PC, and number here is
made up for illustration and is never canon. Match the **shape and quality**;
design your own monster from your own vault and your own party.

## 1. Party read and canon

| PC | Level | AC | HP | Weak saves | Round-1 damage | Signature trick | Escape and mobility |
|---|---|---|---|---|---|---|---|
| Oriel (monk) | 5 | 17 | 38 | Int, Cha, Con | 24 | Stunning Strike | Flies |
| Bram (paladin) | 5 | 20 | 49 | Dex, Int | 30 | Divine Smite | None |
| Sefa (wizard) | 5 | 13 | 32 | Str, Dex, Con | 28 | Fireball, Hypnotic Pattern | Misty Step |
| Tamsin (ranger) | 5 | 16 | 44 | Int, Cha, Con | 20 | Hunter's Mark at range | Longbow |

Party: average AC 16.5, highest 20. Nova about 70 after misses; sustained
about 48 per round; attack bonus about +7; Con saves about +2. Their last two
bosses were stunned by Oriel in round one and never used their best moves.

Canon inventory: `[[harrow-mouth]]` (fishing town on mudflats), `[[wader-guild]]`
(fisherfolk who wade the flats at dawn), `[[sea-fog-of-harrow]]` (lore: fog
rolls in at every spring tide), `[[bellglass]]` (item: lamp glass cast from
something's dried bell).

## 2. Path

Full design: no existing creature grabs from the air and swallows.

## 3. Concept

- **Stock version:** a giant jellyfish.
- **Twist:** a floating colony of small bodies that together form one bell as
  wide as a roof; it senses by its own hum and hunts in fog over land.
- **Niche:** drifts over the mudflats at dawn in spring fog and eats wading
  birds and waders. Nothing else in the region hunts from the air in fog.
- **Form follows function:** the bell's hum is its sense (blindsight by
  sound), the bell's shape is its thunderclap (Toll), four tendril curtains
  are its grabs, the gas bell is why fire drops it, and the ring of glowing
  inner bodies is why it can split.
- **Fiction sentence:** a floating ambush controller that grabs prey from the
  fog and reels it into its bell, to feed before the fog lifts; it fears fire
  and wind, and gives players silence, fire, and deaf ears as answers. Proof:
  the hum stops before it tolls.
- **Swap test:** "it stings" was true of every jellyfish; replaced with the
  swallow and the split.

## 4. The fight

- **Target:** Terrifying (spring-fog boss).
- **Role:** Controller; solo.
- **Signature move:** Toll. Tell: the hum stops and the rim draws tight for a
  full round. Threat: thunder and Prone across 30 feet. Answers: spread out,
  cast Silence on it, plug ears with wax (Deafened creatures succeed), get
  swallowed (inside is safe from Toll, not from acid). Payoff: prone targets
  are easy to grab and reel.
- **Separation:** Reel swallows a grabbed PC into the bell, 5 feet up, out of
  the party's reach.
- **Answers to their tricks:** Oriel's stun meets 2 Legendary Resistance, each
  use darkening one of the glowing inner bodies. Sefa's Hypnotic Pattern needs
  eyes it lacks, but her fire drops the bell to the ground. Bram's smites land
  when it is grounded or when he climbs a tendril.
- **Escalation:** at Bloodied it tears into two halves.
- **Morale:** each half flees into the fog when it drops below 15 HP; the fog
  lifting at sunrise ends the hunt.

## 5. Numbers

Target: Deadly. Its defense matches CR 10 (HP 190 is high, AC 14 is low) and
its offense matches CR 8 (about 60 damage per round at +9), so the label is
CR 9 (PB +4). It lasts about 4.5 party rounds (Deadly: 4) and can drop Sefa, the
most exposed PC, in about 2 (Deadly: about 2). Tuned against the party read: +9 hits average AC 16.5 about 67%
of the time and Bram 50%. DC 15 Con fails about 60% against their weak Con.
Effective HP about 215 after bludgeoning resistance lasts about 4.5 party
rounds across both forms. It survives the nova (190 minus 70) to act twice.

Three-round script: round 1 it lashes two PCs (about 18), grabs, and reels
Sefa in with a legendary action; the party deals about 70. Round 2: acid on
Sefa 14, lashes 18, legendary lash 9, Toll if recharged (about 65 across three
PCs); the party deals about 48 and it becomes Bloodied. Round 3: two halves,
each lashing and reeling. About 90 damage to the party in three rounds without
a Toll, about 150 with one. Two PCs are in danger; wax, Silence, and fire
change that sharply.

```statblock
layout: Basic 5e Layout
name: "Fogbell"
size: Huge
type: monstrosity
alignment: unaligned
ac: "14 (natural armor)"
hp: 190
hit_dice: "20d12 + 60"
speed: "0 ft., fly 20 ft. (hover)"
stats: [20, 10, 16, 3, 14, 6]
saves:
  - constitution: 7
  - wisdom: 6
skillsaves:
  - perception: 6
damage_resistances: "Bludgeoning"
damage_immunities: "Thunder"
condition_immunities: "Prone"
senses: "Blindsight 120 ft., Passive Perception 16"
languages: "—"
cr: "9"
traits:
  - name: "Echo Sense"
    desc: "The fogbell has no eyes. While it is Deafened or inside a Silence spell, it has the Blinded condition."
  - name: "Gas Bell"
    desc: "When the fogbell takes Fire damage, its bell sags: until the end of its next turn, its Fly Speed is 0, it rests on the ground, and it can't use Reel."
  - name: "Low Drift"
    desc: "The fogbell's rim hangs just above head height. Creatures on the ground within 5 feet of its space can reach it with melee attacks, and a creature can climb a tendril (Strength (Athletics) DC 12) to stand on its bell."
  - name: "Indrawn Hum"
    desc: "When Toll recharges, the fogbell's hum stops and its rim draws tight. It uses Toll on its next turn if it can."
  - name: "Legendary Resistance (2/Day)"
    desc: "If the fogbell fails a saving throw, it can choose to succeed instead. One of the glowing bodies inside its bell goes dark each time."
  - name: "Colony Split"
    desc: "The first time the fogbell is Bloodied, at the start of its next turn it tears into two Fogbell Halves in unoccupied spaces within 10 feet, each with half its remaining Hit Points. Swallowed creatures fall free and have the Prone condition. The halves act on the fogbell's initiative."
actions:
  - name: "Multiattack"
    desc: "The fogbell makes two Tendril Lash attacks. It can replace one attack with Reel."
  - name: "Tendril Lash"
    desc: "Melee Attack Roll: +9, reach 20 ft. Hit: 14 (2d8 + 5) Bludgeoning damage. If the target is Large or smaller, it has the Grappled condition (escape DC 15). The fogbell can have up to four creatures Grappled."
  - name: "Reel"
    desc: "Each creature Grappled by the fogbell is pulled up to 20 feet straight toward it. A creature that ends this pull within 5 feet of the fogbell is swallowed: the grapple ends, and the creature has the Blinded and Restrained conditions, has Total Cover against effects outside the fogbell, and takes 14 (4d6) Acid damage at the start of each of the fogbell's turns. The fogbell can hold two swallowed creatures. If a swallowed creature deals 20 damage or more to it on one turn, the fogbell must succeed on a DC 15 Constitution saving throw at the end of that turn or expel every swallowed creature, which lands Prone beneath it."
  - name: "Toll (Recharge 5–6)"
    desc: "Constitution Saving Throw: DC 15, each creature in a 30-foot Emanation originating from the fogbell, except swallowed creatures. A Deafened creature automatically succeeds. Failure: 22 (5d8) Thunder damage, and the target has the Prone condition. Success: Half damage only."
legendary_actions:
  - name: ""
    desc: "Legendary Action Uses: 3. Immediately after another creature's turn, the fogbell can expend a use to take one of the following actions. It regains all expended uses at the start of each of its turns."
  - name: "Drift"
    desc: "The fogbell flies up to 10 feet without provoking Opportunity Attacks."
  - name: "Lash"
    desc: "The fogbell makes one Tendril Lash attack. It can't take this action again until the start of its next turn."
  - name: "Reel"
    desc: "The fogbell uses Reel."
```

The first time it is Bloodied it splits. Each half uses this block.

```statblock
layout: Basic 5e Layout
monster: "Fogbell"
name: "Fogbell Half"
size: Large
hp: "half the Fogbell's remaining"
hit_dice: ""
traits-:
  - name: "Legendary Resistance (2/Day)"
  - name: "Colony Split"
actions-:
  - name: "Multiattack"
  - name: "Toll (Recharge 5–6)"
actions+:
  - name: "Toll (Recharge 6)"
    desc: "Constitution Saving Throw: DC 15, each creature in a 15-foot Emanation originating from the half, except swallowed creatures. A Deafened creature automatically succeeds. Failure: 13 (3d8) Thunder damage, and the target has the Prone condition. Success: Half damage only."
legendary_actions-:
  - name: ""
  - name: "Drift"
  - name: "Lash"
  - name: "Reel"
```

## 6. In the world

- **Habitat:** the mudflats of [[harrow-mouth]] during the spring fog
  ([[sea-fog-of-harrow]]); it never leaves the fog and sinks into the channel
  mud when the fog lifts.
- **Diet:** wading birds, seals, and waders. It leaves birds with their skin
  whole and their insides gone.
- **In the world:** the [[wader-guild]] calls it the Knell, wades in pairs
  with wax in their ears during spring fog, and pays well for dried bell
  jelly, which becomes [[bellglass]].
- **Signs:** a hum in the fog that no bird makes; rings of flattened mud 60
  feet across; drag lines that stop in the middle of the flat; hollow birds;
  guild waders with wax-stained ears.

## 7. Packet and narration

Tells: the ring of glowing inner bodies (Legendary Resistance, split), the
hum (its sense, and its silence before Toll), the bell shape, four tendril
curtains trailing in the mud (reach and grab), the gas-filled sag of the bell.

> A fogbell is a bell of pale jelly as wide as a cottage roof, drifting a little above head height over the mudflats with the spring fog. Four curtains of grey-green tendrils hang from its rim and trail in the mud behind it, leaving long shallow drag lines. Inside the bell, a ring of fist-sized bodies pulses with a faint blue light, and the dome above them bulges and sags like a sail full of wind. The whole colony gives off a low hum, the sound of a wet finger circling the rim of a glass, and it smells of low tide and cut copper. It drifts only where the fog lies, over flats scored with rings of flattened mud.

Why it works: every tell is plain appearance on the body part that carries
it. A player who asks about the hum, the glowing ring, or the sagging dome
has found a real answer, and the page has it.
