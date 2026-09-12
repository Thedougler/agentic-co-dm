# dndsim

Rules-agnostic Monte-Carlo D&D 5e combat simulation engine. This file is
the schema and CLI source of truth; skills and runbooks point here, never
restate. Behavioral divergences from the predecessor JS engine are
recorded in `DIVERGENCES.md`.

## Setup

Standalone `uv` project on free-threaded CPython 3.14 (`3.14t`):

```sh
uv python install 3.14t   # once
uv sync --project utils/dndsim
```

## CLI

Six verbs, run either directly with `uv` or via the `npm run dndsim --`
wrapper (both shown once; every other example uses the `npm` form):

```sh
uv run --project utils/dndsim dndsim <verb> [args]
npm run dndsim -- <verb> [args]
```

`npm run test:dndsim` runs the test suite (plain `pytest` from the repo
root collects an unrelated audio project and dies on collection).
`npm run dndsim:diff` runs the differential parity harness against the old
engine.

### `sim-combat [X] [Y]` — run X vs. Y, or the bundled fixture

Runs `X` (party side) vs. `Y` (enemy side) across the RNG batch and prints
a markdown encounter report. X takes the party role and Y the enemy role
regardless of what either page's own `sim: side` says. Omitting both X and
Y runs a fixed, hardcoded party-vs-enemies fixture
(`rules/dnd5e_2014/fixture.py`'s `PARTY_VS_ENEMIES_FIXTURE`) — the
explicit no-argument default, not the only way to run this command.
Passing only one of X/Y is an error.

```sh
npm run dndsim -- sim-combat --seed 1 --universes 10000
npm run dndsim -- sim-combat perrin-black-jaw grung-elite-warrior:2 --seed 1
npm run dndsim -- sim-combat party otar-the-foul --seed 1
```

#### Side-spec grammar (X and Y)

Each of X/Y is one of:

- a bare **slug** (`perrin-black-jaw`) — resolved against
  `content/monsters/srd/`, `content/monsters/homebrew/`, and `--party-glob`'s
  directory: a file's basename
  with any trailing `-sheet`/`-statblock` suffix stripped, the bare
  basename itself, or the file's own frontmatter `alias:` value must equal
  the slug exactly (case-sensitive, no fuzzy matching);
- a **literal path**, used as-is;
- `<slug-or-path>:<count>` — that combatant repeated `count` times (each
  copy gets its own entity id; `count` must be a positive base-10 integer,
  or the whole token is treated as a slug/path instead, e.g.
  `grung:latest` is not a count);
- a **comma-separated list** of any of the above, for a heterogeneous
  roster (`perrin-black-jaw,ysolde,grung-skirmisher:2`);
- the reserved keyword **`party`**, which expands `--party-glob` (sorted)
  into one combatant per match.

An unresolvable or ambiguous slug fails loudly, naming every directory
searched (unresolvable) or every candidate file found (ambiguous) — never
fuzzy-matched.

| Option | Default | Meaning |
|---|---|---|
| `--party-glob <str>` | `content/pcs/character-sheets/*-sheet.md` | Glob the `party` keyword expands to. |
| `--seed <int>` | random | RNG seed; identical seed → identical output. Omitted seeds are generated and printed. |
| `--universes`/`-u <int>` | 10000 | Monte Carlo universes for a fixed (non-adaptive) run. |
| `--round-cap <int>` | 20 | Max rounds before a matchup scores a stalemate (counted as a loss). |
| `--policy <str>` | `dndsim:policy/greedy` | Registered Policy id (`dndsim.policies` entry-point group). |
| `--adaptive` | off | Stop once the win-rate CI converges (within floor/cap) instead of running a fixed `--universes` batch. |
| `--adaptive-chunk <int>` | 500 | Universes per adaptive chunk. |
| `--adaptive-floor <int>` | 500 | Minimum universes before stopping is considered. |
| `--adaptive-threshold <float>` | 0.02 | Stop once the 95% CI half-width is ≤ this. |
| `--adaptive-cap <int>` | 10000 | Maximum universes regardless of convergence. |
| `--audit-log <path>` | `utils/dndsim/dndsim-audit.jsonl` | Append-only audit log path for this invocation. |
| `--no-audit-log` | off | Suppress the audit line for this invocation. |
| `--out <path>` | stdout | Write the report here instead of stdout. |
| `--monitor` | off | Attach the live run monitor (issue #56); degrades cleanly off a live terminal; never changes report output. |

`--workers` is deliberately not offered here — it exists only on the sweep
verbs (`sweep-corpus`/`sweep-count`), which have independent cells to
thread across; a single `sim-combat` matchup is one cell regardless of how
many combatants a side spec resolves to.

### `profile <path>` — PC-only analysis, no opposing side

Profiles one character with no opposition: exact closed-form hit chance
across an AC ladder, a sampled damage-per-round distribution, exact
closed-form chance to be hit, and effective hit points.

```sh
npm run dndsim -- profile content/pcs/character-sheets/perrin-black-jaw-sheet.md --seed 1
```

| Option | Default | Meaning |
|---|---|---|
| `--ac-min <int>` | 10 | Lowest AC in the closed-form hit-chance/DPR sweep. |
| `--ac-max <int>` | 20 | Highest AC in the closed-form hit-chance/DPR sweep. |
| `--attack-bonus-min <int>` | 2 | Lowest incoming attack bonus in the be-hit/EHP sweep. |
| `--attack-bonus-max <int>` | 10 | Highest incoming attack bonus in the be-hit/EHP sweep. |
| `--iterations <int>` | 2000 | Monte Carlo samples per AC for the DPR distribution. |
| `--seed <int>` | random | RNG seed for the DPR distribution; identical seed → identical output. |
| `--audit-log <path>` | `utils/dndsim/dndsim-audit.jsonl` | Append-only audit log path for this invocation. |
| `--no-audit-log` | off | Suppress the audit line for this invocation. |
| `--out <path>` | stdout | Write the report here instead of stdout. |

### `parse <files>...` — validate/dump, no opposing side

Parses each file's native statblock fence and prints the normalized
content. Scope is the native Fantasy Statblocks fence keys only (`name`,
`ac`, `hp`, `stats`, `saves`, damage tags, `cr`, `speed`, `senses`) —
ADR-0009. A missing required key or an unparseable value raises, naming
the offending field; an empty fence is reported as a stub page, not an
error.

```sh
npm run dndsim -- parse content/monsters/srd/otar-the-foul-statblock.md
```

| Option | Default | Meaning |
|---|---|---|
| `--json` | off | Emit normalized content as JSON instead of a one-line summary. |

### `lint [files]...` — statblock and character-sheet validation

Lints every statblock and character-sheet combatant-sheet page dndsim owns
(ADR-0010). The parser is the validator: a `` ```statblock `` fence that
won't parse, an action whose prose drifted off the SRD attack grammar the
sim reads, or a character-sheet page missing a valid party-side combatant block,
fails here rather than silently producing a wrong report later.

```sh
npm run dndsim -- lint
```

| Argument/Option | Default | Meaning |
|---|---|---|
| `files` | the full scoped corpus | Statblock/character-sheet file(s) to lint. |
| `--json` | off | Emit `markdownlint-obsidian --output-formatter json`-shaped payload — one entry per file, `errors: []` for a clean file — so `utils/scripts/lib/lint-findings.mjs` can merge this producer's findings with markdownlint-obsidian's before the one lint ratchet (docs/adr/0005, docs/adr/0006) evaluates them. |

### `sweep-corpus <subject>` — one subject vs. every creature in the corpus

One independently-seeded cell per opponent (issue #53). `subject` is a
path to a statblock/character-sheet page, or the literal keyword `party`, which
chains one sweep per PC in `--party-glob` and concatenates their reports.

```sh
npm run dndsim -- sweep-corpus content/pcs/character-sheets/perrin-black-jaw-sheet.md --seed 1
```

| Option | Default | Meaning |
|---|---|---|
| `--corpus-dir <path>` | `content/monsters/srd`, `content/monsters/homebrew` | Corpus directory (repeatable). |
| `--party-glob <str>` | `content/pcs/character-sheets/*-sheet.md` | Glob `party` expands to. |
| `--seed <int>` | random | RNG seed; identical seed → identical output. |
| `--universes`/`-u <int>` | 10000 | Monte Carlo universes per cell. |
| `--round-cap <int>` | 20 | Max rounds before a matchup is scored a draw. |
| `--policy <str>` | `dndsim:policy/greedy` | Registered Policy id. |
| `--workers <int>` | 1 | Thread count across sweep cells (one per opponent); never changes output. |
| `--audit-log <path>` | `utils/dndsim/dndsim-audit.jsonl` | Append-only audit log path. |
| `--no-audit-log` | off | Suppress the audit line for this invocation. |
| `--out <path>` | stdout | Write the report here instead of stdout. |
| `--monitor` | off | Attach the live run monitor (issue #56); never changes report output. |

### `sweep-count <party> <monster>` — how many should I throw at them

Fixed party vs. a swept count of one monster type (issue #53). Reports the
smallest count reaching each difficulty band, then the full count matrix.

```sh
npm run dndsim -- sweep-count content/pcs/character-sheets/perrin-black-jaw-sheet.md content/monsters/srd/grung-elite-warrior-statblock.md --seed 1
```

| Argument/Option | Default | Meaning |
|---|---|---|
| `party` | — | Comma-separated path(s) to the fixed party-side page(s) (typically PC sheets). |
| `monster` | — | Path to the single monster page whose count is swept. |
| `--seed <int>` | random | RNG seed; identical seed → identical output. |
| `--universes`/`-u <int>` | 10000 | Monte Carlo universes per cell. |
| `--min-count <int>` | 1 | Swept range floor. |
| `--max-count <int>` | 8 | Swept range ceiling. |
| `--round-cap <int>` | 20 | Max rounds before a matchup is scored a draw. |
| `--policy <str>` | `dndsim:policy/greedy` | Registered Policy id. |
| `--workers <int>` | 1 | Thread count across the swept cells; never changes output. |
| `--audit-log <path>` | `utils/dndsim/dndsim-audit.jsonl` | Append-only audit log path. |
| `--no-audit-log` | off | Suppress the audit line for this invocation. |
| `--out <path>` | stdout | Write the report here instead of stdout. |
| `--monitor` | off | Attach the live run monitor (issue #56); never changes report output. |

## Statblock input contract

Every combatant — PC, NPC, or creature — is authored as a standard
Fantasy Statblocks `` ```statblock `` YAML fence, using its native keys
unchanged, plus one custom `sim:` extension namespace (top-level and
per-action) that only this engine reads (ADR-0009). A page with no `sim:`
block at all still parses, defaulting to `sim: { side: enemy }`.

`sim_extension.py` is authoritative for the schema; its module docstring
states the strictness rule directly: a
sub-object that is key-checked (the top-level `sim:` map, a
per-action `sim:` sub-map, `sim.position`) is `extra="forbid"` here too, a
typo rejected loudly naming the field; a sub-object the reference never
key-checks (every ability modifier and its nested `save`/`cost`/
`on_fail`/`on_success`/`damage`/`effects`, `sim.resources[]`,
`sim.save_advantage[]`, `sim.spellcasting[]`, a per-action `cost`/`heal`/
`on_success`) is `extra="allow"` here too, because real vault content
carries keys there the reference accepts.

### Top-level `sim:`

| Key | Type | Notes |
|---|---|---|
| `side` | `party` \| `enemy` | default `enemy` if `sim:` is absent or omits it |
| `level`, `initiative`, `temp_hp`, `crit_range`, `concentration_save` | number | all optional |
| `edition` | `2014` \| `2024` (string or bare int) | documentation only — parsing auto-detects grammar per action regardless |
| `save_advantage` | `[{vs, mode: advantage\|disadvantage}]` | situational save adv/disadv |
| `resources` | `[{id, max, recharge: long_rest\|short_rest\|round\|encounter}]` | resource pools the engine enforces; `max` must be ≥ 1 |
| `abilities` | list of `Modifier` | the combatant's own always-available capabilities — see § Modifier kinds. A scenario-only kind (`resource_budget`, `setup_round`, `assume_rider_triggers`, `save_action_priority`) is rejected here |
| `routine` | map | ordered preference lists per slot: `action`, `bonus`, `reaction`, `legendary` — each present slot must be a list |
| `position` | `{start_band: 0..3}` | authored deployment band |
| `spellcasting` | list of pool | see § Spellcasting below |

### Per-action `sim:`

On any `actions:`/`bonus_actions:`/`reactions:`/`legendary_actions:` entry
— replaces prose-derived values when present, never merges:

| Key | Type | Notes |
|---|---|---|
| `id` | string | stable ref for `routine`/reactions |
| `cost` | `{resource, spend: ≥1}` | spends against a declared `sim.resources` pool |
| `concentration` | bool | |
| `once_per_turn` | bool | |
| `on_success` | `{damage_multiplier: 0\|0.5}` | half-damage-on-save override |
| `on_fail` | `{damage: [{dice, type}], effects: [{effect, escape_dc?, save_ends?}]}` | override, not merge; `effect` must be a known condition tag |
| `on_hit_effects` | `[{effect, escape_dc?, save_ends?}]` | |
| `heal` | `{dice}` | routes this entry to the heals list instead of actions |
| `action_cost` | `action` \| `bonus` | |
| `kind` | `damage_reduction` \| `damage_reduction_pct` \| `extra_attack` \| `ac_bonus` \| `unmodeled` | reaction mechanic |
| `die` | string (dice expr) | `damage_reduction`'s die, checked only when `kind` is `damage_reduction` |
| `attack`, `bonus`, `trigger` | — | reaction-kind-specific fields |
| `reach`, `range` | number (ft) | override prose-derived reach/range |
| `fraction` | number | `damage_reduction_pct`'s fraction |
| `redirect` | map, unchecked | Deflect Attacks-style redirect clause — a known key, not type-validated (matches the reference) |
| `damage_types` | list of string | filter |

### Modifier kinds (`sim.abilities[]`)

The 29-entry vocabulary registered in `MODIFIER_CLASSES`
(`sim_extension.py`) — any other `kind` is a validation error naming the
unknown value:

`flat_to_hit`, `flat_damage`, `extra_damage`, `advantage`, `disadvantage`,
`impose_disadvantage_on_enemy`, `crit_range`, `tradeoff`,
`replace_attack`, `bonus_attack`, `bonus_attack_on`,
`extra_attack_count`, `reroll_add`, `reroll_take_best`,
`damage_reduction_reaction`, `reaction_ac_bonus`, `temp_hp`,
`heal_policy`, `condition_on_hit`, `save_action_priority`,
`setup_round`, `assume_rider_triggers`, `legendary_resistance_like`,
`resource_budget`, `periodic_effect`, `post_hit_rider`,
`trade_dice_for_rider`, `retaliate`, `movement_boost`.

`resource_budget`, `setup_round`, `assume_rider_triggers`, and
`save_action_priority` are scenario-only: legal in a loadout file's
`modifiers:` list, rejected on a statblock's own `sim.abilities`.

Every modifier accepts an optional free-text `source` (loadout-authoring
convention, e.g. `{ kind: advantage, source: "ally Faerie Fire" }`) and is
otherwise open (`extra="allow"`) — a kind's own declared fields are
type-checked, unrecognized extra keys pass through.

### Spellcasting

`sim.spellcasting` is a **list** — a multiclass caster has independent
pools:

```yaml
sim:
  spellcasting:
    - { ability: cha, dc: 15, attack_bonus: 7, level: 5,
        slots: { 1: pact_slot_1 },
        known: ["Eldritch Blast", "Hex", "Armor of Agathys"] }
```

Each pool requires `ability`, `dc`, and a non-empty `known` list; `slots`
keys (when present) must be integers 1..9. Extra keys (`ability_mod`,
`source`, ...) are allowed and passed through, matching real vault content
(`perrin-black-jaw-sheet.md`).

```yaml
sim:
  side: party
  resources:
    - { id: pact_slot_1, max: 2, recharge: short_rest }
  abilities:
    - { kind: extra_damage, id: hex, dice: 1d6, type: necrotic, when: on_hit,
        requires: { concentration: true }, cost: { resource: pact_slot_1, spend: 1 } }
  routine:
    action: [{ ref: eldritch_blast }]
actions:
  - name: "Eldritch Blast"
    desc: "Ranged Spell Attack: +7, range 120 ft. 10 (2d10) Force damage."
    sim: { id: eldritch_blast }
```

## Output contract

### Encounter report (`sim-combat`)

Header (engine version, seed, universes, round cap), outcome distribution
(win rate ± 95% CI/MC-stderr for both sides, stalemate rate, rounds
mean/median/p95), party outcomes (P(TPK), P(≥1 down), and the full
P(≥k down) family when more than one k is tracked), Per-PC (HP-remaining
p5/p50/p95, P(down)), Per-combatant output (mean damage dealt, mean
reactions spent, mean concentration breaks), Positional figures (mean
turns without a reachable target, mean opportunity attacks), and the
Effective Difficulty Rating with the exact rule that fired (e.g. "P(win)
< 0.75 or P(≥1 down) > 0.5 or P(TPK) ≥ 0.05"). Any section whose source
data is empty on that run renders "Not available this run" instead of an
empty table, collected into a trailing "Data gaps in this run" warnings
block rather than a silently missing section. The policy id closes the
report.

### Profile report (`profile`)

Header (character name, engine version, seed, iterations/AC, loadout,
AC/HP), per-attack hit-chance-vs-AC tables (closed-form exact: hit %
including crit, crit %), a damage-per-round-vs-AC table (Monte Carlo:
mean, stddev, min, p5/p50/p95, max), chance-to-be-hit vs. incoming
attack-bonus (closed-form), effective hit points (expected attacks
survived per incoming-damage tier), and a trailing Warnings block for
anything the parser couldn't model (e.g. an unmodeled multi-beam attack,
an unscaled upcast effect).

## Determinism and reproducibility

One rule underlies both (ADR-0011): a `BatchRNG` wraps exactly one
`numpy.random.Generator` per run, and every draw pulls from it in the same
call order for a given code path — identical seed + identical call
sequence ⇒ identical output.

**Seed layering** (issue #50, ADR-0012) makes that survive running
independent cells in parallel:

- **Run seed** — the top-level seed a caller supplies, or one generated
  (`random_seed()`) and reported when they don't.
- **Substream seed** (`substream_seed(seed, index)`) — derived from the
  run seed and a cell's *position*. Two cells at different positions never
  collide, regardless of which order threads finish in.
- **Cell seed** (`cell_seed(seed, key)`) — derived from the run seed and a
  cell's stable string *identity*, not its position, so one cell of a
  larger run can be re-run alone, by key, and reproduce exactly.

**Why output is identical at any `--workers` count**: `run_threaded`
(`core/threaded.py`) writes each cell's result to its own index in the
returned list regardless of which order the thread pool finishes cells in
— thread count is purely a performance knob, never an input to what gets
computed. `--workers 1` (the default everywhere it's exposed — only
`sweep-corpus`/`sweep-count`) takes the exact serial path, no pool
constructed. Combined with substream/cell seeding, a swept report is
bit-identical for the same `--seed` at any `--workers` value; only
wall-clock time differs.

**Audit log**: every invocation that produces a reportable figure appends
one JSON line to `utils/dndsim/dndsim-audit.jsonl` (override with
`--audit-log <path>`, suppress with `--no-audit-log`) recording engine
version, seed, argv, subject, totals, per-cell results, and a SHA-256
digest of the rendered report — so any cited number traces back to the
run that produced it. `profile` has the same `--audit-log`/
`--no-audit-log` flags as every other verb (issue #67) and appends on the
same terms.

## Divergences

Where dndsim's behavior intentionally differs from its predecessor,
it is a Divergence recorded with a measured delta: `DIVERGENCES.md`.

## Layout

- `src/dndsim/core/` — the rules-agnostic engine (entities, attributes,
  event bus, registry, timeline, resource pools, tags, batched RNG).
- `src/dndsim/rules/` — Rules packs, discovered through the `dndsim.rules`
  entry-point group; `dnd5e_2014/` is the first one.
- `src/dndsim/cli.py` — the `dndsim` command-line entry point.
- `tests/core/`, `tests/rules/` — unit tests per layer.
- `tests/property/` — the registry-wide Hypothesis property test binding
  every Mechanic's `resolve()` to its `expected_value()`.
- `tests/goldens/` — golden-snapshot fixtures; regenerating one is a
  deliberate step documented in its own test file.

## Development

```sh
uv run --project utils/dndsim pytest
uv run --project utils/dndsim ruff check
uv run --project utils/dndsim ruff format
uv run --project utils/dndsim mypy
```
