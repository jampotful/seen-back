#!/usr/bin/env python3
"""Score an exported slot exactly as the page would, through tools/fusion/fuse.py, and set its two thresholds.

  python3 -I tools/eval/shipped.py <root> <slot dir> [--name pocket] [--out docs/eval/shipped-<name>.json] [--limit N]

1. Reads the slot as the page does (fuse.load_slot: half-precision rows, biases, the species table).
2. On the tuning photos, with naming switched off, records what fuse.py would name and offer. From those it sets
   name_at, the lowest level from which a named species was right at least nine times in ten, and offer_at, the lowest
   level from which the three offered species held the right one at least nine times in ten. Both go into manifest.json.
3. On the test photos, with the thresholds set, reports what the page would show and how often it is right.
The photos' vectors are the ones named in the manifest's "evaluation" block (for a pocket model, the WASM int8 vectors).
"""
import argparse, copy, hashlib, json, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "fusion"))
import ev
import fuse as F

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("slot")
ap.add_argument("--name")
ap.add_argument("--out")
ap.add_argument("--limit", type=int, default=0, help="score only the first N tuning and N test photos (for a quick try)")
a = ap.parse_args()
name = a.name or os.path.basename(os.path.normpath(a.slot))
slot = F.load_slot(a.slot)
man, table = slot["manifest"], slot["table"]
evn = man["evaluation"]
keys = json.load(open(os.path.join(a.slot, man["species"]["table"]), encoding="utf-8"))["keys"]
E, ids = ev.load_images(a.root, evn["model"], evn["test_vectors"].split("/", 1)[1])
ES = ev.EvalSet(a.root, ids)
k2row = {k: i for i, k in enumerate(keys)}
truth = np.array([k2row.get(int(r["key"]), -1) for r in ES.rows])
if evn["tuned_on"] == "val":
    tune = ES.val.copy()
else:
    h = np.array([int(hashlib.sha256(i.encode()).hexdigest()[:8], 16) % 3 for i in ids])
    tune = ES.val & (h == 2)
E64 = E.astype(np.float64)
E64 /= np.linalg.norm(E64, axis=1, keepdims=True)


def run(mask, manifest):
    idx = np.nonzero(mask)[0]
    if a.limit:
        idx = idx[:a.limit]
    kd = E64[idx] @ slot["kinds"].T
    sd = E64[idx] @ slot["species"].T
    out = []
    for j, i in enumerate(idx):
        r = F.fuse(manifest, table, int(ES.month[i]), kd[j], sd[j], kind_bias=slot["kind_bias"], species_bias=slot["species_bias"])
        out.append(r)
    return idx, out


def level(conf, hit, floor=0.9, least=30):
    good = None
    for tau in np.round(np.arange(0.05, 0.996, 0.01), 2)[::-1]:
        m = conf >= tau
        if m.sum() < least:
            continue
        if hit[m].mean() >= floor:
            good = float(tau)
        else:
            break
    return good


sci_of = [r[0] for r in table]
t0 = time.time()
# 2. thresholds from the tuning photos: naming off, offers always made
probe = copy.deepcopy(man)
probe["fusion"]["name_at"], probe["fusion"]["offer_at"] = 2.0, 0.0
idx, res = run(tune, probe)
top_p = np.array([r["species"][0]["p"] for r in res])
top_ok = np.array([r["species"][0]["kind"] == r["kind"] and r["kind"] not in ("none", "person") for r in res])
top_right = np.array([truth[i] >= 0 and r["species"][0]["sci"] == sci_of[truth[i]] for i, r in zip(idx, res)])
name_at = level(top_p[top_ok], top_right[top_ok])
named = top_ok & (top_p >= name_at) if name_at is not None else np.zeros(len(res), bool)
off_p = np.array([sum(o["p"] for o in r["offers"]) for r in res])
off_has = np.array([truth[i] >= 0 and any(o["sci"] == sci_of[truth[i]] for o in r["offers"]) for i, r in zip(idx, res)])
can_offer = ~named & np.array([len(r["offers"]) > 0 for r in res])
offer_at = level(off_p[can_offer], off_has[can_offer])
man["fusion"]["name_at"] = name_at if name_at is not None else 2.0
man["fusion"]["offer_at"] = offer_at if offer_at is not None else 2.0
man["fusion_thresholds_note"] = "set by tools/eval/shipped.py on %d tuning photos (%s) through tools/fusion/fuse.py; 2 means never" % (len(res), evn["tuned_on"])
if not a.limit:
    with open(os.path.join(a.slot, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(man, f, indent=1)
        f.write("\n")

# 3. the test photos, as the page would answer
idx, res = run(ES.test, man)
n = len(res)
eyes = ES.eyes[idx]
kind_right = np.array([r["kind"] == e for r, e in zip(res, eyes)])
is_named = np.array([r["named"] is not None for r in res])
is_offer = np.array([len(r["offers"]) > 0 for r in res])
rest = ~is_named & ~is_offer
tsci = [sci_of[truth[i]] if truth[i] >= 0 else None for i in idx]
named_right = np.array([r["named"] is not None and r["named"]["sci"] == t for r, t in zip(res, tsci)])
offer_has = np.array([any(o["sci"] == t for o in r["offers"]) for r, t in zip(res, tsci)])
top1 = np.array([r["species"][0]["sci"] == t for r, t in zip(res, tsci)])
top5 = np.array([any(s["sci"] == t for s in r["species"]) for r, t in zip(res, tsci)])
said = np.array([r["kind"] for r in res])
# parity with a direct computation of the top species from the same files
f = man["fusion"]
W = np.array([r[3] for r in table], dtype=np.float64)
lp = np.log(np.maximum(W / W.sum(0, keepdims=True), f.get("prior_floor", 1e-6))).T
zs = f["t_species"] * (E64[idx] @ slot["species"].T) + (slot["species_bias"] if slot["species_bias"] is not None else 0) + f["alpha_prior"] * lp[ES.month[idx]]
differ = int((np.array([sci_of[j] for j in zs.argmax(1)]) != np.array([r["species"][0]["sci"] for r in res])).sum())
num = {"test_photos": n, "tuning_photos": int(tune.sum()), "name_at": name_at, "offer_at": offer_at,
       "kind_right": ev.ci(kind_right), "called_person": float((said == "person").mean()), "called_none": float((said == "none").mean()),
       "species_top1": ev.ci(top1), "species_top5": ev.ci(top5),
       "named": ev.ci(is_named), "named_right": ev.ci(named_right[is_named]), "named_kind_right": ev.ci(kind_right[is_named]),
       "offered": ev.ci(is_offer), "offered_holds_species": ev.ci(offer_has[is_offer]), "offered_kind_right": ev.ci(kind_right[is_offer]),
       "kind_only": ev.ci(rest), "kind_only_kind_right": ev.ci(kind_right[rest]),
       "top_species_differs_from_direct_computation": differ, "seconds": round(time.time() - t0, 1)}


def pci(v):
    return "–" if not v or v[0] is None else "%.1f%% (%.1f to %.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])


text = ("The slot holds the head `%s` for `%s` (%s), fitted on `%s`, with %d species rows%s. Every photo's vector (`%s`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). "
        "Settings: rule `%s`, t_kind %g, w_kind %g, alpha_prior %g. On %d tuning photos (%s) the thresholds came out as name_at %s and offer_at %s. "
        "On the %d test photos the kind of eye is right for %s; the top species is right for %s and is among the first five for %s. `person` was said for %.2f%% of these photos and `none` for %.2f%%; the set holds neither. "
        "The top species from fuse.py differs from a direct matrix computation on the same files for %d photos.") % (
    evn["head"], evn["model"], evn["choice"], evn["train_vectors"], len(table), ", and a bias a row" if slot["species_bias"] is not None else "", evn["test_vectors"],
    f.get("rule", "product"), f["t_kind"], f["w_kind"], f["alpha_prior"], len(top_p), evn["tuned_on"],
    ("%.2f" % name_at) if name_at is not None else "never (no level reached nine in ten)", ("%.2f" % offer_at) if offer_at is not None else "never (no level reached nine in ten)",
    n, pci(num["kind_right"]), pci(num["species_top1"]), pci(num["species_top5"]), 100 * num["called_person"], 100 * num["called_none"], differ)
if man.get("needs"):
    text += " The slot needs: %s." % "; ".join(man["needs"])
# how many photos get a name when a named species must be right more often than nine times in ten
t_p = np.array([r["species"][0]["p"] for r in res])
t_ok = np.array([r["species"][0]["kind"] == r["kind"] and r["kind"] not in ("none", "person") for r in res])
levels = []
for floor in (0.9, 0.95, 0.98):
    tau = level(top_p[top_ok], top_right[top_ok], floor=floor)
    m = t_ok & (t_p >= tau) if tau is not None else np.zeros(n, bool)
    levels.append({"right_at_least": floor, "name_at": tau, "named": ev.ci(m), "named_right": ev.ci(top1[m])})
num["levels"] = levels

# 4. photos of people, pets, livestock and rooms (data/extra/<name>), when their vectors are published
extra = []
for xname in ("coco-kinds",):
    xman = os.path.join(a.root, "data", "extra", xname, "manifest.csv")
    xv = next((v for v in (xname + ".wasm-int8-per-channel", xname) if os.path.exists(os.path.join(a.root, "lab", evn["model"], "images", v + ".f16.npy"))), None) if "wasm" in evn["test_vectors"] else (xname if os.path.exists(os.path.join(a.root, "lab", evn["model"], "images", xname + ".f16.npy")) else None)
    if not os.path.exists(xman) or xv is None:
        continue
    Ex, xids = ev.load_images(a.root, evn["model"], xv)
    by = {r["id"]: r for r in ev.read_manifest(a.root, "extra/" + xname)}
    sel = [k for k, i in enumerate(xids) if by[i]["split"] == "test"]
    if a.limit:
        sel = sel[:a.limit]
    Ex = Ex[sel].astype(np.float64)
    Ex /= np.linalg.norm(Ex, axis=1, keepdims=True)
    xr = [by[xids[k]] for k in sel]
    kdx, sdx = Ex @ slot["kinds"].T, Ex @ slot["species"].T
    xres = [F.fuse(man, table, int(r["month"] or 6) - 1, kdx[j], sdx[j], kind_bias=slot["kind_bias"], species_bias=slot["species_bias"]) for j, r in enumerate(xr)]
    xe = np.array([r["eyes"] for r in xr])
    xs = np.array([r["kind"] for r in xres])
    xn = np.array([r["named"] is not None for r in xres])
    rows_x = [{"kind": k, "n": int((xe == k).sum()), "right": ev.ci(xs[xe == k] == k), "person": float((xs[xe == k] == "person").mean()), "none": float((xs[xe == k] == "none").mean()), "named": float(xn[xe == k].mean())} for k in ("person", "none", "cat", "dog", "deer") if (xe == k).any()]
    extra.append({"set": xname, "vectors": "images/" + xv, "rows": rows_x,
                  "text": "The %d test photos of the extra set `%s` (COCO photos of people, cats, dogs, grazing animals and rooms with nothing alive; vectors `images/%s`) went through the same slot. A species name on a photo of a person or a room is always wrong." % (len(xr), xname, xv)})
    print(extra[-1]["text"])
    for g in rows_x:
        print("  %-7s n %4d  right %s  person %.3f  none %.3f  named %.3f" % (g["kind"], g["n"], pci(g["right"]), g["person"], g["none"], g["named"]))

outcomes = [{"what": "a species name", "share": num["named"][0], "right": "the name is right for %s; the kind for %s" % (pci(num["named_right"]), pci(num["named_kind_right"]))},
            {"what": "three species to choose from", "share": num["offered"][0], "right": "the three hold the species for %s; the kind is right for %s" % (pci(num["offered_holds_species"]), pci(num["offered_kind_right"]))},
            {"what": "a kind of eye only", "share": num["kind_only"][0], "right": "the kind is right for %s" % pci(num["kind_only_kind_right"])}]
out = {"made_by": "tools/eval/shipped.py", "slot": name, "manifest": {k: man[k] for k in ("id", "fusion", "evaluation", "needs") if k in man}, "numbers": num, "text": text, "outcomes": outcomes, "extra": extra}
print(text)
for o in outcomes:
    print("  %-30s %5.1f%%  %s" % (o["what"], 100 * (o["share"] or 0), o["right"]))
if not a.limit:
    ev.write_json(a.out or "docs/eval/shipped-%s.json" % name, out)
