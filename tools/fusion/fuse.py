#!/usr/bin/env python3
"""The recognizer's scoring, in plain numpy: from scores to a kind of eye, a name and offers.

This is the reference for what the page computes in `pocket.fuse` (src/cam.rec.js). Import it to report numbers "as shipped".

    from fuse import fuse, dots, load_slot
    slot = load_slot("models/pocket")            # a slot directory, or the path of a manifest inside one
                                                 # -> {"manifest", "table", "kinds", "species", "kind_bias", "species_bias"}; arrays are float64
    out = fuse(slot["manifest"], slot["table"], month, dots(slot["kinds"], e), dots(slot["species"], e),
               kind_bias=slot["kind_bias"], species_bias=slot["species_bias"])

Inputs
  manifest      the slot's manifest.json as a dict (uses manifest["kinds"]["labels"] and manifest["fusion"])
  table         the species table rows, [scientific, English, kind, twelve monthly weights or None] (or dicts with sci, en, kind|eyes, m); None if no species
  month         0 for January ... 11 for December; None when no month is known, and then the prior is left out
  kind_dots     row . e for each kind row, e being the unit image vector (use dots(rows, e))
  species_dots  the same for each species row, or None
  kind_bias, species_bias   a trained head's biases, or None. The score of a row is t * (row . e) + bias.
Output, the same fields as the page's result
  {"kind", "kindP", "sure", "kinds": [{"key", "p", "head", "list"}] best first, "kindOffers": [keys], "species": top five [{"sci", "en", "p", "kind"}],
   "named": row or None, "offers": [rows]}
  "sure" is False when the manifest sets fusion.kind_at and the winning kind's probability is under it. Then the page asserts no kind
  and changes no eyes: "named" is None, and "kindOffers" holds the three likeliest kinds other than "none", best first (the buttons
  the page shows). When "sure" is True, "kindOffers" is empty. Without fusion.kind_at every answer is sure, as before build 8.

A slot without a kinds head (no manifest["kinds"]: the larger model on the device): pass kind_dots=None. The labels are then the kinds
the species table has, in the order of KINDS, and a kind's probability is its share of the species answer ("head" is None).

Settings read from manifest["fusion"]: t_kind, and with species t_species, alpha_prior, w_kind, name_at, offer_at;
optional prior_floor (1e-6), offer_any_kind (false), rule ("product", the default, or "mix"), guard (1e-9, product rule only),
kind_at (absent or null: every answer is sure). Without a kinds head t_kind, w_kind, rule and guard are not read.
The two rules are described in README.md. Ties are broken by order: the earlier label, the earlier species row.
A label may stand on more than one row of the kinds head. Those rows are one kind: their probabilities are added in row
order, and the kind takes the place of the label's first row (tools/world/head.py --recipe merge keeps the row of a
group it cannot name well and labels it `other`). The page must do the same before such a slot ships.
The page (build 8 on; build 7 lacks kind_at and slots without a kinds head) computes the same thing in fuseWith, src/cam.rec.js; parity.py holds the two to the same answers.
A rule the page does not know is refused by both: the page will not load such a slot, and fuse() raises ValueError.
"""
import json, math, pathlib
import numpy as np

KINDS = ("cat", "dog", "squirrel", "deer", "rabbit", "hawk", "wader", "bird", "alligator", "reptile", "frog", "bee", "insect", "plant", "other", "person",
         # the groups with no view yet (GROUPS in src/cam.a.js), which a species table or a kinds head may carry since build 22
         "fungus", "slime", "spider", "jumper", "fish", "shark", "snail", "sealife", "crab", "salamander", "worm", "scorpion", "tick",
         "mammal", "primate", "whale", "bat", "flyingfox", "cephalopod")


def total(x):
    """The sum taken left to right, one term after the next, as the page's loops take it (numpy's own sum pairs terms up,
    which rounds differently in the last place and can break an exact tie the other way)."""
    return float(np.cumsum(x)[-1]) if len(x) else 0.0


def softmax(z):
    z = np.asarray(z, dtype=np.float64)
    e = np.exp(z - z.max())
    return e / total(e)


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


_KEPT = {}


def prepared(table):
    """The table as the page reads it, worked out once for each table object (thousands of photos are scored against one table)."""
    hit = _KEPT.get(id(table))
    if hit is None or hit["table"] is not table:
        rows = clean_table(table)
        names = sorted({r["kind"] for r in rows}, key=KINDS.index)
        hit = {"table": table, "rows": rows, "kinds": names, "index": np.array([names.index(r["kind"]) for r in rows], dtype=np.int64), "prior": {}}
        if len(_KEPT) > 8: _KEPT.clear()
        _KEPT[id(table)] = hit
    return hit


def prior_log(rows, month, floor):
    """log of each species' share of this month's records, floored; all zero when the month has no records at all, or no month is known."""
    if month is None or not (0 <= month < 12) or int(month) != month:
        return np.zeros(len(rows))
    month = int(month)
    w = np.array([max(0.0, float(r["m"][month] or 0)) if r["m"] else 0.0 for r in rows])
    whole = total(w)
    if not whole > 0:
        return np.zeros(len(rows))
    with np.errstate(divide="ignore"):                                  # a floor of zero makes an unrecorded species impossible: log 0
        return np.log(np.maximum(w / whole, floor))


def fuse(manifest, table, month, kind_dots, species_dots=None, kind_bias=None, species_bias=None):
    f = manifest["fusion"]
    rule = f.get("rule", "product")
    if rule not in ("product", "mix"):
        raise ValueError("a combination rule this reference does not know: %r" % (rule,))
    head = manifest.get("kinds") is not None                            # a slot may come without a kinds head
    T = prepared(table) if table is not None and species_dots is not None else None
    if not head and T is None:
        raise ValueError("a slot without a kinds head needs its species table and their scores")
    labels = list(manifest["kinds"]["labels"]) if head else list(T["kinds"])
    p = None
    if head:
        z = f["t_kind"] * np.asarray(kind_dots, dtype=np.float64)
        if kind_bias is not None:
            z = z + np.asarray(kind_bias, dtype=np.float64)
        p = softmax(z)
        uniq = list(dict.fromkeys(labels))
        if len(uniq) < len(labels):
            # rows that share a label are one kind (a group whose row is kept but not named is labelled `other`):
            # their probabilities are added, in row order, and the kind takes the place of the label's first row
            pu = np.zeros(len(uniq))
            for i, lab in enumerate(labels):
                pu[uniq.index(lab)] += float(p[i])
            p, labels = pu, uniq
    n = len(labels)
    rows = T["rows"] if T else None
    s, q, order, species, has = None, {}, [], [], set()
    if rows is not None:
        zs = f["t_species"] * np.asarray(species_dots, dtype=np.float64)
        if species_bias is not None:
            zs = zs + np.asarray(species_bias, dtype=np.float64)
        if f["alpha_prior"]:                                             # a weight of zero leaves the prior out altogether
            floor = f.get("prior_floor", 1e-6)
            key = (month, floor)
            if key not in T["prior"]:
                T["prior"][key] = prior_log(rows, month, floor)
            zs = zs + f["alpha_prior"] * T["prior"][key]
        s = softmax(zs)
        sums = np.bincount(T["index"], weights=s, minlength=len(T["kinds"]))   # each kind's share, its species added in row order
        q = {k: float(sums[i]) for i, k in enumerate(T["kinds"])}
        has = set(T["kinds"])
        order = np.argsort(-s, kind="stable").tolist()                     # stable: equal scores keep row order
        species = [{"sci": rows[j]["sci"], "en": rows[j]["en"], "p": float(s[j]), "kind": rows[j]["kind"]} for j in order[:5]]
    speaks = [s is not None and labels[i] in has for i in range(n)]     # can the species list speak for this kind?
    if not head:
        c = np.array([q.get(labels[i], 0.0) for i in range(n)], dtype=np.float64)   # each kind's share of the species answer
    elif rule == "mix":
        # the species head only re-divides the share the kinds head gave to the kinds it can speak for
        a = 0.0
        for i in range(n):
            if speaks[i]: a += float(p[i])
        c = np.array([f["w_kind"] * float(p[i]) + (1 - f["w_kind"]) * a * q.get(labels[i], 0.0) if speaks[i] else float(p[i]) for i in range(n)], dtype=np.float64)
        whole = total(c)
        c = c / whole if whole > 0 else p.copy()                        # all of it given to kinds outside the labels: the kinds alone
    else:
        g = f.get("guard", 1e-9)
        score = np.array([f["w_kind"] * math.log(max(float(p[i]), g)) + (1 - f["w_kind"]) * math.log(max(q.get(labels[i], 0.0), g)) if speaks[i] else math.log(max(float(p[i]), g)) for i in range(n)])
        c = softmax(score)
    kinds = [{"key": labels[i], "p": float(c[i]), "head": (float(p[i]) if head else None), "list": (q.get(labels[i], 0.0) if speaks[i] else None)} for i in range(n)]
    kinds.sort(key=lambda k: -k["p"])                                   # stable: equal scores keep label order
    kind, named, offers = kinds[0]["key"], None, []
    # not sure is an answer: under kind_at no kind is asserted and no species named, and the three likeliest kinds are offered
    kind_at = f.get("kind_at")
    sure = not (kind_at is not None and kinds[0]["p"] < kind_at)
    kind_offers = [] if sure else [k["key"] for k in kinds if k["key"] != "none"][:3]
    if species and kind not in ("none", "person"):
        if sure and species[0]["p"] >= f["name_at"] and species[0]["kind"] == kind:
            named = species[0]
        else:
            pool = order if f.get("offer_any_kind") else [j for j in order if rows[j]["kind"] == kind]
            three = [{"sci": rows[j]["sci"], "en": rows[j]["en"], "p": float(s[j]), "kind": rows[j]["kind"]} for j in pool[:3]]
            if sum(t["p"] for t in three) >= f["offer_at"]:
                offers = three
    return {"kind": kind, "kindP": kinds[0]["p"], "sure": sure, "kinds": kinds, "kindOffers": kind_offers, "species": species, "named": named, "offers": offers}


def load_slot(where):
    """Read a slot as the page does: manifest, half-precision rows, optional biases, species table.
    `where` is the slot's directory (its manifest.json is read) or the path of a manifest file inside it."""
    d = pathlib.Path(where)
    mf = d if d.suffix == ".json" else d / "manifest.json"
    d = mf.parent
    m = json.loads(mf.read_text(encoding="utf-8"))
    w = m["width"]
    out = {"manifest": m, "table": None, "kinds": None, "species": None, "kind_bias": None, "species_bias": None}
    if m.get("kinds"):                                                  # a slot without a kinds head has none of these
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
