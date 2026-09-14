# Research: PC Page Redesign

## Decisions

### Canonical owner and source boundary

- Live PC owners remain `wiki/entities/pc/<kebab-slug>.md`; the sole copy-start scaffold is `wiki/templates/pc.md`. This follows `wiki/AGENTS.md` § Frontmatter, § Layout, and § Page filenames and matches all five live pages.
- The five conformance targets are `jean-claude-tabarnack.md`, `perrin-black-jaw.md`, `catarina-davirelli.md`, `crissdalynn-khinriss.md`, and `delmar-fisk.md`. Files under `wiki/_archive/{abilities,character-sheets,combat-profile,galleries,inventory,session-logs,spells,stats,va-scripts}` remain evidence, not competing owner pages.
- Conformance is structure-only. Existing facts, aliases, sources, lifecycle, reveal, visibility, art references, player handles, and links remain unchanged unless a source conflict is explicitly marked for verification. No campaign fact is silently selected or promoted.

### Page shape and scan surfaces

- Every filed page has one H1, leading `> [!narration] Narration`, and the shared Title Case spine: `At a Glance`, `Connections`, `Sheet`, `Combat Profile`, `Abilities`, conditional `Spells`, `Inventory`, conditional `Session Log`, and conditional `Art`. There is no `Voice` section: PCs are player-controlled, not DM-voiced.
- Pair `At a Glance` with `Connections`, and `Sheet` with `Combat Profile`, using the supported nested `col` / `col-md` codeblock syntax. Keep the narration callout outside fences. Put each heading inside its child column so the page remains readable when the columns plugin is unavailable.
- `Sheet` owns exact combat numbers and current state. `Combat Profile` owns interpretation, counters, dependencies, and party synergy; it points to the Sheet or named resource rows rather than retyping the same numeric value. Abilities own uses and recovery for actions and resources. This resolves the current duplicate combat-skims problem.
- Spells is conditional: omit it for a non-caster; when present, use `Spellcasting`, `Cantrips`, `Prepared or Known`, and `Slots or Casting Resources`, omitting empty subsections. Inventory similarly omits empty `Attuned`, `Carried`, `Stowed`, and `Currency` subsections.

### Player-control boundary

- Existing `Voice` prose is not preserved as a DM performance surface. Decision-relevant behavior moves into the existing DM thesis or a named `Connections` entry; mechanical constraints move into `Abilities`; player performance choices remain attributable in source evidence when they do not affect adjudication. No new section replaces `Voice`.

### Markdown and agent contract

- `wiki/AGENTS.md` remains the campaign authority for type, lifecycle, reveal, visibility, owner paths, approval, headings, and omission. `obsidian-markdown` owns syntax: wikilinks, escaped table-cell pipes, callouts, complete sentences, inline-code DCs/dice, real newlines, and columns.
- Because FR-010 explicitly requires codeblock columns for PC pages, add a narrow owner-page PC exception to the current columns guidance. It must not weaken the existing session/run rule: narration stays outside fences and headings/tables remain the semantic fallback.
- Update `pc-interview` from the retired `templates/PC.md` and `wiki/<campaign>/pcs/` paths to the canonical template/path and map stated answers only into existing PC sections. An interview transcript is evidence; it is not an extra live PC facet or required heading.
- Update `wiki-ingest` and reconciliation pointers to name the PC template, owner path, satellite-flattening rule, and conflict/unknown handling. Do not duplicate the full page contract in each skill.
- The `obsidian-markdown` frontmatter type list must include `pc`, matching `wiki/AGENTS.md` and the lint implementation.

### Conflicts, unknowns, and preservation

- Existing sources contain real conflicts, including Crissdalynn's AC/HP/speed, Jean-Claude's HP/initiative, Perrin's AC/player handle, and Catarina's historical source density. Preserve the current owner value and attach a concise verification marker naming the conflicting source; do not invent a resolution.
- Missing owner links remain explicit unresolved links or stated unknowns under existing wiki rules. Named item, spell, place, faction, and party pages are linked when present; their full descriptions are not copied.
- Optional trust/provenance fields already present on a page are preserved. The redesign does not normalize lifecycle, confidence, tier, or source lineage as a side effect.

### Verification

- The public seam is the markdown owner-page contract, not an API. Use the feature contract plus a small feature-local fixture checker only for observable invariants; do not add AST or column-parser infrastructure.
- Run scoped `./scripts/lint-wiki-write --path wiki/entities/pc`, strict scoped Markdown lint, and `./scripts/wiki-lint --json` after implementation. Use a five-page timed reference review and a source-to-owner fact-preservation comparison for outcomes that lint cannot prove.
- `tools/check_wiki_pages.py` is not PC proof because its type set omits `pc`. `context-waste-scan.py` is diagnostic only; it must not score or delete narrative/mechanics.

## Alternatives considered

- **Keep the old split satellite model:** rejected because current `wiki/AGENTS.md` requires one owner page, and multi-H1/facet dumps and Foundry copies are documented structural context waste.
- **Use `[!col]` callouts:** rejected for this feature because FR-010 pins codeblock syntax and codeblocks preserve a real narration callout beside scan surfaces.
- **Add a PC-specific campaign `type` or folder taxonomy:** rejected because `pc` and `wiki/entities/pc/` already exist and shared type/path rules forbid duplicate taxonomies.
- **Copy full sheet, spell, and item text into multiple sections:** rejected because each fact needs one owner; pages should link to named owners and keep one canonical numeric home.
- **Resolve conflicting source values during conformance:** rejected because structure-only work cannot change campaign facts; unresolved values need explicit verification markers.
