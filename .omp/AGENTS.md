@../AGENTS.md

# OMP runtime

OMP list settings replace rather than merge. Preserve every existing entry when changing arrays such as `disabledProviders` and `disabledExtensions`.

Read `.omp/config.yml` for model roles, caps, isolation, and discovery settings. Do not copy those values here. Read `specs/<feature>/` for feature requirements and task state.

## Behavioral validation

Use the weakest available configured model for every skill evaluation, behavioral test, benchmark, and related validation of agent behavior. Select the configured `smol` role when it is the weakest available role. Give it cold context (the changed instruction excerpt, task or slice, scope, and success criteria) and no write permission; reconcile its output before declaring that wiki behavior is complete. The `skill-creator` workflow is reserved for modifying agent skills; other agent-facing changes use their applicable workflow. Code, CLI, infrastructure, and other non-wiki changes use direct tests or smoke checks.

