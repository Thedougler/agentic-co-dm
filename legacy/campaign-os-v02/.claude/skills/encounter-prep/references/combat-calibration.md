# Empirical difficulty calibration (not CR alone)

Empirical difficulty calibration is `combat-profiles`'s own skill
(`.claude/skills/`) — read its persisted party profile rather than
deriving the math here; can also validate a roster with the
`utils/dndsim/` Monte Carlo (§ Encounter validation sim below).

Load before finalizing the Challenge Calibration section of any combat
encounter, or before validating a homebrew creature's difficulty against a
specific party.

**Read first: `.claude/skills/combat-profiles/`'s
`vault/campaigns/shattered-sea/pcs/combat-profile/party-combat-profile.md`.** That skill now owns
this territory as a persisted, cumulative artifact — its own § Effective
CR Band is the mandatory pre-read for any combat encounter or homebrew
creature's difficulty check, not the fallback procedure below. If that
page exists and is current (check its `last_compiled` against whether any
PC profile changed since), cite it directly and stop here.

**Fallback only — no `vault/campaigns/shattered-sea/pcs/combat-profile/party-combat-profile.md` exists yet.** Run the same
derivation inline, once, from what's already on `vault/campaigns/shattered-sea/pcs/*.md` — but flag to
the DM that running `combat-profiles` would make this persist across
encounters instead of being recomputed from scratch every time (an earlier
version of this file dropped the persistence layer entirely on the
mistaken premise that no path in this architecture could hold it; a
DM-intel directory outside the wiki lint roots, same class as
`vault/ideas/`, closes that gap, so the
fallback below is now genuinely a fallback, not the only option).

## Encounter validation sim (optional; recommended for Deadly/boss fights)

Before finalizing any Challenge Calibration section the party could
actually lose, statistically validate the planned roster: run the
`utils/dndsim/` encounter Monte Carlo — party sheets (`avg`
loadouts) vs the planned roster's own statblock pages — and paste the
outcome distribution (win %, P(≥1 down), P(TPK), Effective Difficulty
Rating, Effective CR scalar, seed) into the encounter page's
`## Challenge Calibration` with `[simulated]` tags. Invocation and
scenario/lair-action encoding: `utils/dndsim/README.md`; loadout
judgment and threshold interpretation:
`.claude/skills/combat-profiles/references/simulation.md` and
`.claude/skills/combat-profiles/references/profiles.md` § Effective CR Band. Record seed + script
version beside the numbers; never hand-adjust a simulated figure.

---

## Procedure (fallback — no script or no profile available)

1. **Baseline.** Start from a concrete standard-baseline number, not an
   invented one: `.claude/skills/encounter-prep/references/encounter-composition.md` § Alternate
   XP-budget cross-check (the SRD 2024 Low/Moderate/High table) and § 9
   Lazy Encounter Benchmark (the quick CR-vs-character-level formula) are
   both citable sources — use either, or cross-check both. `vault/refs/vault/monster/
   references/cr-tables.md` § 1 has the CR/XP mapping for a
   specific creature's own value. A DM's stated house-preference for the
   budget still wins if given.
2. **Read the party's actual stats.** `grep` `vault/campaigns/shattered-sea/pcs/*.md` frontmatter
   (`hp_max`, `ac`, `class_levels`) — see this skill's Standard queries.
   Paste the hits. This replaces "assume a textbook party of this level"
   with the real numbers.
3. **Read the empirical evidence.** Grep each relevant PC's `## Session
   Log` section for past combat outcomes at or near this encounter's
   intended CR. A PC page with no combat history yet has no evidence —
   that's informative, not a gap to paper over.
4. **Adjust, don't just look up.**
   - Evidence the party trivializes a given CR → treat that CR as *easier*
     than the table says; raise the floor for what counts as "Hard."
   - Evidence the party nearly wiped at a given CR → treat that CR as
     *harder* than the table says; lower the ceiling for "Deadly."
   - Weight recent sessions over old ones — a level-3 near-TPK says nothing
     about a level-9 party's current ceiling.
   - No evidence at all → state the band is `[theoretical]` and fall back
     to the standard baseline plainly. Never invent false confidence to
     fill the gap.
5. **Multi-enemy scaling.** This party's strengths/weaknesses shift with
   enemy count more than CR alone predicts.

   **N of one monster type → run the count sweep instead of eyeballing.**
   `npm run dndsim -- sweep-count <pc-sheets.md,...> <monster.md>`
   (`party` is a comma-separated list of PC sheet paths, not a keyword;
   optional `--min-count N`/`--max-count N`, default 1..8, extending toward
   the break-even point where win probability crosses 0.5; `--seed N`;
   `--no-audit-log`; `--out <path>`) sweeps that monster's
   count against the full party and returns a `## Recommended count per
   difficulty band` table — the smallest count landing in each of
   Trivial/Easy/Medium/Hard/Deadly, with win%, P(≥1 down), and P(TPK), plus
   an explicit "not reached in swept range" row for any band the sweep
   never hit — and a `## Appendix — full count matrix` with every count's
   full row. Paste the recommended count and its band row into the Challenge
   Calibration section with `[simulated]`, same as the encounter validation
   sim above. Every invocation appends a line to
   `utils/dndsim/dndsim-audit.jsonl` unless `--no-audit-log` is passed.

   **Named multi-type combos still use the table below.** `--sweep-count`
   sweeps one monster type at a time — a hand-authored roster of mixed
   monster types stays on the encounter validation sim's `--scenario`/
   `--loadouts` path above, or this manual adjustment when no sim is run:

   | Enemy count | Adjustment | Why |
   |---|---|---|
   | 1 (solo) | Treat as harder than raw CR suggests unless it has legendary actions | Party can focus-fire a single target down fast |
   | 2–3 | Standard CR math holds | Balanced action economy both directions |
   | 4–6 | Treat as harder than raw CR suggests if the party has no AoE | Check party AoE capability before trusting the CR total |
   | 7+ (horde) | Treat as an attrition fight, not a burst fight — run it with `.claude/skills/encounter-prep/references/running-the-encounter.md` § Running hordes (pool damage, bulk-resolve attacks/saves) | Resource drain matters more than any single round |

6. **Confidence label, always.** Mark any band derived from fewer than 3
   comparable encounters `[low confidence]`. A band with zero evidence is
   `[theoretical]`, not a number presented as fact.
7. **Paste the result into the encounter page**, in the Challenge
   Calibration section: the adjusted band, its confidence label, and the
   specific evidence (session numbers, what happened) it's based on. This
   *is* the deliverable — there is no separate file to update afterward.

## Anti-patterns (carried from the legacy skill, still true)

- **Averaging without weighting.** A PC in 5 logged combats is more
  reliable evidence than one in 1. Don't average them as equals.
- **Static bands.** If you calibrated this same CR two sessions ago and
  nothing's changed, that's fine — but if 2+ new sessions of combat data
  exist since the last time this was calibrated, redo the read, don't
  reuse the old number by memory (L1).
- **Over-precision.** "CR 7–9 = Hard" is more honest than "CR 8.3 = Hard."
  Express bands as ranges.
- **Forgetting the worst matchup.** If the Session Log shows a specific
  thing that nearly ended the party (a save type, a condition, an enemy
  archetype), that is the hard ceiling for this encounter — surface it,
  don't bury it under an average.
