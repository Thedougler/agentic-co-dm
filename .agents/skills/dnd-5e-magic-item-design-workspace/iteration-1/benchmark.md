# dnd-5e-magic-item-design benchmark — iteration 1 (Batch B RE-SCORE)

Branch: `evals/batch-b-rescore-pr149` @ post-`6d53ff9` (#149 tighten) + #148 suites
Workspace: `.agents/skills/dnd-5e-magic-item-design-workspace/iteration-1/`
Worktree: `/home/box/wt-batch-b-rescore/`
Skill: `.agents/skills/dnd-5e-magic-item-design/` (SKILL.md **not** modified)
Template: `wiki/templates/item.md` (live wiki **not** edited; outputs under workspace only)

## Aggregate

| Configuration | Mean pass rate | Mean tokens | Mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | 1.000 ± 0.000 | 37590 | 89.5 |
| without_skill | 0.000 ± 0.000 | 16240 | 38.7 |
| **delta** | **+100.0 pp** | **+131.5%** | **+131.5%** |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| fate-spinner-improve | 1.000 (8/8) | 0.000 (0/8) |
| fate-spinner-resist-invent | 1.000 (6/6) | 0.000 (0/6) |
| tideglass-compass-from-scratch | 1.000 (7/7) | 0.000 (0/7) |
| black-lotus-heart-flesh | 1.000 (7/7) | 0.000 (0/7) |
| create-a-rare-lantern | 1.000 (5/5) | 0.000 (0/5) |
| design-a-2024-rare | 1.000 (4/4) | 0.000 (0/4) |
| make-a-very-rare | 1.000 (4/4) | 0.000 (0/4) |
| write-a-sword-that | 1.000 (4/4) | 0.000 (0/4) |
| create-an-amulet-that | 1.000 (4/4) | 0.000 (0/4) |
| target-resist-invent | 1.000 (4/4) | 0.000 (0/4) |
| design-boots-that-make | 1.000 (3/3) | 0.000 (0/3) |
| combine-the-strongest-features | 1.000 (3/3) | 0.000 (0/3) |

## Analyst observations (RE-SCORE)

- With-skill passes **59/59** assertions (mean pass_rate **1.000**). Baseline **0/59** (mean **0.000**).
- #149 tightenings held: durable process locus (transcript), At-the-Table omit-if-empty ban, eval-8 content paired with once-per-turn, eval-5 redesign hard-limit assertion, tightened Fate Spinner canon signals.
- Prior baseline free passes eliminated: eval-1 At-the-Table silent omit + vague canon preserve; eval-8 unbounded every-hit 'frequency' content pass.
- with_skill remains **100%** after tighten — success bar held.
- Timing/token figures are inline-executor estimates (`total_tokens: null` in timing.json; benchmark tokens from duration×420 heuristic).

## Assertion totals

- with_skill: **59 / 59** passed
- without_skill: **0 / 59** passed
