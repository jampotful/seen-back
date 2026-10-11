#!/usr/bin/env python3
"""Compare the numbers in two directories of the studies' JSON files, such as a rerun against the committed files.

  python3 -I tools/eval/compare.py <dir a> <dir b> [--tolerance 0.0005]

For every JSON file present in both it walks the two trees and counts the numbers compared, those that differ by more
than the tolerance, and the largest difference. Run times and the list of inputs are left out. Text is compared only
where it holds no number. The exit code is 0 either way; the output is the result.
"""
import argparse, json, os

ap = argparse.ArgumentParser()
ap.add_argument("a")
ap.add_argument("b")
ap.add_argument("--tolerance", type=float, default=0.0005)
A = ap.parse_args()
SKIP = {"seconds", "inputs", "text", "what", "settings_text", "saved_head", "fusion_note", "fusion_thresholds_note", "right", "detail"}


def walk(x, y, path, out):
    if isinstance(x, dict) and isinstance(y, dict):
        for k in sorted(set(x) | set(y)):
            if k in SKIP:
                continue
            if k not in x or k not in y:
                out["missing"].append(path + "/" + k)
            else:
                walk(x[k], y[k], path + "/" + k, out)
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            out["missing"].append(path + " (lists of %d and %d)" % (len(x), len(y)))
        for i, (p, q) in enumerate(zip(x, y)):
            walk(p, q, "%s[%d]" % (path, i), out)
    elif isinstance(x, bool) or isinstance(y, bool) or x is None or y is None or isinstance(x, str) or isinstance(y, str):
        out["other"] += 1
        if x != y:
            out["other_differ"].append("%s: %r | %r" % (path, x, y))
    else:
        out["numbers"] += 1
        d = abs(float(x) - float(y))
        out["largest"] = max(out["largest"], d)
        if d > A.tolerance:
            out["differ"].append("%s: %r | %r" % (path, x, y))


total = 0
for name in sorted(os.listdir(A.a)):
    if not name.endswith(".json"):
        continue
    if not os.path.exists(os.path.join(A.b, name)):
        print("%-36s only in %s" % (name, A.a))
        continue
    out = {"numbers": 0, "largest": 0.0, "differ": [], "missing": [], "other": 0, "other_differ": []}
    walk(json.load(open(os.path.join(A.a, name), encoding="utf-8")), json.load(open(os.path.join(A.b, name), encoding="utf-8")), "", out)
    total += len(out["differ"])
    print("%-36s %6d numbers compared, %d differ by more than %g, largest difference %.6f; %d other values, %d differ; %d keys on one side only" % (
        name, out["numbers"], len(out["differ"]), A.tolerance, out["largest"], out["other"], len(out["other_differ"]), len(out["missing"])))
    for line in (out["differ"] + out["other_differ"] + out["missing"])[:12]:
        print("    " + line[:300])
for name in sorted(os.listdir(A.b)):
    if name.endswith(".json") and not os.path.exists(os.path.join(A.a, name)):
        print("%-36s only in %s" % (name, A.b))
print("numbers that differ by more than the tolerance, all files:", total)
