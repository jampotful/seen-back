#!/usr/bin/env python3
"""Fit the pocket model's group head on the world photos, choose its settings on the tuning photos, and score it against
the pass marks of docs/COVERAGE.md on the test photos, beside the head the page ships today.

The head is the same kind of head as the shipped one (tools/eval/study2.py): logistic regression with C = 20 on an
encoder's unit image vectors from the original model, fitted on photos allowed by the licence rule `nc`, a photo
weighted by its group's count to the power -`power` and by the weight of its set (--alachua-weight, --coco-weight).
Its labels are the seventeen of today's head followed by the groups of GROUPS in src/cam.a.js, one row of the
encoder's width each (1,024 bytes in half precision for a width of 512).

The encoder is a setting: --model names a laboratory model (tinyclip-39m-16, the page's encoder today, or another
whose vectors are published on pub/lab-<model>, such as bioclip-b16). Today's page is always scored as it runs
today: the slot given by --slot on TinyCLIP 39M/16's vectors from the phone's WASM runtime, on the same photos as
the new head. With an encoder other than the slot's, the county species list needs rows of that encoder's: they are
fitted here as the shipped ones were (the discriminant head of tools/eval/study2.py on the Alachua training photos,
its shrinkage, prior weight and scale chosen on the Alachua tuning photos) for the same species and the same monthly
weights.

Photos (ROOT is laid out as tools/eval/fetch.py lays it out, with pub/data-world in ROOT/world and each model's
vectors in ROOT/lab/<model>/images):
  fitting   the world photos (`fit`, dated through 2024), the COCO extra set's fit part, and with --with-alachua the
            Alachua training photos too, each labelled by tools/world/groups.py from GBIF's ranks in the county list;
            the original model's vectors
  tuning    the world `tune` photos, the Alachua `val` photos and the COCO `tune` part; the world and Alachua photos
            through the vectors the phone's WASM runtime computes where the laboratory has made them for the model
            (--vectors), the COCO photos through the original model's
  test      the world `test` photos, the Alachua `test` photos and the COCO `test` rows, WASM vectors where made; they
            choose nothing, and they are not loaded until every setting is fixed

The page is scored as it runs from build 22: in the county's time zone the head is combined with the county species
list by the rule `mix` (tools/fusion/fuse.py, src/cam.rec.js), the list's species relabelled to the groups carried
where the county list files them under `other`; elsewhere the head answers alone. So the world photos are scored by
the head alone, the Alachua photos with the list, and the COCO photos both ways. Today's page is scored as it runs
today, with the list everywhere. A vectorized copy of the rule is checked against fuse.py on tuning photos before use.

Two recipes (--recipe), every choice made on the tuning photos:
  fold   (head runs 2 and 3) (1) the fitting recipe, with or without the Alachua photos and the power, every group
         carried; (2) the groups carried: each must be named for 75% of its world tuning photos and be right for 75% of
         the photos it is called for, and the worst failing group is put back in `other` and the head refitted until
         every group carried passes (docs/COVERAGE.md: "a group that fails stays in `other` until it passes");
         (3) t_kind and w_kind for the county, the most Alachua photos right with the COCO photos within 1 point of
         today's page.
  merge  (the merge trial of tools/world/EXPERIMENTS.md) one head with a row for every group, fitted once (power 0,
         Alachua rows weighted 3 and COCO rows 10); per-group bias offsets calibrated on the world tuning photos
         (coordinate ascent on the sum over the groups of the smaller of named and right when called, the head
         alone); then the worst failing group's row is merged into `other`, its probability added to other's with no
         refit, until every group still named passes; then t_kind and w_kind on the grid {0.5, 1, 2} x {0.5, 0.7, 0.9,
         1.0}, the most Alachua photos of the old kinds right with the COCO photos within 1 point of today's page (both
         with the list); the fold is checked again at the chosen t_kind. A merged row keeps its numbers and is labelled
         `other` in the slot: rows that share a label are one kind, their probabilities added (tools/fusion/fuse.py).
Both end with kind_at, the level from which asserted kinds are right 95 times in 100 on each tuning set. The test
photos are then read once. A group carried that fails on them is put back too (refitted for fold, merged for merge),
the settings chosen again on the tuning photos, and the test photos read a second time; both readings are kept.

Usage: python3 -I tools/world/head.py ROOT --slot models/pocket --out OUT [--recipe fold|merge] [--model M] [...]
Writes OUT/report.json, OUT/REPORT.md and, for the chosen head, OUT/slot/ (kinds.f16.bin, manifest.json and
species.json relabelled, the species rows when they were fitted here) with OUT/slot/fitted_on.csv. --tune-only stops
before the test photos are loaded (for trying the code), and writes the report of the tuning photos only.
"""
import argparse
import csv
import hashlib
import json
import os
import sys
import time
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "fusion"))
from groups import group_of, NEW  # noqa: E402
import fuse as F  # noqa: E402

TODAY = "tinyclip-39m-16"        # the encoder of today's page; today's answers always come from its slot and its WASM vectors
MODEL = TODAY                    # the encoder of the new head (--model)
WASM = ".wasm-int8-per-channel"
OLD = ["cat", "dog", "squirrel", "deer", "rabbit", "hawk", "wader", "bird", "alligator", "reptile", "frog", "bee", "insect",
       "plant", "person", "other", "none"]
LABELS = OLD + list(NEW)
VIEWS = [k for k in OLD if k not in ("person", "other", "none")]
KINDS_ALL = list(dict.fromkeys(list(F.KINDS) + list(NEW)))   # the kinds a species table may carry once the page knows the groups
ALLOWED = ("cc0", "cc-by", "cc-by-nc", "pd")
C_REG = 20.0
SEED = 20261012
RESAMPLES = 2000
COCO_KEYS = ("person", "none", "cat", "dog", "deer")

RECIPES = {
    "fold": {"with_alachua": "both", "powers": "0,0.5,1", "alachua_weight": 1.0, "coco_weight": 1.0, "calibrate": False,
             "groups": "fold", "t_kinds": "0.5,1,2", "w_kinds": "0.3,0.5,0.7,0.9,1.0", "settle_on": "all"},
    "merge": {"with_alachua": "yes", "powers": "0", "alachua_weight": 3.0, "coco_weight": 10.0, "calibrate": True,
              "groups": "merge", "t_kinds": "0.5,1,2", "w_kinds": "0.5,0.7,0.9,1.0", "settle_on": "old", "other_view": None},
    # the merge recipe with `other`'s bias raised until at most 9% of the world tuning photos in `other` get a view
    "merge-other": {"with_alachua": "yes", "powers": "0", "alachua_weight": 3.0, "coco_weight": 10.0, "calibrate": True,
                    "groups": "merge", "t_kinds": "0.5,1,2", "w_kinds": "0.5,0.7,0.9,1.0", "settle_on": "old", "other_view": 0.09},
}
RECIPES["fold"]["other_view"] = None


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def h8(s):
    return int(hashlib.sha256(s.encode()).hexdigest()[:8], 16)


def unit(X):
    X = np.asarray(X, dtype=np.float32)
    return X / np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-12)


def vec_path(root, model, name):
    return os.path.join(root, "lab", model, "images", name)


def has_vec(root, model, name):
    return os.path.exists(vec_path(root, model, name) + ".f16.npy")


def load_vec(root, name, model=None):
    p = vec_path(root, model or MODEL, name)
    if not os.path.exists(p + ".f16.npy"):
        return None, None
    return unit(np.load(p + ".f16.npy")), json.load(open(p + ".ids.json"))


def eval_name(root, model, base, vectors):
    """The vectors of the tuning and test photos: the phone's WASM runtime's where the laboratory made them."""
    if vectors in ("wasm", "auto") and has_vec(root, model, base + WASM):
        return base + WASM
    if vectors == "wasm":
        sys.exit("no WASM vectors of %s for %s" % (base, model))
    return base


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def licence_ok(s):
    s = (s or "").strip().lower().replace("_", "-")
    base = s.split("-4.0")[0].split("-3.0")[0].split("-2.0")[0].split("-1.0")[0]
    return base in ALLOWED or s in ("cc0-1.0", "public domain", "no known copyright restrictions", "united states government work")


# ---------------------------------------------------------------- photos

class Today:
    """Today's page sees each photo through TinyCLIP 39M/16 in the phone's WASM runtime (the COCO tuning photos through
    the original model, as today's settings were chosen); this gives those vectors for any photo ids."""

    def __init__(self, root):
        self.root, self.kept = root, {}

    def vectors(self, name, ids):
        if name not in self.kept:
            X, got = load_vec(self.root, name, TODAY)
            if X is None:
                sys.exit("today's vectors %s are missing" % name)
            self.kept[name] = (X, {j: i for i, j in enumerate(got)})
        X, pos = self.kept[name]
        keep = np.array([j in pos for j in ids], dtype=bool)
        return X[[pos[j] for j, k in zip(ids, keep) if k]], keep


def subset(d, keep):
    out = {}
    for k, v in d.items():
        if isinstance(v, np.ndarray) and len(v) == len(keep):
            out[k] = v[keep]
        elif isinstance(v, list) and len(v) == len(keep):
            out[k] = [x for x, kk in zip(v, keep) if kk]
        else:
            out[k] = v
    return out


def with_today(d, today, name):
    """Adds today's vectors (Xt) for the same photos, leaving out a photo either encoder lacks."""
    if today is None:
        return d
    Xt, keep = today.vectors(name, d["ids"])
    d = subset(d, keep)
    d["Xt"] = Xt
    return d


def world_parts(root, parts, vectors, today):
    """The world photos: fit (the original model's vectors), tune and test (WASM vectors where made), with group,
    continent and month; tune and test also with today's vectors."""
    out, used = {}, {}
    if "fit" in parts:
        fit = {r["id"]: r for r in read_csv(os.path.join(root, "world", "lab", "world-fit", "manifest.csv"))}
        X, ids = load_vec(root, "world-fit")
        keep = [i for i, j in enumerate(ids) if j in fit and licence_ok(fit[j]["licence"])]
        out["fit"] = {"X": X[keep], "y": np.array([fit[ids[i]]["group"] for i in keep]),
                      "cont": np.array([fit[ids[i]]["continent"] for i in keep]), "ids": [ids[i] for i in keep],
                      "month": np.array([int(fit[ids[i]]["date"][5:7]) - 1 for i in keep]), "rows": [fit[ids[i]] for i in keep]}
        used["fit"] = "world-fit"
    ev_parts = [s for s in ("tune", "test") if s in parts]
    if ev_parts:
        ev = {r["id"]: r for r in read_csv(os.path.join(root, "world", "lab", "world-eval", "manifest.csv"))}
        name = eval_name(root, MODEL, "world-eval", vectors)
        Xw, idw = load_vec(root, name)
        for s in ev_parts:
            keep = [i for i, j in enumerate(idw) if j in ev and ev[j]["set"] == s]
            d = {"X": Xw[keep], "y": np.array([ev[idw[i]]["group"] for i in keep]),
                 "cont": np.array([ev[idw[i]]["continent"] for i in keep]), "ids": [idw[i] for i in keep],
                 "month": np.array([int(ev[idw[i]]["date"][5:7]) - 1 for i in keep]),
                 "order": [ev[idw[i]]["order"] for i in keep], "cls": [ev[idw[i]]["class"] for i in keep]}
            out[s] = with_today(d, today, "world-eval" + WASM)
            used[s] = name
    return out, used


def county_keys(root):
    sp = json.load(open(os.path.join(root, "data", "regions", "us-fl-alachua", "species.json")))["species"]
    by_key = {}
    for r in sp:
        eyes = r.get("eyes")
        names = {r.get(k) or "" for k in ("kingdom", "phylum", "class", "order", "family", "genus")}
        g = group_of(names, r.get("genus") or None, r.get("family") or None)
        by_key[str(r["key"])] = (eyes, g if eyes == "other" else eyes, r)
    return by_key


def alachua_parts(root, parts, vectors, today, by_key):
    """The county photos: training rows (the original model's vectors) and val and test (WASM vectors where made),
    labelled with today's kind of eye and with the new group, from GBIF's ranks in the county list."""
    out, used = {}, {}
    if "fit" in parts:
        man = {r["id"]: r for r in read_csv(os.path.join(root, "data", "train", "alachua-pre2025", "manifest.csv"))}
        X, ids = load_vec(root, "alachua-pre2025")
        keep = [i for i, j in enumerate(ids) if j in man and man[j]["key"] in by_key and licence_ok(man[j]["licence"])]
        out["fit"] = {"X": X[keep], "y": np.array([by_key[man[ids[i]]["key"]][1] for i in keep]),
                      "old": np.array([by_key[man[ids[i]]["key"]][0] for i in keep]), "ids": [ids[i] for i in keep],
                      "keys": [man[ids[i]]["key"] for i in keep], "rows": [man[ids[i]] for i in keep]}
        used["fit"] = "alachua-pre2025"
    ev_parts = [(s, split) for s, split in (("tune", "val"), ("test", "test")) if s in parts]
    if ev_parts:
        ev = {r["id"]: r for r in read_csv(os.path.join(root, "data", "eval", "alachua-2025", "manifest.csv"))}
        name = eval_name(root, MODEL, "alachua-2025", vectors)
        Xw, idw = load_vec(root, name)
        for s, split in ev_parts:
            keep = [i for i, j in enumerate(idw) if j in ev and ev[j]["split"] == split and ev[j]["key"] in by_key]
            d = {"X": Xw[keep], "y": np.array([by_key[ev[idw[i]]["key"]][1] for i in keep]),
                 "old": np.array([by_key[ev[idw[i]]["key"]][0] for i in keep]), "ids": [idw[i] for i in keep],
                 "keys": [ev[idw[i]]["key"] for i in keep], "month": np.array([int(ev[idw[i]]["month"]) - 1 for i in keep])}
            out[s] = with_today(d, today, "alachua-2025" + WASM)
            used[s] = name
    return out, used


def coco_parts(root, parts, vectors, today):
    """The COCO extra set (people, pets, livestock under `deer`, rooms with nothing alive under `none`): fit and tune
    from the original model's vectors, test from the WASM vectors where made, as tools/eval/kinds.py cuts it."""
    man = {r["id"]: r for r in read_csv(os.path.join(root, "data", "extra", "coco-kinds", "manifest.csv"))}

    def part(r):
        return "test" if r["split"] == "test" else ("fit" if h8(r["id"]) % 3 < 2 else "tune")

    out, used = {}, {}
    if "fit" in parts or "tune" in parts:
        X, ids = load_vec(root, "coco-kinds")
        for s in ("fit", "tune"):
            if s not in parts:
                continue
            keep = [i for i, j in enumerate(ids) if j in man and part(man[j]) == s and (s != "fit" or licence_ok(man[j].get("licence")))]
            d = {"X": X[keep], "y": np.array([man[ids[i]]["eyes"] for i in keep]), "ids": [ids[i] for i in keep],
                 "month": np.array([h8("month|" + ids[i]) % 12 for i in keep]), "rows": [man[ids[i]] for i in keep]}
            out[s] = with_today(d, today, "coco-kinds") if s == "tune" else d
            used[s] = "coco-kinds"
    if "test" in parts:
        name = eval_name(root, MODEL, "coco-kinds", vectors)
        Xw, idw = load_vec(root, name)
        keep = [i for i, j in enumerate(idw) if j in man and part(man[j]) == "test"]
        d = {"X": Xw[keep], "y": np.array([man[idw[i]]["eyes"] for i in keep]), "ids": [idw[i] for i in keep],
             "month": np.array([h8("month|" + idw[i]) % 12 for i in keep])}
        out["test"] = with_today(d, today, "coco-kinds" + WASM)
        used["test"] = name
    return out, used


def world_sets(root):
    """The interface of 12 October (tools/world/exp.py): every part, TinyCLIP's WASM vectors for tuning and test."""
    return world_parts(root, ("fit", "tune", "test"), "auto", None)[0]


def alachua_sets(root):
    by_key = county_keys(root)
    return alachua_parts(root, ("fit", "tune", "test"), "auto", None, by_key)[0], by_key


def coco_sets(root):
    return coco_parts(root, ("fit", "tune", "test"), "auto", None)[0]


# ---------------------------------------------------------------- the page's answer, many photos at a time

class Table:
    """The species head and its table as the page reads them, with the table's kinds as given."""

    def __init__(self, slot, table, kinds_known):
        self.S = slot["species"].astype(np.float32)
        self.sb = slot["species_bias"].astype(np.float32) if slot["species_bias"] is not None else np.zeros(len(self.S), np.float32)
        self.rows = []
        for r in table:
            k = r[2] if r[2] in kinds_known else "other"
            m = r[3] if isinstance(r[3], (list, tuple)) and len(r[3]) == 12 else None
            self.rows.append({"sci": r[0], "en": r[1], "kind": k, "m": m})
        self.kinds = sorted({r["kind"] for r in self.rows}, key=kinds_known.index)
        self.idx = np.array([self.kinds.index(r["kind"]) for r in self.rows])
        self.prior = {}

    def prior_log(self, month, floor):
        if (month, floor) not in self.prior:
            self.prior[(month, floor)] = F.prior_log(self.rows, month, floor).astype(np.float32)
        return self.prior[(month, floor)]


_SHARES = {}


def species_shares(X, months, table, fusion, chunk=2048):
    """Each photo's share of the species answer for each kind the table carries (the part of the rule that does not
    depend on the kinds head), worked out once for each set of photos and table."""
    key = (id(X), len(X), id(table.S), tuple(table.kinds), hashlib.sha256(table.idx.tobytes()).hexdigest(), fusion["t_species"],
           fusion.get("alpha_prior"), fusion.get("prior_floor", 1e-6))
    if key in _SHARES:
        return _SHARES[key]
    q = np.zeros((len(X), len(table.kinds)))
    S = table.S.astype(np.float64)
    for a in range(0, len(X), chunk):
        Xa = X[a:a + chunk].astype(np.float64)
        zs = fusion["t_species"] * (Xa @ S.T) + table.sb
        if fusion.get("alpha_prior"):
            pri = np.stack([table.prior_log(int(m), fusion.get("prior_floor", 1e-6)) for m in months[a:a + chunk]])
            zs = zs + fusion["alpha_prior"] * pri
        zs -= zs.max(axis=1, keepdims=True)
        e = np.exp(zs); e /= e.sum(axis=1, keepdims=True)
        for j in range(len(table.kinds)):
            q[a:a + chunk, j] = e[:, table.idx == j].sum(axis=1)
    _SHARES[key] = q
    return q


def answer(X, months, K, kb, labels, fusion, table=None):
    """The fused kind and its probability for each photo, by the rule `mix` (or the head alone when table is None).
    Rows that share a label are one kind: their probabilities are added, in row order, before the rule combines them."""
    z = fusion["t_kind"] * (X.astype(np.float64) @ K.T) + kb
    z -= z.max(axis=1, keepdims=True)
    p = np.exp(z); p /= p.sum(axis=1, keepdims=True)
    ul = list(dict.fromkeys(labels))
    if len(ul) < len(labels):
        pu = np.zeros((len(p), len(ul)))
        for i, lab in enumerate(labels):
            pu[:, ul.index(lab)] += p[:, i]
        p = pu
    speaks = np.array([table is not None and lab in table.kinds for lab in ul])
    if table is not None and speaks.any():
        q = species_shares(X, months, table, fusion)
        Q = np.zeros_like(p)
        for i, lab in enumerate(ul):
            if speaks[i]:
                Q[:, i] = q[:, table.kinds.index(lab)]
        share = (p * speaks).sum(axis=1, keepdims=True)
        w = fusion["w_kind"]
        c = np.where(speaks, w * p + (1 - w) * share * Q, p)
        c /= c.sum(axis=1, keepdims=True)
    else:
        c = p
    best = np.argmax(c, axis=1)                    # ties go to the earlier label, as in the page
    kind = np.array([ul[b] for b in best], dtype=object)
    return kind, c[np.arange(len(c)), best]


def parity(m, K, kb, tab, table_rows, X, months, n=60):
    """The vectorized rule against tools/fusion/fuse.py on n photos; returns the number of answers that differ."""
    old = F.KINDS
    F.KINDS = tuple(KINDS_ALL)
    try:
        kind, prob = answer(X[:n], months[:n], K, kb, m["kinds"]["labels"], m["fusion"], tab)
        bad = 0
        for i in range(min(n, len(X))):
            o = F.fuse(m, table_rows, int(months[i]), F.dots(K, X[i]), F.dots(tab.S.astype(np.float64), X[i]), kind_bias=kb,
                       species_bias=tab.sb.astype(np.float64))
            if o["kind"] != kind[i] or abs(o["kindP"] - prob[i]) > 1e-6:
                bad += 1
        return bad
    finally:
        F.KINDS = old


# ---------------------------------------------------------------- fitting

def fit_head(X, y, power, labels, mult=None):
    from sklearn.linear_model import LogisticRegression
    cls, cnt = np.unique(y, return_counts=True)
    sw = (cnt.astype(np.float64) ** -power)[np.searchsorted(cls, y)]
    if mult is not None:
        sw = sw * mult
    sw *= len(y) / sw.sum()
    t0 = time.time()
    lr = LogisticRegression(C=C_REG, max_iter=1000).fit(X, y, sample_weight=sw)
    W = np.zeros((len(labels), X.shape[1])); b = np.full(len(labels), -50.0)
    for j, c in enumerate(lr.classes_):
        W[labels.index(c)], b[labels.index(c)] = lr.coef_[j], lr.intercept_[j]
    return W, b, {"iterations": int(np.max(lr.n_iter_)), "seconds": round(time.time() - t0, 1), "classes": len(lr.classes_)}


def calibrate_offsets(Z, y, labels, groups, grid=np.arange(-3.0, 3.01, 0.25), passes=3):
    """Offsets for the groups' biases, by coordinate ascent on the sum over the groups of min(named, right when called),
    the head alone with every row its own label (tools/world/exp.py, trial `merge`)."""
    off = np.zeros(len(labels)); gi = [labels.index(g) for g in groups]
    lab = np.array(labels, dtype=object)

    def total(o):
        k = lab[(Z + o).argmax(1)]
        return sum(min(np.mean(k[y == g] == g), np.mean(y[k == g] == g) if (k == g).any() else 0.0) for g in groups)
    cur = total(off)
    for _ in range(passes):
        moved = False
        for j in gi:
            best = (cur, off[j])
            for d in grid:
                o = off.copy(); o[j] = d
                t = total(o)
                if t > best[0] + 1e-9:
                    best = (t, d)
            if best[1] != off[j]:
                off[j] = best[1]; cur = best[0]; moved = True
        if not moved:
            break
    return off


# ---------------------------------------------------------------- the county list for another encoder

REL = (0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.75, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0)   # tools/eval/study2.py
SCALES = (0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 16.0, 24.0, 32.0, 48.0, 64.0, 96.0, 128.0)
T_SPECIES = 100.0


def lda(X, y, S, shrink):
    """Rows and biases of Gaussian classes with a shared covariance (tools/eval/study2.py); species without a fitting
    photo get no row."""
    have = np.zeros(S, bool); have[y] = True
    cnt = np.bincount(y, minlength=S).astype(np.float32)
    M = np.zeros((S, X.shape[1]), np.float32)
    np.add.at(M, y, X)
    M[have] /= cnt[have, None]
    Xc = X - M[y]
    cov = (Xc.T @ Xc) / max(1, len(X) - int(have.sum()))
    out, d = {}, X.shape[1]
    for g in shrink:
        C = (1 - g) * cov + g * (np.trace(cov) / d) * np.eye(d, dtype=np.float32)
        W = np.linalg.solve(C.astype(np.float64), M.T.astype(np.float64)).T.astype(np.float32)
        b = (-0.5 * (W * M).sum(1)).astype(np.float32)
        b[~have] = -1e9
        out[g] = (W, b)
    return out, have


def fit_species(Afit, Atune, keys, table_rows, floor):
    """The county list's rows for this encoder, as tools/eval/study2.py made the shipped ones: the discriminant head on
    the Alachua training photos (licence rule nc), the shrinkage and the prior's weight chosen by the share of Alachua
    tuning photos whose species comes first, then the scale by the lowest negative log likelihood there. Returns the
    rows as the page stores them (score = t_species * row . e + bias + alpha_prior * log share), and a record."""
    k2i = {str(k): i for i, k in enumerate(keys)}
    S = len(keys)
    y = np.array([k2i.get(str(k), -1) for k in Afit["keys"]]); ok = y >= 0
    X, y = Afit["X"][ok], y[ok]
    yu = np.array([k2i.get(str(k), -1) for k in Atune["keys"]])
    Xu, mu = Atune["X"], Atune["month"]
    rows = [{"m": r[3] if isinstance(r[3], (list, tuple)) and len(r[3]) == 12 else None} for r in table_rows]
    lp = np.stack([F.prior_log(rows, int(m), floor) for m in range(12)]).astype(np.float32)[mu]
    shrink = (0.03, 0.1, 0.3, 1.0)
    L, have = lda(X, y, S, shrink)
    best = None
    for g in shrink:
        W, b = L[g]
        Z = Xu @ W.T + b
        top2 = np.partition(Z, -2, axis=1)[:, -2:]
        u = float(np.median(top2[:, 1] - top2[:, 0])) or 1e-6
        for r in REL:
            acc = float(((Z + np.float32(r * u) * lp).argmax(1) == yu).mean())
            if best is None or acc > best[0]:
                best = (acc, g, r, u)
    acc, g, r, u = best
    W, b = L[g]
    Z = Xu @ W.T + b + np.float32(r * u) * lp
    okc = yu >= 0
    sbest = None
    for k in SCALES:
        Lg = (np.float32(k / u) * Z[okc]).astype(np.float64)
        mx = Lg.max(1, keepdims=True)
        nll = float((mx[:, 0] + np.log(np.exp(Lg - mx).sum(1)) - Lg[np.arange(okc.sum()), yu[okc]]).mean())
        if sbest is None or nll < sbest[0]:
            sbest = (nll, k / u)
    s = sbest[1]
    rec = {"head": "discriminant", "shrinkage": g, "prior_weight_relative": r, "gap": round(u, 6), "scale": round(s, 6),
           "alpha_prior": round(float(r * u * s), 6), "tuning_top1": round(acc, 4), "tuning_nll": round(sbest[0], 4),
           "fitting_photos": int(len(y)), "species_with_rows": int(have.sum()), "species": S}
    stored = (np.float32(s) * W / np.float32(T_SPECIES)).astype("<f2").astype(np.float32)
    return stored, (np.float32(s) * b).astype(np.float32), rec


# ---------------------------------------------------------------- measures

def boot(n, seed=SEED):
    return np.random.default_rng(seed).integers(0, n, size=(RESAMPLES, n))


def ci_mean(x, idx=None):
    x = np.asarray(x, dtype=np.float64)
    if len(x) == 0:
        return [None, None, None, 0]
    idx = boot(len(x)) if idx is None else idx
    m = x[idx].mean(axis=1)
    return [round(float(x.mean()), 4), round(float(np.percentile(m, 2.5)), 4), round(float(np.percentile(m, 97.5)), 4), int(len(x))]


def balanced_share(kind, y, keys):
    return float(np.mean([np.mean(kind[y == k] == k) for k in keys if (y == k).any()]))


def kind_at_level(kind, prob, y, bar=0.95, grid=np.round(np.arange(0.20, 0.9951, 0.01), 2), least=100):
    """The lowest level from which, at every higher level with at least `least` photos, an asserted kind is right at
    least `bar` of the time (tools/eval/kinds.py)."""
    ok = None
    for lv in grid[::-1]:
        sel = prob >= lv
        if sel.sum() >= least and np.mean(kind[sel] == y[sel]) < bar:
            break
        ok = lv
    return float(ok) if ok is not None else 0.99


def folded(y, carried):
    """Truth or fitting labels with the groups the head does not carry put back in `other`."""
    return np.array([v if (v not in NEW or v in carried) else "other" for v in y], dtype=object)


def group_marks(kind, y, groups):
    out = {}
    for g in groups:
        n_g = int((y == g).sum()); called = int((kind == g).sum()); tp = int(((kind == g) & (y == g)).sum())
        rec = tp / n_g if n_g else None; prec = tp / called if called else None
        out[g] = {"photos": n_g, "named": round(rec, 4) if rec is not None else None, "called": called,
                  "right_when_called": round(prec, 4) if prec is not None else None,
                  "pass": bool(rec is not None and prec is not None and rec >= 0.75 and prec >= 0.75)}
    return out


def worst_of(fails):
    return min(fails, key=lambda g: min(fails[g]["named"] or 0, fails[g]["right_when_called"] or 0))


# ---------------------------------------------------------------- main

def floats(s):
    return [float(x) for x in str(s).split(",") if x != ""]


def main():
    global MODEL
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("--slot", default="models/pocket", help="today's slot, whose head and list today's page runs")
    ap.add_argument("--out", required=True)
    ap.add_argument("--recipe", default="fold", choices=sorted(RECIPES), help="the defaults of the options below")
    ap.add_argument("--model", default=TODAY, help="the encoder of the new head, a laboratory model id")
    ap.add_argument("--vectors", default="auto", choices=("auto", "wasm", "torch"), help="the tuning and test photos' vectors: the phone runtime's where made (auto)")
    ap.add_argument("--with-alachua", choices=("both", "yes", "no"))
    ap.add_argument("--powers")
    ap.add_argument("--alachua-weight", type=float)
    ap.add_argument("--coco-weight", type=float)
    ap.add_argument("--calibrate", choices=("yes", "no"))
    ap.add_argument("--groups", help="'fold' (refit without each failing group), 'merge' (merge each failing group's row into other), 'all', or a comma list")
    ap.add_argument("--t-kinds")
    ap.add_argument("--w-kinds")
    ap.add_argument("--settle-on", choices=("old", "all"), help="the Alachua tuning photos the settings are chosen on: those of the old kinds, or all")
    ap.add_argument("--other-view", type=float, help="merge only: raise other's bias, in steps of 0.05, until at most this share of the world tuning photos in other is given a view; then fold and settle again")
    ap.add_argument("--max-fit", type=int, default=0, help="fit on an even sample of at most this many photos of each set (0: all; for trying the code)")
    ap.add_argument("--tune-only", action="store_true", help="stop before the test photos are loaded")
    a = ap.parse_args()
    R = dict(RECIPES[a.recipe])
    for k in R:
        v = getattr(a, k)
        if v is not None:
            R[k] = (v == "yes") if k == "calibrate" else v
    MODEL = a.model
    os.makedirs(a.out, exist_ok=True)
    rep = {"model": MODEL, "today_model": TODAY, "C": C_REG, "recipe": a.recipe, "options": R, "made": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "page": "away from the county's time zone the page leaves the county list out (the head alone); in it, the head and the list are combined by the rule mix"}
    today = Today(a.root)
    by_key = county_keys(a.root)
    W, uw = world_parts(a.root, ("fit", "tune"), a.vectors, today)
    A, ua = alachua_parts(a.root, ("fit", "tune"), a.vectors, today, by_key)
    X3, uc = coco_parts(a.root, ("fit", "tune"), a.vectors, today)
    rep["vectors"] = {"world": uw, "alachua": ua, "coco": uc, "today": {"encoder": TODAY, "world": "world-eval" + WASM, "alachua": "alachua-2025" + WASM,
                                                                        "coco_tune": "coco-kinds", "coco_test": "coco-kinds" + WASM}}
    if a.max_fit:
        rng = np.random.default_rng(SEED)
        for d in (W, A, X3):
            n = len(d["fit"]["y"])
            if n > a.max_fit:
                k = np.sort(rng.choice(n, a.max_fit, replace=False))
                d["fit"] = subset(d["fit"], np.isin(np.arange(n), k))
        rep["max_fit"] = a.max_fit
    for name, d in (("world", W), ("alachua", A), ("coco", X3)):
        rep.setdefault("photos", {})[name] = {s: int(len(v["y"])) for s, v in d.items()}
    log("model", MODEL, "recipe", a.recipe, json.dumps(R))
    log("photos", json.dumps(rep["photos"]), "vectors", json.dumps(rep["vectors"]))

    # today's head and table
    slot = F.load_slot(a.slot)
    m_old = slot["manifest"]
    K_old, kb_old = slot["kinds"], slot["kind_bias"]
    sci2group = {r["sci"]: g for (eyes, g, r) in by_key.values()}
    table_old = slot["table"]
    T_old = Table(slot, table_old, list(F.KINDS))
    bad = parity(m_old, K_old, kb_old, T_old, table_old, A["tune"]["Xt"], A["tune"]["month"])
    rep["parity_with_fuse_py"] = {"photos": 60, "set": "Alachua tuning photos", "different": bad}
    log("parity with fuse.py on 60 Alachua tuning photos, today's slot:", bad, "different")
    if bad:
        sys.exit("the vectorized rule disagrees with tools/fusion/fuse.py")

    # the new head's species rows: the slot's for its own encoder, fitted here for another
    fusion0 = dict(m_old["fusion"])
    if MODEL == m_old.get("id", TODAY):
        spec = {"species": slot["species"], "species_bias": slot["species_bias"]}
        rep["species_rows"] = {"from": a.slot}
    else:
        keys = json.load(open(os.path.join(a.slot, m_old["species"]["table"])))["keys"]
        t0 = time.time()
        S_new, sb_new, srec = fit_species(A["fit"], A["tune"], keys, table_old, fusion0.get("prior_floor", 1e-6))
        spec = {"species": S_new.astype(np.float64), "species_bias": sb_new.astype(np.float64)}
        fusion0 = dict(fusion0, t_species=T_SPECIES, alpha_prior=srec["alpha_prior"])
        srec["seconds"] = round(time.time() - t0, 1)
        rep["species_rows"] = dict(srec, made_by="tools/world/head.py fit_species (the discriminant head of tools/eval/study2.py) on images/alachua-pre2025 of " + MODEL)
        log("species rows fitted for", MODEL, json.dumps(srec))

    def table_for(carried):
        rows = [[r[0], r[1], (sci2group.get(r[0], "other") if r[2] == "other" else r[2]), r[3]] for r in table_old]
        rows = [[r[0], r[1], (r[2] if (r[2] not in NEW or r[2] in carried) else "other"), r[3]] for r in rows]
        return rows, Table(spec, rows, KINDS_ALL)

    def old_answers(d, fused=True):
        return answer(d["Xt"], d["month"], K_old, kb_old, m_old["kinds"]["labels"], m_old["fusion"], T_old if fused else None)

    today_coco_tune = balanced_share(old_answers(X3["tune"])[0], X3["tune"]["y"], COCO_KEYS)
    sel_old_a = np.isin(A["tune"]["y"], VIEWS)
    today_alachua_old = float(np.mean(old_answers(A["tune"])[0][sel_old_a] == A["tune"]["y"][sel_old_a]))
    t_grid, w_grid = floats(R["t_kinds"]), floats(R["w_kinds"])

    def settle(Wk, bk, labels, T, ya):
        """t_kind and w_kind for the page in the county, on the Alachua and COCO tuning photos combined with the list:
        the most Alachua photos right (of the old kinds, or all of them) with the COCO photos within 1 point of
        today's page."""
        best, rows = None, []
        sel = np.isin(ya, VIEWS) if R["settle_on"] == "old" else np.ones(len(ya), bool)
        for t_kind in t_grid:
            for w_kind in w_grid:
                fu = dict(fusion0, t_kind=t_kind, w_kind=w_kind, rule="mix")
                ka, _ = answer(A["tune"]["X"], A["tune"]["month"], Wk, t_kind * bk, labels, fu, T)
                kc, _ = answer(X3["tune"]["X"], X3["tune"]["month"], Wk, t_kind * bk, labels, fu, T)
                sa = float(np.mean(ka[sel] == ya[sel])); sc = balanced_share(kc, X3["tune"]["y"], COCO_KEYS)
                ok = round(sc - today_coco_tune, 4) >= -0.01
                rows.append({"t_kind": t_kind, "w_kind": w_kind, "alachua": round(sa, 4), "coco": round(sc, 4), "coco_ok": ok})
                if R["settle_on"] == "old":
                    key = (ok, round(sa - today_alachua_old, 4) if ok else sc, round(sc - today_coco_tune, 4), t_kind, w_kind)
                else:
                    key = (ok, sa if ok else sc, w_kind)
                if best is None or key > best[0]:
                    best = (key, {"t_kind": t_kind, "w_kind": w_kind, "alachua": round(sa, 4), "coco": round(sc, 4), "coco_within_1_point": ok,
                                  "alachua_today": round(today_alachua_old, 4) if R["settle_on"] == "old" else None, "coco_today": round(today_coco_tune, 4)})
        return dict(best[1], grid=rows)

    def head_alone(d, Wk, bk, labels, t_kind=1.0):
        fu = dict(fusion0, t_kind=t_kind)
        return answer(d["X"], d["month"], Wk, t_kind * bk, labels, fu, None)

    def fitting(with_a, carried):
        Xf = [W["fit"]["X"], X3["fit"]["X"]]; yf = [W["fit"]["y"], X3["fit"]["y"]]
        mult = [np.ones(len(W["fit"]["y"])), np.full(len(X3["fit"]["y"]), float(R["coco_weight"]))]
        if with_a:
            Xf.append(A["fit"]["X"]); yf.append(A["fit"]["y"]); mult.append(np.full(len(A["fit"]["y"]), float(R["alachua_weight"])))
        return np.concatenate(Xf), folded(np.concatenate(yf), carried), np.concatenate(mult)

    def eff_labels(named):
        """The slot's labels: a group's row that is not named is labelled `other`, so that its probability is added to other's."""
        return [l if (l not in NEW or l in named) else "other" for l in LABELS]

    mixes = {"no": [False], "yes": [True], "both": [False, True]}[R["with_alachua"]]
    powers = floats(R["powers"])
    every = list(NEW)
    history = []
    off = np.zeros(len(LABELS))

    if R["groups"] == "merge":
        # one fit with every group's row; the fit's choices are the recipe's (several only if the options give several)
        grid = []
        cands = []
        for with_a in mixes:
            Xf, yf, mult = fitting(with_a, every)
            for pw in powers:
                Wk, bk, info = fit_head(Xf, yf, pw, LABELS, mult)
                info.update(with_alachua=with_a, power=pw, photos=int(len(yf)))
                log("fitted", json.dumps(info))
                cands.append((Wk, bk, info))
        for ci_, (Wk, bk, info) in enumerate(cands):
            Z = W["tune"]["X"].astype(np.float64) @ Wk.T + bk
            o = calibrate_offsets(Z, W["tune"]["y"], LABELS, every) if R["calibrate"] else np.zeros(len(LABELS))
            kw, _ = answer(W["tune"]["X"], W["tune"]["month"], Wk, bk + o, LABELS, dict(fusion0, t_kind=1.0), None)
            m_ = group_marks(kw, W["tune"]["y"], every)
            score = float(sum(min(v["named"] or 0, v["right_when_called"] or 0) for v in m_.values()))
            grid.append({"cand": ci_, **{k: info[k] for k in ("with_alachua", "power", "iterations", "seconds", "photos")}, "groups_score": round(score, 4),
                         "groups_passing": sum(1 for v in m_.values() if v["pass"])})
            cands[ci_] = (Wk, bk, info, o)
        pick = max(grid, key=lambda g: (g["groups_score"], -g["cand"]))
        Wk, bk, info, off = cands[pick["cand"]]
        recipe = {"with_alachua": info["with_alachua"], "power": info["power"]}
        rep["recipe_grid"] = {"grid": grid, "chosen": pick}
        rep["offsets"] = {g: float(off[LABELS.index(g)]) for g in every if off[LABELS.index(g)] != 0}
        log("offsets", json.dumps(rep["offsets"]))
        b2 = bk + off

        def merge_fold(named, t_kind):
            """Merges the worst failing group into other until every group still named passes on the world tuning photos."""
            while True:
                labs = eff_labels(named)
                kw, _ = head_alone(W["tune"], Wk, b2, labs, t_kind)
                yw = folded(W["tune"]["y"], named)
                marks = group_marks(kw, yw, named)
                fails = {g: m for g, m in marks.items() if not m["pass"]}
                history.append({"t_kind": t_kind, "carried": list(named), "marks": marks, "world_tune_right": round(float(np.mean(kw == yw)), 4)})
                log("t_kind %s, named %d, failing %d: %s" % (t_kind, len(named), len(fails), ", ".join("%s %s/%s" % (g, m["named"], m["right_when_called"]) for g, m in sorted(marks.items()))))
                if not fails:
                    return named
                worst = worst_of(fails)
                named = [g for g in named if g != worst]
                log("merged into other:", worst)

        carried = merge_fold(list(every), 1.0)

        def choose(carried):
            for _ in range(6):
                labs = eff_labels(carried)
                _, T_ = table_for(carried)
                st = settle(Wk, b2, labs, T_, folded(A["tune"]["y"], carried))
                again = merge_fold(list(carried), st["t_kind"])
                if again == carried:
                    return carried, st
                carried = again
            return carried, st
        carried, st = choose(carried)
        rep["other_offset"] = 0.0
        if R.get("other_view") is not None:
            # `other` lends no eyes: its bias is raised until the share of the world tuning photos in `other` given a view
            # is at most the target, at the chosen t_kind, the head alone; then the fold and the settings again, until steady
            oi = LABELS.index("other")
            for _ in range(5):
                labs = eff_labels(carried)
                yw = folded(W["tune"]["y"], carried); so = yw == "other"
                base = b2[oi]
                found = None
                for d in np.round(np.arange(0.0, 8.0001, 0.05), 2):
                    b2[oi] = base + d
                    kw, _ = head_alone(W["tune"], Wk, b2, labs, st["t_kind"])
                    if float(np.isin(kw[so], VIEWS).mean()) <= R["other_view"]:
                        found = d
                        break
                if found is None:
                    b2[oi] = base
                    log("no offset of other up to 8 gives the target on the tuning photos")
                    break
                rep["other_offset"] = round(rep["other_offset"] + float(found), 2)
                log("other's bias raised by %s (in all %s)" % (found, rep["other_offset"]))
                again, st2 = choose(list(carried))
                if again == carried and found == 0:
                    st = st2
                    break
                carried, st = again, st2
        bias_rows = b2
    else:
        # 1. the fitting recipe, with every group carried, chosen on the tuning photos
        _, T_all = table_for(every)
        grid = []
        for with_a in mixes:
            Xf, yf, mult = fitting(with_a, every)
            for pw in powers:
                Wk, bk, info = fit_head(Xf, yf, pw, LABELS, mult)
                kw, _ = head_alone(W["tune"], Wk, bk, LABELS)
                sw = balanced_share(kw, W["tune"]["y"], sorted(set(W["tune"]["y"])))
                st = settle(Wk, bk, LABELS, T_all, A["tune"]["y"])
                g = {"with_alachua": with_a, "power": pw, "world_alone": round(sw, 4), **{k: v for k, v in st.items() if k != "grid"},
                     "score": round((sw + st["alachua"] + st["coco"]) / 3, 4), **info}
                grid.append(g)
                log("recipe", json.dumps(g))
        recipe = max(grid, key=lambda g: g["score"])
        rep["recipe_grid"] = {"grid": grid, "chosen": recipe}
        # 2. the groups carried, refitted without the worst failing group until every group carried passes
        carried = list(NEW) if R["groups"] in ("fold", "all") else [g for g in NEW if g in R["groups"].split(",")]
        while True:
            labels = OLD + carried
            Xf, yf, mult = fitting(recipe["with_alachua"], carried)
            Wk, bk, info = fit_head(Xf, yf, recipe["power"], labels, mult)
            yw = folded(W["tune"]["y"], carried)
            kw, _ = head_alone(W["tune"], Wk, bk, labels)
            marks = group_marks(kw, yw, carried)
            fails = {g: m for g, m in marks.items() if not m["pass"]}
            history.append({"t_kind": 1.0, "carried": list(carried), "marks": marks, "world_tune_right": round(float(np.mean(kw == yw)), 4)})
            log("carried %d, failing %d: %s" % (len(carried), len(fails), ", ".join("%s %s/%s" % (g, m["named"], m["right_when_called"]) for g, m in sorted(marks.items()))))
            if R["groups"] != "fold" or not fails:
                break
            worst = worst_of(fails)
            carried.remove(worst)
            log("put back in other:", worst)
        _, T_ = table_for(carried)
        st = settle(Wk, bk, OLD + carried, T_, folded(A["tune"]["y"], carried))
        bias_rows = bk

    def labels_of(carried):
        return eff_labels(carried) if R["groups"] == "merge" else OLD + carried

    def levels_for(carried, Wk, brows, st):
        labels = labels_of(carried)
        _, T_new = table_for(carried)
        fu = dict(fusion0, t_kind=st["t_kind"], w_kind=st["w_kind"], rule="mix")
        kb = st["t_kind"] * brows
        kw, pw_ = head_alone(W["tune"], Wk, brows, labels, st["t_kind"])
        ka, pa = answer(A["tune"]["X"], A["tune"]["month"], Wk, kb, labels, fu, T_new)
        kc, pc = answer(X3["tune"]["X"], X3["tune"]["month"], Wk, kb, labels, fu, T_new)
        yw = folded(W["tune"]["y"], carried)
        levels = {"world": kind_at_level(kw, pw_, yw), "alachua": kind_at_level(ka, pa, folded(A["tune"]["y"], carried)),
                  "coco": kind_at_level(kc, pc, X3["tune"]["y"])}
        fu["kind_at"] = max(levels.values())
        so = yw == "other"
        tune = {"world_marks": group_marks(kw, yw, carried), "world_old_right": round(float(np.mean(kw[np.isin(yw, VIEWS)] == yw[np.isin(yw, VIEWS)])), 4),
                "world_old_right_today": round(float(np.mean(old_answers(W["tune"])[0][np.isin(yw, VIEWS)] == yw[np.isin(yw, VIEWS)])), 4),
                "other_given_a_view": round(float(np.isin(kw[so], VIEWS).mean()), 4) if so.any() else None,
                "alachua_old_right": round(float(np.mean(ka[np.isin(A["tune"]["y"], VIEWS)] == A["tune"]["y"][np.isin(A["tune"]["y"], VIEWS)])), 4),
                "alachua_old_right_today": round(today_alachua_old, 4), "coco_with_list": round(balanced_share(kc, X3["tune"]["y"], COCO_KEYS), 4),
                "coco_today": round(today_coco_tune, 4)}
        kca, _ = head_alone(X3["tune"], Wk, brows, labels, st["t_kind"])
        tune["coco_alone"] = round(balanced_share(kca, X3["tune"]["y"], COCO_KEYS), 4)
        return fu, kb, {**{k: v for k, v in st.items() if k != "grid"}, "kind_at": fu["kind_at"], "levels": levels, "bar": 0.95, "grid": st.get("grid")}, tune

    fu, kb, settings, tune_marks = levels_for(carried, Wk, bias_rows, st)
    log("settings", json.dumps({k: v for k, v in settings.items() if k != "grid"}))
    # the vectorized rule against tools/fusion/fuse.py for the new head, rows that share a label added, on tuning photos
    rows_chk, T_chk = table_for(carried)
    bad = parity({"kinds": {"labels": labels_of(carried)}, "fusion": fu}, Wk, kb, T_chk, rows_chk, A["tune"]["X"], A["tune"]["month"])
    rep["parity_with_fuse_py_new_head"] = {"photos": 60, "set": "Alachua tuning photos", "different": bad}
    log("parity with fuse.py on 60 Alachua tuning photos, the new head:", bad, "different")
    if bad:
        sys.exit("the vectorized rule disagrees with tools/fusion/fuse.py for the new head")
    log("tuning photos", json.dumps({k: v for k, v in tune_marks.items() if k != "world_marks"}))
    rep["fitted"] = info
    rep["recipe_chosen"] = recipe

    def write_slot(carried, Wk, kb, fu, table_new, tag):
        sd = os.path.join(a.out, "slot")
        os.makedirs(sd, exist_ok=True)
        labels = labels_of(carried)
        Wk.astype("<f2").tofile(os.path.join(sd, "kinds.f16.bin"))
        man = json.loads(json.dumps(m_old))
        man["kinds"] = dict(man["kinds"], labels=labels, bias=[round(float(v), 5) for v in kb],
                            made_from="tools/world/head.py (recipe %s, encoder %s), world photos of pub/data-world%s" % (
                                a.recipe, MODEL, " and the Alachua training photos" if recipe["with_alachua"] else ""))
        if R["groups"] == "merge":
            man["kinds"]["rows_fitted_as"] = LABELS
            man["kinds"]["same_label"] = "rows that share a label are one kind: their probabilities are added before the rule combines them"
        man["fusion"] = dict(man["fusion"], t_kind=fu["t_kind"], w_kind=fu["w_kind"], kind_at=fu["kind_at"], rule="mix",
                             t_species=fusion0["t_species"], alpha_prior=fusion0["alpha_prior"])
        if MODEL != m_old.get("id", TODAY):
            man["id"] = MODEL
            man["species"] = dict(man["species"], url="species.f16.bin", bias_url="species.bias.f32.bin")
            spec["species"].astype("<f2").tofile(os.path.join(sd, "species.f16.bin"))
            spec["species_bias"].astype("<f4").tofile(os.path.join(sd, "species.bias.f32.bin"))
            card = {}
            try:
                card = json.load(open(os.path.join(a.root, "lab", MODEL, "card.json")))
            except (OSError, ValueError):
                pass
            man["vision_note"] = "the encoder is %s; the vision block is to be written from pub/lab-%s (card.json: %s) before this slot can ship" % (
                MODEL, MODEL, ", ".join("%s %s" % (k, card.get(k)) for k in ("source", "licence") if card.get(k)))
            man.pop("evaluation", None); man.pop("fitted_on", None)
        man["evaluation_world"] = {"made_by": "tools/world/head.py", "reading": tag, "report": "report.json beside this slot on the run's results"}
        json.dump(man, open(os.path.join(sd, "manifest.json"), "w"), indent=1)
        sj = json.load(open(os.path.join(a.slot, m_old["species"]["table"])))
        sj = dict(sj, species=table_new) if isinstance(sj, dict) else table_new
        json.dump(sj, open(os.path.join(sd, os.path.basename(m_old["species"]["table"])), "w"), ensure_ascii=False, separators=(",", ":"))
        with open(os.path.join(sd, "fitted_on.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f); w.writerow(["id", "label", "photo_url", "licence", "obs_url"])
            for r, lab in zip(W["fit"]["rows"], folded(W["fit"]["y"], carried if R["groups"] != "merge" else every)):
                w.writerow([r["id"], lab, r["photo_url"], r["licence"], r["obs_url"]])
            for r, lab in zip(X3["fit"]["rows"], X3["fit"]["y"]):
                w.writerow([r["id"], lab, r.get("photo_url", ""), r.get("licence", ""), r.get("obs_url", "")])
            if recipe["with_alachua"]:
                for r, lab in zip(A["fit"]["rows"], folded(A["fit"]["y"], carried if R["groups"] != "merge" else every)):
                    w.writerow([r["id"], lab, r.get("photo_url", ""), r.get("licence", ""), r.get("obs_url", "")])

    if a.tune_only:
        rep["groups"] = {"rule": R["groups"], "history": history, "carried": carried, "left_in_other": [g for g in NEW if g not in carried]}
        rep["settings"] = settings; rep["tuning"] = tune_marks; rep["test"] = None
        json.dump(rep, open(os.path.join(a.out, "report.json"), "w"), indent=1)
        log("tuning only: the test photos were not loaded; written", a.out)
        return

    # the test photos, loaded only now that every setting is fixed
    Wt, uw = world_parts(a.root, ("test",), a.vectors, today)
    At, ua = alachua_parts(a.root, ("test",), a.vectors, today, by_key)
    Ct, uc = coco_parts(a.root, ("test",), a.vectors, today)
    rep["vectors"]["world"].update(uw); rep["vectors"]["alachua"].update(ua); rep["vectors"]["coco"].update(uc)
    for name, d in (("world", Wt), ("alachua", At), ("coco", Ct)):
        rep["photos"][name]["test"] = int(len(d["test"]["y"]))
    WT, AT, CT = Wt["test"], At["test"], Ct["test"]

    def finish(carried, Wk, brows, fu, kb):
        """The test photos: today's page against the new head as the page would use it."""
        labels = labels_of(carried)
        table_new, T_new = table_for(carried)
        res = {}
        yw = folded(WT["y"], carried); ya = folded(AT["y"], carried)
        ko_w, _ = old_answers(WT); kn_w, pn_w = head_alone(WT, Wk, brows, labels, fu["t_kind"])
        kf_w, _ = answer(WT["X"], WT["month"], Wk, kb, labels, fu, T_new)
        ko_a, _ = old_answers(AT); kn_a, pn_a = answer(AT["X"], AT["month"], Wk, kb, labels, fu, T_new)

        def paired(ko, kn, truth):
            sel = np.isin(truth, VIEWS)
            ro = (ko[sel] == truth[sel]).astype(float); rn = (kn[sel] == truth[sel]).astype(float)
            idx = boot(int(sel.sum()))
            d = ci_mean(rn - ro, idx)
            return {"today": ci_mean(ro, idx), "new": ci_mean(rn, idx), "difference": d, "pass": bool(d[1] is not None and d[1] > -0.02)}

        res["old_groups_world"] = paired(ko_w, kn_w, yw)                     # away: the head alone
        res["old_groups_world_with_list"] = paired(ko_w, kf_w, yw)           # for the record: as in the county's time zone
        res["old_groups_alachua"] = paired(ko_a, kn_a, ya)
        res["new_groups"] = group_marks(kn_w, yw, carried)
        kc_old, _ = old_answers(CT)
        kc_new, _ = answer(CT["X"], CT["month"], Wk, kb, labels, fu, T_new)
        kc_alone, _ = head_alone(CT, Wk, brows, labels, fu["t_kind"])
        so = balanced_share(kc_old, CT["y"], COCO_KEYS)
        sn = balanced_share(kc_new, CT["y"], COCO_KEYS); sa_ = balanced_share(kc_alone, CT["y"], COCO_KEYS)
        res["coco"] = {"today": round(so, 4), "new_with_list": round(sn, 4), "new_alone": round(sa_, 4), "pass": bool(sn >= so - 0.01 and sa_ >= so - 0.01),
                       "named_a_new_group": int(np.isin(kc_new, NEW).sum() + np.isin(kc_alone, NEW).sum()), "photos": int(len(kc_new))}
        truth_raw = WT["y"]
        sel = yw == "other"
        res["other"] = {"photos": int(sel.sum()), "given_a_view_today": round(float(np.isin(ko_w[sel], VIEWS).mean()), 4),
                        "given_a_view_new": round(float(np.isin(kn_w[sel], VIEWS).mean()), 4)}
        res["other"]["pass"] = bool(res["other"]["given_a_view_new"] < 0.10)
        parts = {}
        for g in ["other"] + [x for x in NEW if x not in carried]:
            s_ = truth_raw == g
            if s_.any():
                parts[g] = {"photos": int(s_.sum()), "given_a_view_today": round(float(np.isin(ko_w[s_], VIEWS).mean()), 4),
                            "given_a_view_new": round(float(np.isin(kn_w[s_], VIEWS).mean()), 4),
                            "views_new": dict(Counter(k for k in kn_w[s_] if k in VIEWS).most_common(5))}
        res["other"]["by_group"] = parts
        so_ = truth_raw == "other"
        orders_view = Counter()
        for i in np.where(so_)[0]:
            o = WT["order"][i] or WT["cls"][i] or "?"
            if kn_w[i] in VIEWS:
                orders_view[(o, kn_w[i])] += 1
        res["other"]["original_other_given_a_view_by_order"] = [{"order": o, "view": v, "photos": n} for (o, v), n in orders_view.most_common(20)]
        res["world_all"] = {"right_new": round(float(np.mean(kn_w == yw)), 4), "right_today": round(float(np.mean(ko_w == yw)), 4),
                            "asserted_new": round(float(np.mean(pn_w >= fu["kind_at"])), 4),
                            "right_when_asserted_new": round(float(np.mean(kn_w[pn_w >= fu["kind_at"]] == yw[pn_w >= fu["kind_at"]])), 4)}
        res["alachua_all"] = {"right_new": round(float(np.mean(kn_a == ya)), 4), "right_today": round(float(np.mean(ko_a == ya)), 4),
                              "asserted_new": round(float(np.mean(pn_a >= fu["kind_at"])), 4),
                              "right_when_asserted_new": round(float(np.mean(kn_a[pn_a >= fu["kind_at"]] == ya[pn_a >= fu["kind_at"]])), 4)}
        res["world_by_continent"] = {c: {"photos": int((WT["cont"] == c).sum()),
                                         "right_new": round(float(np.mean(kn_w[WT["cont"] == c] == yw[WT["cont"] == c])), 4),
                                         "right_today": round(float(np.mean(ko_w[WT["cont"] == c] == yw[WT["cont"] == c])), 4)}
                                     for c in sorted(set(WT["cont"]))}
        conf = Counter((t, k) for t, k in zip(yw, kn_w) if t != k)
        res["commonest_confusions"] = [{"truth": t, "answer": k, "photos": n} for (t, k), n in conf.most_common(25)]
        res["size_bytes"] = int(len(labels) * Wk.shape[1] * 2)
        res["blocking"] = {"old_groups_world": res["old_groups_world"]["pass"], "old_groups_alachua": res["old_groups_alachua"]["pass"],
                           "new_groups": all(m["pass"] for m in res["new_groups"].values()), "coco": res["coco"]["pass"],
                           "other": res["other"]["pass"], "size": res["size_bytes"] < 50000}
        res["passes_every_mark_measured_here"] = all(res["blocking"].values())
        return res, table_new

    test, table_new = finish(carried, Wk, bias_rows, fu, kb)
    failed = [g for g, m in test["new_groups"].items() if not m["pass"]]
    log("first reading of the test photos:", json.dumps(test["blocking"]), "failing groups:", failed)
    if failed and R["groups"] in ("fold", "merge"):
        # a group carried that fails on the test photos stays in other too (docs/COVERAGE.md): it is put back (refitted for
        # fold, merged for merge), the settings are chosen again on the tuning photos, and the test photos are read a second
        # time for the head that ships; both readings are kept
        rep["test_first_reading"] = test; rep["failed_on_test"] = failed
        rep["settings_first_reading"] = settings; rep["tuning_first_reading"] = tune_marks
        carried = [g for g in carried if g not in failed]
        log("failed on the test photos, put back in other:", ", ".join(failed))
        if R["groups"] == "merge":
            carried, st = choose(carried)
        else:
            Xf, yf, mult = fitting(recipe["with_alachua"], carried)
            Wk, bk, info = fit_head(Xf, yf, recipe["power"], OLD + carried, mult)
            bias_rows = bk
            rep["fitted_second"] = info
            _, T_ = table_for(carried)
            st = settle(Wk, bias_rows, OLD + carried, T_, folded(A["tune"]["y"], carried))
        fu, kb, settings, tune_marks = levels_for(carried, Wk, bias_rows, st)
        test, table_new = finish(carried, Wk, bias_rows, fu, kb)
        log("second reading of the test photos:", json.dumps(test["blocking"]))
    rep["groups"] = {"rule": R["groups"], "history": history, "carried": carried, "left_in_other": [g for g in NEW if g not in carried]}
    rep["labels"] = labels_of(carried)
    rep["table_relabelled"] = dict(Counter(r[2] for r, o in zip(table_new, table_old) if o[2] == "other"))
    rep["settings"] = settings
    rep["tuning"] = tune_marks
    rep["test"] = test
    write_slot(carried, Wk, kb, fu, table_new, "second" if rep.get("failed_on_test") else "first")
    json.dump(rep, open(os.path.join(a.out, "report.json"), "w"), indent=1)
    write_md(rep, os.path.join(a.out, "REPORT.md"))
    log("written", a.out)


def write_md(rep, path):
    t = rep["test"]
    yes = lambda b: "yes" if b else "no"
    L = ["# The group head on world photos", "",
         "Made by `tools/world/head.py` (%s), recipe `%s`, encoder `%s`. The page is scored as it would run: %s." % (rep["made"], rep["recipe"], rep["model"], rep["page"]),
         "Vectors of the new head's tuning and test photos: %s. Today's page: %s." % (
             "; ".join("%s %s" % (k, ", ".join("%s %s" % kv for kv in v.items())) for k, v in rep["vectors"].items() if k != "today"),
             ", ".join("%s %s" % kv for kv in rep["vectors"]["today"].items())), ""]
    ch = rep["recipe_chosen"]
    L.append("Fitting: power %s, %s; options %s. Groups named (%d): %s. In `other` (%d): %s." % (
        ch["power"], "with the Alachua training photos" if ch["with_alachua"] else "world and COCO photos only", json.dumps(rep["options"]),
        len(rep["groups"]["carried"]), ", ".join(rep["groups"]["carried"]) or "none",
        len(rep["groups"]["left_in_other"]), ", ".join(rep["groups"]["left_in_other"]) or "none"))
    if rep.get("offsets") is not None:
        L.append("Bias offsets calibrated on the world tuning photos: %s." % (", ".join("%s %+g" % kv for kv in rep["offsets"].items()) or "none"))
    if rep.get("species_rows", {}).get("head"):
        s = rep["species_rows"]
        L.append("County list rows fitted for this encoder: discriminant, shrinkage %s, prior weight %s, scale %s (alpha_prior %s); tuning top-1 %s." % (
            s["shrinkage"], s["prior_weight_relative"], s["scale"], s["alpha_prior"], s["tuning_top1"]))
    s = rep["settings"]
    L.append("Settings for the county: t_kind %s, w_kind %s, kind_at %s (levels %s)." % (s["t_kind"], s["w_kind"], s["kind_at"], s["levels"]))
    L += ["", "| Pass mark | Measured | Passes |", "|---|---|---|"]
    for key, what in (("old_groups_world", "world test photos, the head alone (away from the county)"), ("old_groups_alachua", "Alachua test photos, head and list combined")):
        d = t[key]
        L.append("| Old groups right, %s: 95%% interval of the paired difference above −2 points | today %s, new %s, difference %s (%s to %s), %d photos | %s |" % (
            what, d["today"][0], d["new"][0], d["difference"][0], d["difference"][1], d["difference"][2], d["difference"][3], yes(d["pass"])))
    npass = sum(1 for g in t["new_groups"].values() if g["pass"])
    L.append("| Every group named found (named and right when called, 75%% or more each, world test photos, head alone) | %d of %d pass | %s |" % (npass, len(t["new_groups"]), yes(npass == len(t["new_groups"]))))
    L.append("| People, pets and rooms within 1 point of today (COCO test) | today %s; new with the list %s, alone %s; a new group named %d times in %d answers | %s |" % (
        t["coco"]["today"], t["coco"]["new_with_list"], t["coco"]["new_alone"], t["coco"]["named_a_new_group"], 2 * t["coco"]["photos"], yes(t["coco"]["pass"])))
    L.append("| `other` given a view under 10%% (world test photos, head alone) | today %s, new %s, of %d photos | %s |" % (
        t["other"]["given_a_view_today"], t["other"]["given_a_view_new"], t["other"]["photos"], yes(t["other"]["pass"])))
    L.append("| Head under 50 KB | %d bytes | %s |" % (t["size_bytes"], yes(t["size_bytes"] < 50000)))
    d = t["old_groups_world_with_list"]
    L += ["", "For the record, the world test photos with the county list combined (as in the county's time zone): old groups today %s, new %s, difference %s (%s to %s)." % (
        d["today"][0], d["new"][0], d["difference"][0], d["difference"][1], d["difference"][2])]
    L += ["", "| Group named | test photos | named | called | right when called | passes |", "|---|---:|---:|---:|---:|---|"]
    for g, d in t["new_groups"].items():
        L.append("| %s | %d | %s | %d | %s | %s |" % (g, d["photos"], d["named"], d["called"], d["right_when_called"], yes(d["pass"])))
    L += ["", "`other` on the world test photos, by what the photo shows:", "", "| Truth | photos | given a view today | given a view, new | the views given, new |", "|---|---:|---:|---:|---|"]
    for g, d in t["other"]["by_group"].items():
        L.append("| %s | %d | %s | %s | %s |" % (g, d["photos"], d["given_a_view_today"], d["given_a_view_new"], ", ".join("%s %d" % kv for kv in d["views_new"].items())))
    L += ["", "The creatures with no group of their own given a view, by order: " + "; ".join("%s as %s %d" % (x["order"], x["view"], x["photos"]) for x in t["other"]["original_other_given_a_view_by_order"]) + "."]
    w = t["world_all"]; al = t["alachua_all"]
    L += ["", "World test photos, every label: right %s (today %s); asserted %s, right when asserted %s." % (w["right_new"], w["right_today"], w["asserted_new"], w["right_when_asserted_new"])]
    L += ["", "Alachua test photos, every label: right %s (today %s); asserted %s, right when asserted %s." % (al["right_new"], al["right_today"], al["asserted_new"], al["right_when_asserted_new"])]
    L += ["", "By continent (new, today): " + "; ".join("%s %s, %s of %d" % (c, d["right_new"], d["right_today"], d["photos"]) for c, d in t["world_by_continent"].items()) + "."]
    L += ["", "Commonest confusions: " + "; ".join("%s as %s %d" % (c["truth"], c["answer"], c["photos"]) for c in t["commonest_confusions"][:15]) + "."]
    tm = rep.get("tuning") or {}
    if tm:
        L += ["", "On the tuning photos, for the head that ships: old groups right on world photos %s (today %s), on Alachua photos %s (today %s); `other` given a view %s; COCO %s with the list, %s alone (today %s)." % (
            tm["world_old_right"], tm["world_old_right_today"], tm["alachua_old_right"], tm["alachua_old_right_today"], tm["other_given_a_view"],
            tm["coco_with_list"], tm["coco_alone"], tm["coco_today"])]
    if rep.get("failed_on_test"):
        f = rep["test_first_reading"]["new_groups"]
        b = rep["test_first_reading"]["blocking"]
        L += ["", "Named after the fold but failing on the test photos, so put back in `other` (first reading, named / right when called): " + "; ".join(
            "%s %s / %s" % (g, f[g]["named"], f[g]["right_when_called"]) for g in rep["failed_on_test"]) + ". The tables above are the second reading, for the head that ships. First reading's marks: " +
            ", ".join("%s %s" % (k, yes(v)) for k, v in b.items()) + "; `other` given a view %s; old groups world %s, Alachua %s." % (
                rep["test_first_reading"]["other"]["given_a_view_new"], rep["test_first_reading"]["old_groups_world"]["difference"], rep["test_first_reading"]["old_groups_alachua"]["difference"])]
    L += ["", "The fold, on the tuning photos (t_kind, named, failing):"]
    for h in rep["groups"]["history"]:
        fails = [g for g, m in h["marks"].items() if not m["pass"]]
        L.append("- t_kind %s, %d named, world right %s; failing: %s" % (h.get("t_kind", 1.0), len(h["carried"]), h["world_tune_right"], ", ".join("%s %s/%s" % (g, h["marks"][g]["named"], h["marks"][g]["right_when_called"]) for g in fails) or "none"))
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
