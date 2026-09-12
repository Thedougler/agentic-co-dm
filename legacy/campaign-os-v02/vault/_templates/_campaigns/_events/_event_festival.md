---
type: event
subtype: festival        # fixed — this template IS the festival fork; other subtypes use vault/_templates/_campaigns/_events/_event.md
status: draft
publish: false
aliases: []
created: "{date}"
updated: "{date}"
tags: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
owner_skill: ".claude/skills/draft-content/references/event.md"   # OPTIONAL — the guide or skill that owns this page's quality
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
event_date: ""           # the in-fiction date this event happened or is scheduled for — e.g. "1495 DR", "Day -5", "Session 07" (campaign-timeline.md's date format)
location: ""             # OPTIONAL — wikilink to where this event happened or will happen
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 7e9b932e-c28d-4805-b309-73b8a4eb83fc
---

# <Name>

*One-line description — what this festival is, in one sentence.*

## What Happened

One paragraph — what happens, or is planned, stated plainly: the
occasion, the shape of the day, and the expected outcome. States the fact
once; canon state lives in `status:` alone, never provenance narration in
prose (`vault/CLAUDE.md` rule 2).

## Customs & Traditions

What actually happens during it — the rites, games, food, performances,
or traditions specific to this observance, stated concretely enough to
run at the table.

## Notable Attendees

Who shows up that the party might interact with, one line each — `- [[wikilink]] — their role in it`.

## Consequences

What changed as a result — or, for a pending festival, what's expected to
change once it happens (an opportunity a PC could use, a rivalry that
surfaces). A hidden consequence the party hasn't discovered yet is still
plain prose, never background knowledge dressed as a callout.
