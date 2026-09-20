import type { HookAPI } from "@oh-my-pi/pi-coding-agent";

export default function qmdSessionRefresh(pi: HookAPI): void {
	pi.on("session_start", async (_event, ctx) => {
		// Keep startup state fresh before the first prompt; qmd-hook bounds work and serializes writers.
		try {
			await pi.exec("scripts/qmd-hook.sh", [], { cwd: ctx.cwd });
		} catch {
			// QMD is an optional local index; startup must stay silent and continue.
		}
	});
}
