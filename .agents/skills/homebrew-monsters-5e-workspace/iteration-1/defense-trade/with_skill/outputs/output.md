# Defense Audit: Aruhe Guardian

## Path and Assumptions

**Audit scope:** Defense stack review for homebrew Aruhe guardian.

**Input brief:** AC 18, 200 HP, resistance to bludgeoning/piercing/slashing (BPS), regeneration 10, +9 to all saves, 30 ft. teleport.

**Assumptions:**
- Guardian is an elite/solo rank (likely CR 12–14 based on HP and AC)
- +9 to all saves is a flat bonus (not ability-based saves)
- 30 ft. teleport has no documented frequency, range limit, or resource cost
- Regeneration 10 applies every turn without trigger/condition stated
- No encounter context (allies, terrain, phase, lightning rod) provided

---

## Peer Calibration

**Numerical peer (CR 13):** ~210 HP, AC 17–19, +4–5 PB
- Expected: high AC OR high saves, not both at maximum
- Expected: one weakness (low damage, low mobility, high target number)

**Role peer:** Elite defender/tank
- Expected: high durability trades for reduced damage output or mobility
- Expected: conditional triggers on strong defenses, not blanket stacking

**Mechanic peer:** Resistance + regeneration on same creature (rare)
- Example pattern: Dragon has high AC (18–20) OR high HP (200+), rarely both with regeneration
- Regeneration typically paired with limited teleport (1/day) or narrow escape (specific condition)

**Shared pattern across peers:**
- Stacking defense mechanics (high AC + high HP + broad resistance + regeneration + high saves + escape) is unusual; when present, the creature lacks one of: damage output, action economy, area control, or has a clear party bypass

**Deliberate deviation noted:** Guardian appears designed to be nearly unkillable through attrition; no bypass or party target mentioned.

---

## Defense Audit Checklist

| Defense axis | Value | Audit finding | Risk level |
|---|---|---|---|
| **Armor Class** | 18 | Appropriate for CR 13; matches peer range | PASS |
| **Hit Points** | 200 | On-target for CR 13; normal pool | PASS |
| **AC trade cost** | None specified | High AC should trade HP, damage, or mobility | **CONCERN** |
| **Effective HP (BPS resist)** | 400 equivalent | Doubles effective durability vs common weapon damage | **CONCERN** |
| **Saving throw** | +9 to all | Extremely high; most save-based controls fail (DC 15 save is ~40% pass rate vs +9 with common stat +0 to +3 mod) | **FAIL** |
| **Save trade cost** | None specified | High saves at +9 should trade AC, HP, or action economy | **FAIL** |
| **Regeneration 10** | Per turn | Adds 10 HP/turn; meaningful durability against normal DPR (50–70); no resource cost stated | **CONCERN** |
| **Regen + resist stack** | Both active | Combines 400 effective HP + 10 HP/turn reset; synergy not broken | **FAIL** |
| **Teleport (30 ft.)** | Unlimited frequency? | No recharge/1/day/action cost stated; enables escape/repositioning without risk | **CONCERN** |
| **Teleport tell** | None stated | No visible telegraph or condition; party cannot anticipate or deny | **FAIL** |
| **Party bypass** | None identified | No save/check to make teleport harder, no limited range, no interruption | **FAIL** |
| **Overall stack** | AC+HP+resist+regen+saves+escape | Six defensive layers with no tradeoff; violates chassis rule #3 | **FAIL** |

---

## Effective HP Modeling

**Against common party damage (weapon-based, no magic penalty):**
- Incoming DPR (baseline): 50–70 damage/round (weapon attacks)
- Effective HP with 3 BPS resistance: 200 HP × 2 = **400 HP equivalent**
- With regeneration 10/turn: adds **effective 1–2 extra rounds** vs normal DPR
- **Total durability:** ~6–8 rounds before incapacitation (vs 2–4 for a normal AC 18 / 200 HP creature)

**Against save-based damage (spell/breath):**
- Incoming DC: typically 15–16 (party spell save)
- Guardian save: +9 to all
- Success probability: ~85–90% (nearly automatic success)
- **Result:** Party spellcasters have minimal control/damage path; forced to rely on weapon attacks only

**Against mixed damage:**
- Nonmagical weapon: 400 effective HP
- Fire/cold/poison/etc (no resistance): 200 HP
- Condition attempts: +9 saves block most (DC 15–16 range)
- **Problem:** Party forced down one narrow path (magic damage type that breaks resistance)

---

## Defense Audit Findings

### Critical Issues (Trade Rule Violations)

**1. Stacked defenses without cost**
- Rule violation: "If AC rises above peers, reduce HP, damage, control, or endurance."
- Current state: AC 18 (at peer max) + 200 HP (at peer max) + BPS resist (no cost) + regeneration (no cost) + +9 saves (no cost) + teleport (no cost)
- **Fix required:** Remove or narrow at least one axis

**2. +9 to all saves is over-tuned**
- Comparison: CR 13 peers typically have +4–5 PB and ability-based saves (Dex +2 to +4, Wis +1 to +3)
- Guardian at +9 flat: nearly guarantees save success against DC 15–16 effects
- **Problem:** Turns off charm, stun, hold, poison, frightened, and other party toolkit
- **Fix required:** Lower saves to +5–6 (peer-aligned) or make saves ability-based (Wis +5, etc.)

**3. Regeneration + resistance stack without bypass**
- Combined effect: Against nonmagical weapons, the creature heals faster than party deals damage in many rounds
- **Problem:** Creates attrition spiral where party loses before guardian takes real damage
- **Bypass:** Party must identify and exploit the one damage type that does not trigger resistance, or party must spike damage hard
- **Fix required:** Add a save/check to deny regeneration, or add a clear tell (e.g., "regeneration stops if the creature takes [damage type] damage this turn")

**4. 30 ft. teleport with no stated limits**
- No documented cost, recharge, or frequency
- No save or check to interrupt
- **Problem:** Guardian can escape from any corner or control setup without party recourse
- **Fix required:** Make teleport reactive (only when threatened), 1/turn, Recharge 5–6, or add a DC to resist/interrupt

---

## Revision Knobs (Smallest Fix per Issue)

### Option A: Narrow the defense stack (preferred)
- **Change:** Remove regeneration OR narrow resistance to one type (only slashing, or only bludgeoning)
- **Effect:** Reduces effective HP from ~400 back to 200–270; keeps party damage on-task
- **Tradeoff:** Guardian remains very durable but beatable in 4–5 rounds vs 6–8
- **Player response:** Damage output choices matter again

### Option B: Trade saves for another axis
- **Change:** Reduce saves to +5 (peer-aligned PB at CR 13); allow party spellcasters to land control
- **Effect:** Charm/stun/hold now land 30–40% of the time (DC 15 vs +5); not guaranteed success
- **Tradeoff:** Guardian loses blanket immunity to control; party gains agency
- **Player response:** Spellcaster uses become meaningful; encounter opens up

### Option C: Add telegraph and cost to teleport
- **Change:** Teleport costs an action AND teleport only works within line of sight of a 60 ft. range; add tell: "its form flickers with [visual effect] before it vanishes"
- **Effect:** Party can deny teleport by denying actions (stun, hold), and can see where it goes (ambush prep)
- **Tradeoff:** Escape is still available but requires setup and party knowledge
- **Player response:** Party can position for follow-up and readiness becomes worthwhile

### Option D: Composite weak fix (minimal revision)
- **Change 1:** Narrow resistance to only slashing (iconic guardian material armor breaks piercing/bludgeoning)
- **Change 2:** Make +9 saves ability-based: Wis +5, others +3 (loses universality)
- **Change 3:** Teleport is 1/turn, Recharge 5–6
- **Effect:** Regeneration remains 10/turn; AC 18 remains; HP 200 remains. Effective HP drops to ~250 vs common damage. Party toolkit opens: spellcasters land control occasionally; strikers can pick damage type; guardian can escape once per 2 turns (reliably once/turn but not freely)
- **Three-round rerun:** 
  - Round 1: Guardian teleports into position (free escape setup)
  - Round 2: Party controls or damages; teleport is on recharge
  - Round 3: Party applies sustained pressure; regeneration is visible but not enough to close gap
  - **Estimated durability:** 5–6 rounds (manageable for CR 13 solo)

---

## Three-Round Offense/Defense Script (Revision D)

**Setup assumptions:**
- 4-person party, levels 13–14 (estimated)
- Mix of weapon strikers, spellcasters, healing support
- No preset terrain or allies

**Round 1:**
- Guardian: Teleports into optimal position (1/turn, recharge), opens combat
- Party: Sees flicker tell; initiates readied actions or takes turns
- **Damage taken:** ~15–20 HP (1–2 hit-and-runs; guardian reposition avoids action economy loss)
- **Save-based control:** Spellcaster attempts charm/hold (DC ~16 vs Wis +5); ~30% succeed

**Round 2:**
- Guardian: Teleport is on recharge; commits to direct action (attack/area/support)
- Party: Applies control or sustained damage; one caster lands effect; strikers converge
- **Cumulative damage:** ~50–60 HP total (regeneration 10 offsets ~1–2 rounds of medium pressure)
- **Effective state:** Guardian at 140–150 HP; not yet bloodied

**Round 3:**
- Guardian: Teleport recharged (Recharge 5–6, likely back); retreats or repositions as needed
- Party: Escalates damage; spellcasters maintain control pressure; strikers follow up
- **Cumulative damage:** ~90–110 HP total (regeneration adds 30 HP over 3 rounds)
- **Effective state:** Guardian at 100–110 HP; near bloodied; party has options

**Verdict:** Defense stack is beatable but very durable; party needs 6–8 rounds (within budget for solo CR 13). **Passes three-round test with Option D revisions.**

---

## Defense Stack Fix (Recommended)

### Option D: Composite Revision
Apply all three changes:

1. **Resistance:** Change to `Damage Resistances slashing` (loses piercing/bludgeoning)
2. **Saves:** Change to `Saving Throws Wisdom +5, others +3` (loses universality; keeps iconic wisdom)
3. **Teleport:** Add frequency: `Teleport (1/Turn, Recharge 5–6)`

**Revised Defense Summary:**
- AC 18 (unchanged)
- HP 200 (unchanged)
- Resistance slashing only (narrowed)
- Regeneration 10 (unchanged; now more visible as a weakness if party uses piercing/magic)
- Saves: Wis +5, others +3 (narrowed)
- Teleport 30 ft., 1/turn or Recharge 5–6 (limited)

**Effective HP (revised):**
- Slashing attacks: 200 HP (no resistance bonus)
- Piercing/bludgeoning: 200 HP (no resistance)
- Magic damage: 200 HP (no resistance)
- **Overall:** Drops from 400 equivalent down to 200–300 depending on party damage mix
- **Result:** Party damage choices matter; regeneration is visible weakness

**Party toolkit (revised):**
- Spellcasters: ~30–40% save success (Wis +5 vs DC 15–16); can land control sometimes
- Strikers: Piercing/bludgeoning and magic attacks deal full damage; action economy restored
- Damage types: Fire, cold, poison, etc., all deal full damage (no broad immunity)

---

## Counterplay and Tells

### Visible Tells (no hidden math)
- **Teleport tell:** "Its form flickers with [elemental effect]" before vanishing; party sees 30 ft. where it lands
- **Regeneration tell:** "Green/blue/silver light coalesces where its wounds close" — visible every round, not hidden
- **Slashing-only resistance:** No tell needed; narrate armor/hide response to specific damage type

### Party Answers
1. **Use piercing/bludgeoning/magic:** Party strikers use rapiers, warhammers, or cantrips; full damage applies
2. **Isolate and pressure:** Keep guardian from reaching allies or terrain advantage; prevent teleport setup
3. **Spike damage in phases:** Rogue + fighter + spellcaster on same target in succession; burst through 60+ DPR to outsace regen
4. **Control with Wis saves:** Wisdom-based saves (Hold Person, Command, etc.) now land ~30% of time; viable pickup
5. **Terrain leverage:** If arena has obstacles, party can force teleport range exhaustion or set up ambush zones

### Failure Consequences
- Party fails to ID that only slashing resists → waste rounds on ineffective type
- Party allows 3+ rounds of regeneration → guardian heals to full by design (intentional encounter timer)
- Party cannot land control → no casters use toolkit → less optimal but still beatable

---

## Final Audit Summary

### Before Revision
- **Status:** FAIL (defense stack violated trade rules; +9 saves untuned; no party bypass stated)
- **Risk:** Guardian unkillable in normal encounter; party forced attrition loss unless specific counter discovered

### After Revision (Option D)
- **Status:** PASS (defense narrowed to 1–2 axes per role; saves tuned; teleport limited; regeneration visible weakness)
- **Risk:** Beatable in 5–7 rounds with mixed party; encounter has clear answers
- **Complexity:** Moderate (three layers: resistance, saves, escape); manageable for DM to run

---

## Implementation Notes

**Stat block changes:**
```
Damage Resistances slashing  [was: bludgeoning, piercing, slashing]
Saving Throws Wisdom +5     [was: +9 to all]
               (others +3)   [was: +9 to all]
```

**Trait addition:**
```
Teleportation (1/Turn, Recharge 5–6). When the guardian takes damage or as a bonus action, 
it magically teleports to an unoccupied space it can see within 30 feet of it, leaving behind 
a flicker of [visual effect]. It can use this trait at most once per turn and recharges on a 
roll of 5 or 6 on a d6 at the start of its turn.
```

**Regeneration (unchanged; now functional weakness):**
```
Regeneration 10. The guardian regains 10 hit points at the start of its turn. 
This regeneration does not function if the guardian has taken slashing damage since its last turn.
```

**Encounter timer:** With regeneration and escape, assume encounter is designed to last 5–8 rounds before party victory or guardian retreat. If shorter, regeneration should not activate. If longer, add a phase or ally to maintain pressure.

---

## Conclusion

The original defense stack violates three trade rules:
1. High AC without reduced HP/damage
2. High saves without narrowed scope
3. Broad resistance + regeneration + escape without party bypass

**Recommended fix:** Apply Option D (narrow resistance, narrow saves to ability-based, add teleport frequency limit). This keeps the defensive fantasy (nearly unkillable guardian) while restoring player agency and party toolkit utility.

**With revision:** Guardian remains challenging (CR 13 appropriate), beatable in expected encounter window (5–7 rounds), and fun to fight (party choices matter, multiple valid answers, visible tells).
