---
type: guide
status: draft
publish: false
aliases: []
created: 2026-07-30
updated: 2026-07-30
tags: [craft]
summary: "State-tracking discipline: chapter frontmatter as the per-chapter record, file ownership by command, replace-not-append on re-runs, and the source's own stated gaps."
tier: supporting
source: "raw/2026-07/stories-playbook-source.md"
source_url: "https://github.com/gsarig/ai-playbooks/tree/main/playbooks/stories"
campaigns: [Shattered Sea]
uid: 5d5f110a-e9c0-46f2-8abc-8010aba39ed3
---

# Stories Playbook: State-Tracking Discipline

- **Chapter frontmatter** (`chapter`, `title`, `status`, `edit_pass`, `wordcount`, `pov`, `timeline_events`, `locations`, `characters`, `tags`, `cssclasses`) is the per-chapter state record. The author updates `edit_pass` (0 = no pass, 1/2/3 = last completed pass) manually only. `/update-chapter` explicitly never touches it.
- **File ownership by command:** `/update-chapter` may only change frontmatter and the tracking files (Timeline.md, Character files, Location files). Never chapter prose. `/dev-edit`, `/language-edit`, and `/audit-story` stay read-only. They present findings and apply nothing themselves. `/language-edit` returns inline markup and Polish Notes that the author selects from manually.
- **Read protocols per command** specify the files each command reads in full before acting: `/continue-story` reads _Index.md, `CLAUDE.md`, Timeline.md, Quicknotes.md, the last two chapters, and relevant Character files. `/dev-edit` also reads `vault/refs/stories/prose-aesthetic.md` to calibrate its findings.
- **Replace-not-append on re-runs:** when `/update-chapter` is re-run on the same chapter (e.g. after a revision), Character-file `Key Moments` entries and Location-file `Key Events` entries get replaced. No duplicate appends.
- **Timeline format** depends on narrative structure (linear table / grouped list / minimal reference points). That choice governs how both `/new-story` and `/update-chapter` write timeline entries going forward.

## Gaps the source leaves unstated

The source references a `_Dashboard.base` file (a Bases-view story tracker with Active/In Revision/Completed/Abandoned states) and Bases "setup instructions" for _Characters/_Index.md and _Locations/_Index.md, but does not itself contain the Base's field/filter definitions or the referenced Character/Location file templates. It also names a "Publication template" used by `/publish-prep` without including that template's contents. These stay exactly as unstated in the source.

See also: vault/refs/stories/update-chapter.md, vault/refs/stories/new-story.md.
