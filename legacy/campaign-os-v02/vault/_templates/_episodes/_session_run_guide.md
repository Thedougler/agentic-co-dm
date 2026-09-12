---
type: session
subtype: run-guide
status: draft
publish: false
aliases: []
created: "{date}"
updated: "{date}"
tags: []
summary: ""                   # one sentence, ≤200 chars — cheap page preview, never empty
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
edit_pass: 0            # OPTIONAL — last completed line pass (0–3); the draft-story skill is this key's sole writer
session_number:          # OPTIONAL — set on episode stretches
session_date:            # OPTIONAL — set on episode stretches
world_date:              # OPTIONAL — this session's in-fiction date, in the campaign calendar's own reckoning, e.g. "15 Eleint, 1495 DR"
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
owner_skill: ".claude/skills/draft-content/references/run-guide.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: ae8178d2-bae5-4004-8215-f2c80aaec1cd
---

# <Stretch name>

Episode stretch: `vault/episodes/<NNN>/e<NN>-run-guide-<slug>.md`.
Situation walk: `<situation-slug>-run-guide.md` beside the Situation page.

## Last Time

OPTIONAL — opening episode stretch only. Delete otherwise (W38).

![[e<NN>-narration-last-time]]

## Prep

This stretch only. Where, who, secrets already live, 1–3 DM reminders.

## 1 — <Beat>

Play order. Spoken picture, then the check table, then the owner heading the DM spends. The next numbered H2 is next inside this file.

![[<page>-narration-<role>]]

> [!check] <Beat>
>
> | Check | DC | Failure | Pass |
> |---|---|---|---|
> | Perception | 14 | the room is the room | [[<secret-or-object>]] |
> | Wisdom save | 13 | <what lands> | they shake it off |
> | Group Dexterity | bands | CF … F … | S … CS … |

![[<page>#What Happens]]

## Side-tracks

OPTIONAL — delete when this stretch has no side-track. Wikilinks to other run-guides or Situations this stretch can open. No embeds.

- [[<page>|<Name>]] — <when>

## Exit

When remaining play is mutually exclusive, each path is a run-guide. A beat's branch conditions stay on its situation's Live Branches rows; landings are the next H2 or a row here.

- <choice or condition> → [[<run-guide>|<Stretch>]]
