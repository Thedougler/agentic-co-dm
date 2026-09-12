# dndsim Divergences

A **Divergence** (`CONTEXT.md`'s term) is an intentional behavior difference
between `dndsim` and the `utils/scripts/combat-sim/` engine it replaces —
never a bug fix or a regression; a known, measured difference that the
statistical parity harness (issue #52) is defined around. This file is
created by, and its entry format set by, issue #46.

## Entry format

Every entry is prose — the mechanism, what combat-sim does, what dndsim
does — followed by exactly one fenced ` ```divergence ` YAML block. The
fenced block is the **machine-readable marker** #52's parity tooling reads;
the prose above it is for a human, never parsed.

```yaml
id: <slug>                      # stable, matches this entry's heading anchor
category: simulate-time | validate-time
mechanism: <one line: what mechanic/field this is about>
old_behavior: <one line: what combat-sim does>
new_behavior: <one line: what dndsim does>
measured:
  seed: <int>                   # null if category is validate-time and no
  universes: <int>              # content in the fixed matchup set triggers
  round_cap: <int>              # the divergent path (see below)
  matchups:
    - id: <matchup id, same shape a future fixed-matchup-set file will use>
      a_win_rate_delta: <new - old, signed>
      b_win_rate_delta: <new - old, signed>
      a_tpk_rate_delta: <new - old, signed>   # a is "the party"; a dying is a TPK
      draw_rate_delta: <new - old, signed>
```

**How the parity harness identifies a Divergence-touching matchup**
(the acceptance criterion this entry format exists to satisfy): #52's fixed
matchup set assigns each matchup a stable `id` of the same
`<namespace>:combatant/<slug>-vs-<namespace>:combatant/<slug>` shape used
under `measured.matchups[].id` below. To exclude Divergence-touching
matchups from the statistical parity comparison and report them
separately, the harness parses every ` ```divergence ` block in this file
and builds one set: the union of `measured.matchups[].id` across every
entry with `category: simulate-time` (a `validate-time` entry never
touches a live matchup's win rate — see the two entries below). Any fixed
matchup whose id is in that set is skipped by the ordinary confidence-
interval comparison and reported with the recorded deltas instead of a
pass/fail. This is a static, curated membership list rather than a runtime
heuristic — deliberately: the fixed matchup set does not change between
runs, so which matchups a Divergence touches is a property of the
Divergence's content and the set, decided once at measurement time, not
re-derived per run.

---

## Death saves

**Mechanism.** A combatant reduced to 0 HP.

**combat-sim.** Declares a `--death-saves` CLI flag
(`utils/scripts/combat-sim/cli.mjs:94`) and threads it into simulation
options (`cli.mjs:326`), but never consults it anywhere: `lib/
simulator.mjs:225-227`'s `isDown` is bare `c.hp.current <= 0` (grepped:
`deathSaves` has 0 hits in any `lib/*.mjs` file). A combatant at 0 HP is
modeled as down-and-permanently-out, unconditionally, regardless of the
flag's value.

**dndsim.** Implements the PHB p.197 mechanic
(`src/dndsim/rules/dnd5e_2014/death_saves.py`): a combatant reduced to 0 HP
falls Down instead of losing outright and, on their turn in place of
attacking, rolls an unmodified d20 death saving throw — natural 1 counts
as two failures, 2-9 is one failure, 10-19 is one success, natural 20 is a
critical success (regain 1 HP, stand up conscious). Three accumulated
successes stabilizes them; three accumulated failures kills them. Taking
damage while Down — stable or not — inflicts one automatic failure and
clears a stabilized combatant's `stable` flag. Wired into
`rules/dnd5e_2014/combat.py`'s `run_combat`: a side is no longer "out" of
the fight at 0 HP, only once dead, so a fight can run longer than it would
under the bare-HP rule.

Not modeled (scope note, not a silent gap): a critical hit landing on a
Down combatant does not inflict two failures instead of one, and massive
damage (damage at or above HP maximum) does not trigger instant death.
Both need `AttackDamageMechanic` to expose its own crit/miss decision,
which it does not do today; each is a narrow, separately-scoped follow-up.

**Measured.** `scripts/measure_death_saves_divergence.py`, run at seed 1,
50,000 universes/matchup, round cap 20 — "old" reimplements combat-sim's
bare-HP rule directly (no death saves at all) against the same seeded RNG
stream, "new" calls `combat.run_combat` (the real, wired-in Divergence):

| Matchup | a_win Δ | b_win Δ | a_tpk (=b_win) Δ | draw Δ | mean rounds (new) |
|---|---|---|---|---|---|
| Perrin vs. Grung Skirmisher | -0.0021 | +0.0001 | +0.0001 | +0.0020 | 9.72 |
| Duelist vs. Bruiser | +0.0047 | -0.0049 | -0.0049 | +0.0002 | 6.57 |
| Paladin vs. Orc Champion | -0.0006 | -0.0089 | -0.0089 | +0.0095 | 10.83 |

The direction is not uniform — death saves both save a losing side (extra
rounds to stabilize and claw back) and cost the winning side round
efficiency (draws appear that never could before) — which is exactly why
this needs a measured run rather than a signed guess.

```divergence
id: death-saves
category: simulate-time
mechanism: a combatant reduced to 0 HP
old_behavior: 'bare hp<=0 == out of the fight, unconditionally (isDown, simulator.mjs:225-227)'
new_behavior: falls Down; rolls PHB death saves each turn until stable, dead, or awake (natural 20)
measured:
  seed: 1
  universes: 50000
  round_cap: 20
  matchups:
    - id: dnd5e_2014:combatant/perrin-vs-dnd5e_2014:combatant/grung-skirmisher
      a_win_rate_delta: -0.0021
      b_win_rate_delta: +0.0001
      a_tpk_rate_delta: +0.0001
      draw_rate_delta: +0.0020
    - id: dnd5e_2014:combatant/duelist-vs-dnd5e_2014:combatant/bruiser
      a_win_rate_delta: +0.0047
      b_win_rate_delta: -0.0049
      a_tpk_rate_delta: -0.0049
      draw_rate_delta: +0.0002
    - id: dnd5e_2014:combatant/paladin-vs-dnd5e_2014:combatant/orc-champion
      a_win_rate_delta: -0.0006
      b_win_rate_delta: -0.0089
      a_tpk_rate_delta: -0.0089
      draw_rate_delta: +0.0095
```

---

## Numeric-string coercion in `sim:` fields

**Mechanism.** A numeric `sim:` field (`dc`, `max`, `spend`,
`start_band`, and roughly 20 others) written as a quoted string in vault
YAML, e.g. `dc: "15"`.

**combat-sim.** Validates with `Number.isFinite("15")`, which is `false`
for a string regardless of its content, so a quoted numeric field is
rejected outright.

**dndsim.** Pydantic's lax mode coerces `"15"` to `15` for every numeric
`sim:` field, so the same content that combat-sim rejects parses cleanly.
dndsim is looser than the engine it replaces here — deliberately not
closed: `strict=True` on ~20 fields is a design call (accepting a quoted
number from hand-written YAML arguably is the better behavior), not a bug
fix, so it was surfaced (issue #46's parent comment) rather than taken
unilaterally.

**Measured.** Not applicable in the win/TPK-rate sense this file's format
otherwise uses: this is a validate-time acceptance difference, not a
runtime behavior difference two completed simulations could diverge on —
content combat-sim rejects here never reaches a simulation at all on that
side, so there is no pair of win rates to diff. No statblock, spell, or
combatant sheet in the current corpus expresses an affected field as a
quoted number (grepped; zero hits), so no fixed-matchup-set matchup is
touched today. Nothing to exclude at #52 time; `matchups: []` below is
empty for exactly that reason, and stays empty until content changes it.

```divergence
id: numeric-string-coercion
category: validate-time
mechanism: 'a quoted numeric sim: field (dc, max, spend, start_band, ~20 total)'
old_behavior: 'Number.isFinite("15") is false -> rejected'
new_behavior: 'pydantic lax mode coerces "15" -> 15 -> accepted'
measured:
  seed: null
  universes: null
  round_cap: null
  matchups: []
```

---

## Modifier dice-expression validation timing

**Mechanism.** A modifier-owned dice expression (`extra_damage.dice`,
`reroll_add.die`, `damage_reduction_reaction.dice`, `retaliate.damage.dice`,
`periodic_effect.dice`).

**combat-sim.** `validateModifier` only checks that the key is present and
is a string; the expression itself is parsed later, downstream, the first
time it is actually used (`engine.mjs`, `pc-profile.mjs`, `evolve.mjs`).

**dndsim.** Validates that the expression parses at the moment the `sim:`
block itself is read — before any simulation runs. This changes *when* a
bad expression is rejected (earlier), never *whether*; no real content is
affected, and it is the one deliberate site where dndsim is stricter than
the reference rather than looser
(`test_extra_damage_requires_a_parseable_dice_expression`).

**Measured.** Not applicable, for the same structural reason as the entry
above: this only changes the *timing* of a rejection both engines already
agree on, not any simulated outcome. No content in the current corpus
carries an unparseable modifier dice expression (grepped; zero hits), so
`matchups: []`.

```divergence
id: modifier-dice-validation-timing
category: validate-time
mechanism: a modifier-owned dice expression (extra_damage.dice, reroll_add.die, etc.)
old_behavior: parsed lazily, first use, deep in engine.mjs/pc-profile.mjs/evolve.mjs
new_behavior: 'parsed eagerly, at sim: block validation, before any simulation runs'
measured:
  seed: null
  universes: null
  round_cap: null
  matchups: []
```

---

## Fixed turn order in party-vs-party combat — RESOLVED

**Status.** Fixed by `95e887c2` ("per-universe rolled initiative replaces
fixed turn order") and merged into the golden snapshot by `d3cd3f2c`.
`run_combat` now rolls 1d20 + Dex modifier per combatant per universe at
encounter start (`_roll_initiative_order`, PHB p.189), vectorized across the
whole batch — the fixed party-then-enemy order described below no longer
exists in the code. Kept here as history: what the bug was, how it was
measured, and how it was ablated to confirm the cause. Not excluded from
parity CI (no live matchup carries this entry's id).

**Mechanism (historical).** The sequence combatants act in during an
encounter.

**combat-sim.** Rolls initiative per iteration
(`lib/simulator.mjs:263-269`: `c.initiative = rng.d20() + c.initiativeBonus`,
sorted descending, ties broken by `initiativeBonus`) — a different turn
order in every Monte-Carlo sample.

**dndsim (historical, pre-`95e887c2`).** `rules/dnd5e_2014/combat.py`'s
`run_combat` (issue #59) used one fixed turn order for the whole batch —
every party member's turn, declared order, then every enemy's, declared
order — identical across every universe. This followed from ADR-0011's
lockstep batching: one event dispatch advances every universe in the batch
at once, driven by one `build_round_timeline`/`Timeline`. `95e887c2` proved
that concern wrong in practice — per-universe rolled initiative was wired
without a distinct `Timeline` per universe, by masking each turn-slot's
window firing to the subset of universes occupying that slot
(`_turn_mask_from_event`) rather than by branching the `Timeline` itself.

**Measured.** Session 07 Phase 1's real matchup — `party` (5 real PC sheets)
vs. `otar-the-foul,minor-slaad:3` — surfaced this Divergence as the dominant
cause of a ~15-17-point party-win-rate gap against `combat-sim` that
survived three unrelated legendary-action fixes untouched. `sim-combat
party otar-the-foul,minor-slaad:3 --seed 1 --universes 2500 --round-cap 20`
through both engines, same real vault pages, same seed:

| Matchup | a_win Δ | a_tpk Δ | draw Δ |
|---|---|---|---|
| Party vs. Otar the Foul + 3 Minor Slaad | +0.361 | -0.361 | 0.000 |

(`combat-sim`: 62.8% party win / 37.2% TPK. `dndsim`: 98.9% party win / 1.1%
TPK.) Unlike the Lair-action entry's measurement, both runs read the real
pages directly (no `scripts/parity_matchups.py` flat-profile collapse), so
this delta isn't confounded by that other narrowing effect.

Directly ablating the mechanism inside `dndsim` alone (monkeypatching
`build_round_timeline`'s `turn_order` argument, same seed/statblocks,
nothing else changed) confirms fixed turn order — not Otar's Multiattack,
not the minor slaad's kit, not any unmodeled trait — drives nearly the
whole gap: reversing to enemies-act-first moves this exact matchup from
99.3%/0.7% to 84.0%/16.0% party-win/TPK — most of the way to combat-sim's
62.8%/37.2% on its own — and an interleaved one-PC-one-enemy order lands at
92.7%/7.3% in between. The party's guaranteed first strike every round lets
it alpha-strike the low-HP minor slaad dead before they ever act far more
often than true per-creature rolled initiative would allow (instrumented
per-combatant attack counts across 2,000 universes: the first-turn-order
slaad fires its Multiattack only 0.006 times/universe on average, the
second 0.83, the third 1.86 — a monotonic, order-determined asymmetry, not
a targeting or compile bug). Otar's own realized damage moves the same way
(mean damage dealt 129.79 baseline -> 213.54 enemies-first, matching
combat-sim's 235.2 far more closely) purely from *when* he gets to act
relative to the party, with his Multiattack routine itself unchanged and
already verified correct (fires Bite/Claw/Tongue Lash at exactly the
authored 1:3:1 ratio every activation).

Resolved by `95e887c2`/`d3cd3f2c` (see Status above) — no longer a live
Divergence. `category` below is `resolved`, not `simulate-time`, so the
parity harness's exclusion-set parser skips this entry entirely.

```divergence
id: fixed-turn-order
category: resolved
mechanism: the sequence combatants act in during a party-vs-party encounter
old_behavior: initiative rolled per iteration (d20 + bonus, sorted descending)
new_behavior: 'one fixed order for the whole batch: party declared order, then enemy declared order'
measured:
  seed: 1
  universes: 2500
  round_cap: 20
  matchups:
    - id: dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/otar-the-foul-plus-minor-slaad-3
      a_win_rate_delta: +0.361
      b_win_rate_delta: -0.361
      a_tpk_rate_delta: -0.361
      draw_rate_delta: 0.000
```

---

## Lair-action default activation

**Mechanism.** Whether a lair action fires at all during an encounter.

**combat-sim.** `simulator.mjs` only ever synthesizes a lair actor when the
caller explicitly supplies `opts.lairActions` (`simulator.mjs:1307-1308`) —
populated exclusively from a `--scenario` loadout file's `scenarios[].lair[]`
entries (`lib/loadout.mjs:143-165`). A statblock page's own `lair_actions:`
prose section is never read by the simulator at all (grepped: zero hits of
`lair_actions` in any `lib/*.mjs` file) — it is purely descriptive content
for a human DM. Running `sim-combat <X> <Y>` with no `--scenario` flag, as
issue #52's harness does, therefore always simulates zero lair effect,
regardless of whether either combatant's page declares lair actions.

**dndsim.** `rules/dnd5e_2014/combat.py`'s `run_combat` fires a lair-action
window unconditionally once any combatant's `CombatantSpec.has_lair` is
`True` (`combat.py:542-564`) — a boolean set at `CombatantSpec` construction
time, applying a fixed generic hazard (a `poisoned` tag reapplied to the
opposing side every round) with no connection to a page's own
`lair_actions:` text either. Issue #52's matchup set sets `has_lair=True` on
its Otar the Foul combatant (`scripts/parity_matchups.py`'s `_otar`) to
exercise this mechanism at all, following the same boolean-flag precedent
`fixture.py`'s pre-existing `PARTY_VS_ENEMIES_FIXTURE` already set for its
"Grung Chief" combatant.

The two engines' defaults are opposite: dndsim's lair hazard is opt-in at
authoring time and then unconditional at run time; combat-sim's is
unconditional at authoring time (any page may declare `lair_actions:`) and
then opt-in at run time (a `--scenario` loadout must be supplied). No
`--scenario` loadout modeling Otar's own lair currently exists — lair
scenario authoring belongs to whichever loadout work picks it up (`rules/
dnd5e_2014/loadouts*` is issue #49's owned path, out of #52's scope) — so
today there is no way to invoke combat-sim with an equivalent lair effect
for this matchup.

**Measured.** `scripts/parity_harness.py`, seed derived via `cell_seed(1,
"dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/otar-the-foul")`, 8,000
universes/iterations, round cap 20 — "old" is `sim-combat party <otar
page>` with no `--scenario` (zero lair effect, per above); "new" is
`run_combat` with Otar's `has_lair=True`:

| Matchup | a_win Δ | a_tpk Δ | draw Δ |
|---|---|---|---|
| Party vs. Otar the Foul | +0.0576 | -0.0691 | +0.0115 |

The direction is intuitive — dndsim's forced per-round hazard does real
extra damage/debuff to the party over a multi-round fight, which should
*lower* the party's win rate and *raise* the TPK rate if the two engines
were otherwise identical — but the measured sign is reversed (party win
rate is *higher*, not lower, under dndsim). This confirms the delta here is
not attributable to the lair hazard alone: `scripts/parity_matchups.py`'s
own `combatant_from_page` collapses every real combatant to one flat attack
profile (see that module's docstring), which independently narrows both
sides' effective offense relative to combat-sim's read of the same pages'
full action lists. This Divergence's matchup is excluded from #52's
strict CI assertion because the two engines are known to structurally
differ here, not because the measured deltas above isolate the lair
hazard's effect on their own — a scenario-file-driven, single-variable
remeasurement is a follow-up, not part of this slice.

```divergence
id: lair-action-default-activation
category: simulate-time
mechanism: whether a lair action fires at all during an encounter
old_behavior: 'lair action requires an explicit --scenario loadout supplying scenarios[].lair[]; a page''s own lair_actions: prose is never read by the simulator'
new_behavior: 'fires unconditionally once any CombatantSpec.has_lair is True, applying a fixed generic hazard unconnected to the page''s own lair_actions: text'
measured:
  seed: 613887531
  universes: 8000
  round_cap: 20
  matchups:
    - id: dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/otar-the-foul
      a_win_rate_delta: +0.0576
      b_win_rate_delta: -0.0691
      a_tpk_rate_delta: -0.0691
      draw_rate_delta: +0.0115
```

