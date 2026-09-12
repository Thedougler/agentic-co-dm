# Source: gsarig/ai-playbooks — stories playbook (fiction writing workflow for Obsidian + Claude Code)

## SOURCE FILE: README.md

# Stories Playbook

A fiction writing workflow for Obsidian and Claude Code. Works for novels, novellas, and short stories.

Claude Code acts as a writing collaborator: scaffolding story structure, tracking characters and locations, running developmental and language editing passes, flagging continuity errors, and managing the state of your story as it evolves.

---

## What you get

- Slash commands for every stage of the writing process (`/new-story`, `/dev-edit`, `/language-edit`, and more)
- Automatic story scaffolding from rough notes or ideas
- Per-chapter state tracking (characters, locations, timeline, word count)
- Three-pass language editing calibrated to your voice
- Consistency audits across all chapters
- Publication prep when you're ready to ship

---

## Requirements

- [Obsidian](https://obsidian.md) — free, available on Windows, macOS, Linux, iOS, Android
- [Claude Code](https://claude.ai/code) — Anthropic's AI assistant for the command line

---

## Setup

### Step 1 — Open this folder in Obsidian

Download or clone this repository. Open the `stories/` folder as an Obsidian vault:

- Launch Obsidian
- Click **Open folder as vault**
- Select the `stories/` folder inside `playbooks/`

### Step 2 — Install community plugins

In Obsidian, go to **Settings → Community plugins → Browse** and install the following:

| Plugin | What it enables | Required |
|--------|----------------|----------|
| [Templater](https://obsidian.md/plugins?id=templater-obsidian) | Auto-applies the chapter template (with auto-numbered filename) whenever you create a new file in `Chapters/` | Required |
| [LanguageTool Integration](https://obsidian.md/plugins?id=obsidian-languagetool-plugin) | Live grammar and style checking as you write; set your native language for second-language support | Recommended |
| [Editing Toolbar](https://obsidian.md/plugins?id=editing-toolbar) | Floating formatting toolbar; pre-configured with text, list, alignment, and insert commands | Recommended |
| [Smart Typography](https://obsidian.md/plugins?id=obsidian-smart-typography) | Converts straight quotes to curly, double-dash to em dash, and triple-dot to ellipsis as you type | Recommended |
| [Typing Transformer](https://obsidian.md/plugins?id=typing-transformer-obsidian) | Custom keystroke shortcuts; pre-configured with `***` → scene-break divider (`✽✽✽`) and other writing shortcuts | Recommended |
| [Better Word Count](https://obsidian.md/plugins?id=better-word-count) | Status bar showing word count and page count (at 300 words/page); replaces Obsidian's built-in word count | Recommended |
| [Iconize](https://obsidian.md/plugins?id=obsidian-icon-folder) | Adds icons to folders and files in the sidebar; pre-configured for `_Archive`, `_Templates`, `_Ideas`, `_Commands`, and `_Dashboard` | Recommended |
| [Outliner](https://obsidian.md/plugins?id=obsidian-outliner) | Improves list behaviour: better Tab/Enter handling, drag-and-drop reordering, cursor stays on bullet | Recommended |
| [Advanced Cursors](https://obsidian.md/plugins?id=advanced-cursors) | Multi-cursor support; adds Cmd/Ctrl+D to select and edit the next matching word — useful for renaming within a chapter | Recommended |
| [Pandoc Plugin](https://obsidian.md/plugins?id=obsidian-pandoc) | Export your story to DOCX, PDF, EPUB, and other formats directly from Obsidian | Recommended |

After installing each plugin, enable it. The settings for each plugin are already pre-configured in this vault — no manual setup needed.

> **LanguageTool:** If you write in English as a second language, go to **Settings → LanguageTool Integration** and set your native language in the **Mother tongue** field. This helps the plugin distinguish errors from stylistic choices.

> **Pandoc Plugin:** This plugin requires [Pandoc](https://pandoc.org/installing.html) to be installed on your system separately. Install Pandoc first, then install the Obsidian plugin. Once set up, use it to export finished chapters or full manuscripts to DOCX (for editors), EPUB (for ebook distribution), or PDF.

### Step 3 — Configure Claude Code

Open a terminal in the `stories/` folder and run:

```
claude
```

Claude Code will read the `CLAUDE.md` in this vault and be ready to use the slash commands.

### Step 4 — Personalise

Two files are designed for you to customise before writing:

**`CLAUDE.md`** — Edit the **Author** section to describe your language background (if writing in a second language). This calibrates the language editing passes.

**`.claude/skills/writing-style/SKILL.md`** — Your personal aesthetic profile. Leave it blank for now and fill it in after your first story, or ask Claude to build it from writing samples you share.

---

## First steps

Once everything is set up, open Claude Code in the vault folder and try:

```
/new-story
```

Claude will ask whether you want to scaffold from an idea in `_Ideas.md`, start an empty novel structure, or start a short story.

---

## Commands

| Command | Purpose |
|---------|---------|
| `/new-story` | Build a story blueprint from an idea or from scratch |
| `/continue-story` | Re-entry brief for returning to a story after time away |
| `/update-chapter ch-XX` | Post-chapter state sync — updates Timeline, Characters, Locations (also works on single-file short stories) |
| `/dev-edit ch-XX` | Developmental editing pass on a chapter |
| `/language-edit ch-XX 1\|2\|3` | Language and grammar pass (three passes) |
| `/audit-story` | Full consistency audit across all chapters |
| `/publish-prep` | Create promo files and publication record |
| `/archive-story` | Move a completed or abandoned story to the archive |

---

## Folder structure

```
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

---

## Notes on the writing-style skill

The `.claude/skills/writing-style/SKILL.md` file is the most powerful customisation available. Once populated, it tells Claude exactly how your prose works — your sentence rhythm, how you handle interiority, what your characteristic moves are, what should never be suggested. Without it, Claude gives generic feedback calibrated to competent fiction writing. With it, Claude gives feedback calibrated to *your* fiction writing.

To build it, share finished writing with Claude and say: *"Read this and build my writing-style skill from it."*

---

## SOURCE FILE: CLAUDE.md

# Fiction Writing Rules — Global

These rules apply to all stories in this vault. Story-specific rules in each story's own `CLAUDE.md` override these where they conflict.

## Author

<!-- Describe your language background here if relevant to your writing. Example: -->
<!-- "Non-native English speaker (Spanish). Flag constructions that sound like direct translations." -->
<!-- Leave blank if writing in your native language. -->

## Language Rules

Applied during all `/language-edit` passes.

- Flag non-native constructions: unnatural article use, verb tense confusion, over-formal register, and idioms that read as direct translations from another language.
- Prefer simple, direct sentence structure. Flag run-on sentences or complex subordinate clause structures that impede clarity.
- Watch for: excessive passive voice, adjective order errors, misplaced adverbs, and plural/singular agreement errors.
- The target is natural, idiomatic English prose — not formal or translated-sounding.
- Do not auto-apply corrections. Present findings with the original text, the issue, and a suggested fix. Let the author decide.

> **Customise this section:** If you write in English as a second language, describe your native language in the Author section above and update the language rules to reflect the patterns most common in your writing. The `/language-edit` command uses these rules to calibrate its Pass 2 refinement.

## Developmental Editing Defaults

Applied during all `/dev-edit` passes unless the story's `CLAUDE.md` overrides them.

- Flag telling instead of showing in emotional beats.
- Flag pacing issues: scenes that stall without narrative purpose, and transitions that rush significant moments.
- Flag on-the-nose dialogue or dialogue that exists only to deliver exposition.
- Flag repetition of words, phrases, or ideas within a chapter.

## Editing Rules

Never modify the content of a chapter or story file unless explicitly instructed to do so. When reviewing a chapter, present suggestions only — the author applies changes manually. The only exception is batch operations (e.g. renaming a character across all files) when explicitly requested.

`/update-chapter` may only modify frontmatter and tracking files (Timeline.md, Character files, Location files). It must never alter chapter prose.

## Consistency Rules

- Use character names exactly as they appear in their Character file. Flag any variation.
- Use location names exactly as they appear in their Location file. Flag any variation.
- Flag any contradiction with the story's `Timeline.md`.
- When uncertain about a world detail, check `_Index.md` before suggesting.
- If a Character file says a character is dead, do not write them as alive.

## Story Context

Whenever the user references a specific story by name, check whether a folder for that story exists in the vault before responding. If it does, read the story's `CLAUDE.md`, `_Index.md`, and `_Lore.md` in full before engaging with any question about that story. Do not rely on memory or prior context alone.

## Session Start

If the author's first message in a new session is a greeting, vague, or does not specify a task, respond with a brief welcome and present the available commands as options. Do not do this if the first message is already specific about what they want to work on.

## Obsidian Skills

When generating Obsidian content, fetch the relevant skill from the official kepano/obsidian-skills repository before proceeding. Do not generate Obsidian-specific syntax from memory.

| Situation | Skill URL |
|-----------|-----------|
| Working with `.md` files (wikilinks, callouts, frontmatter, embeds) | `https://raw.githubusercontent.com/kepano/obsidian-skills/main/skills/obsidian-markdown/SKILL.md` |
| Working with `.base` files (Bases views, filters, formulas) | `https://raw.githubusercontent.com/kepano/obsidian-skills/main/skills/obsidian-bases/SKILL.md` |

## Commands

| Command | Purpose |
|---------|---------|
| `/new-story` | Build a story blueprint from an idea or from scratch |
| `/continue-story` | Re-entry brief for returning to a story after time away |
| `/update-chapter ch-XX` | Post-chapter state sync — updates Timeline, Characters, Locations, checks Quicknotes |
| `/dev-edit ch-XX` | Developmental editing pass on a chapter |
| `/language-edit ch-XX 1\|2\|3` | Language and grammar pass on a chapter (three passes) |
| `/audit-story` | Full consistency audit across all chapters |
| `/publish-prep` | Create promo files and publication record when ready to publish |
| `/archive-story` | Move a completed or abandoned story to the archive |

---

## SOURCE FILE: _Commands.md

# Claude Code Commands

Run these from inside a story folder.

| Command | Purpose |
|---------|---------|
| `/new-story` | Build a story blueprint from an idea or from scratch |
| `/continue-story` | Re-entry brief for returning to a story after time away |
| `/update-chapter ch-XX` | Post-chapter state sync — updates Timeline, Characters, Locations |
| `/dev-edit ch-XX` | Developmental editing pass on a chapter |
| `/language-edit ch-XX 1\|2\|3` | Language and grammar pass (three passes) |
| `/audit-story` | Full consistency audit across all chapters |
| `/publish-prep` | Create promo files and publication record when ready to publish |
| `/archive-story` | Move a completed or abandoned story to the archive |

---

## `/new-story`

Reads `Quicknotes.md` and builds the full story blueprint. Asks about form (short story / novella / novel) before creating structure.

- **Novel / novella:** creates `_Index.md`, `CLAUDE.md`, `Timeline.md`, `_Lore.md`, `_Lines.md`, `Quicknotes.md`, `Chapters/`, `_Characters/`, `_Locations/`, `_Research/`, `_Assets/`.
- **Short story:** leaner structure — single story file, `_Index.md`, `CLAUDE.md`, `Quicknotes.md`, optional `_Characters/`.

Timeline format is chosen based on narrative structure (linear table / grouped list / minimal reference points).

---

## `/continue-story`

Re-entry brief for returning to a story after time away.

Reads the last two chapters, `_Index.md`, `CLAUDE.md`, `Timeline.md`, and `Quicknotes.md`, then presents: where the story stands, last chapter recap, open threads, Quicknotes to action, and what to write next.

---

## `/update-chapter ch-XX`

Post-chapter sync. Run after finishing or revising a chapter.

Reads the chapter, then proposes (before applying):
- New timeline entries
- New or updated character files
- New or updated location files
- Updated chapter frontmatter (`timeline_events`, `locations`, `characters`, `status`, `wordcount`)
- Quicknotes items that appear to have been addressed
- Any inconsistencies found against existing notes

Works on single-file short stories too — pass the story filename instead of a chapter reference.

---

## `/dev-edit ch-XX`

Developmental editing pass on a chapter or story file. Prompts to switch to Opus before starting.

Covers: structure and pacing, showing vs. telling, dialogue, POV consistency, repetition, continuity, story-specific focus areas (from `CLAUDE.md`), and strengths. Calibrated to the author's writing-style skill.

Read-only — presents findings only, applies nothing.

---

## `/language-edit ch-XX 1|2|3`

Language and grammar pass. Pass number is required.

- **Pass 1** — Errors only: grammar, syntax, punctuation, clear non-native constructions
- **Pass 2** — Refinement: subtle idiomaticity issues, rationale explained for every change. Prompts to switch to Opus.
- **Pass 3** — Final sweep: minimal, genuine errors only, fresh read

Returns inline markup (~~strikethrough~~ old / **bold** new) with sequential Polish Notes. Applies nothing — author selects changes.

---

## `/audit-story`

Full consistency audit across all chapters, timeline, characters, and locations.

Checks: timeline consistency, character consistency (status, traits, names), location consistency, world rule violations, orphaned notes, frontmatter gaps.

Read-only — presents findings only.

---

## `/publish-prep`

Creates the `_Promo/` folder (Blurb, Tags, Campaign) and `_Publication.md` when a story is ready for publication. Pre-fills what it can from `_Index.md`; leaves the rest as placeholders.

---

## `/archive-story`

Moves a completed or abandoned story to `_Archive/Completed/` or `_Archive/Abandoned/`. Updates `_Index.md` status. Asks before applying. Suggests running `/publish-prep` first if the story is complete and has no publication file.

---

## SOURCE FILE: .claude/skills/writing-style/SKILL.md

---
name: writing-style
description: The author's aesthetic philosophy, prose style, and creative sensibility. Use whenever writing, editing, suggesting, or evaluating anything related to the author's fiction — stories, chapters, characters, scenes, or developmental feedback.
---

# Author Writing Style

> **This file is a placeholder.** It is meant to capture your personal aesthetic so Claude can calibrate editing feedback to your voice rather than generic standards.
>
> Fill it in yourself, or ask Claude to build it for you: share a few pieces of your published or finished writing and say "Build my writing-style skill from these." Claude will read the work and extract patterns — sentence rhythm, narrative distance, how you handle interiority, what your prose does that is distinctly yours.
>
> The more specific this file is, the more useful `/dev-edit` and `/language-edit` become. Vague preferences ("I like short sentences") produce vague feedback. Specific patterns ("I use single-sentence paragraphs as ironic payoffs, not as emphasis — never suggest expanding them") produce precise, calibrated feedback.

---

## Core Aesthetic

<!-- What is the single thread running through everything you write? Genre, register, the kind of strangeness or truth you are after. -->

---

## Prose Style

<!-- How do your sentences actually work? Rhythm, length variation, use of fragments, relationship between narration and interiority. -->

---

## Narrator and Voice

<!-- Reliability, distance, whether perspective shifts are a device or an error in your work, use of free indirect discourse. -->

---

## Structure

<!-- How you build stories: linear vs. non-linear, chapter titles, embedded forms, how you handle time. -->

---

## What You Do Not Do

<!-- Patterns to never suggest. Moves that would break your voice. Endings you would never write. -->

---

## Influences and What They Mean in Practice

<!-- Not a reading list — specific techniques you have absorbed from writers you admire, and how they appear in your own work. -->

---

## Developmental Feedback Calibration

<!-- How Claude should interpret your choices during a dev-edit pass. What looks like an error but is intentional. What should always be questioned. -->

---

## Source Note

<!-- How this skill was built (from which works, when last updated). Update this when you add new material. -->

---

## SOURCE FILE: .claude/commands/new-story.md

Begin by checking whether a title was passed as an argument ("$ARGUMENTS").

---

## Step 0 — Choose a path

If no argument was given, present the following options to the author and wait for their choice before doing anything else:

> **Starting a new story. How would you like to proceed?**
>
> 1. **From an idea** — scaffold from a specific idea in `_Ideas.md`
> 2. **Empty novel / novella** — create the full structure with blank files, ready to fill in
> 3. **Short story** — create a lean structure with a single prose file

If a title argument was given, go directly to **Option 1** and skip the menu.

---

## Option 1 — Scaffold from `_Ideas.md`

### 1a — Find the idea

Read `_Ideas.md` from the vault root.

Ideas are separated by `---` (horizontal rule). Each idea has a `##` heading as its title. Parse the file into individual idea blocks using `---` as the boundary.

- If a title argument was given: find the block whose `##` heading matches (case-insensitive, partial match acceptable). If no match, tell the author and list available titles.
- If no title argument was given: list all idea titles found and ask the author which one to use. Wait for their answer before continuing.

### 1b — Extract and remove

Once the target idea is identified:

1. Copy its full content (heading + body) — this becomes the story's `Quicknotes.md`.
2. Remove the idea block from `_Ideas.md`, including its surrounding `---` separators (but do not leave a double `---` gap or a dangling separator). Write the cleaned file back.

### 1c — Understand the premise

Read the extracted content carefully. The notes may be in any language (including Greek — translate internally, the story will be in English). Extract:

- Story title (use the `##` heading, or propose a refinement if the heading is vague)
- **Approximate form: short story / novella / novel** — ask if unclear
- Genre
- Core premise (1–3 sentences)
- Known characters and any details
- Known locations
- Known world rules or lore
- Structural ideas (ending, key scenes, themes, narrative structure)
- Open questions (things still undecided)

Present your understanding to the author. Confirm the story title and form before building anything.

### 1d — Build the structure

**For novels and novellas**, create inside `{Story Title}/`:

```
{Story Title}/
├── _Index.md          (populated from the idea notes)
├── CLAUDE.md          (populated from world rules and tone notes)
├── Timeline.md        (format chosen based on story structure — see Timeline rules below)
├── Quicknotes.md      (the extracted idea content, preserved verbatim)
├── Chapters/
│   └── ch-01.md       (empty chapter file with frontmatter, no prose)
├── _Characters/
│   └── _Index.md      (Bases setup + any characters mentioned in the notes)
├── _Locations/
│   └── _Index.md      (Bases setup + any locations mentioned in the notes)
├── _Research/
└── _Assets/
```

**For short stories**, create inside `{Story Title}/`:

```
{Story Title}/
├── {Story Title}.md   (the story itself — blank, ready to write)
├── _Index.md          (premise, themes, lore, open questions)
├── CLAUDE.md          (world rules and tone — may be minimal)
├── Quicknotes.md      (the extracted idea content, preserved verbatim)
├── _Characters/
│   └── _Index.md      (only if characters were mentioned in the notes)
└── _Assets/
```

No `Chapters/`, no `Timeline.md`, no `_Locations/` for short stories unless the notes suggest they're needed.

---

## Option 2 — Empty novel / novella

Ask for the story title if not already provided. Wait for the answer.

Create the following inside `{Story Title}/`. All files are minimal — frontmatter and section headers only. Do not invent any content.

```
{Story Title}/
├── _Index.md
├── CLAUDE.md
├── Timeline.md
├── Quicknotes.md      (empty — just a heading)
├── Chapters/
│   └── ch-01.md       (empty chapter file with frontmatter, no prose)
├── _Characters/
│   └── _Index.md
├── _Locations/
│   └── _Index.md
├── _Research/
└── _Assets/
```

**`_Index.md`** — include the title and status in frontmatter, placeholder sections for premise, themes, world rules, and open questions. Nothing filled in.

**`CLAUDE.md`** — include the standard section headers (Story Identity, World Rules, Character Voice Guidelines, Developmental Focus, Open Rules) with everything blank.

**`Timeline.md`** — include a note that the format should be decided when the story's structure is clearer, and a placeholder for the first strand.

**`_Characters/_Index.md`** and **`_Locations/_Index.md`** — Bases setup instructions only (see Option 1 for the format).

---

## Option 3 — Empty short story

Ask for the story title if not already provided. Wait for the answer.

Create a lean structure. No `Chapters/`, no `Timeline.md`, no `_Locations/`.

```
{Story Title}/
├── {Story Title}.md   (blank prose file — just a title heading)
├── _Index.md          (frontmatter + placeholder sections, nothing filled in)
├── CLAUDE.md          (minimal — section headers only)
├── Quicknotes.md      (empty — just a heading)
└── _Assets/
```

No `_Characters/` unless the author mentions the story has notable characters. Ask if unsure.

---

## Timeline format rules (Option 1 novels only)

Choose the format based on the story's structure:

- **Linear narrative:** standard table — `Story Date | Chapter | Event | Characters | Location | Notes`
- **Non-linear, parallel timelines, or flashback-heavy:** grouped list — events grouped by strand or character, with notes on temporal position and how strands connect
- **Circular or paradoxical structure:** minimal reference list only — note explicitly that timeline order is the story's central conceit

---

## Chapter file format (ch-01.md)

All chapter files use this frontmatter:

```yaml
---
chapter: 1
title: ""
status: draft
edit_pass: 0
wordcount:
pov:
timeline_events: []
locations: []
characters: []
tags:
  - chapter
cssclasses:
  - chapter
---
```

Leave the title field empty — the author fills it in when they have one.

---

## Step — Report

When everything is created, present a brief summary:
- What was built
- What is empty and needs filling in
- Any open questions that should be resolved before writing begins

---

## SOURCE FILE: .claude/commands/continue-story.md

Read the following files in full:
- `_Index.md`
- `CLAUDE.md`
- `Timeline.md` (if it exists)
- `Quicknotes.md`
- The last two chapter files (by chapter number, not modification date) — or the single story file if this is a short story
- Any Character files for characters appearing in those final chapters

Then present a structured re-entry brief to help the author pick up where they left off.

---

## Re-entry Brief: {Story Title}

### Where the story stands
A 2–3 sentence summary of the story's current state: what has happened, where we are in the arc, and what the narrative momentum is pointing toward.

### Last chapter recap
What happened in the most recent chapter. Key beats, character states, where it ended. Be specific — quote or closely paraphrase important moments.

### Open threads
Unresolved plot threads, unanswered questions, and character arcs in progress. Draw from Timeline.md, character files, and _Index.md open questions section.

### Quicknotes to action
Any items in Quicknotes.md that appear ready to be written — ideas, fragments, or reminders that seem to belong to what comes next.

### What to write next
Based on everything above: what does the story appear to need next? Not a prescription — just an orientation. One short paragraph.

---

Keep the brief tight. The goal is to get the author back into the world in under two minutes of reading.

---

## SOURCE FILE: .claude/commands/update-chapter.md

Locate the file to update from "$ARGUMENTS":
- If the story uses a `Chapters/` folder, find the file whose name starts with or matches the argument (e.g. "ch-05" → `Chapters/ch-05*.md`).
- If the story is a single-file short story, the argument will be the story filename itself (e.g. "Full Circle" → `Full Circle.md` in the story root).
- If the argument is ambiguous, list matching files and ask which one to use.

Then read the following files in full:
- `Timeline.md` (if it exists)
- `_Characters/_Index.md` and any individual Character files for characters mentioned in the chapter
- `_Locations/_Index.md` and any individual Location files for locations mentioned in the chapter
- `Quicknotes.md`
- `_Index.md` (for world/lore context)
- `CLAUDE.md` in this story folder (for continuity anchors and world rules)

Based on everything you have read, prepare the following updates. **Present them to the author as a structured summary before applying anything. Wait for confirmation.**

---

### 1. Timeline updates

Before proposing timeline entries, consider the story's temporal structure:
- **Linear:** propose entries in story-chronological order with story date, chapter reference, event description, characters, location.
- **Non-linear or multi-strand:** group entries by timeline strand or character arc; note temporal position relative to other events rather than asserting a single sequence. Flag where chronological order is uncertain or deliberately ambiguous.
- **Circular or paradoxical:** note the temporal position of events relative to the story's own logic, not an external timeline. Do not flatten paradoxical or simultaneous events into a sequence that implies a linearity the story rejects.

If Timeline.md does not exist (common for short stories), propose whether one is worth creating given what the story contains. If the story is short and self-contained, it may not be needed.

### 2. Character updates

For each character appearing in this file:
- **New characters:** create a Character file using the template. Set `first_appearance` to this chapter or file. Add this chapter to `appearances`.
- **Existing characters:**
  - Add this chapter to the `appearances` array in frontmatter (if not already present).
  - Update `last_seen` to this chapter.
  - Note any changes to `status` (alive/dead/missing) or Relationships.
  - Add or update a `Key Moments` entry for this chapter. Use a short list of bullets under the chapter heading, one per significant beat involving this character:
    ```
    - **Ch-XX:**
      - What the character does or discovers.
      - How they respond or what changes for them.
      - Any significant interaction, decision, or revelation.
    ```
    Include only beats that are narratively significant — not every action. One bullet is fine if the chapter is light on this character. If `/update-chapter` is run again on the same chapter (e.g. after a revision), replace the existing entry for that chapter rather than appending a duplicate.

For the character's name in the file: use whatever the story uses. Descriptive labels — "The Boy", "The Mother", "The Man" — are valid character names if that is how the story refers to them. Do not invent or infer a real name that the story deliberately withholds.

### 3. Location updates

For each location appearing in this file:
- **New locations:** create a Location file using the template. Set `first_appearance` to this chapter or file. Add this chapter to `appearances`.
- **Existing locations:**
  - Add this chapter to the `appearances` array in frontmatter (if not already present).
  - Add or update a `Key Events` entry for this chapter. Use a short list of bullets under the chapter heading, one per significant event at this location:
    ```
    - **Ch-XX:**
      - What happens here in this chapter.
      - Any change to the location's significance or atmosphere.
    ```
    Include only events that are narratively significant. One bullet is fine for minor appearances. If `/update-chapter` is run again on the same chapter, replace the existing entry rather than appending a duplicate.

### 4. Frontmatter update

Proposed values for:
- `timeline_events` — list of story-time anchors for key events. For non-linear stories, include a brief note on temporal position where relevant.
- `locations` — all locations appearing
- `characters` — all characters appearing, using whatever names or labels the story uses
- `status` — keep existing value unless you have a reason to change it
- `wordcount` — count the words in the chapter and update this field
- `edit_pass` — do not change this field; it is updated manually by the author to track language editing progress (0 = no pass, 1/2/3 = last completed pass)

Note: `appearances` and `last_seen` are maintained in the individual Character and Location files (updated in steps 2 and 3 above), not in the chapter frontmatter.

### 5. Quicknotes check

List any items in `Quicknotes.md` that appear to have been addressed or placed in this chapter or file. Flag them for the author — do not remove them until confirmed.

### 6. Inconsistencies

List any contradictions found between this file and the existing notes (Timeline, Character files, Location files, `_Index.md`). Be specific: quote the conflicting text. Do not flag deliberate ambiguity or unexplained elements as inconsistencies — only flag things that appear to contradict an established fact.

---

After the author confirms (all, partial, or with modifications), apply the approved changes.

---

## SOURCE FILE: .claude/commands/dev-edit.md

**Before starting:** This task benefits from Opus. If you are currently on Sonnet, let the author know and suggest switching with `/model opus` before proceeding. Wait for their response.

Locate the file to edit from "$ARGUMENTS":
- If a `Chapters/` folder exists, find the file whose name starts with or matches the argument.
- If no `Chapters/` folder exists (short story), look for the file in the story root.
- If ambiguous, list matches and ask.

Then read:
- `CLAUDE.md` in this story folder (world rules, character voice, developmental focus)
- `_Index.md` (premise, themes, lore)
- The preceding chapter if it exists (for continuity context)
- Any Character files for characters appearing in this chapter (for voice drift checks)
- The writing-style skill at `../.claude/skills/writing-style/SKILL.md` (author's aesthetic — use this to calibrate every finding)

Perform a **developmental editing pass** on the chapter. Do not rewrite. Return structured findings only — the author decides what to act on.

---

## Developmental Edit Report: $ARGUMENTS

### Structure & Pacing
Note scenes that stall without narrative purpose, or significant moments that feel rushed. Be specific about which paragraph or beat.

### Showing vs Telling
Quote instances where an emotional beat is told rather than shown. Suggest the showing approach briefly.

### Dialogue
Flag:
- On-the-nose dialogue (characters saying exactly what they mean or feel)
- Exposition dumps disguised as conversation
- Voice drift from the character's established speech pattern (check `CLAUDE.md`)

### POV Consistency
Flag any head-hopping or POV slippage if the story uses a limited perspective.

### Repetition
List repeated words, phrases, or ideas within this chapter. Group by type (word-level vs. idea-level).

### Continuity
Flag anything that conflicts with established facts from `_Index.md`, character files, or the timeline.

### Story-Specific Focus
Apply the developmental priorities listed in this story's `CLAUDE.md`. Note findings under each listed priority.

### Strengths
Note what is working well. Developmental editing is not only corrective.

---

Do not apply changes. Present findings only.

---

## SOURCE FILE: .claude/commands/language-edit.md

Parse "$ARGUMENTS" to extract the chapter reference and pass number (e.g. "ch-01 2" = chapter ch-01, pass 2). If no pass number is given, ask: "Which pass? 1 (errors), 2 (refinement), or 3 (final sweep)."

**If the pass number is 2:** This pass benefits from Opus. If you are currently on Sonnet, let the author know and suggest switching with `/model opus` before proceeding. Wait for their response.

Locate the file from the chapter reference:
- If a `Chapters/` folder exists, find the file whose name starts with the chapter reference.
- If no `Chapters/` folder exists (short story), look for the file in the story root.

Also read this story's `CLAUDE.md` and the vault-level `CLAUDE.md`. Use them to distinguish intentional stylistic choices from genuine errors — never flag or correct deliberate form.

Read the writing-style skill at `../.claude/skills/writing-style/SKILL.md`. This is the single source of truth for the author's aesthetic. Any pattern described there is intentional and must not be flagged as an error.

**Standard across all passes:** American English, Chicago Manual of Style (CMOS), Oxford comma.

**Output format (all passes):**
- For each paragraph, show inline edits using ~~strikethrough~~ for deletions and **bold** for additions.
- If a paragraph needs no changes, return it unchanged with a Polish Note stating "No substantive corrections needed."
- Follow each paragraph with a **Polish Note** labeled sequentially (PN1, PN2, PN3…) across the full chapter.
- Process the entire chapter. Do not summarise or add commentary outside the Polish Notes.

---

## Pass 1 — Errors

**Job:** Fix what is broken. Grammar, syntax, CMOS punctuation, clear non-native constructions that impede comprehension. Do not chase subtlety — that is Pass 2's job.

**Correct:**
- Grammar and syntax errors.
- CMOS punctuation (American quotation conventions, Oxford comma, capitalisation, numbers).
- Non-native constructions that cause misreading or genuine confusion.
- Dummy pronouns and unclear pronoun references where fixing yields a clear improvement.
- Maintain past-tense narration except inside dialogue.

**Do not:**
- Fix phrasing that is grammatically correct but sounds slightly non-native — flag it in the Polish Note, leave it for Pass 2.
- Rephrase for style, rhythm, or flow.
- Add, remove, or invent content.

**Polish Note format:** One line. State what was corrected and why. If flagging something for Pass 2, quote the phrase and note: "Pass 2: [brief reason]."

---

## Pass 2 — Refinement

**Job:** Assume errors are fixed. Now focus on what is technically correct but still sounds non-native to a fluent English ear.

**Target:**
- Non-native constructions specific to the author's first language (see vault-level `CLAUDE.md` for language background). Look for: unnatural article use, literal preposition choices, calqued idioms, word order that reflects the source language, constructions that are grammatically acceptable but mark non-native usage.
- Phrasing that is idiomatically weak in American English even though it is not wrong.
- Distracting word repetitions — list up to three alternatives in the Polish Note; do not force replacements.

**Be more assertive than Pass 1** on idiomatic fixes, but preserve voice. If a construction is intentional or fits the author's register, leave it.

**Polish Note format:** Two parts on one line separated by `|`:
- **Part A:** What was done (one line).
- **Part B:** Rationale — why the change preserves meaning and voice; quote flagged phrases; list alternatives separated by semicolons.

Example: `PN4: Changed "he was feeling" to **he felt** | Non-native construction: source language uses progressive where English prefers simple past in narration; preserves tense and voice.`

---

## Pass 3 — Final Sweep

**Job:** Read as if seeing the text fresh. Flag only what genuinely sticks out. Minimal by design — do not manufacture changes.

**Correct only:**
- Genuine grammatical or consistency errors that slipped through.
- CMOS issues not caught earlier.
- Anything that would make a native reader pause involuntarily.

**Do not:**
- Re-examine idiomaticity already addressed.
- Rephrase for preference.
- Add commentary on structure, pacing, or style.

**Polish Note format:** One line. If nothing sticks out in a paragraph, return it unchanged and write "No substantive corrections needed." Keep the entire pass light — if you find yourself making many changes, stop and flag that the text may need another Pass 2 instead.

---

## SOURCE FILE: .claude/commands/audit-story.md

Read the following files in full:
- `_Index.md`
- `CLAUDE.md`
- `Timeline.md` (if it exists)
- All files in `_Characters/` (if the folder exists)
- All files in `_Locations/` (if the folder exists)
- All chapter files in `Chapters/` if the folder exists; otherwise read the single story file in the story root (short story structure)

Then produce a **full consistency audit** across the entire story. This is a read-only operation — present findings only, apply nothing.

---

## Story Audit Report

### Timeline Consistency
- Identify any events in the chapters that contradict the timeline order in `Timeline.md`.
- Identify any events in `Timeline.md` that are not supported by chapter text.
- Flag any time jumps that are established in the timeline but not explained in the chapters.

### Character Consistency
For each character in `_Characters/`:
- Verify `first_appearance` matches the actual chapter where they are introduced.
- Verify `last_seen` is up to date.
- Verify `status` (alive/dead/missing) is consistent with the most recent chapter they appear in.
- Flag any chapter where the character behaves in a way that contradicts their established voice or arc.

### Location Consistency
For each location in `_Locations/`:
- Verify `first_appearance` is accurate.
- Flag any chapter where a location is described in a way that contradicts its established description.
- Flag locations mentioned in chapters but missing from `_Locations/`.

### World Rule Violations
Check all chapters against the world rules in `_Index.md` and `CLAUDE.md`. List any violation, quoting the offending text.

### Orphaned Notes
- Characters mentioned in chapters but with no Character file.
- Locations mentioned in chapters but with no Location file.
- Timeline entries that reference chapters that don't exist yet.

### Chapter Frontmatter Gaps
List any chapters with incomplete frontmatter (missing characters, locations, or timeline_events fields).

### Summary
A short prioritised list of the most significant issues found.

---

## SOURCE FILE: .claude/commands/publish-prep.md

Read `_Index.md` to confirm the story title and current status.

Then create the following in the current story folder and populate what can be inferred from `_Index.md`. Leave everything else as empty placeholders — do not invent details.

---

## Files to create

**`_Promo/Blurb.md`**
A working document for the story's blurb. Pre-fill with the premise from `_Index.md` as a starting point — this is a draft, not a final blurb.

**`_Promo/Tags.md`**
A working document for keywords, categories, and tags for storefronts. Pre-fill with genre and any themes noted in `_Index.md`.

**`_Promo/Campaign.md`**
An empty document for marketing campaign notes, ARC list, launch plan, etc.

**`_Publication.md`** (in the story root)
Use the Publication template. Pre-fill the title. Leave storefront links, ISBN/ASIN, and cover path as empty placeholders.

---

After creating the files, present a summary of what was created and what the author needs to fill in manually.

---

## SOURCE FILE: .claude/commands/archive-story.md

Read `_Index.md` in the current story folder to confirm the story title and current status.

Then ask the author: **"Archive as Completed or Abandoned?"**

Wait for the answer before proceeding.

---

Once confirmed, propose the following actions and wait for approval before applying:

1. **Update `_Index.md` frontmatter** — set `status` to `complete` or `abandoned` as appropriate.
2. **Move the story folder** to `../_Archive/Completed/` or `../_Archive/Abandoned/` accordingly.

Present the exact folder path the story will move to so the author can confirm.

---

After the author approves, apply both changes and confirm completion.

Note: if the story is being archived as **Completed** and does not yet have a `_Publication.md` file, suggest running `/publish-prep` before or after archiving to capture publication details.

---

## SOURCE FILE: _Templates/Story CLAUDE.md

# Claude Code Rules — {{Story Title}}

> Story-specific rules. These override the vault-level `CLAUDE.md`.
> Fill this in before writing begins. Refine it as the story evolves.

---

## Story Identity
- **Genre:**
- **Length:** short story | novella | novel
- **POV:** (leave blank to inherit vault default)
- **Tense:** (leave blank to inherit vault default)
- **Tone & Atmosphere:**

---

## World Rules

<!-- Anything Claude must treat as established, non-negotiable fact. -->
<!-- Add one rule per line. Be specific. -->

-

---

## Character Voice Guidelines

<!-- How specific characters speak or think. Claude uses this in dev-edit to flag voice drift. -->
<!-- Example: "Mira speaks in clipped, defensive sentences. She never volunteers information." -->

-

---

## Developmental Focus for This Story

<!-- Weaknesses you are actively working on. Claude will prioritize flagging these. -->
<!-- Example: "Watch for over-explaining the magic system — trust the reader." -->

-

---

## Continuity Anchors

<!-- High-stakes facts Claude must never contradict, even in suggestions. -->
<!-- Example: "The main character's father is dead. He cannot appear alive." -->

-

---

## Open Rules

<!-- Things still undecided. Claude should ask rather than assume. -->

-

---

## SOURCE FILE: _Templates/Lines.md

---
title: Reserved Lines — {{story title}}
tags:
  - lines
---

# Reserved Lines

Lines to be used at some point. Speaker and approximate placement noted where known. Do not force them — find where they land naturally.

---

<!-- Add a section per character or thematic group. Example: -->

## {{Character Name}}

**"The line goes here."**
Context note: when this line might land, what it signals, why it matters. Leave blank if unknown.

---

<!-- To add a new line: duplicate the block above. -->
<!-- To mark a line as used: add "~~" strikethrough or move it to a Used section below. -->

---

## SOURCE FILE: _Templates/Lore.md

---
title: Lore — {{story title}}
tags:
  - lore
  - worldbuilding
---

# Lore — {{story title}}

> Detailed worldbuilding reference. Populated over time as the story develops.
> Summarise world rules in `_Index.md` — keep the rich detail here.
> Claude reads this file in full when you reference this story by name.

---

## World Rules

<!-- Established facts about how this world works. Be specific. -->
<!-- These are non-negotiable — Claude will not contradict them. -->

-

---

## Cosmology / Premise

<!-- The central conceit, mechanism, or speculative premise of the story. -->
<!-- Include what is deliberately left unexplained and why. -->

---

## Factions / Institutions

<!-- Groups, organisations, power structures that shape the world. -->

---

## History & Mythology

<!-- Background events the reader may never see but that shape character and world. -->

---

## Objects & Technology

<!-- Significant objects, technologies, or systems with their own rules. -->

---

## Deliberate Silences

<!-- Things that are intentionally never explained in the text. -->
<!-- List them here so Claude does not try to fill them in. -->

-

---

