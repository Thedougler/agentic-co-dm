---
type: system
dm_name: Nick
feature_npc_voice: true
feature_record_session_audio: true
feature_battlemap_render: false
---

# CONFIG.md — operator config

*Installation-level setup: who's running this Claude Code checkout and which
optional subsystems are turned on. Not campaign data — campaign-os runs
multiple campaigns (only Shattered Sea is live so far); each campaign's own
identity lives on its `vault/campaigns/<slug>/campaign-overview.md` page,
never here. No secrets here either — this file is committed; secrets go in
`.env.local`.*

## Optional subsystems

Turn a subsystem off (`false`) if you haven't provisioned it — the owning
skill checks its toggle first and stops with a pointer back here instead of
failing mid-task.

| Toggle | Subsystem | Needs | Setup lives in |
|---|---|---|---|
| `feature_npc_voice` | npc-voice (NPC dialogue audio) | `ELEVENLABS_API_KEY` | `.env.local`; `cd vault/campaigns/.claude/skills/npc-voice/scripts && npm install` |
| `feature_record_session_audio` | record-session-audio (table capture) | `shattered-audio` install, mics, `HF_TOKEN` | `utils/tools/audio/` install; `utils/tools/audio/config.yaml` |
| `feature_battlemap_render` | battlemap-render (tactical maps) | Replicate image access (`use-replicate`) | `.env.local`/`.env`; `cd vault/campaigns/.claude/skills/battlemap-render/scripts && npm install` |

## Where configuration lives

- **Secrets and machine paths** → `.env.local` (template: `.env.example`).
  API keys, plus the optional `CAMPAIGN_ROOT` repo-root override.
- **Audio hardware** → `utils/tools/audio/config.yaml` — CoreAudio devices,
  mic list, speaker→character redaction map. Owned by the audio toolchain,
  not mirrored here.
