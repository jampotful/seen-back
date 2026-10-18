#!/usr/bin/env python3
"""The full database extended with the species people photograph at home, and its measurements (tools/species/EVERYDAY.md).

Reads the species tools/species/everyday.py resolved (species.csv, photos.csv), the shipped world slot (the parts, scale,
table and place files of models/naturalist/manifest.json), the world test's photos (pub/world-place) and their BioCLIP 2
vectors (pub/lab-bioclip2-l14). On a build machine (.github/workflows/everyday.yml):

  1. The rows. A species the world table already holds (same GBIF key, or the same scientific name) keeps its row; any
     other gets a new row at the end, made as the world rows were made (tools/coverage/text.py: "a photo of <name>.",
     BioCLIP 2's text half; tools/world/pack.py: one byte a number with a scale a row). Three existing rows are made
     again the same way as a check that the route agrees with the shipped rows.
  2. The prior for where people live. Each resolved species' row gets a home share, beta times its iNaturalist
     observations marked captive or cultivated over all of iNaturalist's observations, added to its share in every cell
     (tools/world/place.py); such a row never moves the place (the encounter rule skips it). beta is chosen on the tune
     photos alone, from BETAS, by the share of species right in the photo's own time zone (the smaller beta on a tie).
  3. The measurements, with the page's arithmetic (fuseWith in src/cam.rec.js, here in numpy): on the test photos of the
     resolved species, the kind right and the species right, in the photo's own time zone, in Alachua County's (America/
     New_York) and with no zone; and the world test's 3,500 photos, right species first, before and after, with no prior,
     with the time zone and with the time zone and three creatures met, at the shipped weight of the prior.
  4. With --stage: the files the page downloads that change (the last part of the rows, the scale, the table with its
     "home" list, the place file), and parts.json with every length and SHA-256.

Usage: python3 -I tools/species/everyday_build.py --species S.csv --photos P.csv --photos-dir DIR --slot DIR
         --place DIR --vectors PREFIX --out DIR [--stage DIR] [--no-world]
"""
import argparse
import csv
import hashlib
import json
import os
import struct
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools", "world"))
sys.path.insert(0, os.path.join(ROOT, "tools", "lab"))
import place  # noqa: E402
import prior  # noqa: E402
from pack import quantize  # noqa: E402

BETAS = (0.0, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0)
ALACHUA_ZONE = "America/New_York"
T0 = time.time()


def log(*a):
    print("[%5.0fs]" % (time.time() - T0), *a, flush=True)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def softmax(z):
    z = z - z.max(1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(1, keepdims=True)


class Slot:
    """Rows (float, scaled to unit length), table and place of the world slot, with the page's fusion settings and its
    kinds head."""

    def __init__(self, Qf, rows, place_raw, zones, man, kinds_rows):
        self.Qf, self.rows, self.man = Qf, rows, man
        self.f = man["fusion"]
        self.labels = man["kinds"]["labels"]
        self.K = kinds_rows
        S = len(rows)
        g = place.Grid(place_raw["res"])
        R = place.Records(g, place_raw["cells"], place_raw["rows"], place_raw["counts"], S)
        zs = {k: (np.asarray(v[0], np.int64), np.asarray(v[1], np.float64)) for k, v in zones["zones"].items()}
        self.place = place.Place(R, zones=zs, alias=zones.get("alias", {}), radius_km=man["place"]["radius_km"], eps=man["place"]["eps"])
        lab_ix = {k: i for i, k in enumerate(self.labels)}
        other = lab_ix["other"]
        self.kind_ix = np.array([lab_ix.get(r[2], other) for r in rows], np.int64)    # knownKind: a group with no view is other
        self.has = np.zeros(len(self.labels), bool)
        self.has[np.unique(self.kind_ix)] = True
        self.members = [np.nonzero(self.kind_ix == k)[0] for k in range(len(self.labels))]
        self._share = {}

    def share(self, zone, met=(), home=None):
        """share(s) for every row with no home share, where the phone probably is (the encounter rule skips a met row
        that has a home share, as the page does)."""
        met = tuple(x for x in met if home is None or not home[x] > 0)
        key = (zone, met)
        if key not in self._share:
            if len(self._share) > 32:
                self._share = {}
            self.place.home = None
            self._share[key] = np.exp(self.place.log_share(self.place.posterior(zone, met)))
        return self._share[key]

    def dots(self, X, chunk=65536):
        out = np.empty((X.shape[0], self.Qf.shape[0]), np.float32)
        for i in range(0, self.Qf.shape[0], chunk):
            out[:, i:i + chunk] = X @ self.Qf[i:i + chunk].T
        return out

    def fuse(self, X, priors, sd):
        """fuseWith of src/cam.rec.js for a slot with a kinds head and the world's prior: per photo the top row, its
        probability, the kind, the kind's probability, sure, named."""
        f = self.f
        s = softmax(f["t_species"] * sd + f["alpha_prior"] * priors)
        q = np.zeros((X.shape[0], len(self.labels)), np.float64)
        for k in range(len(self.labels)):
            if self.has[k]:
                q[:, k] = s[:, self.members[k]].sum(1)
        p = softmax(f["t_kind"] * (X @ self.K.T).astype(np.float64))
        A = (p * self.has[None, :]).sum(1, keepdims=True)
        comb = np.where(self.has[None, :], f["w_kind"] * p + (1 - f["w_kind"]) * A * q, p)
        comb = comb / comb.sum(1, keepdims=True)
        kind = comb.argmax(1)
        kp = comb[np.arange(len(kind)), kind]
        top = s.argmax(1)
        tp = s[np.arange(len(top)), top]
        sure = kp >= f["kind_at"] if f.get("kind_at") is not None else np.ones(len(kind), bool)
        lab = np.array(self.labels)
        named = sure & (tp >= f["name_at"]) & (self.kind_ix[top] == kind) & ~np.isin(lab[kind], ["none", "person"])
        return top, tp, kind, kp, sure, named


def read_slot(d, man):
    parts = [os.path.join(d, os.path.basename(p["url"])) for p in man["species"]["parts"]]
    raw = b"".join(open(p, "rb").read() for p in parts)
    Q = np.frombuffer(raw, np.int8).reshape(man["species"]["count"], man["width"])
    sc = np.fromfile(os.path.join(d, os.path.basename(man["species"]["scale"]["url"])), "<f4")
    table = json.load(open(os.path.join(d, os.path.basename(man["species"]["table"]["url"])), encoding="utf-8"))
    pr = prior.read_place(os.path.join(d, os.path.basename(man["place"]["url"])))
    zones = json.load(open(os.path.join(d, os.path.basename(man["place"]["zones"]["url"]))))
    return Q, sc, table, pr, zones


def write_place(src, dst, n_new):
    """The place file with n_new species that have no records added at the end (a varint 0 each)."""
    b = bytearray(open(src, "rb").read())
    ver, res, nr, nc, S, npairs, nbytes = struct.unpack("<IfIIIII", b[4:32])
    b[4:32] = struct.pack("<IfIIIII", ver, res, nr, nc, S + n_new, npairs, nbytes + n_new)
    b += bytes(n_new)
    open(dst, "wb").write(bytes(b))


def rate(mask):
    return float(mask.mean()) if len(mask) else float("nan")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--species", required=True)
    ap.add_argument("--photos", required=True)
    ap.add_argument("--photos-dir", required=True)
    ap.add_argument("--slot", required=True)
    ap.add_argument("--place", default="")
    ap.add_argument("--vectors", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--stage", default="")
    ap.add_argument("--no-world", action="store_true")
    ap.add_argument("--manifest", default=os.path.join(ROOT, "models", "naturalist", "manifest.json"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    man = json.load(open(a.manifest))
    Q, sc, table, pr, zones = read_slot(a.slot, man)
    rows, keys = table["species"], table["keys"]
    S0 = len(rows)
    log("slot: %d rows, width %d" % Q.shape)
    K = np.frombuffer(open(os.path.join(os.path.dirname(a.manifest), man["kinds"]["url"]), "rb").read(), np.float16)
    K = K.reshape(len(man["kinds"]["labels"]), man["width"]).astype(np.float32)

    # 1. which species have a row already, which need one
    sp = list(csv.DictReader(open(a.species, encoding="utf-8")))
    summ = json.load(open(os.path.join(os.path.dirname(a.species), "summary.json")))
    by_key = {}
    for i, k in enumerate(keys):
        if k:
            by_key.setdefault(int(k), i)
    by_sci = {}
    for i, r in enumerate(rows):
        by_sci.setdefault(r[0], i)
    new = []
    for s in sp:
        k = int(s["gbif_key"])
        if k in by_key:
            s["row"], s["row_from"] = by_key[k], "key"
        elif s["sci"] in by_sci:
            s["row"], s["row_from"] = by_sci[s["sci"]], "name"
        else:
            s["row"], s["row_from"] = S0 + len(new), "new"
            new.append(s)
    log("species %d: %d have a row (%d by key, %d by name), %d new" % (len(sp), len(sp) - len(new),
        sum(s["row_from"] == "key" for s in sp), sum(s["row_from"] == "name" for s in sp), len(new)))

    import lab  # noqa: E402 - torch and open_clip are needed from here on
    m = lab.load(lab.model_entry("bioclip2-l14"))

    def text_rows(names):
        out = []
        for j in range(0, len(names), 64):
            nj = [lab.bioclip_scientific({"sci": x}) for x in names[j:j + 64]]
            out.append(lab.unit(lab.unit(np.asarray(m.encode_text(["a photo of {}.".format(x) for x in nj]), np.float32))))
        return np.concatenate(out) if out else np.zeros((0, man["width"]), np.float32)

    # the route agrees with the shipped rows: three rows made again
    chk = [i for i in (0, S0 // 2, S0 - 1)]
    again = text_rows([rows[i][0] for i in chk])
    shipped = Q[chk].astype(np.float32) * sc[chk][:, None]
    agree = [float(x) for x in (again * shipped).sum(1)]
    log("the route made three shipped rows again, cosine %s" % agree)
    vnew = text_rows([s["sci"] for s in new])
    qn, sn = quantize(vnew)
    Qx = np.concatenate([Q, qn]) if len(new) else Q
    scx = np.concatenate([sc, sn]) if len(new) else sc
    rows_x = rows + [[s["sci"], s["en"], s["kind"]] for s in new]
    keys_x = list(keys) + [int(s["gbif_key"]) for s in new]
    for s in new:
        log("  new row %d: %s (%s) kind %s" % (s["row"], s["sci"], s["en"], s["kind"]))

    # 2. the photos' vectors
    ph = list(csv.DictReader(open(a.photos, encoding="utf-8")))
    ids, X, bad, el = lab.embed_rows(m, ph, a.photos_dir)
    log("photos: %d embedded, %d missing or unreadable, %.0fs" % (len(ids), len(bad), el))
    np.save(os.path.join(a.out, "photos.f16.npy"), X.astype(np.float16))
    json.dump(ids, open(os.path.join(a.out, "photos.ids.json"), "w"))
    pos = {x: i for i, x in enumerate(ids)}
    ph = [r for r in ph if r["id"] in pos]
    X = X[[pos[r["id"]] for r in ph]].astype(np.float32)
    row_of = {int(s["gbif_key"]): s["row"] for s in sp}
    truth = np.array([row_of[int(r["gbif_key"])] for r in ph], np.int64)

    Qf = Qx.astype(np.float32)
    Qf *= scx[:, None]
    slot = Slot(Qf, rows_x, pr, zones, man, K)
    lab_ix = {k: i for i, k in enumerate(slot.labels)}
    tkind = slot.kind_ix[truth]
    total = float(summ["inat_observations_all"])
    h = np.zeros(len(rows_x), np.float64)
    for s in sp:
        h[s["row"]] = max(h[s["row"]], float(s["captive_obs"] or 0) / total)
    zone_of = [r["zone"] if slot.place.zone_name(r["zone"]) else "" for r in ph]
    conds = {"own": zone_of, "alachua": [ALACHUA_ZONE] * len(ph), "nozone": [""] * len(ph)}

    def measure(betas, which):
        idx = np.array([i for i, r in enumerate(ph) if r["set"] == which], np.int64)
        acc = {(b, c): [[] for _ in range(6)] for b in betas for c in conds}
        for b0 in range(0, len(idx), 100):
            bi = idx[b0:b0 + 100]
            sd = slot.dots(X[bi])
            for c, zl in conds.items():
                base = np.stack([slot.share(zl[i]) for i in bi])
                for b in betas:
                    o = slot.fuse(X[bi], np.log(base + b * h[None, :]).astype(np.float32), sd)
                    for L, v in zip(acc[(b, c)], o):
                        L.append(v)
        res = {}
        for b in betas:
            res[b] = {}
            for c in conds:
                top, tp, kind, kp, sure, named = (np.concatenate(v) for v in acc[(b, c)])
                t, tk = truth[idx], tkind[idx]
                res[b][c] = {"photos": int(len(idx)), "kind_right": rate(kind == tk), "kind_sure": rate(sure),
                             "kind_right_when_sure": rate((kind == tk)[sure]), "species_right": rate(top == t),
                             "named": rate(named), "named_right": rate((top == t)[named]), "_top": top, "_kind": kind}
        return res

    tune = {}
    allr = measure(BETAS, "tune")
    for b in BETAS:
        r = allr[b]
        tune[b] = {c: {k: v for k, v in x.items() if not k.startswith("_")} for c, x in r.items()}
        log("tune beta %-5g own: kind %.3f species %.3f | alachua: kind %.3f species %.3f" % (
            b, r["own"]["kind_right"], r["own"]["species_right"], r["alachua"]["kind_right"], r["alachua"]["species_right"]))
    best = max(BETAS, key=lambda b: (round(tune[b]["own"]["species_right"], 6), -b))
    log("beta chosen on the tune photos: %g" % best)
    tb = measure(sorted({best, 0.0}), "test")
    test_best, test_zero = tb[best], tb[0.0]
    marks = {}
    for c in ("own", "alachua"):
        marks[c] = {"kind_right>=0.85": test_best[c]["kind_right"] >= 0.85, "species_right>=0.60": test_best[c]["species_right"] >= 0.60}
    # by species, in the own zone, for the record
    te = np.array([i for i, r in enumerate(ph) if r["set"] == "test"], np.int64)
    per = {}
    for j, i in enumerate(te):
        k = int(ph[i]["gbif_key"])
        d = per.setdefault(k, {"sci": ph[i]["sci"], "kind": ph[i]["kind"], "n": 0, "kind_right": 0, "species_right": 0, "said": {}})
        d["n"] += 1
        d["kind_right"] += int(test_best["own"]["_kind"][j] == tkind[i])
        d["species_right"] += int(test_best["own"]["_top"][j] == truth[i])
        said = rows_x[int(test_best["own"]["_top"][j])][0]
        d["said"][said] = d["said"].get(said, 0) + 1
    for d in per.values():
        d["said"] = sorted(d["said"].items(), key=lambda x: -x[1])[:3]

    out = {"species": len(sp), "rows_new": len(new), "rows_kept": len(sp) - len(new), "route_check_cosine": agree,
           "photos": {"tune": int(sum(r["set"] == "tune" for r in ph)), "test": int(sum(r["set"] == "test" for r in ph)), "missing": len(bad)},
           "home_denominator": total, "betas": list(BETAS), "beta": best, "tune": tune,
           "test": {c: {k: v for k, v in x.items() if not k.startswith("_")} for c, x in test_best.items()},
           "test_beta0": {c: {k: v for k, v in x.items() if not k.startswith("_")} for c, x in test_zero.items()},
           "marks": marks, "by_species": per}

    # 3. the world test, before and after, at the shipped weight of the prior
    if not a.no_world and a.place and a.vectors:
        V = np.load(a.vectors + ".f16.npy").astype(np.float32)
        V /= np.linalg.norm(V, axis=1, keepdims=True)
        vid = json.load(open(a.vectors + ".ids.json"))
        vid = vid.get("ids") if isinstance(vid, dict) else vid
        vpos = {x: i for i, x in enumerate(vid)}
        wt = [r for r in csv.DictReader(open(os.path.join(a.place, "test.tsv"), encoding="utf-8"), delimiter="\t") if r["id"] in vpos and r["lat"]]
        met = {}
        for r in csv.DictReader(open(os.path.join(a.place, "met.tsv"), encoding="utf-8"), delimiter="\t"):
            met.setdefault(r["id"], []).append(int(r["row"]))
        wtruth = np.array([int(r["row"]) for r in wt], np.int64)
        XW = V[[vpos[r["id"]] for r in wt]]
        old = Slot(Qf[:S0], rows, pr, zones, man, K)
        hb = best * h
        world = {"before": {}, "after": {}}
        tops = {(n, c): [] for n in world for c in ("none", "zone", "zone+3")}
        for b0 in range(0, len(wt), 125):
            bi = range(b0, min(len(wt), b0 + 125))
            sd = slot.dots(XW[b0:b0 + 125])
            for c in ("none", "zone", "zone+3"):
                for n, sl in (("before", old), ("after", slot)):
                    Z = sl.f["t_species"] * sd[:, :len(sl.rows)]
                    if c != "none":
                        mets = [tuple(met.get(wt[i]["id"], [])[:3]) if c == "zone+3" else () for i in bi]
                        if n == "before":
                            P = np.stack([np.log(sl.share(wt[i]["zone"], m3)) for i, m3 in zip(bi, mets)])
                        else:
                            P = np.stack([np.log(sl.share(wt[i]["zone"], m3, hb) + hb) for i, m3 in zip(bi, mets)])
                        Z = Z + sl.f["alpha_prior"] * P.astype(np.float32)
                    tops[(n, c)].append(Z.argmax(1))
            log("world test %d/%d" % (min(len(wt), b0 + 125), len(wt)))
        home_rows = [s_["row"] for s_ in sp]
        for (n, c), v in tops.items():
            top = np.concatenate(v)
            world[n][c] = {"photos": len(wt), "top1": rate((top == wtruth) & (wtruth >= 0)), "taken_by_a_home_row": int(np.isin(top, home_rows).sum())}
            log("world test %s %s: top1 %.4f" % (n, c, world[n][c]["top1"]))
        out["world_test"] = world
        out["world_drop_points"] = {c: round(100 * (world["before"][c]["top1"] - world["after"][c]["top1"]), 2) for c in world["before"]}
        out["marks"]["world_test_no_drop_over_1_point"] = all(v <= 1.0 for v in out["world_drop_points"].values())

    # 4. the files that change, for the page
    if a.stage:
        os.makedirs(a.stage, exist_ok=True)
        last = man["species"]["parts"][-1]
        lp = os.path.join(a.slot, os.path.basename(last["url"]))
        with open(os.path.join(a.stage, os.path.basename(last["url"])), "wb") as f:
            f.write(open(lp, "rb").read())
            f.write(qn.tobytes())
        scx.astype("<f4").tofile(os.path.join(a.stage, "scale.f32"))
        tx = dict(table)
        tx["species"], tx["keys"] = rows_x, keys_x
        tx["home"] = [[int(r), float("%.6g" % (best * v))] for r, v in enumerate(h) if v > 0]
        tx["home_from"] = ("tools/species/everyday_build.py: beta %g times the species' iNaturalist observations marked captive or "
                           "cultivated over all iNaturalist observations (%d), added to its share in every cell" % (best, total))
        json.dump(tx, open(os.path.join(a.stage, "table.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
        write_place(os.path.join(a.slot, os.path.basename(man["place"]["url"])), os.path.join(a.stage, "place.bin"), len(new))
        whole = hashlib.sha256()
        for p in man["species"]["parts"][:-1]:
            whole.update(open(os.path.join(a.slot, os.path.basename(p["url"])), "rb").read())
        whole.update(open(os.path.join(a.stage, os.path.basename(last["url"])), "rb").read())

        def one(n):
            p = os.path.join(a.stage, n)
            return {"name": n, "bytes": os.path.getsize(p), "sha256": sha(p)}
        pj = {"count": len(rows_x), "width": man["width"], "rows_bytes": int(Qx.size), "rows_sha256": whole.hexdigest(),
              "last_part": one(os.path.basename(last["url"])), "scale": one("scale.f32"), "table": one("table.json"),
              "place": one("place.bin"), "beta": best, "new_rows": len(new)}
        json.dump(pj, open(os.path.join(a.stage, "parts.json"), "w"), indent=1)
        out["stage"] = pj
        log("stage: %s" % json.dumps(pj))
        # the extended slot read back as the page reads it
        pr2 = prior.read_place(os.path.join(a.stage, "place.bin"))
        assert pr2["S"] == len(rows_x) and len(pr2["rows"]) == len(pr["rows"])
    json.dump(out, open(os.path.join(a.out, "everyday.json"), "w"), indent=1, default=float)
    log("marks: %s" % json.dumps(out["marks"]))


if __name__ == "__main__":
    main()
