# Lava Asp Design Output

## Path and Assumptions

**Path chosen:** Full design (not reskin or variant).

**Why:** The signature mechanic—heat shimmer as a ranged evasion tool—and the pair-hunting social structure centrally define the creature's role and decision loop. Neither can be expressed through reskin or a one-or-two-hook variant.

**Assumptions:**
- Party tier: 4–5, medium (CR 5 appropriate for midtier play)
- Party size: 4–5 characters
- Volcanic island environment with lava tubes, vents, heat shimmer visible at range
- Pair hunting is the expected social unit; individual encounter would still face a CR 5 creature
- 2024/2025 mechanics throughout (no 2014 conversion)
- Action economy: standard package (action + bonus + reaction, no legendary actions)

---

## Reference-Gate Dossier

### Peer Selection and Patterns

**Numerical peer: Wyvern (CR 6)**
- AC 15, HP 110, +7 to hit, ~36 DPR
- Melee ambusher with ranged tail strike and flying mobility
- Ranks above CR 5 but represents aerial/distance evasion pattern

**Role peer: Giant Constrictor Snake (CR 2)**
- AC 12, HP 60, +6 to hit, ~14 DPR
- Terrain-based ambusher from undergrowth; grapple-focused
- Demonstrates isolation-and-immobilize pattern at lower tier

**Mechanic peer: Manticore (CR 3)**
- AC 13, HP 52, +5 to hit
- Tail spikes as ranged option while engaged in melee
- Multi-attack split (melee + ranged rider) at mid-tier

### Shared Patterns
- Ambusher creatures front-load concealment or positioning (terrain, distance, stealth)
- Isolation mechanics (grapple, drag, pin) shift action economy toward the creature
- Ranged pressure from creatures that also brawl in melee reduces party range advantage
- Two-attack rotation (melee + rider) is standard at CR 3–6

### Deliberate Deviations
- **Heat shimmer as a ranged concealment tool** (not cover/stealth): Lava Asp stays visible but blurred, making ranged attacks against it unreliable while it approaches. This is not invisibility (not broken) but creates a "why bother shooting" moment—player answer is to close distance or use AOE.
- **Pair-bonded behavior**: When both Asps target the same prey, they gain a bonus. This incentivizes the party to split the pair (player counterplay). Solo Asp is still complete.
- **Venom delay mechanic**: Poison damage comes on the *next* turn, creating a resource-tracking and decision moment (do I burn an action on a saving throw, or do I prepare for damage?). This mirrors the grapple isolation pattern but with a damage-over-time framing.

### Counterplay
- **Ranged attacks against shimmer-obscured Asp**: disadvantage while at range (shimmer fades within 30 feet)
- **Cold/water damage**: Thermal predator is vulnerable to sudden cold (no resistance, vulnerability is too harsh; instead, it triggers a retreat instinct if hit by cold)
- **Pack separation**: If one Asp is killed or forced 60+ feet away, the survivor loses the coordination bonus
- **Area denial**: Caltrops, spike growth, or difficult terrain slow approach and counter the venom strike setup

### Math Note
**Expected numbers for CR 5 standard:**
- AC 15 (natural armor) — in range with Wyvern peer
- HP 82 (11d8 + 33) — fits 15 + (15 × 5) baseline
- Attack +6 to hit (PB +3, DEX +3)
- Damage per round: ~28 DPR base (two medium attacks), ~42 with venom on setup turn
- Three-round DPR (scripted below): 14 (approach) + 35 (pair strike) + 28 (cleanup) = ~77 DPR across 3 rounds for a pair; ~39 DPR average

**Peer comparison:**
- Wyvern (CR 6) outputs 36 DPR; lava Asp pair averages 39 DPR → reasonable
- Wyvern has 110 HP; Asp at 82 HP is below to compensate for pair coordination bonus
- Wyvern AC 15 matches Asp AC 15

### 2014/2024 Note
No 2014 conversion; 2024 mechanics throughout. Saving throw DC = 8 + PB 3 + CON 3 = DC 14 (poison).

### Uncertainty
- Pair bonus (advantage on next attack if both target same prey) has not been playtested; may be too strong or too weak
- Shimmer concealment (ranged attack disadvantage) is strong; if it trivializes ranged damage, change to just partial cover (+2 AC bonus instead)
- Venom is delayed damage, creating a two-turn decision loop; needs table feedback on whether it feels swingy

---

## Fiction Signature

**One-sentence fantasy:**
"This is a scaled volcanic ambusher that uses heat shimmer to close distance, hunts in coordinated pairs to isolate prey, and manifests delayed venom to create decision pressure."

**Expanded signature frame:**
- **Fantasy:** Lava Asp is a sleek, heat-adapted reptilian predator of volcanic vents. Its body is dark obsidian-black with rust-red scales along the spine; the skin radiates retained volcanic heat.
- **Signature:** Heat shimmer distorts the Asp as it approaches, making it unreliable to target from range. Paired Asps coordinate their strikes, both moving to the same target simultaneously to overwhelm defense.
- **Goal:** Isolate a single party member from the group, strike together, and inject venom to create an ongoing threat. A poisoned prey is marked; the pair will pursue it across terrain to capitalize on the delayed venom damage.
- **Fear:** Sudden cold, separation from its hunting partner, exposure to sustained ranged pressure before it closes distance.
- **Counterplay:** Force the pair to split (damage one at range, separate them); use area denial or obstacles to disrupt the coordinated approach; cast hold or restraining spells to prevent the setup; use water or cold to trigger its retreat instinct; or silence the "hiss" that coordinates the pair.
- **Proof (observable tell):** The shimmer is visible at range (wavy heat distortion). As the Asp closes, the pair begins a synchronized hiss—a coordinated rattling sound that signals an incoming simultaneous strike. If separated, each Asp loses the bonus, making them individually less dangerous and more cautious.

---

## Role, Rank, and Decision Loop

**Primary role:** Ambusher (enters from cover, strikes on approach, reorients for pair coordination)

**Rank/CR:** Standard (not elite, not solo) — designed as a pair unit

**Encounter job:** Establish danger through coordinated ambush; create split decisions (focus one Asp or spread damage?); force party into a position where staying grouped is punished and splitting is exposed to venom isolation.

**Decision loop for each signature feature:**

**Heat Shimmer (trait)**
- **Tell:** Wavy heat distortion visible at 60+ feet; shimmer dissipates as Asp closes to 30 feet
- **Threat:** Ranged attacks against shimmer-obscured Asp suffer disadvantage; incentivizes melee response or area effects
- **Responses:** (1) Approach the Asp to within 30 feet to lose the shimmer penalty; (2) Use AOE spell or weapon to bypass ranged disadvantage; (3) Ignore ranged attacks and let the Asp close for melee
- **Payoff:** Asp trades range advantage for position advantage; if the party chooses to approach, the Asp has closed distance for its pair strike. If the party uses AOE, it limits action economy for setup. If the party ignores ranged attacks, the Asp applies venom on turn 2 with a coordinated setup.

**Coordinated Strike (trait)**
- **Tell:** Synchronized hiss from both Asps; simultaneous movement toward one target
- **Threat:** If both Asps target the same creature and both hit, they gain advantage on their next attack. The target is overwhelmed (4 strikes in rapid succession if both pair actions activate)
- **Responses:** (1) Kill or disable one Asp before the pair strike lands; (2) Have the target use reaction to move away or block with shield; (3) Position a defender between the target and the Asps; (4) Use crowd control to prevent the coordinated approach
- **Payoff:** Pair gains advantage (higher hit rate, more venom applications), but if the party prevents coordination, the Asps lose the bonus and become much less threatening (standard attacks instead of setup advantage)

**Venom Strike (action)**
- **Tell:** Asp lunges with open mouth, fangs glistening
- **Threat:** On a hit, the target does not take venom damage immediately; instead, it takes poison damage at the start of its next turn (9 poison) unless it makes a DC 14 Constitution saving throw. The delayed application means the party cannot benefit from immediate healing surge—the poison comes *after* the turn ends. Stacked venom from both Asps means two poison damage rolls tracking in parallel.
- **Responses:** (1) Use a Constitution saving throw to resist (high-WIS or high-CON characters can try); (2) Cast Lesser Restoration before the poison triggers; (3) Use a potion or other healing action to offset the poison damage once it arrives; (4) Target the Asp's mobility or defense to prevent the setup turn
- **Payoff:** Asp creates a two-turn decision loop. If the poison lands, the party must budget a bonus action or reaction to recover, or take the damage and lose an action. If the party spends the action to resist, the Asp buys a round of setup. The threat scales with venom stacking—two poisoned targets means two damage rolls competing for the party's resources.

---

## Combat Role Summary

The Lava Asp is a **skirmisher/ambusher hybrid**:
- Enters from cover using terrain (lava tubes, heat vents, volcanic breaks)
- Approaches at range under shimmer concealment (ranged pressure falls off)
- Pairs coordinate to focus one target, creating overwhelming action economy in a single-turn window
- Venom creates a two-turn resource-tracking loop that forces party choices
- Movement is good (40 ft.) but not exceptional; the Asp relies on positioning and pair bonus, not pure mobility

---

## Stat Block

```
LAVA ASP
Small monstrosity, unaligned

Armor Class 15 (natural armor, heat shimmer)
Hit Points 82 (11d8 + 33)
Speed 40 ft., climb 30 ft.

| STR | DEX | CON | INT | WIS | CHA |
|---|---|---|---|---|---|
| 14 (+2) | 16 (+3) | 16 (+3) | 2 (−4) | 12 (+1) | 5 (−3) |

Saving Throws CON +5
Skills Perception +4, Stealth +5
Senses darkvision 60 ft., passive Perception 14
Languages —
Challenge 5 (1,800 XP)  PB +3

___

### Traits

**Heat Shimmer.** While the Asp is more than 30 feet away from the party, the air around it shimmers with retained heat. A creature that attacks the Asp with a ranged weapon attack while the Asp is outside 30 feet makes the attack roll with disadvantage.

**Thermal Vision.** The Asp can see through magical darkness and nonmagical obscuration caused by volcanic ash, smoke, or steam as if that area were lightly obscured. Heat sources (including warm-blooded creatures) are visible to the Asp even through solid volcanic rock up to 60 feet away.

**Pack Coordination.** If another lava Asp within 60 feet of this one targets the same creature that this Asp targets with an attack on the same turn, this Asp has advantage on its attack roll against that creature.

**Cold Sensitivity.** If the Asp takes cold damage, it has disadvantage on attack rolls until the end of its next turn.

___

### Actions

**Multiattack.** The Asp makes two Fang Strikes.

**Fang Strike.** *Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 10 (2d6 + 3) piercing damage, and the target must make a DC 14 Constitution saving throw. On a failed save, the target is **poisoned**. The poison does not deal damage immediately; instead, at the start of the target's next turn, the poisoned creature takes 9 (2d8) poison damage, and the condition ends. A creature can be poisoned by multiple venom strikes; each tracks separately and deals damage on its next turn.

**Venom Spray (Recharge 5–6).** *Ranged Weapon Attack:* +6 to hit, range 15/30 ft., one target. *Hit:* 13 (2d8 + 3) poison damage, and the target makes a DC 14 Constitution saving throw. On a failed save, the target is poisoned as described in Fang Strike (poison damage at the start of the target's next turn).

___

### Reactions

**Thermal Coil.** *Trigger:* The Asp is hit by an attack while it is at least 30 feet away from the attacker. *Response:* The Asp moves up to half its speed without provoking opportunity attacks. This movement is silent and difficult to track in the shimmering heat.

```

---

## Three-Round Offense and Defense Audit

### Offense Script (Pair Scenario, Full Coordination)

**Round 1 (Setup and approach)**
- Both Asps are 60+ feet away, hidden in volcanic breaks or lava-tube openings
- Shimmer is visible; ranged attacks against them suffer disadvantage
- Party must decide: approach the shimmering heat sources or use area effects
- Round 1 action: If Asps approach (40 ft. movement), both move to 30 feet away from the party's front line (shimmer fades)
- Attacks made: None; setup round
- Expected output: Party is forced to commit to positioning or area effect; no damage is dealt yet

**Round 2 (Coordinated pair strike)**
- Both Asps are within 30 feet and in melee range of one target (typically the front-line defender)
- Both target the same creature
- Asp A: Multiattack (2× Fang Strike) at advantage (pack coordination bonus)
  - Attack 1: +6 to hit with advantage → expect ~75% hit rate = 7.5 damage expected; if hit, venom triggers DC 14 CON save (expect ~40% failure) = +3.6 venom tracking expected
  - Attack 2: +6 to hit with advantage → 7.5 damage expected; venom tracking +3.6 expected
  - Total round 2 A: ~15 damage + 7.2 venom tracking
- Asp B: Identical (mirrors Asp A)
  - Total round 2 B: ~15 damage + 7.2 venom tracking
- **Round 2 pair total: ~30 damage + 14.4 venom tracking (2–4 poison stacks likely)**
- Counterplay windows: Defender uses shield or dodge; ranged character focuses fire on one Asp; caster uses hold/restrain; spell uses area effect to disrupt pairing

**Round 3 (Persistence and recharge)**
- One Asp likely wounded or dead (party focus fire on one); surviving Asp(s) continue or retreat
- If Asp survives: Multiattack again (without advantage if pair is broken)
  - Attack 1: +6 to hit → 5 damage expected
  - Attack 2: +6 to hit → 5 damage expected
  - Possibly Venom Spray if recharged (DC 14 CON save, 6.5 damage + venom tracking)
- Expected round 3 output: 10–15 damage + venom tracking
- Venom from round 2 triggers at start of affected creatures' turns, creating a 9-damage pulse per poisoned creature

### Three-Round Total (Pair, Scripted Scenario)
- Round 1: 0 damage (approach)
- Round 2: 30 damage + multiple poison stacks
- Round 3: 10–15 damage + venom triggers (9 per poisoned target)
- **Subtotal: 40–45 damage across rounds + 9–27 poison damage triggering over turns 3–4**
- **If party kills one Asp in round 2:** Surviving Asp loses coordination bonus, drops to ~10–15 DPR base; no pair advantage in subsequent rounds

### Comparison with Peers
- **Wyvern (CR 6)** at full aggression: 36 DPR (melee + tail strike + tail recharge)
- **Lava Asp pair**: 39 average DPR over 3 rounds (accounting for setup, pair bonus, venom tracking)
- **Solo Lava Asp**: 14 DPR base (two strikes at standard hit rate, no bonus) → falls below Wyvern
- **Verdict:** Pair matches Wyvern tier; solo Asp is below CR 5 and benefits from pair bonus to reach it. **This is intentional**; an encounter with two Asps separated is harder than with one; facing them paired is the design challenge.

### Defense Audit

**AC and avoidance:**
- AC 15 is standard for CR 5 (matches Wyvern peer)
- Heat Shimmer provides ranged disadvantage as a form of defense but no flat AC boost
- Thermal Coil reaction allows 20-foot repositioning, which extends the shimmer advantage into round 2

**Hit Points:**
- 82 HP = 15 + (15 × 5) baseline formula
- Effective HP: Standard (no resistance, no regeneration, no healing)
- Against a 5-character party dealing 15–20 damage per round on average: survives 4–5 rounds solo, 3–4 rounds under pair focus fire

**Saves:**
- CON +5 (strong); poison DC 14 is appropriate for CR 5
- Weak save coverage otherwise (INT, WIS, CHA unbosted); party casters with control can target these

**Cold Sensitivity:**
- Not an immunity or broad vulnerability; cold damage triggers disadvantage on attacks (one round)
- Provides a player counterplay (use cold spells to reduce offense) without invalidating the Asp

**Movement and escape:**
- 40 ft. speed is good but not exceptional; matches Giant Scorpion, below Wyvern
- Climb 30 ft. enables vertical positioning and escape into lava tubes
- Thermal Coil reaction gives silent repositioning once per reaction

**Damage spread:**
- 2d6 + 3 per melee strike = 10 average (reasonable for CR 5 melee)
- Venom Spray 2d8 + 3 = 13 average (reasonable for ranged, with venom setup)
- No single attack is devastating; party is not one-shot at any tier

**Party bypass:**
- No immunity or broad resistance to common damage types
- No feature that invalidates an entire party tactic (save-based control still works; area effects still work; ranged advantage comes at cost of shimmer disadvantage, not impossibility)

### Conclusion
The Lava Asp is defensively in line with CR 5 peers. The shimmer defense trades durability for positioning advantage. Venom creates a resource-tracking loop but not a turn-deletion condition. The pair bonus is powerful but fragile—killing one Asp collapses it. **No major concerns for balance.**

---

## Encounter Integration

### Allies and Terrain
- **Opening position:** Both Asps hidden in lava-tube openings or volcanic vents, 60–80 feet from the party's approach
- **Terrain:** Volcanic islands feature broken ground, steam vents, lava flows that are difficult terrain or hazardous
  - Lava pools: 2d6 fire damage per round if a creature enters or starts its turn there (standard hazard)
  - Volcanic ash clouds: 20-foot visibility, creatures within have concealment (Asps' Thermal Vision negates this for them)
  - High-heat thermal vents: The shimmer effect is more pronounced; party's first ranged attacks have disadvantage naturally before the Asp's trait even applies
- **Lightning rods:** None; the Asps are the only mobile threats. Static hazards (lava, vents) provide terrain-based choices

### Reinforcements and Escape
- **First-round retreat:** If one Asp is killed in round 1 (unlikely) or both are driven below 30 HP before round 2, the pair retreats into lava tubes (difficult to pursue; Asps climb 30 ft. and move through narrow steam vents)
- **Reinforcements:** A third juvenile Asp (CR 1/2, 10 HP) could join from a side vent if the party is winning decisively. This extends the encounter but does not create an unwinnable scenario for a competent party
- **Failure state:** Both Asps driven to 0 HP or separated by 120+ feet and one killed. The survivor retreats and does not return (lava Asp territories are personal; a widowed Asp leaves the island)

### Tells and Signs
- **Pre-encounter:** Party notices heat shimmer in the distance; ground is warm. Scorched fur, bones of prey animals with fang marks, sulfur smell concentrated around lava-tube openings
- **During encounter:** Synchronized hiss from the pair before coordinated movement; rustling as both Asps shift position to same target
- **After:** Heat-blackened stone, shed scales (dark obsidian and rust), venom residue (smells acidic and hot)

---

## Running Notes

### Counterplay and Party Answers
1. **Separate the pair:** Focus fire on one Asp before both are in melee range. Each round one Asp stays alive solo without the other, the coordination bonus is lost. A single Asp drops to standard actions and becomes vulnerable.
2. **Force range:** Use spells or abilities that keep the Asps at distance. Push them back (Thunderwave, Eldritch Blast with Repelling Blast) to reset the shimmer advantage.
3. **Area effects:** Spike Growth, Fireball, or Chain Lightning bypass the shimmer disadvantage and can catch both Asps if they're coordinated
4. **Cold offense:** Any cold damage triggers Cold Sensitivity, giving the next attack disadvantage. This is a strong counter if the party has cold source
5. **Turn denial:** Hold Person, Tasha's Mind Whip, or similar control effects prevent setup and reset pair coordination
6. **Escape and distance:** Movement-focused characters (monks, rogues with mobility) can deny the coordinated approach by spreading out; isolated prey is still prey, but two Asps at distance are not as threatening as two Asps in melee
7. **Healing and resource tracking:** Track venom stacks on each character; remember that poison damage comes at the start of the affected creature's turn, not immediately. This creates decision moments around healing surge timing

### Revision Knobs

**If the Asp is too weak:**
- Add a second Venom Spray recharge (instead of 5–6, make it 5 for faster reload)
- Increase Fang Strike damage to 2d8 + 3 (13 average instead of 10)
- Add a trait: **Coordinated Venom**: If both Asps hit the same target with poison on the same turn, the poison damage increases to 13 (3d8) instead of 9 (2d8)

**If the pair bonus is too strong:**
- Remove Pack Coordination entirely; each Asp is independent, and the pair threat comes only from simultaneous action economy
- Change Pack Coordination to: "This Asp has advantage on attack rolls against a creature that is within 5 feet of another lava Asp" (proximity bonus instead of same-target bonus)
- Reduce the venom damage to 6 (1d12) instead of 9 to lower the stacked poison threat

**If the shimmer defense trivializes ranged damage:**
- Change Heat Shimmer to grant the Asp +2 AC (partial cover) instead of disadvantage; less swingy, more transparent
- Remove shimmer entirely from ranged attacks; instead, make shimmer grant the Asp resistance to fire damage (thematic, not a ranged defense)
- Keep the shimmer mechanic but reduce its range: disadvantage only at 60+ feet, not 30+ feet

**If venom tracking is confusing in play:**
- Simplify to immediate venom damage: "On a hit, the target takes 4 poison damage immediately plus an additional 5 poison damage at the start of its next turn" (splits the damage but applies both)
- Remove the saving throw; venom always takes effect (harsher but simpler)

---

## Summary

The Lava Asp is a CR 5 skirmisher/ambusher designed for volcanic terrain. Its signature is the heat shimmer approach (ranged disadvantage during setup) paired with coordinated melee strikes (advantage when paired). Venom creates a two-turn resource-tracking loop. Pair scaling (strong together, weaker solo) incentivizes party focus fire and pair separation. The design is defensively in line with Wyvern/Manticore peers; offense balances setup, coordination, and venom threats. Cold, area effects, and pair separation are clear counterplay paths.
