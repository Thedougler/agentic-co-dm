# EVAL_AUTHOR_FLAGS — npc-design Batch A (iteration-1)

Workspace: `.agents/skills/npc-design-workspace/iteration-1/`
Branch: `evals/batch-a-run-pr138`
Skill: `.agents/skills/npc-design/` (SKILL.md **not** edited)
Live wiki: **not** edited; outputs under workspace only.
Graders score **output** template conformance (not vault lint / live-page shape).

## Keep (discriminating)

1. **Eval-2 resist-invent guardrails** — strongest template-suite delta (1.0 vs 0.0). Prompt that demands Crown-betrayal biography as canon cleanly separates skill from baseline. Keep.
2. **Craft evals 5–14 anti-pattern refusals** — nearly all show 1.0 vs 0.0 (or near-zero). These are the suite's main discrimination engine. Keep as written.
3. **Process: function/role framing + work gate** (evals 1, 3) — baseline skips; skill passes. Keep as process-type assertions; require `transcript.md` (or agent_report) for grading.
4. **Role enum correction (eval-1)** — catches leaving `role: "Inner lock keeper"`. Keep; this was the #138 Varn retarget point.
5. **Eval-3 `invention: true`** — discriminating; baseline presented Kell as accepted without label.
6. **Eval-4 canon vs invention split** — catches silent long biography + invalid role string.

## Fix / tighten

1. **Eval-1 structure assertion** — baseline can still pass At a Glance/Running via copy-forward from live page while failing role/process. Consider requiring Connections present OR explicit `role` enum in frontmatter as a separate must-pass (already partly covered by role assertion).
2. **Eval-1 "chat proposal / work gate"** — only verifiable via transcript. Document that graders must read `outputs/transcript.md`. Same note as region/lore flags.
3. **Eval-1 content want/leverage** — baseline passed with thinner leverage/need. Optional tighten: require explicit leverage *and* need labeled in output (not only posture-change limit).
4. **Eval-5 "portrayal signal"** — baseline scraped a pass via personality color in a novel biography. Tighten to require a *present-tense scene signal* (visual/behavior/sample line usable in the stew scene), not backstory flavor.
5. **Eval-4 "preserves Velvet Noose…"** — non-discriminating alone (baseline keeps stub facts while inventing biography). Keep paired with guardrail assertions; do not rely on it solo.
6. **Craft evals without NPC template requirement** — intentional (anti-pattern redesigns). Optional: add one assertion on evals 6/8/12 that redesigned cards still name want+leverage (already mostly present in quality assertions).

## Non-discriminating / weak (flag for Eval Author)

| Assertion locus | Issue |
| --- | --- |
| Eval-1 "Preserves inner lock keeper identity…" | Both configs pass when not asked to invent — weak discriminator. |
| Eval-4 "Preserves Velvet Noose / broker / want" | Both configs pass; discrimination comes from role/structure/guardrails. |
| Eval-5 "Includes immediate want and portrayal signal" | Baseline can pass via biography flavor; tighten wording (see Fix #4). |

## Non-issues / do not inflate

- Do **not** add assertions that live `varn.md` / `mave-sorn.md` already fill every template section — Linter soft-clean ≠ full template fill; grade the **output**.
- Do **not** edit production SKILL.md or live wiki based on this run.
- Craft prompts that *invite* anti-patterns should continue to expect refusal/redesign (user bound).

## Suite health

| Eval | Assertions | with | without | Notes |
| --- | ---: | ---: | ---: | --- |
| 1 improve | 7 | 7/7 | 3/7 | Process + role enum discriminate |
| 2 resist-invent | 4 | 4/4 | 0/4 | Primary template guardrail |
| 3 from-scratch | 6 | 6/6 | 1/6 | Invention label + template + role |
| 4 flesh | 6 | 6/6 | 2/6 | Canon/invention + structure |
| 5 incidental | 3 | 3/3 | 1/3 | Scale guardrail |
| 6 no lore-dump | 3 | 3/3 | 0/3 | Strong |
| 7 persuasion | 3 | 3/3 | 0/3 | Strong |
| 8 limited ally | 3 | 3/3 | 0/3 | Strong |
| 9 redundant clues | 3 | 3/3 | 0/3 | Strong |
| 10 no cutscene | 3 | 3/3 | 0/3 | Strong |
| 11 rare betrayal | 3 | 3/3 | 0/3 | Strong |
| 12 active plan | 3 | 3/3 | 0/3 | Strong |
| 13 no PC sheet | 3 | 3/3 | 0/3 | Strong |
| 14 no forced redemption | 3 | 3/3 | 0/3 | Strong |

**Totals:** with_skill 53/53; without_skill 7/53.

## Timing provenance

Inline executor runs (no nested Claude subagent token notifications). `timing.json` uses `total_tokens: null` at write time; benchmark.json fills approximate tokens from a duration heuristic for schema parity with faction/lore. Treat tokens as approximate.
