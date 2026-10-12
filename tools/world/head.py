#!/usr/bin/env python3
"""Fit the pocket model's group head on the world photos, choose its settings on the tuning photos, and score it against
the pass marks of docs/COVERAGE.md on the test photos, beside the head the page ships today.

The head is the same kind of head as the shipped one (tools/eval/study2.py): logistic regression with C = 20 on
TinyCLIP 39M/16's unit image vectors from the original model, a photo weighted by its group's count to the power
-`power`, fitted on photos allowed by the licence rule `nc`. Its labels are the seventeen of today's head followed by
the groups of GROUPS in src/cam.a.js that it carries, one row of 512 numbers each (1,024 bytes in half precision).

Photos (ROOT is laid out as tools/eval/fetch.py lays it out, with pub/data-world in ROOT/world):
  fitting   the world photos (`fit`, dated through 2024), the COCO extra set's fit part, and with --with-alachua the
            Alachua training photos too, each labelled by tools/world/groups.py from GBIF's ranks in the county list
  tuning    the world `tune` photos, the Alachua `val` photos and the COCO `tune` part; the world and Alachua photos
            through the vectors the phone's WASM runtime computes, the COCO photos through the original model's
  test      the world `test` photos, the Alachua `test` photos and the COCO `test` rows, WASM vectors throughout;
            they choose nothing and are read once, at the end

The page is scored as it runs from build 22: in the county's time zone the head is combined with the county species
list by the rule `mix` (tools/fusion/fuse.py, src/cam.rec.js), the list's species relabelled to the groups carried
where the county list files them under `other`; elsewhere the head answers alone. So the world photos are scored by
the head alone, the Alachua photos with the list, and the COCO photos both ways. Today's page is scored as it runs
today, with the list everywhere. A vectorized copy of the rule is checked against fuse.py on a sample before use.

Steps, all on the tuning photos: (1) the fitting recipe (with or without the Alachua photos, and the power), with every
group carried; (2) with --groups fold, the groups carried: each must be named for 75% of its world tuning photos and be
right for 75% of the photos it is called for, and the worst failing group is put back in `other` and the head refitted
until every group carried passes (docs/COVERAGE.md: "a group that fails stays in `other` until it passes"); (3) t_kind
and w_kind for the county, the most Alachua photos right with the COCO photos within 1 point of today's page, and
kind_at, the level from which asserted kinds are right 95 times in 100 on each tuning set.

Usage: python3 -I tools/world/head.py ROOT --slot models/pocket --out OUT [--with-alachua both|yes|no] [--groups fold|all|a,b]
Writes OUT/report.json, OUT/REPORT.md and, for the chosen head, OUT/slot/ (kinds.f16.bin, manifest.json and
species.json relabelled) with OUT/slot/fitted_on.csv.
"""
import argparse
import csv
import hashlib
import json
import os
import shutil
import sys
import time
from collections import Counter, defaultdict

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "fusion"))
from groups import group_of, NEW  # noqa: E402
import fuse as F  # noqa: E402

MODEL = "tinyclip-39m-16"
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


def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def h8(s):
    return int(hashlib.sha256(s.encode()).hexdigest()[:8], 16)


def unit(X):
    X = np.asarray(X, dtype=np.float32)
    return X / np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-12)


def load_vec(root, name):
    p = os.path.join(root, "lab", MODEL, "images", name)
    if not os.path.exists(p + ".f16.npy"):
        return None, None
    return unit(np.load(p + ".f16.npy")), json.load(open(p + ".ids.json"))


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def licence_ok(s):
    s = (s or "").strip().lower().replace("_", "-")
    base = s.split("-4.0")[0].split("-3.0")[0].split("-2.0")[0].split("-1.0")[0]
    return base in ALLOWED or s in ("cc0-1.0", "public domain", "no known copyright restrictions", "united states government work")


# ---------------------------------------------------------------- photos

def world_sets(root):
    """The world photos: fit (torch vectors), tune and test (WASM vectors), each with group, continent and month."""
    out = {}
    fit = {r["id"]: r for r in read_csv(os.path.join(root, "world", "lab", "world-fit", "manifest.csv"))}
    X, ids = load_vec(root, "world-fit")
    keep = [i for i, j in enumerate(ids) if j in fit and licence_ok(fit[j]["licence"])]
    out["fit"] = {"X": X[keep], "y": np.array([fit[ids[i]]["group"] for i in keep]),
                  "cont": np.array([fit[ids[i]]["continent"] for i in keep]), "ids": [ids[i] for i in keep],
                  "month": np.array([int(fit[ids[i]]["date"][5:7]) - 1 for i in keep]), "rows": [fit[ids[i]] for i in keep]}
    ev = {r["id"]: r for r in read_csv(os.path.join(root, "world", "lab", "world-eval", "manifest.csv"))}
    Xw, idw = load_vec(root, "world-eval" + WASM)
    for s in ("tune", "test"):
        keep = [i for i, j in enumerate(idw) if j in ev and ev[j]["set"] == s]
        out[s] = {"X": Xw[keep], "y": np.array([ev[idw[i]]["group"] for i in keep]),
                  "cont": np.array([ev[idw[i]]["continent"] for i in keep]), "ids": [idw[i] for i in keep],
                  "month": np.array([int(ev[idw[i]]["date"][5:7]) - 1 for i in keep]),
                  "order": [ev[idw[i]]["order"] for i in keep], "cls": [ev[idw[i]]["class"] for i in keep]}
    Xt, idt = load_vec(root, "world-eval")
    keep = [i for i, j in enumerate(idt) if j in ev and ev[j]["set"] == "casual"]
    out["casual"] = {"X": Xt[keep], "y": np.array([ev[idt[i]]["group"] for i in keep]), "ids": [idt[i] for i in keep],
                     "month": np.array([int((ev[idt[i]]["date"] or "2025-06")[5:7]) - 1 for i in keep])}
    return out


def alachua_sets(root):
    """The county photos: training rows (torch vectors) and val and test (WASM vectors), labelled with today's kind of
    eye and with the new group, from GBIF's ranks in the county list."""
    sp = json.load(open(os.path.join(root, "data", "regions", "us-fl-alachua", "species.json")))["species"]
    by_key = {}
    for r in sp:
        eyes = r.get("eyes")
        names = {r.get(k) or "" for k in ("kingdom", "phylum", "class", "order", "family", "genus")}
        g = group_of(names, r.get("genus") or None, r.get("family") or None)
        by_key[str(r["key"])] = (eyes, g if eyes == "other" else eyes, r)
    out = {}
    man = {r["id"]: r for r in read_csv(os.path.join(root, "data", "train", "alachua-pre2025", "manifest.csv"))}
    X, ids = load_vec(root, "alachua-pre2025")
    keep = [i for i, j in enumerate(ids) if j in man and man[j]["key"] in by_key and licence_ok(man[j]["licence"])]
    out["fit"] = {"X": X[keep], "y": np.array([by_key[man[ids[i]]["key"]][1] for i in keep]),
                  "old": np.array([by_key[man[ids[i]]["key"]][0] for i in keep]), "ids": [ids[i] for i in keep],
                  "rows": [man[ids[i]] for i in keep]}
    ev = {r["id"]: r for r in read_csv(os.path.join(root, "data", "eval", "alachua-2025", "manifest.csv"))}
    Xw, idw = load_vec(root, "alachua-2025" + WASM)
    for s, split in (("tune", "val"), ("test", "test")):
        keep = [i for i, j in enumerate(idw) if j in ev and ev[j]["split"] == split and ev[j]["key"] in by_key]
        out[s] = {"X": Xw[keep], "y": np.array([by_key[ev[idw[i]]["key"]][1] for i in keep]),
                  "old": np.array([by_key[ev[idw[i]]["key"]][0] for i in keep]), "ids": [idw[i] for i in keep],
                  "month": np.array([int(ev[idw[i]]["month"]) - 1 for i in keep])}
    return out, by_key


def coco_sets(root):
    """The COCO extra set (people, pets, livestock under `deer`, rooms with nothing alive under `none`): fit and tune
    from the original model's vectors, test from the WASM vectors, as tools/eval/kinds.py cuts it."""
    man = {r["id"]: r for r in read_csv(os.path.join(root, "data", "extra", "coco-kinds", "manifest.csv"))}

    def part(r):
        return "test" if r["split"] == "test" else ("fit" if h8(r["id"]) % 3 < 2 else "tune")

    out = {}
    X, ids = load_vec(root, "coco-kinds")
    for s in ("fit", "tune"):
        keep = [i for i, j in enumerate(ids) if j in man and part(man[j]) == s and (s != "fit" or licence_ok(man[j].get("licence")))]
        out[s] = {"X": X[keep], "y": np.array([man[ids[i]]["eyes"] for i in keep]), "ids": [ids[i] for i in keep],
                  "month": np.array([h8("month|" + ids[i]) % 12 for i in keep]), "rows": [man[ids[i]] for i in keep]}
    Xw, idw = load_vec(root, "coco-kinds" + WASM)
    keep = [i for i, j in enumerate(idw) if j in man and part(man[j]) == "test"]
    out["test"] = {"X": Xw[keep], "y": np.array([man[idw[i]]["eyes"] for i in keep]), "ids": [idw[i] for i in keep],
                   "month": np.array([h8("month|" + idw[i]) % 12 for i in keep])}
    return out


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
    key = (id(X), len(X), id(table), tuple(table.kinds), hashlib.sha256(table.idx.tobytes()).hexdigest(), fusion["t_species"],
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
    """The fused kind and its probability for each photo, by the rule `mix` (or the head alone when table is None)."""
    z = fusion["t_kind"] * (X.astype(np.float64) @ K.T) + kb
    z -= z.max(axis=1, keepdims=True)
    p = np.exp(z); p /= p.sum(axis=1, keepdims=True)
    speaks = np.array([table is not None and lab in table.kinds for lab in labels])
    if table is not None and speaks.any():
        q = species_shares(X, months, table, fusion)
        Q = np.zeros_like(p)
        for i, lab in enumerate(labels):
            if speaks[i]:
                Q[:, i] = q[:, table.kinds.index(lab)]
        share = (p * speaks).sum(axis=1, keepdims=True)
        w = fusion["w_kind"]
        c = np.where(speaks, w * p + (1 - w) * share * Q, p)
        c /= c.sum(axis=1, keepdims=True)
    else:
        c = p
    best = np.argmax(c, axis=1)                    # ties go to the earlier label, as in the page
    kind = np.array([labels[b] for b in best], dtype=object)
    return kind, c[np.arange(len(c)), best]


def parity(slot_like, table_rows, X, months, n=60):
    """The vectorized rule against tools/fusion/fuse.py on n photos; returns the number of kinds that differ."""
    old = F.KINDS
    F.KINDS = tuple(KINDS_ALL)
    try:
        m, K, kb, tab = slot_like
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

def fit_head(X, y, power, labels):
    from sklearn.linear_model import LogisticRegression
    cls, cnt = np.unique(y, return_counts=True)
    sw = (cnt.astype(np.float64) ** -power)[np.searchsorted(cls, y)]
    sw *= len(y) / sw.sum()
    t0 = time.time()
    lr = LogisticRegression(C=C_REG, max_iter=1000).fit(X, y, sample_weight=sw)
    W = np.zeros((len(labels), X.shape[1])); b = np.full(len(labels), -50.0)
    for j, c in enumerate(lr.classes_):
        W[labels.index(c)], b[labels.index(c)] = lr.coef_[j], lr.intercept_[j]
    return W, b, {"iterations": int(np.max(lr.n_iter_)), "seconds": round(time.time() - t0, 1), "classes": len(lr.classes_)}


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


# ---------------------------------------------------------------- main

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


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("--slot", default="models/pocket")
    ap.add_argument("--out", required=True)
    ap.add_argument("--with-alachua", default="both", choices=("both", "yes", "no"))
    ap.add_argument("--powers", default="0,0.5,1")
    ap.add_argument("--groups", default="fold", help="'fold' (carry the groups that pass on the tuning photos), 'all', or a comma list")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rep = {"model": MODEL, "C": C_REG, "made": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "page": "away from the county's time zone the page leaves the county list out (the head alone); in it, the head and the list are combined by the rule mix"}

    W = world_sets(a.root); A, by_key = alachua_sets(a.root); X3 = coco_sets(a.root)
    for name, d in (("world", W), ("alachua", A), ("coco", X3)):
        rep.setdefault("photos", {})[name] = {s: int(len(v["y"])) for s, v in d.items()}
    log("photos", json.dumps(rep["photos"]))

    # today's head and table
    slot = F.load_slot(a.slot)
    m_old = slot["manifest"]
    K_old, kb_old = slot["kinds"], slot["kind_bias"]
    sci2group = {r["sci"]: g for (eyes, g, r) in by_key.values()}
    table_old = slot["table"]
    T_old = Table(slot, table_old, list(F.KINDS))
    bad = parity((m_old, K_old, kb_old, T_old), table_old, A["test"]["X"], A["test"]["month"])
    rep["parity_with_fuse_py"] = {"photos": 60, "different": bad}
    log("parity with fuse.py on 60 Alachua photos, today's slot:", bad, "different")
    if bad:
        sys.exit("the vectorized rule disagrees with tools/fusion/fuse.py")

    def table_for(carried):
        rows = [[r[0], r[1], (sci2group.get(r[0], "other") if r[2] == "other" else r[2]), r[3]] for r in table_old]
        rows = [[r[0], r[1], (r[2] if (r[2] not in NEW or r[2] in carried) else "other"), r[3]] for r in rows]
        return rows, Table(slot, rows, KINDS_ALL)

    def old_answers(d, fused=True):
        return answer(d["X"], d["month"], K_old, kb_old, m_old["kinds"]["labels"], m_old["fusion"], T_old if fused else None)

    COCO_KEYS = ("person", "none", "cat", "dog", "deer")
    today_coco_tune = balanced_share(old_answers(X3["tune"])[0], X3["tune"]["y"], COCO_KEYS)

    def settle(Wk, bk, labels, T, ya):
        """t_kind and w_kind for the page in the county: the most Alachua tuning photos right, with the COCO tuning
        photos (combined with the list, as there) within 1 point of today's page."""
        best = None
        for t_kind in (0.5, 1.0, 2.0):
            for w_kind in (0.3, 0.5, 0.7, 0.9, 1.0):
                fu = dict(m_old["fusion"], t_kind=t_kind, w_kind=w_kind, rule="mix")
                ka, _ = answer(A["tune"]["X"], A["tune"]["month"], Wk, t_kind * bk, labels, fu, T)
                kc, _ = answer(X3["tune"]["X"], X3["tune"]["month"], Wk, t_kind * bk, labels, fu, T)
                sa = float(np.mean(ka == ya)); sc = balanced_share(kc, X3["tune"]["y"], COCO_KEYS)
                key = (sc >= today_coco_tune - 0.01, sa if sc >= today_coco_tune - 0.01 else sc, w_kind)
                if best is None or key > best[0]:
                    best = (key, {"t_kind": t_kind, "w_kind": w_kind, "alachua": round(sa, 4), "coco": round(sc, 4)})
        return best[1]

    def head_alone(d, Wk, bk, labels, t_kind=1.0):
        fu = dict(m_old["fusion"], t_kind=t_kind)
        return answer(d["X"], d["month"], Wk, t_kind * bk, labels, fu, None)

    def fitting(with_a, carried):
        Xf = [W["fit"]["X"], X3["fit"]["X"]]; yf = [W["fit"]["y"], X3["fit"]["y"]]
        if with_a:
            Xf.append(A["fit"]["X"]); yf.append(A["fit"]["y"])
        return np.concatenate(Xf), folded(np.concatenate(yf), carried)

    # 1. the fitting recipe, with every group carried, chosen on the tuning photos
    mixes = {"no": [False], "yes": [True], "both": [False, True]}[a.with_alachua]
    powers = [float(p) for p in a.powers.split(",")]
    every = list(NEW)
    _, T_all = table_for(every)
    labels_all = OLD + every
    grid = []
    for with_a in mixes:
        Xf, yf = fitting(with_a, every)
        for pw in powers:
            Wk, bk, info = fit_head(Xf, yf, pw, labels_all)
            kw, _ = head_alone(W["tune"], Wk, bk, labels_all)
            sw = balanced_share(kw, W["tune"]["y"], sorted(set(W["tune"]["y"])))
            st = settle(Wk, bk, labels_all, T_all, A["tune"]["y"])
            g = {"with_alachua": with_a, "power": pw, "world_alone": round(sw, 4), **st, "score": round((sw + st["alachua"] + st["coco"]) / 3, 4), **info}
            grid.append(g)
            log("recipe", json.dumps(g))
    recipe = max(grid, key=lambda g: g["score"])
    rep["recipe"] = {"grid": grid, "chosen": recipe}

    # 2. the groups carried: each must be named for 75% of its world tuning photos and be right for 75% of the photos
    # called by it (the head alone, as the page away from the county); the worst is put back in `other` and the head
    # refitted until every group carried passes
    if a.groups == "fold":
        carried = list(NEW)
    elif a.groups == "all":
        carried = list(NEW)
    else:
        carried = [g for g in NEW if g in a.groups.split(",")]
    history = []
    while True:
        labels = OLD + carried
        Xf, yf = fitting(recipe["with_alachua"], carried)
        Wk, bk, info = fit_head(Xf, yf, recipe["power"], labels)
        yw = folded(W["tune"]["y"], carried)
        kw, _ = head_alone(W["tune"], Wk, bk, labels)
        marks = group_marks(kw, yw, carried)
        fails = {g: m for g, m in marks.items() if not m["pass"]}
        history.append({"carried": list(carried), "marks": marks, "world_tune_right": round(float(np.mean(kw == yw)), 4)})
        log("carried %d, failing %d: %s" % (len(carried), len(fails), ", ".join("%s %s/%s" % (g, m["named"], m["right_when_called"]) for g, m in sorted(marks.items()))))
        if a.groups != "fold" or not fails:
            break
        worst = min(fails, key=lambda g: min(fails[g]["named"] or 0, fails[g]["right_when_called"] or 0))
        carried.remove(worst)
        log("put back in other:", worst)
    rep["groups"] = {"rule": a.groups, "history": history, "carried": carried, "left_in_other": [g for g in NEW if g not in carried]}
    rep["labels"] = labels
    table_new, T_new = table_for(carried)
    rep["table_relabelled"] = dict(Counter(r[2] for r, o in zip(table_new, table_old) if o[2] == "other"))

    # 3. the settings for the page in the county, and the level under which it is not sure
    st = settle(Wk, bk, labels, T_new, folded(A["tune"]["y"], carried))
    fu = dict(m_old["fusion"], t_kind=st["t_kind"], w_kind=st["w_kind"], rule="mix")
    kb = st["t_kind"] * bk
    kw, pw_ = head_alone(W["tune"], Wk, bk, labels, st["t_kind"])
    ka, pa = answer(A["tune"]["X"], A["tune"]["month"], Wk, kb, labels, fu, T_new)
    kc, pc = answer(X3["tune"]["X"], X3["tune"]["month"], Wk, kb, labels, fu, T_new)
    levels = {"world": kind_at_level(kw, pw_, folded(W["tune"]["y"], carried)), "alachua": kind_at_level(ka, pa, folded(A["tune"]["y"], carried)),
              "coco": kind_at_level(kc, pc, X3["tune"]["y"])}
    fu["kind_at"] = max(levels.values())
    rep["settings"] = {**st, "kind_at": fu["kind_at"], "levels": levels, "bar": 0.95}
    log("settings", json.dumps(rep["settings"]))

    # 4. the test photos, once: today's page against the new head as the page would use it
    res = {}
    yw = folded(W["test"]["y"], carried); ya = folded(A["test"]["y"], carried)
    ko_w, _ = old_answers(W["test"]); kn_w, pn_w = head_alone(W["test"], Wk, bk, labels, st["t_kind"])
    kf_w, _ = answer(W["test"]["X"], W["test"]["month"], Wk, kb, labels, fu, T_new)
    ko_a, _ = old_answers(A["test"]); kn_a, pn_a = answer(A["test"]["X"], A["test"]["month"], Wk, kb, labels, fu, T_new)

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
    kc_old, _ = old_answers(X3["test"])
    kc_new, _ = answer(X3["test"]["X"], X3["test"]["month"], Wk, kb, labels, fu, T_new)
    kc_alone, _ = head_alone(X3["test"], Wk, bk, labels, st["t_kind"])
    so = balanced_share(kc_old, X3["test"]["y"], COCO_KEYS)
    sn = balanced_share(kc_new, X3["test"]["y"], COCO_KEYS); sa_ = balanced_share(kc_alone, X3["test"]["y"], COCO_KEYS)
    res["coco"] = {"today": round(so, 4), "new_with_list": round(sn, 4), "new_alone": round(sa_, 4), "pass": bool(sn >= so - 0.01 and sa_ >= so - 0.01),
                   "named_a_new_group": int(np.isin(kc_new, NEW).sum() + np.isin(kc_alone, NEW).sum()), "photos": int(len(kc_new))}
    truth_raw = W["test"]["y"]
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
    orders = Counter(); orders_view = Counter()
    for i in np.where(so_)[0]:
        o = W["test"]["order"][i] or W["test"]["cls"][i] or "?"
        orders[o] += 1
        if kn_w[i] in VIEWS:
            orders_view[(o, kn_w[i])] += 1
    res["other"]["original_other_given_a_view_by_order"] = [{"order": o, "view": v, "photos": n} for (o, v), n in orders_view.most_common(20)]
    res["world_all"] = {"right_new": round(float(np.mean(kn_w == yw)), 4), "right_today": round(float(np.mean(ko_w == yw)), 4),
                        "asserted_new": round(float(np.mean(pn_w >= fu["kind_at"])), 4),
                        "right_when_asserted_new": round(float(np.mean(kn_w[pn_w >= fu["kind_at"]] == yw[pn_w >= fu["kind_at"]])), 4)}
    res["alachua_all"] = {"right_new": round(float(np.mean(kn_a == ya)), 4), "right_today": round(float(np.mean(ko_a == ya)), 4),
                          "asserted_new": round(float(np.mean(pn_a >= fu["kind_at"])), 4),
                          "right_when_asserted_new": round(float(np.mean(kn_a[pn_a >= fu["kind_at"]] == ya[pn_a >= fu["kind_at"]])), 4)}
    res["world_by_continent"] = {c: {"photos": int((W["test"]["cont"] == c).sum()),
                                     "right_new": round(float(np.mean(kn_w[W["test"]["cont"] == c] == yw[W["test"]["cont"] == c])), 4),
                                     "right_today": round(float(np.mean(ko_w[W["test"]["cont"] == c] == yw[W["test"]["cont"] == c])), 4)}
                                 for c in sorted(set(W["test"]["cont"]))}
    conf = Counter((t, k) for t, k in zip(yw, kn_w) if t != k)
    res["commonest_confusions"] = [{"truth": t, "answer": k, "photos": n} for (t, k), n in conf.most_common(25)]
    res["size_bytes"] = int(len(labels) * Wk.shape[1] * 2)
    res["blocking"] = {"old_groups_world": res["old_groups_world"]["pass"], "old_groups_alachua": res["old_groups_alachua"]["pass"],
                       "new_groups": all(m["pass"] for m in res["new_groups"].values()), "coco": res["coco"]["pass"],
                       "size": res["size_bytes"] < 50000}
    rep["test"] = res
    rep["fitted"] = info

    # the candidate slot
    sd = os.path.join(a.out, "slot")
    os.makedirs(sd, exist_ok=True)
    Wk.astype("<f2").tofile(os.path.join(sd, "kinds.f16.bin"))
    man = json.loads(json.dumps(m_old))
    man["kinds"] = dict(man["kinds"], labels=labels, bias=[round(float(v), 5) for v in kb],
                        made_from="tools/world/head.py, world photos of pub/data-world" + (" and the Alachua training photos" if recipe["with_alachua"] else ""))
    man["fusion"] = dict(man["fusion"], t_kind=fu["t_kind"], w_kind=fu["w_kind"], kind_at=fu["kind_at"], rule="mix")
    json.dump(man, open(os.path.join(sd, "manifest.json"), "w"), indent=1)
    sj = json.load(open(os.path.join(a.slot, man["species"]["table"])))
    sj = dict(sj, species=table_new) if isinstance(sj, dict) else table_new
    json.dump(sj, open(os.path.join(sd, os.path.basename(man["species"]["table"])), "w"), ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(sd, "fitted_on.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["id", "label", "photo_url", "licence", "obs_url"])
        for r, lab in zip(W["fit"]["rows"], folded(W["fit"]["y"], carried)):
            w.writerow([r["id"], lab, r["photo_url"], r["licence"], r["obs_url"]])
        for r, lab in zip(X3["fit"]["rows"], X3["fit"]["y"]):
            w.writerow([r["id"], lab, r.get("photo_url", ""), r.get("licence", ""), r.get("obs_url", "")])
        if recipe["with_alachua"]:
            for r, lab in zip(A["fit"]["rows"], folded(A["fit"]["y"], carried)):
                w.writerow([r["id"], lab, r.get("photo_url", ""), r.get("licence", ""), r.get("obs_url", "")])
    json.dump(rep, open(os.path.join(a.out, "report.json"), "w"), indent=1)
    write_md(rep, os.path.join(a.out, "REPORT.md"))
    log("written", a.out)


def write_md(rep, path):
    t = rep["test"]
    yes = lambda b: "yes" if b else "no"
    L = ["# The group head on world photos", "", "Made by `tools/world/head.py` (%s). The page is scored as it would run: %s." % (rep["made"], rep["page"]), ""]
    ch = rep["recipe"]["chosen"]
    L.append("Recipe chosen on the tuning photos: power %s, %s. Groups carried (%d): %s. Put back in `other` (%d): %s." % (
        ch["power"], "with the Alachua training photos" if ch["with_alachua"] else "world and COCO photos only",
        len(rep["groups"]["carried"]), ", ".join(rep["groups"]["carried"]) or "none",
        len(rep["groups"]["left_in_other"]), ", ".join(rep["groups"]["left_in_other"]) or "none"))
    s = rep["settings"]
    L.append("Settings for the county: t_kind %s, w_kind %s, kind_at %s (levels %s)." % (s["t_kind"], s["w_kind"], s["kind_at"], s["levels"]))
    L += ["", "| Pass mark | Measured | Passes |", "|---|---|---|"]
    for key, what in (("old_groups_world", "world test photos, the head alone (away from the county)"), ("old_groups_alachua", "Alachua test photos, head and list combined")):
        d = t[key]
        L.append("| Old groups right, %s: 95%% interval of the paired difference above −2 points | today %s, new %s, difference %s (%s to %s), %d photos | %s |" % (
            what, d["today"][0], d["new"][0], d["difference"][0], d["difference"][1], d["difference"][2], d["difference"][3], yes(d["pass"])))
    npass = sum(1 for g in t["new_groups"].values() if g["pass"])
    L.append("| Every group carried found (named and right when called, 75%% or more each, world test photos, head alone) | %d of %d pass | %s |" % (npass, len(t["new_groups"]), yes(npass == len(t["new_groups"]))))
    L.append("| People, pets and rooms within 1 point of today (COCO test) | today %s; new with the list %s, alone %s; a new group named %d times in %d answers | %s |" % (
        t["coco"]["today"], t["coco"]["new_with_list"], t["coco"]["new_alone"], t["coco"]["named_a_new_group"], 2 * t["coco"]["photos"], yes(t["coco"]["pass"])))
    L.append("| `other` given a view under 10%% (world test photos, head alone) | today %s, new %s, of %d photos | %s |" % (
        t["other"]["given_a_view_today"], t["other"]["given_a_view_new"], t["other"]["photos"], yes(t["other"]["pass"])))
    L.append("| Head under 50 KB | %d bytes | %s |" % (t["size_bytes"], yes(t["size_bytes"] < 50000)))
    d = t["old_groups_world_with_list"]
    L += ["", "For the record, the world test photos with the county list combined (as in the county's time zone): old groups today %s, new %s, difference %s (%s to %s)." % (
        d["today"][0], d["new"][0], d["difference"][0], d["difference"][1], d["difference"][2])]
    L += ["", "| Group carried | test photos | named | called | right when called | passes |", "|---|---:|---:|---:|---:|---|"]
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
    L += ["", "The fold, on the tuning photos (carried, failing):"]
    for h in rep["groups"]["history"]:
        fails = [g for g, m in h["marks"].items() if not m["pass"]]
        L.append("- %d carried, world right %s; failing: %s" % (len(h["carried"]), h["world_tune_right"], ", ".join("%s %s/%s" % (g, h["marks"][g]["named"], h["marks"][g]["right_when_called"]) for g in fails) or "none"))
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
