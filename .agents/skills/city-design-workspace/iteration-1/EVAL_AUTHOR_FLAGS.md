# EVAL_AUTHOR_FLAGS — city-design Batch A re-score (post-#151)

Re-scored on `evals/batch-a-crl-rescore-pr151` after session-beats adversarial uplift (#151 @ 5256033). Soft lint / vault completeness correctly out of scope. Success bar: with_skill mean **1.000** — **HIT**.

## New from this re-score

- **Suite 4→10.** Added evals 5–10 (forced rail, PC civic fiat, secrets-in-Arrival, single-lever vault, skip-gate+plague, combat-only rail). All with_skill **1.0**; all without_skill **0.0**.
- **No new Author-blocking failures** on with_skill (10/10 evals at 100% assertion pass).
- **Adversarial discrimination is sharp:** new refuse-shaped prompts fully separate skill from baseline (mean without_skill pulled down vs post-#145 0.169).
- **Evals 1–4** unchanged assertions from #145 — carried forward; still 1.0 with_skill.

## Discriminating (keep)

- **Resist-invent plague/siege as canon** (eval-2): still perfect discriminator.
- **Forced single plot rail** (eval-5): keep hostile docks→memorial→vault→duke wording.
- **PC civic fiat as page fact** (eval-6): keep party-duke / dissolved leverage / Simone-steward wording.
- **Secrets/DCs in Arrival** (eval-7): keep DC 18 + toxin-lab + loyalty-in-narration prompt.
- **Clue-less single lever** (eval-8): keep sealed-vault / session-stop wording.
- **Skip work gate + unmarked plague/districts** (eval-9): keep skip-proposal + silent wiki/ framing.
- **Combat-only six-fight rail** (eval-10): keep no-social/investigate/travel/recovery wording.
- **Closed S1 thread must stay closed** (evals 1, 5, 8).
- **Durable process locus** (process-notes.md / transcript.md) — keep post-#145 text.
- **Split canon preserves** (eval-4 five content asserts) — keep split form.

## Non-discriminating / soft

- **Template structure with some fill** (evals 1, 3, 4): without_skill can still clear substance floor on craft prompts — useful as floor, weak alone. New adversarial evals do not rely on it.
- **Frontmatter type:place kind:city** when prompt names `wiki/templates/city.md`.

## Flaky / evidence-dependent

- Process asserts are **not** flaky when `process-notes.md` / `transcript.md` are required outputs. This re-score wrote both under each run's `outputs/`.

## Bounds held

- No SKILL.md edits. No live wiki/ writes. Workspace `*/outputs/` only. Did not touch Batch B / `wt-batch-b-spell` / main.
