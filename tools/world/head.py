#!/usr/bin/env python3
"""Fit the pocket model's group head on the world photos, choose its settings on the tuning photos, and score it against
the pass marks of docs/COVERAGE.md on the test photos, beside the head the page ships today.

The head is the same kind of head as the shipped one (tools/eval/study2.py): logistic regression with C = 20 on
TinyCLIP 39M/16's unit image vectors from the original model, a photo weighted by its group's count to the power
-`power`, fitted on photos allowed by the licence rule `nc`. Its labels are the seventeen of today's head followed by
the nineteen groups of GROUPS in src/cam.a.js, 36 rows of 512 numbers (36,864 bytes in half precision).

Photos (ROOT is laid out as tools/eval/fetch.py lays it out, with pub/data-world in ROOT/world):
  fitting   the world photos (`fit`, dated through 2024), the COCO extra set's fit part, and with --with-alachua the
            Alachua training photos too, each labelled by tools/world/groups.py from GBIF's ranks in the county list
  tuning    the world `tune` photos, the Alachua `val` photos and the COCO `tune` part; the world and Alachua photos
            through the vectors the phone's WASM runtime computes, the COCO photos through the original model's
  test      the world `test` photos, the Alachua `test` photos and the COCO `test` rows, WASM vectors throughout;
            they choose nothing

The answer is scored as the page gives it: the head combined with the county species list by the rule `mix`
(tools/fusion/fuse.py, src/cam.rec.js), the list's kinds relabelled to the nineteen groups where the county list
files a species under `other`. A vectorized copy of the rule is checked against fuse.py on a sample before use.

Usage: python3 -I tools/world/head.py ROOT --slot models/pocket --out OUT [--with-alachua both|yes|no]
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
                  "month": np.array([int(ev[idw[i]]["date"][5:7]) - 1 for i in keep])}
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
    key = (id(X), len(X), id(table), fusion["t_species"], fusion.get("alpha_prior"), fusion.get("prior_floor", 1e-6))
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

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("root")
    ap.add_argument("--slot", default="models/pocket")
    ap.add_argument("--out", required=True)
    ap.add_argument("--with-alachua", default="both", choices=("both", "yes", "no"))
    ap.add_argument("--powers", default="0,0.5,1")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rep = {"model": MODEL, "labels": LABELS, "C": C_REG, "made": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

    W = world_sets(a.root); A, by_key = alachua_sets(a.root); X3 = coco_sets(a.root)
    for name, d in (("world", W), ("alachua", A), ("coco", X3)):
        rep.setdefault("photos", {})[name] = {s: int(len(v["y"])) for s, v in d.items()}
    log("photos", json.dumps(rep["photos"]))

    # today's head and table, and the table relabelled to the groups
    slot = F.load_slot(a.slot)
    m_old = slot["manifest"]
    K_old, kb_old = slot["kinds"], slot["kind_bias"]
    sci2group = {r["sci"]: g for (eyes, g, r) in by_key.values()}
    table_old = slot["table"]
    table_new = [[r[0], r[1], (sci2group.get(r[0], "other") if r[2] == "other" else r[2]), r[3]] for r in table_old]
    moved = Counter(r[2] for r, o in zip(table_new, table_old) if o[2] == "other")
    rep["table_relabelled"] = dict(moved)
    T_old = Table(slot, table_old, list(F.KINDS)); T_new = Table(slot, table_new, KINDS_ALL)
    bad = parity((m_old, K_old, kb_old, T_old), table_old, A["test"]["X"], A["test"]["month"])
    rep["parity_with_fuse_py"] = {"photos": 60, "different": bad}
    log("parity with fuse.py on 60 Alachua photos, today's slot:", bad, "different")
    if bad:
        sys.exit("the vectorized rule disagrees with tools/fusion/fuse.py")

    def old_answers(d, fused=True):
        return answer(d["X"], d["month"], K_old, kb_old, m_old["kinds"]["labels"], m_old["fusion"], T_old if fused else None)

    # fitting sets
    mixes = {"no": [False], "yes": [True], "both": [False, True]}[a.with_alachua]
    powers = [float(p) for p in a.powers.split(",")]
    cands = []
    for with_a in mixes:
        Xf = [W["fit"]["X"], X3["fit"]["X"]]; yf = [W["fit"]["y"], X3["fit"]["y"]]
        if with_a:
            Xf.append(A["fit"]["X"]); yf.append(A["fit"]["y"])
        Xf = np.concatenate(Xf); yf = np.concatenate(yf)
        for pw in powers:
            Wk, bk, info = fit_head(Xf, yf, pw, LABELS)
            info.update(with_alachua=with_a, power=pw, photos=int(len(yf)))
            log("fitted", json.dumps(info))
            cands.append((Wk, bk, info))

    # choose settings on the tuning photos: the head, t_kind and w_kind, by the mean of three shares
    def tuned(Wk, bk, t_kind, w_kind):
        fu = dict(m_old["fusion"], t_kind=t_kind, w_kind=w_kind, rule="mix")
        kb = t_kind * bk
        kw, pw_ = answer(W["tune"]["X"], W["tune"]["month"], Wk, kb, LABELS, fu, T_new)
        ka, pa = answer(A["tune"]["X"], A["tune"]["month"], Wk, kb, LABELS, fu, T_new)
        kc, pc = answer(X3["tune"]["X"], X3["tune"]["month"], Wk, kb, LABELS, fu, T_new)
        sw = balanced_share(kw, W["tune"]["y"], sorted(set(W["tune"]["y"])))
        sa = float(np.mean(ka == A["tune"]["y"]))
        sc = balanced_share(kc, X3["tune"]["y"], ("person", "none", "cat", "dog", "deer"))
        return (sw + sa + sc) / 3, sw, sa, sc, (kw, pw_, ka, pa, kc, pc)

    grid = []
    for ci_, (Wk, bk, info) in enumerate(cands):
        for t_kind in (0.5, 1.0, 2.0):
            for w_kind in (0.5, 0.7, 0.9, 1.0):
                score, sw, sa, sc, _ = tuned(Wk, bk, t_kind, w_kind)
                grid.append({"cand": ci_, "t_kind": t_kind, "w_kind": w_kind, "score": round(score, 4), "world": round(sw, 4),
                             "alachua": round(sa, 4), "coco": round(sc, 4), **{k: info[k] for k in ("with_alachua", "power")}})
        log("tuned candidate", ci_, max((g for g in grid if g["cand"] == ci_), key=lambda g: g["score"]))
    best = max(grid, key=lambda g: (g["score"], -g["cand"]))
    rep["tuning"] = {"grid": grid, "chosen": best}
    Wk, bk, info = cands[best["cand"]]
    fu = dict(m_old["fusion"], t_kind=best["t_kind"], w_kind=best["w_kind"], rule="mix")
    kb = best["t_kind"] * bk
    _, _, _, _, (kw, pw_, ka, pa, kc, pc) = tuned(Wk, bk, best["t_kind"], best["w_kind"])
    levels = {"world": kind_at_level(kw, pw_, W["tune"]["y"]), "alachua": kind_at_level(ka, pa, A["tune"]["y"]),
              "coco": kind_at_level(kc, pc, X3["tune"]["y"])}
    fu["kind_at"] = max(levels.values())
    rep["kind_at"] = {"levels": levels, "chosen": fu["kind_at"], "bar": 0.95}
    log("chosen", json.dumps(best), "kind_at", fu["kind_at"])

    # the test photos: today's head against the new one, both combined with the county list as the page does
    new = lambda d: answer(d["X"], d["month"], Wk, kb, LABELS, fu, T_new)
    res = {}
    # 1. old groups cost little: paired, on the photos whose group has a view
    for name, d in (("world", W["test"]), ("alachua", A["test"])):
        ko, _ = old_answers(d); kn, pn = new(d)
        truth = d["y"]
        sel = np.isin(truth, VIEWS)
        ro = (ko[sel] == truth[sel]).astype(float); rn = (kn[sel] == truth[sel]).astype(float)
        idx = boot(int(sel.sum()))
        res["old_groups_" + name] = {"today": ci_mean(ro, idx), "new": ci_mean(rn, idx), "difference": ci_mean(rn - ro, idx),
                                     "pass": bool(ci_mean(rn - ro, idx)[1] is not None and ci_mean(rn - ro, idx)[1] > -0.02)}
    # 2. every new group found, on the world test photos
    ko, _ = old_answers(W["test"]); kn, pn = new(W["test"]); y = W["test"]["y"]
    found = {}
    for g in NEW:
        tp = int(((kn == g) & (y == g)).sum()); n_g = int((y == g).sum()); called = int((kn == g).sum())
        rec = tp / n_g if n_g else None; prec = tp / called if called else None
        found[g] = {"photos": n_g, "named": round(rec, 4) if rec is not None else None, "called": called,
                    "right_when_called": round(prec, 4) if prec is not None else None,
                    "pass": bool(rec is not None and prec is not None and rec >= 0.75 and prec >= 0.75)}
    res["new_groups"] = found
    # 3. people, pets and rooms
    kc_old, _ = old_answers(X3["test"]); kc_new, _ = new(X3["test"])
    keys = ("person", "none", "cat", "dog", "deer")
    so = balanced_share(kc_old, X3["test"]["y"], keys); sn = balanced_share(kc_new, X3["test"]["y"], keys)
    res["coco"] = {"today": round(so, 4), "new": round(sn, 4), "pass": bool(sn >= so - 0.01),
                   "named_a_new_group": int(np.isin(kc_new, NEW).sum()), "photos": int(len(kc_new))}
    # 4. other stops lending the wrong eyes
    sel = y == "other"
    res["other"] = {"photos": int(sel.sum()), "given_a_view_today": round(float(np.isin(ko[sel], VIEWS).mean()), 4) if sel.any() else None,
                    "given_a_view_new": round(float(np.isin(kn[sel], VIEWS).mean()), 4) if sel.any() else None}
    res["other"]["pass"] = bool(res["other"]["given_a_view_new"] is not None and res["other"]["given_a_view_new"] < 0.10)
    # the whole world test set, the head alone, and what is asserted
    res["world_all"] = {"right_new": round(float(np.mean(kn == y)), 4),
                        "asserted_new": round(float(np.mean(pn >= fu["kind_at"])), 4),
                        "right_when_asserted_new": round(float(np.mean(kn[pn >= fu["kind_at"]] == y[pn >= fu["kind_at"]])), 4)}
    kh, _ = answer(W["test"]["X"], W["test"]["month"], Wk, kb, LABELS, fu, None)
    res["world_all"]["right_head_alone"] = round(float(np.mean(kh == y)), 4)
    by_cont = {}
    for c in sorted(set(W["test"]["cont"])):
        s = W["test"]["cont"] == c
        by_cont[c] = {"photos": int(s.sum()), "right_new": round(float(np.mean(kn[s] == y[s])), 4)}
    res["world_by_continent"] = by_cont
    conf = Counter((t, k) for t, k in zip(y, kn) if t != k)
    res["commonest_confusions"] = [{"truth": t, "answer": k, "photos": n} for (t, k), n in conf.most_common(25)]
    res["size_bytes"] = int(len(LABELS) * Wk.shape[1] * 2)
    rep["test"] = res
    rep["fitted"] = info

    # the candidate slot
    sd = os.path.join(a.out, "slot")
    os.makedirs(sd, exist_ok=True)
    Wk.astype("<f2").tofile(os.path.join(sd, "kinds.f16.bin"))
    man = json.loads(json.dumps(m_old))
    man["kinds"] = dict(man["kinds"], labels=LABELS, bias=[round(float(v), 5) for v in kb],
                        made_from="tools/world/head.py, world photos of pub/data-world" + (" and the Alachua training photos" if info["with_alachua"] else ""))
    man["fusion"] = dict(man["fusion"], t_kind=fu["t_kind"], w_kind=fu["w_kind"], kind_at=fu["kind_at"], rule="mix")
    json.dump(man, open(os.path.join(sd, "manifest.json"), "w"), indent=1)
    sj = json.load(open(os.path.join(a.slot, man["species"]["table"])))
    if isinstance(sj, dict):
        sj = dict(sj, species=table_new)
    else:
        sj = table_new
    json.dump(sj, open(os.path.join(sd, os.path.basename(man["species"]["table"])), "w"), ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(sd, "fitted_on.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["id", "label", "photo_url", "licence", "obs_url"])
        for r, lab in zip(W["fit"]["rows"], W["fit"]["y"]):
            w.writerow([r["id"], lab, r["photo_url"], r["licence"], r["obs_url"]])
        for r, lab in zip(X3["fit"]["rows"], X3["fit"]["y"]):
            w.writerow([r["id"], lab, r.get("photo_url", ""), r.get("licence", ""), r.get("obs_url", "")])
        if info["with_alachua"]:
            for r, lab in zip(A["fit"]["rows"], A["fit"]["y"]):
                w.writerow([r["id"], lab, r.get("photo_url", ""), r.get("licence", ""), r.get("obs_url", "")])
    json.dump(rep, open(os.path.join(a.out, "report.json"), "w"), indent=1)
    write_md(rep, os.path.join(a.out, "REPORT.md"))
    log("written", a.out)


def write_md(rep, path):
    t = rep["test"]
    L = ["# The group head on world photos", "", "Made by `tools/world/head.py` (%s)." % rep["made"], ""]
    ch = rep["tuning"]["chosen"]
    L.append("Chosen on the tuning photos: power %s, %s, t_kind %s, w_kind %s, kind_at %s (levels %s). Score %.4f (world %.4f, Alachua %.4f, COCO %.4f)." % (
        ch["power"], "with the Alachua training photos" if ch["with_alachua"] else "world and COCO photos only", ch["t_kind"], ch["w_kind"],
        rep["kind_at"]["chosen"], rep["kind_at"]["levels"], ch["score"], ch["world"], ch["alachua"], ch["coco"]))
    L += ["", "| Pass mark | Measured | Passes |", "|---|---|---|"]
    for name in ("world", "alachua"):
        d = t["old_groups_" + name]
        L.append("| Old groups right, %s test photos: 95%% interval of the paired difference above −2 points | today %s, new %s, difference %s (%s to %s), %d photos | %s |" % (
            name, d["today"][0], d["new"][0], d["difference"][0], d["difference"][1], d["difference"][2], d["difference"][3], "yes" if d["pass"] else "no"))
    npass = sum(1 for g in t["new_groups"].values() if g["pass"])
    L.append("| Every new group found (named and right when called, 75%% or more each) | %d of %d groups pass | %s |" % (npass, len(t["new_groups"]), "yes" if npass == len(t["new_groups"]) else "no"))
    L.append("| People, pets and rooms within 1 point of today (COCO test) | today %s, new %s; a new group named for %d of %d | %s |" % (
        t["coco"]["today"], t["coco"]["new"], t["coco"]["named_a_new_group"], t["coco"]["photos"], "yes" if t["coco"]["pass"] else "no"))
    L.append("| `other` given a view under 10%% | today %s, new %s, of %d photos | %s |" % (
        t["other"]["given_a_view_today"], t["other"]["given_a_view_new"], t["other"]["photos"], "yes" if t["other"]["pass"] else "no"))
    L.append("| Head under 50 KB | %d bytes | %s |" % (t["size_bytes"], "yes" if t["size_bytes"] < 50000 else "no"))
    L += ["", "| New group | test photos | named | called | right when called | passes |", "|---|---:|---:|---:|---:|---|"]
    for g, d in t["new_groups"].items():
        L.append("| %s | %d | %s | %d | %s | %s |" % (g, d["photos"], d["named"], d["called"], d["right_when_called"], "yes" if d["pass"] else "no"))
    L += ["", "World test photos, every group: right %s as the page gives it, %s by the head alone; asserted %s, right when asserted %s." % (
        t["world_all"]["right_new"], t["world_all"]["right_head_alone"], t["world_all"]["asserted_new"], t["world_all"]["right_when_asserted_new"])]
    L += ["", "By continent: " + "; ".join("%s %s of %d" % (c, d["right_new"], d["photos"]) for c, d in t["world_by_continent"].items()) + "."]
    L += ["", "Commonest confusions: " + "; ".join("%s as %s %d" % (c["truth"], c["answer"], c["photos"]) for c in t["commonest_confusions"][:15]) + "."]
    open(path, "w", encoding="utf-8").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
