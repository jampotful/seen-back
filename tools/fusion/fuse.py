#!/usr/bin/env python3
"""The recognizer's scoring, in plain numpy: from scores to a kind of eye, a name and offers.

This is the reference for what the page computes in `pocket.fuse` (src/cam.rec.js). Import it to report numbers "as shipped".

    from fuse import fuse, load_slot
    slot = load_slot("models/pocket")            # {"manifest", "table", "kinds", "species", "kind_bias", "species_bias"}; arrays are float64
    out = fuse(slot["manifest"], slot["table"], month, kind_dots, species_dots,
               kind_bias=slot["kind_bias"], species_bias=slot["species_bias"])

Inputs
  manifest      the slot's manifest.json as a dict (uses manifest["kinds"]["labels"] and manifest["fusion"])
  table         the species table rows, [scientific, English, kind, twelve monthly weights or None] (or dicts with sci, en, kind|eyes, m); None if no species
  month         0 for January ... 11 for December
  kind_dots     row . e for each kind row, e being the unit image vector (use dots(rows, e))
  species_dots  the same for each species row, or None
  kind_bias, species_bias   a trained head's biases, or None. The score of a row is t * (row . e) + bias.
Output, the same fields as the page's result
  {"kind", "kindP", "kinds": [{"key", "p", "head", "list"}] best first, "species": top five [{"sci", "en", "p", "kind"}], "named": row or None, "offers": [rows]}

Settings read from manifest["fusion"]: t_kind, and with species t_species, alpha_prior, w_kind, name_at, offer_at;
optional prior_floor (1e-6), offer_any_kind (false), rule ("product", the default, or "mix"), guard (1e-9, product rule only).
The two rules are described in README.md. Ties are broken by order: the earlier label, the earlier species row.
"""
import json, math, pathlib
import numpy as np

KINDS = ("cat", "dog", "squirrel", "deer", "rabbit", "hawk", "wader", "bird", "alligator", "reptile", "frog", "bee", "insect", "plant", "other", "person")


def softmax(z):
    z = np.asarray(z, dtype=np.float64)
    e = np.exp(z - z.max())
    return e / e.sum()


def dots(rows, e):
    """row . e for every row; e is made unit length first, as the page's worker does."""
    e = np.asarray(e, dtype=np.float64)
    n = math.sqrt(float(e @ e)) or 1.0
    return np.asarray(rows, dtype=np.float64) @ (e / n)


def clean_table(table):
    out = []
    for r in table:
        a = r if isinstance(r, (list, tuple)) else [r.get("sci"), r.get("en"), r.get("kind") or r.get("eyes"), r.get("m")]
        kind = a[2] if a[2] in KINDS else "other"
        m = a[3] if isinstance(a[3], (list, tuple)) and len(a[3]) == 12 else None
        out.append({"sci": a[0] or "", "en": a[1] or "", "kind": kind, "m": m})
    return out


def prior_log(rows, month, floor):
    """log of each species' share of this month's records, floored; all zero when the month has no records at all."""
    w = np.array([max(0.0, float(r["m"][month] or 0)) if r["m"] else 0.0 for r in rows])
    total = w.sum()
    if not total > 0:
        return np.zeros(len(rows))
    return np.log(np.maximum(w / total, floor))


def fuse(manifest, table, month, kind_dots, species_dots=None, kind_bias=None, species_bias=None):
    f = manifest["fusion"]
    labels = list(manifest["kinds"]["labels"])
    n = len(labels)
    z = f["t_kind"] * np.asarray(kind_dots, dtype=np.float64)
    if kind_bias is not None:
        z = z + np.asarray(kind_bias, dtype=np.float64)
    p = softmax(z)
    rows = clean_table(table) if table is not None and species_dots is not None else None
    s, q, order, species, has = None, {}, [], [], set()
    if rows is not None:
        zs = f["t_species"] * np.asarray(species_dots, dtype=np.float64)
        if species_bias is not None:
            zs = zs + np.asarray(species_bias, dtype=np.float64)
        zs = zs + f["alpha_prior"] * prior_log(rows, month, f.get("prior_floor", 1e-6))
        s = softmax(zs)
        for j, r in enumerate(rows):
            q[r["kind"]] = q.get(r["kind"], 0.0) + float(s[j])
            has.add(r["kind"])
        order = sorted(range(len(rows)), key=lambda j: -s[j])          # stable: equal scores keep row order
        species = [{"sci": rows[j]["sci"], "en": rows[j]["en"], "p": float(s[j]), "kind": rows[j]["kind"]} for j in order[:5]]
    speaks = [s is not None and labels[i] in has for i in range(n)]     # can the species list speak for this kind?
    if f.get("rule", "product") == "mix":
        # the species head only re-divides the share the kinds head gave to kinds it can speak for
        a = sum(float(p[i]) for i in range(n) if speaks[i])
        c = np.array([f["w_kind"] * p[i] + (1 - f["w_kind"]) * a * q.get(labels[i], 0.0) if speaks[i] else p[i] for i in range(n)], dtype=np.float64)
        c = c / c.sum()
    else:
        g = f.get("guard", 1e-9)
        score = np.array([f["w_kind"] * math.log(max(p[i], g)) + (1 - f["w_kind"]) * math.log(max(q.get(labels[i], 0.0), g)) if speaks[i] else math.log(max(p[i], g)) for i in range(n)])
        c = softmax(score)
    kinds = [{"key": labels[i], "p": float(c[i]), "head": float(p[i]), "list": (q.get(labels[i], 0.0) if speaks[i] else None)} for i in range(n)]
    kinds.sort(key=lambda k: -k["p"])                                   # stable: equal scores keep label order
    kind, named, offers = kinds[0]["key"], None, []
    if species and kind not in ("none", "person"):
        if species[0]["p"] >= f["name_at"] and species[0]["kind"] == kind:
            named = species[0]
        else:
            pool = order if f.get("offer_any_kind") else [j for j in order if rows[j]["kind"] == kind]
            three = [{"sci": rows[j]["sci"], "en": rows[j]["en"], "p": float(s[j]), "kind": rows[j]["kind"]} for j in pool[:3]]
            if sum(t["p"] for t in three) >= f["offer_at"]:
                offers = three
    return {"kind": kind, "kindP": kinds[0]["p"], "kinds": kinds, "species": species, "named": named, "offers": offers}


def load_slot(directory):
    """Read a slot directory as the page does: manifest, half-precision rows, optional biases, species table."""
    d = pathlib.Path(directory)
    m = json.loads((d / "manifest.json").read_text(encoding="utf-8"))
    w = m["width"]
    out = {"manifest": m, "table": None, "species": None, "kind_bias": None, "species_bias": None}
    out["kinds"] = np.fromfile(d / m["kinds"]["url"], dtype="<f2").astype(np.float64).reshape(-1, w)
    if m["kinds"].get("bias") is not None:
        out["kind_bias"] = np.asarray(m["kinds"]["bias"], dtype=np.float64)
    sp = m.get("species")
    if sp:
        out["species"] = np.fromfile(d / sp["url"], dtype="<f2").astype(np.float64).reshape(-1, w)
        t = json.loads((d / sp["table"]).read_text(encoding="utf-8"))
        out["table"] = t if isinstance(t, list) else t["species"]
        if sp.get("bias_url"):
            out["species_bias"] = np.fromfile(d / sp["bias_url"], dtype="<f4").astype(np.float64)
    return out


if __name__ == "__main__":
    # The cases of test/rec/check_rec.js "fuse", whose answers the page gave on 10 October 2026 (build 6, stand-in slot).
    here = pathlib.Path(__file__).resolve().parents[2] / "test" / "rec" / "models" / "standin"
    slot = load_slot(here)
    m, t = slot["manifest"], slot["table"]
    L = m["kinds"]["labels"]
    kd = lambda o: [o.get(k, 0) for k in L]
    sd = lambda o: [o.get(r[1], 0) for r in t]
    cases = [
        ("januaryAnole", fuse(m, t, 0, kd({"reptile": 1}), sd({"Brown Anole": .9, "Green Anole": .9})), ("reptile", 1.0, "Green Anole", 0.9947)),
        ("julyAnole", fuse(m, t, 6, kd({"reptile": 1}), sd({"Brown Anole": .9, "Green Anole": .9})), ("reptile", 1.0, "Brown Anole", 0.9946)),
        ("personNotOutvoted", fuse(m, t, 6, kd({"person": 1, "bird": .95}), sd({"Northern Cardinal": .9})), ("person", 0.9239, "Northern Cardinal", 0.5413)),
        ("noneNotOutvoted", fuse(m, t, 6, kd({"none": 1, "plant": .96}), sd({"Beggarticks": .9})), ("none", 0.8798, "Beggarticks", 1.0)),
        ("kindDisagrees", fuse(m, t, 6, kd({"plant": 1, "wader": .9}), sd({"Great Blue Heron": .9, "Beggarticks": .9 - math.log(.65 / .35) / m["fusion"]["t_species"]})), ("plant", 0.9909, "Great Blue Heron", 0.65)),
    ]
    bad = 0
    for name, r, (kind, kp, top, tp) in cases:
        ok = r["kind"] == kind and abs(r["kindP"] - kp) < 5e-5 and r["species"][0]["en"] == top and abs(r["species"][0]["p"] - tp) < 5e-5
        bad += not ok
        print("ok " if ok else "DIFFERS", name, r["kind"], round(r["kindP"], 4), r["species"][0]["en"], round(r["species"][0]["p"], 4), "| page:", kind, kp, top, tp)
    raise SystemExit(1 if bad else 0)
