#!/usr/bin/env python3
"""Study 2: heads trained on local photos, on frozen image vectors.

  python3 -I tools/eval/study2.py <root> --train val              [--models a,b] [--out docs/eval/study2-val.json] [--save <dir>]
  python3 -I tools/eval/study2.py <root> --train alachua-pre2025  [--models a,b] [--out docs/eval/study2-alachua-pre2025.json] [--save <dir>]

--train alachua-pre2025 is the real study: heads are fitted on the training photos (from before 2025), every setting
is chosen on the evaluation set's `val` split, and every number is from its `test` split.
--train val is a stand-in that proves the machinery before the training vectors exist: two thirds of `val` (by a hash
of the row id) are the fitting photos, the last third chooses the settings, and `test` is reported as usual. Its numbers
say little about what a real training set gives: there are about two fitting photos a species.

For a pocket model the heads are fitted on the original model's vectors and tested on the vectors the browser's WASM
runtime computes (images/alachua-2025.wasm-int8-per-channel), when those are published.

Every species head has the page's form: score = rows . e + bias + alpha * log(share of the month's records), with e the
unit image vector. The heads:
  sentences               the model's own label rows (the best of the label sets on the tuning photos)
  prototypes              the mean vector of each species' fitting photos; species without photos have no row
  prototypes + sentences  the sum of a species' prototype and beta times its sentence row; species without photos keep the sentence row and get a bias
  discriminant            Gaussian classes with one shared covariance (shrunk), which is a linear head with a bias
  discriminant + sentences  the same with gamma times the sentence row added, and sentence rows for species without photos
  mapped to BioCLIP 2     a ridge regression from this model's vectors to BioCLIP 2's, folded into BioCLIP 2's label rows
With --save the best head of each model is written to <dir>/<model>.npz for tools/eval/export_heads.py.
"""
import argparse, hashlib, json, os, sys, time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ev

REL = (0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0)   # prior weight, in units of a head's usual gap between first and second
SCALES = (0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0, 8.0, 12.0, 16.0, 24.0, 32.0, 48.0, 64.0, 96.0, 128.0)   # calibration scale, in the same units
T_KIND = (20.0, 50.0, 100.0)                                            # temperature of the kind phrases in the page's combination
W_KIND = (0.0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 1.0)                       # weight of the kind phrases against the species list
SMOOTH = ((0.0, 0.1), (2.0, 1.0))                                       # (lam, c) of the prior's monthly weights
TRAIN_BINS = [("no training photo", 0, 0), ("1 or 2", 1, 2), ("3 to 9", 3, 9), ("10 to 29", 10, 29), ("30 or more", 30, 10 ** 9)]
NEG = np.float32(-1e9)


def log(*a):
    print(*a, flush=True)


def fit_set(root, model, mode):
    """Fitting vectors X (unit), species index y, kind of eye, and the masks of tuning and test rows of the evaluation set."""
    E0, ids = ev.load_images(root, model)
    ES = ev.EvalSet(root, ids)
    if mode == "val":
        h = np.array([int(hashlib.sha256(i.encode()).hexdigest()[:8], 16) % 3 for i in ids])
        fit, tune = ES.val & (h < 2), ES.val & (h == 2)
        return ES, E0[fit], ES.y[fit], ES.eyes[fit], tune, [i for i, f in zip(ids, fit) if f], "images/" + ev.EVALSET + " (two thirds of val)"
    X, tid = ev.load_images(root, model, mode)
    if X is None:
        return None
    by = {r["id"]: r for r in ev.read_manifest(root, "train/" + mode)}
    y = np.array([ES.key2i.get(int(by[i]["key"]), -1) for i in tid])
    eyes = np.array([by[i]["eyes"] for i in tid])
    return ES, X, y, eyes, ES.val.copy(), tid, "images/" + mode


def tune_head(cands, Xu, lps, y_tune, m_tune):
    """Choose among candidate (label, rows, bias) triples and prior settings by top-1 on the tuning photos.
    Returns the choice without the prior (accuracy, candidate, gap) and with it (accuracy, candidate, gap, smoothing, relative weight)."""
    best0, best1 = None, None
    lpms = [lp[m_tune] for lp in lps]
    buf = None
    for ci, (label, rows, bias) in enumerate(cands):
        Z = Xu @ rows.T + bias
        top2 = np.partition(Z, -2, axis=1)[:, -2:]
        u = float(np.median(top2[:, 1] - top2[:, 0])) or 1e-6
        acc0 = float((Z.argmax(1) == y_tune).mean())
        if best0 is None or acc0 > best0[0]:
            best0 = (acc0, ci, u)
        buf = np.empty_like(Z) if buf is None else buf
        for si, lpm in enumerate(lpms):
            for r in REL[1:]:
                np.multiply(lpm, np.float32(r * u), out=buf)
                buf += Z
                acc = float((buf.argmax(1) == y_tune).mean())
                if best1 is None or acc > best1[0]:
                    best1 = (acc, ci, u, si, r)
    return best0, best1


def calibrate(Z, y, u):
    """The scale s (from SCALES / u) that gives the lowest mean negative log likelihood of softmax(s * Z) on rows whose species has a row."""
    ok = (y >= 0) & (Z[np.arange(len(y)), np.maximum(y, 0)] > NEG / 2)
    best = None
    for k in SCALES:
        L = (np.float32(k / u) * Z[ok]).astype(np.float64)
        mx = L.max(1, keepdims=True)
        nll = float((mx[:, 0] + np.log(np.exp(L - mx).sum(1)) - L[np.arange(ok.sum()), y[ok]]).mean())
        if best is None or nll < best[0]:
            best = (nll, k / u)
    return best[1], best[0]


def lda(X, y, S, shrink):
    """Rows and biases of Gaussian classes with a shared covariance; species without a fitting photo get no row."""
    have = np.zeros(S, bool)
    have[y] = True
    cnt = np.bincount(y, minlength=S).astype(np.float32)
    M = np.zeros((S, X.shape[1]), np.float32)
    np.add.at(M, y, X)
    M[have] /= cnt[have, None]
    Xc = X - M[y]
    cov = (Xc.T @ Xc) / max(1, len(X) - int(have.sum()))
    out = {}
    d = X.shape[1]
    for g in shrink:
        C = (1 - g) * cov + g * (np.trace(cov) / d) * np.eye(d, dtype=np.float32)
        W = np.linalg.solve(C.astype(np.float64), M.T.astype(np.float64)).T.astype(np.float32)
        b = (-0.5 * (W * M).sum(1)).astype(np.float32)
        b[~have] = NEG
        out[g] = (W, b)
    return out, have, cnt


def fused(pk, Q, speaks, w, rule, guard=1e-9):
    """The page's combination of the kinds head (pk) with the species list's summed probabilities (Q), as tools/fusion/fuse.py computes it."""
    if rule == "mix":
        A = pk[:, speaks].sum(1, keepdims=True)
        c = np.where(speaks[None, :], w * pk + (1 - w) * A * Q, pk)
        return c / c.sum(1, keepdims=True)
    sc = np.where(speaks[None, :], w * np.log(np.maximum(pk, guard)) + (1 - w) * np.log(np.maximum(Q, guard)), np.log(np.maximum(pk, guard)))
    return ev.softmax_rows(sc)


def evaluate(Z, lp_m, rho, s, ES, mask, keep_rows):
    """Top-1, top-5 and the kind from summed probabilities on the rows of `mask`, for scores Z (rows . e + bias)."""
    y = ES.y[mask]
    base = Z + np.float32(rho) * lp_m if rho else Z
    r = ev.ranks(base, y)
    Pm = ev.softmax_rows((np.float32(s) * base).astype(np.float64))
    kinds = [k for k in ev.KINDS if (ES.sp_eyes[keep_rows] == k).any()]
    Q = np.stack([Pm[:, keep_rows & (ES.sp_eyes == k)].sum(1) for k in kinds], 1)
    ksum = np.array(kinds)[Q.argmax(1)]
    return r, Pm, ksum


def run_model(root, model, mode, save):
    t0 = time.time()
    got = fit_set(root, model, mode)
    if got is None:
        log(model, ": no training vectors published (images/%s)" % mode)
        return None
    ES, X, ytr, eyes_tr, tune, fit_ids, train_name = got
    ok = ytr >= 0
    X, ytr, eyes_tr = X[ok], ytr[ok], eyes_tr[ok]
    S = len(ES.species)
    tv = ev.EVALSET + ".wasm-int8-per-channel"
    Et, ids_t = ev.load_images(root, model, tv)
    if Et is None:
        tv = ev.EVALSET
        Et, ids_t = ev.load_images(root, model, tv)
    assert ids_t == [r["id"] for r in ES.rows]
    te = ES.test
    Xu, Xt = Et[tune], Et[te]
    yu, yt = ES.y[tune], ES.y[te]
    lps = [ev.log_share(ev.prior_weights(ES.M, ES.N, lam, c)) for lam, c in SMOOTH]
    res = {"train_vectors": train_name, "train_photos": int(len(X)), "train_species": int(len(set(ytr.tolist()))), "tuning_photos": int(tune.sum()),
           "test_vectors": "images/" + tv, "test_photos": int(te.sum()), "species_heads": [], "kind_heads": [], "notes": []}
    heads = {}       # name -> list of (label, rows, bias)

    # sentences
    texts = {}
    for ls in ("species_sci", "species_com", "species_taxon_com"):
        T_, _ = ev.load_text(root, model, ls)
        if T_ is not None:
            texts[ls] = T_
    zero = np.zeros(S, np.float32)
    if texts:
        heads["sentences"] = [(ls, T_, zero) for ls, T_ in texts.items()]
    # prototypes
    have = np.zeros(S, bool)
    have[ytr] = True
    cnt = np.bincount(ytr, minlength=S)
    Pr = np.zeros((S, X.shape[1]), np.float32)
    np.add.at(Pr, ytr, X)
    Pr = ev.unit(Pr)
    Pr[~have] = 0
    heads["prototypes"] = [("class means", Pr, np.where(have, 0, NEG).astype(np.float32))]
    if texts:
        # the label set that does best by itself on the tuning photos is the one mixed into the trained heads
        ls_best = max(texts, key=lambda ls: tune_head([(ls, texts[ls], zero)], Xu, lps, yu, ES.month[tune])[1][0])
        Tb = texts[ls_best]
        heads["prototypes + sentences"] = [("%s, beta %g, bias for species without photos %g" % (ls_best, beta, c0), Pr + np.float32(beta) * Tb, np.where(have, 0, c0).astype(np.float32))
                                           for beta in (0.5, 1.0, 2.0, 4.0, 8.0) for c0 in (0.2, 0.35, 0.5, 0.65, 0.8)]
    # discriminant
    shrink = (0.03, 0.1, 0.3, 1.0)
    L, _, _ = lda(X, ytr, S, shrink)
    heads["discriminant"] = [("shrinkage %g" % g, L[g][0], L[g][1]) for g in shrink]
    if texts:
        dm = []
        for g in shrink:
            W, b = L[g]
            sc = float(np.median(np.linalg.norm(W[have], axis=1)))
            for gam in (0.1, 0.3, 1.0, 3.0):
                rows = np.where(have[:, None], W + np.float32(gam * sc) * Tb, np.float32((1 + gam) * sc) * Tb)
                bias = np.where(have, b, np.float32(np.median(b[have])))
                dm.append(("shrinkage %g, %s, gamma %g" % (g, ls_best, gam), rows.astype(np.float32), bias.astype(np.float32)))
        heads["discriminant + sentences"] = dm
    # mapped into BioCLIP 2's space
    big = "bioclip2-l14"
    if model != big:
        if mode == "val":
            Eb, idb = ev.load_images(root, big)
            pair_x, pair_y = X, (Eb[[idb.index(i) for i in fit_ids]][ok] if Eb is not None else None)
        else:
            Eb, idb = ev.load_images(root, big, mode)
            if Eb is not None:
                pos = {i: k for k, i in enumerate(idb)}
                sel = [k for k, i in enumerate(np.array(fit_ids)[ok]) if i in pos]
                pair_x, pair_y = X[sel], Eb[[pos[i] for i in np.array(fit_ids)[ok][sel]]]
            else:
                pair_y = None
        Sb, _ = ev.load_text(root, big, "species_sci")
        if pair_y is not None and Sb is not None:
            G = (pair_x.T @ pair_x).astype(np.float64)
            XY = (pair_x.T @ pair_y).astype(np.float64)
            tr = np.trace(G) / G.shape[0]
            heads["mapped to BioCLIP 2"] = [("ridge %g, %d pairs" % (lam, len(pair_x)), (Sb @ np.linalg.solve(G + lam * tr * np.eye(G.shape[0]), XY).T.astype(np.float32)).astype(np.float32), zero) for lam in (0.001, 0.01, 0.1, 1.0)]
            res["notes"].append("The map into BioCLIP 2's space was fitted on %d pairs of vectors of the same photos." % len(pair_x))
        else:
            res["notes"].append("The map into BioCLIP 2's space could not be fitted: BioCLIP 2's vectors of the fitting photos are not published yet.")

    ntr = cnt[np.maximum(yt, 0)] * (yt >= 0)
    chosen, table_cols, table_hits = None, [], []
    for name, cands in heads.items():
        b0, b1 = tune_head(cands, Xu, lps, yu, ES.month[tune])
        # without the prior
        _, c0i, u0 = b0
        rows0, bias0 = cands[c0i][1], cands[c0i][2]
        r0 = ev.ranks(Xt @ rows0.T + bias0, yt)
        # with the prior
        acc1, ci, u, si, rel = b1
        label, rows, bias = cands[ci]
        rho = rel * u
        Zu0 = Xu @ rows.T + bias
        s, nll = calibrate(Zu0 + np.float32(rho) * lps[si][ES.month[tune]], yu, u)
        Zt = Xt @ rows.T + bias
        keep_rows = bias > NEG / 2
        r1, Pm, ksum = evaluate(Zt, lps[si][ES.month[te]], rho, s, ES, te, keep_rows)
        h = {"name": name, "plain": {"top1": ev.ci(r0 == 0), "top5": ev.ci(r0 < 5), "choice": cands[c0i][0], "tuning_top1": round(b0[0], 4)},
             "prior": {"top1": ev.ci(r1 == 0), "top5": ev.ci(r1 < 5), "kind_from_sum": ev.ci(ksum == ES.eyes[te]), "tuning_top1": round(acc1, 4), "choice": label,
                       "settings": {"lam": SMOOTH[si][0], "c": SMOOTH[si][1], "alpha_prior": round(float(rho * s), 4), "scale": round(float(s), 4), "tuning_nll": round(nll, 4), "rows_with_a_species": int(keep_rows.sum())},
                       "settings_text": "%s; alpha %.2f; lam %g, c %g" % (label, rho * s, SMOOTH[si][0], SMOOTH[si][1])}}
        res["species_heads"].append(h)
        table_cols.append(name)
        table_hits.append(r1 == 0)
        log("  %-26s plain %.4f | prior %.4f top5 %.4f kind %.4f | tune %.4f | %s" % (name, h["plain"]["top1"][0], h["prior"]["top1"][0], h["prior"]["top5"][0], h["prior"]["kind_from_sum"][0], acc1, label))
        if chosen is None or acc1 > chosen["tune"]:
            chosen = {"tune": acc1, "name": name, "label": label, "rows": rows * np.float32(s), "bias": np.where(keep_rows, bias * np.float32(s), NEG).astype(np.float32),
                      "alpha": float(rho * s), "smooth": SMOOTH[si], "Zt": Zt, "Zu": Zu0, "rho": rho, "s": s, "si": si, "keep": keep_rows, "hit": r1 == 0}
    res["by_train_photos"] = {"heads": table_cols, "rows": [{"group": g, "n": int(((ntr >= lo) & (ntr <= hi)).sum()), "top1": [round(float(hh[(ntr >= lo) & (ntr <= hi)].mean()), 4) if ((ntr >= lo) & (ntr <= hi)).any() else None for hh in table_hits]} for g, lo, hi in TRAIN_BINS]}
    res["chosen_species_head"] = {"name": chosen["name"], "choice": chosen["label"], "tuning_top1": round(chosen["tune"], 4)}

    # kind of eye
    K, klabels = ev.load_text(root, model, "kinds")
    eyes_t = ES.eyes[te]
    if K is not None:
        pred = np.array(klabels)[(Xt @ K.T).argmax(1)]
        res["kind_heads"].append({"name": "kind phrases (sentence rows, with `person` and `none`)", "accuracy": ev.ci(pred == eyes_t), "called_person": float((pred == "person").mean()), "called_none": float((pred == "none").mean())})
    try:
        from sklearn.linear_model import LogisticRegression
        clf = LogisticRegression(C=20.0, max_iter=300).fit(X, eyes_tr)
        zk = clf.decision_function(Xt)
        pred = clf.classes_[zk.argmax(1)]
        res["kind_heads"].append({"name": "trained on the fitting photos (logistic regression, %d kinds, no row for `person` or `none`)" % len(clf.classes_), "accuracy": ev.ci(pred == eyes_t), "called_person": 0.0, "called_none": 0.0})
        if K is not None:
            # sentence rows for person and none beside the trained rows: their bias is set so that at most 0.5% of tuning photos are called person or none
            pn = [klabels.index("person"), klabels.index("none")]
            zu = clf.decision_function(Xu)
            tk = float(zu.std() / max(1e-6, (Xu @ K.T).std()))
            margin = (tk * (Xu @ K[pn].T)).max(1) - zu.max(1)
            off = -float(np.quantile(margin, 0.995))
            z2 = np.concatenate([zk, tk * (Xt @ K[pn].T) + off], 1)
            lab2 = np.array(list(clf.classes_) + ["person", "none"])
            pred2 = lab2[z2.argmax(1)]
            res["kind_heads"].append({"name": "trained rows, with the sentence rows for `person` and `none` kept beside them", "accuracy": ev.ci(pred2 == eyes_t), "called_person": float((pred2 == "person").mean()), "called_none": float((pred2 == "none").mean())})
            res["notes"].append("The wildlife records hold no people and no photos with nothing alive in them. The sentence rows for `person` and `none` are kept, with a bias set on the tuning photos so that at most 0.5% of them are called `person` or `none`. How often a person is then called a person is unmeasured.")
    except Exception as e:                                                # scikit-learn missing or the fit failed: say so
        res["notes"].append("The trained kind head was not fitted: %s." % type(e).__name__)
    res["kind_heads"].append({"name": "summed species probabilities of the head `%s`" % chosen["name"], "accuracy": next(h["prior"]["kind_from_sum"] for h in res["species_heads"] if h["name"] == chosen["name"]), "called_person": 0.0, "called_none": 0.0})

    # confidence of the chosen head: thresholds from the tuning photos, outcomes on test
    lpu, lpt = lps[chosen["si"]][ES.month[tune]], lps[chosen["si"]][ES.month[te]]
    Pu = ev.softmax_rows((np.float32(chosen["s"]) * (chosen["Zu"] + np.float32(chosen["rho"]) * lpu)).astype(np.float64))
    Pt = ev.softmax_rows((np.float32(chosen["s"]) * (chosen["Zt"] + np.float32(chosen["rho"]) * lpt)).astype(np.float64))

    # the page's combination of the kind phrases with the species list: weight, temperature and rule chosen on the tuning photos
    fusion = None
    if K is not None:
        kl = np.array(klabels)
        speaks = np.array([(ES.sp_eyes[chosen["keep"]] == k).any() for k in klabels])
        Qu = np.stack([Pu[:, chosen["keep"] & (ES.sp_eyes == k)].sum(1) for k in klabels], 1)
        Qt = np.stack([Pt[:, chosen["keep"] & (ES.sp_eyes == k)].sum(1) for k in klabels], 1)
        tried = []
        for rule in ("mix", "product"):
            for tk in T_KIND:
                pku = ev.softmax_rows((tk * (Xu @ K.T)).astype(np.float64))
                for w in W_KIND:
                    tried.append((float((kl[fused(pku, Qu, speaks, w, rule).argmax(1)] == ES.eyes[tune]).mean()), rule, tk, w))
        res["fusion_tried_on_tuning_photos"] = [{"rule": r_, "t_kind": tk, "w_kind": w, "kind_right": round(a_, 4)} for a_, r_, tk, w in tried]
        for rule in ("mix", "product"):
            a_, _, tk, w = max((t for t in tried if t[1] == rule), key=lambda t: t[0])
            pred = kl[fused(ev.softmax_rows((tk * (Xt @ K.T)).astype(np.float64)), Qt, speaks, w, rule).argmax(1)]
            res["kind_heads"].append({"name": "the page's combination of the kind phrases and the head `%s` (rule `%s`, t_kind %g, w_kind %g)" % (chosen["name"], rule, tk, w),
                                      "accuracy": ev.ci(pred == eyes_t), "called_person": float((pred == "person").mean()), "called_none": float((pred == "none").mean())})
            if rule == "mix":
                fusion = {"rule": rule, "t_kind": tk, "w_kind": w, "tuning_kind_right": round(a_, 4)}

    def tops(Pm, y):
        o = np.argsort(-Pm, 1)[:, :3]
        p3 = np.take_along_axis(Pm, o, 1)
        return p3[:, 0], o[:, 0] == y, p3.sum(1), (o == y[:, None]).any(1)

    pu, hu, su, h3u = tops(Pu, yu)
    pt, ht, st, h3t = tops(Pt, yt)
    grid = np.round(np.arange(0.05, 0.996, 0.01), 2)

    def threshold(conf, hit, floor=0.9, least=30):
        """The smallest threshold from which every higher threshold keeps the share right at or above `floor` on the tuning photos."""
        good = None
        for tau in grid[::-1]:
            m = conf >= tau
            if m.sum() < least:
                continue
            if hit[m].mean() >= floor:
                good = float(tau)
            else:
                break
        return good

    name_at = threshold(pu, hu)
    named_u = pu >= name_at if name_at is not None else np.zeros(len(pu), bool)
    offer_at = threshold(su[~named_u], h3u[~named_u])
    bins = [(lo, lo + 0.1) for lo in np.arange(0, 1, 0.1)]
    rel = [{"from": round(float(lo), 1), "to": round(float(hi), 1), "photos": int(((pu >= lo) & (pu < hi + (hi >= 1))).sum()),
            "mean_probability": round(float(pu[(pu >= lo) & (pu < hi + (hi >= 1))].mean()), 4) if ((pu >= lo) & (pu < hi + (hi >= 1))).any() else None,
            "right": round(float(hu[(pu >= lo) & (pu < hi + (hi >= 1))].mean()), 4) if ((pu >= lo) & (pu < hi + (hi >= 1))).any() else None} for lo, hi in bins]
    ece = float(sum(b["photos"] * abs(b["mean_probability"] - b["right"]) for b in rel if b["photos"]) / len(pu))
    conf = {"head": chosen["name"], "reliability_on_tuning_photos": rel, "expected_calibration_error": round(ece, 4), "name_at": name_at, "offer_at": offer_at}
    if name_at is not None:
        named = pt >= name_at
        offered = ~named & (st >= offer_at) if offer_at is not None else np.zeros(len(pt), bool)
        rest = ~named & ~offered
        conf["test"] = {"named": ev.ci(named), "named_right": ev.ci(ht[named]), "offered": ev.ci(offered), "offered_holds_species": ev.ci(h3t[offered]), "kind_only": ev.ci(rest)}
        conf["text"] = ("For the head `%s`, the scale was set on the tuning photos (expected calibration error %.3f there). A species is named when its probability is at least %.2f, the lowest level from which named species were right at least nine times in ten on the tuning photos%s. "
                        "On the test photos a species is then named for %s of photos and that name is right for %s of them; three species are offered for %s and hold the right one for %s; %s get a kind of eye only. This table leaves out the page's rule that offers come from the winning kind; the section on shipping applies it." % (
                            chosen["name"], ece, name_at, ("; three species are offered when the first three together reach %.2f, set the same way" % offer_at) if offer_at is not None else "; no level for offers reached nine in ten",
                            _pci(conf["test"]["named"]), _pci(conf["test"]["named_right"]), _pci(conf["test"]["offered"]), _pci(conf["test"]["offered_holds_species"]), _pci(conf["test"]["kind_only"])))
    else:
        conf["text"] = "For the head `%s`, no probability level made named species right nine times in ten on the tuning photos, so this head should name no species by itself." % chosen["name"]
    res["confidence"] = conf
    if save:
        os.makedirs(save, exist_ok=True)
        keep = chosen["keep"]
        np.savez(os.path.join(save, model + ".npz"), rows=chosen["rows"][keep], bias=chosen["bias"][keep], keep=np.nonzero(keep)[0],
                 meta=json.dumps({"model": model, "head": chosen["name"], "choice": chosen["label"], "train": mode, "train_vectors": train_name, "test_vectors": "images/" + tv,
                                  "alpha_prior": chosen["alpha"], "lam": chosen["smooth"][0], "c": chosen["smooth"][1], "name_at": name_at, "offer_at": offer_at, "fusion": fusion,
                                  "tuned_on": "the third of val kept for tuning" if mode == "val" else "val", "made_by": "tools/eval/study2.py"}))
        res["saved_head"] = os.path.join(save, model + ".npz")
    res["seconds"] = round(time.time() - t0, 1)
    return res


def _pci(v):
    return "–" if not v or v[0] is None else "%.1f%% (%.1f to %.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--train", default="val")
    ap.add_argument("--models", default="tinyclip-39m-16,tinyclip-8m-16,bioclip2-l14")
    ap.add_argument("--out")
    ap.add_argument("--save")
    a = ap.parse_args()
    out_path = a.out or "docs/eval/study2-%s.json" % a.train
    standin = a.train == "val"
    what = ("This run is a stand-in that proves the machinery. No training vectors were published when it ran, so two thirds of the `val` photos were used to fit the heads and the last third to choose settings. "
            "With about two fitting photos a species, these numbers say little about what the real training set (up to sixty photos a species) will give. They are here to show that every step runs and to be replaced."
            if standin else
            "Heads were fitted on the training photos `%s` (from before 2025, up to sixty a species), settings were chosen on `val`, and every number is from `test`." % a.train)
    out = {"made_by": "tools/eval/study2.py --train " + a.train, "standin": standin, "what": what,
           "method": {"resamples": ev.RESAMPLES, "seed": ev.SEED, "prior_weight_grid": REL, "scale_grid": SCALES, "smoothing": SMOOTH}, "models": {}}
    fetched = os.path.join(a.root, "FETCHED.json")
    if os.path.exists(fetched):
        out["inputs"] = {"branches": json.load(open(fetched))}
    for m in a.models.split(","):
        log("==", m)
        r = run_model(a.root, m, a.train, a.save)
        if r is not None:
            out["models"][m] = r
            ev.write_json(out_path, out)
