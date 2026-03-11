# MIT License
# Copyright (c) 2025 Motohiro Suzuki

"""
Generate Evidence Bundle for QSP Stage212

This script collects CI artifacts and logs and builds
a reproducible evidence bundle.

Structure produced:

evidence_bundle/
 ├ replay_attack.log
 ├ downgrade_attack.log
 ├ session_integrity.log
 ├ fail_closed.log
 ├ actions_runs.json
 ├ actions_jobs.json
 └ summary.md
"""

from pathlib import Path
import json
import datetime
import shutil

ROOT = Path(__file__).resolve().parents[1]

CI_DIR = ROOT / "out" / "ci"
LOG_DIR = ROOT / "out" / "logs"

BUNDLE_DIR = ROOT / "evidence_bundle"


def ensure_dir():
    BUNDLE_DIR.mkdir(exist_ok=True)


def copy_if_exists(src, dst):
    if src.exists():
        shutil.copy(src, dst)
        print(f"[OK] copied {src}")
    else:
        print(f"[WARN] missing {src}")


def collect_ci():
    copy_if_exists(CI_DIR / "actions_runs.json", BUNDLE_DIR / "actions_runs.json")
    copy_if_exists(CI_DIR / "actions_jobs.json", BUNDLE_DIR / "actions_jobs.json")


def collect_logs():
    logs = [
        "replay_attack.log",
        "downgrade_attack.log",
        "session_integrity.log",
        "fail_closed.log",
    ]

    for log in logs:
        src = LOG_DIR / log
        dst = BUNDLE_DIR / log
        copy_if_exists(src, dst)


def build_summary():
    now = datetime.datetime.utcnow().isoformat()

    summary = {
        "generated_at": now,
        "bundle_path": str(BUNDLE_DIR),
        "files": sorted([p.name for p in BUNDLE_DIR.glob("*")]),
        "structure": [
            "Claim",
            "CI Job",
            "Evidence Artifact",
            "CI Run ID",
            "Evidence Bundle",
        ],
    }

    summary_file = BUNDLE_DIR / "summary.md"

    with open(summary_file, "w") as f:
        f.write("# QSP Evidence Bundle\n\n")
        f.write(f"Generated: {now}\n\n")

        f.write("## Structure\n\n")
        for s in summary["structure"]:
            f.write(f"- {s}\n")

        f.write("\n## Files\n\n")
        for file in summary["files"]:
            f.write(f"- {file}\n")

    print(f"[OK] summary written: {summary_file}")


def main():
    print("[INFO] generating evidence bundle")

    ensure_dir()
    collect_ci()
    collect_logs()
    build_summary()

    print("[DONE] evidence bundle ready")


if __name__ == "__main__":
    main()
