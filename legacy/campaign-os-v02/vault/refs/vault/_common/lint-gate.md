---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The lint-to-zero gate every prep skill clears before opening a QC round, and why a review opened before it is a round thrown away."
created: "2026-08-10"
updated: "2026-08-15"
tags: [craft]
uid: aebf2b65-635e-40bb-82bf-45c21f64bc58
---

# Draft — Lint Gate

Run before any QC dispatch, by every prep skill that writes a typed page
(`composing-beats` and its `writing-*-beats` skills, `draft-run-guide`,
`encounter-prep`, `rule-prep`):

```bash
npm run lint -- <file>
```

Fix until it reports zero findings, then dispatch the checker.

## Why the order is fixed

The rewrites lint forces land on the same sentences a quality checker
scores. A QC round opened while findings are still open is a round thrown
away: the checker reads prose that is about to change, and its verdict
expires before it is acted on.

## Scope the claim

`clean` or `0 findings` is only ever written beside the exact command that
produced it and the paths it covered. A claim whose scope is narrower than
the work gets read as a full pass and trusted as one.

A run that reports `0 files` linted nothing — a mistyped path, or a shell
that did not split a variable holding several paths. That is not a pass;
re-run with the paths spelled out.
