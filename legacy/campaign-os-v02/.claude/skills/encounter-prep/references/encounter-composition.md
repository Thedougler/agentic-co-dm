# Encounter composition and terrain

Load when choosing how many/what shape of enemies to field, what the
battlefield itself needs, or a standard-baseline difficulty number before
`combat-profiles`' empirical Effective CR Band exists. This is the
canonical home for combining creatures, the party, and terrain into a
fight — `.claude/skills/draft-content/references/monster.md` designs one creature's own stat block and cites
this file back for anything about the fight around it (composition,
tiers-of-play calibration, boss/minion pairing all moved here from
`vault/refs/vault/monster/references/cr-design.md`, condensed from the
same external sources it originally cited).

---

## 1. Composition shapes

Justification: pick the *shape* of the fight before picking specific
monsters — solo, matched group, or boss+minions each read differently at
the table and call for different terrain/tactics. Condensed from
`vault/refs/quick-encounter-building.md`.

Ratios by character level (approximate — a fast sanity check, not a
substitute for Step 5, below):

- **1st level.** CR 0–¼: one monster per character. CR ½: one per two
  characters. CR 1: one per four characters.
- **2nd–4th level.** CR = 1/10 level: two monsters per character. CR =
  ¼ level: one per character. CR = ½ level: one per two characters. CR =
  level: one per four characters.
- **5th–20th level.** CR = 1/10 level: four monsters per character. CR =
  ¼ level: two per character. CR = ½ level: one per character. CR = ¾
  level: one per two characters. CR = level + 3: one per four characters.

For an exact CR breakdown of a **boss+minions** or **boss+lieutenants+
minions** shape at a specific party size and level, consult
`vault/refs/vault/monster/references/combinations.md`'s full tables (four/five/six-character
parties, levels 1–20, hard-challenge baseline) rather than eyeballing it —
scale the whole table ±1–2 levels for deadly, −2 for medium, −4 for easy
(same file).

## 2. Creature-type cap

Justification: `vault/refs/combat-encounter-checklist.md` — more than three
distinct creature *types* in one fight is hard to manage at the table.
Two or three types that work well together (a bruiser up front, artillery
behind) reads as a complex, climactic battle; four or more reads as
clutter. For a bigger set-piece, use **waves** of the same 2–3 types
instead of adding a fourth type all at once.

## 3. Set-piece checklist

Justification: for a big, self-contained combat encounter or boss fight,
run this nine-element menu — `vault/refs/combat-encounter-checklist.md`'s own
framing: **no battle needs all of these**, pick what fits.

- **Interesting monsters** — 2–3 creature types that complement each
  other (§ 2, above).
- **A fantastic location** — a room/space with real shape, not an empty
  box; small enough that every PC reaches the interesting part within two
  moves.
- **Zone-wide effects** — one ongoing effect touching everyone in the
  fight (an unholy aura halving healing, periodic lightning strikes, a
  thick fog past 30 ft.). Avoid effects that are simply annoying (constant
  prone) or that lopsidedly punish one class (disadvantage on attacks
  hurts martials more; limited visibility hurts ranged attackers).
- **Traps and hazards** — a few, not everywhere; make them matter (in the
  path of the fight, not off to the side) and let the party spring them on
  enemies too, not just suffer them.
- **Advantageous positions** — high ground, an arcane circle, anywhere
  worth fighting over — turns the room into a "king of the hill" contest.
- **Interactive objects** — things a PC can physically use: a toppleable
  statue, a chandelier to swing from, a lever, a crane, a brazier to tip.
- **Cover** — broken terrain to duck behind; make sure the players know
  it's there and what it does.
- **Difficult or fantastic terrain** — a specific area with a specific
  effect (a crumbling bridge, slippery oiled floor, a gas-belching bog) —
  not a zone-wide effect, localized instead.
- **A goal** — what "winning" requires beyond killing everyone, if
  anything (stop the ritual, recover the artifact, activate the gateway).
  Lands in this skill's `objective` Toy field.

## 4. Boss/environment/minion pairing

Justification: a boss rarely fights alone — matching it to a plausible
environment and minion type is faster than inventing both from scratch.
Sample rows, condensed from `.claude/skills/draft-content/references/monster.md`'s own prior citation of this
material; extend by analogy for a boss CR not listed.

| Boss CR | Boss archetype | Environment | Minion archetype |
|---|---|---|---|
| 1–2 | Goblin/bandit/cultist leader | Caves, ruins, sewers, cities | Goblins, bandits, cultists, thugs |
| 3–5 | [[ogre\|Ogre]]/hag/giant | Ruins, swamps, mountains | Orcs, bullywugs, lesser giants |
| 6–9 | Hobgoblin warlord, mage, oni | Keeps, towers, cities | Hobgoblins, animated constructs, imps |
| 10–13 | [[aboleth\|Aboleth]], efreeti, archmage | Caverns, deserts, towers | Cultists, elementals, golems |
| 14–17 | Adult dragon, marilith, death knight | Terrain matching type/theme | Elementals, lesser demons/undead |
| 19+ | [[balor\|Balor]], lich, pit fiend | Lower Planes, crypts, ruins | Mid-CR demons/devils/undead |

## 5. Monsters and the tiers of play

Justification: the CR number says what a creature's stats look like;
this says how that same CR *plays* against a party at a given level
bracket — a distinct axis from raw CR math. Condensed from
`vault/refs/vault/monster/references/tiers-of-play.md`. Cross-reference
`combat-calibration.md` — this is the standard-baseline layer; that
file's empirical Effective CR Band read is the mandatory adjustment on
top of it (Hard Rule 4).

- **1st level.** Characters are fragile — a CR 1/2 creature can crit-kill
  outright. Stay at or below CR 1/4 for anything but a lone boss (CR 1/2
  at most), and lean toward fewer monsters than characters.
- **2nd–4th level.** The easiest bracket to calibrate; characters handle
  CR 1/8–1 in groups, CR 2–3 in pairs, up to ~CR 5 solo.
- **5th–10th level (the power spike).** Extra attacks, Action Surge,
  *fireball*-tier spells, and save-or-suck effects arrive — a single
  nonlegendary creature can no longer be trusted to challenge a group
  alone; a well-placed AoE or control spell can end a fight outright.
  This is exactly the bracket `running-the-encounter.md`'s difficulty
  dials and running-hordes tools are built for. Complexity matters more
  than CR alone from here up.
- **11th–16th level.** Characters are superheroes with wide power
  variance between builds — battles take longer to run, and a boss
  fought alone (no lieutenants) is usually too easy. Published high-CR
  monsters can under-deal damage for their CR at this bracket; watch DPR
  against actual party HP, not just the CR table.
- **17th–20th level.** Near-godlike; a monster not customized for this
  specific party is rarely a real threat regardless of CR. Expect longer
  fights and heavier prep per encounter at this bracket.

## 6. Zone-based terrain definition

Justification: defining terrain as a handful of named zones is faster to
prep and run than a precise grid, and reads better in prose on a wiki
page. Condensed from `vault/refs/zone-based-combat.md`; § Zone movement in
`running-the-encounter.md` covers how movement/range/opportunity attacks
actually work once play starts — this section is the prep-time step only.

- Define **1–3 zones**, each roughly 25 ft. on a side (can be any size).
  Give each an evocative one-line description — "a crumbling bridge over
  a bottomless gorge," "a blood-covered altar" — not a dimension-and-
  furniture inventory.
- For each zone, name what's interactable in it: cover, elevation, a
  hazard, an interactive object (§ 3, above).
- Most encounters need one zone. Reach for two or more only for a real
  set-piece battle where the party's expected to move between distinct
  spaces mid-fight.

## 7. Gameplay Toolbox — combat features and traps

Justification: `vault/refs/gameplay-toolbox.md`'s own Combat Encounters and Traps
sections, unclaimed elsewhere in this repo (`.claude/skills/draft-content/references/location.md` only cites
this file's § Travel Pace).

**Combat-encounter features** that reward positioning and movement:

- **Changes in elevation** — crate stacks, ledges, balconies — reward
  climbing, flying, jumping, teleporting.
- **Defensive positions** — enemies in hard-to-reach or fortified spots
  force ranged characters to move to engage.
- **Mixed monster groups** — different types working together (like a
  party of different classes) read as a more coordinated, tougher force
  than the same total CR in one type.
- **Reasons to move** — a chandelier, a keg of oil, a rolling-stone trap —
  anything that gives both sides motive to reposition mid-fight.

**Trap-writing shape**, condensed from the same file's example traps —
use this shape for any Terrain hazard that's a genuine trap rather than
passive difficult terrain: name it, then state its *trigger* (pressure
plate, trip wire, wrong key), *duration* (instantaneous, until disarmed,
resets), *effect* (save DC + damage, scaled to the party's level band),
and *detect/disarm* (the check and DC that finds and defuses it). Traps
work best sparingly — too many make players overcautious and slow the
table down; the best ones are either a fast distraction skilled
characters shrug off, or a genuine puzzle. Never undetectable and
inescapable.

## 8. Alternate XP-budget cross-check

Justification: a second, newer concrete baseline alongside § 9's Lazy
Encounter Benchmark — `vault/refs/gameplay-toolbox.md`'s SRD 2024 XP Budget table.
Use either, or both as a sanity cross-check against each other; neither
replaces `combat-calibration.md`'s empirical read once party data exists.

1. **Pick a difficulty** — Low (characters win with no casualties, one or
   two scary moments), Moderate (could go badly without healing, slim
   death chance), or High (could be lethal, needs real tactics/luck).
2. **Look up the per-character XP budget** for the party's level and
   chosen difficulty, then multiply by party size. (Full Low/Moderate/
   High-by-level table: `vault/refs/gameplay-toolbox.md` § Combat Encounter
   Difficulty.)
3. **Spend the budget** on creatures by their stat block's XP value,
   without going over (a small unspent remainder is fine).

Troubleshooting, same source: more than 2 creatures per character raises
lucky-streak risk (include some fragile ones); more than 2–3 distinct
stat blocks in one fight is hard to run (§ 2, above); a creature with CR
higher than party level can one-shot a low-level character even in an
otherwise "balanced" budget — check that specifically.

## 9. Lazy Encounter Benchmark

Justification: a single mental-math formula for a fast deadliness
gut-check, faster than the full XP-budget table above. Condensed from
`vault/refs/lazy-encounter-benchmark.md` and
`vault/refs/lazy-combat-encounter-building.md`.

- **Formula.** An encounter may be deadly if total monster CR exceeds ¼
  of total character levels (characters 1st–4th level), or ½ of total
  character levels (5th level+). A single monster may be deadly on its
  own if its CR ≥ average character level (or ×1.5 that level, 5th+).
- **Average character HP**, for a fast damage-vs-survivability check on
  any monster/trap/hazard: `(level × 7) + 3`.
- **Scaling past 10th level** (optional, only if encounters built with
  the base formula are consistently too easy): ¾ of total levels at
  11th–16th, equal to total levels at 17th+.
- This is a warning gauge, not a hard cap — circumstances (numbers favor
  the party, terrain favors the party, monsters come in waves, the party
  doesn't need to eliminate every foe) regularly make an "in the red"
  encounter play easier than the number suggests, and the reverse
  (monsters have position/terrain advantage, party is already worn down)
  makes an under-budget encounter play harder.

## 10. Design philosophy

Justification: closing rider — `.claude/skills/composing-beats/references/composition.md` § Encounters,
the six things a good encounter does regardless of composition math:

- Serves a story purpose — never a pure roadblock.
- Comes in variety — combat, social, physical/intellectual challenge,
  puzzle — not combat by default.
- Leaves room for a creative solution the DM didn't script.
- Difficulty varies deliberately, shaping session pacing (a string of
  identical-difficulty fights reads as flat).
- Is easy to run — if it needs a lookup table mid-round, it's over-built.
- Is designed to actually be played, not just to look good on the page.
