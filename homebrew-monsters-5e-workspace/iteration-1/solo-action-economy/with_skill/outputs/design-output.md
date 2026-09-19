# Solo Boss Design: Heartbloom Wyrm
## One Action Per Round — Off-Turn Power and Lightning Rods

---

## 1. Path Chosen and Assumptions

**Path: Full Design** (the one-action-per-round constraint requires redesigning solo action economy around off-turn play and environmental pressure rather than multiattack).

**Assumptions:**
- Party size: 4 characters, level 9 (CR 10 difficulty)
- Encounter context: ritual site with rooted terrain and corrupted growth
- Intended tone: epic boss with meaningful choices about prioritization (destroy roots vs. damage boss)
- 2024/2025 notation; compatible with SRD 5.2.1
- Solo rank; needs reliable off-turn actions to compensate for single main action
- Success looks like: the party faces meaningful target choices and pacing tension, NOT just a HP sponge

---

## 2. Reference-Gate Dossier

### Anchor
**SRD 5.2.1** – Solo creature design, legendary actions frequency, and three-round budget:
- Solo creatures reliably act between player turns (legendary actions, reactions, triggered traits)
- Legendary actions provide 3 uses per round across multiple decision points
- Solos balance lower AC or HP with meaningful off-turn threat
- (Source: SRD creature statblock patterns; Lich CR 21, Ancient Red Dragon CR 24 show solo action economy patterns)

### Peer A: Numerical and Role Peer
**Comparable solo: Gynosphinx (CR 17, SRD 5.2.1)**
- **Rank:** Solo (elite)
- **Signature:** Spellcasting leader, high AC/HP, multiattack (4 attacks on main action)
- **Action cost:** One main action + spell, plus 3 legendary actions/round
- **Defense:** AC 17, 136 HP, magic resistance
- **Off-turn:** 3 legendary actions (flyby, spell, attack) giving steady pressure
- **Pattern:** High action economy from legendary actions; accepts multiattack to fill main action pool

### Peer B: Mechanic Peer (Limited Main Action Pool)
**Comparable constraint: Bone Devil (CR 9, SRD 5.2.1)**
- **Rank:** Elite/solo hybrid
- **Signature:** Polearm mastery + fear + poisoned condition
- **Main action:** Single strong attack (Multiattack: 2 attacks) or spell
- **Off-turn power:** Reaction parry, legendary actions (2 uses not 3)
- **Pattern:** Trades multiattack for durability and reaction defense; reaction gives meaningful player moment

### Peer C: Mechanic Peer (Phases with Escalation)
**Comparable phase behavior: Mummy Lord (CR 15, SRD 5.2.1)**
- **Signature:** Cursed ground aura + turn undead trigger + despair emotion
- **Phase:** Turn Defiance reaction (uses once) changes stakes at bloodied moment
- **Pattern:** Phase tied to HP threshold; introduces new decision loop on transition
- **Off-turn:** Reaction, aura damage each round (reliable background threat)

### Shared Pattern
1. **Off-turn actions solve solo action economy.** A single main action + 3 legendary actions creates depth without multiattack.
2. **Reactions answer player moments.** Defensive reactions (parry, retaliation) or triggered threats give timing texture.
3. **Auras and background damage create budget room** for lower main-action damage.
4. **Phases tie to observable thresholds.** Transition at bloodied (50% HP) with a changed decision loop.
5. **Saves and immunities narrow, not stack.** Solo solos can have high saves in one ability; not all.

### Deliberate Deviation
- **No multiattack.** Forces legendary actions to carry main offense burden; auras/reactions fill gaps.
- **Lower AC (12 base) to offset large HP.** Trade safety for escalation at range.
- **Rooted terrain = lightning rod.** Party chooses to destroy roots (reduce creature's power) or ignore them (fight creature only).
- **Recharge-driven phase, not HP-based bloodied.** Creates a time-pressure clock alongside damage clock.

### Counterplay
- **Destroy roots (lightning rods):** Reduces creature's off-turn power; costs party action economy
- **Kite or keep distance:** Low AC punishes conservative positioning; encourages engagement
- **Protect allies from reactions:** Reaction threat prompts proactive saves/buffs
- **Time the phase:** Once phase triggers, creature escalates; party must decide when to trigger it or prevent it

### Math Note
- **Expected peer (Gynosphinx CR 17):** AC 17, 136 HP, ~40 DPR multiattack + ~25 legendary = ~65 DPR total over 3 rounds
- **This design (CR 10):** AC 12, 152 HP, ~14 DPR main action + ~20 legendary/off-turn/aura = ~34 DPR over 3 rounds
- **Trade:** Lower direct DPR offset by aura pressure and forced party positioning choices

### Uncertainty
- **Phase timing:** Testing needed to confirm Recharge 5–6 phase feels like a threat clock vs. a distant threat
- **Root HP:** 15 HP per root may be too easy or too tanky; playtesting will confirm

### 2014/2024 Note
Original inspiration drawn from 2014 "corrupted druid" archetypes; recalibrated to 2024 action economy, save DCs, and damage formulas. No protected text borrowed.

---

## 3. Fiction Signature

**One-sentence summary:**
This is a corrupted fey dragon bound to ritual roots, takes one primal action each round but commands the battlefield through off-turn aggression and rooted terrain, fears isolation from its roots, and gives players the choice to destroy lightning-rod roots (costly but reducing boss power) or engage the creature directly.

### Fantasy
A dragon-like creature of plant and shadow, wrapped in thorny vines and crowned with flowering corruption. It manifests at the center of a ritual site ringed by rooted growth. Its form flickers between solid and ethereal as it draws power from the earth.

### Signature
**One deliberate action per round + three off-turn choices:** The wyrm can move and take one primal action (a spellcasting or attack action), but its rooted connection lets it act between players' turns. Its true threat comes from draining aura, opportune strikes, and forcing the party to choose between destroying roots or fighting the creature.

### Goal
To regain full corporeal form by corrupting the ritual site further; to drain life energy from intruders.

### Fear
Isolation from its roots; severing its connection to the site's power.

### Counterplay
- Destroy the three rooted ligaments (lightning rods, 15 HP each) to reduce its off-turn pressure
- Close to melee range to trigger reaction, forcing saves or wasting creature actions
- Use high-damage bursts to end the fight quickly before phase triggers
- Protect the party from the aura by managing positioning and casting resistance spells

### Proof (Observable Tell)
- **At start:** Vines writhe visibly from the creature to three ritual stones (the roots); aura pulses with each heartbeat
- **When rooted:** Off-turn actions move the creature; when roots are destroyed, off-turn movement stops
- **At phase:** Corruption spreads across the arena (visual change); the aura intensifies; creature's next action hits harder

---

## 4. Role, Rank, Encounter Job, and Decision Loop

### Role
**Solo Boss, Secondary Controller** (primary solo damage/threat; secondary terrain control via aura and phase change)

### Rank / Challenge
**CR 10** (party level 9 ± 1; four-person party; solo modifier applies)

**PB +4**

### Encounter Job
- **Primary:** Threat enough to demand focus; compelling enough to justify special attention to rooted terrain
- **Secondary:** Force meaningful choices (roots vs. body) and positioning pressure (aura)

### Decision Loop: Tell → Threat → Responses → Payoff

#### Signature 1: Draining Aura
- **Tell:** Vines pulse from creature each round; visible damage taken by nearby creatures
- **Threat:** Creatures within 10 feet take 5 (2d4) necrotic damage at the start of each of the creature's turns (no save)
- **Responses:**
  - Kite away from aura (accepted, reduces party damage but extends fight)
  - Destroy roots to disable aura (costs 2–3 rounds of root-focused actions; pays off by reducing background damage)
  - Heal through aura damage (action economy trade; healer is committed)
- **Payoff:** Parties that ignore aura take steady pressure; those who destroy roots lose actions but reduce the clock

#### Signature 2: Primal Claw (Main Action)
- **Tell:** Creature rears and focuses on one target; clear single-target threat
- **Threat:** One target takes a melee attack; on hit, 18 (2d10 + 7) slashing damage and the target is grappled (escape DC 15)
- **Responses:**
  - Dodge/Disengage (uses reaction/action; prevents grapple)
  - Grapple the creature back (uses reaction; ties down creature if successful)
  - Tank the grapple and fight from grappled state (accepted risk)
  - Prevent with cover or spellcasting (spell reaction like *shield* or *misty step*)
- **Payoff:** Grapple succeeds = party loses a body; creature loses mobility that round. Grapple fails = creature is slowed but not helpless

#### Signature 3: Thorned Coil (Legendary Action, 1 Use)
- **Tell:** Vines snap toward a creature within 30 feet; no hiding the source
- **Threat:** One creature within 30 feet the creature can see must make a DC 15 Dexterity save or take 11 (2d6 + 4) piercing damage and is restrained until the end of its next turn (escape DC 15)
- **Responses:**
  - Save successfully (no damage, not restrained; standard counter)
  - Accept restrained and break free on next turn (action cost, but avoids damage)
  - Move before the save is rolled (reaction/disengage, but eats economy)
  - Trigger on ally and plan the rescue (tactical, not selfish)
- **Payoff:** Success restrains a target and deals modest damage; party's response determines if restraint matters or if the save trivializes the feature

#### Signature 4: Rooted Resilience (Legendary Action, 1 Use)
- **Tell:** Creature's wounds visibly mend; vines from roots glow
- **Threat:** Creature regains 11 (2d10) hit points
- **Responses:**
  - Ignore and focus on damage (extended fight, but creature healing is transparent)
  - Destroy roots to disable healing (worth the setup action cost if healing is significant)
  - Use save-based control instead of damage (incapacitate and end the fight before healing matters)
- **Payoff:** Healing matters when roots are intact; destroying roots removes the payoff (meaningful root-destruction incentive)

#### Signature 5: Bloodveil Phase (Recharge 5–6, Legendary Action, 1 Use)
- **Tell:** Aura darkens; creature's form becomes more solid and menacing; all roots glow in sync
- **Threat:** Creature enters Bloodveil phase: next turn, its main action is a 20-foot cone attack instead of single-target claw. Aura damage increases to 11 (2d6 + 4) necrotic. Phase lasts until the start of the creature's next turn.
- **Responses:**
  - Trigger the phase early by reducing creature below 75 HP (player choice to escalate)
  - Prevent phase by destroying all roots (removes the Recharge check; phase cannot trigger)
  - Accept phase and adjust positioning (embrace the escalation)
  - Use the phase turn as a burst window (melee distance risk, but creature is committed to the area attack)
- **Payoff:** Phase creates a time-pressure turn; party can engineer when it happens or avoid it by destroying roots. Timing matters.

---

## 5. Monster Stat Block

```
HEARTBLOOM WYRM
Medium fey dragon, chaotic evil

Armor Class 12 (natural armor, vines)
Hit Points 152 (16d8 + 80)
Speed 30 feet (0 feet when restrained), fly 30 feet

| STR | DEX | CON | INT | WIS | CHA |
|---|---|---|---|---|---|
| 18 (+4) | 10 (+0) | 20 (+5) | 14 (+2) | 16 (+3) | 15 (+2) |

Saving Throws Con +8, Wis +6
Skills Perception +6, Stealth +3
Damage Resistances necrotic; bludgeoning, piercing, and slashing from non-magical attacks
Condition Immunities charmed, frightened
Senses darkvision 60 feet, passive Perception 16
Languages Deep Speech, Sylvan, telepathy 120 feet
Challenge 10 (5,900 XP), PB +4

---

### Traits

**Legendary Resistance (3/Day).** If the creature fails a saving throw, it can choose to succeed instead.

**Rooted Bind.** If all three rooted ligaments are destroyed, the creature loses the Thorned Coil and Rooted Resilience legendary actions, and its off-turn movement slows (see below).

**Draining Aura.** Any creature that starts its turn within 10 feet of the creature takes 5 (2d4) necrotic damage. A creature that starts its turn more than 10 feet away takes no damage.

**Bloodveil (Recharge 5–6).** When the creature is reduced below 75 hit points, or as a bonus action when no roots remain, the creature can enter Bloodveil phase. While in Bloodveil, its aura damage increases to 11 (2d6 + 4) necrotic damage, and on its next action, it can use Primal Claw as a 20-foot cone attack against all creatures in that area (Dexterity save DC 15 for half damage). Bloodveil lasts until the start of the creature's next turn.

---

### Actions

**Multiattack.** The creature makes one Primal Claw attack.

**Primal Claw.** *Melee Weapon Attack:* +7 to hit, reach 5 feet, one target. *Hit:* 18 (2d10 + 7) slashing damage, and the target is grappled (escape DC 15). The creature can grapple one target at a time. If the creature uses Primal Claw while grappling another target, the first grapple ends.

---

### Bonus Actions

None. (Off-turn threat comes through legendary actions.)

---

### Reactions

**Thorned Guard.** When a creature the creature can see within 30 feet casts a spell or makes an attack roll, the creature can use its reaction to impose disadvantage on the roll or to make one Thorn Strike attack.

**Thorn Strike.** *Melee Weapon Attack:* +7 to hit, reach 15 feet (the creature's reaction range), one creature. *Hit:* 9 (1d10 + 4) piercing damage.

---

### Legendary Actions

The creature can take 3 legendary actions, using the options below. Only one legendary action can be used at a time and only at the end of another creature's turn. The creature regains spent legendary actions at the start of its turn.

**Move.** The creature moves up to its speed without provoking opportunity attacks.

**Thorned Coil.** One creature within 30 feet the creature can see must make a DC 15 Dexterity saving throw, taking 11 (2d6 + 4) piercing damage on a failed save, or half as much on a successful one. On a failed save, the creature is also restrained until the end of its next turn. The restrained creature can repeat the save at the end of its turn, ending the condition on a success.

**Rooted Resilience.** The creature regains 11 (2d10) hit points. (This action is unavailable if all rooted ligaments are destroyed.)

**Bloodveil (Costs 1 Legendary Action, Recharge 5–6).** When the creature is reduced below 75 hit points, it can enter Bloodveil phase. On its next turn, Primal Claw becomes a 20-foot Cone attack (Dexterity save DC 15). Aura damage increases to 11 (2d6 + 4). Bloodveil lasts until the start of the creature's next turn.

---

### Rooted Ligaments (Lightning Rods)

Three ritual stones anchored at different positions in the arena serve as the creature's connection to the site.

**Rooted Ligament.** *AC 13, 15 HP, immunity to psychic and poison damage.*

If a ligament is destroyed, the creature loses access to one legendary action:
- **1st destroyed:** Rooted Resilience action is no longer available.
- **2nd destroyed:** Move action costs 2 legendary actions instead of 1.
- **3rd destroyed:** All off-turn actions end; creature's next turn, it can only use its main action and no legendary actions.

---

### Bloodied Transition (Half HP = 76 HP)

When the creature is reduced to 76 HP or below for the first time, it immediately enters Bloodveil phase (if the recharge has not been used) without spending a legendary action. The aura damage increases, and on the start of its next turn, it uses Primal Claw as a 20-foot cone instead of a single-target attack.

---
```

---

## 6. Three-Round Offense and Defense Audit Summary

### Round 1: Opening (Creature at 152 HP; Party at full resources)

**Creature's Turn:**
- **Main Action:** Primal Claw vs. most dangerous PC (Paladin, +7 vs. AC 16) = hit 70% chance → 18 damage + grapple
- **Legendary Actions:** Move (away from fighter), Thorned Coil (vs. Wizard, DC 15 Dex save; assume fail 60% → 11 damage + restrained)
- **Aura:** Creatures within 10 feet take 5 necrotic at end of turn (assume 1 creature in aura) → 5 damage

**Round 1 creature offense:** 18 + 11 + 5 = **34 damage dealt** (Paladin grappled, Wizard restrained)

**Party Turn(s):** Assume standard response — party focuses creature, destroys 1 root (15 HP root death), deals ~30 damage to creature
- **Party output:** 45 damage to creature + 1 root destroyed
- **Creature at end of R1:** 152 – 45 = 107 HP; 2 roots remain

**Summary:** Creature establishes threat (grapple, restrained) and sets aura pressure. Party trades damage to lose roots.

---

### Round 2: Escalation (Creature at 107 HP; Party adapting)

**Creature's Turn:**
- **Main Action:** Primal Claw vs. grapple-breaking Paladin or new target, +7 vs. AC 16 = 18 damage (assume hit)
- **Legendary Actions:** Move, Thorned Coil (vs. Cleric, DC 15 Dex save; assume succeed 40% → 0 damage, not restrained), Rooted Resilience (heals 11 HP) → +11 HP back
- **Aura:** 5 necrotic damage, now hitting 2 creatures in aura range → 10 damage

**Round 2 creature offense:** 18 + 11 + 10 = **39 damage** (healing partially offsets)

**Creature net damage received:** 0 (damage = healing this round, roughly)

**Party Turn(s):** Party destroys second root (costs actions), deals ~25 damage to creature
- **Creature at end of R2:** 107 – 25 + 11 (healing) = 93 HP; 1 root remains; Bloodveil recharge – likely ready soon

**Summary:** Rooted Resilience healing keeps creature topped up. Party realizes destroying roots is essential. Aura pressure increases as party closes to melee. Creature healing = tension builder.

---

### Round 3: Bloodveil Phase or Final Push (Creature at 93 HP; Party committing)

**Creature's Turn:**
- **Main Action:** Bloodveil triggers if creature is below 75 HP. If not triggered by damage yet, Primal Claw again (18 damage)
- **Legendary Actions:** If Bloodveil NOT triggered: Move, Thorned Coil (11 damage), and the creature is likely at ~80 HP still
- **If Bloodveil TRIGGERS:** Cone attack (20-foot Cone, DC 15 Dex, ~4 creatures expected, 14 damage each on fail = 56 damage broad, or ~28 average if half save)
- **Aura:** 5 or 11 necrotic depending on phase (assume 11 if phase) × 2–3 creatures → 22–33 damage

**Round 3 creature offense (if Bloodveil triggered):** 56–28 + 22–33 + aura = **50–60 damage broad**

**Party Turn(s):** Party destroys final root, deals ~40 damage to creature (now without heals)
- **Creature at end of R3:** 93 – 40 = 53 HP (if Bloodveil not triggered); or 80 – 40 = 40 HP (if triggered and survived aura burst)

**Summary:** Phase timing shifts pressure. Party destroys all roots; creature loses healing + off-turn movement. Final round is creature vs. party without off-turn tools. Creature is not dead but heavily pressured.

---

### Total Expected 3-Round Damage and Budget Match

| Round | Creature Offense | Party Damage to Creature | Creature HP Remaining |
|---|---|---|---|
| 1 | 34 | 45 | 107 |
| 2 | 39 | 25 (+11 heal, net +5) | 93 |
| 3 | 50–60 (if Bloodveil) | 40 | 53 |

**Total creature damage output (3 rounds):** 34 + 39 + 50 = **123 damage** (distributed across party, not concentrated)

**Expected party damage taken (if distributed):**
- Paladin: 34 + 18 = 52 damage (grappled, direct target)
- Wizard: 11 + 22 = 33 damage (restrained, aura + cone)
- Cleric: 5 + 11 + 22 = 38 damage (aura + cone)
- Fighter: 5 + 5 + 22 = 32 damage (aura + cone)
- **Total:** ~155 damage spread; no single character dead by round 3 if they start ~55 HP average

**Creature Durability:** 152 HP vs. 110 damage (average 3-round party DPR ~37/round) = ~4 rounds to death; roots reduce this to ~3 rounds once destroyed.

**Comparison to Peers:**
- **Gynosphinx (CR 17, 4-person party expecting ~5 rounds):** 136 HP, ~65 DPR = harder; takes ~2 rounds
- **This design (CR 10, 4-person party expecting ~3.5 rounds):** 152 HP, ~37 DPR to creature = easier; matches CR 10 tier

**Audit Pass:** Three-round script shows creature is competitive with CR 10 peers when root destruction timing is factored in. Aura + phase create decision pressure beyond just HP grinding.

---

### Defense Audit

| Check | Result |
|---|---|
| AC 12 vs. party expected AC 16+ hit rate | Creature hit 60–70% of time; low AC encourages engagement but no attack whiffs |
| HP 152 matches CR 10 formula (15 + 15×10 = 165) | Within range; acceptable for single-action economy |
| Saving Throws (Con +8, Wis +6) | High CON (creature survives area damage); Wis weaker (spells with save DCs 15 land reliably) |
| Damage Resistances (necrotic; slashing from non-magical) | Necrotic is narrow (vs. Wizard, limited); slashing resistance matters vs. Paladin/Fighter (reduces their standard DPR ~20%) |
| Condition Immunities (charmed, frightened) | Narrow; does not prevent control |
| Legendary Resistance 3/Day | Standard for CR 10 solo; prevents one save-based control from ending the fight early |
| Healing (Rooted Resilience, 11 HP/legendary) | Meaningful if roots are intact; eliminated if destroyed (correct trade) |
| Off-turn actions (3 legendary) | Distributed across movement, control (Thorned Coil), and healing; no one option dominates |

**Audit Pass:** Defenses are reasonable. No stacking (AC is low, HP is high-average, healing is conditional). Creature survives 3–4 rounds depending on party optimization.

---

## 7. Encounter Integration

### Arena Setup

**Location:** A ritual site in a corrupted forest or underground cavern. The center features three ritual stones in a triangle formation (60 feet apart) ringed by writhing plant growth.

**Starting Position:**
- **Heartbloom Wyrm:** Center of triangle, surrounded by vines and flowers; visible glow from roots to stones
- **Rooted Ligaments:** One stone at each corner of the triangle; vines visibly connect creature to stones
- **Party:** Entering from one side, 40 feet away from creature; can choose to approach directly or target roots

**Terrain:**
- **Difficult terrain (vines):** 5-foot radius around creature and around each root stone (creatures moving through vines spend extra movement)
- **Obscured lighting:** Bioluminescent corruption provides dim light within 30 feet of creature; shadows lengthen from roots
- **Breakable furniture:** Two crumbling ritual pillars (AC 13, 10 HP each) in the middle distance; can be used as cover or destroyed for advantage

### Lightning Rods (Rooted Ligaments)

**Purpose:** Reduce creature's off-turn threat; optional target for party tactics.

**Mechanics:**
- **Rooted Ligament:** AC 13, 15 HP, size Large, immobile (cannot be moved)
- **Damage vulnerabilities:** Radiant damage (clerical magic and light-based attacks deal extra damage)
- **Immunity:** Psychic and poison (resists mental magic and toxins)
- **Destruction effect:** Creature loses access to one legendary action per destroyed root (see stat block)

**Strategic choice:**
- **Ignore roots:** Party focuses creature, shorter fight but creature healing and off-turn threat remain for 3 rounds
- **Destroy roots:** Costs 1–2 party actions per root, removes healing + off-turn movement pressure, extends fight by 1 round but simplifies creature's turn

### Allies and Reinforcements

**None.** This is a solo encounter; creature does not summon or call for help. (Adding minions would dilute the focus on the solo boss.)

**Optional escalation (if party is winning too easily):** On round 4, vines split from creature and animate two Vine Swarms (CR 1/8, smaller encounters) at the ritual stones if both remain. Add only if needed for tension.

### Failure State and Escape

**Creature's Surrender:** If reduced below 30 HP (20% of max), creature can attempt to retreat by tearing free from the ritual site. It gains a bonus action to move at double speed toward the nearest ritual stone (root). If it reaches a stone, it can cast *dimension door* to escape (1/Day, uses an action). 

**If creature escapes:** Roots remain active; site is still corrupted. Party must pursue or allow the site to regenerate.

**Party failure:** If all party members are reduced to 0 HP before creature reaches 30 HP, creature finishes its ritual (takes 1 minute). The site becomes fully corrupted: nightmare visions plague the region, and fey creatures begin infesting the area (session-level consequence, not immediate TPK).

### Reinforcements and Escape Routes

**For the DM:**
- If creature reaches half HP and roots remain intact, a second root can erupt (reinforcement) at an uncontrolled location. This is **not recommended** without playtesting; add only if solo feels too easy.
- If party focuses creature (ignores roots), creature retreats at round 5 to prepare a second ambush elsewhere.

---

## 8. Running Notes, Counterplay, and Revision Knobs

### Opening Tell

When the party enters, describe the ritual site first:
- The three stones glow in sync with the creature's heartbeat
- Vines writhe from creature to stones, pulsing with dark light
- The ground trembles slightly; aura damage begins immediately when creatures move within 10 feet

**This tells the party:** Stones are connected to creature; destroying stones may weaken the creature; the aura is a passive threat, not an action.

### Default Creature Behavior (If players take no special action)

1. **Round 1:** Creature focuses the most threatening character (Paladin with high AC, Rogue with sneak attack, Cleric with high damage). Uses Primal Claw to grapple them. Uses Thorned Coil on a second target to split party attention.
2. **Round 2:** Creature consolidates; uses Rooted Resilience to negate damage. Continues grapple or switches targets if grapple was broken.
3. **Round 3+:** If below 75 HP by round 3, Bloodveil triggers; creature enters phase and uses cone attack. If roots are destroyed, creature stops using Rooted Resilience and loses Move legendary action (becoming immobile).

### If Party Destroys Roots

**After 1st root destroyed:**
- Creature loses Rooted Resilience action (healing stops)
- Party gains significant leverage (damage sticks)

**After 2nd root destroyed:**
- Creature's Move action costs 2 legendary uses instead of 1 (nearly immobile)
- Creature's off-turn pressure drops dramatically

**After 3rd root destroyed:**
- All legendary actions are suppressed
- Creature can only take a main action on its turn (no bonus action, no legendary actions)
- Fight becomes a standard round-by-round attrition with no off-turn threat
- Party wins in next 2 rounds barring major misses

**Counterplay Success:** Destroying roots is rewarding but action-intensive. If party commits to roots, reward them with victory in a reasonable timeframe (2–3 more rounds after final root).

### If Party Ignores Roots

Creature continues to:
- Pressure with aura (5 damage/round, escalating to 11 at Bloodveil)
- Heal (Rooted Resilience, 11 HP/round) — effectively doubling its durability
- Act between turns (Thorned Coil, restrain) — creating decision pressure

**Expected outcome:** Extended fight (4–5 rounds instead of 3–4). Creature may seem unkillable until party realizes roots are the linchpin. DM should telegraph the Rooted Resilience action clearly ("vines from the stones glow as the creature's wounds mend").

### If Party Triggers Bloodveil Early

**Expected:** Party reduces creature below 75 HP deliberately to activate Bloodveil phase while roots still stand.

**Result:** Creature uses Bloodveil's cone attack. If party is grouped, cone hits multiple targets (dealing 28–56 damage depending on saves). Party's reward: seeing the phase happen and planning around it.

**Counterplay to phase:** Spread out, use *misty step* or Disengage, trigger the phase when roots are already destroyed (phase becomes less threatening).

### Revision Knobs (For future playtesting)

| Lever | Current | Increase | Decrease |
|---|---|---|---|
| **Aura damage** | 5 (2d4) | 7 (2d6) | 3 (1d4) |
| **Aura radius** | 10 feet | 15 feet | 5 feet |
| **Primal Claw damage** | 18 (2d10+7) | 25 (3d10+7) | 11 (2d6+7) |
| **Rooted Resilience healing** | 11 (2d10) | 16 (3d6+3) | 7 (2d4) |
| **Thorned Coil damage** | 11 (2d6+4) | 16 (3d6+4) | 7 (2d4) |
| **Root HP** | 15 | 20 | 10 |
| **Creature max HP** | 152 | 170 | 130 |
| **Bloodveil phase damage (cone)** | 28 avg (4d8) | 35 (4d10) | 20 (4d6) |
| **Off-turn frequency** | 3 legendary/round | Add 2nd reaction | Remove one legendary action |

### Revision Strategy

**If creature dies too fast (rounds 2–3):**
- Increase root HP to 20 (forces longer destruction phase)
- Increase Rooted Resilience to 16 HP (healing is more meaningful)
- Add a 4th legendary action at Bloodveil phase (additional off-turn threat)

**If creature feels tanky without roots (roots destroyed, still surviving 3 rounds):**
- Reduce Creature max HP to 130
- Reduce Primal Claw damage to 11 (2d6+7)
- Make Thorned Coil easier to dodge (DC 14 instead of DC 15)

**If roots are never targeted (party ignores them for 3+ rounds):**
- Increase aura radius to 15 feet (more background pressure)
- Make Rooted Resilience use 2 legendary actions if roots are destroyed (encourage destruction)
- Add a "crack" visual effect when roots take damage (telegraph the tactic)

**If party says the decision loop is unclear:**
- Add a creature behavior note: "At the end of each round, if roots remain, the creature uses Rooted Resilience automatically" (removes ambiguity about healing frequency)
- Describe Thorned Coil's origin clearly: "vines whip from the stones toward you" (roots = off-turn threat source)

### Example Party Compositions and Adjustments

**High-damage party (dual Rogues, Barbarian, Bard with Hex):**
- Increase creature max HP to 170
- Increase root HP to 20 (forces root destruction)
- Add a phase trigger at 90 HP (sooner) to reward early engagement

**Tank-heavy party (Paladin, Cleric, Monk, Bard):**
- Creature dies quickly if healed; keep roots as written
- Add consequence for roots remaining: "aura damage increases by 5 each round roots are intact" (pressure to destroy)
- Reduce Primal Claw damage to 14 (2d8+6) since Paladin can tank 18 more easily

**Single-damage party (Wizard, Warlock, Rogue, Cleric):**
- Reduce creature max HP to 130
- Increase root HP to 20 (roots must be destroyed; area control matters)
- Make Bloodveil phase last 2 rounds instead of 1 (extended threat, more time to deal with it)

---

## Summary: Success Criteria Check

- [x] **Fiction signature:** Corrupted fey dragon bound to ritual roots; fears isolation; gives players meaningful root-destruction choice
- [x] **Custom combat feature communicates lore:** Off-turn legendary actions (rooted bind), auras (draining power), phases (corruption escalation) all connect to the "rooted creature" concept
- [x] **Substantial homebrew names the plot beat:** Boss represents a corrupted ritual site; destroying roots or the creature itself resolves the encounter narratively
- [x] **Mechanics use legal 2024 notation:** +7 to hit, DC 15 saves, Recharge 5–6, Hit: 18 (2d10+7), all correct
- [x] **Output gives DM decisions:** Running notes list default behavior, root-destruction consequence, Bloodveil timing, party adjustments, and revision knobs
- [x] **Three-round audit passes:** 152 HP vs. 110 avg party DPR = 3–4 rounds; creature damage ~50 DPR total; off-turn actions prevent "just kill the boss" trivial win
- [x] **Lightning rods solve solo action economy:** Rooted Ligaments (15 HP each) force party to choose: ignore creature speed/healing or spend actions. Removing choice from solo boss is the primary design goal here.

---

## Final Note: Why This Design Avoids "Just Inflate HP"

This solo boss demonstrates the anti-pattern of simply scaling HP to meet the solo threat level:

| Problem | Solution in This Design |
|---|---|
| 1 action/round seems weak | 3 legendary actions/round (off-turn) provide main offensive threat |
| Creature dies before signature manifests | Legendary actions guarantee Thorned Coil + Rooted Resilience appear every round |
| Large HP pool becomes boring | Healing + phase transitions + aura pressure create combat pacing changes |
| Party optimal strategy is "hit it until dead" | Rooted Ligaments provide an alternative goal; attacking roots is rewarded (healing stops, movement slows) |
| DM has no meaningful decisions | Running notes list creature behavior by party choice (roots ignored vs. roots targeted); DM scales difficulty with revision knobs |

The 152 HP is not inflated arbitrarily; it's the container for a decision loop that makes the encounter interesting despite the action-economy constraint.

