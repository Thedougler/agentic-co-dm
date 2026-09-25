#!/usr/bin/env python3
"""
Report an incumbent-vs-candidate comparison from luna-eval run directories.

Reads, per run, grading.json (task_outcome, graded expectations), metrics.json
(total_tool_calls, retries, tokens.total, model, effort), and timing.json
(duration_ms), and reports facts only (data-model §3, FR-044):

- per eval: task-outcome regressions (incumbent pass, candidate not pass) and
  assertions that passed for the incumbent and fail for the candidate;
- medians of total_tool_calls, retries, tokens.total, and latency, per eval and
  overall, for each config.

It prints no verdict and no mean ± stddev. The keep/refuse decision is the
agent's, by the promotion rule in skill-creator/SKILL.md. A comparison whose
runs differ in model or effort is refused (exit 2): those runs are not
comparable.

Layout (scripts/luna-eval --out <iteration>):
    <iteration>/<eval id>/eval_metadata.json
    <iteration>/<eval id>/<config>/run-<n>/{grading,metrics,timing}.json

Usage:
    python aggregate-benchmark.py <iteration> [--incumbent old_skill] [--candidate with_skill]

Writes <iteration>/benchmark.json (read by eval-viewer) and benchmark.md.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from statistics import median

METRICS = ("total_tool_calls", "retries", "tokens", "latency_s")


def _read(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return {}


def load_runs(iteration: Path) -> list[dict]:
    runs = []
    for eval_dir in sorted(p for p in iteration.iterdir() if p.is_dir()):
        meta = _read(eval_dir / "eval_metadata.json")
        for run_dir in sorted(eval_dir.glob("*/run-*")):
            grading, metrics, timing = (_read(run_dir / f"{n}.json") for n in ("grading", "metrics", "timing"))
            if not grading and not metrics:
                continue
            expectations = grading.get("expectations", [])
            passed = sum(1 for e in expectations if e.get("passed"))
            runs.append({
                "eval_id": meta.get("eval_id", eval_dir.name),
                "eval_name": meta.get("eval_name", eval_dir.name),
                "configuration": run_dir.parent.name,
                "run_number": int(run_dir.name.split("-")[1]),
                "task_outcome": grading.get("task_outcome"),
                "model": metrics.get("model"),
                "effort": metrics.get("effort"),
                "metrics": {
                    "total_tool_calls": metrics.get("total_tool_calls"),
                    "retries": metrics.get("retries"),
                    "tokens": (metrics.get("tokens") or {}).get("total"),
                    "latency_s": timing["duration_ms"] / 1000 if timing.get("duration_ms") is not None else None,
                },
                "result": {  # the eval-viewer per-eval breakdown reads these
                    "pass_rate": round(passed / len(expectations), 4) if expectations else 0.0,
                    "passed": passed, "failed": len(expectations) - passed, "total": len(expectations),
                    "time_seconds": timing["duration_ms"] / 1000 if timing.get("duration_ms") is not None else None,
                    "tokens": (metrics.get("tokens") or {}).get("total"), "tool_calls": metrics.get("total_tool_calls"),
                },
                "expectations": expectations,
            })
    return runs


def _medians(runs: list[dict]) -> dict:
    out = {}
    for key in METRICS:
        values = [r["metrics"][key] for r in runs if r["metrics"][key] is not None]
        out[key] = median(values) if values else None
    return out


def compare(runs: list[dict], incumbent: str, candidate: str) -> dict:
    pairs = {(r.get("model"), r.get("effort")) for r in runs if r["configuration"] in (incumbent, candidate)}
    if len(pairs) > 1:
        raise ValueError(f"runs differ in model or effort: {sorted(map(str, pairs))}")
    per_eval, all_by_config = [], {incumbent: [], candidate: []}
    for eval_id in dict.fromkeys(r["eval_id"] for r in runs):
        by = {c: [r for r in runs if r["eval_id"] == eval_id and r["configuration"] == c] for c in (incumbent, candidate)}
        for c in by:
            all_by_config[c] += by[c]
        inc, cand = by[incumbent], by[candidate]
        outcome_regression = (bool(inc) and bool(cand) and all(r["task_outcome"] == "pass" for r in inc)
                              and any(r["task_outcome"] != "pass" for r in cand))
        inc_pass = {e["text"] for e in inc[0]["expectations"] if e.get("passed")} if inc else set()
        for r in inc[1:]:
            inc_pass &= {e["text"] for e in r["expectations"] if e.get("passed")}
        cand_fail = {e["text"] for r in cand for e in r["expectations"] if not e.get("passed")}
        per_eval.append({
            "eval_id": eval_id,
            "eval_name": (inc or cand or [{}])[0].get("eval_name", eval_id),
            "task_outcome": {incumbent: [r["task_outcome"] for r in inc], candidate: [r["task_outcome"] for r in cand]},
            "task_outcome_regression": outcome_regression,
            "incumbent_pass_candidate_fail": sorted(inc_pass & cand_fail),
            "medians": {incumbent: _medians(inc), candidate: _medians(cand)},
        })
    return {"model": next(iter(pairs), (None, None))[0], "effort": next(iter(pairs), (None, None))[1],
            "per_eval": per_eval, "medians": {c: _medians(rs) for c, rs in all_by_config.items()}}


def markdown(skill: str, incumbent: str, candidate: str, report: dict) -> str:
    def row(label: str, m: dict) -> str:
        return f"| {label} | " + " | ".join("—" if m[k] is None else f"{m[k]:g}" for k in METRICS) + " |"

    lines = [f"# Promotion report: {skill or 'skill'}", "",
             f"Incumbent `{incumbent}` vs candidate `{candidate}`; model `{report['model']}`, effort `{report['effort']}`.",
             "Facts only; decide by the promotion rule in skill-creator/SKILL.md.", "",
             "## Medians (all evals)", "", "| Config | tool calls | retries | tokens | latency (s) |", "|---|---|---|---|---|",
             row(incumbent, report["medians"][incumbent]), row(candidate, report["medians"][candidate]), "", "## Per eval", ""]
    for e in report["per_eval"]:
        lines += [f"### {e['eval_name']}", "",
                  f"- task outcome: {incumbent} {e['task_outcome'][incumbent]}, {candidate} {e['task_outcome'][candidate]}"
                  + (" — **regression**" if e["task_outcome_regression"] else ""),
                  "- incumbent-pass → candidate-fail assertions: "
                  + ("; ".join(f"`{t}`" for t in e["incumbent_pass_candidate_fail"]) or "none"),
                  "", "| Config | tool calls | retries | tokens | latency (s) |", "|---|---|---|---|---|",
                  row(incumbent, e["medians"][incumbent]), row(candidate, e["medians"][candidate]), ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("iteration", type=Path, help="luna-eval --out directory")
    parser.add_argument("--incumbent", default="old_skill")
    parser.add_argument("--candidate", default="with_skill")
    parser.add_argument("--skill-name", default="")
    parser.add_argument("--output", "-o", type=Path, help="benchmark.json path (default: <iteration>/benchmark.json)")
    args = parser.parse_args()

    runs = load_runs(args.iteration)
    try:
        report = compare(runs, args.incumbent, args.candidate)
    except ValueError as exc:
        print(json.dumps({"status": "error", "error": str(exc),
                          "hint": "compare runs made with one --model/--effort pair",
                          "example": "scripts/luna-eval --skill <dir> --eval <id> --config old_skill --subject-skill <snapshot> --out <iteration>"}))
        return 2
    benchmark = {
        "metadata": {"skill_name": args.skill_name, "incumbent": args.incumbent, "candidate": args.candidate,
                     "model": report["model"], "effort": report["effort"],
                     "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                     "evals_run": [e["eval_id"] for e in report["per_eval"]],
                     "runs_per_configuration": max((r["run_number"] for r in runs), default=0)},
        "report": report,
        "runs": runs,
        "notes": [],
    }
    out = args.output or args.iteration / "benchmark.json"
    out.write_text(json.dumps(benchmark, indent=2))
    out.with_suffix(".md").write_text(markdown(args.skill_name, args.incumbent, args.candidate, report))
    print(out.with_suffix(".md").read_text())
    return 0


if __name__ == "__main__":
    sys.exit(main())
