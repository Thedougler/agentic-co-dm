# Source ingest queue: ss-faction-sentinels

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/factions/sentinels-of-the-eyrie.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `faction :: entities/factions/sentinels-of-the-eyrie.md`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN: 2026-07-13 — per the user's handoff mission..."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/factions/sentinels-of-the-eyrie.md — triage: entity-source, ready

## Claims — entities/factions/sentinels-of-the-eyrie.md

- [x] faction :: Sentinels of the Eyrie :: world/factions/sentinels-of-the-eyrie.md (new) — full faction identity, doctrine, pilgrimage/Long Reach, DM-only true-head flag, no invented Front clock (%%src: legacy%%)

## Flags

1. **`status: canon` — signal that decided it.** Ledger line 27 pre-declares
   `status: canon` as this line's disposition, but per this agent's rails
   (round-1 learning) that's verified independently, not taken on faith —
   same discipline the sibling npc/estratto queue applied (and overrode, in
   that case). For this file the independent check confirms canon: the
   *source repo's* `player-primer.md` (lines 133, 157) names "The Sentinels
   of the Eyrie" and their watch over the Drowned Maw as established
   player-facing setting knowledge, and
   `sessions/session-01-scene-02-crissdalynn.md` (line 27) is read-aloud
   backstory text telling the PC Crissdalynn her own training under this
   order already happened before session 1. Both are player-facing/
   already-revealed material in the source campaign, not DM-only prep — so
   `status: canon` stands, unlike the npc line where the equivalent check
   flipped the disposition to `pending`.

2. **Front clock — Hard Rule 4.** The source's DM callout links
   `sentinels-true-head` (a *different*, out-of-ledger-scope situation file:
   "late-game revelation — the 200-year record is kept by a Soul Incarnate
   sealed beneath High Eyrie"). No segments/trigger/consequence are stated
   anywhere in the source for this pressure. Written as an identity fact in
   `## DM Only` only, explicitly **not** a Front, per Hard Rule 4. If the DM
   wants this playable as a Front, that's `faction-prep`'s job, not this
   agent's — flagging the handoff, not building it.

3. **Unresolved wikilinks — written as plain text, not `[[wikilinks]]`.**
   Source links to five other entities, none of which have pages in
   campaign-os `world/`/`pcs/` yet:
   - `high-eyrie` (location) — `relink: high-eyrie — once its page lands`
   - `waveservants` (faction) — relinked ✓ — `world/factions/waveservants.md` landed;
     the "Waveservants of Umberlee" mention now links `[[waveservants|Waveservants]]`
     (link-restoration pass R4, 2026-07-14)
   - `umberlee` (deity — no deity page type exists yet in this migration
     wave, per ledger line 29) — `relink: umberlee — once its page lands`
   - `the-drowned-maw` (location) — `relink: the-drowned-maw — once its page lands`
   - `crissdalynn-khinriss` — resolved ✓ (link-pass R6, 2026-07-14):
     `pcs/crissdalynn-khinriss.md` landed (canon rung 2, R5); the "Crissdalynn
     Khinriss trained under this tradition" mention now links
     `[[crissdalynn-khinriss|Crissdalynn Khinriss]]`.
   - `sentinels-true-head` (situation, dormant, DM secret) — **not** on the
     ledger's 15 lines at all (the ledger's one situation line is
     `draves-bloodline-question`, a different file). `relink:
     sentinels-true-head — only if a future wave migrates this specific
     situation file; not guaranteed by this stress test's scope`.

4. **Tag substitution — one dropped outright, not force-fit.** Source tags
   `drowned-maw`, `recurring` are neither canonical Domain tags nor listed
   aliases in `world/_meta/tags.md` (Project tags empty at bootstrap).
   Substituted `drowned-maw` → `mystery` (nearest domain fit: an order whose
   doctrine is recording an unexplained phenomenon without interpreting it)
   plus added `exploration` (perimeter circuits, reef mapping — stated
   pilgrimage content, not invented). **`recurring` was dropped, not
   substituted** — it describes campaign-play frequency, not tone/genre, and
   forcing it onto a Domain tag (unlike the npc/estratto precedent, which
   substituted both source tags) would misrepresent the taxonomy. Flagged as
   a judgment call rather than following the estratto precedent's 1:1
   substitution count.

5. **Frontmatter fields with no contract home.** Source frontmatter carried
   `campaign`, `audience`, `confidence_level`, `sources:` — none are
   governed keys in wiki-contract.md's faction schema. Dropped from
   frontmatter; no substitute invented.

6. **`created`/`touched: legacy`.** Same placeholder as the npc/estratto
   line — `wiki-contract.md` only defines `sNN` or `prep`; `legacy` is the
   closest-fidelity value, sanctioned per MIGRATION-LEDGER.md `## Flags`
   (round-1 friction F4).
