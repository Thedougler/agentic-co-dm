---
type: event
subtype: ritual           # fixed — this template IS the ritual fork; other subtypes use vault/_templates/_campaigns/_events/_event.md
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
uid: 0a2632fe-3d23-4228-b3bc-418eae759f8e
---

# <Name>

*One-line description — what rite was performed and why, in one sentence.*

## What Happened

One paragraph — what happened, or what's planned, stated plainly: the
trigger, the turn, and the outcome (or the expected outcome, for a
pending event). States the fact once; canon state lives in `status:`
alone, never provenance narration in prose (`vault/CLAUDE.md` rule 2).

## The Rite

What was actually performed — the steps, words, or components that
mattered, and who filled which role (officiant, subject, witness),
concretely enough to run or reference at the table.

## Effect

What the rite actually did or was meant to do — a binding sealed, a title
conferred, a working completed or interrupted — stated as a fact, not an
aspiration. A rite that failed or was interrupted states that plainly,
including how far it got.

## Consequences

What changed as a result — or, for a pending rite, what's expected to
change once it happens. A hidden consequence the party hasn't discovered
yet is still plain prose, never background knowledge dressed as a
callout.
