# EVAL_AUTHOR_FLAGS — city-design Batch A re-score (post-#145)

Re-scored on `evals/batch-a-rescore-pr145` after assertion tighten (#145 @ ae11c9c). Soft lint / vault completeness correctly out of scope. Success bar: with_skill mean **1.000** — **HIT**.

## New from this re-score

- **No new Author-blocking failures** on with_skill (8/8, 4/4, 6/6, 11/11).
- **Eval-4 split content asserts** (Dravosi / Seven Houses / Paludi-Rattkin / Warren-Passage / Simone-Lavinia): with_skill 5/5, without_skill 0/5. Split improves diagnosability without weakening discrimination.
- **DM-thesis negative** (eval-1): without_skill plague-arc thesis correctly fails; with_skill function-in-play thesis passes. Keep.
- **Durable process locus** (process-notes.md / transcript.md): with_skill satisfies; without_skill omits identity sentence and work gate. Graders must read those artifacts, not only the page file.
- **Structure+substance companions**: both configs can still clear the floor when template headings are visible and partially filled — discrimination remains in process / guardrail / content. Optional future sharpen: require Orientation ≥2 *named function-linked* districts with non-placeholder pressure cells.

## Discriminating (keep)

- **Resist-invent plague/siege as canon** (eval-2): strongest discriminator (1.0 vs 0.0). Keep hostile prompt wording.
- **Closed S1 thread must stay closed** (eval-1 content + If-nobody-intervenes).
- **invention: true on from-scratch** (eval-3).
- **kind: settlement → kind: city upgrade** (eval-4).
- **Split canon preserves** (eval-4 five content asserts) — keep split form.
- **Identity sentence / work gate** with durable locus wording — keep post-#145 text.

## Non-discriminating / soft

- **Template structure with some fill** (evals 1,3,4): without_skill often still passes the substance floor. Useful as a floor, weak alone.
- **Frontmatter type:place kind:city** on improve/from-scratch when prompt names `wiki/templates/city.md`.

## Flaky / evidence-dependent

- Process asserts are **not** flaky when `process-notes.md` / `transcript.md` are required outputs of the executor. This re-score wrote both under each run's `outputs/`.

## Bounds held

- No SKILL.md edits. No live wiki/ writes. Workspace `*/outputs/` only. Did not touch Batch B / `wt-batch-b-spell` / main.
