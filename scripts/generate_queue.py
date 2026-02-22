#!/usr/bin/env python3
"""
generate_queue.py — Find the next probframe pattern module to work on.

Usage:
  python3 scripts/generate_queue.py --next 1
  python3 scripts/generate_queue.py --next 5
  python3 scripts/generate_queue.py --all
  python3 scripts/generate_queue.py --status draft
"""

import os
import re
import argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATTERNS_DIR = os.path.join(BASE, "patterns")

# Build priority order (pattern IDs, highest priority first)
BUILD_PRIORITY = [
    "039", "047", "054", "021", "010",
    "029", "045", "071", "034", "062",
    "072", "074", "016", "021", "024",
]

STATUSES = ["empty", "scaffolded", "draft", "sourced", "reviewed", "published"]


def get_status(readme_path):
    if not os.path.exists(readme_path):
        return "missing"
    with open(readme_path) as f:
        for line in f:
            m = re.match(r"^Status:\s*(\S+)", line.strip())
            if m:
                return m.group(1).rstrip(".")
    return "unknown"


def scan_all():
    modules = []
    if not os.path.exists(PATTERNS_DIR):
        print(f"patterns/ directory not found at {PATTERNS_DIR}")
        return modules
    for section in sorted(os.listdir(PATTERNS_DIR)):
        section_path = os.path.join(PATTERNS_DIR, section)
        if not os.path.isdir(section_path):
            continue
        for pattern in sorted(os.listdir(section_path)):
            pattern_path = os.path.join(section_path, pattern)
            if not os.path.isdir(pattern_path):
                continue
            readme = os.path.join(pattern_path, "README.md")
            outline = os.path.join(pattern_path, "outline.md")
            status = get_status(readme)
            pid = pattern.split("_")[0]
            modules.append({
                "id": pid,
                "name": pattern.replace("_", " ", 1).split(" ", 1)[-1].replace("_", " "),
                "path": os.path.relpath(pattern_path, BASE),
                "section": section,
                "status": status,
                "readme": readme,
                "outline": outline,
            })
    return modules


def priority_key(m):
    try:
        return BUILD_PRIORITY.index(m["id"])
    except ValueError:
        return 999 + int(m["id"])


def main():
    parser = argparse.ArgumentParser(description="Generate probframe work queue")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--next", type=int, metavar="N",
                       help="Show next N modules to work on (lowest lifecycle status, priority order)")
    group.add_argument("--all", action="store_true",
                       help="Show all modules with status")
    group.add_argument("--status", metavar="STATUS",
                       help="Show all modules at a given status")
    args = parser.parse_args()

    modules = scan_all()
    if not modules:
        print("No modules found.")
        return

    if args.all:
        for s in STATUSES:
            group_mods = [m for m in modules if m["status"] == s]
            if group_mods:
                print(f"\n=== {s.upper()} ({len(group_mods)}) ===")
                for m in sorted(group_mods, key=lambda x: x["id"]):
                    print(f"  {m['id']}  {m['name']}")
                    print(f"       {m['path']}")
        return

    if args.status:
        target = args.status.lower()
        matches = [m for m in modules if m["status"] == target]
        if not matches:
            print(f"No modules at status '{target}'.")
        for m in sorted(matches, key=lambda x: x["id"]):
            print(f"{m['id']}  {m['name']}")
            print(f"     {m['path']}")
        return

    # --next N: lowest status modules, sorted by build priority
    in_progress = sorted(
        [m for m in modules if m["status"] in ("empty", "scaffolded", "draft")],
        key=priority_key
    )
    queue = in_progress[: args.next]
    if not queue:
        print("No modules in progress. Check --all for full status.")
        return
    print(f"Next {len(queue)} module(s) to work on:\n")
    for m in queue:
        print(f"  [{m['status'].upper()}]  {m['id']} — {m['name']}")
        print(f"  Path:  {m['path']}")
        print(f"  Files: {m['path']}/README.md")
        print(f"         {m['path']}/outline.md")
        print()


if __name__ == "__main__":
    main()
