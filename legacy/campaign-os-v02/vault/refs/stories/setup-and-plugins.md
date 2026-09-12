---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "Setup steps and Obsidian community plugins for gsarig/ai-playbooks' stories fiction-writing vault."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: 73979773-e584-427b-8359-364a71bb2a9f
---

# Stories Playbook: Setup and Plugins

Requires Obsidian and Claude Code.

1. Open the stories/ folder (inside playbooks/) as an Obsidian vault.
2. Install community plugins via **Settings → Community plugins → Browse**:

| Plugin | What it enables | Required |
|--------|----------------|----------|
| Templater | Auto-applies the chapter template (auto-numbered filename) when a new file is created in Chapters/ | Required |
| LanguageTool Integration | Live grammar/style checking; set native language for second-language support | Recommended |
| Editing Toolbar | Floating formatting toolbar; text, list, alignment, insert commands | Recommended |
| Smart Typography | Straight quotes → curly, `--` → em dash, `...` → ellipsis as you type | Recommended |
| Typing Transformer | `***` → scene-break divider (`✽✽✽`) and other keystroke shortcuts | Recommended |
| Better Word Count | Status-bar word/page count (300 words/page) | Recommended |
| Iconize | Sidebar icons pre-configured for `_Archive`, `_Templates`, `_Ideas`, `_Commands`, `_Dashboard` | Recommended |
| Outliner | Better Tab/Enter list handling, drag-drop reorder, cursor stays on bullet | Recommended |
| Advanced Cursors | Cmd/Ctrl+D selects next matching word for renaming within a chapter | Recommended |
| Pandoc Plugin | Export to DOCX/PDF/EPUB from Obsidian | Recommended |

All plugin settings are pre-configured in the vault. If writing English as a second language, set native language in LanguageTool's **Mother tongue** field so it distinguishes errors from stylistic choices. Pandoc plugin requires Pandoc installed on the system separately, before the Obsidian plugin; use it to export finished chapters/manuscripts to DOCX (editors), EPUB (ebook distribution), or PDF.

1. Open a terminal in stories/ and run `claude`. Claude Code reads the vault's `CLAUDE.md` and is ready to use the slash commands.
2. Personalize before writing:
   - **`CLAUDE.md`**: edit the Author section to describe language background (if writing in a second language). This calibrates the language editing passes.
   - **`vault/refs/stories/prose-aesthetic.md`**: personal aesthetic profile. Leave blank initially, fill in after the first story, or ask Claude to build it from writing samples.

First step once set up: run `/new-story`. Claude asks whether to scaffold from an idea in _Ideas.md, start an empty novel structure, or start a short story.

See also: [[vault-architecture]], [[global-rules]], [[stories-playbook-overview|Stories Playbook: fiction writing workflow]].
