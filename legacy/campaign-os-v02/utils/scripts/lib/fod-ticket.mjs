// Write a fix-on-discovery ticket in `record-it`'s schema. The audits emit
// findings as tickets rather than as a report, because the autonomous
// `fix-on-discovery` driver already drains that queue on background
// subagents — a report needs a human to read it, a ticket does not.
//
// Idempotent by slug: re-running an audit rewrites its own pending ticket
// rather than piling up duplicates, and never touches one the sweep has
// already ruled on (status PASS or FAIL).
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

/**
 * @param {string} repoRoot
 * @param {{slug: string, lever: string, target: string, title: string,
 *          gap: string, saves: string, red: string}} ticket
 * @returns {"written" | "unchanged" | "skipped-ruled"}
 */
export function writeTicket(repoRoot, ticket) {
  const dir = join(repoRoot, ".claude", "fix-on-discovery");
  mkdirSync(dir, { recursive: true });
  const path = join(dir, `${ticket.slug}.md`);

  if (existsSync(path)) {
    const existing = readFileSync(path, "utf8");
    // A ticket the sweep already ruled on is history — never reopen it from
    // an audit run, or a fixed thing re-files itself every session forever.
    if (/^status:\s*(PASS|FAIL)\s*$/m.test(existing)) return "skipped-ruled";
  }

  const body = `---
status: pending
lever: ${ticket.lever}
target: ${ticket.target}
---
# ${ticket.title}

**Gap:** ${ticket.gap}

**Saves:** ${ticket.saves}

**RED:** ${ticket.red}

**GREEN:** — filled by the sweep.
`;

  if (existsSync(path) && readFileSync(path, "utf8") === body) return "unchanged";
  writeFileSync(path, body);
  return "written";
}
