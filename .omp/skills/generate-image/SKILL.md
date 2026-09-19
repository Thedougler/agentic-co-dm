---
name: generate-image
description: >
  Generate or edit images in OMP via xd://generate_image. Use for identity art,
  tokens, battlemaps, illustrations, and image edits. Does not gather vault
  anchors or place wiki art; those stay with visual-references and visual-aids.
---

# Generate image (OMP)

Read `xd://generate_image` for the live contract, then send one JSON request to that device.

Load `visual-references` before any depiction of a vault owner. Load `visual-aids` when the result must be attached, promoted, or placed.

## Request

- `subject` is required. Keep one detailed subject prompt. Use `action`, `scene`, `composition`, `lighting`, and `style` for structured direction.
- Put visual anchors in `input[]` and name each input's role in `subject` (`Image 1`, `Image 2`, …). Each input is a local `path`, base64 `data`, and/or `mime_type`. A filename in prompt text is not an input. A previous generated frame is not an identity anchor.
- Edits: source image in `input[]`, requested changes in `changes[]`.
- Use only enumerated `aspect_ratio` and `image_size` values. For an unavailable 16K reference-sheet target, choose the nearest supported size.
- `provider` selects the backend for one request (`auto` is default). It does not change the request shape.

Done when the device returns the requested asset or an actionable error.
