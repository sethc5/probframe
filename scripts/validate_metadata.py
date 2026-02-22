#!/usr/bin/env python3
"""
validate_metadata.py — Check README.md metadata quality and completeness.

Usage:
  python3 scripts/validate_metadata.py                        # check all
  python3 scripts/validate_metadata.py --status sourced       # check sourced+ only
  python3 scripts/validate_metadata.py --warn-only            # exit 0 even with issues
  python3 scripts/validate_metadata.py patterns/06_Resource_and_Positioning_Patterns/039_Chokepoint_Control/README.md
"""

import os
import re
import sys
import argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATTERNS_DIR = os.path.join(BASE, "patterns")

STATUSES = ["empty", "scaffolded", "draft", "sourced", "reviewed", "published"]
STATUS_RANK = {s: i for i, s in enumerate(STATUSES)}

REQUIRED_FIELDS = [
    "Status",
    "Pattern class",
    "Related patterns",
    "Often combined with",
    "Degrades into",
    "Modframe instances",
    "Last reviewed",
    "Domains",
    "Actors",
]

SOURCED_REQUIRED = [
    "Related patterns",
    "Often combined with",
    "Degrades into",
    "Modframe instances",
    "Last reviewed",
    "Domains",
    "Actors",
]

DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}$")
ID_RE = re.compile(r"^[0-9]{3}$")


def parse_readme(path):
    fields = {}
    if not os.path.exists(path):
        return fields
    with open(path) as f:
        content = f.read()
    for field in REQUIRED_FIELDS + ["Tags", "Contributors", "Purpose"]:
        m = re.search(rf"^{re.escape(field)}:[ \t]*(.*)$", content, re.MULTILINE)
        if m:
            fields[field] = m.group(1).strip()
    m = re.search(r"^Status:\s*(\S+)", content, re.MULTILINE)
    if m:
        fields["Status"] = m.group(1).rstrip(".")
    return fields


def check_readme(path, require_status=None, warn_only=False):
    issues = []
    fields = parse_readme(path)

    if not fields:
        issues.append("UNREADABLE or EMPTY")
        return issues

    status = fields.get("Status", "unknown")
    status_rank = STATUS_RANK.get(status, -1)
    require_rank = STATUS_RANK.get(require_status, 0) if require_status else 0

    if status_rank < require_rank:
        return []  # skip modules below the required status

    # Check status valid
    if status not in STATUSES:
        issues.append(f"Invalid Status: '{status}'")

    # At sourced+, all fields must be populated
    if status_rank >= STATUS_RANK.get("sourced", 3):
        for f in SOURCED_REQUIRED:
            val = fields.get(f, "")
            if not val or val in ("-", "[]", ""):
                issues.append(f"REQUIRED at sourced: '{f}' is empty")

    # Last reviewed format
    lr = fields.get("Last reviewed", "")
    if lr and not DATE_RE.match(lr):
        issues.append(f"Last reviewed must be YYYY-MM format, got: '{lr}'")

    # Pattern ID format for cross-reference fields
    for field in ("Related patterns", "Often combined with", "Degrades into"):
        val = fields.get(field, "")
        if val and val not in ("-", "none", ""):
            ids = [v.strip() for v in val.split(",") if v.strip()]
            for pid in ids:
                if not ID_RE.match(pid):
                    issues.append(f"{field}: '{pid}' is not a 3-digit pattern ID")

    return issues


def scan_all(require_status=None, warn_only=False):
    errors = 0
    ok = 0
    for root, dirs, files in os.walk(PATTERNS_DIR):
        if "README.md" in files:
            path = os.path.join(root, "README.md")
            issues = check_readme(path, require_status=require_status, warn_only=warn_only)
            rel = os.path.relpath(path, BASE)
            if issues:
                print(f"\nFAIL  {rel}")
                for issue in issues:
                    print(f"  ✗ {issue}")
                errors += 1
            else:
                ok += 1
    print(f"\n{ok} passed, {errors} failed.")
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate probframe README metadata")
    parser.add_argument("paths", nargs="*", help="Specific README.md paths to check")
    parser.add_argument("--status", metavar="STATUS",
                        help="Only check modules at or above this status")
    parser.add_argument("--warn-only", action="store_true",
                        help="Print issues but exit 0")
    args = parser.parse_args()

    if args.paths:
        total_issues = 0
        for p in args.paths:
            issues = check_readme(p, require_status=args.status, warn_only=args.warn_only)
            if issues:
                print(f"FAIL  {p}")
                for issue in issues:
                    print(f"  ✗ {issue}")
                total_issues += len(issues)
            else:
                print(f"OK    {p}")
        sys.exit(0 if args.warn_only or total_issues == 0 else 1)
    else:
        errors = scan_all(require_status=args.status, warn_only=args.warn_only)
        sys.exit(0 if args.warn_only or errors == 0 else 1)


if __name__ == "__main__":
    main()
