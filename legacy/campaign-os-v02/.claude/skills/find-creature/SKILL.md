---
name: find-creature
description: Before statting a creature from scratch in a Campaign OS repo (vault/ present), check whether a licensed 5e sourcebook already has one and pull that page into vault/third-party/ instead. Use on "find a statblock for X", "is there a published version of X", "vendor this creature". Skip this for a fully homebrew concept (monster GUIDE) or a bulk ingest (llm-wiki-ingest).
---

# Find Creature

Retrieves one already-published creature at a time and vendors a faithful
local copy, so the same lookup never re-fetches every session. Coexists
with, never replaces, this vault's bulk SRD ingest
(`vault/srd/monsters/` — `llm-wiki-ingest`, document-level): this skill is
for a single creature found on demand.

**This is fidelity work, not authoring.** Same discipline as
`find-guidelines`: faithful recreation of the source's mechanical content
only — never a lossy summary, never invented content filling a gap the
source leaves silent.

## Workflow

1. **Local-first, always.** Before any web call:

   ```bash
   grep -ril "<creature name/concept>" vault/srd/monsters/ vault/third-party/ 2>/dev/null
   ```

   A hit ends the skill — hand that page back, never vendor a duplicate.
2. **Web search, license-restricted.** Search only for a source
   positively identifiable as OGL-1.0a, CC-BY-4.0, or ORC licensed —
   confirmed from the source itself, never assumed from a publisher's
   general reputation. Can't positively identify the license -> stop and
   hand back to `.claude/skills/draft-content/references/monster.md` (homebrew authoring)
   instead of vendoring anything.
3. **Vendor exactly one page.** Target:
   `vault/third-party/<publisher>/monsters/<slug>.md`, instantiated from
   `vault/_templates/_srd/_monster.md` — copy it, never retype from
   memory. Set `source:` (the sourcebook or
   document title), `source_url:`, and `license:` from the real source.
4. **Fidelity check before returning.** Every stat, trait, and action
   matches the source exactly — reworded only where the source's own
   grammar needs normalizing to the codeblock format
   (`vault/refs/vault/monster/references/statblock-format.md`). A field the
   source leaves silent stays unfilled or `# OPTIONAL` per the template,
   never guessed.
5. **Hand back the path.** Report the vendored page's path to whatever
   drafting flow called this skill; it never proceeds to fill in
   narrative sections (`## Description`, `## Ecology`, `## Toy Chest`) —
   that's `.claude/skills/draft-content/references/monster.md`'s job once the mechanical page exists.

## Owned paths

`vault/third-party/<publisher>/monsters/<slug>.md` only — create, never
overwrite an existing vendored page with a second source; a hit at step 1
ends the skill before this point. Never writes `vault/srd/monsters/`
(bulk ingest's tree) or a homebrew page.

## Degrade by asking

- No license can be positively confirmed -> stop and hand back to
  `.claude/skills/draft-content/references/monster.md`, never vendor on a guess.
- Two sources conflict on the same creature's stats -> ask which source
  to vendor, don't merge them.
- The local search returns a near-miss (same creature, different edition
  or CR) -> ask whether it's close enough to reuse before vendoring a
  second page for the same creature.
