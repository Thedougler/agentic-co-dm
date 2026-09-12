---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "Folder architecture of a stories-playbook vault: shared vault files, and the novel/novella vs. short-story folder layouts."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: f231bcd9-2223-41dd-928a-cb0d7ab6675e
---

# Stories Playbook: Vault Architecture

```text
stories/
├── CLAUDE.md               Global writing rules for Claude
├── _Commands.md            Quick reference for all slash commands
├── _Dashboard.base         Story tracker — Active, In Revision, Completed, Abandoned
├── _Ideas.md               Idea scratchpad — source for /new-story
├── _Templates/             Obsidian templates (auto-applied by Templater)
├── _Archive/               Completed and abandoned stories
│   ├── Completed/
│   └── Abandoned/
│
├── My Novel/               Novel or novella — created by /new-story
│   ├── _Index.md           Story premise, themes, open questions
│   ├── _Lore.md            Detailed worldbuilding — rules, cosmology, factions
│   ├── _Lines.md           Reserved lines to place later in the draft
│   ├── CLAUDE.md           Story-specific rules (overrides vault CLAUDE.md)
│   ├── Timeline.md         Event tracking
│   ├── Quicknotes.md       Working notes and fragments
│   ├── Chapters/           One file per chapter (ch-01.md, ch-02.md, …)
│   ├── _Characters/        One file per character
│   │   └── _Index.md       Character roster and Bases view guidance
│   ├── _Locations/         One file per location
│   │   └── _Index.md       Location roster and Bases view guidance
│   ├── _Research/          Reference material
│   └── _Assets/            Cover images and design files
│
└── My Short Story/         Short story — leaner structure
    ├── _Index.md           Story premise and open questions
    ├── CLAUDE.md           Story-specific rules
    ├── Quicknotes.md       Working notes and fragments
    ├── my-short-story.md   The story itself (single file)
    └── _Characters/        Optional — only if the cast needs tracking
        └── _Index.md
```

Short stories skip Chapters/, Timeline.md, and _Locations/ unless the notes suggest they're needed.

See also: [[setup-and-plugins]], [[global-rules]], [[story-templates]].
