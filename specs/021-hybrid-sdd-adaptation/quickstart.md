# Quickstart: Hybrid Spec-Driven Development

Validate the routing, artifact, evidence, telemetry, and compatibility seams after implementation. This guide checks behavior through files and CLIs; it does not snapshot instruction wording or require a hosted service.

## Prerequisites

From the repository root:

```bash
python3 --version
specify --version
specify integration status --json
./scripts/check-omp-baseline.sh
```

Expected baseline: Spec Kit status is `ok`, integrations include `omp`, `codex`, `grok`, and `claude`, no managed files are missing or modified, and the OMP baseline passes. The current checkout name may differ from the resolver's feature branch; do not switch branches as part of this check.

The native-tokenizer comparison path also requires the separate tracked governance change identified in the feature assumptions. Until it lands, do not claim that the native-tokenizer policy is active.

## Generated-file preservation boundary

This feature leaves the managed/generated Spec Kit outputs unchanged. Do not edit:

```text
.agents/skills/speckit-*/
.omp/commands/speckit.*
.specify/templates/*
.specify/extensions/*
```

The hybrid route and checks live in the repository-owned files named below; `specify integration status --json` and `./scripts/check-omp-baseline.sh` verify that the managed paths remain clean.

## Public command surfaces

The public commands for this feature are:

```bash
python3 scripts/hybrid-sdd-check.py --help
python3 scripts/efficiency-trace.py --help
.venv/bin/python specs/021-hybrid-sdd-adaptation/fixtures/check.py
```

`scripts/hybrid-sdd-check.py` is the deterministic route/evidence checker, `scripts/efficiency-trace.py` is the redacted trace record/report checker, and `specs/021-hybrid-sdd-adaptation/fixtures/check.py` is the feature fixture checker with the single `PASS`/failure surface.


## Public fixture check

```bash
.venv/bin/python specs/021-hybrid-sdd-adaptation/fixtures/check.py
```

Expected output is a single `PASS` summary. The checker uses temporary directories for trace and helper data and leaves no normal telemetry in the repository.

## Validation scenarios

### 1. Classification and mixed routing

Run the route fixtures for an agent-system change, campaign architecture, creative system, routine NPC, engineering request, entity collision, proposed canon, and mixed request.

Expected: full SDD receives exactly one class and `route: full-sdd`; routine content uses its existing skill route; mixed work splits the system-changing slice from routine content; no fictional canon is created.

### 2. Specification, plan, and task topology

Inspect the route and dependency fixtures with `scripts/hybrid-sdd-check.py`.

Expected: class, objective, value, authorities, scope, acceptance, failure modes, owner artifacts, intentionally omitted context, agency/canon constraints where applicable, and real dependency edges are present. Parallel fixtures have disjoint canonical write surfaces; no task is parallel merely because it is prose.

### 3. Canon and agency boundary

Run the evidence fixtures containing an existing alias, an uncertain collision, a conditional future event, a player refusal, and a safe deterministic maintenance action.

Expected: existing owners are reused or ambiguity is surfaced; proposals remain proposals; DM acceptance is required only for fact-changing Work; player decisions remain open; deterministic maintenance is not blocked by a needless human gate.

### 4. Deterministic versus semantic verification

Run the hard-gate fixtures for invalid schema/type/lifecycle/owner/link values, canon precedence, entity-before-spoken, DM explicitness, reveal, visibility, and accept-before-write. Run the paired semantic fixture separately.

Expected: objective violations are reported by the deterministic checker; semantic judgments are recorded by the blind paired evaluator and never emitted as deterministic lint failures.

### 5. Trace recording and reporting

Record complete `prep` and `wrapup` fixtures, a disabled measurement-gap fixture, produced/accepted/failed/incomplete Work, useful and unused retrieval, a retry, a fallback, and overlapping provenance.

```bash
python3 scripts/efficiency-trace.py record --input specs/021-hybrid-sdd-adaptation/fixtures/telemetry/complete.json
python3 scripts/efficiency-trace.py report --input specs/021-hybrid-sdd-adaptation/fixtures/telemetry/complete.json
```

Expected: JSONL output contains only redacted metadata and counts; every token occurrence has one primary owner; all required report metrics have labels and denominators; failed/incomplete Work is retained but excluded from accepted-Work denominators; audit/replay is metadata only.

### 6. Schema evolution and retention

Run additive and incompatible trace fixtures, then the retention fixture.

Expected: additive records remain readable; incompatible records are quarantined with an observable error; no historical record is rewritten; normal local traces are retained for 90 days and sanitized fixtures/baselines remain commit-safe.

### 7. Promotion paths

Run low-, moderate-, and high-risk paired fixtures using the versioned policy.

Expected: at least 10 same-kind pairs and a 5% median reduction are required; low risk needs a 10% canary, moderate risk needs shadow replay and canary review, high risk needs human review, and any hard-gate or semantic regression rolls back.

## Repository checks

```bash
python3 scripts/hybrid-sdd-check.py --help
python3 scripts/efficiency-trace.py --help
specify integration status --json
./scripts/check-omp-baseline.sh
```

Do not replace these checks with a text snapshot of `AGENTS.md`, generated Spec Kit adapters, or the contract prose. Generated adapters and managed templates must remain clean under Spec Kit status.

## Expected command outcomes

The route checker returns `PASS classify: 7 fixture record(s)` for the seven route scenarios. The evidence subcommands return `PASS` after validating agency, canon, topology, plan, and verification records; an objective violation returns `FAIL` on stderr and exit status `1`.

The trace CLI returns JSON for `record`, `report`, `retain`, and `promote`. `record` appends only redacted records to `.local/efficiency/traces.jsonl`; incompatible schemas are copied to quarantine and return `FAIL`. Reports label each metric `measured`, `estimated`, or `inferred` and include denominators.

Before the separate native-tokenizer governance change lands, records may be collected with `measurement_status: measurement-gap` and reason `native-tokenizer-governance-pending`, but cross-family comparison and promotion return `FAIL` and exclude those records from complete comparison samples. Do not activate or claim native-tokenizer comparisons from this feature alone.

The feature runner is the single integration surface:

```bash
.venv/bin/python specs/021-hybrid-sdd-adaptation/fixtures/check.py
```

It returns one `PASS` summary only after route, evidence, telemetry, retention, promotion, and compatibility fixtures pass. `specify integration status --json` must report `status: ok`, and `./scripts/check-omp-baseline.sh` must exit `0`; either failure remains an actionable repository failure rather than a fixture pass.

## Observed validation

On 2026-09-16:

- `.venv/bin/python specs/021-hybrid-sdd-adaptation/fixtures/check.py` → `PASS: hybrid SDD route, evidence, telemetry, promotion, retention, and compatibility fixtures`
- `specify integration status --json` → `status: ok`, default `omp`, four installed integrations, zero missing or modified managed files
- `./scripts/check-omp-baseline.sh` → `omp-speckit-baseline: pass`
