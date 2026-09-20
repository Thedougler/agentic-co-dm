@../AGENTS.md

# OMP runtime

OMP list settings replace rather than merge. Preserve every existing entry when changing arrays such as `disabledProviders` and `disabledExtensions`.

Read `.omp/config.yml` for model roles, caps, isolation, and discovery settings. Do not copy those values here. Read `specs/<feature>/` for feature requirements and task state.

## Behavioral validation

Use the configured `smol` role only for changes to agent behavior while reading, writing, querying, or routing wiki content. Give it cold context (the changed instruction excerpt, task or slice, scope, and success criteria) and no write permission; reconcile its output before declaring that wiki behavior complete. Code, CLI, infrastructure, and other non-wiki changes use direct tests or smoke checks.

