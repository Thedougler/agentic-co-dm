---
name: obsidian-automation
description: Automate ad-hoc Obsidian note workflows — daily/meeting notes, auto-linking,
  Dataview queries, graph orphan analysis — for a Campaign OS repo's non-canon working notes
  (inbox/ capture, personal PKM habits, research scratch space). Use when the user wants a
  daily note, a meeting note, a zettelkasten/book note, auto-linking rules, a Dataview query,
  or orphan/cluster graph analysis in the vault's ancillary space. Never for vault/campaigns/shattered-sea/pcs/sessions
  canon pages — those use their own prep skills and `_templates/`.
---

# Obsidian Automation

Automates Obsidian note-taking conveniences (templates, linking, Dataview, graph insights) for
a Campaign OS repo's non-canon working space — `inbox/` capture and personal scratch notes.
It never touches `vault/` canon pages (including `vault/campaigns/shattered-sea/pcs/` or
`vault/episodes/`): those are owned by their prep
skills (`.claude/skills/draft-content/references/npc.md`, `draft-moment`, etc.) and `vault/_templates/`, not this skill.

## Workflow

1. **Identify the note type** the user wants: daily note, meeting note, zettelkasten/book note,
   auto-linking rule, Dataview query, or graph-insight query (orphans, clusters, link
   suggestions). Confirm it targets `inbox/` or another non-canon location, not a canon page.
2. **Pull the matching spec** from `.claude/skills/obsidian-automation/references/templates.md` — filename pattern, folder,
   frontmatter, and body shape for note templates; query shape for Dataview; rule shape for
   auto-linking and graph insights.
3. **Apply it** — create the note or write the query/rule, filling `{{placeholders}}` with the
   user's actual title/date/attendees/topic.
4. **Best practices** while applying: one idea per note (atomic), consistent naming, link
   liberally, prefer templates over ad-hoc structure, use both tags and links.

## Reference

| Need | File |
|---|---|
| Note templates (daily, meeting, zettelkasten, book) | `.claude/skills/obsidian-automation/references/templates.md` § Note Creation |
| Auto-linking rules, alias support | `.claude/skills/obsidian-automation/references/templates.md` § Smart Linking |
| Dataview query examples | `.claude/skills/obsidian-automation/references/templates.md` § Dataview Queries |
| Web clipper / research workflow automations | `.claude/skills/obsidian-automation/references/templates.md` § Workflow Automations |
| Graph orphan/cluster/link-suggestion analysis | `.claude/skills/obsidian-automation/references/templates.md` § Graph Analysis |
