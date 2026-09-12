---
type: event
status: draft
publish: false
aliases: []
created: "{date}"
updated: "{date}"
tags: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
owner_skill: ".claude/skills/draft-content/references/event.md"   # OPTIONAL — the guide or skill that owns this page's quality
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
subtype: general        # general | battle | disaster | arrival | festival | negotiation | ritual | disappearance — set the real subtype; general is a placeholder
event_date: ""           # the in-fiction date this event happened or is scheduled for — e.g. "1495 DR", "Day -5", "Session 07" (campaign-timeline.md's date format)
location: ""             # OPTIONAL — wikilink to where this event happened or will happen
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
uid: 8b0acb80-3519-4fe7-b6b8-458a8f346608
---

# <Name>

*One-line description — what this event is, in one sentence.*

## What Happened

One paragraph — what happened, or what's planned, stated plainly: the
trigger, the turn, and the outcome (or the expected outcome, for a
pending event). States the fact once; canon state lives in `status:`
alone, never provenance narration in prose (`vault/CLAUDE.md` rule 2).

## Participants

Who was there or is expected to be there, one line each — `- [[wikilink]] — their role in it`.

## Consequences

What changed as a result — or, for a pending event, what's expected to
change once it happens. A hidden consequence the party hasn't discovered
yet is still plain prose, never background knowledge dressed as a
callout.
