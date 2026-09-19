# EVAL_AUTHOR_FLAGS — dnd-5e-magic-item-design Batch B (iteration-1)

Workspace: `.agents/skills/dnd-5e-magic-item-design-workspace/iteration-1/`
Worktree / branch: `/home/box/wt-batch-b-spell/` · `evals/batch-b-run-pr140`
Skill: `.agents/skills/dnd-5e-magic-item-design/` (SKILL.md **not** edited)
Live wiki: **not** edited; outputs under workspace only.
Graders score **output** template conformance (not vault lint / live-page shape).
Citations: workspace `CITATIONS.md` + `.agents/skills/_eval-notes/batch-b-citations.md`

## Keep (discriminating)

1. **Eval-2 Fate Spinner resist-invent** — 1.0 vs 0.0. Secret body-control curse + Sentinels-as-forgers as silent canon cleanly separates skill from baseline. Keep.
2. **Craft evals 5–12 anti-pattern / balance refusals** — nearly all 1.0 vs 0.0 (eval-8 baseline 0.25). Main discrimination engine. Keep as written.
3. **Process: Signature/pitch + work gate** (evals 1, 3, 4) — baseline skips; skill passes. Keep; require `transcript.md` for grading.
4. **Eval-3 `invention: true`** — discriminating; baseline presented Tideglass as vault relic.
5. **Eval-4 canon vs invention split** — catches silent ecology + undeclared curse.
6. **Eval-6 comparator matrix + no votes/ratings** — strong process/guardrail pair.
7. **Eval-10 curse agency / visible tells** — mirrors Fate Spinner resist theme at craft level; keep both.

## Fix / tighten

1. **Eval-1 "At the Table (if present)…"** — baseline passed by omission (no section). For improve-on-complex-magic, prefer requiring At the Table presence OR grade N/A explicitly so omit does not inflate baseline.
2. **Eval-1 "chat proposal / work gate"** — only verifiable via transcript. Document that graders must read `outputs/transcript.md`.
3. **Eval-8 "States exact trigger, damage, frequency…"** — baseline can pass while failing once-per-turn guardrail. Keep paired; do not rely on content assertion solo.
4. **Eval-1 content "Preserves Crissdalynn…"** — non-discriminating alone (baseline keeps core facts while inventing). Keep paired with guardrail/process.
5. **Craft evals without full item.md requirement** — intentional (anti-pattern redesigns). Optional: add one assertion on evals 5/7/9 that redesigned cards still name cost/limit (already mostly present).

## Non-discriminating / weak (flag for Eval Author)

| Assertion locus | Issue |
| --- | --- |
| Eval-1 "Preserves Crissdalynn / Kyzil / …" | Both configs can keep core canon; discrimination from process/guardrail. |
| Eval-1 At the Table omit-if-empty | Baseline pass-by-absence. |
| Eval-8 exact trigger/frequency content | Can pass on unbounded every-hit writeups. |

## Non-issues / do not inflate

- Do **not** add assertions that live `fate-spinner.md` already fills every template section — grade the **output**.
- Do **not** edit production SKILL.md or live wiki based on this run.
- Craft prompts that *invite* anti-patterns should continue to expect refusal/redesign (user bound).
- Flora/`hazard.md` ownership deferred per citations — out of scope this suite.

## Suite health

| Eval | Assertions | with | without | Notes |
| --- | ---: | ---: | ---: | --- |
| 1 improve | 8 | 8/8 | 2/8 | Process + structure + guardrail discriminate |
| 2 resist-invent | 6 | 6/6 | 0/6 | Primary template guardrail |
| 3 from-scratch | 7 | 7/7 | 0/7 | Invention label + template + limits |
| 4 flesh | 7 | 7/7 | 0/7 | Canon/invention + harvest grounding |
| 5 rare lantern | 4 | 4/4 | 0/4 | Pitch-first + no always-on |
| 6 2024 rare | 4 | 4/4 | 0/4 | Comparator matrix |
| 7 very rare | 4 | 4/4 | 0/4 | Envelope trades |
| 8 sword rider | 4 | 4/4 | 1/4 | Once-per-turn; content alone weak |
| 9 amulet | 4 | 4/4 | 0/4 | Concentration guardrail |
| 10 curse resist | 4 | 4/4 | 0/4 | Agency / tells |
| 11 boots travel | 3 | 3/3 | 0/3 | Travel-loop preservation |
| 12 combine rares | 3 | 3/3 | 0/3 | Rarity reassessment |

**Totals:** with_skill 58/58; without_skill 3/58.

## Timing provenance

Inline executor runs in worktree `/home/box/wt-batch-b-spell` (no nested Claude subagent token notifications). `timing.json` uses `total_tokens: null` per run brief; `benchmark.json` fills approximate tokens from duration×420 heuristic for schema parity with faction/Batch A. Treat tokens as approximate.
