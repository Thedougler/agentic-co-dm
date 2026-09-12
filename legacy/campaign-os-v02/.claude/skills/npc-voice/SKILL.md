---
name: npc-voice
description: Generate literal spoken NPC dialogue audio via ElevenLabs, in a Campaign OS repo (vault/ present). Use for "give this NPC a voice", "generate dialogue audio", "voice line for X", "make X say...", "design a voice", "what does X sound like". Never another TTS provider. Not table audio (record-session-audio) or scene music (draft-run-guide).
---

# npc-voice

## Overview

Generates NPC dialogue clips with ElevenLabs and saves them into the wiki, where a
native Obsidian embed (`![[clip.mp3]]`) renders an inline play button — no plugin or
button infrastructure. Custom voices persist in the GM's ElevenLabs account and on the
NPC's page (`voice_id` frontmatter), so the same NPC always speaks with the same voice.

One-time setup: `cd .claude/skills/npc-voice/scripts && npm install`, and put
`ELEVENLABS_API_KEY` in `.env.local` at the repo root.

## Commands

Run from repo root: `npm run voice -- <command> ...`

| Command | Cost | Does |
|---|---|---|
| `voices [--search <q>]` | free | List account voices (voice_id, name, description). |
| `design "<voice description>" [--text "<sample line>"] [--out <dir>]` | $$ | Generate ~3 voice previews into a temp dir. Prints preview path + `generated_voice_id` per row. Previews NEVER go in the vault. |
| `create --name "<Name>" --description "<desc>" --generated-voice-id <id>` | free | Save the GM's picked preview as a permanent account voice; prints its `voice_id`. |
| `say --voice <voice_id> --text "<line>" --out <path>.mp3 [--stability <0..1>] [--similarity <0..1>] [--dry-run] [--force]` | $ | Generate one dialogue clip. `--dry-run` validates and prints the planned call without paying. Refuses to overwrite without `--force`. |

## Workflow — one dialogue clip

1. Read the NPC's page frontmatter. `voice_id` set → skip to step 4. (Grep the page —
   never assume; the whole point is one NPC, one voice, every session.)
2. No `voice_id`: run `voices --search` first — an existing account voice the GM already
   likes beats paying to design a new one. Offer matches to the GM.
3. Nothing fits: write a voice description grounded in the NPC's canon page (accent,
   age, timbre — see `references/voice-design.md`), run `design` with a signature line
   from the page as `--text`. Surface the preview mp3 paths to the GM and **ask which
   preview wins — never auto-pick a paid voice**. Then `create`, and write both keys
   into the NPC page frontmatter: `voice_id` (the id) and `voice` (the description).
4. `say` with the page's `voice_id`, output to
   `_assets/dialogue/<page-slug>-<line-slug>.mp3`, flat — no session nesting even for a
   scene-specific line, e.g. Thunk's greeting on `vault/campaigns/shattered-sea/npcs/thunk.md` →
   `_assets/dialogue/thunk-dockside-greeting.mp3`; a session-scene line →
   `_assets/dialogue/session-06-scene-01-<line-slug>.mp3` (the session/scene lives in the
   filename, not a subfolder). The `<page-slug>-` prefix is load-bearing: the
   `audio-asset-linked` lint keys on it.
5. Embed the clip directly under the dialogue/read-aloud line in the page, using
   the same full vault-relative path as the output — `![[_assets/dialogue/<page-slug>-<line-slug>.mp3]]`
   (e.g. `![[_assets/dialogue/thunk-dockside-greeting.mp3]]`). A bare-filename
   embed (`![[<page-slug>-<line-slug>.mp3]]`) fails `OFM022` — this repo's
   markdownlint-obsidian resolves non-markdown embeds by literal vault-relative
   path, not by vault-wide filename search.
6. Lint before calling it done (`npm run lint -- <path>`) — an unembedded clip in
   `_assets/dialogue/` is a named lint finding.

Clips in `_assets/dialogue/` are committed (LFS-tracked, gitignore-excepted) — they are vault
content, unlike raw session recordings.

## Owned paths

- `_assets/dialogue/*.mp3`, flat, regardless of source (NPC dialogue and session-scene dialogue
  share the one folder)
- `voice_id` / `voice` frontmatter keys on NPC pages
- Never flips `status:` or `publish:`; the embed edit is asset-only.

## Degrade by asking

- No API key → point at `.env.local` + `.env.example`, stop.
- Quota exhausted (the CLI names it) → report, don't retry.
- GM hasn't picked a design preview → don't `create`, don't guess.
- The line isn't verbatim on a page → confirm exact wording with the GM before paying
  for generation.

## Out of scope

- Recording or transcribing table audio — `record-session-audio`.
- Any non-ElevenLabs TTS provider for NPC speech — voice consistency lives in the
  ElevenLabs account; a one-off clip from another provider breaks it.

## Reference files

| File | Read for |
|---|---|
| `references/voice-design.md` | Writing voice descriptions that design well; stability/similarity settings. |
