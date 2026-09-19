@../AGENTS.md

# OMP runtime

OMP list settings replace rather than merge. Preserve every existing entry when changing arrays such as `disabledProviders` and `disabledExtensions`.

Read `.omp/config.yml` for model roles, caps, isolation, and discovery settings. Do not copy those values here. Read `specs/<feature>/` for feature requirements and task state.

## Behavioral validation

For any agent-facing surface change, use the configured `smol` role as an independent behavioral test subject. Give it cold context, no write permission, the relevant task or slice, and explicit scope and success criteria. Reconcile its output as evidence before declaring completion; if it cannot run, record the blocker and compensating validation. Done when the subject demonstrates the requested behavior without out-of-scope work.

