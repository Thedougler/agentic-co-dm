---
name: find-item
description: A magic item's mechanics (rarity, attunement, its stat line) already exist in a real, licensed 5e sourcebook, in a Campaign OS repo (vault/ present) — vendor that source's page into vault/third-party/ rather than reinventing it. Use on "find a version of X item", "is there a published X", "vendor this item". Not a homebrew concept with no real-world analog (item GUIDE) or a bulk document ingest (llm-wiki-ingest).
---

# Find Item

Retrieves one already-published magic item at a time and vendors a
faithful local copy, so the same lookup never re-fetches every session.
Coexists with, never replaces, this vault's bulk SRD ingest
(`vault/srd/items/` — `llm-wiki-ingest`, document-level): this skill is
for a single item found on demand. Magic items appear in published
third-party OGL/ORC sourcebooks constantly — the same "worth vendoring on
demand" case `find-creature` already covers for monsters.

**This is fidelity work, not authoring.** Same discipline as
`find-creature`: faithful recreation of the source's mechanical content
only — never a lossy summary, never invented content filling a gap the
source leaves silent.

## Workflow

1. **Local-first, always.** Before any web call:

   ```bash
   grep -ril "<item name/concept>" vault/srd/items/ vault/third-party/ 2>/dev/null
   ```

   A hit ends the skill — hand that page back, never vendor a duplicate.
2. **Web search, license-restricted.** Search only for a source
   positively identifiable as OGL-1.0a, CC-BY-4.0, or ORC licensed —
   confirmed from the source itself, never assumed from a publisher's
   general reputation. Can't positively identify the license -> stop and
   hand back to `.claude/skills/draft-content/references/item.md` (homebrew authoring)
   instead of vendoring anything.
3. **Vendor exactly one page.** Target:
   `vault/third-party/<publisher>/items/<slug>.md`, instantiated from
   `vault/_templates/_srd/_item.md` — copy it, never retype from memory.
   Set `source:` (the sourcebook or document
   title), `source_url:`, and `license:` from the real source.
4. **Fidelity check before returning.** Every stat line, power, rarity,
   and attunement requirement matches the source exactly — reworded only
   where the source's own grammar needs normalizing to this vault's stat
   line format (`vault/refs/vault/item/references/srd-conventions.md` § Stat
   line format). A field the source leaves silent stays unfilled or
   `# OPTIONAL` per the template, never guessed.
5. **Hand back the path.** Report the vendored page's path to whatever
   drafting flow called this skill; it never proceeds to fill in
   narrative sections (the Item Toy table, `## Provenance`'s
   in-fiction ownership) — that's `.claude/skills/draft-content/references/item.md`'s job
   once the mechanical page exists.

## Owned paths

`vault/third-party/<publisher>/items/<slug>.md` only — create, never
overwrite an existing vendored page with a second source; a hit at step 1
ends the skill before this point. Never writes `vault/srd/items/` (bulk
ingest's tree) or a homebrew page.

## Degrade by asking

- No license can be positively confirmed -> stop and hand back to
  `.claude/skills/draft-content/references/item.md`, never vendor on a guess.
- Two sources conflict on the same item's stats -> ask which source to
  vendor, don't merge them.
- The local search returns a near-miss (same item, different edition or
  a variant rarity) -> ask whether it's close enough to reuse before
  vendoring a second page for the same item.
