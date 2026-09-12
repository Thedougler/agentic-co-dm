---
type: event
subtype: negotiation     # fixed — this template IS the negotiation fork; other subtypes use vault/_templates/_campaigns/_events/_event.md
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
uid: b2e3b90a-4336-41b3-853e-eb3720c701fd
---

# <Name>

*One-line description — who's negotiating and over what, in one sentence.*

## What Happened

One paragraph — what happened, or what's planned, stated plainly: the
trigger, the turn, and the outcome (or the expected outcome, for a
pending event). States the fact once; canon state lives in `status:`
alone, never provenance narration in prose (`vault/CLAUDE.md` rule 2).

## Parties & Stakes

Each side at the table — wikilink who represents them, what they're
actually after (stated even when it differs from their opening position),
and what they stand to lose if it fails, one line each per side: `- <Side>
— [[<wikilink>]] representing, wants <X>, risks <Y>`.

## Terms & Outcome

What was actually agreed, or the specific point it broke down on — never
"negotiations succeeded" with no stated terms. For a pending negotiation,
the terms each side would accept going in.

## Consequences

What changed as a result — or, for a pending negotiation, what's expected
to change once it happens. A hidden consequence the party hasn't
discovered yet is still plain prose, never background knowledge dressed
as a callout.
