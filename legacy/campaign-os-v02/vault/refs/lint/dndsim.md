---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-15"
updated: "2026-08-15"
tags: [craft]
summary: "dndsim: reading the rule name in the message, where each rule's requirement is defined, and the opt-in flag these findings run behind."
uid: eec84ac8-fde5-443e-aba3-6629740ad937
---

# dndsim — statblock and combatant-block defects

The `dndsim` producer parses each page's own ```statblock fence with the
combat engine and reports what the engine cannot run. The rule name at the
head of the message says which contract failed —
`W-statblock-simulatable`, `W-combatant-block`.

## Fix

Fix the defect inside the page's own ```statblock fence.
`utils/dndsim/src/dndsim/lint/rules.py` holds what each rule requires.

These findings are opt-in, behind `WIKI_CLI_DNDSIM=1`. Clearing that variable
hides the finding and leaves the statblock unrunnable.
