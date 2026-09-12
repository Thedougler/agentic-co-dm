# Campaign-OS

An AI co-DM LLM-wiki, browsable locally in Obsidian, powered by Claude Code.

## Overview

Campaign-OS is composed of multiple interwoven agent systems and loops built
on a stateless [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern — a self-healing, self-organizing, additive knowledge base for
tracking a campaign over the long term. The GitHub repo **is** the Obsidian
vault: one file tree, no second database. Users interact with it through
manually invoked skills; an autonomous loop maintains the wiki itself.

For the full directory map — skills, agents, templates, hooks, linter,
guardrails — see [index.md](index.md). For current campaign state, see
[hot.md](hot.md). For the full system architecture, see the `campaign-os`
skill (`.claude/skills/campaign-os/SKILL.md`).

## Goals

Campaign-OS is a prescriptive system, not a one-off toolkit — the aim is a
fully general co-DM pattern any long-running tabletop campaign can run:

- **Compile, don't retrieve.** Knowledge is distilled once into maintained
  wiki pages and kept current, never re-derived from raw transcripts or
  recalled from chat memory. This holds however large the campaign grows.
- **A complete, mostly-autonomous session loop.** Prep, run, capture, ingest
  (writes canon directly — a transcript is recorded play), recap, and publish
  should each require only the human checkpoints the system explicitly gates
  on — never manual bookkeeping to keep canon straight.
- **Canon integrity over time.** The wiki stays internally consistent and
  contradiction-free across an indefinitely long campaign, with drift caught
  and surfaced rather than silently compounding.
- **Default-deny, leak-safe publishing.** The player-facing site always
  reflects only what the table has actually learned, kept in sync
  automatically as canon changes.
- **Portability beyond this campaign.** The pattern, skills, and guardrails
  should generalize to any GM's campaign, not stay bound to this one's
  specific setting or history.
- **Proven, not assumed.** Every mechanism here is validated against a real,
  ongoing campaign at the table before it's trusted — the campaign is the
  test suite.

## Setup

1. **Secrets** — copy `.env.example` → `.env.local` (gitignored) and fill in
   only the API keys you use. An absent `.env.local` is fine; scripts
   auto-detect the repo root, so `CAMPAIGN_ROOT` is an optional override.
2. **Config** — edit `CONFIG.md` (or copy `CONFIG.example.md` over it): your
   name, and turn on only the optional subsystems you've set up.
3. **Audio** (only for `record-session-audio`) — device/mic settings live in
   `utils/tools/audio/config.yaml`.

`CONFIG.md` is the map to all three surfaces.

## Development

This GitHub repo is the current development of Campaign-OS, being validated against real campaign(s).

SUPER EARLY DEVELOPMENT. EXPECT REGULAR BREAKING CHANGES.

- Many skills "work," but generated prose and content are still being actively improved.
- Repo organizational structure not yet finalized.
- Total system(s) not yet finalized.
- Nothing is sacred.
