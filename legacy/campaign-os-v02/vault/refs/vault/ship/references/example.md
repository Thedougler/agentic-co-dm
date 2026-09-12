---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "A worked ship page running interview through tier justification, DM review gate, and finished vessel stats, with the PC draw left as a placeholder slot."
created: "2026-08-03"
updated: "2026-08-10"
tags: [maritime, survival]
uid: c7e9efeb-68ad-4687-ab61-4a9e938b166a
---

# Worked example (fixture — placeholder name, not real campaign content)

User: "The party just took a smuggling sloop in a harbor raid — stat it up as one
PC's ship."

Standard queries: `grep -ril "smuggling sloop\|<PC name>.*ship" vault/ vault/campaigns/shattered-sea/pcs/` → no
hits. Clean to create.

Interview fills in: party-shared vessel, primary connection to `<PC name>`'s smuggling
contacts (fill the slot from the PC sheets, never from this page); Tier 1 (party's
current funds and the arc's scale both point here); Prize
(boarded during the harbor raid, then patched up at a friendly shipyard); crew —
that PC as Captain, a hireling Bosun, Navigator role currently open; pure vehicle
for now, no bastion facilities installed.

DM Review Gate (the DM Review Gate): tier + cost, crew composition, and the Prize acquisition
presented; DM approves. `status:` flips to `pending`.

false-flag-runner.md:

```markdown
---
type: ship
status: pending
publish: false
aliases: ["False Flag Runner"]
created: 2026-07-30
updated: 2026-07-30
tags: []
ship_class: sloop
tier: 1
home_port: ""
---

# False Flag Runner

> [!read-aloud] A low, lean sloop with a patched mainsail and a hull painted a
> nondescript grey-green. Fresh timber shows pale against the weathered planking
> along her port side, where the boarding action left its mark.

*Sloop · Tier 1 · unmoored*

| Field | Value |
|---|---|
| tier_justification | Tier 1 — matches the party's current funds and the smuggling arc's scale. |
| pc_connection | Gives <PC name>'s smuggling contacts a way to reach the outer islands. |
| acquisition_method | Prize — boarded during the harbor raid, patched up at a friendly shipyard afterward. |
| crew_composition | <PC name> as Captain; a hireling Bosun; Navigator role currently open. |
| current_status | Docked, party-controlled, Worn condition (post-raid patching). |
| bastion_facilities | None — pure vehicle for now. |

## Stats & Combat

| | |
|---|---|
| **Hull Points** | 40 |
| **Hull AC** | 12 |
| **Damage Threshold** | — (below Tier 2's threshold floor, per SRD calibration) |
| **Speed** | 70 mi/day (good wind), 35 (poor), 15 (calm, oars) |
| **Cargo** | 20 tons |
| **Crew (min/full)** | 2–4 / 8–12 |

## Crew

- Captain: <PC name>
- Bosun: hireling, unnamed
- Navigator: open

## Session Log
```
