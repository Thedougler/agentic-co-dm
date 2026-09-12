---
type: event
subtype: disappearance    # fixed — this template IS the disappearance fork; other subtypes use vault/_templates/_campaigns/_events/_event.md
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
uid: 62bd2120-8565-45f5-b7b4-c1e8c43bc12b
---

# <Name>

*One-line description — who or what vanished, in one sentence.*

## What Happened

One paragraph — what happened, or what's planned, stated plainly: the
trigger, the turn, and the outcome (or the expected outcome, for a
pending event). States the fact once; canon state lives in `status:`
alone, never provenance narration in prose (`vault/CLAUDE.md` rule 2).

## Last Seen

The final confirmed sighting — who saw them, where, when, and doing what
— stated plainly. If nothing is confirmed yet, state that explicitly
rather than leaving the section silently empty.

## Known Leads

What's actually been found or ruled out so far, one line each — a
genuinely unknown cause is stated as unknown, never invented to fill the
section; a cause known to the DM but not yet the party is still plain
prose here, never background knowledge dressed as a callout.

## Consequences

What changed as a result — or, for a pending disappearance, what's
expected to change once it happens. A hidden consequence the party
hasn't discovered yet is still plain prose, never background knowledge
dressed as a callout.
