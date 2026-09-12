---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-15"
tags: [craft]
summary: "QC profile for a stretch run-guide page and the episode overview page."
uid: d860c3d3-d9ae-4077-8796-99a8e776abdf
---

# QC profile: run-guide

For a `subtype: run-guide` page. Check against Narrative Islands and
ADR-0059: unused prep has no authority; numbered H2s transclude owners;
Exit is the only heading that opens another file.

Template: `vault/_templates/_episodes/_session_run_guide.md`. Checklist: `.claude/skills/draft-content/references/run-guide.md` § Checklist.

| CATEGORY | Contract | How to check |
|---|---|---|
| LAST-TIME | Opening episode stretch only. Closes on the prior `vault/episodes/NNN/sNN-recap.md` closer. Later stretches omit the heading. | Read the closer against the prior recap. Confirm later stretches have no Last Time. |
| PREP | This stretch only: where, who, live secrets, 1–3 DM reminders. | A check table under Prep fails. A fact that belongs on a later stretch fails. |
| WALK | Numbered H2s are play order. Spoken picture, then a check table, then the owner heading. A picture with no table fails. | Walk H2s against RG6 and `.claude/skills/composing-beats/references/runtime-surface.md`. |
| SIDE-TRACKS | Other walks this stretch can open are wikilinks. A `![[` there fails. | Grep `![[` under that heading. |
| EXIT | Each mutually exclusive remainder is a run-guide wikilink. A beat's branch conditions stay on its situation's Live Branches rows. | Resolve every Exit target as a run-guide. |
| HOP | Mid-play set is this run-guide until Exit. | Cold-run the first H2, one middle H2, one Exit target. |
| BLOAT | A fact restated here instead of transcluded or wikilinked fails. | Grep suspected restated facts against source pages. |
| BREVITY | Per ADR 0028 — judged, not counted. | "What does the table lose if this sentence goes?" |
| VOICE | Per [[register]], both directions. | Voice check, never a taste edit. |
| META | The file speaks only to the DM running this stretch. | Flag self-referential passage. |
| STATE | Reads cold at the table. | A stranger with this file and the wiki can run the stretch. |
| FRONTMATTER | Every non-OPTIONAL key of the run-guide template; `status:` `draft`/`pending`; `publish: false`; episode basename matches `eNN-run-guide-<slug>`. | Diff frontmatter; check basename. |
| PRE-SHIP | Every run-guide item in `.claude/skills/draft-content/references/run-guide.md` § Checklist holds. | Read that list. |

## Overview pages

For a `subtype: overview` page. Read this page before a run-guide.

Template: `vault/_templates/_episodes/_session_overview.md`. Checklist: `.claude/skills/draft-content/references/run-guide.md` § Checklist.

| CATEGORY | Contract | How to check |
|---|---|---|
| TONIGHT | Shape, start, opening pressure, opening stretch wikilink. `session_shape:` is one of the nine shapes. | Walk Tonight against frontmatter and the first Run-guides line. |
| RUN-GUIDES | Every walk that can start tonight is a wikilink, start order, one line each. Far planned guides stay off this list. | Resolve every wikilink; confirm nearby + tonight-reachable only. |
| BLOAT | A fact restated here instead of wikilinked fails. | Grep suspected restated facts against source pages. |
| META | The file speaks to the agent and the DM briefing tonight. | Flag self-referential passage. |
| FRONTMATTER | Every non-OPTIONAL key of the overview template; `status:` `draft`/`pending`; `publish: false`; basename matches `e` plus two-digit session plus `-overview`. | Diff frontmatter; check basename. |
| PRE-SHIP | Every overview item in `.claude/skills/draft-content/references/run-guide.md` § Checklist holds. | Read that list. |

## Episode-level pass

One additional checker over the overview, every this-episode run-guide,
and every this-session frame.

| CATEGORY | Contract | How to check |
|---|---|---|
| NAV | Every required beat appears on at least one episode run-guide. Every Exit target exists. | Union the walks; resolve Exit. |
| AGREE | Overview Run guides and the episode run-guide files name the same tonight-reachable set. | Diff overview Run guides against `eNN-run-guide-*.md` plus listed situation guides. |
| HOP | Same as the per-document HOP row, over the whole set. | Three cold runs. |
