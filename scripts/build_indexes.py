#!/usr/bin/env python3
"""
build_indexes.py — Generate actor, domain, and pattern indexes from README metadata.

Usage:
  python3 scripts/build_indexes.py                 # write indexes to docs/indexes/
  python3 scripts/build_indexes.py --stdout         # print to stdout only
  python3 scripts/build_indexes.py --index domains  # build domain index only
"""

import os
import re
import json
import argparse
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATTERNS_DIR = os.path.join(BASE, "patterns")
INDEXES_DIR = os.path.join(BASE, "docs", "indexes")

STATUSES = ["empty", "scaffolded", "draft", "sourced", "reviewed", "published"]


def parse_readme(path):
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        content = f.read()
    data = {}

    def extract(field):
        m = re.search(rf"^{re.escape(field)}:[ \t]*(.*)$", content, re.MULTILINE)
        return m.group(1).strip() if m else ""

    def extract_list(field):
        val = extract(field)
        if not val or val in ("-", ""):
            return []
        return [v.strip() for v in val.split(",") if v.strip()]

    data["status"] = extract("Status").rstrip(".")
    data["pattern_class"] = extract("Pattern class")
    data["related_patterns"] = extract_list("Related patterns")
    data["often_combined_with"] = extract_list("Often combined with")
    data["degrades_into"] = extract_list("Degrades into")
    data["modframe_instances"] = extract_list("Modframe instances")
    data["last_reviewed"] = extract("Last reviewed")

    domains_m = re.findall(r"^\s+-\s+(\w+)$", content, re.MULTILINE)
    data["domains"] = domains_m

    actor_blocks = re.findall(
        r"^\s+-\s+name:\s*(.+)$\n\s+type:\s*(.+)$", content, re.MULTILINE
    )
    data["actors"] = [{"name": n.strip(), "type": t.strip()} for n, t in actor_blocks]

    return data


def scan_modules():
    modules = []
    for root, dirs, files in os.walk(PATTERNS_DIR):
        if "README.md" not in files:
            continue
        readme = os.path.join(root, "README.md")
        rel = os.path.relpath(root, BASE)
        parts = rel.split(os.sep)
        if len(parts) < 2:
            continue
        pattern_dir = parts[-1]
        pid = pattern_dir.split("_")[0]
        name = pattern_dir[len(pid)+1:].replace("_", " ")
        data = parse_readme(readme)
        data["id"] = pid
        data["name"] = name
        data["path"] = rel
        modules.append(data)
    return sorted(modules, key=lambda m: m["id"])


def build_domain_index(modules):
    index = defaultdict(list)
    for m in modules:
        for d in m.get("domains", []):
            if d:
                index[d].append({"id": m["id"], "name": m["name"], "path": m["path"], "status": m["status"]})
    return dict(sorted(index.items()))


def build_actor_index(modules):
    index = defaultdict(list)
    for m in modules:
        for a in m.get("actors", []):
            atype = a.get("type", "unknown")
            index[atype].append({"id": m["id"], "name": m["name"], "path": m["path"],
                                  "actor": a.get("name", ""), "status": m["status"]})
    return dict(sorted(index.items()))


def build_status_index(modules):
    index = defaultdict(list)
    for m in modules:
        s = m.get("status", "unknown")
        index[s].append({"id": m["id"], "name": m["name"], "path": m["path"]})
    # preserve lifecycle order
    return {s: index[s] for s in STATUSES if s in index}


def build_degrade_graph(modules):
    graph = {}
    for m in modules:
        targets = m.get("degrades_into", [])
        if targets:
            graph[m["id"]] = targets
    return graph


def write_index(name, data, stdout=False):
    content = json.dumps(data, indent=2)
    if stdout:
        print(f"\n=== {name} ===")
        print(content)
    else:
        os.makedirs(INDEXES_DIR, exist_ok=True)
        path = os.path.join(INDEXES_DIR, f"{name}.json")
        with open(path, "w") as f:
            f.write(content)
        print(f"  wrote  {os.path.relpath(path, BASE)}")


def main():
    parser = argparse.ArgumentParser(description="Build probframe metadata indexes")
    parser.add_argument("--stdout", action="store_true", help="Print to stdout instead of writing files")
    parser.add_argument("--index", choices=["domains", "actors", "status", "degrade_graph"],
                        help="Build a specific index only")
    args = parser.parse_args()

    modules = scan_modules()
    print(f"Scanned {len(modules)} modules.")

    builders = {
        "domains": ("domain_index", build_domain_index),
        "actors": ("actor_index", build_actor_index),
        "status": ("status_index", build_status_index),
        "degrade_graph": ("degrade_graph", build_degrade_graph),
    }

    targets = [args.index] if args.index else list(builders.keys())
    for key in targets:
        filename, fn = builders[key]
        data = fn(modules)
        write_index(filename, data, stdout=args.stdout)

    if not args.stdout:
        print("Done.")


if __name__ == "__main__":
    main()
