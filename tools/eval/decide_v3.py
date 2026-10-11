#!/usr/bin/env python3
"""Does the candidate for pocket v3 ship? The rule was set by the coordinator before anyone had seen the candidate's numbers.

  python3 -I tools/eval/decide_v3.py --candidate alachua-pre2025-nc-tinyclip-39m-16 [--live val-tinyclip-39m-16] [--dir docs/eval] [--out docs/eval/decision-pocket-v3.json]

The candidate is the slot whose heads were fitted on the training photos under the licence rule `nc` (tools/eval/licences.py),
for TinyCLIP 39M/16, scored by tools/eval/shipped.py with --name-bar 0.92. It ships unless, on the test photos:
  (i)   its kind of eye on wildlife is worse than pocket v2's (the slot `val-tinyclip-39m-16`, docs/eval/shipped-val-tinyclip-39m-16.json,
        the same photos) by a paired difference whose 95% interval lies wholly below zero;
  (ii)  its kind of eye on the extra set's test photos is right for less than 96.5%;
  (iii) it names a species on more than 1% of the extra set's test photos of people and rooms (kinds `person` and `none`, together).
If it fails, the fallback is pocket v2 refitted under the same licence rule (`val-nc-tinyclip-39m-16`), and this file says so.
"""
import argparse, json, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ev

ap = argparse.ArgumentParser()
ap.add_argument("--candidate", required=True)
ap.add_argument("--live", default="val-tinyclip-39m-16")
ap.add_argument("--dir", default="docs/eval")
ap.add_argument("--out")
a = ap.parse_args()


def load(name):
    return json.load(open(os.path.join(a.dir, "shipped-%s.json" % name), encoding="utf-8"))


C, L = load(a.candidate), load(a.live)
pc, pl = C["per_photo"], L["per_photo"]
assert pc["wildlife"]["ids_sha256"] == pl["wildlife"]["ids_sha256"], "the two slots were scored on different wildlife photos"
bits = lambda s: np.frombuffer(s.encode(), dtype=np.uint8).astype(np.int8) - ord("0")
xc, xl = bits(pc["wildlife"]["kind_right"]), bits(pl["wildlife"]["kind_right"])
d = (xc - xl).astype(np.float32)
b = d[ev.boot_index(len(d))].mean(1)
lo, hi = np.percentile(b, [2.5, 97.5])
diff = [round(float(d.mean()), 4), round(float(lo), 4), round(float(hi), 4)]
fail_i = diff[2] < 0

kc = C["numbers"]["kind"]
extra_right = kc["test_extra"]["kind_right"]
fail_ii = extra_right[0] < 0.965

rows = {r["kind"]: r for r in kc["table_extra"]}
pr = [rows[k] for k in ("person", "none") if k in rows]
n_pr = sum(r["n"] for r in pr)
named_pr = sum(round(r["named"] * r["n"]) for r in pr)
share_pr = named_pr / n_pr if n_pr else None
fail_iii = share_pr is None or share_pr > 0.01

# reported beside the rule and deciding nothing: paired differences (candidate minus pocket v2) on the same photos
beside = []
for sname, keys in (("wildlife", ("asserted_right", "asserted_wrong", "named", "named_right")), ("extra", ("kind_right", "asserted_wrong", "named"))):
    if sname not in pc or sname not in pl or pc[sname]["ids_sha256"] != pl[sname]["ids_sha256"]:
        continue
    for key in keys:
        if key not in pc[sname] or key not in pl[sname]:
            continue
        va, vb = bits(pc[sname][key]), bits(pl[sname][key])
        dd = (va - vb).astype(np.float32)
        bb = dd[ev.boot_index(len(dd))].mean(1)
        l_, h_ = np.percentile(bb, [2.5, 97.5])
        beside.append({"photos": sname, "measure": key, "candidate": round(float(va.mean()), 4), "pocket_v2": round(float(vb.mean()), 4),
                       "difference": [round(float(dd.mean()), 4), round(float(l_), 4), round(float(h_), 4)], "n": int(len(dd))})
fails = [t for t, f in (("(i)", fail_i), ("(ii)", fail_ii), ("(iii)", fail_iii)) if f]
ships = not fails
nc, nl = C["numbers"], L["numbers"]
out = {
    "made_by": "tools/eval/decide_v3.py",
    "rule": "The candidate (heads fitted on the training photos under the licence rule nc, TinyCLIP 39M/16, name_at at the 92-in-100 level on val) ships unless, on the test photos, "
            "(i) its kind of eye on wildlife is worse than pocket v2's by a paired difference whose 95% interval lies wholly below zero, (ii) its kind of eye on the extra set's test photos is right for less than 96.5%, "
            "or (iii) it names a species on more than 1% of the test photos of people and rooms. The rule was set by the coordinator before the candidate was measured.",
    "candidate": a.candidate, "pocket_v2": a.live,
    "tests": {
        "i_wildlife_kind_paired_difference": {"candidate": nc["kind_right"], "pocket_v2": nl["kind_right"], "difference": diff, "photos": int(len(d)), "fails": bool(fail_i)},
        "ii_extra_kind_right": {"candidate": extra_right, "bar": 0.965, "fails": bool(fail_ii)},
        "iii_named_on_people_and_rooms": {"photos": n_pr, "named": named_pr, "share": share_pr, "by_kind": {r["kind"]: {"n": r["n"], "named": r["named"]} for r in pr}, "bar": 0.01, "fails": bool(fail_iii)},
    },
    "beside": beside,
    "fails": fails, "ships": ships,
    "slot": a.candidate if ships else None,
    "why": ("The candidate passes all three tests, so it ships as pocket v3." if ships else
            "The candidate fails test %s, so the fallback (pocket v2 refitted under the licence rule) is the slot to consider." % " and ".join(fails)),
}
ev.write_json(a.out or os.path.join(a.dir, "decision-pocket-v3.json"), out)
print(json.dumps(out["tests"], indent=1))
print(out["why"])
