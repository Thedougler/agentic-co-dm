# Campaign OS combatant drops

Last mile from a **foreign drop** onto this vault. **Chassis-first.** **Derive-only.**

`writing-statblocks` is craft after an entity exists. This path mints the page.

## Catalog

Closed. Report anything else; leave it on the main ingest path.

1. 5etools creature JSON (object or array)
2. 5etools quote-statblock markdown
3. Markdown with a valid `statblock` fence, plus an optional same-stem image

## 1. Normalize

From `_system/scripts/`:

```bash
npm run normalize-combatants -- <paths>
```

Missing 5etools cache: add `--ensure-tools`. Needs `ttrpg-convert` on PATH.

Read every `_raw/_normalized/<slug>.md` this run wrote.

**Complete when** each being in the catalog paths has one intermediate, and unknown files are listed.

### Intermediate (`combatant@1`)

Staging, never Knowledge.

```yaml
normalize_schema: combatant@1
name: Blink Dog
slug: blink-dog
catalog: 5etools-json          # or quote-statblock | foreign-fence
source_abbrev: XMM             # null when the drop has no book
source_page: 46
is_named_creature: false
has_ecology: false             # true only when the drop has species prose
image: null                    # vault-relative sidecar, if any
original: _raw/_archived/...
```

**Stats** — a `statblock` fence, a 5etools `ad-statblock` fence (tags already expanded), or a quote-statblock. Transcribe the last two into the vault fence. Numbers come from the drop.

**Ecology** — species prose from the drop, or `Source is silent.`

**Notes** — leftovers that are not ecology. Environment tags are not ecology.

## 2. Mint the chassis

**Official-source branch.** If `sources/source-entry.<publication>.statblock.<slug>.md` exists, last-mile with `npm run source -- fork --entry source-entry.<publication>.statblock.<slug>`. That is the same fork as any other adoption. Do not invent a second import verb. If no source-entry exists yet, mint the chassis below and append it to the publication's `adopted:`.

**Homebrew / no book.** Instantiate `_system/schemas/statblock/template.md` as `rules/statblock.<slug>.md` directly (ADR-0009). No publication page.

- `canon: provisional`
- `subtype: monster` unless the drop is a named unique (`npc-combat`)
- `usage: adversary` unless the drop states otherwise
- `combat_role:` only if the actions make one or two roles obvious
- Unplaced chassis: `status: dormant`, empty `creatures:` / `npcs:`
- `sources:` → `[[source.<abbrev-lower>]]` when `source_abbrev` is a published book; otherwise the archived drop path
- `## Stats` — copy a `statblock` fence; transcribe `ad-statblock` or quote-statblock into the template fence (`layout: Basic 5e Layout`). Invoke `obsidian-fantasy-statblocks` for fence keys
- `## Tactics` — opener / pressure / pivot / exit derived from the actions that exist. Missing beats: `Source is silent.`
- Required headings with no source text: `Source is silent.`
- Named unique stays unplaced

If `image` is set and there is no creature page, move the file to `assets/creatures/<slug>.<ext>` and embed it under Notes: `![[assets/creatures/<slug>.<ext>]]`.

**Complete when** every intermediate has a `statblock@2` page and unplaced blocks are dormant with empty entity lists.

## 3. Mint a creature only when ecology exists

`has_ecology: true` only. Instantiate `_system/schemas/creature/template.md` as `world/creature.<slug>.md`.

Copy ecology prose into Overview / Ecology / Behavior / Habitat only where the drop states it. Remaining required headings: `Source is silent.` Tactics points at `[[statblock.<slug>]]`. Set `statblock.creatures:` to that page. Move `image` to `assets/creatures/<slug>.<ext>`, cite it in the creature's `reference_images:`, and embed it in Overview. The creature owns the identity file. The statblock may keep the same embed for the fight; it does not gain `reference_images`.

**Complete when** every ecology-bearing drop has a `creature@1` page, and no creature was minted from environment tags or a named unique.

## 4. Provenance

Published `source_abbrev`: mint or update `sources/source.<abbrev-lower>.md` from `_system/schemas/source/template.md`. `indexing_status: partial`. Human-set `ingest_policy` (default `blocked` until set). Append the new block to `adopted:` (not a typed `statblocks:` inventory).

Homebrew with no book: no source page. `sources:` on the statblock (and creature) is the archived drop.

**Complete when** every published abbreviation this run touched has a source page listing the new statblocks.

## 5. Archive and validate

Move each original drop that produced pages into `_raw/_archived/` (exact path, no globs). Move or delete its intermediates. Run `npm run doctor` from `_system/scripts/`. Repair errors this run introduced.

Then return to wiki-ingest Step 7 for `.manifest.json`, `log.md`, and `hot.md`.

**Complete when** those originals are not still in the live `_raw/` tree, doctor is clean for the new pages, and every claim on the new pages is in the drop.
