# Benchmark — spell-design iteration-1 (Batch B)

Branch worktree: `/home/box/wt-batch-b-spell` (`evals/batch-b-run-pr140`).
Pattern: skill-creator with_skill vs without_skill → grade → aggregate.
Bounds held: no SKILL.md edits; no live wiki writes; no `wiki/entities/spell/` seeding; fixtures labeled non-canon.

## Aggregate

| Configuration | Mean pass rate | Stddev | Mean duration (s) | Mean tokens |
| --- | ---: | ---: | ---: | ---: |
| with_skill | **1.000** | 0.000 | 132.5 | n/a |
| without_skill | 0.122 | 0.092 | 64.0 | n/a |
| **delta** | **+87.8%** (pp) | — | +107.0% | n/a |

## Per-eval pass rates

| Eval | with_skill | without_skill |
| --- | ---: | ---: |
| spell-fixture-improve | 9/9 (1.000) | 2/9 (0.222) |
| spell-craft-anti-pattern | 5/5 (1.000) | 0/5 (0.000) |
| ledgerbind-from-scratch | 8/8 (1.000) | 1/8 (0.125) |
| spell-fixture-flesh | 7/7 (1.000) | 1/7 (0.143) |

## Analyst observations

- With-skill passes 100% of assertions across all four evals; without-skill mean pass rate ~0.122 — discriminating delta (+87.8 pp) driven by process (identity sentence, work gate), invention labeling, scroll-item guardrail, and resist-invent.
- Eval 2 (craft anti-pattern / resist inventing ancient-druids-taking-spell as Taking origin) is the sharpest discriminator: with_skill 5/5, without_skill 0/5. Baseline complies with the hostile prompt and files Claimbind as Current Truth.
- Eval 1 (Saltwake fixture improve) without_skill cites spell-scroll-fog-cloud.md as exemplar and files as canon — scroll-item guardrail + invention label discriminate; structure floor alone is weak (baseline still gets casting headings + premise).
- Eval 3 (Ledgerbind from-scratch) without_skill fails invention:true, identity/work gate, and runnable seal effect — only casting-field presence passes. Keep quality assertion requiring contested check / fail / end.
- Eval 4 (Red Wake Knell flesh) without_skill bleeds Taking-on-Aruhe metaphysics into Umberlee doctrine as Current Truth and cites spell-scroll-locate-creature — guardrails discriminate; stub-premise preservation alone is non-discriminating.
- Fixtures correctly treated as labeled work drafts — no wiki/entities/spell/ folder created; outputs only under workspace */outputs/.
- Tokens unavailable (timing.total_tokens null; inline-executor). Duration: with_skill mean ~132.5s vs without ~64.0s (~+107.0%) — extra cost is process notes + fuller template fill.
- Process assertions need process-notes.md (or transcript) as evidence locus — same Batch A author flag.
