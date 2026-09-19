# Batch A digest — Eval Runner

Branch: `evals/batch-a-run-pr138` (based on `c3e1370` / #138+#139).
Pattern: skill-creator with_skill vs without_skill → grade → aggregate.
Bounds held: no SKILL.md rewrites; no live wiki writes; workspaces on feature branch only.

## Pass rates (mean assertion pass rate)

| Skill | with_skill | without_skill | delta (reported) | Workspace |
| --- | ---: | ---: | --- | --- |
| city-design | **1.000** | 0.181 | +81.9% | `.agents/skills/city-design-workspace/iteration-1/` |
| region-design | **1.000** | 0.364 | +174.7% | `.agents/skills/region-design-workspace/iteration-1/` |
| lore-design | **1.000** | 0.456 | +54.4% | `.agents/skills/lore-design-workspace/iteration-1/` |
| npc-design | **1.000** | 0.090 | +91.0% | `.agents/skills/npc-design-workspace/iteration-1/` |
| place-design | **1.000** | 0.162 | +517.3% | `.agents/skills/place-design-workspace/iteration-1/` |

## Notes
- Timing/tokens are inline-executor estimates (`total_tokens` often null).
- Graders scored **output template conformance**, not vault lint-clean.
- All five skills hit with_skill mean **1.000** on this iteration.
- Mid-run note: an executor briefly checked out other branches; results restored onto this feature branch. Main left clean.

## Eval Author fix list (route to Eval Author, not Nick)

Per-skill detail: each workspace `EVAL_AUTHOR_FLAGS.md`. Cross-cutting:

1. **Process assertions** need durable artifacts (`process-notes.md` / `agent_report.md` / `transcript.md`) as evidence locus — city, region, lore, npc.
2. **Resist-invent evals** are the strongest discriminators across suites — keep hostile prompt wording.
3. **Bare template-heading / frontmatter** checks are weak alone (baseline can copy template).
4. **npc:** eval-1 lock-keeper identity + eval-4 Velvet Noose preserve non-discriminating; craft 5–14 keep; tighten eval-5 scene-signal wording.
5. **place:** eval-14 cardinals / travel-day / Where conventions non-discriminating; eval-10 move wording false-positive on negation — require five-part move shape.
6. **region:** optional tighten Feared-for/thesis; optional parent-region invention assert; optional ban retained five-sentence kernel on Midchain flesh.
7. **city:** split eval-4 compound content assertion; tighten Mercatura DM-thesis negative check.
8. **lore:** tighten eval-1 structure vs callout copy-forward; keep invention + rumour≠Current Truth.

## Stop
Awaiting CoS before Phase 3 optimize.
