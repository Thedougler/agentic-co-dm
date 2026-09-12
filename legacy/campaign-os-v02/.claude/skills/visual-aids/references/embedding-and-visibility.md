# Embedding, Placement, and Visibility

## Embedding in Markdown

**Syntax:** Obsidian wikilink embed. Path from repo root — see `visual-aids`'s own § Owned
paths for the `_assets/<type>/...` layout.

```markdown
![[_assets/portraits/renn-oxby-portrait.webp]]
```

**No alt text.** Leave the embed bare — no pipe, no generation prompt. If a regeneration
record is needed, keep the prompt out of the page (a prompt log, a commit message, or the
image generator's own history), never as alt text on the embed.

**Width control** (optional, only when the default is too large):

```markdown
![[_assets/portraits/renn-oxby-portrait.webp|400]]
```

### Placement rules

| Document type | Where to embed | Limit |
|---|---|---|
| NPC page | Inside `## Player-Known`, after the Quote, before the Lore Sheet | 1 portrait |
| Location page | Inside `## Player-Known`, after the opening `[!read-aloud]` callout | 1 banner or establishing shot |
| Session recap | Between narrative sections, at the scene break it illustrates | 1 per major scene beat |
| Run guide | Inline with the scene it supports | 1 per scene |
| Encounter page | Top, before tactical details | 1 scene-setter |
| PC gallery page (`vault/campaigns/shattered-sea/pcs/galleries/<pc-slug>-gallery.md`) | Under the matching `## Portraits`/`## Scenes`/`## Reference` heading, the subfolder from `wiki.toml`'s `[thresholds]`'s `ASSET_SUBFOLDERS` matching each embed | No per-page limit — this page exists to accumulate images |

**Never:**
- Embed images inside a `[!read-aloud]` callout — place them as their own block
  immediately before or after the callout per the table above.
- Place more than one image between consecutive prose paragraphs.
- Embed without a blank line above and below the embed line.
- Embed art depicting content still under `## DM Only` into a page or slot a player will see —
  see § Visibility.

## Visibility

This skill generates images; it never decides what a player is allowed to see — that's L3
(default-deny publishing) and the template's Player-Known/DM Only split, same as prose.

- Art that depicts or reveals a `## DM Only` secret (a hidden true identity, a concealed wound,
  a not-yet-revealed threat) is generated, if at all, as a **DM-only reference image** — embed
  it under `## DM Only`, never under `## Player-Known`, and never in a `publish: true` page's
  built output. When in doubt whether a visual detail counts as a reveal, ask the DM rather than
  guessing.
- A page's `publish: false` default (every `_templates/<type>.md` defaults to it) means none of its
  embedded art ships to the player site either, until `publish-site` flips the page — this skill
  doesn't need to double-check publish state itself, but never embeds secret-revealing art on
  the *assumption* a page will stay unpublished.
