# Sticky rules

Run the checks named in the task. Finish only with verification evidence.

Edit sources. Generated `.omp/commands/speckit.*` stay as Spec Kit wrote them.

Wait for an explicit instruction before push or deploy.

Map each change to a `tasks.md` id.

Spec Kit artifacts beat harness memory. Safety in this file beats live feature context. Live context names the active feature.

## Wiki write finalization

`.omp/hooks/post/wiki-qmd-refresh.ts` automatically launches `scripts/qmd-hook.sh` after each successful OMP `edit` or `write` targeting `wiki/`; do not invoke it manually for those writes. `tools/wiki_ops/Transaction` owns finalization for transaction writes and must not be followed by a second invocation. The post-hook is non-blocking, while `scripts/qmd-hook.sh` serializes concurrent runs, updates QMD collections, and performs one bounded embedding pass. A non-zero background result is logged without rolling back the already-committed wiki write.
