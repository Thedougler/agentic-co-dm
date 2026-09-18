# OMP Repository Addendum

This file records OMP-only runtime behavior, collision traps, and mounted-device request mechanics. `AGENTS.md` owns project context; the constitution owns shared agent behavior; `.omp/RULES.md` owns sticky OMP constraints; Spec Kit artifacts own feature behavior and task state.

## OMP-specific traps

- OMP list settings replace rather than merge. Preserve every existing entry when changing arrays such as `disabledExtensions`.
- `.omp/AGENTS.md` is an import-only shim for `../AGENTS.md`; keep project context there, not in the shim.
- OMP may discover Claude compatibility files. This project disables the duplicate Claude context extension; do not re-enable it or disable the whole Claude provider to solve a context collision.

## Ownership boundary

- Read `.omp/config.yml` for current model roles, caps, isolation, and extension settings; do not copy those values into this file.
- Read `specs/<feature>/` for feature requirements and task state; OMP commands and agents consume those artifacts rather than becoming alternate Spec Kit phases.

## Behavioral validation

For any agent-facing surface change, use the configured `smol` role as an independent behavioral test subject. Give it cold context, no write permission, the relevant task or slice, and explicit scope and success criteria. Reconcile its output as evidence before declaring completion; if it cannot run, record the blocker and compensating validation. Done when the subject demonstrates the requested behavior without out-of-scope work.

## Wiki-write finalization

`tools/wiki_ops/Transaction` runs `scripts/qmd-hook.sh` exactly once after a successful write set. Direct OMP-managed wiki writes invoke the standalone hook once after committing; never turn it into a git hook or run it once per file.

## Native image generation

When an OMP task needs image generation or editing, read the mounted `generate_image` contract and send one JSON request to `xd://generate_image`.

- `subject` is required. Keep one detailed subject prompt; use `action`, `scene`, `composition`, `lighting`, and `style` for structured direction.
- Put visual anchors in `input[]`, describing each input's role in `subject`. Inputs use a local `path`, base64 `data`, and/or `mime_type`; chat-only references are not local paths.
- For edits, put the source image in `input[]` and requested changes in `changes[]`; a filename in prompt text is not an image input.
- Use only enumerated `aspect_ratio` and `image_size` values. For the unavailable 16K reference-sheet target, choose the nearest supported size.
- `provider` selects the backend for one request (`auto` is the default); it does not change the request shape.

The visual skills own identity anchors and scene direction. OMP owns only request construction and input transport. Done when the device returns the requested asset or an actionable error.
