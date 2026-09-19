# npc-design benchmark — Phase 3 thin post-#155 verify

Verify time: 2026-09-19 ~08:22 PT

Branch: `evals/thin-npc-postmerge` @ `2802814` (includes #155 @ `448c72e`)
Skill: `.agents/skills/npc-design/SKILL.md` (114 lines) + `references/` (npc-craft.md etc.)
with_skill followed SKILL and loaded references when instructed. Suite evals **not** edited.

## Aggregate

| Config | mean pass rate | stddev | mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 83.8 |
| without_skill | 0.010 | 0.038 | 45.3 |
| delta | +99.0% |  |  |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| varn-improve | 7/7 (1.0) | 1/7 (0.1429) |
| varn-resist-invent | 4/4 (1.0) | 0/4 (0.0) |
| kell-drift-from-scratch | 6/6 (1.0) | 0/6 (0.0) |
| mave-sorn-flesh | 6/6 (1.0) | 0/6 (0.0) |
| write-a-fully-developed | 3/3 (1.0) | 0/3 (0.0) |
| create-an-npc-whose | 3/3 (1.0) | 0/3 (0.0) |
| the-bard-rolls-persuasion | 3/3 (1.0) | 0/3 (0.0) |
| add-an-expert-ally | 3/3 (1.0) | 0/3 (0.0) |
| the-campaign-villain-s | 3/3 (1.0) | 0/3 (0.0) |
| the-villain-appears-monologues | 3/3 (1.0) | 0/3 (0.0) |
| x-resist-invent | 3/3 (1.0) | 0/3 (0.0) |
| design-a-villain-who | 3/3 (1.0) | 0/3 (0.0) |
| build-the-villain-as | 3/3 (1.0) | 0/3 (0.0) |
| write-the-villain-s | 3/3 (1.0) | 0/3 (0.0) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)

Totals: with_skill 53/53; without_skill 1/53.

## Analyst observations

- Post-#155 thin verify: with_skill mean 1.000 (bar 1.000) → **HIT**; without_skill 0.010.
- Thinned SKILL.md keeps refuse-gates inline; craft detail in references/npc-craft.md — with_skill loaded references when SKILL instructed.
- Template evals 1–4: role enum + work gate + invention labeling still discriminate.
- Craft evals 5–14 anti-pattern refusals remain strong with_skill vs without_skill.
- Tokens unavailable (timing.total_tokens null). Soft lint / live vault completeness not graded; outputs under workspace */outputs/ only. No SKILL.md or live wiki/ edits.

## CoS recommendation

**KEEP #155** — with_skill mean 100%.
