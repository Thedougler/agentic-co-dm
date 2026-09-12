---
type: event
subtype: battle          # fixed — this template IS the battle fork; other subtypes use vault/_templates/_campaigns/_events/_event.md
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
uid: f8444859-a0b6-4e08-ad44-632bfe2bafbd
---

# <Name>

*One-line description — what this battle was, in one sentence.*

## What Happened

One paragraph — what happened, or what's planned, stated plainly: the
trigger, the turn, and the outcome (or the expected outcome, for a
pending event). States the fact once; canon state lives in `status:`
alone, never provenance narration in prose (`vault/CLAUDE.md` rule 2).

## Combatants

The sides — each side's forces, notable commanders or named
participants, and relative strength, one line each per side: `- <Side> — [[wikilink]] commander, <force description>`.

## Casualties & Outcome

Losses on each side (named deaths get a wikilink; unnamed losses get a
stated count or scale), who came out ahead, and the concrete territorial
or political shift that resulted — never "the battle was decisive" with
no stated shift.

## Consequences

What changed as a result — or, for a pending battle, what's expected to
change once it happens. A hidden consequence the party hasn't discovered
yet is still plain prose, never background knowledge dressed as a
callout.
