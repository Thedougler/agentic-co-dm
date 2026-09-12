---
type: runbook
status: canon
publish: false
aliases: []
created: "2026-07-23"
updated: "2026-07-23"
tags: [survival, travel]
summary: "Any friction with this repo's own Claude Code setup — not feature code or campaign content — routed through Observe → Diagnose → Fix → Prove, live or unattended."
phase: any
uid: 0af84c8e-1942-4525-8551-2c3d01091350
---

# Self-improve runbook (any own-setup friction)

Run the moment friction with this repo's own Claude Code setup surfaces. This can happen live, mid-task, or mined unattended at session edges. It orchestrates `flag-the-gap` → `where-it-lives` → `apply-inline` → `blind-proof`. It never restates any of their procedures. `flag-the-gap`'s own routing table is the map of how these and the other builder skills relate. Cite it, don't rebuild it here.

## GATE — what fires this loop

Fires on one of `flag-the-gap`'s six live fingerprints: **Correction · Surprise · Bloat · Noise callout · Noise mis-fix · Calcified quirk**. Also fires on the two fingerprints only `fix-on-discovery` can mine from history: **Repetition · Skipped-step**. For full fingerprint definitions, see `flag-the-gap`'s routing-table.md.

Does not fire on feature-code bugs, the user's own campaign content, canon facts, first-time occurrences with no observed recurrence, normal exploration (an empty grep), platform bugs, or documented transients you haven't verified are actually stale yet (`flag-the-gap` § "Is it really friction?").

## Observe → Diagnose → Fix → Prove

1. **Observe** via `flag-the-gap`. Name the friction in one line: `FG1: <fingerprint>. <friction>`. Ground it through a mined recurrence count, a verified condition change, or a reasoned trivial-skip: `FG2: grounded via <...>`.
2. **Diagnose** via `where-it-lives`. Pick the lowest-noise lever that holds (deterministic / on-demand / always-on), confirmed against its net-win gate: `WIL2: <lever>. <builder skill>`.
3. **Fix** via `apply-inline`. Apply at the root cause via the builder skill `where-it-lives` named. The full roster lives in `flag-the-gap`'s routing table. Classify each as Trivial, Validatable, or Cannot-Validate. Only Cannot-Validate issues wait on the user: `AI1`/`AI2`/`AI3: <classification>. <what happened>`.
4. **Prove** via `blind-proof`. A fresh, blind agent runs the real trigger scenario and scores PASS or FAIL against a quoted line. It uses single mode for one live fix, or batch mode for a queued or wider set: `BP4: PASS|FAIL. <quoted line>`. Any FAIL climbs `where-it-lives`'s escalation-ladder.md without being left standing or silently reverted.

## Unattended — fix-on-discovery

At SessionStart and on `/loop`, `fix-on-discovery` runs this same four-step loop automatically and batched on background subagents it orchestrates. It mines friction since the last watermark (`session-transcripts`'s sweep lens) that live-catching would miss (Repetition, Re-derivation, Skipped-step). It grounds each candidate, diagnoses and fixes every validatable one, proves the whole batch at once, then advances the watermark. Its own steps report `FOD1` through `FOD5`. Only a change that can't be validated or a FAIL that stays FAIL after ratcheting surfaces to the user. Everything else the loop closes on its own, unprompted and without derailing the user's task.

## Done

A completed pass ends every fingerprint it fired on one of two ways: a validated fix with a PASS proof (`AI1`/`AI2` + `BP4: PASS`), or a one-line ticket filed and surfaced for what can't be auto-validated (`AI3`). No FAIL left standing. An unattended pass also ends with `FOD5: watermark advanced to <session id>`.
