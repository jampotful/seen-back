#!/usr/bin/env python3
"""The full database extended with the species people photograph at home, and its measurements (tools/species/EVERYDAY.md).

Reads the species tools/species/everyday.py resolved (species.csv, photos.csv), the world slot as it was before these
species (the parts, scale, table and place files kept by pin/naturalist-world-9ae0806), the world test's photos
(pub/world-place) and their BioCLIP 2 vectors (pub/lab-bioclip2-l14). On a build machine (.github/workflows/everyday.yml):

  1. The rows, under two rules. "own" (build 34): a species the world table already holds (same GBIF key, or the same
     scientific name) keeps its row, and any other gets a new row at the end, made as the world rows were made
     (tools/coverage/text.py: "a photo of <name>.", BioCLIP 2's text half; tools/world/pack.py: one byte a number with a
     scale a row). "accepted" (build 35): as "own", except that a species GBIF lists as a synonym takes the world row of
     the species GBIF accepts for it (the accepted name's species key, from api.gbif.org) when that row already carries
     the same English name, as the domestic dog does under Canis lupus. Three existing rows are made again the same way
     as a check that the route agrees with the shipped rows.
  2. The prior for where people live. Each resolved species' row gets a home share, beta times its iNaturalist
     observations marked captive or cultivated over all of iNaturalist's observations, added to its share in every cell
     (tools/world/place.py); such a row never moves the place (the encounter rule skips it). beta is chosen on the tune
     photos alone, from BETAS, by the share of species right in the photo's own time zone (the smaller beta on a tie),
     among the betas whose world-test drops are all within the mark.
  3. The measurements, with the page's arithmetic (fuseWith in src/cam.rec.js, here in numpy): on the test photos of the
     resolved species, the kind right and the species right, in the photo's own time zone, in Alachua County's (America/
     New_York) and with no zone; and the world test's 3,500 photos, right species first, before and after, with no prior,
     with the time zone and with the time zone and three creatures met, at the shipped weight of the prior. The
     softmax over the rows is taken exactly, with the rows that have no home share summed once a photo and the home rows
     added for each beta.
  4. With --stage: the files the page downloads that change (the last part of the rows, the scale, the table with its
     "home" list, the place file), and parts.json with every length and SHA-256, for the rule --rule names.

Usage: python3 -I tools/species/everyday_build.py --species S.csv --photos P.csv --photos-dir DIR --slot DIR
         --place DIR --vectors PREFIX --out DIR [--photo-vectors DIR] [--stage DIR] [--rule accepted|own] [--no-world]
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
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "tools", "world"))
sys.path.insert(0, os.path.join(ROOT, "tools", "lab"))
import place  # noqa: E402
import prior  # noqa: E402
from pack import quantize  # noqa: E402

BETAS = (0.0, 0.1, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0)
BUILD34_BETA = 30.0
WORLD_MARK = 1.0                       # points: no world-test score may drop by more
RULES = ("own", "accepted")
ALACHUA_ZONE = "America/New_York"
GBIF = "https://api.gbif.org/v1/"
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


def plain(s):
    return " ".join((s or "").lower().replace("-", " ").split())


class Slot:
    """Rows (float, scaled to unit length), table and place of a world slot, with the page's fusion settings and its
    kinds head. `base` is a float matrix of the first rows shared between slots; `extra` the rows after them."""

    def __init__(self, base, extra, rows, place_raw, zones, man, kinds_rows, home=None):
        self.base, self.extra, self.rows, self.man = base, extra, rows, man
        self.f = man["fusion"]
        self.labels = man["kinds"]["labels"]
        self.K = kinds_rows
        S = len(rows)
        g = place.Grid(place_raw["res"])
        R = place.Records(g, place_raw["cells"], place_raw["rows"], place_raw["counts"], S)
        zs = {k: (np.asarray(v[0], np.int64), np.asarray(v[1], np.float64)) for k, v in zones["zones"].items()}
        self.place = place.Place(R, zones=zs, alias=zones.get("alias", {}), radius_km=man["place"]["radius_km"], eps=man["place"]["eps"])
        lab_ix = {k: i for i, k in enumerate(self.labels)}
        self.other = lab_ix["other"]
        self.kind_ix = np.array([lab_ix.get(r[2], self.other) for r in rows], np.int64)   # knownKind: a group with no view is other
        self.has = np.zeros(len(self.labels), bool)
        self.has[np.unique(self.kind_ix)] = True
        self.home = np.zeros(S) if home is None else np.asarray(home, np.float64)
        self.H = np.nonzero(self.home > 0)[0]
        self.hH = self.home[self.H]
        self.OH = np.zeros((S, len(self.labels)), np.float32)        # one-hot kinds of the rows without a home share
        self.OH[np.arange(S), self.kind_ix] = 1.0
        self.OH[self.H] = 0.0
        self.OHH = np.zeros((len(self.H), len(self.labels)), np.float64)
        self.OHH[np.arange(len(self.H)), self.kind_ix[self.H]] = 1.0
        self.noname = np.isin(np.array(self.labels), ["none", "person"])
        self._share = {}

    def logshare0(self, zone, met=()):
        """log share(s) for every row with no home share added, where the phone probably is; the encounter rule skips a
        met row that has a home share, as the page does."""
        met = tuple(x for x in met if not self.home[x] > 0)
        key = (zone, met)
        if key not in self._share:
            if len(self._share) > 400:
                self._share = {}
            self.place.home = None
            self._share[key] = self.place.log_share(self.place.posterior(zone, met)).astype(np.float32)
        return self._share[key]

    def dots(self, X, base_dots=None):
        bd = base_dots if base_dots is not None else dot_rows(X, self.base)
        if self.extra is None or not len(self.extra):
            return bd
        return np.concatenate([bd, X @ self.extra.T], axis=1)

    def split(self, sd, L0):
        """The rows without a home share, once: their best row and value, and the sum of exp(z - best) for each kind."""
        f = self.f
        Z = f["t_species"] * sd
        if L0 is not None:
            Z += f["alpha_prior"] * L0
        if len(self.H):
            Z[:, self.H] = -np.inf
        bi = Z.argmax(1)
        bv = Z[np.arange(len(bi)), bi].astype(np.float64)
        Z -= bv[:, None].astype(np.float32)
        np.exp(Z, out=Z)
        ks = (Z @ self.OH).astype(np.float64)
        zH = (f["t_species"] * sd[:, self.H]).astype(np.float64) if len(self.H) else None
        sH = np.exp(L0[:, self.H].astype(np.float64)) if (L0 is not None and len(self.H)) else None
        return bi, bv, ks, zH, sH

    def at(self, parts, beta, with_prior=True):
        """The top row, its probability and the species' mass of each kind, at this beta."""
        bi, bv, ks, zH, sH = parts
        f = self.f
        if zH is None:
            M = bv
            tot = ks
            top, tv = bi, bv
        else:
            zh = zH + (f["alpha_prior"] * np.log(sH + beta * self.hH[None, :]) if with_prior else 0.0)
            hm = zh.max(1)
            M = np.maximum(bv, hm)
            tot = ks * np.exp(bv - M)[:, None] + np.exp(zh - M[:, None]) @ self.OHH
            hj = zh.argmax(1)
            take = hm > bv
            top = np.where(take, self.H[hj], bi)
            tv = np.where(take, hm, bv)
        Zs = tot.sum(1)
        return top, np.exp(tv - M) / Zs, tot / Zs[:, None]

    def kinds(self, X, q, top, tp):
        """fuseWith's kind for a slot with a kinds head: the kind, its probability, sure, named."""
        f = self.f
        p = softmax(f["t_kind"] * (X @ self.K.T).astype(np.float64))
        A = (p * self.has[None, :]).sum(1, keepdims=True)
        comb = np.where(self.has[None, :], f["w_kind"] * p + (1 - f["w_kind"]) * A * q, p)
        comb = comb / comb.sum(1, keepdims=True)
        kind = comb.argmax(1)
        kp = comb[np.arange(len(kind)), kind]
        sure = kp >= f["kind_at"] if f.get("kind_at") is not None else np.ones(len(kind), bool)
        named = sure & (tp >= f["name_at"]) & (self.kind_ix[top] == kind) & ~self.noname[kind]
        return kind, kp, sure, named


def dot_rows(X, Qf, chunk=65536):
    out = np.empty((X.shape[0], Qf.shape[0]), np.float32)
    for i in range(0, Qf.shape[0], chunk):
        out[:, i:i + chunk] = X @ Qf[i:i + chunk].T
    return out


def read_slot(d, man):
    names = sorted(x for x in os.listdir(d) if x.startswith("rows.i8.part"))
    raw = b"".join(open(os.path.join(d, p), "rb").read() for p in names)
    Q = np.frombuffer(raw, np.int8).reshape(-1, man["width"])
    sc = np.fromfile(os.path.join(d, "scale.f32"), "<f4")
    table = json.load(open(os.path.join(d, "table.json"), encoding="utf-8"))
    pr = prior.read_place(os.path.join(d, "place.bin"))
    zones = json.load(open(os.path.join(d, "zones.json")))
    assert len(Q) == len(sc) == len(table["species"]) == pr["S"], "the slot's files disagree on the number of rows"
    return Q, sc, table, pr, zones


def write_place(src, dst, n_new):
    """The place file with n_new species that have no records added at the end (a varint 0 each)."""
    b = bytearray(open(src, "rb").read())
    ver, res, nr, nc, S, npairs, nbytes = struct.unpack("<IfIIIII", b[4:32])
    b[4:32] = struct.pack("<IfIIIII", ver, res, nr, nc, S + n_new, npairs, nbytes + n_new)
    b += bytes(n_new)
    open(dst, "wb").write(bytes(b))


def with_new_rows(pr, n_new):
    """The place records of a slot with n_new rows that have no records added at the end."""
    q = dict(pr)
    q["S"] = pr["S"] + n_new
    return q


def rate(mask):
    return float(mask.mean()) if len(mask) else float("nan")


def accepted_rows(sp, rows, by_key, by_sci, cache, english):
    """For each species GBIF lists as a synonym: the species GBIF accepts for it, and the world row of that species when
    the row carries the English name the species' own row would carry (english(s), never empty). GBIF's answers are kept
    in `cache` (read from and written to accepted.json)."""
    import everyday  # noqa: E402 - the HTTP helper of the resolve step
    out = {}
    for s in sp:
        if s["status"] != "SYNONYM" or not s.get("accepted_key"):
            continue
        k = str(int(s["accepted_key"]))
        if k not in cache:
            j = everyday.get(GBIF + "species/%s" % k)
            cache[k] = {x: j.get(x) for x in ("key", "canonicalName", "rank", "taxonomicStatus", "speciesKey", "species")}
        a = cache[k]
        r = None
        if a.get("speciesKey") is not None and int(a["speciesKey"]) in by_key:
            r = by_key[int(a["speciesKey"])]
        elif a.get("species") in by_sci:
            r = by_sci[a["species"]]
        en = english(s)
        same = r is not None and plain(en) != "" and plain(rows[r][1]) == plain(en)
        out[int(s["gbif_key"])] = {"sci": s["sci"], "en": en, "accepted": a.get("canonicalName"), "accepted_rank": a.get("rank"),
                                   "species": a.get("species"), "species_key": a.get("speciesKey"), "world_row": r,
                                   "world_row_name": rows[r][:2] if r is not None else None, "same_english": bool(same)}
    return out


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
    ap.add_argument("--rule", default="accepted", choices=RULES)
    ap.add_argument("--no-world", action="store_true")
    ap.add_argument("--embed-shard", default="", help="i/n: only the BioCLIP 2 vectors of this block of photos, to --out")
    ap.add_argument("--photo-vectors", default="", help="a directory of vec-*.f16.npy and vec-*.ids.json from --embed-shard, "
                    "or of photos.f16.npy and photos.ids.json from an earlier build")
    ap.add_argument("--accepted", default=os.path.join(ROOT, "data", "everyday", "accepted.json"),
                    help="GBIF's accepted names for the synonyms, read if present and written to --out")
    ap.add_argument("--manifest", default=os.path.join(ROOT, "models", "naturalist", "manifest.json"))
    ap.add_argument("--batch", type=int, default=100)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    if a.embed_shard:
        import lab  # noqa: E402
        ph = lab.shard_rows(list(csv.DictReader(open(a.photos, encoding="utf-8"))), a.embed_shard, "block")
        m = lab.load(lab.model_entry("bioclip2-l14"))
        ids, X, bad, el = lab.embed_rows(m, ph, a.photos_dir)
        tag = a.embed_shard.replace("/", "of")
        np.save(os.path.join(a.out, "vec-%s.f16.npy" % tag), X.astype(np.float16))
        json.dump({"ids": ids, "bad": bad, "seconds": el}, open(os.path.join(a.out, "vec-%s.ids.json" % tag), "w"))
        log("shard %s: %d embedded, %d missing or unreadable, %.0fs" % (a.embed_shard, len(ids), len(bad), el))
        return
    man = json.load(open(a.manifest))
    Q, sc, table, pr, zones = read_slot(a.slot, man)
    rows, keys = table["species"], table["keys"]
    assert "home" not in table, "the slot must be the world slot from before the species people keep"
    S0 = len(rows)
    log("slot: %d rows, width %d" % Q.shape)
    K = np.frombuffer(open(os.path.join(os.path.dirname(a.manifest), man["kinds"]["url"]), "rb").read(), np.float16)
    K = K.reshape(len(man["kinds"]["labels"]), man["width"]).astype(np.float32)

    # 1. which species have a row already, which need one, under each rule
    sp = list(csv.DictReader(open(a.species, encoding="utf-8")))
    summ = json.load(open(os.path.join(os.path.dirname(a.species), "summary.json")))
    by_key = {}
    for i, k in enumerate(keys):
        if k:
            by_key.setdefault(int(k), i)
    by_sci = {}
    for i, r in enumerate(rows):
        by_sci.setdefault(r[0], i)
    def english(s):                  # iNaturalist's English name, where its taxon is this name or holds it as a synonym
        X = chr(0xd7)
        own = (s.get("inat_name") or "").replace(X + " ", "").replace(X, "") in (s.get("query"), s["sci"])
        return s["en"] if (own or s.get("inat_via") == "synonym") else ""

    cache = json.load(open(a.accepted)) if os.path.exists(a.accepted) else {}
    acc = accepted_rows(sp, rows, by_key, by_sci, cache, english)
    json.dump(cache, open(os.path.join(a.out, "accepted.json"), "w"), indent=1, sort_keys=True)
    for k, v in acc.items():
        log("synonym %s (%s): GBIF accepts %s (%s), species %s, world row %s %s%s" % (
            v["sci"], v["en"], v["accepted"], v["accepted_rank"], v["species"], v["world_row"], v["world_row_name"],
            ", same English name: takes that row under the rule accepted" if v["same_english"] else ""))

    plan = {}
    for rule in RULES:
        row, frm, new = {}, {}, []
        for s in sp:
            k = int(s["gbif_key"])
            if k in by_key:
                row[k], frm[k] = by_key[k], "key"
            elif s["sci"] in by_sci:
                row[k], frm[k] = by_sci[s["sci"]], "name"
            elif rule == "accepted" and k in acc and acc[k]["same_english"]:
                row[k], frm[k] = acc[k]["world_row"], "accepted"
            else:
                row[k], frm[k] = S0 + len(new), "new"
                new.append(s)
        plan[rule] = {"row": row, "from": frm, "new": new}
        log("rule %s: species %d, %d have a row (%d by key, %d by name, %d by GBIF's accepted name), %d new" % (
            rule, len(sp), len(sp) - len(new), sum(v == "key" for v in frm.values()), sum(v == "name" for v in frm.values()),
            sum(v == "accepted" for v in frm.values()), len(new)))

    import lab  # noqa: E402 - torch and open_clip are needed from here on
    m = lab.load(lab.model_entry("bioclip2-l14"))

    def text_rows(names):
        out = []
        for j in range(0, len(names), 64):
            nj = [lab.bioclip_scientific({"sci": x}) for x in names[j:j + 64]]
            out.append(lab.unit(lab.unit(np.asarray(m.encode_text(["a photo of {}.".format(x) for x in nj]), np.float32))))
        return np.concatenate(out) if out else np.zeros((0, man["width"]), np.float32)

    # the route agrees with the shipped rows: three rows made again
    chk = [0, S0 // 2, S0 - 1]
    again = text_rows([rows[i][0] for i in chk])
    shipped = Q[chk].astype(np.float32) * sc[chk][:, None]
    agree = [float(x) for x in (again * shipped).sum(1)]
    log("the route made three shipped rows again, cosine %s" % agree)
    allnew = plan["own"]["new"]                                   # every rule's new rows are among these
    vq, vs = quantize(text_rows([s["sci"] for s in allnew]))
    at_new = {int(s["gbif_key"]): i for i, s in enumerate(allnew)}
    total = float(summ["inat_observations_all"])
    Qbase = Q.astype(np.float32)
    Qbase *= sc[:, None]
    for rule in RULES:
        P = plan[rule]
        ix = [at_new[int(s["gbif_key"])] for s in P["new"]]
        P["qn"], P["sn"] = vq[ix], vs[ix]
        P["extra"] = P["qn"].astype(np.float32) * P["sn"][:, None]
        P["rows_x"] = rows + [[s["sci"], english(s), s["kind"]] for s in P["new"]]
        P["keys_x"] = list(keys) + [int(s["gbif_key"]) for s in P["new"]]
        h = np.zeros(len(P["rows_x"]), np.float64)
        for s in sp:
            r = P["row"][int(s["gbif_key"])]
            h[r] = max(h[r], float(s["captive_obs"] or 0) / total)
        P["h"] = h
        for s in P["new"]:
            log("  rule %s, new row %d: %s (%s) kind %s" % (rule, P["row"][int(s["gbif_key"])], s["sci"], english(s), s["kind"]))

    # 2. the photos' vectors
    ph = list(csv.DictReader(open(a.photos, encoding="utf-8")))
    if a.photo_vectors and os.path.exists(os.path.join(a.photo_vectors, "photos.ids.json")):
        ids = json.load(open(os.path.join(a.photo_vectors, "photos.ids.json")))
        X = np.load(os.path.join(a.photo_vectors, "photos.f16.npy")).astype(np.float32)
        bad, el = [r["id"] for r in ph if r["id"] not in set(ids)], 0.0
    elif a.photo_vectors:
        import glob
        ids, Xs, bad, el = [], [], [], 0.0
        for f in sorted(glob.glob(os.path.join(a.photo_vectors, "**", "vec-*.ids.json"), recursive=True)):
            j = json.load(open(f))
            ids += j["ids"]
            bad += j["bad"]
            el += j["seconds"]
            Xs.append(np.load(f.replace(".ids.json", ".f16.npy")).astype(np.float32))
        X = np.concatenate(Xs)
    else:
        ids, X, bad, el = lab.embed_rows(m, ph, a.photos_dir)
    log("photos: %d embedded, %d missing or unreadable, %.0fs" % (len(ids), len(bad), el))
    np.save(os.path.join(a.out, "photos.f16.npy"), X.astype(np.float16))
    json.dump(ids, open(os.path.join(a.out, "photos.ids.json"), "w"))
    pos = {x: i for i, x in enumerate(ids)}
    ph = [r for r in ph if r["id"] in pos]
    X = X[[pos[r["id"]] for r in ph]].astype(np.float32)

    slots = {}
    for rule in RULES:
        P = plan[rule]
        slots[rule] = Slot(Qbase, P["extra"], P["rows_x"], with_new_rows(pr, len(P["new"])), zones, man, K, home=P["h"])
        P["truth"] = np.array([P["row"][int(r["gbif_key"])] for r in ph], np.int64)
        P["tkind"] = slots[rule].kind_ix[P["truth"]]
    zone_of = [r["zone"] if slots["own"].place.zone_name(r["zone"]) else "" for r in ph]
    conds = {"own": zone_of, "alachua": [ALACHUA_ZONE] * len(ph), "nozone": [""] * len(ph)}

    def measure(idx, betas):
        """Every rule, condition and beta on the photos idx: per photo the top row, the kind, sure and named."""
        acc_ = {(rule, b, c): [[] for _ in range(6)] for rule in RULES for b in betas for c in conds}
        for b0 in range(0, len(idx), a.batch):
            bi = idx[b0:b0 + a.batch]
            Xb = X[bi]
            based = dot_rows(Xb, Qbase)
            for rule in RULES:
                sl = slots[rule]
                sd = sl.dots(Xb, based)
                for c, zl in conds.items():
                    L0 = np.stack([sl.logshare0(zl[i]) for i in bi])
                    parts = sl.split(sd, L0)
                    for b in betas:
                        top, tp, q = sl.at(parts, b)
                        kind, kp, sure, named = sl.kinds(Xb, q, top, tp)
                        for L, v in zip(acc_[(rule, b, c)], (top, tp, kind, kp, sure, named)):
                            L.append(v)
            log("  photos %d/%d" % (min(len(idx), b0 + a.batch), len(idx)))
        res = {}
        for (rule, b, c), v in acc_.items():
            top, tp, kind, kp, sure, named = (np.concatenate(x) for x in v)
            t, tk = plan[rule]["truth"][idx], plan[rule]["tkind"][idx]
            res.setdefault(rule, {}).setdefault(b, {})[c] = {
                "photos": int(len(idx)), "kind_right": rate(kind == tk), "kind_sure": rate(sure),
                "kind_right_when_sure": rate((kind == tk)[sure]), "species_right": rate(top == t), "named": rate(named),
                "named_right": rate((top == t)[named]), "_top": top, "_tp": tp, "_kind": kind, "_named": named}
        return res

    def strip(x):
        return {c: {k: v for k, v in y.items() if not k.startswith("_")} for c, y in x.items()}

    tune_ix = np.array([i for i, r in enumerate(ph) if r["set"] == "tune"], np.int64)
    test_ix = np.array([i for i, r in enumerate(ph) if r["set"] == "test"], np.int64)
    allr = measure(tune_ix, BETAS)
    tune = {rule: {b: strip(allr[rule][b]) for b in BETAS} for rule in RULES}
    for rule in RULES:
        for b in BETAS:
            r = tune[rule][b]
            log("tune %-8s beta %-5g own: kind %.3f species %.3f | alachua: kind %.3f species %.3f" % (
                rule, b, r["own"]["kind_right"], r["own"]["species_right"], r["alachua"]["kind_right"], r["alachua"]["species_right"]))

    # 3. the world test, before and after, at the shipped weight of the prior, for every rule and beta
    world, drops = None, {}
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
        old = Slot(Qbase, None, rows, pr, zones, man, K)
        CW = ("none", "zone", "zone+3")
        tops = {("before", None, c): [] for c in CW}
        for rule in RULES:
            tops[(rule, None, "none")] = []
            for b in BETAS:
                for c in CW[1:]:
                    tops[(rule, b, c)] = []
        for b0 in range(0, len(wt), 125):
            bi = list(range(b0, min(len(wt), b0 + 125)))
            based = dot_rows(XW[b0:b0 + 125], Qbase)
            sds = {rule: slots[rule].dots(XW[b0:b0 + 125], based) for rule in RULES}
            for c in CW:
                mets = [tuple(met.get(wt[i]["id"], [])[:3]) if c == "zone+3" else () for i in bi]
                Z = old.f["t_species"] * based
                if c != "none":
                    Z = Z + old.f["alpha_prior"] * np.stack([old.logshare0(wt[i]["zone"], m3) for i, m3 in zip(bi, mets)])
                tops[("before", None, c)].append(Z.argmax(1))
                for rule in RULES:
                    sl, sd = slots[rule], sds[rule]
                    if c == "none":
                        tops[(rule, None, c)].append((sl.f["t_species"] * sd).argmax(1))
                        continue
                    L0 = np.stack([sl.logshare0(wt[i]["zone"], m3) for i, m3 in zip(bi, mets)])
                    parts = sl.split(sd, L0)
                    for b in BETAS:
                        tops[(rule, b, c)].append(sl.at(parts, b)[0])
            log("world test %d/%d" % (min(len(wt), b0 + 125), len(wt)))
        world = {"photos": len(wt), "before": {}}
        for (rule, b, c), v in tops.items():
            top = np.concatenate(v)
            home_rows = np.nonzero(slots[rule].home > 0)[0] if rule != "before" else np.zeros(0, np.int64)
            x = {"top1": rate((top == wtruth) & (wtruth >= 0)), "taken_by_a_home_row": int(np.isin(top, home_rows).sum())}
            if rule == "before":
                world["before"][c] = x
            elif b is None:
                world.setdefault(rule, {})["none"] = x
            else:
                world.setdefault(rule, {}).setdefault(str(b), {})[c] = x
        for rule in RULES:
            for b in BETAS:
                d = {"none": round(100 * (world["before"]["none"]["top1"] - world[rule]["none"]["top1"]), 2)}
                for c in CW[1:]:
                    d[c] = round(100 * (world["before"][c]["top1"] - world[rule][str(b)][c]["top1"]), 2)
                drops.setdefault(rule, {})[b] = d
                log("world test %-8s beta %-5g drop (points): %s, home rows took %d and %d" % (
                    rule, b, d, world[rule][str(b)]["zone"]["taken_by_a_home_row"], world[rule][str(b)]["zone+3"]["taken_by_a_home_row"]))
        log("world test before: %s" % json.dumps(world["before"]))

    # beta: the best on the tune photos among those the world test allows
    def allowed(rule, b):
        return not drops or all(v <= WORLD_MARK for v in drops[rule][b].values())
    best = {rule: max([b for b in BETAS if allowed(rule, b)] or [0.0], key=lambda b: (round(tune[rule][b]["own"]["species_right"], 6), -b)) for rule in RULES}
    log("beta chosen on the tune photos, within the world test's mark: %s" % best)

    tb = measure(test_ix, sorted(set(best.values()) | {0.0, BUILD34_BETA}))
    out = {"species": len(sp), "rule": a.rule, "rules": {}, "route_check_cosine": agree, "synonyms": {str(k): v for k, v in acc.items()},
           "photos": {"tune": int(len(tune_ix)), "test": int(len(test_ix)), "missing": len(bad)},
           "home_denominator": total, "betas": list(BETAS), "tune": {r: {str(b): x for b, x in tune[r].items()} for r in RULES}}
    for rule in RULES:
        b = best[rule]
        P = plan[rule]
        t = P["truth"]
        rr = {"rows_new": len(P["new"]), "rows_kept": len(sp) - len(P["new"]), "beta": b,
              "test": strip(tb[rule][b]), "test_beta0": strip(tb[rule][0.0]), "test_beta30": strip(tb[rule][BUILD34_BETA]),
              "marks": {c: {"kind_right>=0.85": tb[rule][b][c]["kind_right"] >= 0.85, "species_right>=0.60": tb[rule][b][c]["species_right"] >= 0.60}
                        for c in ("own", "alachua")}}
        if drops:
            rr["world_drop_points"] = drops[rule][b]
            rr["world_drop_points_by_beta"] = {str(x): drops[rule][x] for x in BETAS}
            rr["marks"]["world_test_no_drop_over_1_point"] = allowed(rule, b)
        per = {}
        for bb in sorted({b, BUILD34_BETA}):
            T = tb[rule][bb]["own"]
            for j, i in enumerate(test_ix):
                k = int(ph[i]["gbif_key"])
                d = per.setdefault(str(bb), {}).setdefault(k, {"sci": ph[i]["sci"], "kind": ph[i]["kind"], "row": int(t[i]), "n": 0, "kind_right": 0,
                                                                "species_right": 0, "named": 0, "said": {}, "kinds_said": {}})
                d["n"] += 1
                d["kind_right"] += int(T["_kind"][j] == P["tkind"][i])
                d["species_right"] += int(T["_top"][j] == t[i])
                d["named"] += int(T["_named"][j])
                said = P["rows_x"][int(T["_top"][j])][0]
                d["said"][said] = d["said"].get(said, 0) + 1
                kn = slots[rule].labels[int(T["_kind"][j])]
                d["kinds_said"][kn] = d["kinds_said"].get(kn, 0) + 1
            for d in per[str(bb)].values():
                d["said"] = sorted(d["said"].items(), key=lambda x: -x[1])[:3]
        rr["by_species"] = per
        out["rules"][rule] = rr
        log("rule %s at beta %g, test: %s" % (rule, b, json.dumps({c: {k: round(v, 4) for k, v in x.items()} for c, x in rr["test"].items()})))
        log("rule %s marks: %s" % (rule, json.dumps(rr["marks"])))
        dog = per[str(b)].get(5219200)
        if dog:
            log("rule %s, the dog at beta %g: kind right %d of %d, species right %d, named %d, said %s, kinds %s" % (
                rule, b, dog["kind_right"], dog["n"], dog["species_right"], dog["named"], dog["said"], dog["kinds_said"]))
    if world:
        out["world_test"] = world
    chosen = out["rules"][a.rule]
    out["beta"], out["test"], out["marks"] = chosen["beta"], chosen["test"], chosen["marks"]
    out["rows_new"] = chosen["rows_new"]
    if drops:
        out["world_drop_points"] = chosen["world_drop_points"]

    # 4. the files that change, for the page
    if a.stage:
        P, b = plan[a.rule], best[a.rule]
        os.makedirs(a.stage, exist_ok=True)
        names = sorted(x for x in os.listdir(a.slot) if x.startswith("rows.i8.part"))
        last = names[-1]
        with open(os.path.join(a.stage, last), "wb") as f:
            f.write(open(os.path.join(a.slot, last), "rb").read())
            f.write(P["qn"].tobytes())
        scx = np.concatenate([sc, P["sn"]])
        scx.astype("<f4").tofile(os.path.join(a.stage, "scale.f32"))
        tx = dict(table)
        tx["species"], tx["keys"] = P["rows_x"], P["keys_x"]
        tx["home"] = [[int(r), float("%.6g" % (b * v))] for r, v in enumerate(P["h"]) if v > 0]
        tx["home_from"] = ("tools/species/everyday_build.py, rule %s: beta %g times the species' iNaturalist observations marked "
                           "captive or cultivated over all iNaturalist observations (%d), added to its share in every cell" % (a.rule, b, total))
        json.dump(tx, open(os.path.join(a.stage, "table.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
        write_place(os.path.join(a.slot, "place.bin"), os.path.join(a.stage, "place.bin"), len(P["new"]))
        whole = hashlib.sha256()
        for p in names[:-1]:
            whole.update(open(os.path.join(a.slot, p), "rb").read())
        whole.update(open(os.path.join(a.stage, last), "rb").read())

        def one(n):
            p = os.path.join(a.stage, n)
            return {"name": n, "bytes": os.path.getsize(p), "sha256": sha(p)}
        pj = {"count": len(P["rows_x"]), "width": man["width"], "rows_bytes": int((len(Q) + len(P["new"])) * man["width"]),
              "rows_sha256": whole.hexdigest(), "last_part": one(last), "scale": one("scale.f32"), "table": one("table.json"),
              "place": one("place.bin"), "beta": b, "rule": a.rule, "new_rows": len(P["new"])}
        json.dump(pj, open(os.path.join(a.stage, "parts.json"), "w"), indent=1)
        out["stage"] = pj
        log("stage: %s" % json.dumps(pj))
        pr2 = prior.read_place(os.path.join(a.stage, "place.bin"))              # the extended slot read back as the page reads it
        assert pr2["S"] == len(P["rows_x"]) and len(pr2["rows"]) == len(pr["rows"])
    json.dump(out, open(os.path.join(a.out, "everyday.json"), "w"), indent=1, default=float)
    log("marks (rule %s): %s" % (a.rule, json.dumps(out["marks"])))


if __name__ == "__main__":
    main()
