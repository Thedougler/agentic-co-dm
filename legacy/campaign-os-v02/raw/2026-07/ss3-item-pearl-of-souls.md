# Source ingest queue: ss3-item-pearl-of-souls

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/items/artifact/pearl-of-souls.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md § Round 3 — `item-artifact :: entities/items/artifact/pearl-of-souls.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:63 "REVIEWED-BY-HUMAN: 2026-07-13 — same user instruction; blessing covers exactly the 14 lines below." (line 69 names this file.)
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/items/artifact/pearl-of-souls.md — triage: entity-source, RESOLVED (enum patched ebb0e41, written)
- [x] entities/items/artifact/pearl-of-souls-dm.md — triage: DM companion of the item above, not a separate claim — folded into `world/items/pearl-of-souls.md`'s DM Only section

## Claims — entities/items/artifact/pearl-of-souls.md

- [x] item :: Pearl of Souls :: world/items/pearl-of-souls.md (new) — WRITTEN, lint clean. DM companion folded in. See Resolution below.

## Verdict (original probe): BLOCKED — genuine enum gap, no shoehorn

Source frontmatter (pearl-of-souls.md:17-18):

```yaml
item_type: artifact
rarity: artifact
```

This is rung 3(b), not 3(a): the source does not merely gesture at
above-legendary power that could be rounded down to `legendary` — it
explicitly declares `rarity: artifact` in its own governed-looking frontmatter
key. wiki-contract.md's item schema enum is:

```text
world/wiki-contract.md:34: - `item`: `rarity: common | uncommon | rare | very rare | legendary`,
```

Writing `rarity: legendary` for this item would silently discard the source's
actual claim (this is meant to be D&D 5e's above-legendary "artifact" tier —
a divine instrument of a deity that passively and continuously harvests
souls, sank five ships' worth of crews as retaliation for its theft — not a
merely-legendary magic item). That is exactly the shoehorn this test is
checking for. Per rails item 3(b): STOPPING BLOCKED before writing any
world/ page. No `world/items/pearl-of-souls.md` was created.

### Artifact-tier file count in source

```console
ls ~/ai-os/shattered-sea/wiki/entities/items/artifact/
  pearl-of-souls-dm.md   (DM companion page for this item — not a separate item)
  pearl-of-souls.md      (the item itself)
```

**1** artifact-tier item exists in the source repo's `items/artifact/`
directory. (The DM companion file is a linked ancillary page, not a second
item entity — it would fold into this same page's DM Only section once the
enum gap is resolved, not become its own claim.)

### Exact enum diff needed (for the orchestrator; this agent does not patch this)

`docs/campaign/wiki-contract.md`? — **not found at that path.** The
governed copy actually lives at
`.claude/skills/campaign-os/references/wiki-contract.md:34`:

```text
- `item`: `rarity: common | uncommon | rare | very rare | legendary`,
```

→ append `| artifact`.

### Recommendation

Add `artifact` as the sixth enum member at the location above. D&D 5e
RAW already treats "artifact" as a rarity tier strictly above legendary (DMG),
so this is a real, recurring rarity in 5e-based content, not a one-off
homebrew label — a plausible future ingest wave will hit it again. This is a
recommendation only; per rails item 7 this agent does not edit
wiki-contract.md itself. Once patched, re-run this queue
line: claim becomes ready, `rarity: artifact` carries through unchanged (same
pattern as the ss2-item-fish-broth.md precedent for already-conformant
enum values), and the item skeleton can be filled from this same source read.

## Flags

1. **BLOCKED — enum gap, not a mechanics gap.** This is not "source too thin
   to fill a field" (Hard Rule 1's usual stub case) — it's the frontmatter's
   own declared rarity falling outside the governed enum entirely. No stub
   note substitutes for a value the schema doesn't accept at all.

2. **Withheld links (would apply once unblocked).** Source body links
   [[delmar-fisk]] (no page — relink), [[umberlee]] (no page — relink),
   [[waveservants]] (exists, on the round-3 real-link allowlist — would be a
   real wikilink), [[world/ships/red-lady|red-lady]] (no page — relink), [[the-drowned-maw]] (no
   page — relink). Not acted on: no page was written to carry them.
   - relink: delmar-fisk — once its page lands
   - relink: umberlee — once its page lands
   - relink: red-lady — once its page lands
   - relink: the-drowned-maw — once its page lands

3. **dm_companion pointer (would apply once unblocked).** Source frontmatter
   `dm_companion: "[[pearl-of-souls-dm|Pearl of Souls (DM)]]"` — the DM
   companion content (pearl-of-souls-dm.md) was not read/decomposed since the
   parent item claim never landed; would fold into the item page's DM Only
   section on a future unblocked pass.

4. **No world/ write, no lint run.** Per rails item 3(b), "queue
   file + gap report committed alone in that case."

## Resolution — 2026-07-13, post enum patch (commit ebb0e41)

Enum gap closed: `rarity: artifact` added to `wiki-contract.md`'s governed
enum (verified it now reads `... | legendary | artifact`
before this write). `world/items/pearl-of-souls.md` written from the item
skeleton, `rarity: artifact` carried through unchanged from source
frontmatter, exactly per the original probe's recommendation.

**DM companion fold.** `pearl-of-souls-dm.md` (audience: dm, publish: false)
read and decomposed into the new page's `## DM Only` section: Seven Pearls
context, precise current-location geography (Shelfworks, planar boundary),
the captains-pressed-into-Fisk secret, the Maw Entanglement mechanic, and the
Aldric Risk / Tessarine Concordat containment plot. One entity, one page —
no second claim line was created for the `-dm` file. Compared line-by-line
against the public page for conflicts: **no contradiction found** — the DM
file only adds detail (it never restates a fact differently). No
CONTRADICTION block was needed on the page.

**Status — rung 2 (actual play).** Neither source file carries an unrevealed
marker (rung 1 doesn't fire). Checked `sessions/` in the *source* repo
(project rule 10 substitute, since the live campaign-os `sessions/` is still
empty during migration):

- `sessions/session-01-scene-03-delmar.md:27` (`type: session`, `status:
  complete`) — "You went in clean, lifted the [[pearl-of-souls|Pearl]], and
  made the outbound tide."
- `sessions/session-04.md:26-27,69` (`type: session`, `status: complete`) —
  "They stole the [[pearl-of-souls|Pearl of Souls]] from a shrine... the Maw
  destroyed the fleet hours later" / "Pearl of Souls — Delmar confirmed:
  stolen from Vafnar shrine, fell into Maw with fleet wreckage."

Both are completed session logs naming the Pearl directly (not conditional
framing) → rung 2 fires cleanly, `status: canon`. Did not fall back to rung 3
(pearl-of-souls.md's own `audience: players`/`publish: true` frontmatter
would have landed the same `canon` outcome anyway, for what it's worth).

**Real links vs. relink flags.** Stub-checked every entity either source
file names, by filename (not substring — several entities are mentioned in
*other* pages' prose without having their own page, which would have been a
false positive): only `waveservants` has a dedicated page
(`world/factions/waveservants.md`) → kept as the one real `[[wikilink]]`.
Everything else — `umberlee`, `delmar-fisk`, `red-lady`, `the-drowned-maw`,
`auralis`, `tessarine-concordat`, `aldric-drave`, `hierarch`, `chain-council`
— has no dedicated page yet → plain text + inline `relink:` flag at first
mention, matching the `ss3-item-delmars-cloak` precedent's inline-flag style.
`maw-pearl-crisis` (a situation, mentioned only in the DM file's Connections
list) was folded as prose context, not carried as its own relink target — no
prose elsewhere on the new page names it.

**Tags.** Source `tags: [umberlee]` is an entity-identity tag — dropped by
design (WIKI.md § Tag taxonomy migrated-tags rule), not mapped. Checked for a
genuine tonal signal instead: the Player-Known section's closing line ("It
does not stop doing this.") is a direct match for WIKI.md's own worked
example ("combat→horror on a page with a horror closing line") → tagged
`horror`, one tag, no others forced.

**Dropped legacy frontmatter fields** (neither is part of `wiki-contract.md`'s
item schema, so neither carried into the new page): `item_type: artifact`
(redundant with `rarity: artifact`), `dm_companion:`/`public_profile:`
cross-reference fields (superseded — both sources are now one page),
`sources: [Homebrew]` / `sources: [Inbox/situations/reference/...]`,
`confidence_level: high` / `confidence_level: medium`, `homebrew: false`.

**Friction — Vel Orn vs. Vafnar (not acted on).** `session-01-scene-03-delmar.md:27`
names the shrine's location as "a shrine on [[world/locations/vel-orn|Vel Orn]]";
`session-04.md:26` names it "a shrine in [[world/locations/sunken-crown|Vafnar]]". This is a
discrepancy *between two session files in the source repo*, not between this
claim's two named sources (`pearl-of-souls.md` and `pearl-of-souls-dm.md`,
both of which leave the shrine's location unspecified) — outside this
claim's write scope, so no CONTRADICTION block was added to the new page for
it. Flagging for the orchestrator/DM in case it needs its own resolution pass
(the source repo's own `discrepancy-log.md` may already track it — not
checked, out of scope for this agent's read-only source access).

**Not touched, on purpose:** `world/factions/waveservants.md` is
`status: canon`. The skill's writeback step 3 calls for reciprocal wikilinks
on durable relationships, which would normally mean adding a pearl-of-souls
backlink there — but rails item 7 ("NEVER: edit MIGRATION-LEDGER.md or canon
pages") and project rule 2 both forbid editing canon pages outside
CANONIZE. No reciprocal link was added; noted here instead of silently
skipped.
