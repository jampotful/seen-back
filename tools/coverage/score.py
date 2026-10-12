#!/usr/bin/env python3
"""What happens to the larger model's answers when its species list grows. Part of the coverage study (docs/COVERAGE.md).

The evaluation photos of Alachua County (data/eval/alachua-2025; settings chosen on `val`, figures from `test`) are scored
by BioCLIP 2 against lists of growing size: the Alachua County list, every species recorded within 100, 400 and 1600 km
of Gainesville, every species in a box round the lower 48 states, the world's 100,000 most recorded species, and every
species recorded anywhere. All lists come from research-grade observations dated through 2024 (tools/coverage/lists.py),
and all rows from one sentence per species (tools/coverage/text.py). A photo whose species has no row in a list counts
as wrong for that list.

For each list: top-1 and top-5 with no prior; top-1 with a prior alpha * log(share), where share is the species' part of
the list region's observations (no season), alpha chosen on `val`; and what the app would do, naming a species only when
the top probability (softmax at temperature 100) clears a level chosen on `val` so that at least 98 named species in 100
are right. Intervals: 2000 bootstrap resamples over test photos, seed 20261011.

Usage: python3 -I tools/coverage/score.py --lists lists --rows rows --images IMG_PREFIX --live-rows ROWS_PREFIX --out out
"""
import argparse
import csv
import json
import os

import numpy as np

T = 100.0
ALPHAS = (0.0, 0.25, 0.5, 0.75, 1.0, 1.5)
CHUNK = 16384
rng = np.random.default_rng(20261011)
B = 2000


def unit(x):
    x = np.asarray(x, np.float32)
    n = np.linalg.norm(x, axis=1, keepdims=True)
    n[n == 0] = 1
    return x / n


def boot(x):
    x = np.asarray(x, np.float64)
    if len(x) == 0:
        return [None, None, None, 0]
    idx = rng.integers(0, len(x), size=(B, len(x)))
    b = x[idx].mean(1)
    return [float(x.mean()), float(np.percentile(b, 2.5)), float(np.percentile(b, 97.5)), int(len(x))]


def level(conf, hit, floor=0.98, least=50):
    good = None
    for tau in np.round(np.arange(0.99, 0.0049, -0.01), 2):
        m = conf >= tau
        if m.sum() < least:
            continue
        if hit[m].mean() >= floor:
            good = float(tau)
        else:
            break
    return good


def run(Rget, nrows, X, truth, lists, alphas_of):
    """One pass over the rows. lists: name -> (mask bool[nrows], logshare float32[nrows]). Returns per (list, alpha):
    top row, count of rows above the true species, log-sum-exp, best adjusted score."""
    M = X.shape[0]
    combos = [(L, al) for L in lists for al in alphas_of(L)]
    st = {c: {"cnt": np.zeros(M, np.int64), "best": np.full(M, -np.inf, np.float64), "arg": np.full(M, -1, np.int64),
              "lm": np.full(M, -np.inf, np.float64), "ls": np.zeros(M, np.float64)} for c in combos}
    has = truth >= 0
    tc = np.full(M, np.nan, np.float32)
    # the true species' score, from the same rows
    for a in range(0, nrows, CHUNK):
        b = min(nrows, a + CHUNK)
        sel = has & (truth >= a) & (truth < b)
        if sel.any():
            Rc = Rget(a, b)
            tc[sel] = np.einsum("ij,ij->i", X[sel], Rc[truth[sel] - a])
    true_adj = {}
    for (L, al) in combos:
        mask, ls = lists[L]
        t = np.full(M, -np.inf, np.float64)
        ok = has & mask[np.maximum(truth, 0)]
        t[ok] = T * tc[ok].astype(np.float64) + al * ls[truth[ok]]
        true_adj[(L, al)] = t
    for a in range(0, nrows, CHUNK):
        b = min(nrows, a + CHUNK)
        Rc = Rget(a, b)
        S = (X @ Rc.T) * np.float32(T)
        for L in lists:
            mask, ls = lists[L]
            cols = np.nonzero(mask[a:b])[0]
            if len(cols) == 0:
                continue
            SL = S if len(cols) == (b - a) else S[:, cols]
            lsc = ls[a:b][cols].astype(np.float32)
            for al in alphas_of(L):
                adj = SL if al == 0 else SL + np.float32(al) * lsc[None, :]
                s = st[(L, al)]
                s["cnt"] += (adj > (true_adj[(L, al)][:, None] + 1e-4)).sum(1)
                am = adj.argmax(1)
                mx = adj[np.arange(M), am].astype(np.float64)
                upd = mx > s["best"]
                s["best"][upd] = mx[upd]
                s["arg"][upd] = a + cols[am[upd]]
                m2 = np.maximum(s["lm"], mx)
                s["ls"] = s["ls"] * np.exp(s["lm"] - m2) + np.exp(adj.astype(np.float64) - m2[:, None]).sum(1)
                s["lm"] = m2
    out = {}
    for c in combos:
        s = st[c]
        out[c] = {"arg": s["arg"], "cnt": s["cnt"], "p": np.exp(s["best"] - (s["lm"] + np.log(s["ls"])))}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lists", required=True)
    ap.add_argument("--rows", required=True)
    ap.add_argument("--images", required=True, help="prefix of <prefix>.f16.npy and <prefix>.ids.json (BioCLIP 2, alachua-2025)")
    ap.add_argument("--live-rows", default="", help="prefix of the live species_sci rows (.f16.npy, .labels.json), for comparison")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)

    W = list(csv.DictReader(open(os.path.join(a.lists, "world.tsv"), encoding="utf-8"), delimiter="\t"))
    N = len(W)
    col = lambda k: np.array([int(r[k]) for r in W], np.int64)
    rg, inal = col("rg_2024"), col("in_alachua_list").astype(bool)
    reg = {k: col(k) for k in ("alachua_2024", "gnv100_2024", "gnv400_2024", "gnv1600_2024", "usa48_2024")}
    parts = sorted(f for f in os.listdir(a.rows) if f.startswith("rows.") and f.endswith(".f16.npy"))
    R = np.concatenate([np.load(os.path.join(a.rows, f)) for f in parts]).astype(np.float16)
    assert R.shape[0] == N, (R.shape, N)
    print("rows", R.shape, flush=True)

    X = unit(np.load(a.images + ".f16.npy"))
    ids = json.load(open(a.images + ".ids.json"))
    if isinstance(ids, dict):
        ids = ids.get("ids")
    tr = {r["id"]: r for r in csv.DictReader(open(os.path.join(a.lists, "eval_truth.csv"), encoding="utf-8"))}
    keep = [i for i, x in enumerate(ids) if x in tr]
    X = X[keep]
    ids = [ids[i] for i in keep]
    truth = np.array([int(tr[x]["row"]) for x in ids], np.int64)
    split = np.array([tr[x]["split"] for x in ids])
    eyes = np.array([tr[x]["eyes"] for x in ids])
    val, test = split == "val", split == "test"
    print("photos", len(ids), "val", int(val.sum()), "test", int(test.sum()), "with a row", int((truth >= 0).sum()), flush=True)

    rank = np.empty(N, np.int64)
    rank[np.argsort(-rg, kind="stable")] = np.arange(N)

    def logshare(c, mask):
        c = c.astype(np.float64)
        tot = c[mask].sum() + mask.sum()
        return np.log((c + 1.0) / tot).astype(np.float32)

    lists = {}
    spec = [
        ("Alachua County list", inal, reg["alachua_2024"]),
        ("within 100 km", reg["gnv100_2024"] > 0, reg["gnv100_2024"]),
        ("within 400 km", reg["gnv400_2024"] > 0, reg["gnv400_2024"]),
        ("within 1600 km", reg["gnv1600_2024"] > 0, reg["gnv1600_2024"]),
        ("lower 48 states", reg["usa48_2024"] > 0, reg["usa48_2024"]),
        ("world, 100,000 commonest", (rank < 100000) & (rg > 0), rg),
        ("world, every species", (rg > 0) | inal, rg),
    ]
    for name, mask, c in spec:
        lists[name] = (mask, logshare(c, mask))
    Rget = lambda lo, hi: R[lo:hi].astype(np.float32)
    res = run(Rget, N, X, truth, lists, lambda L: ALPHAS)

    out = {"photos": {"all": len(ids), "val": int(val.sum()), "test": int(test.sum())}, "rows": N, "lists": []}
    base_hit = None
    chosen = {}
    for name, mask, c in spec:
        sizes = int(mask.sum())
        inl = (truth >= 0) & mask[np.maximum(truth, 0)]
        per = {}
        for al in ALPHAS:
            r = res[(name, al)]
            hit = (r["arg"] == truth) & inl
            per[al] = {"hit": hit, "top5": (r["cnt"] < 5) & inl, "p": r["p"]}
        al_best = max(ALPHAS, key=lambda al: (per[al]["hit"][val].mean(), -al))
        chosen[name] = al_best
        e = {"list": name, "species": sizes, "mb_float16": round(sizes * R.shape[1] * 2 / 1e6, 1), "mb_int8": round(sizes * R.shape[1] / 1e6, 1),
             "test_species_in_list": boot(inl[test]), "alpha": al_best}
        for tag, al in (("no_prior", 0.0), ("prior", al_best)):
            h, t5, p = per[al]["hit"], per[al]["top5"], per[al]["p"]
            tau = level(p[val], h[val])
            named = (p >= tau) if tau is not None else np.zeros(len(p), bool)
            e[tag] = {"top1": boot(h[test]), "top5": boot(t5[test]), "name_at": tau, "named": boot(named[test]),
                      "named_right": boot(h[test & named]), "tuning_top1": float(h[val].mean())}
        if base_hit is None:
            base_hit = {"no_prior": per[0.0]["hit"], "prior": per[al_best]["hit"]}
        e["paired_vs_alachua_list"] = {"no_prior": boot((per[0.0]["hit"].astype(float) - base_hit["no_prior"].astype(float))[test]),
                                       "prior": boot((per[al_best]["hit"].astype(float) - base_hit["prior"].astype(float))[test])}
        if name in ("Alachua County list", "world, every species"):
            h = per[al_best]["hit"]
            e["top1_by_kind"] = {k: [float(h[test & (eyes == k)].mean()), int((test & (eyes == k)).sum())] for k in sorted(set(eyes.tolist())) if (test & (eyes == k)).sum() >= 20}
        out["lists"].append(e)
        print("%-26s %7d  in list %.3f  top1 %.4f  prior(a=%.2f) %.4f  named %.3f right %.3f" % (
            name, sizes, e["test_species_in_list"][0], e["no_prior"]["top1"][0], al_best, e["prior"]["top1"][0],
            e["prior"]["named"][0] or 0, e["prior"]["named_right"][0] or 0), flush=True)

    # the world list with int8 rows (the download would be half the size)
    def q8(lo, hi):
        r = R[lo:hi].astype(np.float32)
        s = np.abs(r).max(1, keepdims=True) / 127.0
        s[s == 0] = 1
        return unit(np.clip(np.round(r / s), -127, 127) * s)
    wname = "world, every species"
    res8 = run(q8, N, X, truth, {wname: lists[wname]}, lambda L: (0.0, chosen[wname]))
    mask = lists[wname][0]
    inl = (truth >= 0) & mask[np.maximum(truth, 0)]
    out["world_int8_rows"] = {}
    for al in (0.0, chosen[wname]):
        h8 = (res8[(wname, al)]["arg"] == truth) & inl
        h16 = (res[(wname, al)]["arg"] == truth) & inl
        out["world_int8_rows"]["alpha %g" % al] = {"top1_int8": boot(h8[test]), "top1_float16": boot(h16[test]), "paired": boot((h8.astype(float) - h16.astype(float))[test])}

    # the live rows of the larger model (four sentences, GBIF's names), on the same photos, no prior
    if a.live_rows and os.path.exists(a.live_rows + ".f16.npy"):
        Rl = unit(np.load(a.live_rows + ".f16.npy"))
        lab = json.load(open(a.live_rows + ".labels.json", encoding="utf-8"))["labels"]
        kpos = {str(r["key"]): i for i, r in enumerate(lab)}
        tl = np.array([kpos.get(tr[x]["key"], -1) for x in ids], np.int64)
        S = X @ Rl.T
        hit = (S.argmax(1) == tl) & (tl >= 0)
        out["live_rows_alachua_no_prior"] = {"top1": boot(hit[test]), "rows": int(Rl.shape[0])}
        print("live rows, Alachua list, no prior: %.4f" % hit[test].mean(), flush=True)

    json.dump(out, open(os.path.join(a.out, "results.json"), "w"), indent=1)
    L = ["# Species lists of growing size, scored by BioCLIP 2 on the Alachua test photos", "",
         "Test photos: %d. Rows: one sentence per species. A photo whose species is not in a list counts as wrong." % int(test.sum()), "",
         "| List | Species | MB (float16) | MB (int8) | Test species in list | Top-1, no prior | Top-1, prior (alpha) | Top-5, prior | Named at the 98 in 100 level | Named and right | Top-1 against the Alachua list (points) |",
         "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    f = lambda v: "–" if v is None or v[0] is None else "%.1f%% (%.1f to %.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])
    g = lambda v: "–" if v is None or v[0] is None else "%+.1f (%+.1f to %+.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])
    for e in out["lists"]:
        L.append("| %s | %d | %.1f | %.1f | %s | %s | %s (%g) | %s | %s | %s | %s |" % (
            e["list"], e["species"], e["mb_float16"], e["mb_int8"], f(e["test_species_in_list"]), f(e["no_prior"]["top1"]),
            f(e["prior"]["top1"]), e["alpha"], f(e["prior"]["top5"]), f(e["prior"]["named"]), f(e["prior"]["named_right"]), g(e["paired_vs_alachua_list"]["prior"])))
    L += ["", "World list with int8 rows: " + json.dumps(out["world_int8_rows"])]
    if "live_rows_alachua_no_prior" in out:
        L += ["", "Live rows (four sentences, GBIF names), Alachua list, no prior: " + f(out["live_rows_alachua_no_prior"]["top1"])]
    open(os.path.join(a.out, "summary.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)


if __name__ == "__main__":
    main()
