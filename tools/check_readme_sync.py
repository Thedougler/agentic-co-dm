#!/usr/bin/env python3
"""Report commits that changed README.md without a later README_TW.md update."""

import subprocess
import sys
from pathlib import Path


def main() -> int:
    repo = Path(__file__).resolve().parent.parent

    tw = repo / "README_TW.md"
    if not tw.exists():
        print("README_TW.md does not exist yet — translation not started.")
        return 0

    diff = subprocess.run(
        ["git", "log", "--oneline", "--", "README.md"],
        capture_output=True, text=True, cwd=repo,
    )

    last_tw_result = subprocess.run(
        ["git", "log", "-1", "--format=%H", "--", "README_TW.md"],
        capture_output=True, text=True, cwd=repo,
    )
    last_tw = last_tw_result.stdout.strip() or None

    if last_tw:
        pending = subprocess.run(
            ["git", "log", "--oneline", f"{last_tw}..HEAD", "--", "README.md"],
            capture_output=True, text=True, cwd=repo,
        )
        pending_lines = pending.stdout.strip().splitlines()
    else:
        pending_lines = diff.stdout.strip().splitlines()

    if not pending_lines:
        print("README_TW.md is up to date.")
        return 0

    print(f"{len(pending_lines)} commit(s) changed README.md since last README_TW.md update:\n")
    for line in pending_lines:
        print(f"  {line}")

    if last_tw:
        en_diff = subprocess.run(
            ["git", "diff", f"{last_tw}..HEAD", "--", "README.md"],
            capture_output=True, text=True, cwd=repo,
        )
    else:
        en_diff = subprocess.run(
            ["git", "diff", "--no-index", "/dev/null", "README.md"],
            capture_output=True, text=True, cwd=repo,
        )
    if en_diff.stdout.strip():
        print(f"\nPending English diff:\n{en_diff.stdout}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
