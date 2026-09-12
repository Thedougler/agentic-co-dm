---
type: event
subtype: disaster        # fixed — this template IS the disaster fork; other subtypes use vault/_templates/_campaigns/_events/_event.md
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
uid: b92074da-1a8d-4180-9641-52063322eede
---

# <Name>

*One-line description — what this disaster was, in one sentence.*

## What Happened

One paragraph — what happened, or what's planned, stated plainly: the
trigger, the turn, and the outcome (or the expected outcome, for a
pending event). States the fact once; canon state lives in `status:`
alone, never provenance narration in prose (`vault/CLAUDE.md` rule 2).

## Cause

What actually triggered it — natural, magical, sabotage, neglect — stated
plainly. A hidden true cause behind a public explanation is still stated
here in plain prose.

## Damage & Casualties

What or who was lost — named losses get a wikilink; unnamed losses get a
stated count or scale (a district, a fleet, a season's harvest). Never a
vague "many died" with no stated scale.

## Consequences

What changed as a result — or, for a pending disaster, what's expected to
change once it happens. A hidden consequence the party hasn't discovered
yet is still plain prose, never background knowledge dressed as a
callout.
