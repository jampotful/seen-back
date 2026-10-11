#!/usr/bin/env python3
"""Parity of the reference with the page, to 1e-6: both rules, trained heads' biases, and awkward inputs.

    python3 -I tools/fusion/parity.py make cases.json            # the cases
    node test/rec/fuse_page.js cases.json page.json               # the page's own answers (needs test/rec/serve.js running; PORT says where)
    python3 -I tools/fusion/parity.py check cases.json page.json  # exits 1 on any difference

Three kinds of case:
  "loaded"  scores fed to the stand-in slot as the page loaded it (test/rec/models/standin): the product rule, no biases.
  "worlds"  scores fed to settings made up here and handed to the page through the same readers a real slot goes through
            (pocket.test.world): each rule, biases for the kinds, the species, both or neither, temperatures from 1e-4 to 1e5,
            weights of 0 and 1, floors and guards, a table whose rows lack monthly weights, a month with no records at all,
            no month, kinds with no species rows, species of kinds outside the labels, ties, zeros, one head sure against the other.
  "photos"  the stand-in's trained-head slot (manifest.trained.json: rows that are not unit vectors, kinds.bias, species.bias_url, the
            mixing rule) run on the test photos in the page from pixels to answer. The page hands back its own embedding, its
            row scores and its answer; the reference must get the row scores from the embedding and the files (to 1e-5: the
            page's are single precision) and the same answer from the page's row scores (to 1e-6).
"""
import json, pathlib, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from fuse import dots, fuse, load_slot

STANDIN = pathlib.Path(__file__).resolve().parents[2] / "test" / "rec" / "models" / "standin"
slot = load_slot(STANDIN)
m, t = slot["manifest"], slot["table"]
nk, ns = len(m["kinds"]["labels"]), len(t)
M12 = [10] * 12


def page_manifest(labels, fusion, kind_bias, n_species):
    """A manifest the page's reader accepts; the encoder's fields are fillers, since nothing is encoded."""
    out = {"id": "parity", "vision": {"url": "x.onnx", "size": 224, "mean": [0, 0, 0], "std": [1, 1, 1]}, "width": 4, "fusion": fusion}
    if labels is not None:                                            # None: a slot without a kinds head
        out["kinds"] = {"url": "k.bin", "labels": labels}
    if kind_bias is not None:
        out["kinds"]["bias"] = kind_bias
    if n_species:
        out["species"] = {"url": "s.bin", "table": "t.json", "count": n_species}
    return out


def make(path):
    rs = np.random.RandomState(20261011)
    cases = []
    # ---- the slot as loaded (the cases of build 6's check)
    for i in range(300):
        scale = [1, 1, 1, 0.001, 0.05, 30][i % 6]                 # tiny and huge temperatures
        cases.append({"kd": (rs.uniform(-0.2, 1, nk) * scale).tolist(), "sd": (rs.uniform(-0.2, 1, ns) * scale).tolist(), "month": int(rs.randint(0, 12))})
    for month in range(12):                                         # everything equal; everything zero
        cases.append({"kd": [0.5] * nk, "sd": [0.5] * ns, "month": month})
        cases.append({"kd": [0.0] * nk, "sd": [0.0] * ns, "month": month})
    for k in range(nk):                                             # each kind sure of itself against a species list sure of something else, and ties between two kinds
        for j in (0, 5, 6, ns - 1):
            kd = [0.0] * nk; kd[k] = 1.0; sd = [0.0] * ns; sd[j] = 1.0
            cases.append({"kd": kd, "sd": sd, "month": (k + j) % 12})
        kd = [0.0] * nk; kd[k] = kd[(k + 1) % nk] = 0.7
        cases.append({"kd": kd, "sd": [0.3] * ns, "month": k % 12})

    # ---- made-up settings
    full = list(m["kinds"]["labels"])
    few = ["wader", "plant", "bird", "person", "none"]                # the table below has kinds these labels lack
    awkward = [
        ["Ardea herodias", "Great Blue Heron", "wader", M12],
        ["Eudocimus albus", "White Ibis", "wader", [0, 0, 5, 0, 9, 9, 9, 9, 9, 9, 9, 9]],
        ["Bidens alba", "Beggarticks", "plant", None],                 # no monthly weights at all
        ["Quercus virginiana", "", "plant", [0] * 12],                  # never recorded
        ["Danaus plexippus", "Monarch", "insect", [3, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2]],
        {"sci": "Dione vanillae", "en": "Gulf Fritillary", "eyes": "insect", "m": [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]},   # a row as an object
        ["Trichonephila clavipes", "Golden Silk Spider", "a kind no page knows", [2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2]],  # read as "other"
        ["Homo sapiens", "Human", "person", [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]],
        ["Cardinalis cardinalis", "Northern Cardinal", "bird", [7, 7, 7, 0, 7, 7, 7, 7, 7, 7, 7]],                         # eleven weights: read as none
    ]                                                                 # April (month 3) has no records in any row: the prior is left out
    tables = {"standin": t, "awkward": awkward, "one": [["Ardea herodias", "Great Blue Heron", "wader", M12]], "none": None}
    worlds = []
    pick = lambda xs: xs[rs.randint(len(xs))]
    for rule in ("product", "mix"):
        for bias in ("none", "kinds", "species", "both"):
            for tname in ("standin", "awkward", "one", "none"):
                for labels in (full, few):
                    for rep in range(2):
                        table = tables[tname]
                        f = {"t_kind": pick([1e-4, 1, 30, 100, 1e5]), "t_species": pick([1e-4, 1, 30, 100, 1e5]), "alpha_prior": pick([0, 0.25, 0.5, 2]),
                             "w_kind": pick([0, 0.3, 0.5, 0.7, 1]), "name_at": pick([0, 0.3, 0.6, 1.1]), "offer_at": pick([0, 0.3, 0.9]), "rule": rule}
                        if rep == 0 and rule == "product":
                            del f["rule"]                             # the default
                        if rs.rand() < 0.5: f["prior_floor"] = pick([1e-6, 1e-3, 0])
                        if rs.rand() < 0.5: f["guard"] = pick([1e-9, 1e-3, 1e-30])
                        if rs.rand() < 0.3: f["offer_any_kind"] = True
                        if rs.rand() < 0.6: f["kind_at"] = pick([0, 0.3, 0.5, 0.9, 1, 1.1])     # not sure is an answer; absent in the rest, as before build 8
                        kb = [float(v) for v in np.round(rs.randn(len(labels)) * 3, 3)] if bias in ("kinds", "both") else None
                        sb = [float(v) for v in np.float32(rs.randn(len(table)) * 3)] if table is not None and bias in ("species", "both") else None
                        if kb is not None and rs.rand() < 0.3: kb[rs.randint(len(kb))] = 50.0     # one bias that outweighs everything
                        if sb is not None and rs.rand() < 0.3: sb[rs.randint(len(sb))] = -50.0
                        worlds.append({"manifest": page_manifest(labels, f, kb, len(table) if table is not None else 0), "table": table, "sb": sb})
    # ---- slots without a kinds head (the larger model): the kind is each kind's share of the species answer
    for tname in ("standin", "awkward", "one"):
        for bias in (False, True):
            for kind_at in (None, 0, 0.5, 0.9, 1, 1.1):
                table = tables[tname]
                f = {"t_species": pick([1e-4, 1, 30, 100, 1e5]), "alpha_prior": pick([0, 0.5, 2]), "name_at": pick([0, 0.3, 0.6, 1.1]), "offer_at": pick([0, 0.3, 0.9])}
                if kind_at is not None: f["kind_at"] = kind_at
                if rs.rand() < 0.5: f["prior_floor"] = pick([1e-6, 1e-3, 0])
                if rs.rand() < 0.3: f["offer_any_kind"] = True
                sb = [float(v) for v in np.float32(rs.randn(len(table)) * 3)] if bias else None
                worlds.append({"manifest": page_manifest(None, f, None, len(table)), "table": table, "sb": sb})
    for w, world in enumerate(worlds):
        headless = "kinds" not in world["manifest"]
        n, table = (0 if headless else len(world["manifest"]["kinds"]["labels"])), world["table"]
        k = len(table) if table is not None else 0
        sd = lambda v: v if table is not None else None
        for i in range(8):
            scale = [1, 1, 5, 0.01][i % 4]                            # a trained head's rows are not unit length: scores beyond 1
            cases.append({"world": w, "kd": (rs.uniform(-0.3, 1, n) * scale).tolist(), "sd": sd((rs.uniform(-0.3, 1, k) * scale).tolist()), "month": int(rs.randint(0, 12))})
        cases.append({"world": w, "kd": [0.5] * n, "sd": sd([0.5] * k), "month": 3})                     # all equal, in the month nobody recorded
        cases.append({"world": w, "kd": [0.0] * n, "sd": sd([0.0] * k), "month": None})                  # all zero, and no month known
        a, b = rs.randint(max(n, 1)), rs.randint(max(k, 1))
        if headless:                                                  # no kind scores at all: one species sure, and every species tied
            s1 = [0.0] * k; s1[b] = 1.0
            cases.append({"world": w, "kd": None, "sd": s1, "month": int(rs.randint(0, 12))})
            cases.append({"world": w, "kd": None, "sd": [0.3] * k, "month": 0})
            for c in cases[-10:]:
                if c.get("world") == w: c["kd"] = None
            continue
        kd = [0.0] * n; kd[a] = 1.0; s1 = [0.0] * k
        if k: s1[b] = 1.0
        cases.append({"world": w, "kd": kd, "sd": sd(s1), "month": int(rs.randint(0, 12))})              # one head sure against the other
        kd = [0.0] * n; kd[a] = kd[(a + 1) % n] = 0.7
        cases.append({"world": w, "kd": kd, "sd": sd([0.3] * k), "month": 0})                            # two kinds tied, every species tied
        cases.append({"world": w, "kd": (rs.uniform(-0.3, 1, n)).tolist(), "sd": None, "month": 6})      # the species head left out, as when the person is far from the list's place
    photos = {"slot": "test/rec/models/standin/manifest.trained.json", "names": sorted(json.loads((STANDIN / "expect.json").read_text())["photos"])}
    pathlib.Path(path).write_text(json.dumps({"cases": cases, "worlds": worlds, "photos": photos}))
    print(len(cases), "cases in", len(worlds), "made-up settings and the loaded slot;", len(photos["names"]), "photos through the trained-head slot")


def differences(r, g):
    why = []
    if r["kind"] != g["kind"]: why.append("kind %s / %s" % (r["kind"], g["kind"]))
    if [k["key"] for k in r["kinds"]] != [k["key"] for k in g["kinds"]]: why.append("order of kinds")
    if [s["sci"] for s in r["species"]] != [s["sci"] for s in g["species"]]: why.append("top five")
    if (r["named"] or {}).get("sci") != (g["named"] or {}).get("sci"): why.append("named")
    if r["sure"] is not g.get("sure"): why.append("sure %s / %s" % (r["sure"], g.get("sure")))
    if r["kindOffers"] != g.get("kindOffers"): why.append("the three kinds offered")
    if [k["head"] is None for k in r["kinds"]] != [k["head"] is None for k in g["kinds"]]: why.append("which answers have a kinds head")
    if [s["sci"] for s in r["offers"]] != [s["sci"] for s in g["offers"]]: why.append("offers")
    if [k["list"] is None for k in r["kinds"]] != [k["list"] is None for k in g["kinds"]]: why.append("which kinds the list speaks for")
    nums = [abs(a["p"] - b["p"]) for a, b in zip(r["kinds"], g["kinds"])] + [abs(a["head"] - b["head"]) for a, b in zip(r["kinds"], g["kinds"]) if a["head"] is not None and b["head"] is not None]
    nums += [abs(a["list"] - b["list"]) for a, b in zip(r["kinds"], g["kinds"]) if a["list"] is not None and b["list"] is not None]
    nums += [abs(a["p"] - b["p"]) for a, b in zip(r["species"], g["species"])] + [abs(r["kindP"] - g["kindP"])]
    d = max(nums)
    if not d <= 1e-6: why.append("numbers differ by %.3g" % d)       # also catches a NaN
    return d, why


def check(cases_path, page_path):
    made = json.loads(pathlib.Path(cases_path).read_text()); page = json.loads(pathlib.Path(page_path).read_text())
    cases, worlds = made["cases"], made["worlds"]
    worst, bad, by, unsure = 0.0, [], {}, 0
    for i, (c, g) in enumerate(zip(cases, page["cases"])):
        if "world" in c:
            w = worlds[c["world"]]
            kb = (w["manifest"].get("kinds") or {}).get("bias")
            r = fuse(w["manifest"], w["table"], c["month"], c["kd"], c["sd"], kind_bias=kb, species_bias=w["sb"])
            tag = (w["manifest"]["fusion"].get("rule", "product") if "kinds" in w["manifest"] else "no kinds head") + (", biases" if w["sb"] is not None or kb is not None else ", no biases")
            tag += ", kind_at" if w["manifest"]["fusion"].get("kind_at") is not None else ""
            unsure += not r["sure"]
        else:
            r = fuse(m, t, c["month"], c["kd"], c["sd"]); tag = "the loaded slot (product, no biases)"
        d, why = differences(r, g)
        worst = max(worst, d); by[tag] = by.get(tag, 0) + 1
        if why: bad.append(("case %d (%s)" % (i, tag), why))
    if len(page["cases"]) != len(cases): bad.append(("count", ["the page answered %d of %d cases" % (len(page["cases"]), len(cases))]))
    for tag in sorted(by): print("  %5d cases: %s" % (by[tag], tag))
    print(len(cases), "cases (%d of them not sure), largest difference in any probability %.3g," % (unsure, worst), len(bad), "differ")
    # ---- the trained-head slot, from pixels
    tr = load_slot(STANDIN / "manifest.trained.json")
    worst_dot, worst_p = 0.0, 0.0
    for name in made["photos"]["names"]:
        g = page["photos"].get(name)
        if not g: bad.append((name, ["the page gave no answer"])); continue
        e = np.asarray(g["emb"], dtype=np.float64)
        dk = float(np.max(np.abs(dots(tr["kinds"], e) - np.asarray(g["kd"])))); ds = float(np.max(np.abs(dots(tr["species"], e) - np.asarray(g["sd"]))))
        r = fuse(tr["manifest"], tr["table"], g["month"], g["kd"], g["sd"], kind_bias=tr["kind_bias"], species_bias=tr["species_bias"])
        d, why = differences(r, g["result"])
        worst_dot, worst_p = max(worst_dot, dk, ds), max(worst_p, d)
        if max(dk, ds) > 1e-5: why.append("row scores differ by %.3g" % max(dk, ds))
        if why: bad.append((name, why))
    print(len(made["photos"]["names"]), "photos through the trained-head slot (%s, rule %s): largest difference in a row score %.3g, in a probability %.3g" % (
        tr["manifest"]["id"], tr["manifest"]["fusion"].get("rule", "product"), worst_dot, worst_p))
    for where, why in bad[:16]: print("  DIFFERS", where, why)
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    if sys.argv[1] == "make":
        make(sys.argv[2])
    else:
        check(sys.argv[2], sys.argv[3])
