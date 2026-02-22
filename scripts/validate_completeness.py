#!/usr/bin/env python3
"""
validate_completeness.py — Check outline.md completeness against lifecycle gates.

Usage:
  python3 scripts/validate_completeness.py                   # check all
  python3 scripts/validate_completeness.py patterns/06_Resource_and_Positioning_Patterns/039_Chokepoint_Control/outline.md
  python3 scripts/validate_completeness.py --gate draft      # check all at draft+ against draft gate
"""

import os
import re
import sys
import argparse

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATTERNS_DIR = os.path.join(BASE, "patterns")

REQUIRED_HEADINGS = [
    "Actors and deployment context",
    "Operational sequence",
    "Where leverage concentrates",
    "Conditions of applicability",
    "Common failure modes",
    "What evidence would prove/disprove key claims",
    "Instantiations",
    "Suggested sources",
    "Analysis outline (6 parts)",
]

CLAIM_LABEL_RE = re.compile(r"\[(Observed|Inferred|Hypothesis)\]")
PLACEHOLDER_RE = re.compile(r"\[claim label\]|\[Deploying actor|\[Target actor|\[Phase name\]|\[Domain [A-C]\]")


def check_outline(path):
    issues = []
    if not os.path.exists(path):
        return [f"MISSING: {path}"]
    with open(path) as f:
        content = f.read()

    # Required headings
    for h in REQUIRED_HEADINGS:
        if f"### {h}" not in content and f"## {h}" not in content:
            issues.append(f"MISSING heading: {h}")

    # Summary and mechanism
    if "**Summary:**" not in content:
        issues.append("MISSING field: **Summary:**")
    if "**Mechanism in one sentence:**" not in content:
        issues.append("MISSING field: **Mechanism in one sentence:**")

    # Placeholder text
    if PLACEHOLDER_RE.search(content):
        issues.append("PLACEHOLDER text remains — remove all template placeholders before advancing to draft")

    return issues


def scan_all(gate=None):
    errors = 0
    ok = 0
    for root, dirs, files in os.walk(PATTERNS_DIR):
        if "outline.md" in files:
            path = os.path.join(root, "outline.md")
            issues = check_outline(path)
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
    parser = argparse.ArgumentParser(description="Validate probframe outline completeness")
    parser.add_argument("paths", nargs="*", help="Specific outline.md paths to check")
    parser.add_argument("--gate", choices=["draft", "sourced"],
                        help="Check against a specific lifecycle gate")
    args = parser.parse_args()

    if args.paths:
        total_issues = 0
        for p in args.paths:
            issues = check_outline(p)
            if issues:
                print(f"FAIL  {p}")
                for issue in issues:
                    print(f"  ✗ {issue}")
                total_issues += len(issues)
            else:
                print(f"OK    {p}")
        sys.exit(1 if total_issues else 0)
    else:
        errors = scan_all(gate=args.gate)
        sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
