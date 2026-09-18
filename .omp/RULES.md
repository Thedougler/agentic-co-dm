# Sticky rules

Run the checks named in the task. Finish only with verification evidence.

Edit sources. Generated `.omp/commands/speckit.*` stay as Spec Kit wrote them.

Wait for an explicit instruction before push or deploy.

Map each change to a `tasks.md` id.

Spec Kit artifacts beat harness memory. Safety in this file beats live feature context. Live context names the active feature.

## Wiki write finalization

After a successful live wiki write transaction, run `scripts/qmd-hook.sh` exactly once. `tools/wiki_ops/Transaction` owns this call during transaction finalization; do not invoke it a second time. For direct OMP-managed writes outside `Transaction`, the agent must invoke the hook once after the write set commits. The hook is silent on success and when QMD is unavailable; it serializes concurrent invocations, updates the index, and performs one bounded embedding pass. A non-zero exit is an actionable finalization failure and must be reported without rolling back the already-committed wiki write.
