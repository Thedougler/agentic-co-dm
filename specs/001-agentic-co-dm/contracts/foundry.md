# Contract: Foundry play surface

Foundry shows accepted Work. The Co-DM does not run during the session and does not push drafts.

## Stage (prep only)

Precondition: source wiki page `lifecycle: accepted`. If `reveal: unrevealed`, do not stage player-visible text until the DM accepts a reveal.

Implementation: existing MCP tools in `foundry-stage` (check → stage → wire). Token art → `foundry-token`. Maps → `foundry-battlemap`.

Done when:

- Foundry entity exists and traces to the wiki page.
- Wording matches accepted text, not drafts or rejected proposals.
- An update of accepted Work replaces mixed draft text.

## Refuse

Refuse to stage `draft`, `proposed`, or `rejected` pages. Report which gate failed.

## Session

No Co-DM. No auto-present. The table waits on the DM.
