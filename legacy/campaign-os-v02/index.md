# Index

Map of the wiki's folder structure, not a catalog of individual pages. Do not list files here — this repo's wiki is too large for a per-file index to stay lean. Point an agent at the right directory; let it find the specific page itself.

## Canon status

Not everything under `vault/campaigns/shattered-sea/` is settled fact. Frontmatter `status:` is `canon` (played at the table, additive-only), `pending` (not yet played, edit freely), or `srd` (imported reference material). Never cite a `pending` page as an established fact. See `vault/CLAUDE.md`.

## `vault/campaigns/shattered-sea/` — the active campaign

- **State files** — `threads.md` (active narrative pressure map), `spoilers.md` (DM-only secrets — never read without DM direction), `hooks.md` (per-player gravity — DM-curated), `party-items.md` (party-wide inventory index)
- `npcs/` — 129 pages, flat (no subfolders) despite being the densest folder in the campaign; check here before assuming a named character is new
- `monsters/` — 37 pages of custom/reskinned statblocks; check here before `vault/srd/monsters/`
- `vehicles/` — 29 pages, mostly ships
- `locations/` — 23 top-level region/standalone pages; 7 of those (`sunken-crown`, `verdant-teeth`, `calders-tooth`, `crown-islands`, `midchain`, `midchain-south`, `the-drowned-maw`) also have a same-named subfolder of individual sub-locations — 199 pages total recursively
- `lore/` — 22 pages, setting history and cosmology specific to this campaign
- `factions/` — 19 pages, each tracks a Front/clock (see the `world-update` skill)
- `quests/` — 11 pages
- `species/` — 8 pages, campaign-specific species variants; check here before `vault/srd/species/` (also 8 pages, unrelated stock SRD species)
- `pcs/` — 5 main character sheets (plus its own `CLAUDE.md`, canon authority for that subtree), each with matching entries across 11 category subfolders (`abilities/`, `character-sheets/`, `combat-profile/`, `inventory/`, `spells/`, `stats/`, `galleries/`, `interviews/`, `session-logs/`, `va-scripts/`, and `players/` for the 6 human players) — 57 pages total
- `items/` — 38 pages sorted into rarity subfolders: `common`, `uncommon`, `rare`, `very-rare`, `artifact`
- `dashboards/` — 12 Obsidian Bases (`.base`) files, not markdown pages — `npcs`, `pcs`, `factions`, `locations`, `monsters`, `quests`, `sessions`, `ships`, `items`, `party-combat`, `prep-queue`, `shop-inventory`
- `encounters/` — 2 pages
- `events/` — 1 page
- `handouts/`, `puzzles/`, `seasons/` — genuinely empty (just `.gitkeep`); a request touching these is drafting new content, not looking something up

## `vault/episodes/NNN/` — per-session prep and history

Sessions 001-008 so far, one numbered folder each; 008 is the most recently played, 009 is in prep. Typical contents: `eNN-overview.md`, `eNN-run-guide-<slug>.md`, `sNN-recap.md`, `sNN-highlights.md`, `transcript.md`, `speakers.yaml`, `world-turn-*.md`, `beat-*.md`, and `prose/` for session-local narration/dialogue. Played folders may still use a bare `run-guide.md` or `eNN-index.md`.

## `vault/stories/` — non-session narrative drafts (arc, quest, season, campaign)

Session stories live in their episode folder (`vault/episodes/NNN/session-NN-*.md`). Non-session scopes (arc, quest, season, campaign) remain here. A run guide or Beat page must never be written before its session story exists (W47).

## `vault/worlds/` — setting-level material above the single campaign

Empty until a second campaign needs shared setting material split out.

## `vault/srd/` — 5e SRD reference, not campaign canon

- `items/` — 472 pages by rarity: `mundane`, `common`, `uncommon`, `rare`, `very-rare`, `legendary`, `artifact`
- `spells/` — 346 pages by school: `abjuration`, `conjuration`, `divination`, `enchantment`, `evocation`, `illusion`, `necromancy`, `transmutation`
- `monsters/` — 336 pages, `rules/` — 184 pages
- `classes/` — 13 base classes, a warlock-eldritch-invocations page, plus `subclasses/` (6 pages)
- `feats/` — 17, `species/` — 8, `backgrounds/` — 4, `lore/` — 2
- 4 core entry pages named in `vault/CLAUDE.md`: `character-creation`, `monsters-overview`, `spells-overview`, `rules-glossary`

## `vault/refs/` — craft and process docs, not campaign content

- `craft/` — 78 pages, prose/writing-craft references
- `draft/` — 70 pages, drafting guides per content type
- `tables/` — 28 random/lookup tables
- `runbooks/` — 21 operational how-tos; see `runbooks/commands.md` for the full command index
- `stories-playbook/` — 15 pages
- `subagents/` — 12 wiki-page write-ups of individual agents (human/LLM-readable reference); the actual runnable specs the Agent tool reads are `.claude/agents/`
- `qc-profiles/` — 10 quality-check profiles, named from `content-quality-checker`
- `lint/` — 8 pages documenting individual lint rules

## `vault/ideas/` — 14 unresolved concept pages

Plus `writers-room/`, dated arc-pitch subfolders from `campaign-writers-room` sessions.

## `vault/dashboards/` — Obsidian Bases dashboards

`.base` query files (craft, classes, backgrounds, lore, feats, species, spells, rules) plus `wiki-hub.md`, the vault's human entry point.

## Beyond `vault/` — the rest of the repo

- `docs/guardrails/` — 14 pages, the routing CLAUDE.md playbooks: `WIKI`, `CODE`, `CONTENT`, `STORY`, `DEBUG`, `VERIFY`, `EFFICIENCY`, `PLAN`, `IDEA`, `LINT`, `PROJECT`, `TRAPS`, plus `MIGRATION-LOG` and `_FORMAT`
- `docs/adr/` — 36 architecture decision records for campaign-os itself; no index file, so a targeted search beats reading all 36
- `docs/vale-styles/` — 10 prose-linter rule sets: `CampaignOS`, `CampaignDiegesis`, `CampaignLiterary`, `CampaignAward`, `AgentGuidance`, `Readability`, `ai-tells`, `ai-tells-commits`, `write-good`, `proselint`, plus shared `config/`
- `docs/exemplars/` — ~15 vendored published-adventure excerpts (PDF+md pairs: PointyHat, GiffyGlyph, etc.), craft/prose gold standards, not campaign content
- `docs/rulings/` — currently empty, reserved for DM rulings
- `_templates/` — 90 page templates plus 1 in `_templates/_plugins/` (`_leaflet.md`); every new vault page starts from one of these, never hand-rolled. `_`-prefixed files (`_campaign`, `_location`, `_item`, `_event`, `_organization`, `_legend`, `_character_basic/_advanced`, `_session_prep`) are shared base templates other templates compose from, not page types themselves
- `raw/` — immutable raw sources, one dated folder per month (`2026-07/`, `2026-08/`); `raw/INGESTED.tsv` tracks what's already been processed
- `inbox/` — unprocessed drop zone; anything still here needs `npm run inbox:to-md` or manual triage
- `utils/wiki-cli/` — the lint engine of record (`npm run lint`, ADR-0064), rules under `src/wiki_cli/rules/`; `utils/site/` — the Quartz publish build
- `utils/dndsim/` — the combat simulator (`npm run dndsim`)
- `_assets/` — media referenced by vault pages, by kind: `maps`, `battlemaps`, `portraits`, `character-sheets`, `scene-art`, `banners`, `dialogue`, `layouts`, `reference`, `misc`
- `.claude/skills/` — 69 skills, `.claude/agents/` — 15 subagent specs; see `.claude/CLAUDE.md`
- `.claude/rules/` — 4 project-level rules: `docs.md`, `external-guides.md`, `scripts.md`, `skills.md`
- Too many skills to browse blindly: session prep and play content start at `composing-beats` (ADR-0060); a single page type routes through `draft-content`
- 10 `obsidian-*` skills cover vault-app mechanics specifically (bases, canvas, leaflet maps, metabind, fantasy-statblocks, etc.) — separate from wiki-content skills

## Root-level docs

- `CLAUDE.md` — this repo's routing table and iron rules, loaded automatically every session
- `CONTEXT.md` — the engineering-domain definition (session pipeline, skills/hooks/linters); campaign terminology lives in `vault/srd/rules/rules-glossary.md` + `docs/rulings/` instead
- `CONFIG.md` — DM name and feature-flag frontmatter (`feature_npc_voice`, `feature_record_session_audio`, `feature_battlemap_render`, etc.)
- `README.md` — human-facing overview of the co-DM system
- `FEATURES.md` — planned-feature backlog checklist

Keep this file at this altitude only. Never grow it into a page-by-page listing.

**Max 100 lines.** At the cap, consolidate or drop entries before adding a new one — never exceed it.

Per the gist: a plain index file "works surprisingly well at moderate scale (~100 sources, ~hundreds of pages)... at small scale the index file is enough, but as the wiki grows you want proper search" — `vault/` alone holds 2,300+ pages, well past that, which is exactly why this file stays structural. For a specific page, chain-load the `llm-wiki-query` skill instead of guessing.
