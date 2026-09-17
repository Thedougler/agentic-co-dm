# Creative Linting

Creative linting is the repository-owned validation layer for generated wiki and session Work. It composes the existing structural checker with Vale and symbolic cross-page checks; it does not replace `tools/lint_wiki.py` or DM judgment.

## Architecture

- `rules/registry.yml` is the single metadata owner. Rule IDs are stable `CATEGORY###` identifiers.
- `rules/bundles.yml` maps task names to categories and severity gates.
- `styles/CoDM/` contains Vale's executable prose rules.
- `tools/creative_lint/` owns the finding contract, registry, bundle resolution, adapters, symbolic checks, waivers, shadow telemetry, and repair loop.
- `scripts/wiki-lint` retains its existing no-subcommand structural mode and lazily loads creative lint only for `task`, `file`, `corpus`, `changed`, `rule`, and `candidate`.

## Finding and status contract

Every evaluator emits `rule_id`, `result`, `severity`, `location`, `evidence`, `reason`, `repair_target`, and `evaluator`. `result` is `pass`, `fail`, or `abstain`; unavailable semantic services use `abstain` and never silently pass.

- `BLOCK` and `REPAIR`: repair and re-lint before completion.
- `REVIEW`: repair or surface the finding for DM judgment.
- `WARN` and `INFO`: diagnostics only; never mechanically optimize them away.

The aggregate status is `repair_required`, `review_needed`, or `clean`. WARN/INFO findings leave status `clean`.

## CLI

```bash
./scripts/wiki-lint task session-prep path/to/output.md --json
./scripts/wiki-lint file wiki/entities/npc/archivist-vel.md --json
./scripts/wiki-lint corpus wiki --json
./scripts/wiki-lint changed --json
./scripts/wiki-lint rule AGENCY001
./scripts/wiki-lint candidate "Stop having NPCs know things they could not know" --json
```

Exit status is 0 for clean/diagnostics, 1 for BLOCK/REPAIR, and 2 for REVIEW without blocking findings. `--severity block,repair` filters output without changing rule evaluation.

## Authoring rules and bundles

Add metadata to `rules/registry.yml`, then add a Vale file when `evaluator: vale`. Registry validation checks required fields, stable IDs, enum values, Vale paths, references, and the WARN ceiling for `scene` and `diversity`. Bundles list categories under `block`, `review`, or `diagnostics`; a category may appear only once. The effective severity is the lower of the inherent severity and the bundle gate.

A creative correction should first search rule titles, messages, and tags with `wiki-lint candidate`. Existing matches improve the rule or its fixtures. A new candidate is written under `rules/candidates/` as `lifecycle: SHADOW`; it requires fixtures and telemetry before promotion. Promotion evidence is greater than 90% human agreement and less than 10% false positives, then a deliberate lifecycle change to ACTIVE. Creative diagnostics can reach WARN but never BLOCK.

## Repair loop

`LintEngine.repair_loop()` passes exact findings, including rule ID and location, to a repair callback and re-lints the changed paths. It stops after three iterations by default. Unconverged BLOCK/REPAIR findings remain visible for DM review; a repair is never treated as complete merely because text changed.

## Lifecycle and shadow mode

Rules move `DRAFT -> SHADOW -> ACTIVE`. DRAFT rules are skipped. SHADOW rules evaluate but are excluded from agent-facing findings and status; `ShadowRecorder` appends JSONL telemetry under `rules/shadow/`. The telemetry directory is ignored by Git. ACTIVE rules participate in the configured bundle.

## Waivers

Waivers live in `rules/waivers.json` and require exact `rule_id`, target, reason, owner, granted, and expires fields. Targets can be `file:<path>`, `npc:<name>`, `session:<N>`, or `*`. Expired waivers remain auditable but do not suppress findings. A waiver attaches suppression metadata and increments the summary rather than deleting the finding.

## Fixtures and maintenance

Each nontrivial rule owns `fail_*.md`, `pass_*.md`, and optional `ambiguous_*.md` fixtures under `tests/fixtures/creative_lint/<RULE_ID>/`. The focused tests exercise registry validation, severity gates, Vale mapping, symbolic checks, waivers, shadow telemetry, repair convergence, and CLI output.

The normal `scripts/wiki-maintain --report` path is unchanged. Add `--creative-lint` to include an optional compact A7 corpus report using the same engine as the live CLI. Existing custom Markdown lint scripts remain until the markdownlint-cli2 migration has passing fixtures; they are not removed by a partial port.
