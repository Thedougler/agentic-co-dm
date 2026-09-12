# Source ingest queue: ss2-dm-perrin-primer

Source root: /Users/nick/ai-os/shattered-sea/wiki/dm/perrin-primer.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:58 —
`dm :: dm/perrin-primer.md → triage per source-ingest (dm-dir material;
expect DM Only-heavy content or a refusal/mapping — agent judges)`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:41-42 "REVIEWED-BY-HUMAN:
2026-07-13 — user instruction \"implement all your recommended fixes, then
proceed to round two\". Blessing covers exactly the 13 lines below." (line 58
is one of the 13.)
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] dm/perrin-primer.md — triage: PC-tactical/DM-primer (not in claim-buckets'
  source-types table), skipped — refusal, PC-creation boundary. No hand-off
  invoked now; see Flags for the eventual destination.

## Claims

- none — refusal outcome gets no claims list, same convention `ss-pc-jean-claude.md`
  used for its character-sheet refusal (SKILL.md §3: a hand-off/skip source gets
  a queue line, not a claims list).

## Triage verdict

**Refusal. No page written, no world/ or pcs/ touch.**

1. **Identity check first (task instruction: "perrin" may be a PC or NPC —
   check both source repos' character dirs).** Confirmed PC, not NPC:

   ```console
   find /Users/nick/ai-os/shattered-sea/wiki -iname "*perrin*"
   → entities/characters/pcs/perrin-black-jaw.md
   → entities/characters/pcs/perrin-black-jaw-sheet.pdf
   ```

   `entities/characters/npcs/` has no Perrin file. Perrin Black-Jaw is a player
   character. Campaign-os `pcs/` has no Perrin page yet (`grep -ril perrin pcs/`
   → no hits).

2. **Content shape: not the source's PC identity/sheet — a DM tactics
   cheat-sheet keyed to that PC.** Frontmatter: `type: dm-intelligence,
   subtype: pc-primer, audience: agent, publish: false`. Body opener: "Agent
   use: Read before building scenes or encounters that involve Perrin ranged
   lanes, water mobility, avoidance, family pressure, or patron fallout." Every
   section (Fast Read, Encounter Levers, Roleplay Levers, Key Mechanics) is
   spotlight/pressure guidance for running Perrin in scenes — no ability
   scores, class/level, or equipment list (the actual `perrin-black-jaw.md`
   PC-identity file is a separate, unpicked source). This is not `claim-buckets.md`
   §Source types' `character-sheet` row on the letter (no stats), but it is a
   PC-scoped artifact whose only coherent home is that PC's own page.

3. **Deciding rule: SKILL.md Owned paths § Never — "a PC page (`pcs/` — PC
   creation is a canon-review-signed event per skills-registry.md's
   `character-interview` row, not this skill's to originate)."** The content's
   natural landing spot in this system is a PC's `## Arc Notes (DM Only)`
   section (`docs/campaign/skeletons/pc.md:22`) — exactly what this primer's
   material is (spotlight/pressure tactics, roleplay levers, family/patron
   hooks). Writing it there means touching `pcs/`, which this skill never
   originates regardless of migration mode. Migration mode's owned-path
   exception doesn't reach this file for an independent reason too: the
   exception requires the ledger line's disposition to be `canon` (condition
   c); this ledger line's disposition is `triage` (agent judges), not `canon`
   — so even a `world/`-side write was never authorized here, matching
   `ss-pc-jean-claude.md`'s precedent (that line's disposition was `ask`, same
   non-`canon` shape).

4. **`research-or-guidance` considered and rejected as the primary row.** It's
   process-shaped (agent-instruction framing, "Read before building scenes")
   and would default to `skipped` on its own terms too — but its
   `Sources`/reasoning is secondary here since Owned-paths' explicit PC-page
   prohibition already forecloses a write on identity grounds alone, before
   content-shape is even reached. Both rows converge on the same outcome
   (skip), so the refusal is over-determined, not a close call.

## Flags

1. **Gap: claim-buckets.md's Source types table has no row for "PC-tactical/
   DM-primer keyed to an existing PC."** `entity-source` covers NPC/item/
   creature identity, not PC tactics; `character-sheet` covers PC stats, not
   PC play-style guidance. This file sits between the two rows. Triaged by
   analogy to the Owned-paths Never bullet and the Round-1 PC refusal
   (`ss-pc-jean-claude.md`) rather than a table row that names this shape
   directly — flagging per the task's own question ("did the skill's triage
   table handle dm/ material or did you improvise?"): partially improvised.
   A future pass could add a `pc-tactical-note` row to claim-buckets.md
   pointing at the same refusal/hand-off outcome, closing the gap explicitly
   instead of leaving it inferred each time.

2. **Hand-off destination, once available.** No skill in this registry
   currently originates a PC's `Arc Notes (DM Only)` section — `dnd5e-character-interview`
   creates `pcs/<name>.md` Overview + Backstory (skills-registry.md:45,
   same citation `ss-pc-jean-claude.md` used), not tactical/DM-only content.
   Once `pcs/perrin-black-jaw.md` exists (via that interview pipeline,
   canon-review-signed), this primer's material is the natural seed for its
   `Arc Notes (DM Only)` heading — but originating or editing that section is
   outside source-ingest's owned paths either way. Not invoking any skill now;
   naming the destination for the DM/orchestrator per the ledger line's
   "agent judges" instruction.

3. **Wikilinks in source, not followed.** Source links `[[frightened|Frightened]]`,
   `[[restrained|Restrained]]`, `[[crissdalynn-khinriss|Crissdalynn]]`,
   `[[party-combat-primer|Party Combat Primer]]`, `[[perrin-black-jaw|Perrin Black-Jaw]]`.
   Not resolved or relinked — refusal outcome writes nothing,
   so no page exists to carry them. Noted only so a future pass on this file
   (if the DM ever wants the tactics content migrated once Perrin's PC page
   exists) doesn't have to re-read the source cold.

4. **No CONTRADICTION, no blocked claim.** This is a clean triage-time
   refusal, not a conflict between sources — nothing to flag to canon-review.
