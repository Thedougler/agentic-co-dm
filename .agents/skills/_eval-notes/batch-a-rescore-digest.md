# Batch A re-score digest — Eval Runner (post-#145)

Branch: `evals/batch-a-rescore-pr145` (worktree `/home/box/agentic-co-dm-batch-a-rescore`).
Tip base includes #145 assertion tighten. Graders scored output template conformance.
**Phase 3 gate:** with_skill mean pass rate **100% on all five skills — HIT**.

## Pass rates (mean assertion pass rate)

| Skill | with_skill | without_skill | delta | 100% bar |
| --- | ---: | ---: | --- | --- |
| city-design | **1.000** | 0.169 | +83.1% | **HIT** |
| region-design | **1.000** | 0.329 | +203.6% | **HIT** |
| lore-design | **1.000** | 0.367 | +172.1% | **HIT** |
| npc-design | **1.000** | 0.022 | ? | **HIT** |
| place-design | **1.000** | 0.084 | +91.6% | **HIT** |

## Gate summary
All five with_skill at 100%: **YES**. CoS may packet Skill Optimizer for token-min while holding 100%.

## Eval Author flags (high level)
Per-skill `EVAL_AUTHOR_FLAGS.md`. Cross-cutting: resist-invent stays strongest; durable process locus works; structure floor alone still soft. place eval-14 pre-#145 non-discrimination **withdrawn**.

## Stop
Slim digest/flags PR next. Then Batch B re-score (#149+#148). Phase 3 Optimizer awaits CoS packet.
