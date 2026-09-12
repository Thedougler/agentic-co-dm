# Data Model: Copy Foundry Config

## Development table

The already-running Foundry world used for this campaign's development.

| Field | Rule |
|---|---|
| host | From copied `mcp.json` `FOUNDRY_HOST` |
| port | From copied `mcp.json` `FOUNDRY_PORT` |
| data root | Target of `foundry-data` symlink (same as campaign of record) |

One instance. This repo does not create a world.

## Table connection settings

Local files, not wiki pages.

| Field | Rule |
|---|---|
| mcp.json | Copy of campaign-of-record Foundry MCP server entry |
| foundry-data | Symlink to the same Foundry Data directory |
| tracked | No. Gitignored |

Validation: after copy, an MCP list call against that host/port succeeds. Secrets never in git.

## Linked art asset

A media file a named ingest source already embeds or wikilinks.

| Field | Rule |
|---|---|
| basename | Exact filename including extension (`bloodhawk-of-aruhe-flight.jpg`) |
| source_vault | Campaign of record (`Documents/ai-co-dm`) |
| dest | `wiki/attachments/<basename>` |
| match | Exact basename only; first hit |
| missing | Report; no file written |
| dest exists | Skip; tell the DM |

Relationship: belongs to one named ingest source. Not a wiki entity page.

## Accepted prep

Unchanged from 001. `lifecycle: accepted` (and reveal rules) before `foundry-stage`. Connection settings do not weaken that gate.

## State

```text
connection: absent → copied (local, ignored) → reachable
art: linked-in-source → found | missing | dest-exists
found → copied to wiki/attachments/
missing → reported, no file
dest-exists → skipped, reported
```
