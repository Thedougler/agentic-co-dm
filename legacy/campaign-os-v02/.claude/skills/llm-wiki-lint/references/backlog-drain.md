# Backlog drain — leading the Haiku linter team

The procedure for a bare invocation (no specific request): the orchestrator
clears the lint backlog with waves of parallel Haiku subagents —
`content-fixer` for every `vault/**.md` file, `general-purpose` for
everything else (`utils/scripts/*.js|mjs`, `.claude/**`, `docs/**`).
Correctness outranks speed — the batch size starts at 1 file per subagent
and only grows on measured evidence. Main thread/orchestrator only: a
dispatched subagent never calls the Agent tool.

1. **DR1 — Autofix + size.** Run `npm run lint:sweep` (whole corpus: the
   autofix phase clears the mechanical subset for free), then paste its
   summary line and manifest. `DR1: <findings / files / rules>`.
2. **DR2 — Worklist.** `npm run lint:drain -- --limit 25` →
   file groups + duplication clusters. Split the groups: a file whose
   findings are ALL handoff-family (W25, W9, W13, W16, W17, W18, W27) goes
   to the handoff queue (SKILL.md's loop step 4 owns those — never a
   drain-wave subagent), everything else is drainable.
   `DR2: <drainable files, handoff files, clusters>`.
3. **DR3 — Dispatch the wave.** Up to 5 concurrent `Agent` calls in one
   message, `subagent_type: content-fixer` for a `vault/**.md` file or
   `general-purpose` otherwise, `model: haiku` explicit, never push. Each
   agent gets `<batch>` files (start: 1) with its exact finding list pasted
   from DR2; a duplication cluster always goes whole to one agent, never
   split, and counts as one slot whatever its file count.
   `DR3: <n agents × batch size>`.
4. **DR4 — Verify, independently.** A subagent's self-report is not
   evidence. After the wave returns:
   `node utils/scripts/rerun-check.mjs lint <every touched path>` — it runs
   the real report with `--fail-on any` and prints one VERDICT line. FAIL →
   redispatch only the still-dirty files (batch 1, fresh agent, current
   findings pasted); a file still dirty after its 2nd agent → stop on it and
   surface to the human (L5). `DR4: VERDICT + <redispatched, or none>`.
5. **DR5 — Adapt the batch.** Each completion notification carries the
   agent's token usage. Wave median < 10,000 tokens AND DR4 passed clean →
   double the batch for the next wave (1 → 2 → 4 → 8, cap 8). Any FAIL, any
   redispatch, or median ≥ 10,000 → halve back (floor 1) — correctness
   outranks throughput. `DR5: <median tokens → next batch size>`.
6. **DR6 — Close the wave.** `npm run lint:debt -- accept --force`,
   then commit the wave's files by explicit path (never `-A`) and push —
   the orchestrator pushes, subagents never do. `DR6: <ratchet delta, rules promoted>`.
7. **DR7 — Loop or land.** Findings remain that a drain-wave subagent may touch →
   back to DR2. Only handoff-family and human-ruling findings left → run
   SKILL.md's loop step 4 handoffs (cross-linker, canon-review,
   tag-taxonomy) and report what remains. `DR7: <looping | landed — remainder by rule>`.

Standing rules, every wave: findings are never silenced or reworded to dodge
a pattern (the rule's intent binds); fix order inside a file is structural +
wikilink rules before prose style — the report prints this; a canon/story
conflict a linter surfaces is never resolved by a linter agent (hand off,
DR2/DR7).
