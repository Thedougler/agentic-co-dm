# Player site (Quartz 4)

This directory is a vendored install of [Quartz v4](https://quartz.jzhao.xyz/),
configured as the default-deny (L3) publish target for the campaign wiki.

Do not build this directly with `npx quartz build` against vault content —
that bypasses the section-strip and leak-check layers. Always build through
`utils/scripts/build_site.sh` from the repo root; see
`content/ref/runbooks/publish.md` for the full contract
and `content/ref/runbooks/publish.md` for the phase runbook.

`quartz.config.ts` carries the `ExplicitPublish` filter (layer 1) and a
belt-and-suspenders `ignorePatterns` denylist. `node_modules/` and `public/`
are gitignored — run `npm install` here after cloning before building.
