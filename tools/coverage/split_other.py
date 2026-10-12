#!/usr/bin/env python3
"""Pilot: what splitting `other` into new groups does to the pocket model's group decision, on Alachua photos.

Fits the kinds head the way pocket v3 was fitted (logistic regression, C=20, a kind's photos weighted by the inverse
square root of their number, licence rule `nc`, the Alachua training photos plus the fitting part of the COCO extra
set), once with the seventeen labels of today and once with `other` split into proposed groups. Scores both on the
same test photos (Alachua 2025 test split, original and WASM int8 vectors; COCO test rows) with the head alone, the way
the page would decide outside Alachua, where no county list can help. Intervals: 2000 bootstrap resamples, seed 20261011.

Usage: python3 -I tools/coverage/split_other.py DIR . OUT_JSON
DIR holds data/train/alachua-pre2025/manifest.csv, data/eval/alachua-2025/manifest.csv, data/extra/coco-kinds/manifest.csv and
data/regions/us-fl-alachua/species.json (from branch pub/data-alachua), and vec/images/<set>.f16.npy with <set>.ids.json for
alachua-pre2025, alachua-2025, alachua-2025.wasm-int8-per-channel, coco-kinds and coco-kinds.wasm-int8-per-channel (from branch
pub/lab-tinyclip-39m-16). POWER (environment, default 0.5) weights a group's photos by their number to the power -POWER.
"""
import csv, hashlib, json, sys, os
from collections import Counter, defaultdict
import numpy as np
from sklearn.linear_model import LogisticRegression

P, REPO, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, os.path.join(REPO, "tools", "species"))
sys.path.insert(0, os.path.join(REPO, "tools", "eval"))
import views_todo, licences  # noqa: E402

POWER = float(os.environ.get("POWER", "0.5"))
rng = np.random.default_rng(20261011)


def unit(x):
    x = np.asarray(x, np.float32)
    return x / np.maximum(np.linalg.norm(x, axis=1, keepdims=True), 1e-12)


def load(name):
    X = unit(np.load(os.path.join(P, "vec", "images", name + ".f16.npy")))
    ids = json.load(open(os.path.join(P, "vec", "images", name + ".ids.json")))
    if isinstance(ids, dict):
        ids = ids.get("ids", ids)
    return X, list(ids)


def manifest(rel):
    return {r["id"]: r for r in csv.DictReader(open(os.path.join(P, "data", rel, "manifest.csv"), newline="", encoding="utf-8"))}


species = {s["key"]: s for s in json.load(open(os.path.join(P, "data", "regions", "us-fl-alachua", "species.json")))["species"]}

# ---- the proposed groups for taxa now in `other`
SPLITS = {"Salticidae": "jumping spider", "Pteropodidae": "flying fox"}
MERGE = {  # proposed view (views_todo) -> class used here
    "spider": "spider", "fungus and lichen": "fungus", "slime mould": "fungus", "fish": "fish",
    "snail and slug": "snail", "raccoon, bear, otter, weasel and other carnivore": "mammal",
    "opossum, kangaroo and other marsupial": "mammal", "pig, hippo, rhino, tapir and other hoofed mammal": "mammal",
    "mole, shrew and hedgehog": "mammal", "armadillo, sloth, anteater and pangolin": "mammal", "monkey and ape": "mammal",
    "manatee and dugong": "mammal", "bat": "bat", "millipede and centipede": "millipede",
    "salamander, newt and caecilian": "salamander", "crab, crayfish, shrimp and lobster": "crustacean",
    "woodlouse and small crustacean": "crustacean", "tick and mite": "tick", "clam, mussel and scallop": "shellfish",
    "harvestman and other arachnid": "harvestman", "scorpion": "harvestman",
    "earthworm, leech and bristle worm": "worm", "flatworm, roundworm and other worm": "worm",
    "springtail": "springtail",
}


def group_of(key, row):
    s = species.get(int(key)) if key else None
    if s is None:
        s = {"kingdom": row.get("kingdom", ""), "phylum": "", "class": row.get("class", ""), "order": row.get("order", ""), "family": row.get("family", "")}
    fam = s.get("family") or ""
    if fam in SPLITS:
        return SPLITS[fam]
    if (s.get("order") or "") == "Ixodida":
        return "tick"
    v = views_todo.view(s.get("kingdom") or "", s.get("phylum") or "", s.get("class") or "", s.get("order") or "", fam)
    if (s.get("order") or "") in ("Trombidiformes", "Mesostigmata", "Sarcoptiformes"):
        return "other"  # mites stay in `other` (the tick sheet: gall mites and eyed predatory mites cannot share the tick's view)
    return MERGE.get(v, "other")


def labels_for(rows, split_other):
    out = []
    for r in rows:
        e = r["eyes"]
        if e == "other" and split_other:
            e = group_of(r.get("key"), r)
        out.append(e)
    return np.array(out)


def part_of(row):
    if row["split"] == "test":
        return "test"
    return "fit" if int(hashlib.sha256(row["id"].encode()).hexdigest()[:8], 16) % 3 < 2 else "tune"


tr_man, ev_man, co_man = manifest("train/alachua-pre2025"), manifest("eval/alachua-2025"), manifest("extra/coco-kinds")
Xtr, idtr = load("alachua-pre2025")
Xev, idev = load("alachua-2025")
Xevw, idevw = load("alachua-2025.wasm-int8-per-channel")
Xco, idco = load("coco-kinds")
Xcow, idcow = load("coco-kinds.wasm-int8-per-channel")

tr_rows = [tr_man[i] for i in idtr]
keep_tr = np.array([licences.allowed(r["licence"], "nc") for r in tr_rows])
co_rows = [co_man[i] for i in idco]
co_part = np.array([part_of(r) for r in co_rows])
keep_co = np.array([licences.allowed(r["licence"], "nc") for r in co_rows]) & (co_part == "fit")
ev_rows = [ev_man[i] for i in idev]
ev_test = np.array([r["split"] == "test" for r in ev_rows])
ev_val = ~ev_test


def fit(split_other):
    ytr = labels_for(tr_rows, split_other)
    yco = np.array([r["eyes"] for r in co_rows])
    X = np.concatenate([Xtr[keep_tr], Xco[keep_co]])
    y = np.concatenate([ytr[keep_tr], yco[keep_co]])
    cls, cnt = np.unique(y, return_counts=True)
    sw = (cnt.astype(np.float64) ** -POWER)[np.searchsorted(cls, y)]
    sw *= len(y) / sw.sum()
    clf = LogisticRegression(C=20.0, max_iter=400).fit(X, y, sample_weight=sw)
    return clf, dict(zip(cls.tolist(), cnt.tolist()))


def boot(x, B=2000):
    x = np.asarray(x, np.float64)
    if len(x) == 0:
        return [None, None, None, 0]
    idx = rng.integers(0, len(x), size=(B, len(x)))
    b = x[idx].mean(1)
    return [float(x.mean()), float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5)), int(len(x))]


res = {"notes": "head alone, no county list; licence rule nc; logistic regression C=20; a group's photos weighted by their number to the power -%g" % POWER}
heads = {}
for name, so in (("today", False), ("split", True)):
    clf, counts = fit(so)
    heads[name] = clf
    res[name + "_fit_counts"] = counts

# truth on test photos, in both label sets
ev_rows_t = [r for r, t in zip(ev_rows, ev_test) if t]
truth_old = np.array([r["eyes"] for r in ev_rows_t])
truth_new = labels_for(ev_rows_t, True)
OLD = [k for k in ("cat", "dog", "squirrel", "deer", "rabbit", "hawk", "wader", "bird", "alligator", "reptile", "frog", "bee", "insect", "plant") if (truth_old == k).any()]

for vecname, Xe, ide in (("original", Xev, idev), ("wasm-int8", Xevw, idevw)):
    pos = {i: n for n, i in enumerate(ide)}
    sel = [pos[r["id"]] for r in ev_rows_t if r["id"] in pos]
    have = np.array([r["id"] in pos for r in ev_rows_t])
    Xt = Xe[sel]
    to, tn = truth_old[have], truth_new[have]
    p_old = heads["today"].predict(Xt)
    p_new = heads["split"].predict(Xt)
    r_old, r_new = (p_old == to), (p_new == tn)
    oldmask = np.isin(to, OLD)
    # a photo of an old kind counts as right under `split` when it is called its own kind
    d = (p_new[oldmask] == to[oldmask]).astype(float) - (p_old[oldmask] == to[oldmask]).astype(float)
    out = {"photos": int(have.sum()),
           "all_right_today": boot(r_old), "all_right_split": boot(r_new),
           "old_kinds_right_today": boot(p_old[oldmask] == to[oldmask]), "old_kinds_right_split": boot(p_new[oldmask] == to[oldmask]),
           "old_kinds_paired_difference": boot(d),
           "other_photos": int((to == "other").sum()),
           "other_right_today (called other)": boot(p_old[to == "other"] == "other"),
           "other_right_split (called its own new group)": boot(p_new[to == "other"] == tn[to == "other"]),
           "other_called_an_old_kind_today": boot(np.isin(p_old[to == "other"], OLD)),
           "other_called_an_old_kind_split": boot(np.isin(p_new[to == "other"], OLD)),
           "by_old_kind": {}, "by_new_group": {}, "confusions_split": {}}
    for k in OLD:
        m = to == k
        out["by_old_kind"][k] = {"n": int(m.sum()), "today": float((p_old[m] == k).mean()), "split": float((p_new[m] == k).mean()),
                                 "split_called_a_new_group": float((~np.isin(p_new[m], OLD + ["person", "none"])).mean())}
    for g in sorted(set(tn[to == "other"].tolist())):
        m = tn == g
        said = Counter(p_new[m].tolist()).most_common(3)
        prec_m = p_new == g
        out["by_new_group"][g] = {"n": int(m.sum()), "recall": float((p_new[m] == g).mean()),
                                  "precision": (float((tn[prec_m] == g).mean()) if prec_m.any() else None),
                                  "said": said}
    conf = Counter((t, p) for t, p in zip(tn, p_new) if t != p)
    out["confusions_split"] = [[a, b, n] for (a, b), n in conf.most_common(25)]
    res["test_" + vecname] = out

# COCO test rows (people, rooms, pets, livestock)
for vecname, Xc, idc in (("original", Xco, idco), ("wasm-int8", Xcow, idcow)):
    rows = [co_man[i] for i in idc]
    t = np.array([r["split"] == "test" for r in rows])
    y = np.array([r["eyes"] for r in rows])[t]
    Xt = Xc[t]
    po, pn = heads["today"].predict(Xt), heads["split"].predict(Xt)
    res["coco_test_" + vecname] = {"photos": int(t.sum()), "by_kind": {k: {"n": int((y == k).sum()), "today": float((po[y == k] == k).mean()), "split": float((pn[y == k] == k).mean())} for k in sorted(set(y.tolist()))},
                                   "mean_over_kinds_today": float(np.mean([(po[y == k] == k).mean() for k in set(y.tolist())])),
                                   "mean_over_kinds_split": float(np.mean([(pn[y == k] == k).mean() for k in set(y.tolist())])),
                                   "split_said_a_new_group": float((~np.isin(pn, OLD + ["person", "none", "other"])).mean())}

# the size of each head, as the page would store it (float16 rows of 512 plus a bias)
for name, clf in heads.items():
    res["head_bytes_" + name] = int(clf.coef_.shape[0] * (clf.coef_.shape[1] * 2 + 4))
    res["labels_" + name] = clf.classes_.tolist()
json.dump(res, open(OUT, "w"), indent=1)
print(json.dumps({k: v for k, v in res.items() if not k.startswith("test_") and not k.startswith("coco")}, indent=1)[:3000])
for k in ("test_original", "test_wasm-int8"):
    o = res[k]
    print(k, "photos", o["photos"], "old kinds today %.4f split %.4f diff %s" % (o["old_kinds_right_today"][0], o["old_kinds_right_split"][0], [round(x, 4) for x in o["old_kinds_paired_difference"][:3]]))
    print("  other: today called other %.4f | split own group %.4f | called an old kind today %.4f split %.4f (n=%d)" % (o["other_right_today (called other)"][0], o["other_right_split (called its own new group)"][0], o["other_called_an_old_kind_today"][0], o["other_called_an_old_kind_split"][0], o["other_photos"]))
    for g, v in o["by_new_group"].items():
        print("   %-16s n=%3d recall %.3f precision %s said %s" % (g, v["n"], v["recall"], None if v["precision"] is None else round(v["precision"], 3), v["said"]))
    for kk, v in o["by_old_kind"].items():
        print("   old %-10s n=%4d today %.3f split %.3f" % (kk, v["n"], v["today"], v["split"]))
for k in ("coco_test_original", "coco_test_wasm-int8"):
    print(k, json.dumps(res[k])[:600])
