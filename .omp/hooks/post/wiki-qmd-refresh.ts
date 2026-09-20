import { resolve, relative, sep } from "node:path";
import type { HookAPI } from "@oh-my-pi/pi-coding-agent";

type WikiWriteInput = { path?: unknown };

function isWikiFile(cwd: string, input: WikiWriteInput): boolean {
	if (typeof input.path !== "string" || input.path.length === 0) return false;

	const wikiRoot = resolve(cwd, "wiki");
	const target = resolve(cwd, input.path);
	const remainder = relative(wikiRoot, target);
	return remainder.length > 0 && remainder !== ".." && !remainder.startsWith(`..${sep}`);
}

export default function (pi: HookAPI): void {
	pi.on("tool_result", (event, ctx) => {
		if ((event.toolName !== "edit" && event.toolName !== "write") || event.isError) return;
		if (!isWikiFile(ctx.cwd, event.input)) return;

		// Keep the post-hook off the agent's critical path; qmd-hook serializes bursts.
		void pi
			.exec("scripts/qmd-hook.sh", [], { cwd: ctx.cwd })
			.then(result => {
				if (result.code !== 0) {
					pi.logger.warn(`wiki QMD refresh failed: ${result.stderr.trim() || `exit ${result.code}`}`);
				}
			})
			.catch(error => {
				pi.logger.warn(`wiki QMD refresh could not start: ${String(error)}`);
			});
	});
}
