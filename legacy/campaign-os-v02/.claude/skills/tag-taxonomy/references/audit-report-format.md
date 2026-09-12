# Tag audit report format

Read this only when producing a full audit report (Workflow step 8 of a
whole-repo or `--since <ref>` sweep). A single-page fix during normal
authoring doesn't need this template.

## Summary block

```
TAG AUDIT — <scope: whole-repo | --since <ref>>
Pages scanned: <n>
Alias remaps applied: <n>
Unknown tags — proposed to tags.md: <n>
Unknown tags — awaiting your call: <n>
Over-cap pages trimmed: <n>
W27 empty-tag pages resolved: <n>
Canon-gated pages reported (not edited): <n>
```

## Table 1 — Non-Canonical → Canonical (mechanical, applied)

| Page | Old tag | New tag |
|---|---|---|
| `vault/campaigns/shattered-sea/npcs/<npc>.md` | `boss-fight` | `combat` |

## Table 2 — Unknown Tags (needs your call)

| Tag | Pages | Proposal |
|---|---|---|
| `windows98` | 1 (`vault/campaigns/shattered-sea/lore/<page>.md`) | Drop — no canonical tone fits; or remap to `reference` if you want it kept |
| `heist-crew` | 3 (`vault/campaigns/shattered-sea/quests/<a>.md`, `vault/campaigns/shattered-sea/quests/<b>.md`, `vault/campaigns/shattered-sea/npcs/<c>.md`) | Add as canonical under `### Domain`, or remap all 3 to `heist` |

## Table 3 — Over-Tagged Pages (>5 non-visibility tags)

| Page | Current tags | Proposed trim |
|---|---|---|
| `vault/campaigns/shattered-sea/quests/<page>.md` | `[intrigue, heist, maritime, mystery, war, politics, combat]` (7) | Keep `[intrigue, heist, maritime, mystery, war]` — drop `politics`, `combat` (weakest signal on this page) |

## Table 4 — W27 Empty-Tag Pages (now a real finding, not legal-and-skipped)

| Page | Status | Proposed tag | Basis |
|---|---|---|---|
| `vault/srd/rules/<rule>.md` | pending | `reference` | Mechanical rules content, no tonal signal |
| `vault/campaigns/shattered-sea/npcs/<canon-npc>.md` | canon | — reported, not applied | Canon-page gate — needs your confirmation |

## Worked examples

**Alias remap (mechanical):**
```yaml
# Before
tags: [boss-fight, maritime]
# After — boss-fight is a listed alias in docs/tags.md
tags: [combat, maritime]
```

**W27 empty-tag resolution:**
```yaml
# Before
tags: []
# After — page is a rules reference with no tonal signal, reference fallback applied
tags: [reference]
```
