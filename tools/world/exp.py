#!/usr/bin/env python3
"""Exploratory trials for the group head, on TUNING photos only (the test photos are never read here).
Imports tools/world/head.py from the worktree. Usage: python3 -I tools/world/exp.py ROOT WORKTREE TRIAL... (results: tools/world/EXPERIMENTS.md)"""
import json
import os
import sys
import time

import numpy as np

ROOT, WT = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.join(WT, "tools", "world"))
import head as H  # noqa: E402

F = H.F
t0 = time.time()
W = H.world_sets(ROOT)
A, by_key = H.alachua_sets(ROOT)
X3 = H.coco_sets(ROOT)
slot = F.load_slot(os.path.join(WT, "models", "pocket"))
m_old = slot["manifest"]
K_old, kb_old = slot["kinds"], slot["kind_bias"]
sci2group = {r["sci"]: g for (eyes, g, r) in by_key.values()}
table_old = slot["table"]
table_new = [[r[0], r[1], (sci2group.get(r[0], "other") if r[2] == "other" else r[2]), r[3]] for r in table_old]
T_old = H.Table(slot, table_old, list(F.KINDS))
T_new = H.Table(slot, table_new, H.KINDS_ALL)
print("loaded in %.0f s" % (time.time() - t0), flush=True)


def old_ans(d):
    return H.answer(d["X"], d["month"], K_old, kb_old, m_old["kinds"]["labels"], m_old["fusion"], T_old)


OLD_W = old_ans(W["tune"])[0]
OLD_A = old_ans(A["tune"])[0]
OLD_C = old_ans(X3["tune"])[0]


def score(Wk, bk, labels, t_kind, w_kind, table=T_new, quiet=False, tag=""):
    fu = dict(m_old["fusion"], t_kind=t_kind, w_kind=w_kind, rule="mix")
    kb = t_kind * bk
    kw, pw = H.answer(W["tune"]["X"], W["tune"]["month"], Wk, kb, labels, fu, table)
    ka, pa = H.answer(A["tune"]["X"], A["tune"]["month"], Wk, kb, labels, fu, table)
    kc, pc = H.answer(X3["tune"]["X"], X3["tune"]["month"], Wk, kb, labels, fu, table)
    yw, ya, yc = W["tune"]["y"], A["tune"]["y"], X3["tune"]["y"]
    out = {"tag": tag, "t_kind": t_kind, "w_kind": w_kind}
    for name, kn, ko, y in (("world", kw, OLD_W, yw), ("alachua", ka, OLD_A, ya)):
        sel = np.isin(y, H.VIEWS)
        out["old_" + name] = round(float(np.mean(kn[sel] == y[sel]) - np.mean(ko[sel] == y[sel])), 4)
    groups = {}
    for g in H.NEW:
        n = (yw == g).sum(); c = (kw == g).sum(); tp = ((kw == g) & (yw == g)).sum()
        groups[g] = (round(tp / n, 3) if n else None, round(tp / c, 3) if c else None)
    out["groups_pass"] = sum(1 for g, (r, p) in groups.items() if r is not None and p is not None and r >= 0.75 and p >= 0.75)
    out["groups_minrp"] = round(float(np.mean([min(r or 0, p or 0) for r, p in groups.values()])), 4)
    sel = yw == "other"
    out["other_view"] = round(float(np.isin(kw[sel], H.VIEWS).mean()), 4) if sel.any() else None
    keys = ("person", "none", "cat", "dog", "deer")
    out["coco"] = round(H.balanced_share(kc, yc, keys) - H.balanced_share(OLD_C, yc, keys), 4)
    out["world_all"] = round(float(np.mean(kw == yw)), 4)
    out["groups"] = groups
    if not quiet:
        print(json.dumps({k: v for k, v in out.items() if k != "groups"}), flush=True)
    return out


def fit_lr(Xf, yf, power, labels, C, mult=None):
    from sklearn.linear_model import LogisticRegression
    cls, cnt = np.unique(yf, return_counts=True)
    sw = (cnt.astype(np.float64) ** -power)[np.searchsorted(cls, yf)]
    if mult is not None:
        sw = sw * mult
    sw *= len(yf) / sw.sum()
    lr = LogisticRegression(C=C, max_iter=1000).fit(Xf, yf, sample_weight=sw)
    Wk = np.zeros((len(labels), Xf.shape[1])); b = np.full(len(labels), -50.0)
    for j, c in enumerate(lr.classes_):
        Wk[labels.index(c)], b[labels.index(c)] = lr.coef_[j], lr.intercept_[j]
    return Wk, b


def calibrate(Z, y, labels, groups, grid=np.arange(-3.0, 3.01, 0.25), passes=3):
    """Offsets for the groups' biases, by coordinate ascent on the sum of min(named, right when called)."""
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


def fitset(with_a=True, a_mult=1.0, c_mult=1.0):
    Xf = [W["fit"]["X"], X3["fit"]["X"]]; yf = [W["fit"]["y"], X3["fit"]["y"]]; mult = [np.ones(len(W["fit"]["y"])), np.full(len(X3["fit"]["y"]), c_mult)]
    if with_a:
        Xf.append(A["fit"]["X"]); yf.append(A["fit"]["y"]); mult.append(np.full(len(A["fit"]["y"]), a_mult))
    return np.concatenate(Xf), np.concatenate(yf), np.concatenate(mult)


if __name__ == "__main__":
    trials = sys.argv[3:]
    LAB = H.LABELS
    res = []
    if "today" in trials:
        # today's head on the tuning photos, as the baseline of every difference
        r = score(K_old, kb_old / m_old["fusion"]["t_kind"], m_old["kinds"]["labels"], m_old["fusion"]["t_kind"], m_old["fusion"]["w_kind"], table=T_old, tag="today")
    if "gap" in trials:
        # torch against WASM vectors for the same tuning photos
        Xt, idt = H.load_vec(ROOT, "world-eval")
        pos = {j: i for i, j in enumerate(idt)}
        Xa = W["tune"]["X"]; Xb = Xt[[pos[j] for j in W["tune"]["ids"]]]
        cos = (Xa * Xb).sum(1)
        print("cosine torch/WASM on world tune: mean %.4f, 5th pct %.4f" % (cos.mean(), np.percentile(cos, 5)), flush=True)
    if "C" in trials:
        Xf, yf, _ = fitset(True)
        for C in (2.0, 5.0, 20.0, 80.0):
            t1 = time.time(); Wk, bk = fit_lr(Xf, yf, 0.5, LAB, C)
            for tk in (0.5, 1.0):
                for wk in (0.7, 0.9):
                    res.append(score(Wk, bk, LAB, tk, wk, tag="C=%g" % C))
            print("C=%g fitted in %.0f s" % (C, time.time() - t1), flush=True)
    if "ceiling" in trials:
        # how separable the groups are on these vectors: the linear head, a small MLP and nearest neighbours, each alone
        Xf, yf, _ = fitset(True)
        yw = W["tune"]["y"]
        def report(tag, kw):
            groups = {g: (np.mean(kw[yw == g] == g), np.mean(yw[kw == g] == g) if (kw == g).any() else 0) for g in H.NEW}
            npass = sum(1 for r, p in groups.values() if r >= 0.75 and p >= 0.75)
            print(tag, "world tune right %.4f, groups passing %d, mean min(named, right when called) %.4f" % (np.mean(kw == yw), npass, np.mean([min(r, p) for r, p in groups.values()])), flush=True)
            return groups
        t1 = time.time(); Wk, bk = fit_lr(Xf, yf, 0.5, LAB, 20.0)
        z = W["tune"]["X"] @ Wk.T + bk
        report("linear C=20", np.array(LAB, dtype=object)[z.argmax(1)]); print("  %.0f s" % (time.time() - t1), flush=True)
        t1 = time.time()
        from sklearn.neural_network import MLPClassifier
        mu = Xf.mean(0); sd = Xf.std(0) + 1e-6
        for hid in (64, 256):
            mlp = MLPClassifier(hidden_layer_sizes=(hid,), alpha=1e-4, batch_size=512, max_iter=40, early_stopping=True, n_iter_no_change=4, random_state=0)
            mlp.fit((Xf - mu) / sd, yf)
            kw = mlp.predict((W["tune"]["X"] - mu) / sd)
            report("mlp %d" % hid, np.asarray(kw, dtype=object)); print("  %.0f s, %d epochs" % (time.time() - t1, mlp.n_iter_), flush=True)
            t1 = time.time()
        Xn = Xf.astype(np.float32); ys = yf
        kws = []
        for a in range(0, len(yw), 1000):
            sim = W["tune"]["X"][a:a + 1000].astype(np.float32) @ Xn.T
            top = np.argpartition(-sim, 15, axis=1)[:, :15]
            for i in range(len(top)):
                vals = ys[top[i]]; w = np.exp(20 * sim[i, top[i]])
                tally = {}
                for v, ww in zip(vals, w):
                    tally[v] = tally.get(v, 0) + ww
                kws.append(max(tally, key=tally.get))
        report("15 nearest", np.array(kws, dtype=object)); print("  %.0f s" % (time.time() - t1), flush=True)
    if "fold" in trials:
        # greedy: carry the groups that pass on the world tuning photos (head alone, as the page away from the county);
        # drop the worst group, refit, until every carried group passes. The county photos fused, as the page there.
        Xf, yf0, _ = fitset(True)
        yw0 = W["tune"]["y"]; ya0 = A["tune"]["y"]
        carried = list(H.NEW)
        while True:
            fold = lambda y: np.array([v if (v not in H.NEW or v in carried) else "other" for v in y], dtype=object)
            yf, yw, ya = fold(yf0), fold(yw0), fold(ya0)
            labels = H.OLD + carried
            t1 = time.time(); Wk, bk = fit_lr(Xf, yf, 0.5, labels, 20.0)
            kw = np.array(labels, dtype=object)[(W["tune"]["X"] @ Wk.T + bk).argmax(1)]
            groups = {g: (float(np.mean(kw[yw == g] == g)), float(np.mean(yw[kw == g] == g)) if (kw == g).any() else 0.0) for g in carried}
            sel = np.isin(yw, H.VIEWS)
            old_w = float(np.mean(kw[sel] == yw[sel]) - np.mean(OLD_W[sel] == yw0[sel]))
            selo = yw == "other"
            other_view = float(np.isin(kw[selo], H.VIEWS).mean())
            tabl = [[r[0], r[1], (r[2] if (r[2] not in H.NEW or r[2] in carried) else "other"), r[3]] for r in table_new]
            T = H.Table(slot, tabl, H.KINDS_ALL)
            best = None
            for tk in (0.5, 1.0, 2.0):
                for wk in (0.3, 0.5, 0.7, 0.9, 1.0):
                    fu = dict(m_old["fusion"], t_kind=tk, w_kind=wk, rule="mix")
                    ka, _ = H.answer(A["tune"]["X"], A["tune"]["month"], Wk, tk * bk, labels, fu, T)
                    sela = np.isin(ya, H.VIEWS)
                    d = float(np.mean(ka[sela] == ya[sela]) - np.mean(OLD_A[sela] == ya0[sela]))
                    kc, _ = H.answer(X3["tune"]["X"], X3["tune"]["month"], Wk, tk * bk, labels, fu, T)
                    dc = H.balanced_share(kc, X3["tune"]["y"], ("person", "none", "cat", "dog", "deer")) - H.balanced_share(OLD_C, X3["tune"]["y"], ("person", "none", "cat", "dog", "deer"))
                    if best is None or d > best[0]:
                        best = (d, tk, wk, dc)
            kc_alone = np.array(labels, dtype=object)[(X3["tune"]["X"] @ Wk.T + bk).argmax(1)]
            dca = H.balanced_share(kc_alone, X3["tune"]["y"], ("person", "none", "cat", "dog", "deer")) - H.balanced_share(OLD_C, X3["tune"]["y"], ("person", "none", "cat", "dog", "deer"))
            fails = {g: v for g, v in groups.items() if v[0] < 0.75 or v[1] < 0.75}
            print(json.dumps({"carried": len(carried), "fails": len(fails), "old_world_alone": round(old_w, 4), "other_view": round(other_view, 4),
                              "alachua_best": [round(best[0], 4), best[1], best[2]], "coco_fused": round(best[3], 4), "coco_alone": round(dca, 4),
                              "world_right": round(float(np.mean(kw == yw)), 4), "s": round(time.time() - t1)}), flush=True)
            print("   ", {g: (round(r, 3), round(p, 3)) for g, (r, p) in sorted(groups.items(), key=lambda kv: min(kv[1]))}, flush=True)
            res.append({"carried": list(carried), "groups": groups, "old_world": old_w, "other_view": other_view, "alachua": best})
            if not fails:
                break
            worst = min(fails, key=lambda g: min(fails[g]))
            carried.remove(worst)
            print("    drop", worst, flush=True)
    if "mix" in trials:
        carried = os.environ.get("CARRIED", "primate,whale,bat").split(",")
        fold = lambda y: np.array([v if (v not in H.NEW or v in carried) else "other" for v in y], dtype=object)
        labels = H.OLD + carried
        yw = fold(W["tune"]["y"]); ya = fold(A["tune"]["y"]); yc = X3["tune"]["y"]
        tabl = [[r[0], r[1], (r[2] if (r[2] not in H.NEW or r[2] in carried) else "other"), r[3]] for r in table_new]
        T = H.Table(slot, tabl, H.KINDS_ALL)
        keys = ("person", "none", "cat", "dog", "deer")
        today_c = H.balanced_share(OLD_C, yc, keys)
        sela = np.isin(ya, H.VIEWS); selw = np.isin(yw, H.VIEWS)
        base_a = float(np.mean(OLD_A[sela] == ya[sela])); base_w = float(np.mean(OLD_W[selw] == yw[selw]))
        print("today: alachua old %.4f, world old %.4f, coco %.4f" % (base_a, base_w, today_c), flush=True)
        for pw in [float(x) for x in os.environ.get("POWERS", "0,0.5,1").split(",")]:
            for am in [float(x) for x in os.environ.get("AMULTS", "1,3").split(",")]:
                Xf, yf0, mult = fitset(True, am)
                t1 = time.time(); Wk, bk = fit_lr(Xf, fold(yf0), pw, labels, 20.0, mult)
                kw = np.array(labels, dtype=object)[(W["tune"]["X"] @ Wk.T + bk).argmax(1)]
                marks = {g: (round(float(np.mean(kw[yw == g] == g)), 3), round(float(np.mean(yw[kw == g] == g)), 3) if (kw == g).any() else 0) for g in carried}
                dw = float(np.mean(kw[selw] == yw[selw])) - base_w
                kca = np.array(labels, dtype=object)[(X3["tune"]["X"] @ Wk.T + bk).argmax(1)]
                ca = H.balanced_share(kca, yc, keys) - today_c
                rows = []
                for tk in (0.5, 1.0, 2.0):
                    for wk in (0.3, 0.5, 0.7, 0.9, 1.0):
                        fu = dict(m_old["fusion"], t_kind=tk, w_kind=wk, rule="mix")
                        ka, _ = H.answer(A["tune"]["X"], A["tune"]["month"], Wk, tk * bk, labels, fu, T)
                        kc, _ = H.answer(X3["tune"]["X"], X3["tune"]["month"], Wk, tk * bk, labels, fu, T)
                        rows.append((round(float(np.mean(ka[sela] == ya[sela])) - base_a, 4), round(H.balanced_share(kc, yc, keys) - today_c, 4), tk, wk))
                feas = [r for r in rows if r[1] >= -0.01]
                best = max(feas) if feas else None
                print(json.dumps({"power": pw, "amult": am, "world_old": round(dw, 4), "coco_alone": round(ca, 4), "best_feasible": best,
                                  "best_any": max(rows), "marks": marks, "s": round(time.time() - t1)}), flush=True)
    if "calib" in trials:
        carried = [g for g in os.environ.get("CARRIED", ",".join(H.NEW)).split(",") if g]
        fold = lambda y: np.array([v if (v not in H.NEW or v in carried) else "other" for v in y], dtype=object)
        labels = H.OLD + carried
        yw = fold(W["tune"]["y"]); ya = fold(A["tune"]["y"]); yc = X3["tune"]["y"]
        tabl = [[r[0], r[1], (r[2] if (r[2] not in H.NEW or r[2] in carried) else "other"), r[3]] for r in table_new]
        T = H.Table(slot, tabl, H.KINDS_ALL)
        keys = ("person", "none", "cat", "dog", "deer")
        today_c = H.balanced_share(OLD_C, yc, keys)
        sela = np.isin(ya, H.VIEWS); selw = np.isin(yw, H.VIEWS)
        base_a = float(np.mean(OLD_A[sela] == ya[sela])); base_w = float(np.mean(OLD_W[selw] == yw[selw]))
        for pw in [float(x) for x in os.environ.get("POWERS", "0.5").split(",")]:
            for am in [float(x) for x in os.environ.get("AMULTS", "1").split(",")]:
                Xf, yf0, mult = fitset(True, am)
                t1 = time.time(); Wk, bk = fit_lr(Xf, fold(yf0), pw, labels, 20.0, mult)
                Z = W["tune"]["X"] @ Wk.T + bk
                lab = np.array(labels, dtype=object)
                for tag, off in (("raw", np.zeros(len(labels))), ("calibrated", calibrate(Z, yw, labels, carried))):
                    b2 = bk + off
                    kw = lab[(Z + off).argmax(1)]
                    marks = {g: (round(float(np.mean(kw[yw == g] == g)), 3), round(float(np.mean(yw[kw == g] == g)), 3) if (kw == g).any() else 0) for g in carried}
                    npass = sum(1 for r, q in marks.values() if r >= 0.75 and q >= 0.75)
                    dw = float(np.mean(kw[selw] == yw[selw])) - base_w
                    kca = lab[(X3["tune"]["X"] @ Wk.T + b2).argmax(1)]
                    ca = H.balanced_share(kca, yc, keys) - today_c
                    rows = []
                    for tk in (0.5, 1.0, 2.0):
                        for wk in (0.5, 0.7, 0.9, 1.0):
                            fu = dict(m_old["fusion"], t_kind=tk, w_kind=wk, rule="mix")
                            ka, _ = H.answer(A["tune"]["X"], A["tune"]["month"], Wk, tk * b2, labels, fu, T)
                            kc, _ = H.answer(X3["tune"]["X"], X3["tune"]["month"], Wk, tk * b2, labels, fu, T)
                            rows.append((round(float(np.mean(ka[sela] == ya[sela])) - base_a, 4), round(H.balanced_share(kc, yc, keys) - today_c, 4), tk, wk))
                    feas = [r for r in rows if r[1] >= -0.01]
                    print(json.dumps({"power": pw, "amult": am, "head": tag, "groups_pass": npass, "world_old": round(dw, 4), "coco_alone": round(ca, 4),
                                      "best_feasible": max(feas) if feas else None, "s": round(time.time() - t1)}), flush=True)
                    print("   ", {g: m for g, m in sorted(marks.items(), key=lambda kv: -min(kv[1]))}, flush=True)
                    if tag == "calibrated":
                        print("    offsets", {g: float(off[labels.index(g)]) for g in carried if off[labels.index(g)] != 0}, flush=True)
    if "merge" in trials:
        # the head carries all nineteen rows; a group that fails is answered as `other` (its probability added to other's)
        labels = H.LABELS
        yw0 = W["tune"]["y"]; ya0 = A["tune"]["y"]; yc = X3["tune"]["y"]
        keys = ("person", "none", "cat", "dog", "deer")
        today_c = H.balanced_share(OLD_C, yc, keys)
        oi = labels.index("other")

        def merged(P, named):
            P = P.copy()
            for g in H.NEW:
                if g not in named:
                    j = labels.index(g); P[:, oi] += P[:, j]; P[:, j] = 0
            return P

        def softmax(Z):
            Z = Z - Z.max(1, keepdims=True); E = np.exp(Z); return E / E.sum(1, keepdims=True)

        def fused(X, months, Wk, b, fu, named, T):
            # the page's mix rule on merged head probabilities
            P = merged(softmax(fu["t_kind"] * (X @ Wk.T) + fu["t_kind"] * b), named)
            labs = labels
            speaks = np.array([lab in T.kinds for lab in labs])
            q = H.species_shares(X, months, T, fu)
            Q = np.zeros_like(P)
            for i, lab in enumerate(labs):
                if speaks[i]:
                    Q[:, i] = q[:, T.kinds.index(lab)]
            share = (P * speaks).sum(1, keepdims=True)
            c = np.where(speaks, fu["w_kind"] * P + (1 - fu["w_kind"]) * share * Q, P)
            return np.array(labs, dtype=object)[c.argmax(1)]

        for combo in os.environ.get("COMBOS", "0:1:1,0.5:1:1").split(","):
            pw, am, cm = [float(x) for x in combo.split(":")]
            Xf, yf0, mult = fitset(True, am, cm)
            t1 = time.time(); Wk, bk = fit_lr(Xf, yf0, pw, labels, 20.0, mult)
            Z = W["tune"]["X"] @ Wk.T + bk
            off = calibrate(Z, yw0, labels, list(H.NEW))
            b2 = bk + off
            named = list(H.NEW)
            while True:
                fold = lambda y: np.array([v if (v not in H.NEW or v in named) else "other" for v in y], dtype=object)
                yw = fold(yw0)
                kw = np.array(labels, dtype=object)[merged(softmax(W["tune"]["X"] @ Wk.T + b2), named).argmax(1)]
                marks = {g: (float(np.mean(kw[yw == g] == g)), float(np.mean(yw[kw == g] == g)) if (kw == g).any() else 0.0) for g in named}
                fails = {g: m for g, m in marks.items() if min(m) < 0.75}
                if not fails:
                    break
                named.remove(min(fails, key=lambda g: min(fails[g])))
            ya = fold(ya0); selw = np.isin(yw, H.VIEWS); sela = np.isin(ya, H.VIEWS)
            dw = float(np.mean(kw[selw] == yw[selw]) - np.mean(OLD_W[selw] == yw0[selw]))
            tabl = [[r[0], r[1], (r[2] if (r[2] not in H.NEW or r[2] in named) else "other"), r[3]] for r in table_new]
            T = H.Table(slot, tabl, H.KINDS_ALL)
            kca = np.array(labels, dtype=object)[merged(softmax(X3["tune"]["X"] @ Wk.T + b2), named).argmax(1)]
            ca = H.balanced_share(kca, yc, keys) - today_c
            rows = []
            for tk in (0.5, 1.0, 2.0):
                for wk in (0.5, 0.7, 0.9, 1.0):
                    fu = dict(m_old["fusion"], t_kind=tk, w_kind=wk, rule="mix")
                    ka = fused(A["tune"]["X"], A["tune"]["month"], Wk, b2, fu, named, T)
                    kc = fused(X3["tune"]["X"], X3["tune"]["month"], Wk, b2, fu, named, T)
                    rows.append((round(float(np.mean(ka[sela] == ya[sela]) - np.mean(OLD_A[sela] == ya0[sela])), 4), round(H.balanced_share(kc, yc, keys) - today_c, 4), tk, wk))
            feas = [r for r in rows if r[1] >= -0.01]
            so = yw == "other"
            print(json.dumps({"power": pw, "amult": am, "cmult": cm, "named": named, "world_old": round(dw, 4), "coco_alone": round(ca, 4), "best_feasible": max(feas) if feas else None,
                              "other_view": round(float(np.isin(kw[so], H.VIEWS).mean()), 4), "marks": {g: [round(x, 3) for x in marks[g]] for g in named}, "s": round(time.time() - t1)}), flush=True)
    json.dump(res, open(os.environ.get("OUT", "exp_out.json"), "w"), indent=1)
