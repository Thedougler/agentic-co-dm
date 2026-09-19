# EVAL_AUTHOR_FLAGS — region-design Batch A re-score (post-#145)

Re-scored on `evals/batch-a-rescore-pr145` after assertion tighten (#145 @ ae11c9c). Soft lint / vault completeness correctly out of scope. Success bar: with_skill mean **1.000** — **HIT**.

Workspace: `.agents/skills/region-design-workspace/iteration-1/`
Skill: `.agents/skills/region-design/` (SKILL.md **not** edited)
Live wiki: **not** edited; outputs under workspace only.
Prior run artifacts restored from `0baa2f8` and re-graded against tightened `eval_metadata.json`.

## New from this re-score

- **No new Author-blocking failures** on with_skill (9/9, 5/5, 7/7, 6/6).
- **Durable process locus** (process-notes.md / agent_report.md / transcript.md): with_skill `agent_report.md` satisfies identity + work gate; without_skill omits all three. Graders must read those artifacts, not only the page file.
- **Eval-1 Feared-for** (F3): with_skill cites taking/razer-grass; without_skill fails on vague "island waking". Keep — sharp quality discriminator.
- **Eval-2 threat-embedded rewrite ban** (F2): with_skill response-only 5/5; without_skill `aruhe-threat-update.md` fails. Keep hostile prompt + rewrite ban.
- **Eval-3 parent-region invent label** (F4): with_skill leaves Parent unassigned/proposed; without_skill asserts Midchain as fact. Keep.
- **Eval-4 Five-sentence kernel ban** (F5): with_skill full region.md; without_skill retains `## Five-sentence kernel (retained)`. Keep explicit ban wording.
- **Structure+substance companions**: both configs can still clear the floor when template headings are visible and partially filled — discrimination remains in process / guardrail / quality.

## Discriminating (keep)

- **Resist-invent ancient evil / warlord as canon** (eval-2): strongest discriminator (1.0 vs 0.0). Keep hostile prompt wording + rewrite ban.
- **Identity sentence / work gate** with durable locus wording — keep post-#145 text.
- **invention: true on from-scratch** (eval-3) + Fronts none-established / labeled.
- **Parent region not silently assigned** for invention entities (eval-3).
- **No occupation/plague as silent canon** + kernel must not remain primary body (eval-4).
- **Feared for cites taking/ecology** (eval-1) — catches soft invention drift.

## Non-discriminating / soft

- **Template structure with some fill** (evals 1,3): without_skill often still passes the substance floor. Useful as a floor, weak alone.
- **Frontmatter type:region + scale/kind/summary** when prompt names `wiki/templates/region.md`.
- **Named place roles** (Slack Basin / Cutoff Lip / Print Braid) when prompt names the place pages.

## Flaky / evidence-dependent

- Process asserts are **not** flaky when `agent_report.md` / `process-notes.md` / `transcript.md` are required outputs of the executor. This re-score grades prior with_skill `agent_report.md` artifacts; without_skill still has none.

## Bounds held

- No SKILL.md edits. No live wiki/ writes. Workspace `*/outputs/` only. Did not touch Batch B / `wt-batch-b-spell` / main.
