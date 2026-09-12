# Contract: check-omp-baseline

Agent-shaped observation of the harness baseline.

## Invoke

```text
scripts/check-omp-baseline.sh
```

Cwd: repository root. No flags.

## Done

Exit 0 when all hold:

1. `.specify/init-options.json` `integration` is `omp` (not `generic`).
2. `.omp/commands/speckit.specify.md` and `speckit.converge.md` exist.
3. `.omp/AGENTS.md` contains `@../AGENTS.md` and both SPECKIT markers.
4. `.omp/RULES.md` contains the five sticky constraints.
5. `.omp/config.yml` has `task.maxConcurrency: 4`, `task.maxRecursionDepth: 1`, `advisor.enabled: false`, and memory/autolearn off.
6. `.omp/agents/spec-auditor.md`, `implementer.md`, `verifier.md` exist, each with `spawns: []`.
7. No `.omp/agents/` file is named after a Spec Kit phase.
8. `.omp/commands/feature-fast.md` exists.
9. No project `CLAUDE.md` (or other same-scope client twin) was added by this baseline.

Stdout: one short status listing the checks that passed.

## Failed

Exit 1. Stderr: the first failing check, one line. Do not repair files.

## Invalid

GUI. Network. Writing the files it is supposed to observe.
