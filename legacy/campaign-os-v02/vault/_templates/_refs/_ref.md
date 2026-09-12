---
type: agent-guidance | reference | runbook | guide | craft   # pick one — see "Which type" below
status: draft
publish: false
title: ""                      # OPTIONAL — display title if it differs from the H1 heading; absent ⇒ the H1 is the title (llm-wiki skill)
aliases: []
summary: ""                    # one sentence, ≤200 chars — cheap page preview, never empty
created: "{date}"
updated: "{date}"
tags: []
tier: supporting               # OPTIONAL — core | supporting | peripheral; absent ⇒ supporting (llm-wiki skill). type: agent-guidance and guide only — delete this key for reference/runbook/craft.
phase: any                     # type: runbook only — 1 | 3 | 4 | 5 | 6 | any, the session-pipeline phase this runbook drives ("any" for standing procedures). Delete this key for every other type.
source: ""                     # type: guide only, REQUIRED — the raw/ path this guide was built from, e.g. raw/2026-07/city-creation-guide.md. Delete this key for every other type.
source_url: ""                 # type: guide only, OPTIONAL — the external URL this guide was originally sourced from. Delete this key for every other type.
campaigns: []                  # type: guide only, OPTIONAL — this page's campaign(s), if this repo runs more than one. Delete this key for every other type.
owner_skill: "~/.claude/skills/writing-for-agents/SKILL.md"   # OPTIONAL — the guide or skill that owns this page's quality; user-level skill, outside this repo, per this template's own consolidation directive
uid: 6d26bb42-c1d8-4a8c-a0e0-8b22585c6907
---

# <Title>

Instantiated directly by whichever skill or CLAUDE.md routing entry needs
it — no single owning skill. Body is freeform prose that directs Claude, same
layout discipline as a `.claude/skills/*/SKILL.md` body: no fixed
headings, no agent-instruction HTML comments (`CampaignOS.TemplateAgentComments`,
error), state facts or steps directly rather than restating what another
file already owns (`.claude/rules/docs.md` § DRY).

## Which type

Every page under `vault/refs/**` is one document family — agent-facing
prose written under `writing-for-agents`'s step/reference split
(`~/.claude/skills/writing-for-agents/SKILL.md`). Pick `type:` by which
side of that split the page is on, and if reference, what it's reference
*of*:

- **runbook** — the one type here with real **steps**: a numbered
  multi-step operation orchestrating templates/skills/linters. Follows
  `vault/refs/README.md`'s shared format — GATE + numbered steps
  + Done (see "runbook shape" below). Every other type is flat
  **reference**, differing only in subject:
- **agent-guidance** — standing operational/architectural knowledge about
  this system itself, addressed to the agent (e.g. `vault/refs/w<N>-*.md`,
  docs/adr/0029). Never a numbered procedure (that's `runbook`) and never
  a lookup catalog of campaign/rules facts (that's `reference`).
- **reference** — a lookup catalog of campaign or rules facts for an
  operator running the campaign: a safety-boundary table, a feature/
  system catalog. States the facts directly.
- **craft** — a house-canon GM-craft standard or method, filed at whichever
  `vault/refs/` location matches its subject (`stories/`, `ideas/`, or flat
  at the top level for cross-cutting doctrine — `vault/refs/README.md`
  indexes the split) that prep and writing skills cite and never restate.
  States the method directly.
- **guide** — reference distilled from a named external source, filed at
  the source's topically-appropriate `vault/refs/` location; `source:` is
  required and names the `raw/` path it was built from. Owned by the
  `find-guidelines` skill.

Every type structures freely with whatever H2/H3 breakdown the content
actually needs — none of the five require fixed sub-headings.

## runbook shape (type: runbook only)

GATE: <shell command proving the prior phase / precondition — paste its
output>. No/failed → STOP; <the remedy>.

1. <Imperative step. Name the skill that does the work (`<skill>` skill)
   and the exact path it writes. Paste a `<MARKER>:` line from real tool
   output.>
2. <…>

Done = <MARKER>: <what to paste>, <checks green>, commit `<verb>(sNN): ...`
