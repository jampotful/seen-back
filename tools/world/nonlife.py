#!/usr/bin/env python3
"""Photos with nothing alive in them: how the pocket slot's head treats them, and whether a rule that sends such a photo to the
"what did you photograph?" sheet can hold the pass marks of docs/tracks/head.md (burst 12, item 2).

The page as it runs (tools/fusion/fuse.py, through head.py's vectorized copy, checked against it here on 60 photos of each set): in
the county's time zone the head with kinds.county_bias is combined with the county species list; elsewhere the head answers alone
with kinds.bias. An answer is asserted ("sure") when the fused probability of the winning kind reaches fusion.kind_at.

The harm measured: a photo of COCO's `none` rows (indoor objects, nothing alive) for which the page asserts a living kind, that is a
kind other than none and person, so that the page shows a creature's eyes for a cup or a heap of coins.

The rules tried, each applied only to an asserted living kind, which it turns into "not sure" (the sheet that asks):
  head_none  the head's own probability of `none` (before the list) is at least tau
  fused_none the fused probability of `none` is at least tau
  gap        the winning kind's fused probability minus that of `none` is under tau
  life       the best species row's dot with the photo is under tau (how near the photo is to any living thing the county list holds)
  other_conf the asserted kind is `other` (which the page calls "this creature") and its fused probability is under tau: a level of
             its own for `other`, above fusion.kind_at

No pass mark counts a real creature filed under `other` that a rule sends to the sheet, so each reading also reports
`real_other_asked`: the world photos of creatures in no carried group (truth `other`) that the page calls "this creature" today
and that the rule newly sends to the sheet.

Scoring is strict: a photo the rule newly sends to the sheet counts as not named and not right, for every mark. The marks:
groups named (primate, whale, bat: 75% named and 75% right when called, world test photos, head alone), old kinds on world photos
(head alone) and on Alachua photos (head and list) with the 95% interval of the paired difference against today above -2 points,
COCO's balanced share within 1 point of 0.9467 (both ways), the share of world `other` photos given a view under 10%. File size and
time do not change: a rule is a comparison on numbers the page already has.

tau is chosen on the tuning photos only (the most COCO `none` photos kept from a living kind with every mark held there); the test
photos are read once, after.

Usage: python3 -I tools/world/nonlife.py ROOT --out OUT   (ROOT laid out as for head.py: data/, lab/tinyclip-39m-16/images/, world/)
"""
import argparse, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "fusion"))
import head as H  # noqa: E402
import fuse as F  # noqa: E402

CARRIED = ("primate", "whale", "bat")
LIVING_NOT = ("none", "person")


def head_probs(X, K, kb, labels):
    z = X.astype(np.float64) @ K.T + kb
    z -= z.max(axis=1, keepdims=True)
    p = np.exp(z); p /= p.sum(axis=1, keepdims=True)
    ul = list(dict.fromkeys(labels))
    pu = np.zeros((len(p), len(ul)))
    for i, lab in enumerate(labels):
        pu[:, ul.index(lab)] += p[:, i]
    return pu, ul


def fused_all(X, months, K, kb, labels, fusion, table):
    """Every kind's fused probability (head.answer gives only the winner's)."""
    p, ul = head_probs(X, K, kb, labels)
    if table is None:
        return p, ul
    speaks = np.array([lab in table.kinds for lab in ul])
    q = H.species_shares(X, months, table, fusion)
    Q = np.zeros_like(p)
    for i, lab in enumerate(ul):
        if speaks[i]:
            Q[:, i] = q[:, table.kinds.index(lab)]
    share = (p * speaks).sum(axis=1, keepdims=True)
    w = fusion["w_kind"]
    c = np.where(speaks, w * p + (1 - w) * share * Q, p)
    return c / c.sum(axis=1, keepdims=True), ul


def features(d, slot, table, with_list):
    m = slot["manifest"]; f = m["fusion"]; labels = m["kinds"]["labels"]
    K = slot["kinds"]; kb = slot["kind_bias_list"] if with_list else slot["kind_bias"]
    X = d["X"]
    kind, prob = H.answer(X, d["month"], K, f["t_kind"] * kb, labels, f, table if with_list else None)
    c, ul = fused_all(X, d["month"], K, f["t_kind"] * kb, labels, f, table if with_list else None)
    ph, _ = head_probs(X, K, f["t_kind"] * kb, labels)
    assert np.all(np.array([ul[i] for i in c.argmax(1)]) == kind)
    ni = ul.index("none")
    life = (X.astype(np.float64) @ slot["species"].T).max(axis=1)
    sure = prob >= f["kind_at"]
    living = sure & ~np.isin(kind, LIVING_NOT)
    return {"kind": kind, "prob": prob, "sure": sure, "living": living, "head_none": ph[:, ni], "fused_none": c[:, ni],
            "gap": prob - c[:, ni], "life": life}


def gate(ft, rule, tau):
    """True where the rule sends an asserted living kind to the sheet."""
    if rule is None:
        return np.zeros(len(ft["kind"]), bool)
    if rule == "other_conf":
        return ft["living"] & (ft["kind"] == "other") & (ft["prob"] < tau)
    v = ft[rule]
    hit = v >= tau if rule in ("head_none", "fused_none") else v < tau
    return ft["living"] & hit


def boot_diff(diff, seed=H.SEED, n=2000):
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(diff), size=(n, len(diff)))
    means = diff[idx].mean(axis=1)
    return float(diff.mean()), float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def marks(S, rule, tau):
    """Every mark for one rule and level on one reading (tuning or test)."""
    out, ok = {}, True
    # groups named, world photos, head alone
    w = S["world"]; ft = w["ft_alone"]; asked = gate(ft, rule, tau); y = w["yf"]
    kind = np.where(asked, "asked", ft["kind"])
    gm = H.group_marks(kind, y, CARRIED)
    out["groups"] = gm; ok &= all(g["pass"] for g in gm.values())
    # old kinds, world (head alone) and Alachua (head and list): paired difference against today, strict
    for name, d, key in (("old_world", w, "ft_alone"), ("old_alachua", S["alachua"], "ft_list")):
        ft = d[key]; sel = np.isin(d["y"], H.VIEWS); asked = gate(ft, rule, tau)
        before = (ft["kind"] == d["y"])[sel].astype(float)
        after = ((ft["kind"] == d["y"]) & ~asked)[sel].astype(float)
        mean, lo, hi = boot_diff(after - before)
        out[name] = {"photos": int(sel.sum()), "today": round(before.mean(), 4), "with_rule": round(after.mean(), 4),
                     "diff_points": round(100 * mean, 2), "ci_points": [round(100 * lo, 2), round(100 * hi, 2)], "pass": bool(100 * lo > -2)}
        ok &= out[name]["pass"]
    # COCO, both ways
    c = S["coco"]
    for name, key in (("coco_list", "ft_list"), ("coco_alone", "ft_alone")):
        ft = c[key]; asked = gate(ft, rule, tau)
        kind = np.where(asked, "asked", ft["kind"])
        share = H.balanced_share(kind, c["y"], H.COCO_KEYS)
        out[name] = {"balanced": round(share, 4), "pass": bool(share >= 0.9467 - 0.01)}
        ok &= out[name]["pass"]
    # world `other` photos given a view (an asserted kind with a view); asked photos get none
    ft = w["ft_alone"]; asked = gate(ft, rule, tau); oth = y == "other"
    view = ft["sure"] & np.isin(ft["kind"], H.VIEWS) & ~asked
    out["other_view"] = {"share": round(float(view[oth].mean()), 4), "pass": bool(view[oth].mean() < 0.10)}
    today_other = ft["living"] & (ft["kind"] == "other") & oth
    out["real_other_asked"] = {"photos": int(today_other.sum()), "asked": int((today_other & asked).sum()),
                               "share": round(float((today_other & asked).sum() / max(1, today_other.sum())), 4), "all_world_asked": round(float(asked.mean()), 4)}
    ok &= out["other_view"]["pass"]
    # the harm: COCO none photos and the made photos given a living kind, both ways
    for name, d, key in (("nonlife_list", c, "ft_list"), ("nonlife_alone", c, "ft_alone"), ("made_list", S["made"], "ft_list"), ("made_alone", S["made"], "ft_alone")):
        ft = d[key]; none = d["y"] == "none"; asked = gate(ft, rule, tau)
        liv = ft["living"] & ~asked
        out[name] = {"photos": int(none.sum()), "living_kind": int(liv[none].sum()), "share": round(float(liv[none].mean()), 4),
                     "kinds": dict(sorted(((str(k), int(n)) for k, n in zip(*np.unique(ft["kind"][none & liv], return_counts=True))), key=lambda x: -x[1]))}
    out["all_pass"] = bool(ok)
    return out


def made_part(made, part):
    """The photos made by tools/world/nonlife_make.py, with a month from a hash of the id as for COCO."""
    man = {r["id"]: r for r in H.read_csv(os.path.join(made, "manifest.csv"))}
    X = H.unit(np.load(os.path.join(made, "nonlife-made.f16.npy")).astype(np.float32))
    ids = json.load(open(os.path.join(made, "nonlife-made.ids.json")))
    keep = [i for i, j in enumerate(ids) if man[j]["set"] == part]
    return {"X": X[keep], "y": np.array(["none"] * len(keep), dtype=object), "ids": [ids[i] for i in keep],
            "family": np.array([man[ids[i]]["family"] for i in keep]), "month": np.array([H.h8("month|" + ids[i]) % 12 for i in keep])}


def reading(root, part, slot, table, by_key, made):
    W, _ = H.world_parts(root, (part,), "auto", None)
    A, _ = H.alachua_parts(root, (part,), "auto", None, by_key)
    C, _ = H.coco_parts(root, (part,), "auto", None)
    w, a, c = W[part], A[part], C[part]
    w["yf"] = H.folded(w["y"], set(CARRIED))
    w["ft_alone"] = features(w, slot, table, False)
    a["ft_list"] = features(a, slot, table, True)
    c["ft_list"] = features(c, slot, table, True)
    c["ft_alone"] = features(c, slot, table, False)
    md = made_part(made, part)
    md["ft_list"] = features(md, slot, table, True)
    md["ft_alone"] = features(md, slot, table, False)
    return {"world": w, "alachua": a, "coco": c, "made": md}


def parity_check(S, slot, table_rows):
    """head.answer against fuse.fuse on 60 photos of each set, as head.py does."""
    m = slot["manifest"]; bad = 0
    for d, key, with_list in ((S["alachua"], "ft_list", True), (S["coco"], "ft_list", True), (S["coco"], "ft_alone", False), (S["world"], "ft_alone", False)):
        for i in range(min(60, len(d["X"]))):
            o = F.fuse(m, table_rows if with_list else None, int(d["month"][i]), F.dots(slot["kinds"], d["X"][i]),
                       F.dots(slot["species"], d["X"][i]) if with_list else None, kind_bias=slot["kind_bias"], species_bias=slot["species_bias"],
                       kind_bias_list=slot["kind_bias_list"] if with_list else None)
            if o["kind"] != d[key]["kind"][i] or abs(o["kindP"] - d[key]["prob"][i]) > 1e-6 or o["sure"] != bool(d[key]["sure"][i]):
                bad += 1
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root"); ap.add_argument("--out", required=True); ap.add_argument("--slot", default="models/pocket")
    ap.add_argument("--made", required=True, help="the output directory of tools/world/nonlife_make.py")
    ap.add_argument("--tune-only", action="store_true", help="stop before the test photos are loaded")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    slot = F.load_slot(a.slot)
    table_rows = slot["table"]
    table = H.Table(slot, table_rows, list(F.KINDS))
    by_key = H.county_keys(a.root)
    rep = {"slot": a.slot, "kind_at": slot["manifest"]["fusion"]["kind_at"]}

    T = reading(a.root, "tune", slot, table, by_key, a.made)
    rep["parity_tune_differ"] = parity_check(T, slot, table_rows)
    if rep["parity_tune_differ"]:
        sys.exit("the vectorized rule disagrees with tools/fusion/fuse.py")
    rep["tune_today"] = marks(T, None, 0)

    # the distributions behind the rules: COCO none photos given a living kind, against living photos rightly asserted
    c = {k: np.concatenate([T["coco"]["ft_list"][k][T["coco"]["y"] == "none"], T["made"]["ft_list"][k]]) for k in ("living", "head_none", "fused_none", "gap", "life")}
    bad = c["living"]
    al = T["alachua"]["ft_list"]; good = al["living"] & (al["kind"] == T["alachua"]["y"])
    rep["tune_spread"] = {r: {"nonlife_wrong": [round(float(np.percentile(c[r][bad], q)), 4) for q in (10, 50, 90)] if bad.any() else None,
                              "alachua_right": [round(float(np.percentile(al[r][good], q)), 4) for q in (1, 5, 10, 50)]} for r in ("head_none", "fused_none", "gap", "life")}
    rep["tune_spread"]["count"] = {"nonlife_wrong": int(bad.sum()), "alachua_right": int(good.sum())}

    grids = {"head_none": np.round(np.arange(0.02, 0.61, 0.02), 2), "fused_none": np.round(np.arange(0.01, 0.13, 0.01), 2),
             "gap": np.round(np.arange(0.88, 1.0, 0.01), 2), "life": np.round(np.percentile(al["life"][good], [0.1, 0.25, 0.5, 1, 2, 3, 5, 8]), 3),
             "other_conf": np.round(np.arange(0.88, 0.99, 0.01), 2)}
    rows, best = [], None
    for rule, grid in grids.items():
        for tau in grid:
            mk = marks(T, rule, float(tau))
            r = {"rule": rule, "tau": float(tau), "all_pass": mk["all_pass"], "nonlife_list": mk["nonlife_list"]["living_kind"],
                 "made_list": mk["made_list"]["living_kind"], "made_alone": mk["made_alone"]["living_kind"],
                 "nonlife_alone": mk["nonlife_alone"]["living_kind"], "old_alachua": mk["old_alachua"]["diff_points"],
                 "old_alachua_lo": mk["old_alachua"]["ci_points"][0], "old_world": mk["old_world"]["diff_points"],
                 "old_world_lo": mk["old_world"]["ci_points"][0], "coco_list": mk["coco_list"]["balanced"], "coco_alone": mk["coco_alone"]["balanced"],
                 "real_other_asked": mk["real_other_asked"]["share"],
                 "groups": {g: [v["named"], v["right_when_called"]] for g, v in mk["groups"].items()}}
            rows.append(r)
            key = (r["nonlife_list"] + r["nonlife_alone"] + r["made_list"] + r["made_alone"], -r["old_alachua"], -r["coco_list"])
            if r["all_pass"] and (best is None or key < best[0]):
                best = (key, rule, float(tau))
    rep["tune_grid"] = rows
    if a.tune_only:
        rep["chosen"] = {"rule": best[1], "tau": best[2]} if best else None
        rep["tune_chosen"] = marks(T, best[1], best[2]) if best else None
        rep["decision"] = "tuning only: the test photos were not read"
    elif best is None:
        rep["chosen"] = None
        rep["decision"] = "no rule holds every mark on the tuning photos; the test photos are not read"
    else:
        rep["chosen"] = {"rule": best[1], "tau": best[2]}
        rep["tune_chosen"] = marks(T, best[1], best[2])
        S = reading(a.root, "test", slot, table, by_key, a.made)                                # read once, after the choice
        rep["parity_test_differ"] = parity_check(S, slot, table_rows)
        rep["test_today"] = marks(S, None, 0)
        rep["test_chosen"] = marks(S, best[1], best[2])
        rep["decision"] = ("the chosen rule holds every mark on the test photos" if rep["test_chosen"]["all_pass"] else "the chosen rule fails a mark on the test photos") + \
            "; whether it ships is decided in tools/world/NONLIFE.md, with real_other_asked beside the marks"
    json.dump(rep, open(os.path.join(a.out, "report.json"), "w"), indent=1)
    print(json.dumps({k: rep[k] for k in ("chosen", "decision")}, indent=1))
    for k in ("tune_today", "tune_chosen", "test_today", "test_chosen"):
        if k in rep:
            r = rep[k]
            print(k, "all_pass", r["all_pass"], "| nonlife list", r["nonlife_list"]["living_kind"], "/", r["nonlife_list"]["photos"], r["nonlife_list"]["kinds"],
                  "| alone", r["nonlife_alone"]["living_kind"], "| made list", r["made_list"]["living_kind"], "/", r["made_list"]["photos"], r["made_list"]["kinds"],
                  "| made alone", r["made_alone"]["living_kind"], r["made_alone"]["kinds"], "| old alachua", r["old_alachua"]["diff_points"], r["old_alachua"]["ci_points"],
                  "| old world", r["old_world"]["diff_points"], r["old_world"]["ci_points"], "| coco", r["coco_list"]["balanced"], r["coco_alone"]["balanced"],
                  "| other view", r["other_view"]["share"], "| real other asked", r["real_other_asked"]["share"], "| groups", {g: (v["named"], v["right_when_called"]) for g, v in r["groups"].items()})


if __name__ == "__main__":
    main()
