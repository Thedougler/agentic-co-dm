---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-03"
tags: [craft]
summary: "QC profile for an episode recap.md."
uid: 8509be38-d228-4555-b39d-346c0be53435
---

# QC profile: recap

For a draft `vault/episodes/NNN/sNN-recap.md` — player-facing prose the table will read, built ONLY from this session's just-ingested `status: canon` pages. Contract source: `vault/refs/runbook-recap.md`.

Template: `vault/_templates/_episodes/_session_recap.md`. Slop reference: `vault/refs/stories/ai-tells.md`.

| CATEGORY | Contract | How to check |
|---|---|---|
| LEDGER | Every claim in the recap traces to this session's own entry on a `vault/`/`vault/campaigns/shattered-sea/pcs/` page the `ingest(sNN)` commit touched (or `vault/episodes/006/ingest-review.md`'s `Pages touched` worklist) — nothing invented, nothing "remembered" from outside those pages; transcript may supply color only, never new facts. | For each recap sentence, name the touched page it derives from. A sentence with no page fails. |
| BREVITY | 900–1350 words. Under 900 is thin. A sentence with no image and no turn fails — replace it, do not only delete down. | Count words in `## Recap`. Ask what the table loses if each sentence goes. |
| SPEAKING-TIME | Same band as BREVITY. Overrun: cut padding, keep the draw and the toys. | W145 on this file. |
| ATTENTION | Draw by sentence two on the session's sharpest image or turn. Not a date-line. Not "Last time the party…" | Read the first two sentences cold. |
| ELICIT | The closing line hands tonight a live question. Scene beats make the table remember what they can still touch. | Confirm the closer is tonight's draw (RECAP-OPENER). |
| RECAP-OPENER | The closing line hands off to the next session's run-guide Recap box and its opening moment (ADR 0026 decision e) — a self-contained ending with no forward draw fails. | Read the closing sentence; confirm it states an open question, threat, or draw the next session can quote almost verbatim. |
| PENDING-LEAK | No `status: pending` vault/campaigns/shattered-sea/pcs content is revealed — pending content never appears in recaps. | Grep the entities the recap names; any whose page is `status: pending` (or whose cited fact is pending) fails. |
| SPOILER | Nothing the table hasn't seen: no DM secrets, unrevealed motives, off-screen events, or facts the transcript can't show the players learned. | Unsure whether something was revealed at the table? It wasn't — grep the transcript, quote the line, then decide. |
| VOICE | Per [[register]] — player-facing only, throughout: no DM mechanics (DCs, HP, roll numbers, encounter design language), no terse DM-note register. | Read as a player; quote any mechanics leak or register drop. |
| SLOP | Per `vault/refs/stories/ai-tells.md`. | Check against that catalog, not memory. |
| META | The recap speaks to players about the session, never about how it was written. | Check against that section's actual contract, not memory. |
| FRONTMATTER | Every non-`# OPTIONAL` key from `vault/_templates/_episodes/_session_recap.md` present; `status: pending`; `publish: false` (publish is proposed later, never set here). | Diff frontmatter against the template. |
