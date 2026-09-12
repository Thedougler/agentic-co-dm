# Source ingest queue: ss2-deity-tyr

Source root: /Users/nick/ai-os/shattered-sea/wiki/entities/deities/tyr.md
Mode: migration (ledger line: docs/campaign/MIGRATION-LEDGER.md:52 —
`deity :: entities/deities/tyr.md → world/lore/ per syranita precedent —
single dispatch, write-if-lore-fits, STOP if verdict differs`)
Gate: REVIEWED-BY-HUMAN confirmed — MIGRATION-LEDGER.md:11 "REVIEWED-BY-HUMAN:
2026-07-13 — per the user's handoff mission (procedure item 4"
Started: 2026-07-13

## Sources (batch order, smallest file first)

- [x] entities/deities/tyr.md — triage: entity-source (deity), ready

## Claims — entities/deities/tyr.md

- [x] lore :: Tyr :: world/lore/tyr.md (new) — deity identity: Lawful Good god
  of law/justice/civic order/Dravosi state legitimacy, clergy's oath-witness
  function, "In the Scatter" clergy placement, DM callout on binding oaths,
  cross-refs to Dravosi Crown and Shattered Sea Pantheon (plain text, neither
  page exists) (%%src: legacy%%). Landed `status: pending` — see Fit verdict.

## Fit verdict

**Lore fits. Write authorized under the conditional dispatch.**

This file's shape is the same as the accepted `syranita.md` precedent, not an
active-NPC page:

1. **No governed/mechanical data to key, no independent agency.** The entire
   body is portfolio description (domain, symbolism, clergy function) and
   theological framing prose. Tyr never acts as a character — no statblock,
   no location the god personally occupies, no dialogue, no independent
   agenda distinct from "what his clergy do." This is the same test
   `ss-deity-syranita.md`'s fit verdict applied (npc skeleton earns its shape
   because NPCs act; Tyr doesn't).
2. **Content shape is a clean fit for `lore`'s three headings** (Player-Known
   / DM Only / Sources) — portfolio + clergy-function prose folds directly
   under DM Only, no forcing, nothing left over.
3. **Findability convention followed**: first sentence of the written page
   states "deity" plainly, matching `world/lore/syranita.md`'s precedent.

No blocking finding — proceeding to write per the dispatch's conditional
authority.

## Status disposition (reveal signal)

Source frontmatter: `status: active`, `confidence_level: confirmed`,
`audience: dm`, `publish: false`. This is **not** the stub/inferred signal
`syranita.md` carried — Tyr's source considers the deity's lore
well-established (DM-side worldbuilding confidence), not speculative.

That is a different signal than "revealed at the table," which is what
governs `status: canon` vs `status: pending` per the skill contract
("`status: canon` for content players have already seen"). Checked for
table-reveal evidence directly:

```bash
grep -rn "\bTyr\b" /Users/nick/ai-os/shattered-sea/wiki/sessions/*.md \
  /Users/nick/ai-os/shattered-sea/wiki/log.md /Users/nick/ai-os/shattered-sea/wiki/hot.md
```

Only hit: `wiki/log.md:135` — an INGEST pipeline log line recording that
`Inbox/Tyr.md` was ingested into `wiki/entities/deities/tyr.md`. No scene,
recap, or session file anywhere mentions Tyr. `audience: dm` + `publish:
false` on the source page independently corroborate: this was never
player-facing content.

**Written `status: pending`**, same outcome as syranita despite the
different source-frontmatter signal — the active/confirmed fields describe
the DM's confidence in the worldbuilding, not a player-facing reveal, and no
reveal evidence exists.

## Flags

1. **Dravosi Crown cross-ref has no page.** Source links
   `[[dravosi-crown|Dravosi Crown]]`. No `world/factions/dravosi-crown.md` (or
   equivalent) exists — `world/factions/` is empty; Dravosi Crown is only
   mentioned in prose on `world/lore/campaign-overview.md`, not its own page,
   and campaign-overview isn't a fit target for a Dravosi-Crown-specific
   link. Written as plain text. `relink: dravosi-crown — once its page
   lands`.
2. **Shattered Sea Pantheon cross-ref has no page.** Source links
   `[[shattered-sea-pantheon|Shattered Sea Pantheon]]`. No
   `world/lore/shattered-sea-pantheon.md` exists yet (stub check: `grep -ril
   "shattered-sea-pantheon" world/` → no hits). Written as plain text.
   `relink: shattered-sea-pantheon — once its page lands`.
3. **Tag `dravosi` dropped, not mapped.** Source tag `dravosi` names a
   faction/people (the Dravosi Crown) — an entity-identity tag, DROPPED BY
   DESIGN per `WIKI.md` § Tag taxonomy final bullet, not mapped to a Domain
   tag. `tags: []` on the written page, same as `syranita.md`.
4. **Frontmatter fields with no contract home.** Source frontmatter carried
   `campaign`, `audience`, `confidence_level`, `sources:` (list) — none are
   governed keys in `wiki-contract.md`'s lore schema (7 universal fields
   only). Dropped from frontmatter; `sources:` list content preserved in the
   page's own `## Sources` section instead.
