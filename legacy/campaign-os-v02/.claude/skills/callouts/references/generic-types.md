# Generic types — docs/meta pages only

**Role:** standard Obsidian callouts for the system's own documentation — `docs/`, `vault/refs/`,
vendored SRD/craft reference, guides, specs. On those pages the reader is a maintainer, not a DM mid-scene, so
the standard semantics apply unchanged.

Play pages (`vault/`, `vault/campaigns/shattered-sea/pcs/`, `vault/campaigns/`) never carry these (lint W23 warns) — every job a
generic type does there is a play type's job done worse. Two governed exceptions below.

## Semantics

| Type | Use for |
|---|---|
| `note` / `info` | A fact worth setting off from the flow |
| `tip` / `hint` | How-to advice, a shortcut |
| `warning` / `caution` | A pitfall — something that breaks if ignored |
| `important` | A constraint the reader must not miss |
| `summary` / `abstract` | A TL;DR at the top of a long doc |
| `example` | A worked example |
| `question` | An open issue awaiting a decision |
| `success` / `failure` | An outcome or verdict |
| `danger` | An irreversible action |
| `bug` | A known defect |
| `quote` | Cited text from a source |

Titles optional (`requireTitle: false`); lowercase always (W22).

## The one governed exception on play pages

Owned elsewhere — this file only points at it:

- `> [!warning] CONTRADICTION` — the canon conflict flag, short-lived by
  design. Format of record: `transcript-ingest`; resolution: `canon-review`
  (evidence-settled → fix the prose, delete the block — no RESOLVED
  callout, git log is the history).

## Found a generic type on a play page?

Convert it — the content is real, the container is wrong:

| Found on a play page | Convert to |
|---|---|
| `caution` / `warning` / `danger` wrapping a hazard or trap | `[!mechanic]` |
| `caution` / `important` / `note` wrapping a secret or handling note | plain prose (`[!dm]` is retired) |
| `important` wrapping an inline stat line | `[!mechanic]` |
| `success` / `failure` pair for roll outcomes | one `[!check]` with tiered lines |
| `tip` GM advice | plain prose |
| `quote` (lowercase, NPC speech) | `[!dialogue]` — `quote` is retired as a play type, docs/meta `quote` semantics are unaffected |

## CSS

No blocks — all generic types use Obsidian's theme built-ins.
