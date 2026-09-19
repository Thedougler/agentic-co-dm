---
name: visual-references
description: >-
  Gather visual anchors — reference images and appearance prose — from vault entity pages before
  generating or editing art that depicts them. Fires before any image generation or image edit call
  when the composition includes a vault PC, NPC, monster, location, vehicle, item, or named moment.
  Kind `visual-references`. Not for placing finished art on pages; use visual-aids for that.
  Missing look → stop; do not invent a face.
---

# Visual References

File what constitution X makes canon. Follow `docs/agents/work.md`.

## Workflow

1. **Resolve every depicted owner.** Use `qmd-retrieval` or a known path to find each entity
   that appears in the image. Completion: every named subject has an owner page, or the gap
   is explicitly flagged as missing.

2. **Collect visual anchors.** Read the sections that carry appearance on each owner page:
   `## Visual reference`, `## Art`, the identity image near the title, `[!narration]` body
   when player-safe, and frontmatter `summary` as a last fallback. Resolve each `![[...]]`
   embed to its actual file under `attachments/` as an absolute path. Record user-attached
   chat images using the active host's native image reference; these may have no vault path.
   Completion: each owner has a list of source lines plus resolved image paths or host references.

3. **Inspect the pixels.** Open each reference image. The pixels are the authority — filename,
   alt text, and prose that contradict what the image actually shows yield to what you see.
   Completion: each reference image has a stated role (e.g. `Delmar identity sheet`,
   `Spoke Ring layout`) and any prose–pixel conflict is resolved in the pixels' favour.

4. **Choose the smallest useful set.** Prefer high-signal anchors in this order:
   - **Reference/design sheets** — identity, outfit, equipment, palette, repeated features.
   - **Portraits** — face, expression, posture, upper-body identity.
   - **Scene or place art** — layout, material, light, environmental silhouette.
   - **Tokens** — low detail; use only when no better identity image exists.

   Keep the strongest anchor for each central subject before adding vibe or layout references.
   Completion: every attached image depicts an owner actually in the composition, and each
   central subject has its strongest available anchor attached.

5. **Feed the host image tool.** Use the active harness's native request contract:
   [Codex](../../../CODEX.md) or [Grok Build](../../../GROK.md).
   The input field must hold the identity files or host-supported image tokens — a filename
   in prompt text is not the input. A previous generated frame is not an identity anchor.
   Read `references/prompt-inventory.md` for the structured brief template. Completion: when
   identity anchors exist, the native image-input field contains them; when none exist, the
   call is text-only.

6. **Stop on missing anchors.** If a known entity has neither appearance prose nor a usable
   reference image, ask for visual guidance or create the missing design through the
   appropriate craft path before generating. Completion: every depicted canon owner is
   grounded in vault anchors, not invented.

## Scope boundary

This skill gathers and feeds visual anchors. It does not decide whether to generate, judge
the result, place finished files, or update owner pages. After generation, hand off to
`visual-aids` when the result needs to be attached, promoted, or embedded in the vault.
