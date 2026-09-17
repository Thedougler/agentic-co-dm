# OMP Repository Addendum

This file records OMP runtime behavior and collision traps only. Project context remains in `AGENTS.md`; shared agent behavior remains in the constitution; sticky OMP constraints remain in `.omp/RULES.md`; Spec Kit artifacts remain the feature authority.

## Start and reload

- The supported primary path is a direct OMP session from the repository root. RPC/ACP can lose project task and isolation settings.
- `.omp/AGENTS.md` is an import-only shim for `../AGENTS.md`; keep project context there, not in the shim.
- After changing an OMP instruction, command, skill, or agent definition, start `/new` (or reload plugins for an in-session skill change). Use `/extensions` to confirm the expected project context is active and not shadowed.

## OMP-specific traps

- OMP list settings replace rather than merge. Preserve existing entries when changing arrays such as `disabledExtensions`; a partial override is not additive.
- `approvalMode: yolo` means tool actions do not pause for interactive approval. Safety and acceptance semantics still come from `.omp/RULES.md` and the shared canonical owners.
- OMP may discover Claude compatibility files. This project disables the duplicate Claude context extension; do not re-enable it or disable the whole Claude provider to solve a context collision.

## Ownership boundary

- Read `.omp/config.yml` for current model roles, caps, isolation, and extension settings; do not copy those values into this file.
- Read `specs/<feature>/` for feature requirements and task state; OMP commands and agents consume those artifacts rather than becoming alternate Spec Kit phases.

## Behavioral test subject

For agent-facing surface changes, use OMP's smol-agent equivalent as the independent behavioral test subject. Give it cold context, no write permission in the prompt, the relevant task or task slice to perform, and explicit scope and success criteria. Reconcile its output as behavioral evidence before declaring completion.

## Native image generation

When an OMP task needs image generation or editing, use the mounted `generate_image` device by writing one JSON request to `xd://generate_image`. Its contract is the source of truth for the current schema.

- `subject` is required. Keep one detailed subject prompt; use `action`, `scene`, `composition`, `lighting`, and `style` for structured direction.
- Supply visual anchors through `input[]`, with each image's role described in `subject`. Each input uses a local `path`, base64 `data`, and/or `mime_type`; OMP does not treat chat-only references as local paths.
- For edits, provide the source image in `input[]` and put the requested changes in `changes[]`. Do not treat a filename mentioned in prompt text as an image input.
- Use only the tool's enumerated `aspect_ratio` and `image_size` values. The reference-sheet prompt's 16K target exceeds OMP's available sizes; choose the nearest supported size instead.
- `provider` selects the backend for one request (`auto` is the default). A provider such as `openai-codex` does not change the OMP call shape.

Keep the visual skills' identity-anchor and scene-direction split. The OMP-specific part is only request construction and input transport; those skills own what the image should depict.
