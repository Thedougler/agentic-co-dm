# Data Model: Agentic Co-DM

All entities are markdown in `wiki/` unless noted. Fields are YAML frontmatter. Bodies are human prose.

## Campaign

One D&D 5e campaign, one table, v1.

| Field | Rule |
|---|---|
| slug | Folder or tag identifying the campaign |
| status | candidate in this repo until cutover; live campaign is ai-co-dm |

## Source

Raw ingest input. Immutable. Tracked in `wiki/.manifest.json`.

| Field | Rule |
|---|---|
| path | Canonical absolute path |
| ingested_at | ISO timestamp |
| pages_created / pages_updated | Vault-relative paths |

## Wiki page

Compiled, citable unit. The DM opens it. The Co-DM cites it.

| Field | Rule |
|---|---|
| title | Human name |
| category | llm-wiki category (`entities`, `concepts`, …) |
| type | Campaign type (`npc`, `place`, `faction`, `item`, `creature`, `session`, `recap`, `work`, …) |
| tags | Includes `visibility/` when needed |
| sources | Trace to Source paths |
| lifecycle | `draft` \| `proposed` \| `accepted` \| `rejected` \| `canon` |
| reveal | `unrevealed` \| `revealed` |
| created / updated | ISO timestamps |
| summary | ≤200 chars, ordinary language |

**Validation**

- Body is complete sentences. Telegram / AI shorthand is invalid (FR-018).
- A new or changed campaign page requires a prior DM-approved proposal, except a named ingest (FR-019).
- Named ingest MAY create thin stub Pages for names that appear in those sources. Stubs are short complete sentences. Invented names not in the source MUST NOT get a page.
- Claims about existing canon cite pages.
- Invented material is marked as invention until accepted.
- Must not contradict another page; conflicts surface to the DM (FR-011).
- `[[wikilinks]]` to related pages.
- Place, item, hazard, and creature pages match the heading order in `wiki/templates/place.md`, `item.md`, `hazard.md`, and `creature.md`. Creature bodies are linear (no column wrappers).
- Early-dev `_raw/` sample ingest keeps that sample's section order and markdown. This is not a general ingest rule.

**Identity:** filename + title. Two pages for one entity → DM merges or links; agent treats linked pages as one.

## Work / Proposal
A proposal is first shown to the DM (chat or inspectable text). It is not a wiki page yet (FR-019).

| Field | Rule |
|---|---|
| lifecycle | After DM approval, file as `accepted` (or `proposed` only if the DM asked to park it). Unapproved text is not filed. |
| grounded_in | Wiki page links and/or "D&D 5e rules" |
| invention | true if not already on a wiki page |

**Transitions**

```text
chat proposal --(DM approves)--> wiki page (accepted, or proposed if parked)
chat proposal --(DM rejects)--> no wiki page
accepted --(DM presents)--> play surface artifact
accepted --(DM accepts as canon)--> page lifecycle=canon
rejected / never-approved --x--> wiki page
rejected / never-approved --x--> play surface
```

Rejected and never-approved never reach the wiki or Foundry. Fun may reshape the chat proposal. Canon only on accept.

## Citation

Pointer on a proposal or distilled claim: `[[page]]` plus enough text to find the claim. Fake citations are invalid. Missing wiki coverage → invent Work and mark invention; do not mint a fake wiki fact.

## Session outcome

Facts from play, filed in wrapup.

| Field | Rule |
|---|---|
| session | Link to session page |
| changes | List of wiki pages to update |
| lifecycle | Chat proposal until DM accepts; then those pages update |

Prep that did not happen does not stay canon.

## Play surface artifact

Foundry actor, item, journal, or scene produced from **accepted** Work.

| Field | Rule |
|---|---|
| source_page | Wiki path |
| foundry_id | Returned by MCP |
| wording | Matches accepted text |

Unrevealed pages stay off the play surface until the DM accepts a reveal.

## Craft toolkit

Not stored data. The Co-DM procedures in `.agents/skills/`. Prep window vs wrapup window. Full pack is in v1. Output is Work unless the DM is filing accepted canon.

Prep (non-exhaustive): `npc-design`, `place-design`, `dungeon-design`, `encounter-prep`, `session-beats`, `theatre-of-the-mind`, `copy-writer`, `foundry-stage`, `foundry-battlemap`, `foundry-token`, `homebrew-monsters-5e`, `dnd5e-mechanics`, `dnd-5e-magic-item-design`, `campaign-planning`, `cold-opens`, `faction-prep`, `traps-trials`, `vehicle-design`, `travel-events`, `narrative-islands`, `sandbox-narrative`, `writing-beats`, `run-guide`, `visual-aids`, `visual-references`, `pc-interview`.

Wrapup: `session-wrapup`, `session-recap`, `reconciling-session-evidence`, `world-tick`.

Every wiki write also loads `obsidian-markdown` and `copy-writer`.
