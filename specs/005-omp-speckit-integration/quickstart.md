# Quickstart: OMP Spec Kit Integration

Proves native integration, ownership split, sticky rules, caps, and the thin orchestrator without running a second feature.

## Prerequisites

- Branch `005-omp-speckit-integration`
- Direct OMP session in repo root (not `omp --mode rpc` / ACP)
- Spec Kit commands already under `.omp/commands/`

## Story 1 — Native, not generic

1. `scripts/check-omp-baseline.sh` — expect exit 0.
2. Open `.specify/init-options.json` — `integration` is `omp`.
3. Invoke `/speckit.specify` help/presence from OMP — command resolves from `.omp/commands/`, not a generic adapter.

## Story 2 — Context vs rules

1. After this plan exists, run `/speckit.agent-context.update` (or the after-plan hook).
2. `.omp/AGENTS.md` managed block names this plan path. Unmanaged lines still `@../AGENTS.md`.
3. Compact or start a new session: `.omp/RULES.md` still forbids skipped verification and hand-edits of generated `speckit.*`.

## Story 3 — Specialists and caps

1. Inspect `.omp/config.yml`: concurrency 4, recursion 1, advisor off, memory off.
2. Inspect `.omp/agents/`: only `spec-auditor`, `implementer`, `verifier`; each `spawns: []`.
3. Dry-read `/feature-fast` steps against [contracts/feature-fast.md](./contracts/feature-fast.md): analyze before waves; isolate only writable disjoint work; structured reports per [contracts/worker-report.md](./contracts/worker-report.md).

## Pass

SC-001: native commands. SC-002: no phase-named agents. SC-004: cap and `spawns: []` visible. SC-007: rules file present after compaction. SC-008: `/feature-fast` exists and does not edit generated commands. Fail = check script exit 1 or RPC used as the path.
