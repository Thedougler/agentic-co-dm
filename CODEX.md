# Codex Repository Addendum

Temporary Codex-only image-generation notes. Shared policy remains in `AGENTS.md`; this file records only native Codex behavior and verified gaps.

## Native image handling

- The repository currently documents `codex exec -m gpt-5.5 -c model_reasoning_effort="medium"` for text collaboration, but it contains no verified Codex-native image-generation or image-edit invocation.
- Do not substitute OMP's `xd://generate_image` request shape for a Codex CLI call. The OMP `openai-codex` provider is a backend selector, not evidence of Codex-harness behavior.
- Preserve host-provided image references exactly. Do not turn an unrecognized Codex attachment token into a guessed vault path.
- Apply the visual skills' identity-anchor and scene-direction brief, then confirm the actual Codex result and returned asset location before filing or linking it.

A future Codex-focused session must replace this temporary boundary with the installed native contract and a tested input/output example.
