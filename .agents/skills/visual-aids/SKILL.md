---
name: visual-aids
description: >-
  Attach, ground, generate, promote, or place a player-safe visual aid for a named campaign owner
  or session moment. Use when a page needs an identity image, prep names a moment to picture, or
  a run guide needs approved images. Kind `visual-aids`. Does not gather references in place of
  visual-references when a known owner is depicted. Reference image is durable identity.
  Illustration is session-scoped and not identity. Not map rendering, spoken narration, or
  invented faces.
---

# Visual Aids

## Work gate

Prep art is Work, not auto-canon. Follow `docs/agents/work.md`.

Show a chat proposal; write a campaign wiki page only after DM accept (FR-019). Reject leaves no page. Invention is required when the wiki lacks the fact: set `invention: true` and ground in wiki pages and/or D&D 5e rules. Cite `[[pages]]` for wiki claims. Show the DM any contradiction with an existing page. Never present invention as a wiki fact. Never write silent canon. A craft `type` becomes `canon` only after DM accept.

Players see nothing until the DM accepts and presents.

Done when: the page is inspectable Work, `lifecycle: proposed`, invention flagged, grounding named.

Remap durable output paths from `campaigns/<slug>/` to `wiki/`; use `wiki/templates/`. Replace knowledge-bank wording with wiki wording. Keep the craft procedure.

The owner's appearance prose is the source of truth. A reference image supports that look; an
illustration depicts one moment and never becomes identity. Spoken `[!narration]` remains the
table's descriptive layer and an image follows the same information boundary.

Distinct things need distinct assets. Existing art, portraits, tokens, and
battlemaps may guide vibe, palette, or genre, but they are depictions of other
owners, sites, or moments. Use an existing asset only for the exact same
depicted owner/site/moment. For new content, mint or request a new image rather
than reusing one that will make different things blur together at the table.

## Ground

Read the named owner's look, existing image links, campaign style guidance if present, and output
audience. Identify every named thing depicted. A missing look is a stop: ask for appearance or
use prose only. Never infer a PC face, secret fact, pending event, or hidden location from another
page's image.

- **Reference image:** durable identity asset linked on the owner and optionally marked safe for
  players.
- **Illustration:** session-scoped moment stored with session/run-guide material, not identity.
- **Map/source art:** owned by map/layout procedure, not this identity workflow.

## Branch and persist

**Attach** an existing file under `wiki/attachments/` named `{subject-slug}-{role}.{ext}` (`wiki/attachments/README.md`). Nested `attachments/<campaign>/` only on multi-campaign collision. Link with `![[attachments/...]]`, and list it on the owner only when the identity is truly shared because the file depicts that exact owner.
Do not mark player-safe by default. On a location, embed the identity image immediately after the
title. Battlemaps and other non-identity art go under **Art**.

**Mint identity** only when a supplied look exists, no identity file is listed, and an authorized
current task needs one. Keep provisional until DM approval. PC images require player-supplied or
player-approved material. **Mint illustration** only for an explicitly named session moment; keep
it session-scoped and out of identity lists. When minting, read
[.agents/references/image-hosts.md](.agents/references/image-hosts.md) for which tool to call on
the current host. **Promote/kill** accepted candidates without leaving
competing faces active. **Assemble** only approved player-safe images for entities actually in the
guide; no gallery backfill. On a run-guide **pass 1** beat card, embed an
identity image already listed on that exact owner's page (`![[attachments/…]]`)
beside Initial Narration or the matching roster heading. Do not use a parent
region image, nearby creature portrait, old battlemap, or similar-looking asset
as identity for a new thing. Do not mint identity during beat construction.
Spoken `[!narration]` still owns the look.

Ground pixels only in style guidance, the depicted owner's look, and that owner's approved identity
references. Exclude secrets, hidden events, inaccessible pages, unrelated illustrations, and details
outside the output audience. Patch the owner, never a `kind: image` page. Use `obsidian-markdown`
and inspect for visibility leakage.

If generation is unavailable, leave an unresolved visual-aid request with the full safe prompt;
do not pretend a file exists. `obsidian-leaflet` owns maps and `theatre-of-the-mind` owns spoken
prose.
