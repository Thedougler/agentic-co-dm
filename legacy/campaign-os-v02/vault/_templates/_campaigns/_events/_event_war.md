---
type: event
subtype: war             # fixed — this template IS the war fork; other subtypes use vault/_templates/_campaigns/_events/_event.md
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
uid: bf2824b3-1eb6-41b5-8e79-e7de480f540a
---

# <Name>

*One-line description — what this war was, in one sentence.*

## What Happened

One paragraph — what happened, or what's planned, stated plainly: the
trigger, the turn, and the outcome (or the expected outcome, for a
pending event). States the fact once; canon state lives in `status:`
alone, never provenance narration in prose (`vault/CLAUDE.md` rule 2).

## Sides & Commanders

The sides — each side's factions, notable commanders or leaders, and
relative strength, one line each per side: `- <Side> — [[wikilink]] commander, <force description>`.

## Campaigns & Phases

The war's shape across time and theatres, one line per campaign or
phase in chronological order: `- <Phase or campaign name> — <what
happened there, and how it shifted the war>`. A single named engagement
inside a phase gets its own `subtype: battle` page (`within:` this war)
rather than restated combat math here.

## Consequences

What changed as a result — or, for a pending war, what's expected to
change once it happens. A hidden consequence the party hasn't discovered
yet is still plain prose, never background knowledge dressed as a
callout.
