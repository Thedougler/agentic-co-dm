---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-03"
tags: [craft]
summary: "QC profile for staged prose drafts — stories, fragments, handout text. The default when no other row matches."
uid: aecd56cd-83fe-45ae-9576-be4fa5aa9917
---

# QC profile: narrative-prose (default)

For any finished prose draft — lore passages, quest text, handouts, dialogue, staged drafts — when no more specific profile applies. This is the profile the checker uses when the caller names none.

Slop reference: `vault/refs/stories/ai-tells.md`.

| CATEGORY | Contract | How to check |
|---|---|---|
| GOAL | `goal:` is a story or world fact, fewest words. A listener who heard only the body can restate it. Texture is not the goal. | Cover the `goal:` and ask a stranger to restate it from the body. |
| CLARITY | The piece runs cold: no undefined terms of art, no names or references the reader must already know, no sentence that only parses with context from outside the document. | Read as a stranger; quote anything that needs external memory to parse. |
| SLOP | Per `vault/refs/stories/ai-tells.md`. | Check against that catalog, not memory. |
| REGISTER | Per [[register]] (`vault/refs/stories/register.md`). | Check against that file's actual contract, not memory. |
| CONTINUITY-ASIDE | A factual contradiction with canon is continuity-checker's territory, not this run's — if one is spotted in passing, it becomes exactly one aside line, never a finding and never the verdict. | Note it in one line after the findings; do not let it affect PASS/FAIL. |
| STRUCTURE | Grounding, per [[structure]]: nothing is leaned on before it's introduced — no character reacting before they're on stage, no place described by contrast to one not yet shown, no payoff whose setup comes later or never. | Walk the piece in order; quote any forward dependency. |
| META | Same contract as `vault/refs/qc-wiki-page.md`'s META row. | Same as that row. |
| MACRO | Section-ending shape variety, shape-plan conformance, exemplar drift. | evidence: paste the `prose-shape.mjs` JSON `flags` array (must be `[]`). |
