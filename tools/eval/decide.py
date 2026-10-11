#!/usr/bin/env python3
"""Which pocket model ships: TinyCLIP 39M/16 or TinyCLIP 8M/16. The rule was written before the trained heads were measured.

  python3 -I tools/eval/decide.py [--dir docs/eval] [--out docs/eval/decision-pocket.json]

It reads the two models' as-shipped results (docs/eval/shipped-<train>-<model>.json, written by tools/eval/shipped.py
through tools/fusion/fuse.py) for the best kind of slot that exists for both: heads fitted on the training photos
(`alachua-pre2025`) when they have been measured, sentence rows (`sentences`) until then. Both slots were scored on the
same photos in the same order, so every difference is paired, with a 95% interval from a bootstrap over photos.

The rule. The pocket model's first job is the kind of eye, for wildlife and for people, pets and rooms alike. The
measure is the share of test photos whose kind the page would get right, averaged over the wildlife test photos and
the extra set's test photos (wildlife alone while either model's vectors of the extra set are missing). TinyCLIP 8M/16
is a quarter of the download and about a third of the time a photo, so it ships unless TinyCLIP 39M/16 is ahead on that
measure by a paired difference whose interval lies wholly above zero. The share of photos that get a right species
name, and the share whose kind is asserted and wrong, are reported beside it and do not decide.
"""
import argparse, json, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ev

BIG, SMALL = "tinyclip-39m-16", "tinyclip-8m-16"
ap = argparse.ArgumentParser()
ap.add_argument("--dir", default="docs/eval")
ap.add_argument("--out")
a = ap.parse_args()


def load(train, model):
    p = os.path.join(a.dir, "shipped-%s-%s.json" % (train, model))
    if not os.path.exists(p):
        return None
    d = json.load(open(p, encoding="utf-8"))
    return d if d.get("per_photo") else None


def bits(s):
    return np.frombuffer(s.encode(), dtype=np.uint8) - ord("0")


def paired(x, y):
    """Mean of x - y over photos with a bootstrap interval, and the resampled means (for averaging over two sets)."""
    d = x.astype(np.float32) - y.astype(np.float32)
    b = d[ev.boot_index(len(d))].mean(1)
    return float(d.mean()), b


def iv(mean, b):
    lo, hi = np.percentile(b, [2.5, 97.5])
    return [round(mean, 4), round(float(lo), 4), round(float(hi), 4)]


train = next((t for t in ("alachua-pre2025", "sentences") if load(t, BIG) and load(t, SMALL)), None)
if train is None:
    print("no pair of as-shipped results with per-photo outcomes for both pocket models; nothing decided")
    raise SystemExit(0)
A, B = load(train, BIG), load(train, SMALL)
pa, pb = A["per_photo"], B["per_photo"]
assert pa["wildlife"]["ids_sha256"] == pb["wildlife"]["ids_sha256"], "the two slots were scored on different wildlife photos"
sets = ["wildlife"]
if "extra" in pa and "extra" in pb and pa["extra"]["ids_sha256"] == pb["extra"]["ids_sha256"]:
    sets.append("extra")
measures, kind_parts = [], []
for sname in sets:
    xa, xb = pa[sname], pb[sname]
    for key, label in (("kind_right", "kind of eye right"), ("asserted_right", "kind asserted and right"), ("asserted_wrong", "kind asserted and wrong"), ("named_right", "a right species name shown"), ("named", "a species name shown")):
        if key not in xa or key not in xb:
            continue
        va, vb = bits(xa[key]), bits(xb[key])
        m, b = paired(va, vb)
        measures.append({"photos": sname, "measure": label, BIG: round(float(va.mean()), 4), SMALL: round(float(vb.mean()), 4), "difference": iv(m, b), "n": int(len(va))})
        if key == "kind_right":
            kind_parts.append((m, b))
m = float(np.mean([p[0] for p in kind_parts]))
b = np.mean([p[1] for p in kind_parts], axis=0)
deciding = iv(m, b)
ahead = deciding[1] > 0
choice = BIG if ahead else SMALL
what = "the mean of the share right on the wildlife test photos and on the extra set's test photos" if len(sets) == 2 else "the share right on the wildlife test photos (the extra set's vectors were not published for both models)"
out = {"made_by": "tools/eval/decide.py", "slots_compared": {BIG: "%s-%s" % (train, BIG), SMALL: "%s-%s" % (train, SMALL)}, "train": train, "sets": sets,
       "rule": "TinyCLIP 8M/16 ships unless TinyCLIP 39M/16 is ahead on the kind of eye, as the page would decide it, by a paired difference whose 95%% interval lies wholly above zero. The measure is %s." % what,
       "deciding_difference": deciding, "measures": measures, "choice": choice, "slot": "%s-%s" % (train, choice), "branch": "pub/heads-%s-%s" % (train, choice),
       "provisional": train != "alachua-pre2025" or len(sets) < 2,
       "why": ("On %s, TinyCLIP 39M/16 is ahead of TinyCLIP 8M/16 by %+.1f points (%+.1f to %+.1f), paired over the same photos. %s" % (
           what, 100 * deciding[0], 100 * deciding[1], 100 * deciding[2],
           "The interval lies above zero, so the larger pocket model ships: a wrong kind gives a person the wrong eyes, and that weighs more than 31 MB downloaded once." if ahead else
           "The interval reaches zero, so the smaller model ships: it is a quarter of the download and about a third of the time a photo."))}
ev.write_json(a.out or os.path.join(a.dir, "decision-pocket.json"), out)
print(out["why"])
print("choice:", choice, "| slot branch:", out["branch"], "| provisional:", out["provisional"])
