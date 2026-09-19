# npc-design benchmark — Batch A re-score post-#145

Rescore time: 2026-09-19 ~01:15 PT (Batch A re-score post-#145)

Branch: `evals/batch-a-rescore-pr145` (includes #145 @ ae11c9c)

## Aggregate

| Config | mean pass rate | stddev | mean duration (s) |
| --- | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 89.4 |
| without_skill | 0.022 | 0.054 | 49.6 |
| delta | +97.8% |  |  |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| varn-improve | 7/7 (1.0) | 1/7 (0.1429) |
| varn-resist-invent | 4/4 (1.0) | 0/4 (0.0) |
| kell-drift-from-scratch | 6/6 (1.0) | 0/6 (0.0) |
| mave-sorn-flesh | 6/6 (1.0) | 1/6 (0.1667) |
| write-a-fully-developed | 3/3 (1.0) | 0/3 (0.0) |
| create-an-npc-whose | 3/3 (1.0) | 0/3 (0.0) |
| the-bard-rolls-persuasion | 3/3 (1.0) | 0/3 (0.0) |
| add-an-expert-ally | 3/3 (1.0) | 0/3 (0.0) |
| the-campaign-villain-s | 3/3 (1.0) | 0/3 (0.0) |
| the-villain-appears-monologues | 3/3 (1.0) | 0/3 (0.0) |
| surprise-the-players-every | 3/3 (1.0) | 0/3 (0.0) |
| design-a-villain-who | 3/3 (1.0) | 0/3 (0.0) |
| build-the-villain-as | 3/3 (1.0) | 0/3 (0.0) |
| write-the-villain-s | 3/3 (1.0) | 0/3 (0.0) |

## Success bar

with_skill mean pass rate 100%: **HIT** (1.0)

Totals: with_skill 53/53; without_skill 2/53.

## Analyst observations

- Re-score after #145: with_skill mean pass rate 1.000 (success bar 1.000); without_skill 0.022.
- Process asserts now require durable locus (process-notes.md / transcript.md); with_skill records function/role framing + work gate there; without_skill omits or drafts directly.
- Eval-1 content compound (salt-stiff / "This gate is mine" / dock-runner limit + role enum) and labeled leverage AND need: with 7/7; without 1/7 (structure floor only).
- Eval-2 resist-invent still sharpest template discriminator (1.0 vs 0.0); grounding+contradictions now must appear in process locus.
- Eval-4 specific Velvet Noose canon (clean captain / sealed case / supernatural confirm / files-to-sell / Perrin's pact): with 6/6; without keeps some broker text but fails role/structure/guardrails (1/6).
- Eval-5 present-tense *scene* signal (not backstory flavor): with 3/3; without 0/3 — #145 tighten removes prior baseline scrape.
- Craft evals 6–14 anti-pattern refusals remain 1.0 vs 0.0 across the board.
- Tokens unavailable (timing.total_tokens null). Soft lint / live vault completeness not graded; outputs under workspace */outputs/ only. No SKILL.md or live wiki/ edits.
