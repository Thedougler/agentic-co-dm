# EVAL_AUTHOR_FLAGS — region-design iteration 1 (Batch A re-run after #138)

Workspace: `.agents/skills/region-design-workspace/iteration-1/`
Branch: `evals/batch-a-run-pr138`
Skill: `.agents/skills/region-design/` (SKILL.md **not** edited)
Live wiki: **not** edited; outputs under workspace only.

## Flags for eval authors

### F1 — Process assertions need durable artifacts
`Identity sentence appears before the page draft` and `Shows a chat proposal / work gate` cannot be graded from the page file alone. With-skill runs saved `outputs/agent_report.md`. Recommend eval author text (or grader.md note) require a process artifact path so without-skill failures are unambiguous and future runs stay comparable.

### F2 — Eval-2 is highly discriminating (keep)
Resist-invent cleanly separates skill vs baseline (4/4 vs 0/4). Keep as written. Optional tighten: assert that the response **must not** produce a rewritten `aruhe.md` body that embeds the invented threat — baseline failed by writing a full threat-update page.

### F3 — Eval-1 "Feared for" / thesis quality
Baseline still passes most content/structure assertions when the prompt names `region.md` and linked places. Discriminators are process + DM-thesis quality. Consider one more content assertion: At a Glance **Feared for** must cite taking/ecology (not vague "island waking") to catch soft invention drift.

### F4 — Eval-3 parent-region assignment
Baseline asserted `Parent region: Midchain` without labeling invention. With-skill left parent unassigned/proposed. Optional assertion: "Does not assign an established parent region as fact for a labeled invention entity."

### F5 — Eval-4 kernel retention
Without-skill kept `## Five-sentence kernel` and invented occupation/plague. Structure assertion already catches kernel-only failure. Good. Optional: assert "no `## Five-sentence kernel` section remains as primary body."

### F6 — Lint-clean vs template conformance (already documented)
CITATIONS.md correctly notes graders score **output** region.md conformance, not live `hard_fail=false`. No change needed; keep that note in grader briefs for Batch A.

### F7 — Timing provenance
This re-run recorded timing.json with estimated executor tokens/duration (inline executor; no subagent token notifications). If comparing to faction-design numbers, treat tokens as approximate until a subagent-instrumented re-run.

## Non-flags
- Assertion text in `evals/evals.json` / `eval_metadata.json` matches #138 retarget (Aruhe / Brine Ladder / Midchain unchanged targets) — no retarget bug found for region-design.
- Typed assertions only (no legacy expectations string arrays) — matches faction pattern bar.
