# Source ingest queue: ss-situation-draves

Source root: /Users/nick/ai-os/shattered-sea/wiki/situations/dormant/draves-bloodline-question.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md — `situation ::
situations/dormant/draves-bloodline-question.md → absorb into faction fronts
(settled wave design) — agent identifies owning faction or flags homeless-pressure
per claim-buckets`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN:
2026-07-13 — per the user's handoff mission (procedure item 4 verbatim)..."
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] situations/dormant/draves-bloodline-question.md — triage: faction-source
  (a pressure/situation naming a would-be interested party, Aldric Drave), blocked
  (no owning faction page, no linked NPC/location page — see Flags)

## Claims — situations/dormant/draves-bloodline-question.md

- [x] situation :: The Draves Bloodline Question :: NONE (homeless-pressure,
  flagged, nothing written) — per claim-buckets.md § Claim buckets row "Pressure/
  situation with no owning faction": write identity facts on whatever linked
  page exists; none exists here. Wrote nothing to world/. (%%src: legacy%% would
  have applied to any written facts; none written.)

## Flags

1. **Homeless pressure — no owning faction, no landing page at all.** The source
   is a DM-side revelation thread, not really a faction Front: its three named
   actors are [[geoffrey-draves|Geoffrey Draves]] (a PC/crew member with a
   suspicious surname), [[world/npcs/aldous-draves|Aldous Draves]] (his father, a Crown
   factor clerk), and [[world/npcs/aldric-drave|Aldric Drave]] (the historical bloodline
   figure whose genealogical apparatus makes the entry structurally interesting).
   None of these has a page in `world/` — `world/factions/` is empty (only
   `.gitkeep`), and stub-check greps for every named entity (`draves`, `drave`,
   `geoffrey`, `aldous`, `aldric`, `knighton`, `dorian bishop`, `dravosi`) across
   `world/`, `pcs/`, `prep/` returned nothing. `world/npcs/estratto.md` is the
   only page in the wiki and is unrelated. Per claim-buckets.md's homeless-
   pressure row: "Write identity facts on whatever linked page exists (NPC/
   location DM Only), flag in queue file, ask the DM" — no linked page exists,
   so per SKILL.md step 3(b) of the task's own claim-bucket routing, nothing was
   written. This is the predicted, correct outcome for a wiki this empty, not a
   failure to find a home.

2. **Faction fronts absorb the *craft*, not necessarily *this specific file*.**
   The migration ledger's disposition text ("absorb into faction fronts —
   settled wave design") describes where *situation-typed content in general*
   now lives once a faction exists to own it. It does not guarantee this
   particular file has an owning faction today. Aldric Drave is the only actor
   with faction-shaped weight (he built Crown infrastructure and has an
   "heir-selection process" — Front-shaped material: a goal, a method, a
   trigger condition), but "Aldric Drave" / "the Crown" has no faction page,
   and inventing one is explicitly out of scope (SKILL.md Claim buckets:
   "don't invent a faction to own it"; rails for this task: "don't invent a
   faction page to house it"). Recommend to the DM: if/when a Crown or
   Aldric-Drave-adjacent faction page is created (e.g. during a future
   `faction :: entities/factions/sentinels-of-the-eyrie.md` -style ledger line,
   or fresh `faction-prep` work), re-run this source against claim-buckets —
   at that point "Aldric's genealogical apparatus already contains the Draves
   entry" becomes a legitimate Front identity claim (goal: confirm/exploit a
   Draves-branch descendant; no stated trigger/consequence numbers in the
   source, so Hard Rule 4 would still leave the clock fields blank pending
   `faction-prep`).

3. **Lifecycle-state mapping — worked out on paper, unusable here.** The source
   frontmatter states `status: dormant` / `lifecycle: dormant`. `faction-prep`'s
   Front template (`.claude/skills/faction-prep/SKILL.md:141`) already defines
   exactly this vocabulary as a *per-Front body field*: `**Lifecycle:** active |
   dormant | resolved` — a clean 1:1 match for this source's own `dormant`
   value, and distinct from the whole-page `faction_status: active | dormant |
   dissolved` frontmatter key (`docs/campaign/skeletons/faction.md:9`), which
   describes the *faction's* current standing, not any one pressure's. So the
   mapping mechanism is real and would work smoothly — **if** there were a
   Front to attach `**Lifecycle:** dormant` to. There isn't (Flag 1), so the
   value was recorded here rather than written anywhere in `world/`.

4. **Reciprocal-link deferral.** All three named actors, plus
   `[[drave-vaults|Drave Vaults]]` and the parent revelation
   `[[aldric-drave-designed-the-crown]]`, are withheld as plain text per
   Migration-mode link deferral — no stub pages created for merely-linked
   entities, per SKILL.md Owned Paths and this task's own rails item 3. Since
   nothing was written to `world/`, this is a note for whichever future ledger
   line creates those pages, not a `relink:` flag on any page of this agent's
   own (there is no page to carry the flag).
