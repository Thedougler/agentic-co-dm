---
paths:
  - "vault/refs/**"
  - "vault/srd/monsters/**"
  - "vault/srd/spells/**"
  - "vault/srd/items/**"
  - "vault/srd/classes/**"
  - "vault/srd/feats/**"
  - "vault/srd/species/**"
  - "vault/srd/backgrounds/**"
---
Vendored SRD/craft reference material is ordinary, editable wiki content
with provenance — advisory reference, not canon, and not read-only (DM
ruling 2026-07-25). Edit it directly like any other page; lint applies in
full. Keep each
page's `source:` pointing at its archived original under
`raw/` — the archive copy, not the live page, is the fidelity record —
and `source_url:` set when an up-to-date external source exists.
Re-importing or recreating a whole source document from scratch still goes
through `find-guidelines` + `guideline-recreator`; sources arrive via
`inbox/`. SRD monster pages use the unified ```statblock``` fence
(`vault/refs/vault/monster/references/statblock-format.md`);
`w-statblock-simulatable` keeps every converted page sim-parseable.
