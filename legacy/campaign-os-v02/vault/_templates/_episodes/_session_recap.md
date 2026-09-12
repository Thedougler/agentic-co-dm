---
type: session
subtype: recap
status: pending
publish: false
aliases: []
created: "{date}"              # the real date this recap was written — RECAP always runs after the session happened
updated: "{date}"              # same value as created on first write
tags: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
tier: supporting        # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill)
edit_pass: 0            # OPTIONAL — last completed line pass (0–3); the draft-story skill is this key's sole writer
number:
date:
title:
campaigns: []            # OPTIONAL — this page's campaign(s), if this repo runs more than one
owner_skill: ".claude/skills/recap-writer/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality
uid: 14edde0d-83f5-4250-ba64-6392ada97c04
---

# Session <NN>: <Title>

Recap-opener coupling
(ADR-0026 decision e): this page is the draft source for session `NN+1`'s
`_templates/_episodes/_session_run_guide.md` `## Last Time` →
`![[e<NN>-run-guide-narration-last-time]]`, which in turn
hands straight off to moment 1's opener — write this page's closing line as the hook that file
should quote or restate almost verbatim, not as a self-contained ending.

## Recap

<Player-facing prose — what happened, as the players experienced it. Close on the open
question, threat, or hook the next session picks up — this closing line is what session
`NN+1`'s Last Time box reuses to cut straight into moment 1's opener, so write it as a
handoff, not a period on the story.>

## Highlights link

`<path-to-highlights>` — a plain path, never a `[[wikilink]]`: every
session's highlights file shares the same basename, so a bare wikilink
would be ambiguous the moment a second session exists.

## Ingest review link

`<path-to-ingest-review>` — a plain path, same reason as above. No
ingest-review.md has landed for this session, or it's already been
deleted post-review → state "Not applicable — no ingest-review.md has
landed for this session" instead; the heading stays either way.
