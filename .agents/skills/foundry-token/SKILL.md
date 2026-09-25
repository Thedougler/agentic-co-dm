---
name: foundry-token
description: >-
  Circular Foundry VTT token — generate a crop-safe stand on a key color,
  isolate the subject onto full transparency, then circular-crop. Use on
  any request for a token, token art, token PNG, or converting a creature
  or NPC image to a Foundry token.
metadata:
  type: workflow
  version: "4.0"
---

# Foundry token
## Accepted-Work gate

Prep only. Follow `docs/agents/work.md`. Precondition: the source page is canon under the rule (`llm-wiki`). If it is not, refuse and name that gate. If `reveal: unrevealed`, do not stage player-visible text until the DM accepts a reveal. Wording matches accepted text.

Two phases. **Art** produces an accepted **stand** — a finished source image
with stable identity, **crop-safe** composition (subject and details survive a
centered circular crop), a **thumbnail-readable** silhouette, and a flat **key**
color filling every pixel that is not the subject. **Finalization** turns the
stand into the import PNG in one short `python3` step with Pillow: chroma-key
the stand onto transparency, centered square cover-crop, resize, anti-aliased
circular alpha mask. The accepted stand remains unchanged. The final asset is a PNG with RGBA alpha, a square canvas,
the subject isolated, and transparency everywhere else inside and outside the
circle.

## Process

### 1. Classify

Decide whether the request needs new art or finalization of an existing image.
For an existing local image, use its exact path. Identify the owner, source
image (or the need to generate one), intended output path, and target size (see
[references/foundry.md](references/foundry.md) for sizing).

**Done when** owner, source, output path, and size are known.

### 2. Generate and iterate

When no accepted stand exists, generate the source image with the image tool.
Read [.agents/references/image-hosts.md](.agents/references/image-hosts.md) for which
tool to call on the current host. Retries are new generations.
Use [references/prompt.md](references/prompt.md) for the prompt template and
[references/slots.md](references/slots.md) for slot guidance. Generate a square
source whenever possible.

Keep the subject centered inside the inner 90% of the frame — **crop-safe**.
Paint the subject on a flat **key** color from
[references/slots.md](references/slots.md). Fill every corner. Save the
accepted stand as PNG so the key field stays flat.

Choose the camera from the request: a readable portrait or action composition
for stand tokens, overhead only when the user asks for top-down art.

Iterate until the stand is accepted: identity stable, composition **crop-safe**,
silhouette **thumbnail-readable**, anatomy and gear clean, key field clean
around the silhouette. Repair with [references/repair.md](references/repair.md)
before finalizing.

**Done when** the stand is crop-safe, thumbnail-readable, identity-stable, and
the key color is a clean field around the silhouette.

### 3. Finalize

Write the final PNG from the accepted stand in one short `python3` step with
Pillow; no repository command does this. In order:

1. **Key.** Set every pixel within a small color distance of the stand's key
   color to full transparency, so anti-aliased key fringe clears too. Keep
   every subject pixel, including a painted ring that is part of the art.
2. **Crop.** Center-crop to a square that covers the frame, then resize to the
   target size with a high-quality filter.
3. **Mask.** Multiply alpha by a centered anti-aliased circle (draw it at 4×
   and downsample). Shrink the circle by about 3% of the width only when the art
   needs transparent breathing room.
4. **Save** as RGBA PNG at the output path (beside the stand as
   `<stand-stem>-token.png` when the request names none). Never write over the
   stand.

When key color survives around the silhouette, the stand has a painted
background: repaint it with the key color ([references/repair.md](references/repair.md))
and finalize again. When the crop cuts a meaningful feature, fix the stand's
composition and finalize again.

**Done when** the PNG exists at the output path and the stand file is
unchanged.

### 4. Verify

Open the final PNG and check:

- Only the subject is opaque. Sky, ground, and leftover key color are gone
  inside the circle as well as outside it.
- Machine checks with Pillow: PNG, RGBA mode, square at the target size, alpha
  0 in all four corners, and no opaque key-colored pixel left.
- Identifying features stay inside the circle edge.
- The art is **thumbnail-readable** at token size.

**Done when** machine checks pass and the isolated subject reads at thumbnail
size inside the circle.

### 5. Deliver

Report the final PNG path and one concise import line: file path, grid
footprint, pixel size, subject isolated on circular transparent alpha, and
facing when relevant. Keep the accepted stand path for future iterations.

**Done when** the user has the file and can identify its import size and framing.

## Reference

- [references/foundry.md](references/foundry.md) — import sizes, framing, and
  the import-line format.
- [references/prompt.md](references/prompt.md) — stand prompt template.
- [references/slots.md](references/slots.md) — prompt slot guidance and presets.
- [references/repair.md](references/repair.md) — repair lines for stand defects.
