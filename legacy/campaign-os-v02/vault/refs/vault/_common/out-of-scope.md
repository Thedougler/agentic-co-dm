---
type: agent-guidance
status: pending
publish: false
aliases: []
summary: "Work that belongs to another skill or phase, and which one owns it — canon edits, publishing, prose craft, art, audio, faction clocks."
created: "2026-08-03"
updated: "2026-08-15"
tags: [craft]
uid: b15b8995-850a-4052-aa04-4f73a58f5c26
---

# Draft — Shared Out Of Scope

Every draft guide routes this work to its real owner instead of doing it
itself. A per-type guide adds the neighbours specific to its type and never
restates a row from here.

| This need | Route to |
|---|---|
| Content already `status: canon` | `canon-review` |
| Flipping `status:` past `pending`, or touching `publish:` | `vault/refs/vault/_common/lifecycle.md`'s two gates |
| A named entity that belongs to a different content type | `vault/refs/vault/_common/handoffs.md`'s routing table |
| Read-aloud paragraph craft, boxed text | `dnd5e-scene-narration` |
| Prose polish beyond stating the facts plainly | `draft-story` (shaping is its DS4 step) |
| Generating art of any kind | `visual-aids` |
| Spoken dialogue audio, ElevenLabs voice design | `npc-voice` |
| Advancing a faction's front clock in canon | `world-update`, after [[ingest\|INGEST]] |
| Assembling the session run guide, or what a session advances | `draft-run-guide` |
| An at-table situation's own content | `composing-beats`' Beat |
| A divergence between two Beats | the Beat Chart's Live Branches |
| Transcribing an existing source document faithfully | `llm-wiki-ingest` |
| Rendering battlemap art | `battlemap-render` |

A draft guide links to the output of these; it never inlines their work.
