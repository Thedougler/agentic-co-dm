---
name: player-characters
description: >-
  Record a player-created character onto a type: pc wiki page. Use when
  supplied source (PDF sheet, prose description, Foundry VTT actor, DM file)
  needs transcribing to a PC owner page. Refuse work that invents a PC,
  generates stats, or writes the player's actions.
---

# Player Characters

Record-only skill for `type: pc` wiki pages. Players create characters; this skill transcribes supplied source onto the canonical owner page. It does not invent PCs, generate stats, prescribe actions, or write voice.

## Work gate

Prep only. Follow `docs/agents/work.md`.

Show a chat proposal; write under `wiki/` only after DM accept. Structure-only conformance (reshaping an existing page without a newer source) does not require accept. New PC pages and source-driven overwrites are Work.

## State

| State | Trigger | Action |
| --- | --- | --- |
| idle | No PC job | Nothing |
| record | DM supplies source for a player-created character | Transcribe onto `wiki/entities/pc/<kebab-slug>.md` |
| refresh-goals | Post-session transcript for a player who was in that session | Refresh Stated Goals on the PC's live page from that transcript |
| refuse | No source supplied, or request to invent/generate/prescribe a PC, or inventing goals | Refuse and say why |

The skill enters `record` only when the DM supplies at least one source. It enters `refresh-goals` after a session that included the player, when the session transcript is available. A request without source is a `refuse`. A request to invent goals is a `refuse`.

## Accepted sources

- PDF character sheet (read with existing tools; no new PDF parser).
- Prose description or notes from the DM.
- Foundry VTT actor via the existing MCP server (`get-character`, `list-characters`, `get-character-entity`, and related character tools).
- Other DM-supplied file (image of a sheet, exported JSON, plain text).

When a source cannot be read (PDF garbled, Foundry MCP unavailable, image illegible), record what can be read and mark unread fields unknown or `[verify]`. Do not invent values. Do not abort a usable partial page when other source remains.

## Procedure

### 1. Retrieve

Read the supplied source. Read the live owner page at `wiki/entities/pc/<kebab-slug>.md` when it exists. Read `wiki/templates/pc.md` for the scaffold and `specs/020-pc-page-redesign/contracts/pc-page.md` for section contracts. Follow `wiki/AGENTS.md` for campaign frontmatter, entity path, and `type: pc` rules. Follow `obsidian-markdown` for syntax.

### 2. Transcribe

Copy `wiki/templates/pc.md` as the scaffold for a new page. For an existing page, reshape to match the template spine.

Fill every field the source provides. Leave fields the source does not cover as unknown or `[verify]`. Omit optional sections that have no content per the contract.

Narration is a real `[!narration]` callout with player-safe sensory description. No secrets, DCs, unearned names, or DM thesis.

#### Art placement

- **Pictures exist:** one featured portrait embed paired with `## Identity` in the col/col-md layout. Additional pictures MAY sit next to the section they illustrate. Leftover approved embeds go in `## Art`.
- **One picture only:** that picture is the featured portrait paired with Identity. Omit `## Art`.
- **No pictures:** `## Identity` renders full-width with no col fences and no empty portrait column. Omit `## Art`.

#### Stated Goals (refresh-goals)

After every session that included the player, refresh from that session's transcript:

1. Read the session transcript. A session summary MAY help locate or paraphrase a transcript-supported goal but MUST NOT be the sole source.
2. Add newly stated goals the player clearly stated in the transcript, in character or out of character. Cite the session.
3. Remove a goal only if the player said it is done or abandoned in the transcript.
4. Do not infer goals from play, connections, or DM thesis. A summary-only goal is not filed.
5. Sessions that did not include the player do not refresh this section.
6. Omit the section entirely when no transcript-supported goals exist.

### 3. Resolve conflicts

**Newer supplied source vs live wiki page:** When a newer supplied source disagrees with the live page on the same number, keep the newer source's value and overwrite the wiki number, including matching frontmatter mirrors. Structure-only conformance is not a newer source.

**Source disagrees with itself:** Keep both values or mark `[verify]`. Do not invent a resolution.

### 4. File

Set frontmatter per `wiki/AGENTS.md` and the contract:

```yaml
type: pc
lifecycle: proposed
reveal: revealed
campaign: <campaign slug>
visibility: dm
```

Fill PC identity frontmatter (`player`, `class_levels`, `level`, `ac`, `hp_max`, `init_mod`, `pp`, `speed`, `status`) from source. Preserve aliases, Foundry identity, provenance, tier, lifecycle dates, source list, and campaign state from the existing page.

File at `wiki/entities/pc/<kebab-slug>.md`. When `WIKI_STAGED_WRITES=true`, land under `wiki/_staging/pc/` instead.

## Boundaries

- MUST NOT invent a PC, generate stats, write the player's actions, or invent goals.
- MUST NOT use `npc-design` for `type: pc` work.
- MUST NOT add `Voice`, `At a Glance`, `Sheet`, `Combat Profile`, `Abilities`, or a DM thesis section.
- MUST NOT add a new PDF parser, database, or Foundry client.
- MUST NOT file a Stated Goal sourced only from a session summary without transcript support.

## Done

The page is done when:

- It lives at `wiki/entities/pc/<kebab-slug>.md` with `type: pc`.
- Every source-provided field is filled; every missing field is unknown or `[verify]`.
- The heading spine matches `specs/020-pc-page-redesign/contracts/pc-page.md`.
- Narration is player-safe with no secrets, DCs, or unearned names.
- Newer-source numbers overwrite stale wiki numbers and their frontmatter mirrors.
- No stats, actions, identity, or goals were invented.
- Art placement follows the art rules: featured portrait paired with Identity when pictures exist; one picture only means no Art section; no pictures means Identity full-width and no Art section.
- Stated Goals contains only transcript-supported player-stated goals with session citations, or the section is omitted.
