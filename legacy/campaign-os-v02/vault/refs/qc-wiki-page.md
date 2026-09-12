---
type: agent-guidance
status: pending
publish: false
aliases: []
created: "2026-08-03"
updated: "2026-08-15"
tags: [survival]
summary: "QC profile for any other typed vault/ page, including vault/campaigns/shattered-sea/pcs/."
uid: b5ab685d-a3c3-4b95-ac34-424c15312031
---

# QC profile: wiki-page

For any page under `vault/` (including `vault/campaigns/shattered-sea/pcs/`) — structural and hygiene checks before the page is trusted as part of the wiki.

Template: the page's typed template under `vault/_templates/` (matched by frontmatter `type:`; resolution rules in `vault/_templates/CLAUDE.md`). Slop reference: `vault/refs/stories/ai-tells.md`.

| CATEGORY | Contract | How to check |
|---|---|---|
| TEMPLATE | Headings and frontmatter match the page's typed template from `vault/_templates/` — required sections present, in the template's order, no freeform structure; every non-`# OPTIONAL` frontmatter key present. | Read the matching template; diff structure and keys against it. |
| ONE-FACT-ONE-PAGE | Each fact lives on exactly one page; elsewhere it is a wikilink. A fact restated on this page that already lives on another page fails — quote both. | Grep distinctive phrases/claims from the page across `vault/`; a duplicate hit fails. |
| WIKILINK | Every `[[wikilink]]` on the page resolves to a real page. | Grep/Glob each link target; a dangling link fails. |
| AGENT-COMMENT | No leftover `<!-- AGENT: ... -->` scaffolding comments — every one is removed before the page is finished, no exceptions. | Grep the file for `<!-- AGENT`. |
| STATUS | Frontmatter `status:` and `publish:` carry correct, unescalated values: status within the enum (`draft | pending | canon | retired`), never promoted past what the workflow allows, and`publish:` never flipped to `true` without user approval. | Read the values; check `git diff`/`git show` for a flip the edit wasn't entitled to make. |
| WANTS | Every named actor page (`npc`, `creature`) carries the scannable bold `**Wants:**` line from its template's opening block (`creature` also carries `**Morale:**`) — a capability-only page, stats with no findable want, fails. | Read the page's opening block against its typed template under `vault/_templates/`; grep `^\*\*Wants:\*\*` (and `^\*\*Morale:\*\*` for `creature`) — missing, empty, or buried past the opener fails. |
| LAYOUT | Load-bearing facts sit bold-led in bullets or under naming headers, never buried mid-paragraph; conditional detail is indented one level under its trigger bullet, never inline if/then prose; 3+ parallel cases sharing the same fields sit in a table; reference material a beat needs in the moment sits adjacent to that beat, not off in a distant section (rubric R27–R31, R33). | Read the page against `vault/refs/exemplar-quality-rubric-layout.md`; flag any load-bearing fact (DC, name, number) buried in a paragraph, any conditional written as prose rather than an indent, and any 3+-case parallel set left as prose instead of a table. |
| SPEAKABLE | Player-facing text — `> [!read-aloud]` boxes, quoted NPC lines — is delivery-ready: grammatical, self-contained, ends on an actionable draw; no stage directions or bracketed narrator notes sit inside the speakable text itself (rubric R13). | Read every `> [!read-aloud]` box and quoted NPC line; flag any that would need editing before it could be read aloud as written, or that embeds a stage direction inside the quoted/boxed text. |
| META | The page speaks to its reader about its subject only — never about itself, its own drafting, or its authorship — stateless wiki content only. | Check against that section's actual contract, not memory. |
| SLOP | Per `vault/refs/stories/ai-tells.md`. | Check against that catalog, not memory. |
