# Foundry import

## Finalization

Finalization (SKILL.md step 3) chroma-keys the stand's flat background to
transparency, center-crops to a square, resizes, preserves the remaining art
and alpha, then applies a centered circular alpha mask. It never overwrites the
stand.

## Sizes

Use the size that matches the intended import footprint and the detail the art
needs:

| Intended footprint | Default final PNG |
|---|---:|
| Tiny or Small | `256x256` |
| Medium or one-square token | `512x512` |
| Large or detailed scene token | `1024x1024` |

Foundry can scale a PNG on import. The target size is the pixel size of the
file, not the grid footprint.

## Framing

The subject is isolated: every non-subject pixel is transparent, including
interior pixels inside the circle. A painted ring is part of the generated
source art and is preserved when present; finalization does not invent one.
Leave a transparent margin of about 3% of the width when the accepted art needs
breathing space between the subject and the canvas edge.

## Facing

Finalization does not rotate or reinterpret the art. Report the intended
facing only when the source composition makes facing relevant. Overhead art may
use Foundry rotation `0` for south; a portrait or medallion token has no
automatic facing rule.

## Import line

Use one concise line:

`artifacts/tokens/owner-token.png — Medium 1x1 — 512 px — subject isolated on circular transparent alpha — facing from source art`
