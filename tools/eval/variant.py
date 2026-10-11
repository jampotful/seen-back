#!/usr/bin/env python3
"""Score a slot on another set of vectors of some evaluation photos, beside the original model's vectors of the same photos.

  python3 -I tools/eval/variant.py <root> <slot dir> --vectors <file.f16.npy> --ids <file.ids.json> --name <label>
        [--name-at 0.78] [--offer-at 0.66] [--out docs/eval/variant-<label>.json]

Made for the larger model's int8 file as the browser's WASM runtime computes it: the laboratory returns its vectors for
a few hundred test photos. Both sets of vectors go through tools/fusion/fuse.py with the slot's own files and the same
settings, photo by photo, so every difference is paired. Only test photos are scored. No setting is tuned here: with
no `val` photo among the vectors, a threshold cannot be set again, so the script reports whether the slot's thresholds
still do on the new vectors what they did on the original ones.
"""
import argparse, copy, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "fusion"))
import ev
import fuse as F

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("slot")
ap.add_argument("--vectors", required=True)
ap.add_argument("--ids", required=True)
ap.add_argument("--name", required=True)
ap.add_argument("--name-at", type=float)
ap.add_argument("--offer-at", type=float)
ap.add_argument("--source", default="", help="where the vectors came from, for the record")
ap.add_argument("--slot-name", help="the slot's name in the report (default: the directory's name)")
ap.add_argument("--out")
a = ap.parse_args()

slot = F.load_slot(a.slot)
man, table = copy.deepcopy(slot["manifest"]), slot["table"]
if a.name_at is not None:
    man["fusion"]["name_at"] = a.name_at
if a.offer_at is not None:
    man["fusion"]["offer_at"] = a.offer_at
model = man["evaluation"]["model"]
V = ev.unit(np.load(a.vectors, allow_pickle=False))
vid = ev.read_ids(a.ids)
E0, ids0 = ev.load_images(a.root, model)
pos = {i: k for k, i in enumerate(ids0)}
assert len(vid) == len(V) and all(i in pos for i in vid), "the ids do not line up with the vectors or the manifest"
ES = ev.EvalSet(a.root, vid)
keys = json.load(open(os.path.join(a.slot, man["species"]["table"]), encoding="utf-8"))["keys"]
k2row = {k: i for i, k in enumerate(keys)}
sci_of = [r[0] for r in table]
sel = np.nonzero(ES.test)[0]
truth = [sci_of[k2row[int(ES.rows[i]["key"])]] if int(ES.rows[i]["key"]) in k2row else None for i in sel]
eyes = ES.eyes[sel]


def score(X):
    X = X.astype(np.float64)
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    kd, sd = X @ slot["kinds"].T, X @ slot["species"].T
    res = [F.fuse(man, table, int(ES.month[i]), kd[j], sd[j], kind_bias=slot["kind_bias"], species_bias=slot["species_bias"]) for j, i in enumerate(sel)]
    return {"kind_right": np.array([r["kind"] == e for r, e in zip(res, eyes)]),
            "top1": np.array([r["species"][0]["sci"] == t for r, t in zip(res, truth)]),
            "top5": np.array([any(s["sci"] == t for s in r["species"]) for r, t in zip(res, truth)]),
            "named": np.array([r["named"] is not None for r in res]),
            "named_right": np.array([r["named"] is not None and r["named"]["sci"] == t for r, t in zip(res, truth)]),
            "offered": np.array([len(r["offers"]) > 0 for r in res]),
            "offer_holds": np.array([any(o["sci"] == t for o in r["offers"]) for r, t in zip(res, truth)]),
            "top_sci": np.array([r["species"][0]["sci"] for r in res]), "top_p": np.array([r["species"][0]["p"] for r in res])}


new, old = score(V[sel]), score(E0[[pos[vid[i]] for i in sel]])
cos = (V[sel] * E0[[pos[vid[i]] for i in sel]]).sum(1)


def side(r):
    return {"kind_right": ev.ci(r["kind_right"]), "species_top1": ev.ci(r["top1"]), "species_top5": ev.ci(r["top5"]), "named": ev.ci(r["named"]), "named_right": ev.ci(r["named_right"][r["named"]]),
            "offered": ev.ci(r["offered"]), "offered_holds_species": ev.ci(r["offer_holds"][r["offered"]]), "kind_only": ev.ci(~r["named"] & ~r["offered"])}


def diff(k):
    d = new[k].astype(np.float32) - old[k].astype(np.float32)
    b = d[ev.boot_index(len(d))].mean(1)
    lo, hi = np.percentile(b, [2.5, 97.5])
    return [round(float(d.mean()), 4), round(float(lo), 4), round(float(hi), 4), int(len(d))]


f = man["fusion"]
out = {"made_by": "tools/eval/variant.py", "name": a.name, "slot": a.slot_name or os.path.basename(os.path.normpath(a.slot)), "model": model, "vectors": a.source or os.path.basename(a.vectors),
       "test_photos": int(len(sel)), "photos_left_out_because_they_are_val": int(len(vid) - len(sel)), "fusion": f,
       "cosine_to_original": {"mean": round(float(cos.mean()), 4), "p01": round(float(np.percentile(cos, 1)), 4), "min": round(float(cos.min()), 4)},
       "original": side(old), "variant": side(new),
       "paired_difference": {k: diff(k) for k in ("kind_right", "top1", "top5", "named", "named_right")},
       "same_top_species": ev.ci(new["top_sci"] == old["top_sci"]),
       "top_probability_mean_absolute_change": round(float(np.abs(new["top_p"] - old["top_p"]).mean()), 4),
       "photos_named_by_one_and_not_the_other": int((new["named"] != old["named"]).sum())}
pc = lambda v: "–" if not v or v[0] is None else "%.1f%% (%.1f to %.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])
pt = lambda v: "%+.1f (%+.1f to %+.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])
out["text"] = ("%d test photos, the slot `%s` with name_at %g and offer_at %g, every photo through `fuse.py` twice: with the original model's vectors and with the vectors `%s`. The two vectors of a photo have a mean cosine of %.4f (1st percentile %.4f). "
               "Top species right: %s with the original vectors and %s with these, a paired difference of %s points; first five: %s and %s. Kind of eye right: %s and %s. A species is named for %s and %s of the photos, and that name is right for %s and %s. "
               "The top species is the same for %s of the photos; the top probability moves by %.3f on average, and %d photos are named under one set of vectors and left unnamed under the other." % (
                   len(sel), out["slot"], f["name_at"], f["offer_at"], out["vectors"], out["cosine_to_original"]["mean"], out["cosine_to_original"]["p01"],
                   pc(out["original"]["species_top1"]), pc(out["variant"]["species_top1"]), pt(out["paired_difference"]["top1"]), pc(out["original"]["species_top5"]), pc(out["variant"]["species_top5"]),
                   pc(out["original"]["kind_right"]), pc(out["variant"]["kind_right"]), pc(out["original"]["named"]), pc(out["variant"]["named"]), pc(out["original"]["named_right"]), pc(out["variant"]["named_right"]),
                   pc(out["same_top_species"]), out["top_probability_mean_absolute_change"], out["photos_named_by_one_and_not_the_other"]))
print(out["text"])
ev.write_json(a.out or "docs/eval/variant-%s.json" % a.name, out)
