# Contract: Wiki pages

The wiki is markdown in `wiki/`. Humans read it. Agents retrieve from it.

## Write

Precondition: the DM approved a proposal, or named these sources for ingest (FR-019).

Every write loads `obsidian-markdown` and `copy-writer`.

Done when:

- Required frontmatter is present (`title`, `category`, `tags`, `sources`, `created`, `updated`).
- Campaign pages also have `type`, `lifecycle`, `reveal`.
- Body is complete sentences a DM can read without decoding agent shorthand. Stubs MAY be short.
- Related pages are `[[wikilinked]]`.
- Provenance: extracted claims cite sources; invented Work is marked; no fake wiki facts.
- Named ingest writes distilled source pages plus thin stubs only for names in those sources.
- `index.md`, `log.md`, `.manifest.json`, `hot.md` updated on ingest (llm-wiki rules).
- New place / item / hazard / creature pages copy the matching file in `wiki/templates/`. Creature pages are linear (no `col` wrappers).
- Early-dev `_raw/` sample ingest keeps that file's section order, markdown, callouts, tables, and embeds.

Invalid: telegram stubs, AI shorthand, silent canon edits, uningested module memory cited as lore, `[!secret]` / extra callouts when `[!narration]` is the spoken slot, a campaign page the DM did not approve, a page for a name the approved sources do not contain, a creature note wrapped in `col` fences, a place/item/creature page that ignores its template headings.

## Read

`wiki-query` (and craft skills) retrieve from pages, not unaudited chat memory.

Done when: the answer names the page(s) used, or the gap is filled as marked invention grounded in wiki pages and/or D&D 5e rules.

## Conflict

If a source or outcome contradicts a page, show the DM. Do not overwrite.
