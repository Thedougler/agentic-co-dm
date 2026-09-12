// Hook cost/yield audit. Hooks are the lever this repo has most often had to
// disable or refactor, so every installed hook is measured rather than
// trusted: what it costs on every session, and what its output actually
// produced downstream.
//
// Cost is measured by running each hook against a scratch file and timing it
// (tinybench, already a dep) and counting the bytes it prints — a
// SessionStart hook's stdout is context every session pays for.
//
// Yield is only claimable where it is derivable: a hook that files
// fix-on-discovery tickets is credited with the tickets in that queue whose
// `status:` reached PASS. A hook that spends context every session and has
// no derivable yield files its own removal ticket — the retirement executes
// itself rather than waiting for someone to read a report.
//
// Nothing here mutates the repo: tool hooks are pointed at a scratch copy,
// never at a real vault file.
import { Bench } from "tinybench";
import { execFileSync } from "node:child_process";
import { mkdtempSync, readFileSync, readdirSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { writeTicket } from "./lib/fod-ticket.mjs";

const repoRoot = join(dirname(fileURLToPath(import.meta.url)), "..", "..");

// A hook whose stdout is context every session pays for. Above this many
// bytes on a clean run it has to justify itself with derivable yield.
const CLEAN_OUTPUT_BUDGET_BYTES = 200;
// Slower than this and the hook is a visible pause on every session start.
const SLOW_MS = 3000;

function loadHooks() {
  const settings = JSON.parse(readFileSync(join(repoRoot, ".claude", "settings.json"), "utf8"));
  const out = [];
  for (const [event, matchers] of Object.entries(settings.hooks ?? {})) {
    for (const matcher of matchers) {
      for (const hook of matcher.hooks ?? []) {
        if (hook.type !== "command") continue;
        out.push({ event, matcher: matcher.matcher ?? "", command: hook.command });
      }
    }
  }
  return out;
}

// PreToolUse/PostToolUse hooks read the edited path from the stdin JSON
// payload (.claude/rules/scripts.md) — point them at a scratch file so the
// audit never lints or rewrites real vault content.
function stdinFor(event, scratchFile) {
  const base = { session_id: "audit", cwd: repoRoot, hook_event_name: event };
  if (event === "PreToolUse" || event === "PostToolUse") {
    return JSON.stringify({ ...base, tool_name: "Edit", tool_input: { file_path: scratchFile } });
  }
  return JSON.stringify({ ...base, source: "startup" });
}

function runHook(command, stdin) {
  try {
    const stdout = execFileSync("bash", ["-c", command], {
      cwd: repoRoot,
      input: stdin,
      encoding: "utf8",
      timeout: 120000,
      maxBuffer: 8 * 1024 * 1024,
    });
    return { ok: true, bytes: Buffer.byteLength(stdout) };
  } catch (err) {
    // A hook that exits non-zero still printed something; both matter.
    return { ok: false, bytes: Buffer.byteLength(String(err.stdout ?? "")) };
  }
}

// Tickets whose status reached PASS are the only derivable yield signal in
// the repo — the queue records what a filed finding actually became.
function queueYield() {
  const dir = join(repoRoot, ".claude", "fix-on-discovery");
  let files;
  try {
    files = readdirSync(dir).filter((f) => f.endsWith(".md"));
  } catch {
    return { filed: 0, passed: 0 };
  }
  let passed = 0;
  for (const file of files) {
    const raw = readFileSync(join(dir, file), "utf8");
    if (/^status:\s*PASS\s*$/m.test(raw)) passed += 1;
  }
  return { filed: files.length, passed };
}

const scratchDir = mkdtempSync(join(tmpdir(), "campaign-os-hook-audit-"));
const scratchFile = join(scratchDir, "scratch.md");
writeFileSync(scratchFile, "---\ntype: note\n---\n\n# Scratch\n\nAudit scratch file.\n");

const rows = [];
try {
  for (const hook of loadHooks()) {
    const stdin = stdinFor(hook.event, scratchFile);
    const first = runHook(hook.command, stdin);

    const bench = new Bench({ iterations: 3, time: 0 });
    bench.add(hook.command, () => runHook(hook.command, stdin));
    await bench.run();
    const ms = Math.round(bench.tasks[0].result?.latency?.mean ?? 0);

    rows.push({ ...hook, bytes: first.bytes, ok: first.ok, ms });
  }
} finally {
  rmSync(scratchDir, { recursive: true, force: true });
}

const { filed, passed } = queueYield();

console.log("HOOK AUDIT");
console.log("");
console.log("| Event | Command | Clean output | Mean ms | Exit |");
console.log("|---|---|---|---|---|");
for (const row of rows) {
  const cmd = row.command.replace(/^utils\/scripts\//, "");
  console.log(`| ${row.event} | ${cmd} | ${row.bytes} B | ${row.ms} | ${row.ok ? "0" : "non-zero"} |`);
}
console.log("");
console.log(`fix-on-discovery queue: ${filed} ticket(s), ${passed} reached PASS.`);

// Verdicts. A hook is reported `retire` only on evidence it costs context
// every session with nothing derivable to show for it — the same bar a
// human would have to meet to justify pulling it.
const verdicts = [];
for (const row of rows) {
  const noisy = row.bytes > CLEAN_OUTPUT_BUDGET_BYTES;
  const slow = row.ms > SLOW_MS;
  const filesTickets = /fix-on-discovery|record-it|session_retro/.test(row.command);
  const yieldless = filesTickets && filed > 0 && passed === 0;

  if (yieldless) {
    verdicts.push({
      row,
      verdict: "retire",
      why: `files tickets but none of the queue's ${filed} reached PASS`,
    });
  } else if (noisy && !filesTickets) {
    verdicts.push({
      row,
      verdict: "review",
      why: `prints ${row.bytes} B on a clean run (budget ${CLEAN_OUTPUT_BUDGET_BYTES} B) with no derivable yield`,
    });
  } else if (slow) {
    verdicts.push({ row, verdict: "review", why: `takes ${row.ms} ms every fire (over ${SLOW_MS} ms)` });
  } else {
    verdicts.push({ row, verdict: "keep", why: `${row.bytes} B, ${row.ms} ms` });
  }
}

console.log("");
for (const v of verdicts) {
  console.log(`${v.verdict.toUpperCase()}: ${v.row.event} ${v.row.command} — ${v.why}`);
}

// Only `retire` files a ticket, and only on derivable yield evidence. A
// `review` verdict is a byte/latency measurement — real, worth reading, but
// not proof a hook is worthless, and the driver acts on tickets without
// asking. Auto-filing on a byte count alone would let it pull the mandated
// orientation hook, whose whole job is printing a directive every session.
let written = 0;
for (const v of verdicts) {
  if (v.verdict !== "retire") continue;
  const slug = `hook-${v.verdict}-${v.row.command.replace(/[^a-z0-9]+/gi, "-").replace(/^-|-$/g, "").toLowerCase()}`;
  const result = writeTicket(repoRoot, {
    slug,
    lever: "settings",
    target: `.claude/settings.json ${v.row.command}`,
    title: `${v.verdict === "retire" ? "Retire" : "Review"} the ${v.row.event} hook ${v.row.command}`,
    gap: `The ${v.row.event} hook \`${v.row.command}\` ${v.why}. A hook that spends context or wall-clock on every fire has to earn it; this one's cost is measured and its yield is not.`,
    saves: `Every session pays this hook's cost whether or not it helps. Removing a hook that does not pay for itself is the cheapest context win available, and leaving it in place teaches the next reader that unmeasured hooks are acceptable.`,
    red: `\`npm run audit:hooks\` on ${new Date().toISOString().slice(0, 10)}: clean-run output ${v.row.bytes} B, mean ${v.row.ms} ms over 3 runs; fix-on-discovery queue holds ${filed} ticket(s), ${passed} at PASS.`,
  });
  if (result === "written") written += 1;
}

console.log("");
console.log(`${written} ticket(s) filed to .claude/fix-on-discovery/.`);
