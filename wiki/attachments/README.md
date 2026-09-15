# Wiki attachments

Flat image store for the campaign vault.

## Filename grammar

`{subject-slug}-{role}.{ext}`

| Role | Use |
|---|---|
| `banner` | Wiki/page hero; mood open; not Foundry |
| `portrait` | Face/bust; TotM + player-visible; not a token |
| `token` | Foundry piece only (circular crop); not TotM spoken art |
| `battlemap` | Tactical grid Foundry/combat; not TotM |
| `overview` | Establishing/wide; TotM “where you are” |
| `reference` | Props/details/still for TotM grounding |
| `handout` | Player-facing table asset (letter, sketch, clue); not battlemap/portrait |
| `teaser` | Cinematic scene still; player-shareable mood/hype; not battlemap, portrait, or diegetic handout |
| `recording` | Session audio/video capture; file as `session-<NN>-recording.{ext}`; not TotM art |

**TotM/spoken / player-shareable:** portrait, overview, reference, handout, teaser (± banner mood).
Distinguish: `overview` = establishing/layout; `teaser` = cinematic scene still; `handout` = diegetic table prop.  
**Foundry-only:** token, battlemap.

## Rules

- kebab-case slug; one role suffix; no spaces
- Embed: `![[attachments/{subject-slug}-{role}.ext]]`
- Prefer flat `wiki/attachments/`; nested `attachments/shattered-sea/{type}/` is deprecated unless multi-campaign collision forces a campaign prefix
- One file per subject+role; no parallel copies
- Embed in a table cell: `![[attachments/{subject-slug}-{role}.ext\|400]]`
- On rename, update embeds in the same pass
- Owner pages: `## Art` cites these roles; omit the section when unused

Mass rename + embed rewrite is an ATE follow-on — do not migrate here without a remorph plan.
