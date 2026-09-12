# Governance, paths, and hard rules

Read this when understanding ownership boundaries, constraints on profile
edits, and the procedural rules that govern every invocation.

## Owned paths

Writes only to `vault/campaigns/shattered-sea/pcs/combat-profile/`: `{pc-slug}-combat-profile.md`,
`vault/campaigns/shattered-sea/pcs/combat-profile/party-combat-profile.md`, and
`vault/campaigns/shattered-sea/pcs/combat-profile/loadouts/*.loadouts.yaml`; and to
`vault/campaigns/shattered-sea/pcs/character-sheets/`: `{pc-slug}-sheet.md` (template:
`_templates/pc-sheet.md`). Outside the wiki lint roots (`vault/`, `vault/campaigns/shattered-sea/pcs/`,
`vault/episodes/`) — no canon-review oversight needed
(rationale: `data-and-sheets.md` § Owned-paths rationale). Lint:
`dndsim lint`'s `W-combatant-block` and this directory's `w-combat-profile-format`
(and `W-statblock-simulatable` on `vault/`). Also writes the PC's four governed
attribute pages, `vault/campaigns/shattered-sea/pcs/{stats,abilities,spells,inventory}/{pc-slug}-{facet}.md`
— real wiki pages, W1/W5/W54-enforced (`data-and-sheets.md` § Attribute
pages). **Never writes `vault/campaigns/shattered-sea/pcs/<name>.md` itself** — `dnd5e-character-interview`'s
exclusive territory (canon-review-gated, `vault/campaigns/shattered-sea/pcs/CLAUDE.md`); this skill only
*reads* its frontmatter and `## Session Log`.

## Contract deltas (why several shared-contract items are N/A)

Items 5 (never flip `status:`/`publish:`) and 7 (`summary:`/`tier:`) — N/A; this
skill never touches a page with either key, and the profile/sheet pages this skill
owns aren't wiki pages. Item 6 (degrade by asking) applies. Creative-domain rider — N/A,
same as `llm-wiki-ingest`: fidelity-only skill; unsourced number → `[unknown]`/
`[theoretical]`, never invented (`data-and-sheets.md` § Extraction rules,
Rule 2).

## Hard rules

1. **About to recompute a profile → check idempotency first.** Before recomputing,
   check whether a profile exists and is current — its `last_session_data`/
   `last_simulated`/`last_compiled` values vs. sessions available AND the sheet's
   Combatant Block + loadout files (changed inputs → stale) — an up-to-date profile
   is a no-op, report and stop.
2. **About to write any number → cite its source tag first.** Every number carries a
   tag from the vocabulary in `data-and-sheets.md` (its single home —
   `[sheet]`, `[srd]`, `[sheet+srd]`, `[session-NN]`, `[calculated]`, `[simulated]`,
   ...). A `[simulated]` tag is valid ONLY for a number copied verbatim from an
   actual script run. No source backing → `[unknown]`/`[theoretical]`, never guessed.
3. **About to place `[simulated]`, `[calculated]`, or observed (`[session-NN]`) data
   → keep them in separate columns/lines, never shared fields** — the simulated-vs-observed
   delta is the primary calibration signal; mixing lanes hides it.
4. **About to touch the Session Combat Log → append only, never edit or delete a
   past entry**; a bad number gets a corrected new entry, not a silent rewrite.
5. **About to record observed or simulated evidence → attach a confidence label,
   always.** For observed evidence: `high` (5+ sessions), `medium` (3-4), `low`
   (1-2), `theoretical` (0). A simulated figure instead carries its assumptions: the
   policy/loadout name (default `optimal`) and `[simulated, seed N]`. Neither is
   presented as settled fact.
6. **About to reuse a past figure for a party's current ceiling → re-derive instead,
   weighting recent sessions over old ones.** A level-3 near-TPK says nothing about
   a level-9 party's current ceiling — never reuse an old number by memory.
7. **About to set a baseline stat → pull it from `vault/campaigns/shattered-sea/pcs/*.md` frontmatter
   first.** `hp_max`, `ac`, `class_levels` are the canonical source (`vault/refs/runbook-wiki.md`
   § Single-source rules). Every other value comes from the PC's attribute pages;
   `{pc-slug}-sheet.md` always includes the `## Combatant Block` (the sim's input —
   `_templates/pc-sheet.md` § Combatant Block); only sourced numbers enter it.
8. **Missing data blocks a number → degrade by asking, not guessing.** See
   SKILL.md § Degrade by asking.
9. **About to record or adjust a `[simulated]` figure → keep it reproducible and
   untouched.** Every `[simulated]` figure records seed, script version, and the
   exact command beside it (profile frontmatter carries `sim_seed`/`sim_version`/
   `last_simulated`). Never hand-adjust a simulated number — record an adjustment as
   a separate, separately-sourced line (`[session-NN]` evidence or judgment prose in
   § Calibration) next to the preserved simulated figure. Script/Node failure →
   see SKILL.md § Degrade by asking; never fabricate a `[simulated]` tag or a seed.
