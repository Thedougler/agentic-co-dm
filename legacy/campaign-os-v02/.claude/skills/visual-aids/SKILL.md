---
name: visual-aids
description: Generate, place, or embed visual aids for the campaign — portraits, banners, scene art, combat art — in a Campaign OS repo (vault/ present). Use for "generate art for", "create a visual", "make a scene image", "add a portrait", "illustrate this", "banner for". Not tactical battlemaps (battlemap-render).
---

# Visual Aids

Art/portrait/scene-image generation and placement for the campaign wiki.

**Creative-domain rider applies.** Facts (character descriptions, established look), canon
(`status:`/`publish:` untouched by this skill), structure (owned paths below), and visibility
(never generate DM-only reveal art into a player-visible slot) are bound. Prompt *style* inside
those rails is free — offer bold, evocative composition choices, not the safest possible
illustration. A generation that plays it visually safe "to be careful" is violating this
skill's contract, not honoring it.

## Before generating

Read `vault/refs/art-style.md` before every generation task. It defines the campaign's
visual style, negative constraints, category overrides, and character appearance references —
this is where the DM's actual aesthetic choices live; this skill supplies structure and
mechanics, never invents the style itself.

**If `vault/refs/art-style.md` does not exist, stop and ask the DM** (degrade by
asking, contract item 6) — do not generate with an improvised style and do not silently fall
back to a generic default. This file has no bootstrap default anywhere in this repo today.

## Standard queries

Before building any prompt that depicts an existing NPC, location, or other established entity:

```
grep -ril "<entity name>" vault/ 2>/dev/null
grep -rn "^## Player-Known\|^## DM Only" <hit path>   # read both — see note below
```

Read every character's wiki page before including them in a prompt. If a character lacks
sufficient visual description on their page, **ask the DM — do not approximate.** Pull physical
description from wherever it lives on the page (Player-Known prose, a Lore Sheet, a DM Only
note) but never depict a DM Only *secret* visually (a hidden true identity, a concealed
injury) — see the Visibility contract in `references/embedding-and-visibility.md`.

## Prompt construction

Build every generation prompt by combining — in this order:

1. **Base style** — `style_prompt` from `vault/refs/art-style.md`
2. **Category modifiers** — aspect ratio and rules from the matching category override (below,
   or `vault/refs/art-style.md`'s own overrides if it defines them — art-style.md wins on conflict, since
   it's the DM's explicit choice)
3. **Scene-specific content** — composition, characters, action, lighting, environment
4. **Character descriptions** — pulled verbatim from wiki pages (Standard queries above), never
   invented
5. **Negative constraints** — `negative` field from `vault/refs/art-style.md`, appended at the end

Diffusion prompts are machine instructions, not player-facing copy — never brand-voice/tone
constraints; see `references/prompt-recipes.md`.

Category aspect-ratio defaults (portraits, banners, scene, combat, handouts):
`references/prompt-recipes.md`.

## Image generation

**Chain-load `use-openrouter`** (Skill tool) to generate — the campaign's OpenRouter image
backend, driven by its `openrouter.sh image` CLI. Read that skill's own images reference for
the model list, the `--reference` flag, and `image_config` options rather than guessing them
here.

Run these steps in order; each ends on its `VA<n>:` tag so a run is provable in the transcript.

1. **VA1 — Style + entity read.** Read `vault/refs/art-style.md` (§ Before generating) and every
   entity page the prompt depicts (§ Standard queries). `VA1: <style loaded + pages read>`.
2. **VA2 — Resolve the reference image.** Before building the prompt, resolve the depicted
   page's `reference_image` so the generator can condition on it and keep the entity on-model.
   Never hand-parse the frontmatter, and never block generation when the field is unset or the
   file is missing -> instead: run the resolver and branch on its exit code (unset is the common
   case — the field is optional). `VA2: <--reference path to pass | none — generate without>`.
   -> chain-load `reference-images`; your next tool call is Read on its SKILL.md, no acting tool
   call beside it — then follow its RI1 (run `resolve-reference-image.mjs <page-path>`) → RI2
   (branch: exit 0 yields a path, exit 3/4/6 → generate with no reference) → RI3 (pass the
   resolved path as `--reference`) recipe.
3. **VA3 — Construct the prompt** per § Prompt construction (the 5-layer combine). The aspect
   ratio from `references/prompt-recipes.md`'s Category defaults (or `vault/refs/art-style.md`'s override)
   is expressed *in the prompt text itself* — e.g. "vertical 3:4 chest-up portrait", "wide 3:1
   establishing banner" — because `openrouter.sh image` takes no aspect flag. `VA3: <prompt
   built, aspect worded in>`.
4. **VA4 — Generate.** Determine the output path from § Owned paths, then run `openrouter.sh
   image` with the model, the constructed prompt, the output path, and any `--reference` from
   VA2 (omit the flag entirely when VA2 yielded none):

   ```bash
   bash ~/.claude/skills/use-openrouter/scripts/openrouter.sh image \
     google/gemini-2.5-flash-image \
     "your constructed prompt here" \
     _assets/scene-art/session-06/kyzil-reunion-scene.png \
     --reference _assets/reference/master-kyzil-reference.webp
   ```

   The script is installed globally, not in this repo — do not hardcode a repo-local path.
   `google/gemini-2.5-flash-image` is the default (it accepts `--reference` for image-to-image
   and emits PNG); pick a higher-tier model from `use-openrouter`'s own model list for a final
   table/publish-ready piece rather than guessing a model id here. `VA4: <image written to
   path>`.
5. **VA5 — Verify + embed.** Show the result to the user in chat, Read the output path to verify
   it yourself before calling it done, regenerate with a refined prompt if it's poor, then embed
   per § Embedding in Markdown below. `VA5: <verified + embedded>`.

### Fulfilling a `[!visual-aid]` callout

When you encounter an existing `[!visual-aid]` callout on a page, use its prompt text to
generate the image via the workflow above, then replace the callout with a standard embed.

### Fallback (no generation available)

Generation fails (no API key, error, no credits, `use-openrouter` not installed) → write the
full prompt as a `> [!visual-aid]` callout instead of skipping the image: `references/fallback-callout.md`.

## Owned paths

Writes into the top-level `_assets/` tree, organized flat by asset type
(`_assets/portraits/`, `_assets/banners/`, `_assets/scene-art/`, `_assets/misc/`, …) — never
co-located with the page. Two cases:

- **Entity art** (portrait, banner, scene/combat art for an NPC, location, faction, item, or
  encounter page) → `_assets/<type>/<page-slug>-<category>.<ext>`, flat, no per-content-type
  subfolder — entity/page slugs are globally unique across the vault. A page at
  vault/campaigns/shattered-sea/npcs/renn-oxby.md gets `_assets/portraits/renn-oxby-portrait.webp` or
  `_assets/banners/renn-oxby-banner.webp`; a category with no dedicated type folder (combat art,
  handouts) lands in `_assets/misc/`. If the entity page is already `status: canon`, flag the
  addition for canon-review rather than attaching it silently.
- **Session art** (recap beats, run-guide scene art) →
  `_assets/scene-art/session-NN/<description>.<ext>` — session-scoped, nested one level further
  by session number under its own type folder. `recap-writer` and `draft-run-guide` embed
  from here; this skill never writes the session's own recap.md, highlights.md, or run-guide.md itself.

Never sets `status:` or `publish:` on any page, never edits page prose other than inserting the
one embed line at the placement this skill specifies — the calling prep/recap skill owns the
rest of the page.

## Embedding in Markdown

**Syntax:** Obsidian wikilink embed. Path from repo root.

```markdown
![[_assets/portraits/renn-oxby-portrait.webp]]
```

**No alt text.** Leave the embed bare — no pipe, no generation prompt. If a regeneration
record is needed, keep the prompt out of the page (a prompt log, a commit message, or the
image generator's own history), never as alt text on the embed.

Width-control syntax, the full Placement rules table (document type → where/limit), the
**Never** list, and the full Visibility contract (DM Only secret art, `publish: false` default):
`references/embedding-and-visibility.md`. Core rule: never embed art depicting a `## DM Only`
secret into a player-visible slot — ask the DM if unsure it counts as a reveal.

## When to generate

Do-generate / do-not-generate triggers: `references/when-to-generate.md`.

## Degrade by asking

- `vault/refs/art-style.md` missing → stop and ask the DM (§ Before generating);
  never improvise a style.
- A named character in the prompt has no visual description on their wiki page → ask the DM;
  never approximate a look.
- Unclear whether a requested image would depict DM Only secret content → ask before
  generating, don't guess and generate anyway.
- `use-openrouter` isn't installed or generation fails → use the § Fallback callout, don't
  silently skip the image or invent an ad hoc generation path.

## Related

- `battlemap-render` — top-down tactical battlemaps; NOT this skill's job, and vice versa.
- `use-openrouter` — the OpenRouter image backend this skill chain-loads (`openrouter.sh image`).
- `reference-images` — owns the `reference_image` convention and the resolver VA2 runs to feed a
  page's reference still to the generator as `--reference` context.
- `vault/refs/art-style.md` — the DM-owned style guide this skill reads and never
  writes.
- `.claude/skills/draft-content/references/npc.md`, `.claude/skills/draft-content/references/location.md`, `encounter-prep`, `draft-run-guide`, `recap-writer` — the
  callers. Each skips this skill silently if it isn't installed or a portrait/scene isn't
  warranted; none of them re-implement image generation themselves.

## Reference files

| File | Covers |
|---|---|
| `references/prompt-recipes.md` | Category aspect-ratio defaults, diffusion-prompt rationale, Common mistakes table |
| `references/embedding-and-visibility.md` | Width-control syntax, Placement rules table, full Visibility contract |
| `references/fallback-callout.md` | Generation fails or `use-openrouter` isn't installed — the `[!visual-aid]` callout fallback |
| `references/when-to-generate.md` | Deciding whether a task calls for generating art at all |
