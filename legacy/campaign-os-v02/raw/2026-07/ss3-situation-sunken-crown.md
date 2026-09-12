# Source ingest queue: ss3-situation-sunken-crown

Source root: /Users/nick/ai-os/shattered-sea/wiki/situations/active/sunken-crown-blessing-crisis.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:75 —
`situation-active :: situations/active/sunken-crown-blessing-crisis.md → absorb
per claim-buckets — owning faction likely [[waveservants]] (exists, canon: this
line sanctions expanding world/factions/waveservants.md); active lifecycle →
Front Lifecycle: active`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:63 "REVIEWED-BY-HUMAN:
2026-07-13 — same user instruction; blessing covers exactly the 14 lines below."
Round-3 line at MIGRATION-LEDGER.md:75. canon_gate.py exit 0 (unchecked ledger
line names the target path, world/factions/waveservants.md).
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] situations/active/sunken-crown-blessing-crisis.md — triage: faction-source
  (a pressure/situation with a real owning faction), ready — owning faction
  page exists at `status: canon` (round-2 landed it, DONE eff7aa7)

## Owner verification

Source names the Waveservants directly, not by inference: a `## Location
Notes` subsection titled "Vel Orn (Shrine)" quotes a **Senior Waveservant**
("The Pearl knows your name. Umberlee is patient. You have a debt, and it is
growing with every tide." / "Your people sent you to set the seas right. This
is where the anger began.") stationed at that shrine, and the page's own
`## Connections` list states outright: "`[[waveservants|Waveservants]]` —
shrine authority tied to debt and the missing Pearl." The pressure (Umberlee's
blessing withdrawn after the Pearl theft) is exactly the Waveservants' own
domain (they collect tribute and witness maritime obligations to Umberlee per
the canon page's `## Player-Known`) — ledger line's guessed owner confirmed
from the source itself, not forced onto it. No other faction is named as
owning this pressure.

## Claims — situations/active/sunken-crown-blessing-crisis.md

- [x] situation :: Sunken Crown Blessing Crisis :: world/factions/
  waveservants.md (expand — `## Goals & Fronts`) — Front identity + Clock
  written (`### Front: The Withdrawn Blessing`, Lifecycle: active) — see
  Flag 2 for the Hard Rule 4 determination (source DOES state trigger +
  consequence fields here, unlike the ss2 precedent; transcribed verbatim,
  no segment count invented) (%%src: legacy%%)

## Flags

1. **Reconciliation, not duplication (L6).** The target page's
   `## Goals & Fronts` already carried one Front (`### Front: <none written
   yet>` — actually empty at time of this claim: round-2's ingest only wrote
   the faction's `primary_goal`-equivalent Agenda paragraph, no Front). This
   claim is the page's first Front, appended after the existing Agenda
   paragraph, not a rewrite of it. No contradiction — the existing Agenda
   paragraph (collect tribute, maintain neutrality) and this Front (collect
   on the Pearl debt specifically) are the same faction operating at two
   different specificity levels, general agenda vs. one named live pressure.

2. **Front written WITH Clock/Trigger/Consequence fields — Hard Rule 4
   determination differs from the ss2 precedent.** Unlike
   `sentinels-true-head.md` (which had only a vague "If Ignored" paragraph,
   no itemized triggers, no segment count — Front written identity-only,
   Clock omitted), THIS source states:
   - An itemized `## Triggers` section (4 concrete events: Stripes' return,
     the party consulting the Archive Stone, the party reaching Vel Orn, the
     ration window closing) — transcribed verbatim into **Trigger
     conditions**.
   - A bifurcated `## Consequences` section ("if unresolved" /
     "if the Pearl is recovered") — the unresolved branch transcribed
     verbatim into **Consequence at fill**; the recovery branch into
     **Possible outcomes**.
   - A `## Key Facts` line stating a countdown: "Keth-Naar can endure
     approximately 2 more seasons at reduced rations before being forced to
     hunt open waters or petition Umberlee directly" — this IS a
     source-stated timeframe, but it is not expressed in the Front
     template's `N segments (4/6)` game-mechanic notation. Writing "Clock: 2
     segments" would silently convert "seasons" into a mechanical unit the
     source never chose — that crosses from transcription into invention.
     Resolution: the Clock field transcribes the source's own words
     ("~2 seasons at reduced rations remain, per the source's own countdown
     — not expressed as a segment clock; DM/faction-prep converts if a
     mechanical clock is wanted") rather than forcing a segment number.
   - The page's own `### World Update — Session 03 (Cold)` entry shows the
     front has ALREADY partially advanced in actual play: the open-water
     hunting branch of the "if unresolved" consequence has begun firing
     (six hunters broke the self-imposed boundary and returned with a
     catch) — transcribed into the Front as a **filled-so-far** note rather
     than invented as "filled: 1," since the source's own record, not a
     guess, states this.
   This is the "faction pressure WITH stated trigger + consequence" row of
   claim-buckets.md (transcribe verbatim, this is formatting existing facts,
   not authoring a new Front) — genuinely different disposition from ss2,
   which is the round-3 "untested corner" this line was flagged to measure.

3. **Off-screen move drawn from the Senior Waveservant's own dialogue, not
   invented.** The source never states an active Waveservant faction move
   (no raid, no ultimatum) — the shrine's posture is patience plus marking
   debt: "Umberlee is patient. You have a debt, and it is growing with every
   tide," and the Pearl Chamber's felt-but-silent absence ("detect magic
   finds nothing"). Off-screen move written as: withholding shrine
   terms/legibility while the debt accrues — the deliberate non-intervention
   itself, not a new invented action, quoting the two lines of dialogue as
   the evidentiary basis.

4. **PC connection — named PCs exist in the source but have no campaign-os
   `pcs/` page yet.** The source names two PCs directly with dialogue aimed
   at them: Delmar Fisk ("The Pearl knows your name...") and Stripes
   Bitemore ("Your people sent you to set the seas right..."), plus
   Stripes's dispatch by Keth-Naar's elders as the connecting thread. Per
   `source-ingest`'s owned-paths (PC creation is a canon-review-signed
   event, never this skill's to originate) and campaign-os's `pcs/`
   directory currently holding zero PC pages (only `.gitkeep` + `CLAUDE.md`),
   the PC connection is written as plain text naming both PCs and the
   specific mechanism (Delmar named directly in the debt-warning; Stripes
   dispatched to investigate and is the parallel Sentinels-side connection
   from the ss2 absorption) — no wikilink, `relink: delmar-fisk — once a
   pcs/ page exists for him` and `relink: stripes-bitemore — once a pcs/
   page exists for him`.

5. **Unresolved wikilinks — written as plain text, not `[[wikilinks]]`.**
   Source links to six entities, none of which are among the 20 pages
   confirmed to exist in campaign-os `world/` this wave (estratto,
   ferrin-locke, calveno, grimaldis-dispensary, preserved-eel, fish-broth,
   sentinels-of-the-eyrie, waveservants, campaign-overview, grung, human,
   syranita, tyr, the-vault-of-the-first-factor, gentle-hag, giant-owl,
   swashbuckler, draconic-sorcery, vethka, greyteeth-runner):
   - `umberlee` (deity) — `relink: umberlee — once its page lands` (same
     open flag already logged in `world/items/delmars-cloak-of-the-manta-
     ray.md`, confirmed by grep — this is the second source independently
     needing it, not a new flag)
   - `sunken-crown` (region/location) — `relink: sunken-crown — once its
     page lands`
   - `pearl-of-souls` (item — Round 3 ledger line `item-artifact` is
     currently unchecked, still pending its own ENUM LIMIT TEST absorption)
     — relinked ✓ — `world/items/pearl-of-souls.md` landed; the "Primary
     goal" and "Possible outcomes" mentions on `world/factions/waveservants.md`'s
     Front block now link `[[pearl-of-souls|Pearl of Souls]]` (link-restoration pass R4, 2026-07-14)
   - `keth-naar` (settlement/community) — `relink: keth-naar — once its
     page lands`
   - `vel-orn` (shrine/location) — `relink: vel-orn — once its page lands`
   - `who-commissioned-the-theft` (situation/quest-shaped, no page type
     confirmed) — `relink: who-commissioned-the-theft — once its page
     lands`

6. **No tag changes.** This is a canon-page *expansion*, not a new page —
   `faction_status: active` and the existing empty `tags: []` are untouched;
   frontmatter left exactly as-is per rails item 4 (no `touched:` bump,
   consistent with the ss2 precedent's disposition on this point).

7. **`### World Update — Session 03 (Cold)` content NOT re-transcribed as a
   separate claim.** That section belongs to `world-update`'s owned
   territory (post-CANONIZE resolution of an already-advancing front), not
   `source-ingest`'s. It is cited here only as evidence for the Front's
   filled-so-far note (Flag 2) — the actual session-03 roll/consequence
   prose is left in the source, not copied onto the canon page, since this
   ledger line's disposition is "absorb the situation's identity," not
   "backfill a session record that predates this campaign-os table's own
   session log."
