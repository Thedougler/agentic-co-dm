---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "A worked fixture running stub check through a completed Front with a clock, showing every checklist item satisfied and PC draws left as placeholder slots."
created: "2026-08-03"
updated: "2026-08-10"
tags: [survival]
uid: f56364a1-df75-41ef-ba54-9962f9e27205
---

# Worked example (fixture — placeholder names, not real campaign content)

User: "I need a faction running the salt-tithe fraud, and it should have a
clock."

Stub check: `grep -ril "salt.tithe" vault/` → no hits. New faction.

Interview answers (given together): concept — a shipping guild skimming
tithe weight; PC connection — pressures `<PC name>`'s kin, who pay that
tithe (name the real PC and the real mechanism when you run this — pull
both from `vault/campaigns/shattered-sea/pcs/`, never from this page);
front needed — yes, they're actively covering the skim before an audit.

Standard queries: `grep -rl "status: canon" vault/campaigns/shattered-sea/factions/` → empty
(nothing canon yet, invent freely within the rails).

Page instantiated at vault/campaigns/shattered-sea/factions/tideglass-concordat.md (fixture
path, not a real page) from the faction template. Front written into
`## Goals & Fronts`:

```markdown
### Front: The Skim Before the Audit
**Lifecycle:** active
**Primary goal:** Close the gap in the tithe ledgers before the Crown
auditor arrives.
**Consistent method:** Pays small debts early and loudly; never negotiates
the tithe rate in public, only in back rooms.
**Off-screen move if unopposed:** Reassigns two clerks to falsify the last
quarter's weigh-slips.
**Trigger conditions:**
- Clock advances one segment per week the falsified slips go unchallenged.
**Clock:** 4 segments — filled: 1
**Consequence at fill:** The Crown auditor signs off clean; the skim
becomes permanent policy, and <PC name>'s kin absorb the shortfall
indefinitely.
**Possible outcomes (2-3):** (a) party exposes the fraud before the audit —
Concordat's leadership purged, tithe rate publicly renegotiated; (b) party
ignores it — consequence at fill triggers as written; (c) party quietly
profits from the skim themselves — Concordat treats them as new partners,
opening a different front.
**PC connection:** Pressures <PC name>'s kin directly — they're the
ones absorbing the falsified shortfall.
**Per-PC awareness:** <PC name>'s kin know the tithe felt short this quarter;
they don't yet know the Concordat itself falsified the slips — that fact
stays inline here, unrevealed, rather than in a separate section.
**Quest link:** none yet — flag for the DM: this could spawn a quest once
the party has a reason to investigate the ledgers.
```

This satisfies the checklist: vector goal, behavioral method, observable
off-screen move, named trigger and lifecycle, specific irreversible
consequence, non-railroading outcomes, a named PC mechanism, and a hidden
fact (the falsification itself) written inline via `Per-PC awareness`
rather than split into its own section. No hidden *conclusion* here (the
fraud is discoverable, not concealed from the reader of the page), so no
Three-Clue Audit was required — flagged explicitly in this example so the
omission reads as a decision, not an oversight.
