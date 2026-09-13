#!/usr/bin/env python3
"""Observable 019 checks. Files and Work outcomes, not AGENTS.md snapshots."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = Path(__file__).resolve().parent
WIKI = FEATURE / "wiki"
OPS = FEATURE / "ops"
HELPER = ROOT / "scripts" / "error-ledger.py"
KIND_DIR = {
    "Encounters": "encounters",
    "Rules": "rules",
    "Campaign State": "campaign-state",
    "DM Intelligence": "dm-intelligence",
    "System": "system",
    "Source Material": "_raw",
}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing {path}")
    return path.read_text()


def run_helper(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(HELPER), "--root", str(root), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def load_json(proc: subprocess.CompletedProcess[str]) -> object:
    if proc.returncode != 0:
        fail(f"helper failed: {proc.stderr.strip() or proc.stdout}")
    return json.loads(proc.stdout)


def load_object(proc: subprocess.CompletedProcess[str]) -> dict[str, object]:
    data = load_json(proc)
    if not isinstance(data, dict):
        fail("helper output is not an object")
    return data

def scenario_aim() -> None:
    missing = read(WIKI / "campaign-hub-missing.md")
    hub = read(WIKI / "campaign-hub.md")
    intel = read(WIKI / "dm-intelligence.md")
    unaimed = read(OPS / "prep-unaimed.md")
    if "players:" in missing or "intent:" in missing:
        fail("missing hub already has table aim")
    if "Campaign State" not in missing or "Campaign State" not in hub:
        fail("aim home is not Campaign State")
    if "players: Alex, Blair, Casey" not in hub or "intent:" not in hub:
        fail("recorded hub missing players or intent")
    if "not aimed" not in unaimed or "Name the players" not in unaimed:
        fail("missing aim was not asked; Work treated as aimed")
    if "players:" in intel or "intent:" in intel:
        fail("DM Intelligence holds a second copy of the aim")


def scenario_gap() -> None:
    gap = read(OPS / "gap-prep.md")
    practice = read(WIKI / "practice.md")
    if "Gap:" not in gap or "Invention:" not in gap:
        fail("gap sitting did not name the gap or yield Work")
    if "Open on a visible clock" not in practice:
        fail("campaign-facing practice changed")


def scenario_reflection() -> None:
    reflection = read(OPS / "wrapup-reflection.md")
    proposal = read(OPS / "canon-proposal.md")
    hub = read(WIKI / "campaign-hub.md")
    if "status: offered" not in reflection:
        fail("wrapup reflection is not chat Work")
    if "observation:" not in reflection:
        fail("reflection missing observation about these players")
    if "not a silent wiki page write" not in proposal:
        fail("accepted fact change was not a canon proposal")
    if "rumor clock is not a live dock fact" in hub:
        fail("rejected or unaccepted reflection wrote wiki facts")


def scenario_sitting() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        first = load_object(
            run_helper(
                root,
                [
                    "sitting",
                    "record",
                    "--kind",
                    "prep",
                    "--job",
                    "harbor-prep",
                    "--path-read",
                    "wiki/hub.md",
                    "--skill",
                    "session-beats",
                ],
            )
        )
        if first.get("kind") != "prep" or first.get("status") != "recorded":
            fail("sitting not recorded")
        if "dm" in first:
            fail("sitting record includes DM")
        cost = first.get("token_cost")
        if not isinstance(cost, dict):
            fail("token_cost missing")
        if "not a tokenizer" not in str(cost.get("note", "")):
            fail("token_cost is not derived")
        listed = load_json(run_helper(root, ["sitting", "list"]))
        if listed != [first]:
            fail("sitting list mismatch")


def scenario_ledger() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        one = load_object(
            run_helper(
                root,
                [
                    "error",
                    "append",
                    "--id",
                    "e-1",
                    "--cause",
                    "missing night watch",
                    "--sitting",
                    "prep-1",
                ],
            )
        )
        load_object(
            run_helper(
                root,
                [
                    "error",
                    "append",
                    "--id",
                    "e-2",
                    "--cause",
                    "unrelated qmd miss",
                    "--sitting",
                    "prep-1",
                ],
            )
        )
        bad = run_helper(root, ["error", "drain", "--id", "e-1", "--cause-fixed", "false"])
        if bad.returncode == 0:
            fail("drain without cause_fixed succeeded")
        if "Drain-without-fix" not in bad.stderr:
            fail("drain-without-fix did not fail the helper")
        load_object(run_helper(root, ["error", "drain", "--id", "e-1", "--cause-fixed", "true"]))
        remaining = load_json(run_helper(root, ["error", "list"]))
        if not isinstance(remaining, list) or len(remaining) != 1:
            fail("unrelated open entries did not remain")
        leftover = remaining[0]
        if not isinstance(leftover, dict) or leftover.get("id") != "e-2":
            fail("wrong entry remained after drain")
        if one.get("status") != "open":
            fail("append did not create an open entry")


def scenario_helper() -> None:
    if not HELPER.is_file():
        fail("repeating-job helper missing")
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        load_object(
            run_helper(
                root,
                ["sitting", "record", "--kind", "prep", "--job", "ledger"],
            )
        )
        second = load_object(
            run_helper(
                root,
                [
                    "sitting",
                    "record",
                    "--kind",
                    "prep",
                    "--job",
                    "ledger",
                    "--helper",
                    "error-ledger",
                ],
            )
        )
        helpers_used = second.get("helpers_used", [])
        if not isinstance(helpers_used, list) or "error-ledger" not in helpers_used:
            fail("second sitting did not use the helper")



def regroup(dump: Path, dest: Path, kinds: dict[str, str]) -> None:
    dest.mkdir(parents=True)
    for name, kind in kinds.items():
        src = dump / name
        target_dir = dest / KIND_DIR[kind]
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target_dir / name)


def scenario_layout() -> None:
    kinds = json.loads(read(OPS / "layout-kinds.json"))
    dump = OPS / "mixed-dump"
    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / "grouped"
        regroup(dump, dest, kinds)
        encounters = list((dest / "encounters").iterdir())
        rules = list((dest / "rules").iterdir())
        system = list((dest / "system").iterdir())
        raw = list((dest / "_raw").iterdir())
        if [p.name for p in encounters] != ["dock-skirmish.md"]:
            fail("retrieving Encounters loaded unrelated files")
        if [p.name for p in rules] != ["grapple.md"]:
            fail("retrieving Rules loaded unrelated files")
        if [p.name for p in system] != ["AGENTS.md"]:
            fail("retrieving System loaded Source Material")
        if [p.name for p in raw] != ["scrap.md"]:
            fail("Source Material not staged in _raw")
        before = (dump / "dock-skirmish.md").read_text()
        after = (dest / "encounters" / "dock-skirmish.md").read_text()
        if before != after:
            fail("layout move changed page facts")
        if "type: session-prep" not in after or "type: lore" not in (dest / "rules" / "grapple.md").read_text():
            fail("layout move changed campaign type")


def scenario_layout_not_canon() -> None:
    hub = read(WIKI / "campaign-hub.md")
    intel = read(WIKI / "dm-intelligence.md")
    scrap = read(OPS / "mixed-dump" / "scrap.md")
    if "players: Alex, Blair, Casey" not in hub:
        fail("aim left the hub")
    if "players:" in intel:
        fail("layout copied table aim onto DM Intelligence")
    if scrap.strip() == "Raw staging note. Not canon.":
        pass
    else:
        fail("Source Material rewritten")
    # A move that rewrites a fact is invalid.
    original = read(OPS / "mixed-dump" / "grapple.md")
    rewritten = original.replace("Mechanical reference for the table.", "Silent canon rewrite.")
    if rewritten == original:
        fail("rewrite fixture is a no-op")
    if "Silent canon rewrite." in original:
        fail("fact text changed without accept")


def scenario_templates() -> None:
    templates = ROOT / "wiki" / "templates"
    expected = {
        "encounter.md": "session-prep",
        "rules.md": "lore",
        "campaign-state.md": "lore",
        "dm-intelligence.md": "work",
    }
    for name, typ in expected.items():
        text = read(templates / name)
        if f"type: {typ}" not in text:
            fail(f"{name} missing type {typ}")
        if "type: encounter" in text or "type: rules" in text:
            fail(f"{name} added a campaign type")
    if (templates / "system.md").is_file() or (templates / "source-material.md").is_file():
        fail("System or Source Material got a wiki template")


def scenario_rewrite() -> None:
    hub = read(WIKI / "campaign-hub.md")
    intel = read(WIKI / "dm-intelligence.md")
    encounter = read(OPS / "mixed-dump" / "dock-skirmish.md")
    rules = read(OPS / "mixed-dump" / "grapple.md")
    proposal = read(OPS / "fact-changing-rewrite.md")
    if "players: Alex, Blair, Casey" not in hub:
        fail("aim left the hub")
    if "A coastal sandbox where the three players chase sea-god debts, not a railroaded module." not in hub:
        fail("hub facts changed")
    if "## Table aim" not in hub:
        fail("campaign state missing template jobs")
    if "players:" in intel or "intent:" in intel:
        fail("aim copied off the hub")
    if "## Table analysis" not in intel:
        fail("DM Intelligence missing template jobs")
    if "A harbor fight package. Facts stay on this page." not in encounter:
        fail("encounter rewrite changed facts")
    if "## Situation" not in encounter:
        fail("encounter missing template jobs")
    if "Mechanical reference for the table." not in rules:
        fail("rules rewrite changed facts")
    if "## Current Truth" not in rules:
        fail("rules missing template jobs")
    if (OPS / "rewrite-accept.md").is_file():
        fail("structure-only rewrite required DM accept")
    if "lifecycle: proposed" not in proposal:
        fail("fact-changing rewrite is not waiting on accept")
    if "Silent canon: the sea-god is dead." in hub:
        fail("fact-changing rewrite landed without accept")



def main() -> int:
    scenario_aim()
    scenario_gap()
    scenario_reflection()
    scenario_sitting()
    scenario_ledger()
    scenario_helper()
    scenario_layout()
    scenario_layout_not_canon()
    scenario_templates()
    scenario_rewrite()
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
