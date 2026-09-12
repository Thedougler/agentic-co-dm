# Research: Copy Foundry Config

## 1. Where table connection settings live

**Decision:** Copy `Documents/ai-co-dm/mcp.json` to this repo root as local `mcp.json`. Recreate `foundry-data` as a symlink to the same target as ai-co-dm (`~/Library/Application Support/FoundryVTT/Data`). Gitignore both.

**Rationale:** That `mcp.json` already talks to the running table (`FOUNDRY_HOST=localhost`, `FOUNDRY_PORT=31415`, `foundry-mcp` via the local `foundry-vtt-mcp` server). `foundry-stage` already assumes a `foundry-data/` symlink for asset placement. This repo has neither file today.

**Alternatives considered:** Re-type host/port from memory (violates spec). Point this repo at a new world (violates one-table). Commit the symlink to `Library/...` (machine path in git). Invent a second MCP schema for Oh My Pi (YAGNI — copy what already works).

## 2. Secrets

**Decision:** Treat `mcp.json` and `foundry-data` as machine-local. Gitignore them even though the current file has no password. If a token appears later it must not be committed.

**Rationale:** FR-004. `.env` is already ignored; same class of file.

**Alternatives considered:** Commit localhost-only mcp.json (fine until a token is added; ignore is cheaper). Put host/port in tracked `.env.example` only (optional later; not needed for v1).

## 3. Campaign of record path for art search

**Decision:** Search `Documents/ai-co-dm` as named in `CONTEXT.md`. Do not add a new config variable.

**Rationale:** One source of truth. The path never changes until cutover.

**Alternatives considered:** `CAMPAIGN_OF_RECORD_PATH` in `.env` (config for a value that does not change). Hardcode an absolute path in the skill (duplicates `CONTEXT.md`).

## 4. How to match linked art

**Decision:** Parse the named source (and the filed page) for Obsidian embeds `![[filename|...]]` and wikilinks to media extensions. Match **exact basename** (including extension) under the campaign of record. Copy the first exact file hit into `wiki/attachments/<basename>`. Do not recurse-copy directories. Do not generate images.

**Rationale:** Bloodhawk names `bloodhawk-of-aruhe-flight.jpg` and `bloodhawk-of-aruhe-token.jpg`; both exist under `Documents/ai-co-dm/attachments/shattered-sea/creatures/`. Exact basename avoids importing `young-bloodhawk-of-aruhe-flight.jpg` for `bloodhawk-of-aruhe-flight.jpg`. Putting files in `wiki/attachments/` lets `![[basename]]` resolve without rewriting embeds.

**Alternatives considered:** Fuzzy name search (wrong-file edge case in the spec). Keep campaign-relative paths (`attachments/shattered-sea/...`) in this vault (would require rewriting every embed). Symlink the whole ai-co-dm attachments tree (third copy / cutover risk; too much surface).

## 5. Overwrite and misses

**Decision:** If `wiki/attachments/<basename>` already exists, skip and tell the DM. If no exact file exists in the campaign of record, skip and list the name. Never write a placeholder image.

**Rationale:** FR-008, FR-009.

**Alternatives considered:** Always overwrite from campaign of record (destroys local edits). Generate a blank PNG so the embed is not red (invented art).

## 6. Staging still uses accepted Work

**Decision:** Do not change the `foundry-stage` accept-gate. Connection copy only makes the MCP reachable. Token copy into `foundry-data/assets/` stays inside existing recipes after accept.

**Rationale:** FR-005. 001 contract `foundry.md` already owns the gate.

**Alternatives considered:** Auto-stage Bloodhawk on ingest (unaccepted/unrevealed; refuse).
