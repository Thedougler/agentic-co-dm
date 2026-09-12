---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "The /update-chapter command: proposing and applying Timeline, Character, Location, and frontmatter updates after a chapter is written."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: c8ee369f-fe49-4996-acc5-0ebb7f452505
---

# Stories Playbook: /update-chapter ch-XX

Locates the target file: in a Chapters/ folder by name match (e.g. "ch-05" → `Chapters/ch-05*.md`). For single-file short stories, the argument is the story filename itself. If ambiguous, it lists matches and asks.

Reads in full: Timeline.md (if it exists), _Characters/_Index.md and individual Character files for characters mentioned, _Locations/_Index.md and individual Location files for locations mentioned, Quicknotes.md, _Index.md, and the story's own `CLAUDE.md`. **Presents proposed updates as a structured summary before applying anything, and waits for confirmation:**

1. **Timeline updates**: linear stories get entries in story-chronological order (date, chapter, event, characters, location). Non-linear/multi-strand stories get entries grouped by strand or character arc, noting temporal position relative to other events rather than a single sequence, flagging deliberately ambiguous order. Circular/paradoxical stories get temporal position noted relative to the story's own internal logic, never flattened into a rejected external sequence. No Timeline.md (common for short stories)? Propose whether one is worth creating.
2. **Character updates**: new characters get a Character file from the template (`first_appearance` = this chapter, chapter added to `appearances`). Existing characters get this chapter added to `appearances`, `last_seen` updated, `status`/Relationships changes noted, and a `Key Moments` entry added under a chapter heading. Each bullet covers one important beat (what they do/discover, how they respond, any significant interaction/decision/revelation). Only narratively important beats. **Re-running on the same chapter replaces the existing entry rather than appending a duplicate.** Character names use whatever the story uses. Descriptive labels ("The Boy") are valid. Never invent a name the story withholds.
3. **Location updates**: same pattern. New locations get a Location file (`first_appearance`/`appearances` set). Existing locations get `appearances` updated and a `Key Events` entry added or replaced (what happens here, any change to significance/atmosphere).
4. **Frontmatter update**: proposes `timeline_events`, `locations`, `characters`, `status` (kept as-is unless there's a reason to change), `wordcount` (recounted). **`edit_pass` is never changed by this command** (the author updates it manually: 0 = no pass, 1/2/3 = last completed pass). `appearances`/`last_seen` live in the Character/Location files, not chapter frontmatter.
5. **Quicknotes check**: lists items that appear addressed or placed in this chapter. Flags them but doesn't remove until confirmed.
6. **Inconsistencies**: lists contradictions with existing notes, quoting the conflicting text. Deliberate ambiguity or unexplained elements are never flagged as inconsistencies.

After confirmation (all, partial, or with modifications), applies the approved changes. Works on single-file short stories too.

See also: [[new-story]], [[continue-story]], [[state-tracking]].
