# Simulation judgment guide — loadouts, rosters, and reading results

The agent-judgment half of the sim workflow. Schemas and CLI syntax:
`utils/dndsim/README.md` — never restated here.

## Relationship to `utils/dndsim/`

The script owns all probability math AND default tactics: closed-form hit
chances, Monte-Carlo damage distributions, encounter outcome statistics,
the Effective Difficulty Rating and Effective CR scalar, and the
perfect-play auto-policy (greedy per-slot expected value — the precise
definition lives in the README's Division-of-labor section). The agent
owns what the policy can't know: building the sheet's Combatant Block and
its `sim.abilities:` list, encoding unmodeled creature prose, curating the
default-sweep monster set, translating a DM brief into a goals spec, and
interpreting results. CLI usage, the unified statblock schema (native
fence keys + the `sim:` extension namespace), the loadout schema, the
goals spec, and the output contract live in
`utils/dndsim/README.md` — read it before the first sim run; never
restate it.

## Declaring abilities (SKILL.md Workflow step 4)

The sheet's Combatant Block carries everything the PC can do: attacks,
save actions, heals, reactions, resources, and the `sim.abilities:` list —
capabilities in the modifier vocabulary (Hex, GWM's tradeoff, Bardic
Inspiration, Lucky). The auto-policy decides when to use each (EV-gated
per target, costs enforced), so declaring a capability is the whole job;
a capability missing from the block is a silent floor on the PC's numbers.
Loadout files remain for what isn't a capability:

- **Scenario assumptions**: `resource_budget` (mid-adventuring-day
  attrition), `setup_round`, `assume_rider_triggers` (Booming Blade's
  movement clause at a stated probability, not wishful 1.0),
  `save_action_priority`.
- **`min` floor runs**: the reserved `min` name still zeroes every pool —
  what the PC does in round 9 of a bad day.
- **Named alternates**: any authored loadout layers forced-on constraints
  over the policy; `--loadout a,b,c` prints a comparison table.

## Goals and evolve (encounter calibration)

**Default: no goals file needed, any verdict.** Any single-enemy-type
result (a plain `sim-combat` run, `--sweep-count` once per sweep,
`--sweep-corpus`'s deadliest opponents) auto-triggers a difficulty-
drivers table plus a difficulty ladder — one tuned variant per band
(Easy/Medium/Hard/Deadly-achievable/TPK-inducing), not just a single
Hard-band target — the README's § Difficulty ladder. Wall-clock budgeted
(`--budget-ms`, default 30s via `lib/budget.mjs`), so a busier statblock
gets a real but bounded search. `--no-tune` opts out. This covers the
common case ("what would an easier/harder version of this look like")
without hand-authoring anything; reach for `--goals`/`--evolve` below only
for a custom target band or a fuller manual search.

Translate a qualitative brief ("should feel deadly, but winnable") into a
goals YAML — e.g. P(win) ≥ 0.67, P(≥1 down) ≥ 0.5, P(≥2 down) ≤ 0.35,
P(TPK) ≤ 0.05 — and run with `--goals` to score the encounter (MET/MISSED
per goal + distance). To tune a statblock toward the goals, `--evolve`
runs the GA over the creature's objective knobs and `--emit-statblock`
writes the winner; sanity-check the emitted deltas against the creature's
fiction before adopting (a −10 HP, +1 multiattack grung is still the DM's
call). Record the goals file beside the sim command (Hard Rule 9).

**Summons and companions** (Eldritch Cannon, familiars, beast companions):
extra combatants in the scenario, not modifiers — see the README. Their
action economy is real action economy.

**Creature side**: encode prose traits the parser flagged `unmodeled`
(WARN lines) via `creature_overrides` when they matter for the matchup —
a deflection reaction, a legendary-resistance-like pool. Lair actions go
in the scenario's `lair:` list. GM optimal play is data too: targeting
policies (`focus_lowest_hp` is default GM ruthlessness; pick `spread` for
an unintelligent brute) and surprise assumptions live in the scenario.

## Default sweeps (PC screening, Workflow step 5; party compile, Workflow step 8)

`npm run dndsim -- sweep-corpus <pc-sheet.md|pc-slug|alias> [--seed N]
[--corpus-dir dir...] [--party-glob '<glob>'] [--no-audit-log] [--out path]`
— a 1v1 win-rate matrix for one PC against every file in the
corpus (point `--corpus-dir` at `vault/srd/monsters/` and
`vault/campaigns/shattered-sea/monsters/`, repeatable). The subject positional accepts a bare
slug, a sheet's frontmatter `alias:` value (e.g. `npm run dndsim --
sweep-corpus pbj`), or a literal path. This is the PC's
default screening run (SKILL.md Workflow step 5), additive to the
closed-form pc-profile run, never a replacement. Its rows feed the Counter
Profile (`_templates/pc-combat-profile.md` §5) as empirical counter
evidence.

`npm run dndsim -- sweep-corpus party [--party-glob '<glob>'] [--seed
N] ...` — chains one sweep-corpus run per PC in the party glob
(default: the real full party), concatenating each PC's report. The
whole-party screening run in one command — the `party` keyword sweeps
every PC by definition.

`npm run dndsim -- sweep-count <pc-sheets.md,...> <monster.md|monster-slug>
[--min-count N] [--max-count N] [--seed N] ...`
— a count sweep (1..8+ by default, extending toward a break-even point)
of one monster type against the named party (the party argument is a
comma-separated list of PC sheet paths — dndsim has no `party` keyword
here; pass a single PC sheet to sweep against that one PC instead). This
is the party profile's
Effective CR Band source (SKILL.md Workflow step 8, `profiles.md`
§ Effective CR Band): curate one monster per band probe — season-relevant
threats, or a CR-spanning sample — real vault statblocks
(`vault/srd/monsters/`, `vault/campaigns/shattered-sea/monsters/`) preferred over
synthetic blocks. Report embeds a
full per-PC/per-combatant breakdown (HP remaining, damage dealt) for the
smallest count reaching each band by default — the "why is this Deadly"
answer, no separate command needed. It answers a count-independent question ("how would this
monster's own stats need to change") separate from "how many copies".

`npm run dndsim -- sim-combat <fileA.md[:N]> <fileB.md[:M]>` — an on-demand
A-vs-B, reusing the existing encounter-mode report
shape, for a specific named matchup outside the default sweeps; the
`:N`/`:M` count suffix on either side spec repeats that combatant.

Every invocation appends a line to `utils/dndsim/dndsim-audit.jsonl`
(seed, argv, adaptive knobs, per-cell totals, result digest) unless
`--no-audit-log` is passed — cite the seed and exact command beside the
figures regardless (Hard Rule 9); the audit log is a record, never the
citation itself.

**Adaptive iteration counts.** Per-cell iteration count now varies under
adaptive Monte-Carlo stopping (converges early on lopsided matchups, caps
at 10,000) — this does not weaken reproducibility: the same seed and
inputs reproduce a report bit-for-bit, and each cell's iteration count is
recorded both in the report and in the audit log.

## Reading results into the templates

- Per-PC ranges (hit%, DPR distribution, be-hit, survivability) →
  pc-combat-profile § Combat Stats, tagged `[simulated]`, seed/version/command in
  frontmatter + above the table.
- `--sweep-corpus`'s band-filtered, win%-ascending appendix rows (opponent,
  win%, band) → pc-combat-profile § Counters & Synergy, tagged `[simulated]`.
- `--sweep-count`'s recommended-count-per-band rows (monster, break-even
  count, win%, P(≥1 down), P(TPK), Effective CR scalar, seed) → party
  profile § Effective CR Band table.
- Band mapping: the script prints its threshold rules with every report;
  the DM may retune thresholds once — record the tuned values in
  `profiles.md` § Effective CR Band and keep using them.
- WARN lines → the profile's unsimulable-abilities list, verbatim names.
- `NOTE ... optimal auto-policy ran instead` means a named loadout wasn't
  authored and the run fell back to the default policy — fine unless the
  number is being cited as that specific loadout.

## Seed discipline

`--seed` defaults to a fresh random value per run (no need to pass one) —
every report prints/records the seed it used, so RECORDING what ran
(seed, script version, exact command — Hard Rule 9) matters more than
ever now that the default itself changes every invocation. Pass that
printed seed back via `--seed <n>` to reproduce one specific run
exactly. Re-running with the same explicit seed and inputs must
reproduce the report bit-for-bit; if it doesn't, the inputs changed —
find what moved before trusting either run. (The difficulty-ladder
section is the one exception — it's wall-clock budgeted, so its exact
search result isn't guaranteed bit-identical across machines even at a
fixed seed; the core simulation numbers still are.) Never average across
seeds by hand; raise `--iterations` instead.
