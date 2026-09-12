## Project — utils/dndsim/ (Python combat engine)

Standing context for any agent working here. Read this instead of asking; a
dispatch prompt names only the issue and what is unusual about it.

611 tests passing, 0 failures. ruff, ruff-format, and mypy gates are
restored in `.pre-commit-config.yaml`. The `includeDndsim` wiki-cli default is `false` (ADR-0015 opt-in:
`wiki lint --dndsim` or `WIKI_CLI_DNDSIM=1`).

### Commands — use these exact forms

- `npm run test:dndsim` — the test suite. Plain `pytest` from the repo root
  collects an unrelated audio project and dies on collection.
- `npm run dndsim -- <verb> [args]` — the CLI. Verbs: `sim-combat`, `profile`,
  `parse`, `lint`, `sweep-corpus`, `sweep-count`.
- `scripts/measure_decision_buckets.py` — ADR-0011 bucket counts.
- `pyright` from the repo root, and the mypy line in `.pre-commit-config.yaml`.
- **Pass `--no-audit-log` in tests and scripts** — the audit log defaults on and
  otherwise appends to the real repo file on every run.

### Layout

`src/dndsim/core/` is rules-agnostic and stays that way: `entity`, `events`, `timeline`,
`resources`, `tags`, `rng`, `registry`, `mechanic`, `primitive`, `policy`,
`importer`, `universe` (`bucket_by_choice`), `stats`, `adaptive`, `threaded`,
`audit`. `tests/core/test_purity.py` greps it for D&D vocabulary and fails the
build — armour class, hit points, conditions and saves belong to a Rules pack.

`src/dndsim/rules/dnd5e_2014/` is the Rules pack: `statblock`, `attack_string` (both SRD
grammars), `sim_extension` (the `sim:` schema), `compile`, `primitives`,
`conditions`, `advantage`, `effects`, `reactions`, `encounter_timeline`,
`position`, `death_saves`, `spells`, `loadouts`, `combat`, `sweep`, `mechanics`,
`dice`, `fixture`.

Top level: `cli`, `report`, `profile` (`load_compiled_statblock` — the page to
`CompiledStatblock` loader, reuse it), `difficulty`, `src/dndsim/lint/`, `src/dndsim/tui/`.

### Contracts that are not negotiable

- A Mechanic implements `resolve()` and `expected_value()` in one class
  (ADR-0008). A registry-wide Hypothesis property test asserts they agree.
- A `kind` resolves through a registry. There is no switch over kinds anywhere,
  and adding one must require no edit to the simulator.
- The condition vocabulary has exactly one definition (`conditions.py`). A test
  fails if a second appears. Consume `advantage.py`'s helpers; never re-derive
  advantage, auto-fail, or turn-gating logic.
- Content is authored in the vault statblock fence (ADR-0009). Never edit
  anything under `vault/` to make code work — if a page will not parse or
  compile, the code is wrong.
- Where behavior intentionally differs from an earlier version, it is a Divergence:
  record it in `DIVERGENCES.md` with a measured delta, never an estimate.

### Gotchas that have cost time

- Python 3.14 (PEP 758) allows unparenthesized `except A, B:` and it catches
  both types. That form is correct — do not "fix" it.
- `ModifierBase` allows extras, matching the reference, so an authored key no
  Modifier declares arrives as a pydantic extra and `model_fields` will not
  report it.
- Regenerating the golden snapshot is expected when behavior genuinely changes;
  follow its documented procedure and state what moved and why. Never regenerate
  to paper over an unexplained diff.

### Working fast

- Run the narrowest failing test while iterating. Run the full gate — tests,
  ruff, mypy, pyright, `dndsim:diff` — once, at the end.
- Read the reference JS at the function you need, not whole files.
- Batch independent tool calls into one message.
- A subagent does not commit, push, or run any git history operation. The
  orchestrator commits. Report the exact list of files you created or modified.
- A failure outside your owned paths is another agent mid-write: re-run once,
  then report it rather than fixing it.
