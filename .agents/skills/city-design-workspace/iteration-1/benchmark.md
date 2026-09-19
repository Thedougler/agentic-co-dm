# city-design benchmark — thin Phase 3 post-#152 re-score

Rescore time: 2026-09-19 ~01:17–01:30 PT (thin city post-merge verify)

Branch: `evals/thin-city-postmerge` @ `5e21149` (main tip includes #152 thin `b2e6114`, #153, #154)

Skill: `.agents/skills/city-design/SKILL.md` (~102 lines) + `references/city-craft.md`


## Aggregate

| Config | mean pass rate | stddev | mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 112.0 |
| without_skill | 0.067 | 0.117 | 70.5 |
| delta | +93.3% |  | +58.9% |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| eval-1-Mercatura-improve | 8/8 (1.0) | 2/8 (0.25) |
| eval-2-Mercatura-resist-invent | 4/4 (1.0) | 0/4 (0.0) |
| eval-3-saltspire-haven-from-scratch | 6/6 (1.0) | 2/6 (0.333) |
| eval-4-calven-and-calveno-flesh | 11/11 (1.0) | 1/11 (0.091) |
| eval-5-Mercatura-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| eval-6-on-wiki-entities-place | 5/5 (1.0) | 0/5 (0.0) |
| eval-7-x-resist-invent | 4/4 (1.0) | 0/4 (0.0) |
| eval-8-add-an-active-situation | 5/5 (1.0) | 0/5 (0.0) |
| eval-9-Mercatura-resist-invent | 5/5 (1.0) | 0/5 (0.0) |
| eval-10-calven-and-calveno-flesh | 4/4 (1.0) | 0/4 (0.0) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)

## Recommendation (CoS)

**KEEP merge #152** (thin city-design). Gate HIT; no with_skill assertion failures.


## Analyst observations

- PRIORITY VERIFY after #152 thin merge: with_skill mean pass rate 1.000 (success bar 1.000) — HIT. Recommend KEEP merge #152.
- Thinned SKILL.md (~102 lines) retains refuse-gates in-body; craft moved to references/city-craft.md. with_skill process-notes/transcript record both loads.
- Suite: post-#151 evals.json (10 evals) unchanged. Evals 1–4 craft/resist + 5–10 adversarial all with_skill 1.0.
- without_skill mean 0.067 (carried post-#151 CRL baselines; skill-independent). Delta pass_rate +93.3%.
- Eval-2 + evals 5/8/9 Mercatura resists and Calven 6/7/10 remain strongest discriminators (with 1.0 vs without 0.0).
- No new Author-blocking failures on with_skill. Thinning did not drop refuse-gate or craft conformance under reference load.
- Tokens unavailable (timing.total_tokens null). Soft lint / live vault completeness not graded; outputs under workspace */outputs/ only.
- Bounds held: no SKILL.md / evals.json / live wiki edits; never checked out other worktrees for writes.
