# Contract: feature-fast

Thin OMP command. Sequences Spec Kit. Does not replace it.

## Invoke

```text
/feature-fast <feature description>
```

Empty description → fail. Do not invent a feature.

File: `.omp/commands/feature-fast.md` (new). Generated `.omp/commands/speckit.*` stay unmodified.

## Steps (each has a done bound)

1. `/speckit.specify` with the description. Done: `specs/*/spec.md` exists for the feature.
2. `/speckit.clarify` only if the spec still has unresolved ambiguity. Done: skip or clarifications applied.
3. `/speckit.plan`. Done: `plan.md` exists.
4. `/speckit.checklist` if the lifecycle uses it. Done: checklist exists or already present.
5. `/speckit.tasks`. Done: `tasks.md` exists.
6. `/speckit.analyze`. Done: report exists. **Stop** if material contradictions remain.
7. Form a dependency wave (≤4 independent items). Batch `implementer` with shared Spec Kit context. Isolate writable disjoint files. Sequential if shared architectural files. Done: every worker report valid; no `blocked`/`failed`.
8. Targeted checks from those reports.
9. `/speckit.converge`. Done: either clean or `tasks.md` appended.
10. If appended, implement **only** appended ids; repeat from 7.
11. Batch `verifier` (not isolated). Done: verifier `status=complete` and `changed_files=[]`.
12. Return a short completion report (feature dir, waves, verifier status).

## Failed

Material analyze findings ignored. Generated `speckit.*` edited. Worker spawn. More than four implementers. RPC/ACP used as the path. Empty input accepted.

## Invalid

A Spec Kit workflow engine and an OMP Swarm DAG both driving this sequence. Specialists named after Spec Kit phases.
