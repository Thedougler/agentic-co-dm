# Quickstart: Place Ingest Preserve

Prove ingest keeps spoken look and place shape. Do not restyle `legacy/` or rewrite `_raw/` place bodies.

## Prerequisites

- Branch `008-place-ingest-preserve`
- Spec [spec.md](./spec.md), contract [contracts/place-ingest.md](./contracts/place-ingest.md)
- `wiki-ingest` preserve GUARD includes `type: place`
- Place jobs remain in `wiki/AGENTS.md` Layout

## 1. Narration survives (P1, SC-001, SC-003)

Pick three complete `_raw/` places with filled `> [!narration] Narration` (start with `wiki/_raw/Aruhe - Old Gardens.md`).

If the DM has approved filing: ingest or promote those three. Open the wiki copies under `wiki/entities/`. Speak each look. Fail if the callout is missing, emptied, or turned into unlabeled prose. Fail if a secret, DC, or unearned name is inside the block.

If filing is not approved: dry-run the skill text — confirm the preserve GUARD would copy those files unchanged, including the narration block. Do not write wiki pages.

## 2. Format not mutated (P1, SC-002)

Side-by-side source and (filed or would-be) wiki page. Fail if Overview, At a glance, If the party, Who, What, Where, or Why is replaced by a concept-page outline. Fail if image embeds or wikilinks are stripped. Unused jobs stay omitted.

## 3. Mixed batch (SC-004)

Same ingest includes one ordinary knowledge source. Expected: place stays a place; knowledge source still compiles. Place does not land in `concepts/`.

## 4. Re-ingest (FR-007)

Re-run ingest with no body change. Fail if narration or outline is rewritten.

## 5. Legacy untouched (SC-005)

This change set does not rewrite `legacy/` or restyle historical places solely to match the sample shape.

## 6. Agent path

Open `.agents/skills/wiki-ingest/SKILL.md`. Confirm `type: place` is on the preserve path, destination `wiki/entities/`, `[!narration]` listed as a treatment not to flatten. Confirm `wiki/AGENTS.md` still owns place jobs.

Pass: steps 1–6 hold. Fail any step → ingest still mutates places.
