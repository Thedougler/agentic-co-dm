# EVAL_AUTHOR_FLAGS — city-design thin Phase 3 post-#152 verify

Re-scored on `evals/thin-city-postmerge` @ `5e21149` after #152 thin merge (`b2e6114`) on main tip (also #153, #154). Suite = post-#151 `evals/evals.json` (10 evals) — **not edited**. Soft lint / vault completeness out of scope. Success bar: with_skill mean **1.000** — **HIT**.

## Gate result

| Metric | Threshold | Observed | Result |
| --- | ---: | ---: | --- |
| with_skill mean pass rate | 1.000 | **1.000** | **HIT** |
| without_skill mean | (discriminator) | 0.067 | sharp |
| Recommendation | | | **KEEP merge #152** |

## New from this verify

- **No with_skill assertion failures** across 10/10 evals (57/57 assertions).
- Thinned `SKILL.md` (~102 lines) keeps refuse-gates in-body; craft detail in `references/city-craft.md`. with_skill runs record both loads in `process-notes.md` / `transcript.md`.
- Adversarial evals 5–10 (forced rail, PC civic fiat, secrets-in-Arrival, single-lever, skip-gate, combat-only) remain with_skill 1.0 / without_skill 0.0.
- Craft evals 1/3/4 still clear structure+substance under reference load; process identity sentence + work gate still discriminate.

## Discriminating (keep)

- Resist-invent plague/siege as canon (eval-2) and related Mercatura resists (5/8/9).
- Calven adversarial 6/7/10 (PC civic fiat, secrets-in-Arrival, combat-only).
- Closed S1 thread must stay closed (eval-1 content + If-nobody-intervenes).
- `invention: true` on from-scratch (eval-3).
- `kind: settlement → kind: city` upgrade (eval-4) + split canon preserves.
- Durable process locus wording (process-notes / transcript).

## Non-discriminating / soft

- Template structure with some fill (evals 1,3,4): without_skill can still clear a weak floor; discrimination remains in process/guardrail/content.

## Thinning-specific note

- Gate risk for #152 was with_skill agents skipping `references/city-craft.md`. This verify's with_skill process artifacts explicitly load craft per SKILL instruction; refuse-gates did not need the reference file (they remain in SKILL). **No REVERT signal.**

## Bounds held

- No SKILL.md edits. No `evals/evals.json` edits. No live `wiki/` writes. Workspace `*/outputs/` only. Did not checkout other worktrees for this verify's writes.
