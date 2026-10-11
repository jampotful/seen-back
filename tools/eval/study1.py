#!/usr/bin/env python3
"""Study 1: photos scored against sentences, for every published model.

  python3 -I tools/eval/study1.py <root> [--out docs/eval/study1.json] [--models a,b,c]

<root> is the directory made by tools/eval/fetch.py. For every model under <root>/lab it measures, on the
evaluation set alachua-2025:
  - the kind of eye from the kind phrases, from the top species, and from summed species probabilities;
  - species top-1 and top-5 for every label set, without a prior and with the place-and-season prior;
  - the same on the int8 and WASM vectors of the pocket models, at the settings tuned on the original vectors.
Every setting (the prior's weight and smoothing, the smallest number of records a species needs to stay in the
list, the temperature) is chosen on the `val` split. Every reported number comes from the `test` split and
carries a 95% interval from a bootstrap over photos (ev.RESAMPLES resamples, seed ev.SEED).
The result is one JSON file; tools/eval/report.py turns it into tables.
"""
import argparse, json, os, re, sys, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ev

MIN_N = (1, 3, 10)                 # the list restricted to species with at least this many records before 2025
LAM = (0.0, 2.0)                   # smoothing of a month's count toward a twelfth of the year's count
C = (0.1, 1.0)                     # count added to every species in every month
RATIO = (0.002, 0.004, 0.006, 0.008, 0.012, 0.016, 0.024, 0.032, 0.048)   # prior weight divided by temperature
TEMPS = (5, 10, 20, 30, 50, 70, 100, 150, 200, 300)
LABELSETS = ("species_sci", "species_com", "species_taxon_com")


def differing_rows(root, ES):
    """Rows whose GBIF species has another name on iNaturalist. From inat.json when it is published (by species);
    otherwise from the pairs listed in the evaluation set's SUMMARY.md (the 25 most frequent of 63)."""
    p = os.path.join(root, "data", "regions", ev.REGION, "inat.json")
    if os.path.exists(p):
        inat = json.load(open(p, encoding="utf-8"))
        flag = np.array([(str(r["key"]) in inat and inat[str(r["key"])].get("sci", r["sci"]) != r["sci"]) for r in ES.rows])
        return flag, "inat.json: the GBIF species key's usual iNaturalist name differs from the GBIF name"
    text = open(os.path.join(root, "data", "eval", ev.EVALSET, "SUMMARY.md"), encoding="utf-8").read()
    gbif_names = set(m.group(1) for m in re.finditer(r"^- \*[^*]+\*: \*([^*]+)\*, \d+$", text, re.M))
    flag = np.array([r["sci"] in gbif_names for r in ES.rows])
    return flag, "SUMMARY.md: the 25 most frequent of the 63 differing pairs (inat.json was not published yet)"


def confusion(true, pred, labels_true, labels_pred):
    return {"rows": labels_true, "columns": labels_pred,
            "counts": [[int(((true == a) & (pred == b)).sum()) for b in labels_pred] for a in labels_true]}


def breakdown(groups, hit1, hit5, base1):
    out = []
    for name, mask in groups:
        if mask.sum() == 0:
            continue
        out.append({"group": name, "n": int(mask.sum()), "top1": ev.ci(hit1[mask]), "top5": ev.ci(hit5[mask]),
                    "top1_no_prior": round(float(base1[mask].mean()), 4)})
    return out


def groups_for(ES, te):
    R = [r for r, t in zip(ES.rows, te) if t]
    eyes = ES.eyes[te]
    g = {"kind": [(k, eyes == k) for k in ev.KINDS]}
    cls = np.array([r["kingdom"] + " / " + (r["class"] or "(none)") for r in R])
    names, counts = np.unique(cls, return_counts=True)
    big = [n for n, c in sorted(zip(names, counts), key=lambda t: -t[1]) if c >= 30]
    g["class"] = [(n, cls == n) for n in big] + [("all other classes", ~np.isin(cls, big))]
    nt = ES.n_true[te]
    g["records"] = [(name, (nt >= lo) & (nt <= hi)) for name, lo, hi in ev.FREQ_BINS]
    mo = ES.month[te]
    g["month"] = [("%02d" % (m + 1), mo == m) for m in range(12)]
    return g


def score_labelset(ES, Z, differ, want_detail):
    """One model, one label set: plain and tuned results on test."""
    va, te = ES.val, ES.test
    y, eyes, month = ES.y, ES.eyes, ES.month
    Zv, Zt = Z[va], Z[te]
    yv, yt = y[va], y[te]
    out = {}
    r0 = ev.ranks(Zt, yt)
    h1, h5 = r0 == 0, r0 < 5
    p0 = Zt.argmax(1)
    out["plain"] = {"top1": ev.ci(h1), "top5": ev.ci(h5), "kind_from_top": ev.ci(ES.sp_eyes[p0] == eyes[te]),
                    "val_top1": round(float((Zv.argmax(1) == yv).mean()), 4)}
    out["restricted_no_prior"] = {}
    for mn in MIN_N[1:]:
        keep = ES.N >= mn
        mask = np.where(keep, 0, -np.inf).astype(np.float32)
        out["restricted_no_prior"][str(mn)] = {"top1": ev.ci((Zt + mask).argmax(1) == yt), "val_top1": round(float(((Zv + mask).argmax(1) == yv).mean()), 4)}
    # the prior: settings chosen on val
    best, buf, tried = None, np.empty_like(Zv), 0
    mv = month[va]
    for mn in MIN_N:
        keep = ES.N >= mn
        for lam in LAM:
            for c in C:
                lpm = ev.log_share(ev.prior_weights(ES.M, ES.N, lam, c), keep)[mv]
                for r in RATIO:
                    np.multiply(lpm, np.float32(r), out=buf)
                    buf += Zv
                    acc = float((buf.argmax(1) == yv).mean())
                    tried += 1
                    if best is None or acc > best[0] + 1e-12:
                        best = (acc, mn, lam, c, r)
    acc, mn, lam, c, r = best
    keep = ES.N >= mn
    lp = ev.log_share(ev.prior_weights(ES.M, ES.N, lam, c), keep)
    base_v = Zv + np.float32(r) * lp[mv]
    okv = (yv >= 0) & keep[np.maximum(yv, 0)]
    nll = {}
    for T in TEMPS:
        L = np.float32(T) * base_v[okv]
        mx = L.max(1, keepdims=True)
        lse = (mx[:, 0] + np.log(np.exp(L - mx).sum(1)))
        nll[T] = float((lse - L[np.arange(okv.sum()), yv[okv]]).mean())
    T = min(nll, key=nll.get)
    base_t = Zt + np.float32(r) * lp[month[te]]
    r1 = ev.ranks(base_t, yt)
    g1, g5 = r1 == 0, r1 < 5
    p1 = base_t.argmax(1)
    P = ev.softmax_rows(np.float32(T) * base_t)
    kinds15 = [k for k in ev.KINDS if (ES.sp_eyes[keep] == k).any()]
    Q = np.stack([P[:, keep & (ES.sp_eyes == k)].sum(1) for k in kinds15], 1)
    ksum = np.array(kinds15)[Q.argmax(1)]
    out["tuned"] = {"settings": {"min_n": mn, "lam": lam, "c": c, "ratio": r, "t_species": T, "alpha_prior": round(r * T, 4), "species_in_list": int(keep.sum()), "combinations_tried": tried},
                    "val_top1": round(acc, 4), "val_nll_by_temperature": {str(k): round(v, 4) for k, v in nll.items()},
                    "top1": ev.ci(g1), "top5": ev.ci(g5), "kind_from_top": ev.ci(ES.sp_eyes[p1] == eyes[te]), "kind_from_sum": ev.ci(ksum == eyes[te]),
                    "top1_gain_over_plain": ev.ci(g1.astype(np.float32) - h1.astype(np.float32)),
                    "ceiling": round(float(((yt >= 0) & keep[np.maximum(yt, 0)]).mean()), 4)}
    d = differ[te]
    out["names_agree_only"] = {"rows_left_out": int(d.sum()), "plain_top1": ev.ci(h1[~d]), "tuned_top1": ev.ci(g1[~d]),
                               "plain_top1_on_rows_left_out": ev.ci(h1[d]), "tuned_top1_on_rows_left_out": ev.ci(g1[d])}
    if want_detail:
        G = groups_for(ES, te)
        out["breakdown"] = {name: breakdown(g, g1, g5, h1) for name, g in G.items()}
        out["kind_confusion_from_top"] = confusion(eyes[te], ES.sp_eyes[p1], [k for k in ev.KINDS if (eyes[te] == k).any()], kinds15)
        Rt = [row for row, t in zip(ES.rows, te) if t]
        pairs = {}
        for i in np.nonzero(~g1 & (yt >= 0))[0]:
            pairs.setdefault((int(yt[i]), int(p1[i])), []).append(Rt[i]["obs_url"])
        top = sorted(pairs.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:15]
        out["commonest_mistakes"] = [{"true": ES.species[a]["sci"], "true_en": ES.species[a]["en"], "said": ES.species[b]["sci"], "said_en": ES.species[b]["en"],
                                      "same_genus": ES.species[a]["genus"] == ES.species[b]["genus"], "photos": len(u), "observations": u[:3]} for (a, b), u in top]
        wrong = np.nonzero(~g1 & (yt >= 0))[0]
        sg = sum(ES.species[int(yt[i])]["genus"] == ES.species[int(p1[i])]["genus"] for i in wrong)
        sf = sum(ES.species[int(yt[i])]["family"] == ES.species[int(p1[i])]["family"] for i in wrong)
        out["mistakes_summary"] = {"wrong_with_species_in_list": int(len(wrong)), "same_genus": int(sg), "same_family": int(sf), "species_not_in_list": int((yt < 0).sum())}
    return out, {"plain_hit": h1, "tuned_hit": g1, "settings": (mn, lam, c, r, T)}


def kinds_block(ES, E, K, klabels):
    te = ES.test
    pred = np.array(klabels)[(E[te] @ K.T).argmax(1)]
    eyes = ES.eyes[te]
    return {"accuracy": ev.ci(pred == eyes), "val_accuracy": round(float((np.array(klabels)[(E[ES.val] @ K.T).argmax(1)] == ES.eyes[ES.val]).mean()), 4),
            "called_person": round(float((pred == "person").mean()), 4), "called_none": round(float((pred == "none").mean()), 4),
            "confusion": confusion(eyes, pred, [k for k in ev.KINDS if (eyes == k).any()], list(klabels))}, pred == eyes


def run_model(root, model, differ_cache):
    t0 = time.time()
    E, ids = ev.load_images(root, model)
    if E is None:
        return None
    ES = ev.EvalSet(root, ids)
    card = json.load(open(os.path.join(root, "lab", model, "card.json"), encoding="utf-8"))
    res = {"rows": len(ids), "test": int(ES.test.sum()), "val": int(ES.val.sum()), "width": int(E.shape[1]),
           "card": {k: card.get(k) for k in ("source", "licence", "role", "params", "ship", "ship_bytes", "ship_sha256")}, "labelsets": {}}
    if model not in differ_cache:
        differ_cache[model] = differing_rows(root, ES)
    differ, how = differ_cache[model]
    res["differing_names_rule"] = how
    K, klabels = ev.load_text(root, model, "kinds")
    kind_hit = None
    if K is not None:
        res["kind_phrases"], kind_hit = kinds_block(ES, E, K, klabels)
    kept = {}
    for ls in LABELSETS:
        S, labels = ev.load_text(root, model, ls)
        if S is None:
            continue
        keys = [l["key"] for l in labels]
        assert keys == [s["key"] for s in ES.species], "label rows of %s/%s are not in the species list's order" % (model, ls)
        Z = E @ S.T
        res["labelsets"][ls], kept[ls] = score_labelset(ES, Z, differ, want_detail=True)
        # scrambled labels: the same scores with the species rows shuffled must fall to chance
        perm = np.random.default_rng(1).permutation(Z.shape[1])
        res["labelsets"][ls]["shuffled_rows_top1"] = round(float((Z[ES.test][:, perm].argmax(1) == ES.y[ES.test]).mean()), 4)
        del Z
    if res["labelsets"]:
        res["best_labelset_on_val"] = max(res["labelsets"], key=lambda k: res["labelsets"][k]["tuned"]["val_top1"])
    # the same settings on the int8 and WASM vectors (pocket models)
    variants = sorted(f[:-8] for f in os.listdir(os.path.join(root, "lab", model, "images")) if f.endswith(".f16.npy") and f.startswith(ev.EVALSET + "."))
    res["variants"] = {}
    for v in variants:
        Ev, idv = ev.load_images(root, model, v)
        if idv != ids:
            res["variants"][v] = {"error": "row ids differ from the original vectors' ids"}
            continue
        cos = (E * Ev).sum(1)
        o = {"cosine_to_original": {"mean": round(float(cos.mean()), 5), "p01": round(float(np.percentile(cos, 1)), 5), "min": round(float(cos.min()), 5)}, "labelsets": {}}
        if K is not None:
            kb, hit = kinds_block(ES, Ev, K, klabels)
            o["kind_phrases"] = {"accuracy": kb["accuracy"], "difference_from_original": ev.ci(hit.astype(np.float32) - kind_hit.astype(np.float32))}
        for ls in kept:
            S, _ = ev.load_text(root, model, ls)
            Z = Ev[ES.test] @ S.T
            mn, lam, c, r, T = kept[ls]["settings"]
            keep = ES.N >= mn
            lp = ev.log_share(ev.prior_weights(ES.M, ES.N, lam, c), keep)
            yt = ES.y[ES.test]
            r0 = ev.ranks(Z, yt)
            r1 = ev.ranks(Z + np.float32(r) * lp[ES.month[ES.test]], yt)
            o["labelsets"][ls] = {"plain_top1": ev.ci(r0 == 0), "plain_top5": ev.ci(r0 < 5), "tuned_top1": ev.ci(r1 == 0), "tuned_top5": ev.ci(r1 < 5),
                                  "plain_top1_difference_from_original": ev.ci((r0 == 0).astype(np.float32) - kept[ls]["plain_hit"].astype(np.float32)),
                                  "tuned_top1_difference_from_original": ev.ci((r1 == 0).astype(np.float32) - kept[ls]["tuned_hit"].astype(np.float32))}
            del Z
        res["variants"][v] = o
    res["seconds"] = round(time.time() - t0, 1)
    return res


def prior_only(root):
    ES = ev.EvalSet(root)
    va, te = ES.val, ES.test
    best = None
    for lam in LAM:
        for c in C:
            lp = ev.log_share(ev.prior_weights(ES.M, ES.N, lam, c))
            acc = float((lp[ES.month[va]].argmax(1) == ES.y[va]).mean())
            if best is None or acc > best[0]:
                best = (acc, lam, c)
    _, lam, c = best
    lp = ev.log_share(ev.prior_weights(ES.M, ES.N, lam, c))[ES.month[te]]
    r = ev.ranks(lp, ES.y[te])
    yt = ES.y[te]
    out = {"settings": {"lam": lam, "c": c}, "top1": ev.ci(r == 0), "top5": ev.ci(r < 5), "kind_from_top": ev.ci(ES.sp_eyes[lp.argmax(1)] == ES.eyes[te]),
           "most_recorded_species_every_time": ev.ci(yt == 0), "commonest_kind_every_time": ev.ci(ES.eyes[te] == "plant"),
           "ceiling": {str(mn): round(float(((yt >= 0) & (ES.N[np.maximum(yt, 0)] >= mn)).mean()), 4) for mn in MIN_N},
           "species_in_list": {str(mn): int((ES.N >= mn).sum()) for mn in MIN_N},
           "test_rows": int(te.sum()), "val_rows": int(va.sum()), "test_rows_species_not_in_list": int((yt < 0).sum()),
           "test_species": int(len(set(yt[yt >= 0].tolist()))), "test_rows_by_records": {name: int(((ES.n_true[te] >= lo) & (ES.n_true[te] <= hi)).sum()) for name, lo, hi in ev.FREQ_BINS}}
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--out", default="docs/eval/study1.json")
    ap.add_argument("--models")
    a = ap.parse_args()
    models = a.models.split(",") if a.models else sorted(os.listdir(os.path.join(a.root, "lab")))
    fetched = json.load(open(os.path.join(a.root, "FETCHED.json"))) if os.path.exists(os.path.join(a.root, "FETCHED.json")) else {}
    out = {"made_by": "tools/eval/study1.py", "inputs": {"branches": fetched,
                                                       "manifest_sha256": ev.sha256_file(os.path.join(a.root, "data", "eval", ev.EVALSET, "manifest.csv")),
                                                       "species_sha256": ev.sha256_file(os.path.join(a.root, "data", "regions", ev.REGION, "species.json"))},
           "method": {"resamples": ev.RESAMPLES, "seed": ev.SEED, "interval": "95% percentile interval, bootstrap over photos", "tuned_on": "val", "reported_on": "test",
                      "grid": {"min_n": MIN_N, "lam": LAM, "c": C, "ratio": RATIO, "temperature": TEMPS}},
           "prior_only": prior_only(a.root), "models": {}}
    cache = {}
    for m in models:
        r = run_model(a.root, m, cache)
        if r is None:
            continue
        out["models"][m] = r
        b = r.get("best_labelset_on_val")
        print(m, "kinds", (r.get("kind_phrases") or {}).get("accuracy"), "|", b, (r["labelsets"][b]["plain"]["top1"], r["labelsets"][b]["tuned"]["top1"], r["labelsets"][b]["tuned"]["settings"]) if b else "no label rows", "| %.0fs" % r["seconds"], flush=True)
        ev.write_json(a.out, out)
