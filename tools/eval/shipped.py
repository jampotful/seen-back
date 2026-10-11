#!/usr/bin/env python3
"""Score an exported slot exactly as the page would, through tools/fusion/fuse.py, and set its two thresholds.

  python3 -I tools/eval/shipped.py <root> <slot dir> [--name pocket] [--out docs/eval/shipped-<name>.json] [--limit N]

1. Reads the slot as the page does (fuse.load_slot: half-precision rows, biases, the species table).
2. On the tuning photos, with naming switched off, records what fuse.py would name and offer. From those it sets
   name_at, the lowest level from which a named species was right at least nine times in ten, and offer_at, the lowest
   level from which the three offered species held the right one at least nine times in ten. Both go into manifest.json.
3. Sets kind_at, the level under which the page says it is not sure of the kind: the lowest level from which an asserted
   kind was right at least 95 times in 100 on the wildlife tuning photos and, taken by themselves, on the tuning third of
   the extra set (people, cats, dogs, grazing animals, rooms with nothing alive; tools/eval/kinds.py), when the
   model's vectors of that set are published.
4. On the test photos, with the thresholds set, reports what the page would show and how often it is right: the
   wildlife test photos, and beside them the extra set's test rows, with a table of the kinds for each.
The photos' vectors are the ones named in the manifest's "evaluation" block (for a pocket model, the WASM int8 vectors).
--vectors names another set of vectors of the evaluation photos (for example the int8 file of the larger model), and
--no-write leaves the slot's manifest as it is.
"""
import argparse, copy, hashlib, json, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "fusion"))
import ev
import kinds
import fuse as F

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("slot")
ap.add_argument("--name")
ap.add_argument("--out")
ap.add_argument("--limit", type=int, default=0, help="score only the first N tuning and N test photos (for a quick try)")
ap.add_argument("--rule", choices=["product"], help="score the slot under the product rule (what build 6 of the page computes) with the settings in fusion_if_rule_product; the thresholds found are written there")
ap.add_argument("--vectors", help="score these vectors of the evaluation photos in place of the manifest's (the part after images/, for example alachua-2025.wasm-int8)")
ap.add_argument("--no-write", action="store_true", help="do not write the thresholds into the slot's manifest")
ap.add_argument("--as-shipped", action="store_true", help="score the slot with the name_at, offer_at and kind_at its manifest carries (the slot as the page has it); implies --no-write")
ap.add_argument("--name-bar", type=float, default=0.9, help="name_at is the lowest level from which a named species was right at least this often on the tuning photos; when no level reaches it, the nine-in-ten level")
a = ap.parse_args()
if a.as_shipped:
    a.no_write = True
name = a.name or os.path.basename(os.path.normpath(a.slot))
slot = F.load_slot(a.slot)
man, table = slot["manifest"], slot["table"]
on_disk = copy.deepcopy(man)
if a.rule == "product":
    alt = man.get("fusion_if_rule_product")
    if not alt:
        raise SystemExit("this slot carries no settings for the product rule")
    man["fusion"] = dict(man["fusion"], rule="product", t_kind=alt["t_kind"], w_kind=alt["w_kind"])
    man["needs"] = [x for x in man.get("needs", []) if "rule mix" not in x]
    name += "-product"
evn = man["evaluation"]
keys = json.load(open(os.path.join(a.slot, man["species"]["table"]), encoding="utf-8"))["keys"]
if a.vectors:
    evn["test_vectors"] = "images/" + a.vectors
E, ids = ev.load_images(a.root, evn["model"], evn["test_vectors"].split("/", 1)[1])
if E is None:
    raise SystemExit("no vectors %s for %s under %s" % (evn["test_vectors"], evn["model"], a.root))
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


def score(V, months, manifest):
    """Every row of V (unit vectors, float64) through fuse.py with the slot's own files."""
    kd = V @ slot["kinds"].T
    sd = V @ slot["species"].T
    return [F.fuse(manifest, table, int(months[j]), kd[j], sd[j], kind_bias=slot["kind_bias"], species_bias=slot["species_bias"]) for j in range(len(V))]


def run(mask, manifest):
    idx = np.nonzero(mask)[0]
    if a.limit:
        idx = idx[:a.limit]
    return idx, score(E64[idx], ES.month[idx], manifest)


def unit64(X):
    X = X.astype(np.float64)
    return X / np.linalg.norm(X, axis=1, keepdims=True)


def kind_fields(res, eyes):
    """From fuse.py's answers: the winning kind, its probability, whether the true kind is among the three likeliest."""
    said = np.array([r["kind"] for r in res])
    prob = np.array([r["kindP"] for r in res])
    three = np.array([e in [k["key"] for k in r["kinds"][:3]] for r, e in zip(res, eyes)], dtype=bool)
    return said, prob, three


# people, pets, livestock and rooms: the tuning third joins the tuning photos of the kind decision, the test rows are reported
XT = kinds.load(a.root, evn["model"], want_wasm="wasm" in evn["test_vectors"])
if XT is not None and a.limit:
    for part in ("tune", "test"):
        XT[part] = {k: (v[:a.limit] if k != "vectors" else v) for k, v in XT[part].items()}


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
name_at = level(top_p[top_ok], top_right[top_ok], floor=a.name_bar)
name_bar_used = a.name_bar
if name_at is None and a.name_bar != 0.9:
    name_at, name_bar_used = level(top_p[top_ok], top_right[top_ok]), 0.9
named = top_ok & (top_p >= name_at) if name_at is not None else np.zeros(len(res), bool)
off_p = np.array([sum(o["p"] for o in r["offers"]) for r in res])
off_has = np.array([truth[i] >= 0 and any(o["sci"] == sci_of[truth[i]] for o in r["offers"]) for i, r in zip(idx, res)])
can_offer_all = np.array([len(r["offers"]) > 0 for r in res])
can_offer = ~named & can_offer_all
offer_at = level(off_p[can_offer], off_has[can_offer])
man["fusion"]["name_at"] = name_at if name_at is not None else 2.0
man["fusion"]["offer_at"] = offer_at if offer_at is not None else 2.0
man["fusion_thresholds_note"] = "set by tools/eval/shipped.py on %d tuning photos (%s) through tools/fusion/fuse.py; 2 means never" % (len(res), evn["tuned_on"])
if a.name_bar != 0.9:
    man["fusion_thresholds_note"] += ("; name_at is the lowest level from which a named species was right at least %d times in 100 on the tuning photos%s; offer_at is the nine-in-ten level for the photos left without a name" % (
        round(100 * a.name_bar), "" if name_bar_used == a.name_bar else " (no level reached that, so the nine-in-ten level was taken)"))
# 3. kind_at: under it the page says it is not sure. Set where an asserted kind is right at least 95 times in 100 on each tuning set by itself.
tune_sets = [("wildlife", kind_fields(res, ES.eyes[idx]), ES.eyes[idx])]
if XT is not None and len(XT["tune"]["ids"]):
    xres_tune = score(unit64(XT["tune"]["X"]), XT["tune"]["month"], probe)
    tune_sets.append(("extra", kind_fields(xres_tune, XT["tune"]["eyes"]), XT["tune"]["eyes"]))
kind_levels = {bar: kinds.kind_at([(f_[1], f_[0] == eyes_) for _, f_, eyes_ in tune_sets], bar) for bar in kinds.BARS}
kind_at = kind_levels[kinds.BAR]
if kind_at is not None:
    man["fusion"]["kind_at"] = kind_at
else:
    man["fusion"].pop("kind_at", None)
man["fusion_kind_at_note"] = ("kind_at was set by tools/eval/shipped.py through tools/fusion/fuse.py: the lowest level from which an asserted kind was right at least %d times in 100 on %s. %s" % (
    round(100 * kinds.BAR), " and on ".join("%d %s tuning photos" % (len(e_), n_ if n_ == "wildlife" else "extra-set (coco-kinds)") for n_, _, e_ in tune_sets),
    "No level reached that, so the key is left out and the page asserts every kind." if kind_at is None else "Under it the page should say that it is not sure and offer its three likeliest kinds."))
if a.as_shipped:
    # the thresholds the manifest carries replace the ones just set on the tuning photos; the slot is scored as the page has it
    f0 = on_disk["fusion"]
    name_at = f0["name_at"] if f0.get("name_at", 2.0) <= 1 else None
    offer_at = f0["offer_at"] if f0.get("offer_at", 2.0) <= 1 else None
    kind_at = f0.get("kind_at")
    man["fusion"]["name_at"], man["fusion"]["offer_at"] = f0.get("name_at", 2.0), f0.get("offer_at", 2.0)
    if kind_at is None:
        man["fusion"].pop("kind_at", None)
    else:
        man["fusion"]["kind_at"] = kind_at
    for k_ in ("fusion_thresholds_note", "fusion_kind_at_note"):
        man[k_] = on_disk.get(k_, "")
if not a.limit and not a.no_write:
    if a.rule == "product":
        on_disk["fusion_if_rule_product"].update(name_at=man["fusion"]["name_at"], offer_at=man["fusion"]["offer_at"],
                                                 note="for a page that only has the product rule (build 6): use these four values in place of the same keys of fusion")
        to_write = on_disk
    else:
        to_write = man
    with open(os.path.join(a.slot, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(to_write, f, indent=1)
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
said, kprob, kthree = kind_fields(res, eyes)
sure = kprob >= kind_at if kind_at is not None else np.ones(n, bool)
sure_field_differs = sum(("sure" in r) and (bool(r["sure"]) != bool(s_)) for r, s_ in zip(res, sure))     # fuse.py's own field, once the page has the answer "not sure"
# parity with a direct computation of the top species from the same files
f = man["fusion"]
W = np.array([r[3] for r in table], dtype=np.float64)
lp = np.log(np.maximum(W / W.sum(0, keepdims=True), f.get("prior_floor", 1e-6))).T
zs = f["t_species"] * (E64[idx] @ slot["species"].T) + (slot["species_bias"] if slot["species_bias"] is not None else 0) + f["alpha_prior"] * lp[ES.month[idx]]
differ = int((np.array([sci_of[j] for j in zs.argmax(1)]) != np.array([r["species"][0]["sci"] for r in res])).sum())
num = {"test_photos": n, "tuning_photos": int(tune.sum()), "name_at": name_at, "offer_at": offer_at, "name_bar_asked": a.name_bar, "name_bar_used": name_bar_used,
       "kind_right": ev.ci(kind_right), "called_person": float((said == "person").mean()), "called_none": float((said == "none").mean()),
       "species_top1": ev.ci(top1), "species_top5": ev.ci(top5),
       "named": ev.ci(is_named), "named_right": ev.ci(named_right[is_named]), "named_kind_right": ev.ci(kind_right[is_named]),
       "offered": ev.ci(is_offer), "offered_holds_species": ev.ci(offer_has[is_offer]), "offered_kind_right": ev.ci(kind_right[is_offer]),
       "kind_only": ev.ci(rest), "kind_only_kind_right": ev.ci(kind_right[rest]),
       "top_species_differs_from_direct_computation": differ, "seconds": round(time.time() - t0, 1)}
# the kind of eye with the answer "not sure": wildlife test photos, and the extra set's test rows beside them
num["kind_at"] = kind_at
num["as_shipped"] = bool(a.as_shipped)
kd_ = {"bar": kinds.BAR, "kind_at": kind_at, "tuned_on": {n_: int(len(e_)) for n_, _, e_ in tune_sets}, "extra_set_vectors_published": XT is not None,
       "fuse_sure_field_differs": int(sure_field_differs),
       "tuning": {n_: kinds.outcome(f_[0], f_[1], f_[2], e_, kind_at) for n_, f_, e_ in tune_sets},
       "test_wildlife": kinds.outcome(said, kprob, kthree, eyes, kind_at),
       "test_wildlife_named_and_asserted": ev.ci(is_named & sure), "test_wildlife_named_and_asserted_right": ev.ci(named_right[is_named & sure]),
       "table_wildlife": kinds.table(said, kprob, kthree, eyes, kind_at, named=is_named, order=[k for k in ev.KINDS if (eyes == k).any()]),
       "asserted_wildlife": kinds.by_said(said, kprob, eyes, kind_at)}
xtest = None
if XT is not None and len(XT["test"]["ids"]):
    xres = score(unit64(XT["test"]["X"]), XT["test"]["month"], man)
    xe = XT["test"]["eyes"]
    xs, xp, x3 = kind_fields(xres, xe)
    xn = np.array([r["named"] is not None for r in xres])
    xo = np.array([len(r["offers"]) > 0 for r in xres])
    xsure = xp >= kind_at if kind_at is not None else np.ones(len(xs), bool)
    kd_["test_extra"] = kinds.outcome(xs, xp, x3, xe, kind_at)
    kd_["test_extra_vectors"] = XT["test"]["vectors"]
    kd_["test_extra_named"] = ev.ci(xn)
    kd_["test_extra_named_and_asserted"] = ev.ci(xn & xsure)
    kd_["test_extra_offered"] = ev.ci(xo)
    kd_["table_extra"] = kinds.table(xs, xp, x3, xe, kind_at, named=xn, order=kinds.EXTRA_KINDS)
    kd_["asserted_extra"] = kinds.by_said(xs, xp, xe, kind_at)
    xtest = (xs, xp, x3, xe)
kd_["levels"] = []
for bar in kinds.BARS:
    tau = kind_levels[bar]
    row = {"right_at_least": bar, "kind_at": tau}
    if tau is not None:
        row["test_wildlife"] = kinds.outcome(said, kprob, kthree, eyes, tau)
        if xtest is not None:
            row["test_extra"] = kinds.outcome(xtest[0], xtest[1], xtest[2], xtest[3], tau)
    kd_["levels"].append(row)
num["kind"] = kd_


def pci(v):
    return "–" if not v or v[0] is None else "%.1f%% (%.1f to %.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])


text = ("The slot holds the head `%s` for `%s` (%s), fitted on `%s`, with %d species rows%s. Every photo's vector (`%s`) went through `tools/fusion/fuse.py`, the reference of the page's arithmetic, with the slot's own files as the page reads them (half-precision rows). "
        "Settings: rule `%s`, t_kind %g, w_kind %g, alpha_prior %g. " + ("The thresholds are the ones the slot's manifest carries: name_at %s and offer_at %s. " if a.as_shipped else "On %d tuning photos (%s) the thresholds came out as name_at %s and offer_at %s. ") +
        "On the %d test photos the kind of eye is right for %s; the top species is right for %s and is among the first five for %s. `person` was said for %.2f%% of these photos and `none` for %.2f%%; the set holds neither. "
        "The top species from fuse.py differs from a direct matrix computation on the same files for %d photos.") % (
    evn["head"], evn["model"], evn["choice"], evn["train_vectors"], len(table), ", and a bias a row" if slot["species_bias"] is not None else "", evn["test_vectors"],
    f.get("rule", "product"), f["t_kind"], f["w_kind"], f["alpha_prior"], *(() if a.as_shipped else (len(top_p), evn["tuned_on"])),
    ("%.2f" % name_at) if name_at is not None else "never (no level reached nine in ten)", ("%.2f" % offer_at) if offer_at is not None else "never (no level reached nine in ten)",
    n, pci(num["kind_right"]), pci(num["species_top1"]), pci(num["species_top5"]), 100 * num["called_person"], 100 * num["called_none"], differ)
pk = lambda v: "–" if not v or v[0] is None else "%.1f%% (%.1f to %.1f)" % (100 * v[0], 100 * v[1], 100 * v[2])
tw = kd_["test_wildlife"]
if kind_at is not None:
    text += (" The kinds head is `%s`. With kind_at %.2f (%s), the page asserts a kind for %s of the wildlife test photos and is right for %s of those; for the %s where it is not sure, the true kind is among its three likeliest for %s." % (
        evn.get("kind_head", "kind phrases"), kind_at, "as the slot's manifest carries it" if a.as_shipped else "set on wildlife tuning photos and the extra set's tuning third" if len(tune_sets) > 1 else "set on wildlife tuning photos alone, because the extra set's vectors were not published for this model",
        pk(tw["asserted"]), pk(tw["asserted_right"]), pk(tw["not_sure"]), pk(tw["not_sure_true_kind_among_three"])))
    if "test_extra" in kd_:
        tx = kd_["test_extra"]
        text += (" On the %d test photos of people, cats, dogs, grazing animals and rooms (`%s`), the kind is right for %s; the page asserts a kind for %s and is right for %s of those; where it is not sure the true kind is among its three likeliest for %s. A species is named on %s of these photos." % (
            tx["photos"], kd_["test_extra_vectors"], pk(tx["kind_right"]), pk(tx["asserted"]), pk(tx["asserted_right"]), pk(tx["not_sure_true_kind_among_three"]), pk(kd_["test_extra_named"])))
else:
    text += " No level of the winning kind's probability made asserted kinds right %d times in 100 on the tuning photos, so the slot carries no kind_at." % round(100 * kinds.BAR)
if man.get("needs"):
    text += " The slot needs: %s." % "; ".join(man["needs"])
# how many photos get a name when a named species must be right more often than nine times in ten, and what the
# three offers then do for the rest; from a second pass over the test photos with naming off and offers always made
_, res2 = run(ES.test, probe)
t_p = np.array([r["species"][0]["p"] for r in res2])
t_ok = np.array([r["species"][0]["kind"] == r["kind"] and r["kind"] not in ("none", "person") for r in res2])
t_right = np.array([r["species"][0]["sci"] == t for r, t in zip(res2, tsci)])
t_off_p = np.array([sum(o["p"] for o in r["offers"]) for r in res2])
t_off_has = np.array([any(o["sci"] == t for o in r["offers"]) for r, t in zip(res2, tsci)])
t_can = np.array([len(r["offers"]) > 0 for r in res2])
levels = []
for floor in sorted({0.9, 0.95, 0.98, a.name_bar}):
    tau = level(top_p[top_ok], top_right[top_ok], floor=floor)
    if tau is None:
        levels.append({"right_at_least": floor, "name_at": None})
        continue
    nm_u = top_ok & (top_p >= tau)
    tau_o = level(off_p[~nm_u & can_offer_all], off_has[~nm_u & can_offer_all])
    m = t_ok & (t_p >= tau)
    of = ~m & t_can & (t_off_p >= tau_o) if tau_o is not None else np.zeros(n, bool)
    levels.append({"right_at_least": floor, "name_at": tau, "named": ev.ci(m), "named_right": ev.ci(t_right[m]), "offer_at": tau_o, "offered": ev.ci(of), "offered_holds_species": ev.ci(t_off_has[of]), "kind_only": ev.ci(~m & ~of)})
num["levels"] = levels

# the older layout of the extra set's rows, kept for the report's short table
extra = []
if "table_extra" in kd_:
    extra.append({"set": kinds.EXTRA, "vectors": kd_["test_extra_vectors"], "rows": [{"kind": g["kind"], "n": g["n"], "right": g["right"], "person": g["said_person"], "none": g["said_none"], "named": g["named"]} for g in kd_["table_extra"]],
                  "text": "The %d test photos of the extra set `%s` (COCO photos of people, cats, dogs, grazing animals and rooms with nothing alive; vectors `%s`) went through the same slot, each with a calendar month drawn by a hash of its id. A species name on a photo of a person or a room is always wrong." % (
                      kd_["test_extra"]["photos"], kinds.EXTRA, kd_["test_extra_vectors"])})

outcomes = [{"what": "a species name", "share": num["named"][0], "right": "the name is right for %s; the kind for %s" % (pci(num["named_right"]), pci(num["named_kind_right"]))},
            {"what": "three species to choose from", "share": num["offered"][0], "right": "the three hold the species for %s; the kind is right for %s" % (pci(num["offered_holds_species"]), pci(num["offered_kind_right"]))},
            {"what": "a kind of eye only", "share": num["kind_only"][0], "right": "the kind is right for %s" % pci(num["kind_only_kind_right"])}]
# one character a photo, in the order of the vectors, so that two slots scored on the same photos can be compared photo by photo (tools/eval/decide.py)
bits = lambda v: "".join("1" if x else "0" for x in v)
sha = lambda ids_: hashlib.sha256("\n".join(ids_).encode()).hexdigest()
per_photo = {"wildlife": {"ids_sha256": sha([ids[i] for i in idx]), "kind_right": bits(kind_right), "asserted_right": bits(kind_right & sure), "asserted_wrong": bits(~kind_right & sure), "named": bits(is_named), "named_right": bits(named_right)}}
if xtest is not None:
    per_photo["extra"] = {"ids_sha256": sha(XT["test"]["ids"]), "kind_right": bits(xs == xe), "asserted_right": bits((xs == xe) & xsure), "asserted_wrong": bits((xs != xe) & xsure), "named": bits(xn)}
out = {"made_by": "tools/eval/shipped.py", "slot": name, "manifest": {k: man[k] for k in ("id", "fusion", "evaluation", "needs") if k in man}, "numbers": num, "text": text, "outcomes": outcomes, "extra": extra}
if not a.limit:
    out["per_photo"] = per_photo
print(text)
for o in outcomes:
    print("  %-30s %5.1f%%  %s" % (o["what"], 100 * (o["share"] or 0), o["right"]))
if not a.limit:
    ev.write_json(a.out or "docs/eval/shipped-%s.json" % name, out)
