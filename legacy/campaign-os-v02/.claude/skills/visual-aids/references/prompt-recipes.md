# Prompt Recipes and Common Mistakes

## Category defaults

Used when `vault/refs/art-style.md` doesn't override a category:

| Category | Aspect ratio | Notes |
|---|---|---|
| Portraits | `3:4` | Vertical, chest-up |
| Banners | `3:1` | Wide establishing shot |
| Scene / session art | `16:9` | Cinematic widescreen |
| Combat art | `16:9` | Terrain/tactical layout emphasis |
| Handouts | Match source (letter/A4 if a document prop) | In-world document or image |

## Diffusion prompts are machine instructions, not player-facing copy

Describe exactly what should appear, literally — a diffusion model has no idea what an evasive
euphemism looks like. Any brand-voice/tone constraints on how the campaign *talks about*
something apply to captions and alt text after generation, never to the generation prompt
itself.

## Common mistakes

| Mistake | Fix |
|---|---|
| Generating without reading the character's wiki page | Standard queries first — approximated appearances drift from canon and can't be un-generated cheaply. |
| Skipping `vault/refs/art-style.md` and using "a similar style" | Stop and ask the DM instead — see § Before generating. |
| Attaching art to an already `status: canon` page without flagging it | Flag the addition for canon-review rather than attaching it silently. |
| Writing the generation prompt into the embed's alt text | Leave the embed bare — no alt text, no pipe. |
| Embedding a second image between the same two paragraphs | One image per gap, per the Placement rules table. |
| Depicting a DM Only secret in player-visible art | Route the image under `## DM Only`; ask if unsure it counts as a reveal. |
| Inventing a bespoke image-gen script | Chain-load `use-openrouter` — its `openrouter.sh image` CLI is this skill's generation backend. |
| Skipping the page's `reference_image` when one is set | Resolve it (VA2, `reference-images`) and pass it as `--reference` so the entity stays on-model. |
| Passing an `--aspect` flag to `openrouter.sh image` | It has no aspect flag — word the aspect ratio into the prompt text (e.g. "vertical 3:4 portrait"). |
