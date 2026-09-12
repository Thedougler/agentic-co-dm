---
type: event
subtype: arrival         # fixed — this template IS the arrival fork; other subtypes use vault/_templates/_campaigns/_events/_event.md
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
uid: 91d63a82-4fde-40e0-acc4-57701b271dda
---

# <Name>

*One-line description — who or what arrived (or departed), in one sentence.*

## What Happened

One paragraph — what happened, or what's planned, stated plainly: the
trigger, the turn, and the outcome (or the expected outcome, for a
pending event). States the fact once; canon state lives in `status:`
alone, never provenance narration in prose (`vault/CLAUDE.md` rule 2).

## Who/What Arrived

The arriving (or departing) party — wikilink named individuals, factions,
or vessels, their stated purpose, and their real purpose if it differs,
the gap stated plainly.

## Reception

How locals, factions, or the party reacted immediately — welcomed,
feared, ignored, contested — and by whom specifically, not "the town."

## Consequences

What changed as a result — or, for a pending arrival, what's expected to
change once it happens. A hidden consequence the party hasn't discovered
yet is still plain prose, never background knowledge dressed as a
callout.
