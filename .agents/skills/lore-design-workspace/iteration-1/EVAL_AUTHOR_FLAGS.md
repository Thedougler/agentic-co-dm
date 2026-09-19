# EVAL_AUTHOR_FLAGS — lore-design Batch A re-score (post-#145)

Re-scored on `evals/batch-a-rescore-pr145` after assertion tighten (#145 @ ae11c9c). Soft lint / vault completeness correctly out of scope. Success bar: with_skill mean **1.000** — **HIT**.

## New from this re-score

- **No new Author-blocking failures** on with_skill (9/9, 5/5, 7/7, 7/7).
- **Eval-1 heading-form At a Glance** (post-#145): without_skill callout copy-forward correctly fails; with_skill heading-form passes. Keep — this was the Fix item from the prior author flags.
- **Eval-3 vault-harbour negative** ("does not claim a named vault harbour already uses this custom"): without_skill Kalowe/Midchain claim fails; with_skill explicit non-claim passes. Keep.
- **Eval-4 Discovery proposed/invention wording**: without_skill unlabeled new clues fail; with_skill labels tide-chapel / chalk clues. Keep.
- **Durable process locus** (process-notes.md / transcript.md): with_skill satisfies; without_skill omits durable question and work gate. Graders must read those artifacts, not only the page file.

## Discriminating (keep)

- **Resist-invent metaphysical cause as Current Truth** (eval-2): strongest discriminator (1.0 vs 0.2). Keep hostile "real answer" prompt wording.
- **invention: true on from-scratch** (eval-3) paired with vault-harbour negative.
- **Rumour ≠ Current Truth** + Accounts split (eval-4).
- **Durable question / work gate** with durable locus wording — keep post-#145 text.
- **Heading-form vs callout copy-forward** (eval-1 structure) — keep; closes prior improve loophole.

## Non-discriminating / soft

- **Template structure with some fill** (evals 3, 4): without_skill can still clear the substance floor when headings are visible and partially filled — discrimination remains in process / guardrail / content.
- **Eval-1 content/guardrail** (fallen-vs-living; no metaphysics) when the prompt does not ask to invent — baseline often still passes.

## Flaky / evidence-dependent

- Process asserts are **not** flaky when `process-notes.md` / `transcript.md` are required outputs of the executor. This re-score wrote both under each run's `outputs/`.
- ### Limits under Current Truth (template) vs assertion text saying `## Limits`: graders should accept template `### Limits` as the Limits section. Optional author polish: align assertion wording to `### Limits` under Current Truth.

## Bounds held

- No SKILL.md edits. No live wiki/ writes. Workspace `*/outputs/` only. Did not touch Batch B / main / other skill workspaces' unfinished runs.
