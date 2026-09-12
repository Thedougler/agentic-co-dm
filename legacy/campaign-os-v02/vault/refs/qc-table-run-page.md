---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-12"
tags: [mystery]
summary: "QC profile for a vault/ page with type: encounter or type: puzzle, run live at the table."
uid: 76ab8ba5-afd9-4dda-9a57-46b7f9bf466a
---

# QC profile: table-run-page

For a `vault/` page the DM runs live at the table — `type: encounter`, `type: puzzle`. These pages are read aloud from and rolled against mid-session, so the wiki-page checks alone leave the two understandability failures uncaught: a read-aloud box the players can't act on, and a fight the DM can't run without stopping.

Template: `vault/_templates/_campaigns/_encounter.md` or `vault/_templates/_srd/_puzzle.md`. [[checklist|Checklist]]: `.claude/skills/encounter-prep/references/checklist.md` for encounter, `.claude/skills/draft-content/references/puzzle.md` for puzzle.

Base checks: all categories in `vault/refs/qc-wiki-page.md` (TEMPLATE, ONE-FACT-ONE-PAGE, WIKILINK, AGENT-COMMENT, STATUS, META, SLOP) apply unchanged — run them first.

Then run COLD-RUNNABILITY from [[qc-beat|`vault/refs/qc-beat.md`]] against this page's operative sections (read-aloud boxes, statblocks, DC tables, encounter narrative).

The page runs on its own — COLD-RUNNABILITY judges whether this page and its operatives (the wiki it transcludes via `![[...]]`) provide every number the DM needs mid-run, without opening a parent session file.
