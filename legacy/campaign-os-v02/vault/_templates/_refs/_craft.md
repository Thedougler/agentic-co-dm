---
type: craft
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
owner_skill: "~/.claude/skills/writing-for-agents/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality; user-level skill, outside this repo, per this template's own consolidation directive
uid: 304560a6-4260-4a94-822c-110fe648736f
---

# <Title>

Instantiated directly by whichever skill or CLAUDE.md routing entry needs
it — no single owning skill. Body is freeform prose that directs Claude, same
layout discipline as a `.claude/skills/*/SKILL.md` body: no fixed
headings, no agent-instruction HTML comments (`CampaignOS.TemplateAgentComments`,
error), state facts or steps directly rather than restating what another
file already owns (`.claude/rules/docs.md` § DRY).

A house-canon GM-craft standard or method, filed at whichever `vault/refs/`
location matches its subject (`stories/`, `ideas/`, or flat at the top level
for cross-cutting doctrine — `vault/refs/README.md` indexes the split) that
prep and writing skills cite and never restate. States the method directly.

Structures freely with whatever H2/H3 breakdown the content actually
needs — no fixed sub-headings required.
