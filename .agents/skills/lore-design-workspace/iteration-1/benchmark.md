# lore-design benchmark — iteration 1 (Batch A re-run after #138)

Branch: `evals/batch-a-run-pr138`
Workspace: `.agents/skills/lore-design-workspace/iteration-1/`
Skill: `.agents/skills/lore-design/` (SKILL.md **not** modified)
Template: `wiki/templates/lore.md` (live wiki **not** edited)

## Aggregate

| Configuration | Mean pass rate | Mean tokens | Mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | 1.000 ± 0.000 | 40250 | 91.8 |
| without_skill | 0.456 ± 0.181 | 25000 | 54.0 |
| **delta** | **+54.4%** | **+61.0%** | **+70.0%** |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| taking-on-aruhe-improve | 1.000 (8/8) | 0.625 (5/8) |
| taking-on-aruhe-resist-invent | 1.000 (5/5) | 0.200 (1/5) |
| pier-debt-custom-from-scratch | 1.000 (6/6) | 0.500 (3/6) |
| taken-whole-flesh | 1.000 (6/6) | 0.500 (3/6) |

## Analyst observations

- With-skill passes all assertions across 4 evals (25/25). Baseline mean pass_rate 0.456 (12/25).
- Largest skill delta on eval-2 resist-invent: with_skill 1.0 vs without_skill 0.2 — baseline invents fungal network as Current Truth when prompted for 'the real answer'.
- Process assertions (durable question, work gate) discriminate improve/from-scratch/flesh: baseline fails them even when content quality is decent (eval-1 content mostly preserved).
- Eval-3 invention labeling and single-question discipline fail without skill (truth:established + Midchain scope; bundles berth/pilot/salvage).
- Eval-4 without_skill keeps Dead Lady/Umberlee names but promotes dock rumour into Current Truth and adds unlabeled Discovery vectors — guardrail assertions catch this.
- With-skill costs ~61% more tokens and ~70% more time; value is guardrail + process, not raw page length.
- Timing/token figures are executor estimates (inline runs; no nested Claude subagent metrics available on this box).

## Assertion totals

- with_skill: **25 / 25** passed
- without_skill: **12 / 25** passed
