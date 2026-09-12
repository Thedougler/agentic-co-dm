# Quickstart: Copy Foundry Config

Proves this project talks to the existing development table and that named ingest brings linked art. Campaign of record stays at `Documents/ai-co-dm`.

## Prerequisites

- Branch `002-copy-foundry-config`
- Foundry already running (same table the campaign of record uses)
- Host agent with `.agents/skills/` loaded

## Story 1 — Table

1. Copy `Documents/ai-co-dm/mcp.json` to this repo root. Recreate `foundry-data` as a symlink to the same target as `Documents/ai-co-dm/foundry-data`. Confirm both are gitignored.
2. From this project, call Foundry MCP enough to prove reach (list scenes or actors). Expect success against the existing table, not a new world.
3. Stage one `lifecycle: accepted` page via `foundry-stage`. Expect that wording on the table. Refuse a `proposed` or `rejected` page.

## Story 2 — Art

1. Name `wiki/_raw/Bloodhawk.md` (already ingested as `type: creature`) or re-run ingest on that file only.
2. Expect `wiki/attachments/bloodhawk-of-aruhe-flight.jpg` and `wiki/attachments/bloodhawk-of-aruhe-token.jpg` (exact names from the source). Embeds on `wiki/entities/Bloodhawk.md` open.
3. Confirm `wiki/_raw/Bloodhawk.md` is still in place. Confirm no `young-bloodhawk-*` file unless that source named it.
4. If a dest file already exists, expect skip + report, not overwrite.

## Pass

SC-001–004: same table, one sitting, no secrets in git. SC-005–006: linked art resolves or is listed missing; no invented images. Accept-gate still holds.
