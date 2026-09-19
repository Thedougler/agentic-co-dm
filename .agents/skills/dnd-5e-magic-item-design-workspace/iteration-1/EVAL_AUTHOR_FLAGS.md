# EVAL_AUTHOR_FLAGS — dnd-5e-magic-item-design Batch B RE-SCORE (iteration-1)

Workspace: `.agents/skills/dnd-5e-magic-item-design-workspace/iteration-1/`
Worktree / branch: `/home/box/wt-batch-b-rescore/` · `evals/batch-b-rescore-pr149` (post-`6d53ff9` #149 + #148)
Skill: `.agents/skills/dnd-5e-magic-item-design/` (SKILL.md **not** edited)
Live wiki: **not** edited; outputs under workspace only.
Graders score **output** template conformance (not vault lint / live-page shape).
Citations: workspace `CITATIONS.md` + `.agents/skills/_eval-notes/batch-b-citations.md`
Prior run: Batch B on `evals/batch-b-run-pr140` (with 1.000 / without 0.042). This file is the **post-#149 re-score**.

## Pass rates (exact)

| Configuration | Mean pass rate | Assertions |
| --- | ---: | ---: |
| with_skill | **1.000** | 59 / 59 |
| without_skill | **0.000** | 0 / 59 |
| delta | **+100.0 pp** | — |

with_skill is **100%** after assertion tighten — success bar held.

## Keep (discriminating — stronger after #149)

1. **Eval-2 Fate Spinner resist-invent** — 1.0 vs 0.0. Secret body-control + Sentinels-as-forgers still primary template guardrail. Durable cite locus in transcript now explicit. Keep.
2. **Craft evals 5–12 anti-pattern / balance refusals** — all 1.0 vs 0.0 after tighten (eval-8 content no longer free-passes unbounded every-hit). Main discrimination engine. Keep.
3. **Process: Signature/pitch + work gate** (evals 1, 3, 4) — durable `transcript.md` locus. Keep; graders must read transcript.
4. **Eval-1 At the Table omit-if-empty ban** — #149 fixed baseline pass-by-absence (prior without 2/8 → now 0/8). Keep as written.
5. **Eval-1 tightened canon signals** — vague 'dreidel retained' / incomplete Changed Record limits now fail. Keep paired with guardrail.
6. **Eval-5 redesign hard-limit assertion** — new #149 assertion; with_skill charges/spend/tell vs without free always-on. Keep.
7. **Eval-8 content paired with once-per-turn** — #149 eliminated baseline content free-pass on unbounded riders. Keep both assertions paired.
8. **Eval-3 `invention: true` / Eval-4 canon vs invention / Eval-6 comparator / Eval-10 curse agency** — still discriminating. Keep.

## Fix / tighten — residual (none blocking)

1. **Eval-1 content + At-the-Table** — #149 addressed prior flags; re-score confirms discrimination. No further tighten needed this pass.
2. **Eval-8 content** — #149 addressed; re-score without 0/4. Keep paired with guardrail indefinitely.
3. **Craft evals 5/7/9 cost/limit** — eval-5 optional hard-limit assertion landed; 7/9 already covered by existing quality/guardrail. Optional only: mirror eval-5 hard-limit wording onto 7/9 if Eval Author wants symmetry.

## Non-discriminating / weak (post-#149 status)

| Assertion locus | Status after re-score |
| --- | --- |
| Eval-1 preserve-canon alone | **Fixed by #149** — now fails vague baseline; still keep paired with process/guardrail. |
| Eval-1 At the Table omit-if-empty | **Fixed by #149** — silent omit fails. |
| Eval-8 exact trigger/frequency content | **Fixed by #149** — unbounded every-hit fails content. |

No new weak free-passes observed on this re-score.

## Non-issues / do not inflate

- Do **not** edit production SKILL.md or live wiki based on this re-score.
- Do **not** add assertions that live `fate-spinner.md` already fills every template section — grade the **output**.
- Craft prompts that *invite* anti-patterns should continue to expect refusal/redesign (user bound).
- Flora/`hazard.md` ownership deferred per citations — out of scope this suite.

## Suite health (RE-SCORE)

| Eval | Assertions | with | without | Notes |
| --- | ---: | ---: | ---: | --- |
| 1 improve | 8 | 8/8 | 0/8 | #149 At-Table + canon tighten killed baseline free passes |
| 2 resist-invent | 6 | 6/6 | 0/6 | Primary template guardrail; cite locus in transcript |
| 3 from-scratch | 7 | 7/7 | 0/7 | Invention label + template + limits |
| 4 flesh | 7 | 7/7 | 0/7 | Canon/invention + harvest grounding |
| 5 rare lantern | 5 | 5/5 | 0/5 | +1 hard-limit assertion (#149) |
| 6 2024 rare | 4 | 4/4 | 0/4 | Comparator matrix |
| 7 very rare | 4 | 4/4 | 0/4 | Envelope trades |
| 8 sword rider | 4 | 4/4 | 0/4 | Content+guardrail both fail unbounded |
| 9 amulet | 4 | 4/4 | 0/4 | Concentration guardrail |
| 10 curse resist | 4 | 4/4 | 0/4 | Agency / tells |
| 11 boots travel | 3 | 3/3 | 0/3 | Travel-loop preservation |
| 12 combine rares | 3 | 3/3 | 0/3 | Rarity reassessment |

**Totals:** with_skill **59/59**; without_skill **0/59**.

## Comparison to pre-#149 Batch B

| Metric | Pre-#149 | Post-#149 RE-SCORE |
| --- | ---: | ---: |
| with_skill mean | 1.000 | **1.000** |
| without_skill mean | 0.042 | **0.000** |
| Assertion count | 58 | **59** (+eval-5 hard-limit) |
| Baseline free passes | eval-1 At-Table omit; eval-8 content | **eliminated** |

## Timing provenance

Inline executor re-score in worktree `/home/box/wt-batch-b-rescore` (no nested Claude subagent token notifications). `timing.json` uses `total_tokens: null` per run brief; `benchmark.json` fills approximate tokens from duration×420 heuristic for schema parity. Treat tokens as approximate.
