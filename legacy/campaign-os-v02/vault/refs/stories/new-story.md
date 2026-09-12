---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "The /new-story command: scaffolding a novel, novella, or short story from an idea or from scratch, plus timeline-format rules and chapter frontmatter."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: 7235e40c-87db-48bd-b58a-f6c1ca0f1c75
---

# Stories Playbook: /new-story

Checks whether a title was passed as an argument. If not, presents three options and waits: (1) From an idea (scaffold from _Ideas.md), (2) Empty novel/novella (full structure, blank files), or (3) Short story (lean structure, single prose file). A title argument skips the menu and goes directly to option 1.

**Option 1: scaffold from _Ideas.md**

- Reads _Ideas.md from the vault root. Ideas are separated by `---`. Each has a `##` heading as its title.
- With a title argument, the script finds the block whose heading matches (case-insensitive, partial match acceptable). If no match, it tells the author and lists available titles. Without an argument, it lists all titles and waits for a choice.
- Once identified: copies the full block (heading + body) into Quicknotes.md. Removes the idea block from _Ideas.md including its `---` separators, with no double `---` gap or dangling separator. Writes the cleaned file back.
- Reads the extracted content carefully. It may be in any language and is translated internally. The final story will be written in English. Extracts title, approximate form (asks if unclear), genre, core premise (1-3 sentences), known characters and locations, world rules and structural ideas, and open questions. Confirms title and form with the author before building anything.
- Novel/novella structure: _Index.md, Timeline.md (format per rules below), Quicknotes.md (verbatim), Chapters/ch-01.md (frontmatter only, no prose), _Characters/_Index.md, _Locations/_Index.md, _Research/, `_Assets/`.
- Short-story structure: `{Story Title}.md` (blank), _Index.md, Quicknotes.md (verbatim), _Characters/_Index.md (only if characters mentioned), `_Assets/`. No Chapters/, Timeline.md, or _Locations/ unless the notes suggest otherwise.

**Option 2: empty novel/novella** asks for the title if not given. Builds option 1's novel layout with every file minimal (frontmatter and section headers only, nothing invented). _Index.md: title/status only, placeholder sections blank. Timeline.md: a note that format should be decided once the structure is clearer, plus a placeholder first strand. Character/Location _Index.md files: setup instructions only.

**Option 3: empty short story** asks for the title if not given. Builds a lean structure with no Chapters/, Timeline.md, or _Locations/. Creates `{Story Title}.md` (title heading only), _Index.md (placeholders, nothing filled), Quicknotes.md (empty heading), and `_Assets/`. Adds _Characters/ only if the author mentions key characters. Ask if unsure.

**Timeline format** (option 1 novels only), chosen by narrative structure:

- Linear: table with columns `Story Date | Chapter | Event | Characters | Location | Notes`.
- Non-linear/parallel/flashback-heavy: grouped list by strand or character, noting temporal position and how strands connect.
- Circular/paradoxical: minimal reference list, with an explicit note that timeline order is the story's central conceit.

**Chapter frontmatter (ch-01.md):**

```yaml
chapter: 1
title: ""
status: draft
edit_pass: 0
wordcount:
pov:
timeline_events: []
locations: []
characters: []
tags: [chapter]
cssclasses: [chapter]
```

Title stays empty until the author has one. Reports at the end show what was built, which sections are empty and need completion, plus any open questions to resolve before writing begins.

See also: [[vault-architecture]], [[update-chapter]].
