# EVAL_AUTHOR_FLAGS — lore-design Batch A (iteration-1)

Flags for Eval Author after grading. Graders score **output** template conformance (not live-page shape).

## Keep (discriminating)

1. **Eval-2 resist-invent guardrails** — strongest skill delta (1.0 vs 0.2). Prompt that demands a metaphysical "real answer" as Current Truth correctly separates skill from baseline.
2. **Process: durable question + work gate** (evals 1, 3, 4) — baseline reliably skips these; skill passes. Keep as process-type assertions.
3. **Eval-4 rumour≠Current Truth** — catches promotion of dock talk / sailor theory; keep paired with Accounts vs Current Truth expectation.
4. **Eval-3 `invention: true`** — discriminating; baseline presented Midchain custom as established.

## Fix / tighten

1. **Eval-1 structure vs live callout shape** — assertion asks for lore.md structure; baseline still passed via callout-form At a Glance matching the live page. Consider requiring heading-form `## At a Glance` (or explicit frontmatter `kind`+`truth`) so improve runs cannot pass on pre-template copy-forward alone.
2. **Eval-1 "chat proposal / work gate"** — only verifiable via transcript/agent report, not the page file. Document that graders must read `transcript.md` (or require a `## Work gate` block in workspace output). Otherwise process assertion is soft.
3. **Eval-3 "one durable question"** — baseline failed by bundling berth/pilot/salvage; good. Optionally add a negative assertion: "does not claim a named vault harbour already uses this custom."
4. **Eval-4 Discovery invention labeling** — works; consider requiring the word `proposed` or `invention` on any clue not present on the stub (checklist item text match).

## Non-issues / do not inflate

- Do **not** add assertions that the live `taking-on-aruhe.md` already fills every template section — Linter hard_fail=false is expected; grade the **output**.
- Eval-2 should continue to forbid promoting rumour/invention to Current Truth (user bound for this re-run).

## Suite health

| Eval | Assertions | with | without | Notes |
| --- | ---: | ---: | ---: | --- |
| 1 improve | 8 | 8/8 | 5/8 | Process + frontmatter discriminate |
| 2 resist-invent | 5 | 5/5 | 1/5 | Primary guardrail eval |
| 3 from-scratch | 6 | 6/6 | 3/6 | Invention label + single question |
| 4 flesh | 6 | 6/6 | 3/6 | Rumour split + proposed Discovery |

No eval looked trivially always-pass for both configs. Eval-1 content/guardrail items are weaker discriminators (baseline keeps fallen-vs-living when not asked to invent).
