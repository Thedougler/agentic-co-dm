# Contract: Skill Design Dispatch

The interface is an instruction edit. The session agent classifies before write. Naming the wrong writer is a fail.

## Gate

Design-impact if the change would alter skill triggering, workflow ownership, standing load, or would create a skill or subagent. Length does not decide. Borderline of those four is `not` (session agent). Claude Code opus is ONLY for making skills, writing agent instructions, or writing wiki templates. Campaign wiki pages, session content, constitution, specs, code, and filling a page from a template are out of this routing.

| Class | Writer |
|---|---|
| design-impact | designated writer |
| not | session agent |
| owner explicitly skips dispatch | session agent |
| file out of scope | this routing does not apply |

## Classification jobs

A second reviewer must name the same class and writer (SC-001). At least these twelve:

| # | Edit | Class | Writer |
|---|---|---|---|
| 1 | Typo in a skill body | not | session agent |
| 2 | Path fix in a skill | not | session agent |
| 3 | Named value change that does not change who does a step | not | session agent |
| 4 | Clarifying sentence that does not change who does what | not | session agent |
| 5 | Long mechanical reorder, no behavior change | not | session agent |
| 6 | Skill `description` / trigger rewrite | design-impact | designated writer |
| 7 | New skill | design-impact | designated writer |
| 8 | New subagent definition | design-impact | designated writer |
| 9 | Always-loaded `AGENTS.md` table or rule | design-impact | designated writer |
| 10 | Move a step from one skill to another | design-impact | designated writer |
| 11 | Mixed: typo plus trigger rewrite | split: typo `not`; trigger `design-impact` | session agent does typo only |
| 12 | Feature spec or generated Spec Kit adapter | out-of-scope | existing authoring loop |

Additional jobs the same reviewers should also agree on:

| # | Edit | Class | Writer |
|---|---|---|---|
| 13 | Sticky rule in `RULES.md` | design-impact | designated writer |
| 14 | Campaign wiki page | out-of-scope | existing authoring loop |
| 15 | Trigger rewrite, owner says skip dispatch | design-impact, overruled | session agent |
| 16 | Trigger rewrite, designated writer unavailable | design-impact | parked; files untouched |
| 17 | Trigger rewrite, usage limit with reset time | design-impact | usage-limited; retry time = that reset; no parked dispatch; do not retry before it |
| 18 | Usage limit with no reset time | design-impact | usage-limited; retry time = 5 hours from the stop; no parked dispatch |
| 19 | Retry still usage-limited, no reset time | design-impact | usage-limited; next retry time = 24 hours from that attempt; no parked dispatch |

## Dispatch rules

1. Classify before any in-scope target changes.
2. Non-design-impact: session agent completes it; no parked issue.
3. Design-impact: session agent does not write the targets. Scoped prompt names outcome, files, bounds.
4. Designated writer is the sole writer of a change that lands.
5. Writer cannot start, stops, refuses, or errors for a reason other than a usage limit: restore targets to dispatch-start content; park `Parked skill design: <outcome>` with `ready-for-agent` and the scoped prompt; session agent does not finish the design.
6. Usage limit: that specific job is incomplete with a retry time (reset time from the report, else 5 hours from the stop, then 24 hours if still limited). Do not create parked dispatch. Do not re-attempt before that time; a new session retries after it. Other in-session jobs are not marked incomplete for that reason.
7. After success: session agent verifies targets ⊆ in-scope and outcome met; does not rewrite.
8. Search existing `Parked skill design:` issues before creating another for the same job.
9. Routing applies even when `skill-creator` / `omp-harness` were not loaded.
10. Constitution, specs, generated adapters, wiki stay out.

## Out of contract

How the designated writer designs. Constitution amendment. Spec Kit specify/plan/tasks loops. A new skill whose only job is this gate. A wrapper CLI around `claude` or `gh`.
