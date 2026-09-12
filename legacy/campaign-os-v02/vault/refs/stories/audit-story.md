---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "The /audit-story command: a read-only consistency audit across timeline, characters, locations, world rules, and chapter frontmatter."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: 6b15275b-5b18-4e69-852b-0f265100dbad
---

# Stories Playbook: /audit-story

Reads in full: _Index.md, the story's rules file, Timeline.md (if it exists), all files in _Characters/ (if it exists), all files in _Locations/ (if it exists), and all chapter files in Chapters/ (or the single story file for short stories).

Read-only: presents findings only, applies nothing. Report shape:

## Story Audit Report

- **Timeline Consistency**: events in chapters contradicting Timeline.md's order. Events in Timeline.md not supported by chapter text. Time jumps established in the timeline but not explained in the chapters.
- **Character Consistency**: for each character in _Characters/, verifies `first_appearance` matches the actual introducing chapter. Confirms `last_seen` is current. Checks `status` (alive/dead/missing) is consistent with the most recent chapter appearance. Flags any chapter where behavior contradicts established voice or arc.
- **Location Consistency**: for each location in _Locations/, verifies `first_appearance` is accurate. Flags any chapter describing a location in a way that contradicts its established description. Flags locations mentioned in chapters but missing from _Locations/.
- **World Rule Violations**: checks all chapters against _Index.md and the story's rules file. Lists any violation with the offending text quoted.
- **Orphaned Notes**: flags any reference (character, location, or timeline entry) that points to a missing or non-existent file.
- **Chapter Frontmatter Gaps**: chapters with incomplete frontmatter. Missing characters, locations, or `timeline_events` fields.
- **Summary**: a prioritised shortlist of the most critical issues found.

See also: [[continue-story]], [[update-chapter]], [[state-tracking]].
