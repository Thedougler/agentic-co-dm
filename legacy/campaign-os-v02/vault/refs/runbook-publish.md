---
type: runbook
status: canon
publish: false
aliases: []
created: 2026-07-30
updated: "2026-08-08"
tags: [craft]
summary: "Phase 6: write the flip/hold publish proposal, get human approval, build the site (strips DM-only), and deploy on a green PUBLISH-CHECK."
phase: 6
uid: edc90de5-0ad1-4d72-a4b9-60b2eaa82e9d
---

# PUBLISH runbook (Phase 6)

GATE: `git log --oneline | grep "recap(sNN)"`. Paste it.
No commit -> STOP. Tell the user RECAP is the missing upstream phase.

Workflow: `.claude/skills/publish-site/SKILL.md` runs proposal -> approval
-> build -> leak-check -> commit/deploy. This page is that skill's contract
(the layered defense, the secrets blacklist, the proposal shape, and the
acceptance bar below) — not a second copy of its procedure.

Done = `PUBLISH-CHECK: PASS` pasted, `publish(sNN): ...` commit, deploy
triggered.

## The layered defense

Secret material must pass **two independent, mandatory, deterministic
layers** to leak, plus an optional third semantic layer. Either mandatory
layer alone would occasionally fail; a weak model operating both will not
fail them identically.

1. **Page opt-in.** Quartz runs the `ExplicitPublish` filter
   (`utils/site/quartz.config.ts`): only `publish: true` pages build.
   Everything else (`status: pending` pages, DM notes, `docs/`) does not
   exist to the builder. Default-deny is `vault/CLAUDE.md` rule 3 and
   `vault/refs/vault/_common/lifecycle.md`; only `publish-site` may flip
   the flag.
2. **Section strip.** `build_site.sh` copies publishable pages to a staging
   dir, deletes every DM-only section and every `%%…%%` comment, and builds
   from staging. A DM-only section is any H2/H3 whose heading text contains
   `dm only` **case-insensitive**, stripped from the heading to the next
   heading of the same-or-higher level. Vault files are never modified;
   the strip happens on the copy.
3. **Optional, advisory:** `.claude/agents/site-auditor.md` reads the built
   pages for inference leaks. Deterministic layers gate the deploy; the
   auditor advises on semantic safety.

Quartz's own `ignore` patterns duplicate the structural denylist
(`docs/`, the vendored CC-BY SRD/craft reference material, `utils/scripts/`,
`.claude/`, transcripts) as a second layer, not as the primary one.

## docs/secrets.md

A human + `canon-review`-maintained blacklist: one line per string that must
never appear player-side, with a pointer to why.

```markdown
%%GENERATED-BY-HUMANS — automated pipelines read, never write%%
- "Solange Barret is Otar"        → vault/campaigns/shattered-sea/npcs/otar-the-foul.md
- "the bell was never drowned"    → vault/campaigns/shattered-sea/quests/the-drowned-bell.md
```

Entries stay short and distinctive (names, unique noun phrases), never
sentences. Short entries match more phrasings. When `canon-review` resolves
a reveal, the resolving session *moves* the line to a `## Revealed` section
rather than deleting it. `vault/refs/runbook-ingest.md` (INGEST) may
*suggest* new lines; only the human commits them.

## What gets published

`vault/episodes/NNN/sNN-recap.md` and `vault/episodes/NNN/sNN-highlights.md` after review; `vault/` pages the
party has actually engaged with; `vault/campaigns/shattered-sea/pcs/` overview/backstory if the players
want them shared; a generated `Latest` page (newest recap + open
`quest_status: active` quest blurbs, written by `build_site.sh`, marked
`%%GENERATED%%`).

## The publish proposal

```markdown
# Publish proposal — s12
Flip publish: true
- vault/episodes/012/s12-recap.md — session recap
- vault/campaigns/shattered-sea/locations/gullscrag.md — party spent the whole session here
Leave unpublished (met but sensitive):
- vault/campaigns/shattered-sea/npcs/otar-the-foul.md — the s12 reveal goes on the page but HOLD
  until the party confirms sharing
```

The human edits/approves in chat or in-file; `publish-site` executes exactly
the approved list and pastes the diff of flipped flags as evidence.

## Acceptance

1. A vault with one `publish: true` page and fifty `publish: false` pages
   builds a site with exactly one page.
2. That page, containing a DM Only section, builds with the section
   stripped, and the vault copy is byte-identical after.
3. The GitHub Action (`.github/workflows/publish-site.yml`) reproduces items 1 and 2.
