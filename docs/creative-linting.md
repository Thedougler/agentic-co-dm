# Creative Linting

Creative linting is the repository-owned validation layer for generated wiki and session Work. It composes the existing structural checker with Vale and symbolic cross-page checks; it does not replace `tools/lint_wiki.py` or DM judgment.

## Architecture and ownership

The implementation has three cooperating layers:

- `tools/lint_wiki.py` remains the owner of the existing structural HARD checks.
- Vale runs static prose-pattern rules from `styles/CoDM/`.
- `tools/creative_lint/` owns registry loading, bundle routing, symbolic evaluators, the finding schema, severity/status computation, waivers, shadow telemetry, and the repair loop.

The CLI entry point is `scripts/wiki-lint`:

- No-subcommand invocations retain the existing structural behavior and delegate to `tools/lint_wiki.py`.
- `task`, `file`, `corpus`, `changed`, `rule`, and `candidate` load creative lint lazily and return the unified finding contract.
- `scripts/wiki-maintain --report` is unchanged. `--creative-lint` adds an optional A7 corpus report using the same engine as live linting.

Configuration has one owner per tool:

- `.vale.ini` is the sole Vale package and path-scope authority. The repository carries `ai-tells`, `proselint`, and `Readability`. Wiki pages also enable `CoDM`, while creative fixtures intentionally enable only `CoDM`. Raw and archive pages are excluded, staging uses only the configured prose packages, and templates are excluded.
- `.markdownlint-cli2.jsonc` owns built-in Markdown structure settings. It excludes `wiki/_raw`, `wiki/_staging`, `wiki/_archive`, `wiki/templates`, `specs`, and `node_modules` from its Markdown globs.
- `package.json` is private metadata only. Its npm scripts are thin aliases to existing repository commands; no Node wrapper or duplicate lint implementation exists. `markdownlint-cli2` is pinned to `0.23.2`, Node is `>=22`, and `package-lock.json` is committed.
- `rules/registry.yml` owns rule metadata. `rules/bundles.yml` owns task-to-category routing. Neither duplicates the Vale package list.

## Finding and status contract

Every evaluator emits the same fields:

```json
{
  "rule_id": "AGENCY001",
  "result": "fail",
  "severity": "BLOCK",
  "location": {
    "file": "wiki/path/to/file.md",
    "line": 42,
    "col": 5,
    "text": "You decide..."
  },
  "evidence": "Matched pattern: 'You decide...'",
  "reason": "Narration authors a player-character decision",
  "repair_target": "Rewrite to describe the situation without prescribing the PC's response",
  "evaluator": "vale"
}
```

`result` is `pass`, `fail`, or `abstain`. Semantic or otherwise unavailable evaluators record their unavailable/abstention state; they do not silently pass. `repair_target` and waiver metadata are optional when they do not apply.

The five severity levels are independent from lifecycle:

- `BLOCK` and `REPAIR`: repair and re-lint before completion.
- `REVIEW`: repair or surface the finding for DM judgment.
- `WARN` and `INFO`: diagnostics only; never mechanically optimize them away.

Aggregate status is `repair_required` when any unwaived `BLOCK` or `REPAIR` finding remains, `review_needed` when only `REVIEW` findings remain, and `clean` for no actionable findings (including WARN/INFO-only output). Exit status follows the same contract: `0` for clean or diagnostics, `1` for BLOCK/REPAIR, and `2` for REVIEW without blocking findings.

## CLI

```bash
./scripts/wiki-lint task session-prep path/to/output.md --json
./scripts/wiki-lint file wiki/entities/npc/archivist-vel.md --json
./scripts/wiki-lint corpus wiki --json
./scripts/wiki-lint changed --json
./scripts/wiki-lint rule AGENCY001
./scripts/wiki-lint candidate "Stop having NPCs know things they could not know" --json
```

Task runs resolve one named bundle and accept optional paths. File runs evaluate active rules at inherent severity. Corpus runs use the corpus bundle; `changed` selects Markdown files from `git diff --name-only HEAD`. `--severity block,repair` filters rendered findings without changing evaluation or status computation.

The existing structural mode remains compatible:

```bash
./scripts/wiki-lint --json wiki
```

Consolidation is explicit and approval-gated:

```bash
./scripts/wiki-lint --consolidate wiki --json
./scripts/wiki-lint --consolidate wiki --json --approve
```

Without `--approve`, the command emits a deterministic dry-run plan and performs no writes. With approval it re-runs the checks, rejects stale or unsafe plans, and applies only safe structural repairs. Invocations without `--consolidate` remain report-only.

## Authoring rules and bundles

To add a rule:

1. Add one metadata entry to `rules/registry.yml` with a stable `CATEGORY###` ID, title, category, scope, five-level severity, evaluator, lifecycle, message, repair guidance, tags, and optional conflict/dependency IDs.
2. For `evaluator: vale`, add `styles/CoDM/<ID>.yml`. Each style file uses a Vale extension point, includes the ID in `message`, maps the registry severity to Vale's `error`/`warning`/`suggestion` level, and scopes the check to the intended content.
3. Add `fail_*.md`, `pass_*.md`, and an `ambiguous_*.md` acceptable-region fixture under `tests/fixtures/creative_lint/<ID>/`. Ambiguous cases are recorded for review rather than treated as suite failures.
4. Add the rule category to the appropriate bundle in `rules/bundles.yml` only once, under `block`, `review`, or `diagnostics`.

The initial static rules are AGENCY001-003, KNOW001-002, TEMP001, and SCENE001-002. Symbolic rules cover CANON001-002, WIKI001-002, and RETRIEVAL001; DIVERSITY001 remains an INFO diagnostic. Rules with `scene` or `diversity` categories may never exceed `WARN`. The bundle's gate caps effective severity, while the registry remains the inherent-severity source.

A correction should first search existing titles, messages, and tags with `wiki-lint candidate`. A match routes the correction to the existing rule and its fixtures. A no-match candidate is written under `rules/candidates/` with lifecycle `SHADOW`; it must accumulate fixtures and telemetry before promotion. Promotion requires greater than 90% human agreement and less than 10% false positives, followed by a deliberate `SHADOW` → `ACTIVE` lifecycle change. Creative diagnostics can reach `WARN`, never `BLOCK`.

## Repair loop

`LintEngine.repair_loop()` passes exact findings, including rule ID and location, to a repair callback, then re-lints the changed surface. It stops after three iterations by default (configurable). If blocking findings do not converge, the remaining findings stay visible for DM review; changed text alone never counts as a successful repair.

## Lifecycle and shadow mode

Rules move through `DRAFT → SHADOW → ACTIVE` independently of severity:

- `DRAFT` rules are skipped.
- `SHADOW` rules evaluate and append JSONL telemetry under `rules/shadow/`, but their findings are excluded from agent-facing findings and status.
- `ACTIVE` rules participate in configured bundles at their declared severity.

Shadow telemetry is ignored by Git. Promotion is evidence-based, not an automatic severity change.

## Waivers

Waivers live in `rules/waivers.json` and require exact `rule_id`, `target`, `reason`, `owner`, `granted`, and `expires` fields. Targets may be `file:<path>`, `npc:<name>`, `session:<N>`, or `*`. Expired waivers remain auditable but no longer suppress findings. A matched waiver attaches suppression metadata and increments the waived summary count; it never deletes the finding from the audit record.

## Fixtures and maintenance

Vale and symbolic fixture families define the acceptable region:

- `tests/fixtures/creative_lint/AGENCY001/` through `SCENE002/` contain static Vale fail/pass/ambiguous cases.
- `CANON001/`, `CANON002/`, `WIKI001/`, `WIKI002/`, `RETRIEVAL001/`, and `DIVERSITY001/` contain symbolic fail/pass/ambiguous cases and counterexamples.
- `integration/session_prep_violations.md` combines an authored PC decision with a stale/dead canonical reference for the agent-loop scenario.
- `registry/` contains valid, duplicate, malformed, missing-style, unresolved-reference, invalid-enum, and severity-ceiling metadata fixtures.
- `symbolic/` keeps focused context fixtures for dead/stale references, frontmatter/schema errors, broken links, and indeterminate state.

Run the normal structural maintenance report as before. Add creative lint only when desired:

```bash
./scripts/wiki-maintain --report --creative-lint
```

The optional A7 payload reports the corpus status and compact finding metrics; it uses the same registry, bundles, Vale adapter, and symbolic evaluators as `scripts/wiki-lint`. The two project-specific Markdown scripts are deprecated compatibility checks: markdownlint-cli2 owns repository structure, while those scripts remain available only for their not-yet-migrated Obsidian and literal-newline checks.
