---
type: runbook
status: canon
publish: false
aliases: []
created: "2026-08-15"
updated: "2026-08-15"
tags: [craft]
summary: "Walking a Situation's Live Branches rows into a branching chain of Beats — the isolation loop, the isolation clause, and termination rules."
phase: any
uid: 486d3daf-74de-4af3-b9ea-4bac5ee87133
---

# Branch-isolation dispatch (walking a situation's live branches)

Drives the dispatch that writes a branching chain of Beats once a
Situation's Beat Chart names two or more Live Branches rows (the
collapse test lives in `.claude/skills/composing-beats/references/audits.md`
§ Branch collapse test). It never restates the contract for what a good
Beat contains — this pattern owns only the walk; the landing Beats belong
to their own `writing-*-beats` skills. Runs on top of § The sequence above
unchanged; this section adds only what is specific to walking a branch.

## Why isolate the branches

All branches out of a divergence are equally valid, and which one the
table takes is not predictable, so all of them get written. One author
holding every branch at once writes the branch they thought of first as
the main line and the rest as alternatives — the ranking then leaks into
the prose, and the DM reads a page that quietly tells them which way the
party is supposed to go.

Isolation removes the ability to rank. Each walker is handed one branch,
told it is the branch, and given no sibling's content. Equal validity is
enforced by what the agent cannot see, never by instructing it to be
even-handed.

## The loop

1. **Enumerate before walking.** The orchestrator writes every Live
   Branches row on the Beat Chart before dispatching anything. This is
   the only place the full branch set is visible, and a branch added
   after its siblings are written is a branch written to fit them.
2. **Reserve numbers.** Assign each walker its own block of numbering
   integers up front. Two walkers claiming the same integer is the one
   shared write this decomposes into, and reservation is what prevents
   it.
3. **Dispatch one agent per unwalked branch**, max 5 concurrent, queue
   the rest. Each brief carries: the Beat Chart's state condition for
   that branch, the session directory, its reserved number block, and
   the isolation clause below.
4. **Each walker stops at its next divergence.** It writes Beats down
   its branch until the fiction diverges again, adds that divergence's
   own Live Branches rows, and stops — reporting the new rows as
   unwalked. It never walks past its own divergence, and it never
   dispatches: a walker is a leaf worker (`vault/refs/runbook-agents.md`
   § Anti-patterns).
5. **The orchestrator dispatches the next wave** from the returned rows.
   Repeat until every branch terminates.
6. **Close each wave** per § The sequence step 4 above — `wave-verifier`
   PASS plus the orchestrator's own re-run of the touched paths' lint,
   both, neither alone.
7. **Back-populate in one pass, one agent, after every branch
   terminates.** Never let a walker set its own predecessor links on a
   Beat a sibling may own — writing to a Beat a sibling walker owns is
   the shared-write hazard the Decomposability check exists to catch.
   The pass reads every landing and every Live Branches row, appends
   each source to its target's predecessor field, and records branch
   depth as the count of divergences on the shortest route from the
   session's first Beat.

## The isolation clause

Every walker brief carries this verbatim:

```text
This branch is the branch the party takes. Write it as the primary line of
the session, not as an alternative to anything. You have not been given
the other branches out of this divergence and you must not read sibling
files to find them — that omission is deliberate, and reconstructing them
would defeat it.
```

## Termination

A branch ends in one of three ways, and a walker reports which:

- **Terminal.** The session ends here — no further link.
- **Rejoin.** The branch reaches a Beat that already exists. The walker
  links it and stops. It never edits that Beat — another walker owns it —
  and it reports the rejoin so the back-population pass records the extra
  predecessor.
- **New divergence.** Handled by step 4 above.

A walk with no termination rule is a walk that expands forever: every
brief states which of the three the walker expects, and a walker that has
written its reserved block without reaching one stops and reports rather
than claiming more numbers.

Done = every branch Terminal, Rejoined, or its new divergence dispatched
and itself resolved, the back-population pass complete, `wave-verifier`
PASS plus the orchestrator's own lint re-run both green per § The
sequence step 4, commit `<verb>(sNN): ...`.
