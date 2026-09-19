# dnd-5e-magic-item-design benchmark — iteration 1 (Batch B)

Branch: `evals/batch-b-run-pr140`
Workspace: `.agents/skills/dnd-5e-magic-item-design-workspace/iteration-1/`
Worktree: `/home/box/wt-batch-b-spell/`
Skill: `.agents/skills/dnd-5e-magic-item-design/` (SKILL.md **not** modified)
Template: `wiki/templates/item.md` (live wiki **not** edited; outputs under workspace only)

## Aggregate

| Configuration | Mean pass rate | Mean tokens | Mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | 1.000 ± 0.000 | 37205 | 88.6 |
| without_skill | 0.042 ± 0.093 | 18550 | 44.2 |
| **delta** | **+95.8%** | **+100.6%** | **+100.5%** |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| fate-spinner-improve | 1.000 (8/8) | 0.250 (2/8) |
| fate-spinner-resist-invent | 1.000 (6/6) | 0.000 (0/6) |
| tideglass-compass-from-scratch | 1.000 (7/7) | 0.000 (0/7) |
| black-lotus-heart-flesh | 1.000 (7/7) | 0.000 (0/7) |
| create-a-rare-lantern | 1.000 (4/4) | 0.000 (0/4) |
| design-a-2024-rare | 1.000 (4/4) | 0.000 (0/4) |
| make-a-very-rare | 1.000 (4/4) | 0.000 (0/4) |
| write-a-sword-that | 1.000 (4/4) | 0.250 (1/4) |
| create-an-amulet-that | 1.000 (4/4) | 0.000 (0/4) |
| item-resist-invent | 1.000 (4/4) | 0.000 (0/4) |
| design-boots-that-make | 1.000 (3/3) | 0.000 (0/3) |
| combine-the-strongest-features | 1.000 (3/3) | 0.000 (0/3) |

## Analyst observations

- With-skill passes 58/58 assertions (mean pass_rate 1.0). Baseline 3/58 (mean 0.042).
- Largest deltas on resist-invent (eval-2) and craft anti-pattern evals 5–12: baseline complies with stacked/unbounded/secret-agency prompts; skill refuses and redesigns.
- Template evals 1/3/4: process (Signature/pitch, work gate) and structure/frontmatter discriminate; eval-1 baseline still preserves core Fate Spinner canon (1 content pass) while inventing stacked power.
- Eval-8 without_skill can pass 'states exact trigger…' while failing once-per-turn guardrail — content assertion is weaker alone; keep paired with guardrail.
- Eval-1 omit-if-empty At the Table: baseline passed by omission; consider requiring presence when improving a complex magic item, or mark N/A explicitly.
- With-skill costs more time/tokens (~duration delta); value is guardrail + process + craft refusal, not page length.
- Timing/token figures are inline-executor estimates (total_tokens null in timing.json; benchmark tokens from duration×420 heuristic for schema parity with Batch A).

## Assertion totals

- with_skill: **58 / 58** passed
- without_skill: **3 / 58** passed
