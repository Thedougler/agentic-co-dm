# Batch B digest — Eval Runner

Branch: `evals/batch-b-run-pr140` (worktree `/home/box/wt-batch-b-spell`).
Pattern: skill-creator with_skill vs without_skill → grade → aggregate.
Bounds: no SKILL.md rewrites; no live wiki writes; bulky workspaces stay on feature branch.

## Pass rates (mean assertion pass rate)

| Skill | with_skill | without_skill | delta | Workspace |
| --- | ---: | ---: | --- | --- |
| dnd-5e-magic-item-design | **1.000** | 0.042 | +95.8% | `.agents/skills/dnd-5e-magic-item-design-workspace/iteration-1/` |
| spell-design | **1.000** | 0.122 | +87.8% | `.agents/skills/spell-design-workspace/iteration-1/` |
| vehicle-design | **1.000** | 0.201 | +79.9% | `.agents/skills/vehicle-design-workspace/iteration-1/` |

## Eval Author fix list

Per-skill: each workspace `EVAL_AUTHOR_FLAGS.md`. Cross-cutting:

1. Resist-invent / craft anti-pattern evals are strongest discriminators — keep hostile wording.
2. Process assertions need durable `process-notes.md` / transcript evidence locus.
3. **spell:** keep spell-scroll≠spell guardrail; casting-field/stub-premise soft alone.
4. **vehicle:** keep Unknown honesty + invention labels; soft bare headings; tighten eval-4 conspiracy reframing; split eval-1 compound content.
5. **item:** keep craft 5–12 refusals + invention/canon split; tighten eval-1 At-the-Table omit-if-empty and preserve-canon-alone; eval-8 exact-trigger vs once-per-turn.

## Stop
Awaiting CoS. Slim digest/flags PR next (workspaces not for main).
