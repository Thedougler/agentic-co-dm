# Contract: Foundry connection

This repo reaches the same development table the campaign of record already uses.

## Copy

Precondition: campaign of record `mcp.json` exists and the table is running.

Done when:

- This repo has a local `mcp.json` with the same `foundry-mcp` command, args, and `FOUNDRY_*` env.
- `foundry-data` is a symlink to the same Foundry Data directory as `Documents/ai-co-dm/foundry-data`.
- Both paths are gitignored.

Invalid: a second world; committed secrets; inventing a new MCP schema.

## Reach

Precondition: copy done; table still running.

Done when: an MCP call from this project lists scenes or actors on that table (non-empty or empty list is fine; connection error is not).

## Stage

Unchanged: `specs/001-agentic-co-dm/contracts/foundry.md`. Refuse unaccepted pages. Wording matches accepted text.
