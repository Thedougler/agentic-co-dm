---
name: reference-images
description: The reference_image convention for a Campaign OS vault (vault/, _templates/ present) — a real reference photo or canon-art a page stores as image-generation context. Mandatory first check before generating a portrait, banner, or depiction of an entity's own page. Not the generated output (visual-aids).
---

# reference-images

`reference_image` is a page's **generation context**: a real reference photo, an actor/likeness
still, or a piece of canon-art the image generator conditions on to keep a character, location,
or item on-model across regenerations. It is distinct from the finished portrait or banner
`visual-aids` generates and embeds — that is *output*; this is *input*. The field is optional;
most pages never set one.

This skill owns the convention (frontmatter field, storage path, display block) and the resolver
a generation skill calls. It does not generate images — `visual-aids` does, over the
`use-openrouter` / `use-replicate` backend.

## The convention

- **Field.** `reference_image:` in page frontmatter — a single vault-relative path (from the repo
  root), or empty. Present in every content template's spine; empty by default.
- **Storage.** `_assets/reference/<page-slug>-reference.<ext>`, flat, page-slug named — the same
  slug the page's other assets use (`vault/_templates/CLAUDE.md` § `ASSET_SUBFOLDERS` registers
  `reference`). Add the file there, then set `reference_image:` to that path.
- **Format.** A raster the generator accepts: `png | jpg | jpeg | webp | gif`. Not `svg` —
  `openrouter.sh --reference` rejects it, and so does the resolver (exit 6).
- **Display.** Each template carries this Meta Bind block near the top; it renders the set image
  as a bounded thumbnail in Obsidian and **renders nothing when the field is empty**, so it is
  safe to ship unconditionally:

  ````text
  ```meta-bind
  VIEW[{reference_image}][image(class(reference-image-view))]
  ```
  ````

  Styled by `vault/.obsidian/snippets/reference-image.css` (`.reference-image-view`). Obsidian-only:
  Meta Bind does not run in Quartz, so the block renders no image on the published player site —
  a reference still (which may be a real person's likeness) never reaches players through it.
  This is the only Meta Bind convention this skill owns — for the plugin's general syntax
  (`INPUT`/`VIEW`/`BUTTON`, bind targets, composed patterns), see `obsidian-metabind`.

## Resolve it — the caller's recipe

A generation skill about to depict an entity feeds that entity's reference image to the generator
as context. Do not hand-parse frontmatter for it — run the resolver, which reads the field,
resolves it against the vault root, and validates the file exists.

1. **RI1 — Resolve.** Run the resolver on the page you are about to depict:
   ```bash
   node .claude/skills/reference-images/scripts/resolve-reference-image.mjs <page-path>
   ```
   It prints the absolute path on stdout (exit 0) when the field is set and the file exists.
   `RI1: <abs path printed | exit code>`.
2. **RI2 — Branch on the exit code, do not treat a non-zero as an error to surface.** Exit 3
   (field unset — the common case, the field is optional) or 4/6 (set but missing/unsupported) →
   generate **without** a reference, exactly as if the page had none; never block generation on a
   missing reference image. Only exit 0 yields a path to pass. `RI2: <path to pass | none —
   generate without reference>`.
3. **RI3 — Feed it as generation context.** Pass the resolved path as a `--reference` flag to the
   image call (`openrouter.sh` accepts one or more; today the field yields one):
   ```bash
   openrouter.sh image <model> "<prompt>" out.png --reference "$REF"
   ```
   `RI3: <generation call includes --reference | no reference passed>`.

Resolver exit codes: `0` path printed · `3` field unset/empty · `4` file missing · `5` vault root
undetectable (pass `--vault-root`) · `6` unsupported extension · `2` bad usage/unreadable page.

## Adding a reference image to a page

Drop the file at `_assets/reference/<page-slug>-reference.<ext>`, set the page's
`reference_image:` to that vault-relative path, and leave the template's Meta Bind block in place
to preview it. On a `status: canon` page, treat the addition like any other canon edit
(canon-review), not a silent attach.

## Related

- `visual-aids` — generates and embeds the *output* portrait/banner/scene art; the caller of this
  skill's resolver. Reference input vs generated output — the two never overlap.
- `use-openrouter` — the `openrouter.sh image ... --reference <path>` backend that consumes the
  resolved path; it base64-encodes and builds the image-to-image payload itself.
- `vault/_templates/CLAUDE.md` — owns `ASSET_SUBFOLDERS` (the `reference` folder) and the frontmatter
  spine that carries the `reference_image` field.
