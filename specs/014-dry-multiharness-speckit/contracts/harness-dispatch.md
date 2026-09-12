# Contract: `docs/agents/harness-dispatch.md`

In-repo Grok Bot / outer-loop procedure. Single owner of orchestration steps.

## Must include

1. Purpose: coordinate coding harnesses; do not own repository truth
2. Procedure: locate repo → read `AGENTS.md` → git state → read Spec Kit artifacts → determine phase → pick a coding harness → hand off objective, paths, phase, extra constraints only
3. Canonical pointers: `AGENTS.md`, constitution, `specs/**/spec.md|plan.md|tasks.md`, source, tests
4. Prohibitions: no Bot-local policy/specs; no re-specify when artifacts exist; no two writers on one workspace; no editing generated Spec Kit adapters
5. Return report: harness used, artifact/workspace changed, tests run, unresolved findings, convergence state, commit/PR if applicable

## Must not include

- Constitution principle text
- Feature requirement text
- Spec Kit command/prompt bodies
- A second copy of `AGENTS.md`

## Not a Spec Kit integration

No `.grok-bot/speckit/`. No generated `speckit-*` under a Bot tree.
