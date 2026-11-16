#!/usr/bin/env python3
"""route: task-keyword traversal of the SEO-CORE technique catalog.

Parses SEO-CORE.md technique tables (| T1 | name | why | under pillar
headings) and emits the techniques whose name/why match the task.
Same contract as pattern-standards' route.py: deterministic, one call,
no prose archaeology.

Usage:
  route.py --task "migrating a site to a new domain"
  route.py --pillar T
  route.py --list

Exit 0 with matches; exit 1 with candidates when nothing scores (the
task is then a strategy question, not a technique lookup).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

DEFAULT_CORE = Path(__file__).resolve().parent.parent / "SEO-CORE.md"
PILLAR_ORDER = ["T", "C", "G", "A", "S", "M", "R"]


def parse_core(path: Path) -> dict[str, list[dict]]:
    """pillar letter -> [{id, name, why}] from technique tables."""
    out: dict[str, list[dict]] = {}
    pillar = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## ([TCGASMR]): ", line)
        if m:
            pillar = m.group(1)
            out.setdefault(pillar, [])
            continue
        m = re.match(r"^\| ([TCGASMR]\d+) \| (.+?) \| (.+?) \|", line)
        if m and pillar:
            out[pillar].append({"id": m.group(1), "name": m.group(2), "why": m.group(3)})
    return out


def match(items: list[dict], task: str) -> list[dict]:
    words = set(re.findall(r"[a-z0-9]+", task.lower()))
    hits = []
    for it in items:
        text = " ".join(re.findall(r"[a-z0-9]+", (it["name"] + " " + it["why"]).lower()))
        toks = set(text.split())
        score = sum(1 for w in words if any(
            w == t or (len(w) >= 4 and len(t) >= 4 and (w.startswith(t) or t.startswith(w)))
            for t in toks))
        if score:
            hits.append((score, it))
    hits.sort(key=lambda x: (-x[0], x[1]["id"]))
    return [it for s, it in hits]


def main() -> int:
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--task")
    ap.add_argument("--pillar", choices=PILLAR_ORDER)
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--core", default=str(DEFAULT_CORE))
    a = ap.parse_args()
    core = Path(a.core)
    if not core.is_file():
        print(f"route: SEO-CORE not found: {core}", file=sys.stderr)
        return 2
    cat = parse_core(core)
    total = sum(len(v) for v in cat.values())
    if a.list or a.pillar:
        for p in PILLAR_ORDER:
            if a.pillar and p != a.pillar:
                continue
            for it in cat.get(p, []):
                print(f"{it['id']}  {it['name']}")
        return 0
    if not a.task:
        ap.print_help(file=sys.stderr)
        return 2
    hits: list[dict] = []
    seen: set[str] = set()
    for p in PILLAR_ORDER:
        for it in match(cat.get(p, []), a.task):
            if it["id"] not in seen:
                seen.add(it["id"])
                hits.append(it)
    if not hits:
        print(f"route: no technique match for {a.task!r}; this is a strategy question.")
        print("Audit order reminder: T -> C -> G -> A -> S -> M -> R (technical failures mask everything).")
        return 1
    cap = 12
    print(f"{len(hits)} technique(s) for {a.task!r} (audit order T->C->G->A->S->M->R"
          + (f"; showing top {cap}, narrow with --pillar" if len(hits) > cap else "") + "):")
    for it in hits[:cap]:
        print(f"  {it['id']}  {it['name']}")
        print(f"        why: {it['why']}")
    print("Deep practice: references/<pillar>.md; refusals: SEO-CORE risk pillar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
