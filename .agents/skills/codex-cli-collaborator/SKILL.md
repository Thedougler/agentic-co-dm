---
name: codex-cli-collaborator
description: Codex CLI at gpt-5.5 medium. Use when running `codex exec` or invoking Codex from the shell.
---

# Codex CLI

Run Codex on the command line. User config is a different model — pin every call.

```bash
codex exec -m gpt-5.5 -c model_reasoning_effort="medium" '<prompt>'
```

Done: the invoked command includes `-m gpt-5.5` and `-c model_reasoning_effort="medium"`.

If Codex reports it is not logged in, tell the user to run `codex login`.
