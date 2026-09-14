---
title: Session 11 assets
category: journal
tags: [shattered-sea, session]
type: session-prep
kind: session-plan
lifecycle: proposed
campaign: shattered-sea
visibility: dm
summary: Drop map for Session 11 summary, transcript, and recording.
created: 2026-09-14
updated: 2026-09-14
---

# Session 11 — asset drop map

All Session 11 post-play files live in **this folder** (same as plan/beats). Do not use `wiki/journal/sessions/shattered-sea/recaps/` or flat `wiki/journal/`.

| What Nick pushes | File here (current standard) | Notes |
|---|---|---|
| Player-facing / table **summary** | `Session-11-Recap.md` | `type: recap`; scaffold from `wiki/templates/recap.md`. Or drop raw into `wiki/_raw/` and run wiki-ingest → files here. |
| **Transcript** (text) | `Session-11-Transcript.md` | Companion note in this folder. Raw dump may land in `wiki/_raw/Session-11-Transcript.md` first; ingest cleans into this path. |
| **Recording** (audio/video) | `wiki/attachments/session-11-recording.{ext}` | Flat attachments; kebab + role `recording`. Optional embed from the recap: `![[attachments/session-11-recording.ext]]`. |

## Already in this folder

Session plan + beats (`Session-11-00-…` through `Session-11-10-…`) — prep only; not the post-play summary.

## Pipeline after drop

1. Recording → attachments (above).
2. Transcript raw → `_raw/` or this folder → `session-transcript-ingest` / reconcile → evidence packet.
3. Summary / recap → `Session-11-Recap.md` via `session-recap` after wrapup accept (or ingest if Nick already wrote it).
4. `session-wrapup` owns durable DM log + canon; do not invent lore on file.

Empty `_raw/` after promote (move sources to `wiki/_archive/`).
