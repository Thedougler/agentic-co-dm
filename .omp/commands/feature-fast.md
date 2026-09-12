---
description: >
  Specify through analyze, then bounded implementer waves, converge, and verify.
  Use when running a feature on the Spec Kit + OMP baseline. Direct OMP session only.
---

## User Input

```text
$ARGUMENTS
```

If `$ARGUMENTS` is empty, stop. Say the feature description is missing. Do not invent a feature.

Primary path: this OMP session. Not RPC. Not ACP.

Do not edit generated `.omp/commands/speckit.*`. Spec Kit owns the lifecycle. This command only sequences it and runs implementation waves.

Worker report schema: `specs/005-omp-speckit-integration/contracts/worker-report.md`. Use `outputSchema` with `schemaMode: strict`. Invalid structure is `failed`.

## Steps

1. Invoke `/speckit.specify` with the description. Done: the feature `spec.md` exists.
2. Invoke `/speckit.clarify` only if that spec still has unresolved ambiguity. Done: skipped, or clarifications applied.
3. Invoke `/speckit.plan`. Done: `plan.md` exists.
4. Invoke `/speckit.checklist` when the lifecycle uses it. Done: checklist exists or already present.
5. Invoke `/speckit.tasks`. Done: `tasks.md` exists.
6. Invoke `/speckit.analyze`. Done: the report exists. **Stop** if material contradictions remain.
7. Form a dependency wave of at most four independent `tasks.md` items. Shared architectural files wait. Batch agent `implementer` with one shared Spec Kit context. Isolate writable disjoint files. Recursion stays one hop (`spawns` unused). Done: every report parses; none are `blocked` or `failed`.
8. Run the targeted checks named in those reports. Done: those checks were executed.
9. Invoke `/speckit.converge`. Done: clean, or `tasks.md` has appended ids.
10. If ids were appended, implement only those ids; repeat from step 7.
11. Batch agent `verifier` (not isolated). Done: `status` is `complete` and `changed_files` is `[]`.
12. Return a short completion report: feature directory, waves run, verifier status.

Do not drive the same graph with a Spec Kit workflow engine and an OMP Swarm DAG.
