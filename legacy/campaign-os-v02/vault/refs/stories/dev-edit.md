---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "The /dev-edit command: developmental editing pass on a chapter, calibrated by the author's prose aesthetic, returning structured findings only."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: f440b513-5230-4437-9253-c770c3f5db1a
---

# Stories Playbook — /dev-edit ch-XX

Developmental editing pass on a chapter or story file. **Before starting, if currently on Sonnet, tells the author this task benefits from Opus and suggests switching with `/model opus`, then waits for their response.**

Locates the file (in Chapters/ by name match, or in the story root if no Chapters/ folder exists). Ambiguous cases list matches and ask for clarification. Then reads the story's rules file (world rules, character voice, developmental focus) and _Index.md (premise, themes, lore). It also reads the preceding chapter if it exists for continuity context, any Character files for characters in this chapter to check for voice drift, and the prose aesthetic guidance at `vault/refs/stories/prose-aesthetic.md` to calibrate every finding.

Performs a developmental editing pass. It does not rewrite or change anything; instead, it returns structured findings only, leaving the decision to the author. Report shape:

## Developmental Edit Report: {chapter reference}

- **Structure & Pacing**: scenes that stall without narrative purpose, or pivotal moments that feel rushed. Notes which paragraph or beat.
- **Showing vs Telling**: quotes instances where an emotional beat is told rather than shown. Briefly suggests the showing approach.
- **Dialogue**: flags on-the-nose dialogue and exposition dumps disguised as conversation. Also checks for voice drift from an established speech pattern (checked against the story's rules file).
- **POV Consistency**: flags head-hopping or POV slippage if the story uses a limited perspective.
- **Repetition**: lists repeated words, phrases, or ideas within the chapter, grouped word-level vs. idea-level.
- **Continuity**: flags anything conflicting with established facts from _Index.md or character files. Also checks against timeline inconsistencies.
- **Story-Specific Focus**: applies the developmental priorities listed in the story's rules file, noting findings under each listed priority.
- **Strengths**: notes what is working well. Developmental editing is not only corrective.

Does not apply changes. Presents findings only.

See also: [[writing-style-profile]], [[language-edit]], [[global-rules]].
