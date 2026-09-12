# Effective CR Band derivation

The template shapes for both output tiers live in
`_templates/pc-combat-profile.md` and `_templates/party-combat-profile.md`
(single source of truth, same as every other type's template) — read
those when building or updating either tier. This file covers the
Effective CR Band procedure and the anti-patterns below, not the template
shapes themselves.

## Output tiers

1. **PC combat profile** — one document per PC: simulated hit/DPR/
   survivability ranges (optimal auto-policy default, `min` resource
   floor, any named loadouts), observed DPR from real
   session data, effective HP, counters, synergies, an append-only combat
   log.
2. **Party combat profile** — compiled from every PC profile into the
   **Effective CR Band**: this party's own difficulty thresholds derived
   from encounter Monte Carlo sweeps, adjusted by session evidence.
   `encounter-prep` and `.claude/skills/draft-content/references/monster.md` read this as their mandatory
   difficulty-calibration input.

## Relationship to `encounter-prep`

`.claude/skills/encounter-prep/references/combat-calibration.md` reads this skill's
`vault/campaigns/shattered-sea/pcs/combat-profile/party-combat-profile.md` as its primary source (mandatory pre-read before
finalizing any Challenge Calibration section) and can run its own
encounter-validation sim per that file, falling back to a fresh,
unpersisted derivation only when no profile exists yet. `.claude/skills/draft-content/references/monster.md`
reads a PC's individual profile the same way and validates homebrew CR by
sim (`vault/refs/vault/monster/references/cr-design.md` § 4).

Anti-patterns: mixing lanes ([simulated]/[calculated]/observed) in one
number; hand-adjusting a simulated figure instead of recording the
adjustment beside it (Hard Rule 9); presenting a sim of an incomplete or
low-fidelity party as the party band without the caveat; treating
support-caster value as captured by DPR sims (the unsimulable list exists
for exactly this); averaging without noting sample size; ignoring
0-damage rounds (the most important counter-profile evidence); stating a
DPR without its policy/loadout and target AC; leaving a PC capability out
of the block's `abilities:` list, silently flooring the sim
(`simulation.md`).

## Effective CR Band — the core output

This is the procedure `encounter-prep` and `.claude/skills/draft-content/references/monster.md` read as their
mandatory difficulty-calibration input: a **simulation-backed band** with
an **empirical adjustment layer**, replacing both generic 5e XP thresholds
and hand-derived judgment bands.

1. **Curate a monster set per band probe** — `simulation.md` § Default
   sweeps: season-relevant threats, or a CR-spanning sample; real vault
   statblocks (`vault/srd/monsters/`, `vault/campaigns/shattered-sea/monsters/`)
   preferred over synthetic blocks.
2. **Run `npm run dndsim -- sweep-count <pc-sheets.md,...> <monster.md>` per
   monster** — default optimal policy; the sweep extends the count (1..8+
   by default) toward that monster's break-even point against the party.
   Record seed, version, command for every row
   (`utils/dndsim/README.md` for invocation).
3. **Map each monster's smallest-count-per-band row to bands via the
   script's printed thresholds** (default: Deadly = P(win) < 0.75 or
   P(≥1 down) > 0.5 or P(TPK) ≥ 0.05; the full ladder prints with every
   report). A band the swept count range never reaches is recorded
   explicitly as "not reached in swept range", never left blank. The DM
   may retune these once — record the tuned values here and keep using
   them: *no DM-tuned thresholds recorded yet; script defaults in force.*
4. **Empirical adjustment layer** — session evidence (Hard Rules 5-6)
   adjusts the band as a separately-stated, separately-sourced delta:
   "simulated band X `[simulated, seed N]`; adjusted to Y on S0N evidence
   `[session-0N]`". The simulated band is always preserved next to the
   adjusted one; low-fidelity combatant blocks stamp their caveat on the
   band line itself.
5. **Confidence labels** — the simulated band carries its assumptions
   (policy used, party/monster fidelity, seed); the empirical adjustment
   keeps the high/medium/low/theoretical ladder. Fewer than 3 comparable
   encounters of table evidence → the ADJUSTMENT is `[low confidence]`;
   the simulated band stands on its own stated assumptions either way.
6. **Write the result** into the party profile's § Effective CR Band table (monster |
   break-even count | win % | P(≥1 down) | P(TPK) | Effective CR scalar |
   seed) — this *is* the deliverable.

## Fallback (script unavailable only — Hard Rule 9)

Label everything `[calculated]`, flag the script failure to the DM, and
derive the old way: start from `.claude/skills/encounter-prep/
references/encounter-composition.md` § Alternate XP-budget cross-check
and § 9 Lazy Encounter Benchmark; read the party's actual `vault/campaigns/shattered-sea/pcs/*.md`
frontmatter; adjust on Session Combat Log evidence; apply the multi-enemy
scaling intuition (solo harder than raw CR without legendary actions;
4-6 enemies harder without AoE; 7+ is attrition). Never present the
fallback as `[simulated]`.
