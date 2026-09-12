---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "The stub check every draft guide runs before creating a page — the grep pair, why it is two commands, and how to escalate on empty output."
created: "2026-08-03"
updated: "2026-08-15"
tags: [craft]
uid: 218b6a41-7685-4469-adc8-20b7a1a0a4db
---

# Draft — Standard Queries

Run before creating anything, and again before writing any prose that names
another established entity — the same check for a draft guide under
`vault/refs/vault/<type>/` and for a prep skill writing a typed page
(`composing-beats` and its `writing-*-beats` skills, `encounter-prep`,
`rule-prep`).

```bash
grep -ril "<entity name>" vault/ vault/campaigns/shattered-sea/pcs/ 2>/dev/null
grep -rl --include=transcript.md -i "<entity name>" vault/episodes/ 2>/dev/null
```

Two separate commands, never one glued together -> in zsh a
`vault/episodes/*/transcript.md` glob aborts the
whole line with "no matches found" whenever that directory has no subdirs
yet, which is every early campaign. The `--include` form degrades to a clean
no-hits instead.

## Reading the result

- **A hit on the first query** -> the Stub Check fires
  (`vault/refs/vault/_common/hard-rules.md`); expand that page, never
  create a duplicate.
- **Two hits that might be the same entity** -> the Ambiguous stub-check
  hits case (`vault/refs/vault/_common/degrade.md`); stop and ask the DM.
- **Empty output on both** -> nothing established yet: name and invent
  freely.

## Before asserting absence

Empty output licenses creating a new page — it does not license claiming
"X doesn't exist" to the DM or in prose. That claim escalates first:
`npm run search:content -- search "<terms>"` for keyword, then
`-- query "<terms>"` for semantic. The entity may live under an alias or
different wording.
