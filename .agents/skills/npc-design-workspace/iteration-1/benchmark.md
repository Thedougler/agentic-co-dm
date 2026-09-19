# npc-design benchmark — iteration 1 (Batch A re-run after #138)

Branch: `evals/batch-a-run-pr138`
Workspace: `.agents/skills/npc-design-workspace/iteration-1/`
Skill: `.agents/skills/npc-design/` (SKILL.md **not** modified)
Template: `wiki/templates/npc.md` (`role` ∈ rival|patron|contact; live wiki **not** edited)

## Aggregate

| Configuration | Mean pass rate | Mean tokens | Mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | 1.000 ± 0.000 | 33150 | 78.9 |
| without_skill | 0.090 ± 0.151 | 13734 | 36.1 |
| **delta** | **+91.0%** | **+141.4%** | **+118.6%** |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| varn-improve | 1.000 (7/7) | 0.429 (3/7) |
| varn-resist-invent | 1.000 (4/4) | 0.000 (0/4) |
| kell-drift-from-scratch | 1.000 (6/6) | 0.167 (1/6) |
| mave-sorn-flesh | 1.000 (6/6) | 0.333 (2/6) |
| write-a-fully-developed | 1.000 (3/3) | 0.333 (1/3) |
| create-an-npc-whose | 1.000 (3/3) | 0.000 (0/3) |
| the-bard-rolls-persuasion | 1.000 (3/3) | 0.000 (0/3) |
| add-an-expert-ally | 1.000 (3/3) | 0.000 (0/3) |
| the-campaign-villain-s | 1.000 (3/3) | 0.000 (0/3) |
| the-villain-appears-monologues | 1.000 (3/3) | 0.000 (0/3) |
| surprise-the-players-every | 1.000 (3/3) | 0.000 (0/3) |
| design-a-villain-who | 1.000 (3/3) | 0.000 (0/3) |
| build-the-villain-as | 1.000 (3/3) | 0.000 (0/3) |
| write-the-villain-s | 1.000 (3/3) | 0.000 (0/3) |

## Analyst observations

- With-skill passes all assertions across 14 evals (53/53). Baseline mean pass_rate 0.09 (7/53).
- Largest skill deltas on resist-invent (eval-2) and craft anti-pattern evals 5–14: baseline complies with anti-pattern prompts; skill refuses/redesigns.
- Template evals 1/3/4: process (role framing, work gate) and role-enum correction discriminate even when baseline content is partly decent.
- Eval-1 without_skill keeps lock-keeper canon but fails role correction, work gate, and adds unused History biography.
- Craft assertions are highly discriminating (often 1.0 vs 0.0): incidental scale, no lore-dump, persuasion≠mind control, limited ally, redundant clues, no cutscene immunity, rare betrayal, active plan, no PC-sheet boss, no predetermined redemption.
- With-skill costs more time (~+118.6% duration); value is guardrail + process + craft refusal, not page length.
- Timing/token figures are executor estimates (inline runs; no nested Claude subagent metrics). Tokens derived from duration heuristic for schema completeness.

## Assertion totals

- with_skill: **53 / 53** passed
- without_skill: **7 / 53** passed
