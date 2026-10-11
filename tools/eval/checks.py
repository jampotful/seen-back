#!/usr/bin/env python3
"""Checks for leakage and for mistakes in the evaluation's inputs.

  python3 -I tools/eval/checks.py <root> [--out docs/eval/checks.json]

Each check is a line of the output with a verdict: "pass", "FAIL", "note" (a fact to know), or "waiting"
(the file it needs is not published yet). The script exits 1 if any check fails.
"""
import argparse, csv, hashlib, json, os, re, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ev

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("--out", default="docs/eval/checks.json")
a = ap.parse_args()
root = a.root
checks = []


def add(name, verdict, detail):
    checks.append({"check": name, "verdict": verdict, "detail": detail})
    print("%-7s %s: %s" % (verdict, name, detail))


rows = ev.read_manifest(root)
species = ev.read_species(root)
spj = json.load(open(os.path.join(root, "data", "regions", ev.REGION, "species.json"), encoding="utf-8"))
through = spj["source"]["records_through"]

# 1. dates
early = [r["id"] for r in rows if r["date"] <= through]
add("every evaluation photo is dated after the species list's last record (%s)" % through, "pass" if not early else "FAIL",
    "%d rows; earliest %s, latest %s; rows on or before %s: %d" % (len(rows), min(r["date"] for r in rows), max(r["date"] for r in rows), through, len(early)))
snap = "2024-05-01"
add("every evaluation photo is dated after the GBIF snapshot behind BioCLIP 2's training data (%s)" % snap, "pass" if min(r["date"] for r in rows) > snap else "FAIL",
    "earliest evaluation date %s. This says nothing about BioCLIP 2.5, whose card gives no snapshot date." % min(r["date"] for r in rows))
# observation numbers on iNaturalist grow with the time an observation was created
obs = np.array([int(r["obs_url"].rsplit("/", 1)[1]) for r in rows])
first_day = min(r["date"] for r in rows)
floor_id = int(min(o for o, r in zip(obs, rows) if r["date"] == first_day))
older = int((obs < floor_id).sum())
add("no evaluation observation was created before the first one dated %s" % first_day, "pass" if older == 0 else "note",
    "observation numbers run from %d to %d; the smallest number among observations dated %s is %d; observations with a smaller number: %d. "
    "A smaller number would mean an observation created earlier than 2025 and dated later." % (obs.min(), obs.max(), first_day, floor_id, older))
bad_month = sum(int(r["month"]) != int(r["date"][5:7]) for r in rows)
add("the month column is the month of the date", "pass" if not bad_month else "FAIL", "%d rows disagree" % bad_month)

# 2. identity
for col in ("id", "gbif_id", "obs_url", "photo_url"):
    n = len({r[col] for r in rows})
    add("no two evaluation rows share a value of %s" % col, "pass" if n == len(rows) else "FAIL", "%d distinct values in %d rows" % (n, len(rows)))
wrong_split = sum(("val" if int(hashlib.sha256(str(r["gbif_id"]).encode()).hexdigest()[:8], 16) % 10 < 3 else "test") != r["split"] for r in rows)
add("the split is the stated function of gbif_id alone (tools/species/build_eval.py, split_of)", "pass" if not wrong_split else "FAIL",
    "%d rows disagree; val %d, test %d" % (wrong_split, sum(r["split"] == "val" for r in rows), sum(r["split"] == "test" for r in rows)))

# 3. the species list
bad_sum = sum(sum(s["m"]) != s["n"] for s in species)
order_ok = all(species[i]["n"] >= species[i + 1]["n"] for i in range(len(species) - 1))
add("in the species list the twelve monthly counts add up to the total, and species are sorted by total", "pass" if not bad_sum and order_ok else "FAIL",
    "%d species; %d whose months do not add up; sorted: %s" % (len(species), bad_sum, order_ok))
keys = [s["key"] for s in species]
add("no GBIF species key appears twice in the list", "pass" if len(set(keys)) == len(keys) else "FAIL", "%d keys, %d distinct" % (len(keys), len(set(keys))))
names = {}
for s in species:
    names.setdefault(s["sci"], []).append(s["key"])
dup = {k: v for k, v in names.items() if len(v) > 1}
add("scientific names carried by more than one species key", "note",
    "%d: %s. Their sentence rows are identical, so the later key can never be the top answer; photos of it on the test split: %d." % (
        len(dup), json.dumps(dup, ensure_ascii=False), sum(r["split"] == "test" and int(r["key"]) in {v for vs in dup.values() for v in vs[1:]} for r in rows)))
key2s = {s["key"]: s for s in species}
mism = sum(1 for r in rows if int(r["key"]) in key2s and (key2s[int(r["key"])]["sci"] != r["sci"] or key2s[int(r["key"])]["eyes"] != r["eyes"]))
add("an evaluation row's name and kind of eye equal the species list's for the same key", "pass" if not mism else "FAIL", "%d rows disagree" % mism)
test = [r for r in rows if r["split"] == "test"]
out_of_list = sum(int(r["key"]) not in key2s for r in test)
add("test photos whose species is not in the list at all", "note", "%d of %d, so a recognizer held to the list can reach at most %.4f." % (out_of_list, len(test), 1 - out_of_list / len(test)))

# 4. vectors line up with rows
mid = [r["id"] for r in rows]
stale, stale_eyes = {}, {}
sha_species = ev.sha256_file(os.path.join(root, "data", "regions", ev.REGION, "species.json"))
for model in sorted(os.listdir(os.path.join(root, "lab"))):
    d = os.path.join(root, "lab", model)
    files = json.load(open(os.path.join(d, "_files.json"))) if os.path.exists(os.path.join(d, "_files.json")) else {}
    problems, seen = [], 0
    for f in sorted(os.listdir(os.path.join(d, "images"))):
        if not f.endswith(".f16.npy") or not f.startswith(ev.EVALSET):
            continue
        name = f[:-8]
        E = np.load(os.path.join(d, "images", f), mmap_mode="r")
        ids = ev.read_ids(os.path.join(d, "images", name + ".ids.json"))
        seen += 1
        if ids != mid:
            problems.append("%s: ids are not the manifest's ids in order (%d ids)" % (name, len(ids)))
        if E.shape[0] != len(ids):
            problems.append("%s: %d vectors for %d ids" % (name, E.shape[0], len(ids)))
        if not np.isfinite(np.asarray(E, dtype=np.float32)).all():
            problems.append("%s: values that are not finite" % name)
        want = (files.get("images/" + f) or {}).get("sha256")
        if want and want != ev.sha256_file(os.path.join(d, "images", f)):
            problems.append("%s: sha256 differs from the branch's _files.json" % name)
    tdir = os.path.join(d, "text")
    for f in sorted(os.listdir(tdir)) if os.path.isdir(tdir) else []:
        if f.startswith("species_") and f.endswith(".labels.json"):
            L = json.load(open(os.path.join(tdir, f), encoding="utf-8"))
            for col in ("key", "sci"):
                if [l.get(col) for l in L["labels"]] != [s[col] for s in species]:
                    problems.append("%s: column %s differs from the species list" % (f, col))
            n_eyes = sum(l.get("eyes") != s["eyes"] for l, s in zip(L["labels"], species))
            if n_eyes:
                stale_eyes.setdefault(n_eyes, []).append(model + "/" + f[:-12])
            if L.get("species_json_sha256") not in (None, sha_species):
                stale.setdefault(sum(l.get("en", "") != s["en"] for l, s in zip(L["labels"], species)), []).append(model + "/" + f[:-12])
            seen += 1
    add("vectors of %s line up with the manifest and the species list" % model, "pass" if not problems else "FAIL",
        "%d files checked; %s" % (seen, "; ".join(problems) or "all 6,000 ids in manifest order, no values missing; label rows carry the list's keys and scientific names in the list's order"))
for n_eyes, sets in sorted(stale_eyes.items()):
    add("label files whose kind of eye differs from the species list", "note",
        "%d label sets (%s) carry another kind of eye than the list in %d of %d rows. The studies take the kind from the species list, so no number here is touched; "
        "a slot built from these label files would show the earlier kinds." % (len(sets), ", ".join(sorted({x.split("/")[0] for x in sets})), n_eyes, len(species)))
for n_en, sets in sorted(stale.items()):
    add("label rows made from an earlier species.json", "note",
        "%d label sets (of %s) were made before the list's English names were revised: %d of %d rows carry an English name the list no longer has "
        "(keys, scientific names and kinds agree in every row). Results for species_sci are unaffected; results for species_com and species_taxon_com "
        "describe the earlier names and would change if the rows were made again." % (len(sets), ", ".join(sorted({x.split("/")[0] for x in sets})), n_en, len(species)))

# what the earlier English names may cost a pocket model that is scored against English names
for model in ("tinyclip-39m-16",):
    E, ids = ev.load_images(root, model)
    Sx, labels = ev.load_text(root, model, "species_com")
    if E is None or Sx is None:
        continue
    ES = ev.EvalSet(root, ids)
    changed = np.array([l.get("en", "") != s_["en"] for l, s_ in zip(labels, species)])
    yt = ES.y[ES.test]
    hit = ev.ranks(E[ES.test] @ Sx.T, yt) == 0
    on = (yt >= 0) & changed[np.maximum(yt, 0)]
    if on.any():
        add("test photos of species whose English label row carries an earlier name (%s, species_com, no prior)" % model, "note",
            "%d of %d test photos; top-1 is %.3f on them and %.3f on the others. Examples of earlier and present names: %s. Making the English-name rows again from the present list is likely to help the pocket models; by how much is unmeasured." % (
                int(on.sum()), len(yt), hit[on].mean(), hit[~on].mean(), "; ".join("%s / %s" % (labels[i].get("en", ""), species[i]["en"]) for i in np.nonzero(changed)[0][:4])))

# 5. the same photo on both sides of the split
for model, level in (("clip-b32", 0.98), ("bioclip2-l14", 0.999)):
    E, ids = ev.load_images(root, model)
    if E is None:
        continue
    ES = ev.EvalSet(root, ids)
    C = E[ES.test] @ E[ES.val].T
    near = int((C.max(1) > level).sum())
    add("test photos with an almost identical photo on val (%s cosine above %s)" % (model, level), "pass" if near == 0 else "note", "%d of %d test photos" % (near, int(ES.test.sum())))
    if model == "bioclip2-l14":
        m95 = C.max(1) > 0.95
        add("how tightly BioCLIP 2 groups a species", "note", "%d of %d test photos have a val photo within cosine 0.95, and for %d of those it is the same species. Photos of one species sit close together in this model, which is why a list of names is enough for it." % (
            int(m95.sum()), int(ES.test.sum()), int((m95 & (ES.y[ES.test] == ES.y[ES.val][C.argmax(1)])).sum())))
    del C

# 6. the training set
tp = os.path.join(root, "data", "train", "alachua-pre2025", "manifest.csv")
if os.path.exists(tp):
    with open(tp, newline="", encoding="utf-8") as f:
        train = list(csv.DictReader(f))
    late = sum(r["date"] > through for r in train)
    add("every training photo is dated on or before %s" % through, "pass" if not late else "FAIL", "%d rows; latest %s; rows after: %d" % (len(train), max(r["date"] for r in train), late))
    for col in ("gbif_id", "obs_url", "photo_url"):
        have = sum(bool(r[col]) for r in train)
        shared = len({r[col] for r in rows if r[col]} & {r[col] for r in train if r[col]})
        if not have:
            # the open-data route to the training photos has no GBIF record ids: this comparison cannot speak
            add("no %s is shared between the training and the evaluation photos" % col, "note", "the training manifest's %s column is empty (it was built from iNaturalist's open-data files, which carry no GBIF record id), so this comparison says nothing; the dates and the photo numbers below do the work" % col)
        else:
            add("no %s is shared between the training and the evaluation photos" % col, "pass" if not shared else "FAIL", "%d shared; %d of %d training rows carry a value" % (shared, have, len(train)))
    # the photo's own number in iNaturalist's bucket, which both routes to the training photos carry in the address
    pid = lambda u: (re.search(r"/photos/(\d+)/", u) or [None, None])[1]
    ep, tp_ = {pid(r["photo_url"]) for r in rows}, {pid(r["photo_url"]) for r in train}
    add("no photo number is shared between the training and the evaluation photos", "pass" if None not in ep and None not in tp_ and not (ep & tp_) else "FAIL",
        "%d evaluation and %d training photo numbers read from the addresses; shared: %d; addresses without a number: %d" % (len(ep - {None}), len(tp_ - {None}), len((ep & tp_) - {None}), sum(pid(r["photo_url"]) is None for r in rows + train)))
    num_obs = sum(r["obs_url"].rsplit("/", 1)[-1].isdigit() for r in train)
    add("training observations can be compared with evaluation observations by number", "note" if num_obs < len(train) else "pass",
        "%d of %d training rows give the observation by its number; the others give it by its UUID, which the evaluation manifest does not hold. An observation has one date, and every training row is dated on or before %s while every evaluation row is dated after it, so no observation can be on both sides." % (num_obs, len(train), through))
    dup = len(train) - len({r["photo_url"] for r in train})
    add("no training photo appears twice", "pass" if not dup else "FAIL", "%d repeated photo addresses in %d rows" % (dup, len(train)))
    eyes_bad = sum(r["eyes"] != key2s[int(r["key"])]["eyes"] for r in train if r["key"] and int(r["key"]) in key2s)
    add("the kind of eye of every training row is the species list's", "pass" if not eyes_bad else "FAIL", "%d rows disagree" % eyes_bad)
    per = {}
    for r in train:
        per[r["key"]] = per.get(r["key"], 0) + 1
    notin = sum(int(k) not in key2s for k in per)
    add("training photos per species", "note", "%d photos of %d species (most for one species: %d); species keys outside the list: %d; list species without a training photo: %d" % (
        len(train), len(per), max(per.values()), notin, len(set(keys) - {int(k) for k in per})))
    for model in sorted(os.listdir(os.path.join(root, "lab"))):
        p = os.path.join(root, "lab", model, "images", "alachua-pre2025")
        if os.path.exists(p + ".f16.npy"):
            tid = ev.read_ids(p + ".ids.json")
            tidx = {r["id"]: i for i, r in enumerate(train)}
            in_order = all(t in tidx for t in tid) and all(tidx[tid[i]] < tidx[tid[i + 1]] for i in range(len(tid) - 1))
            n = np.load(p + ".f16.npy", mmap_mode="r").shape[0]
            add("training vectors of %s line up with the training manifest" % model, "pass" if in_order and n == len(tid) else "FAIL", "%d vectors, %d ids, of %d manifest rows; ids in manifest order: %s" % (n, len(tid), len(train), in_order))
            Et, _ = ev.load_images(root, model, "alachua-pre2025")
            Ee, eid = ev.load_images(root, model)
            mx = np.zeros(len(eid), dtype=np.float32)
            for i in range(0, len(Et), 20000):
                mx = np.maximum(mx, (Ee @ Et[i:i + 20000].T).max(1))
            add("evaluation photos with an almost identical training photo for %s (cosine above 0.995)" % model, "note", "%d of %d" % (int((mx > 0.995).sum()), len(eid)))
else:
    add("training photos share no record with the evaluation photos", "waiting", "`data/train/alachua-pre2025/manifest.csv` was not published when the checks ran.")

# 7. the extra set: people, pets, livestock and rooms (COCO 2017)
xp = os.path.join(root, "data", "extra", "coco-kinds", "manifest.csv")
if os.path.exists(xp):
    import kinds as KX
    with open(xp, newline="", encoding="utf-8") as f:
        xrows = list(csv.DictReader(f))
    n_id, n_ph = len({r["id"] for r in xrows}), len({r["photo_url"] for r in xrows})
    add("no two rows of the extra set share an id or a photo", "pass" if n_id == len(xrows) == n_ph else "FAIL", "%d rows, %d ids, %d photo addresses" % (len(xrows), n_id, n_ph))
    wrong_home = sum(("/val2017/" in r["photo_url"]) != (r["split"] == "test") or ("/train2017/" in r["photo_url"]) != (r["split"] == "train") for r in xrows)
    add("the extra set's test rows come from COCO's val2017 and its train rows from train2017", "pass" if not wrong_home else "FAIL", "%d rows disagree. COCO keeps the two apart, so no photo is on both sides." % wrong_home)
    parts = {}
    for r in xrows:
        parts.setdefault(KX.part_of(r), {}).setdefault(r["eyes"], 0)
        parts[KX.part_of(r)][r["eyes"]] += 1
    add("how the extra set is cut (tools/eval/kinds.py)", "note", "; ".join("%s: %s" % (p_, ", ".join("%s %d" % kv for kv in sorted(parts[p_].items()))) for p_ in ("fit", "tune", "test") if p_ in parts) +
        ". `fit` (two thirds of COCO's train rows by a hash of the id) may be used to fit a kind head, `tune` joins the wildlife tuning photos for the kind decision, `test` is only reported.")
    xid = {r["id"]: r for r in xrows}
    for model in sorted(os.listdir(os.path.join(root, "lab"))):
        for vn in ("coco-kinds", "coco-kinds" + KX.WASM):
            p = os.path.join(root, "lab", model, "images", vn)
            if os.path.exists(p + ".f16.npy"):
                vid = ev.read_ids(p + ".ids.json")
                n = np.load(p + ".f16.npy", mmap_mode="r").shape[0]
                ok = n == len(vid) == len(set(vid)) and all(i in xid for i in vid)
                add("extra-set vectors `%s` of %s line up with the manifest" % (vn, model), "pass" if ok else "FAIL", "%d vectors, %d ids, of %d manifest rows; by part: %s" % (
                    n, len(vid), len(xrows), ", ".join("%s %d" % (p_, sum(KX.part_of(xid[i]) == p_ for i in vid if i in xid)) for p_ in ("fit", "tune", "test"))))
        Ex, exid = ev.load_images(root, model, "coco-kinds")
        if Ex is not None and len(exid) > 1:
            part = np.array([KX.part_of(xid[i]) for i in exid])
            if (part == "test").any() and (part != "test").any():
                mx = np.zeros(int((part == "test").sum()), dtype=np.float32)
                rest = Ex[part != "test"]
                for i in range(0, len(rest), 4000):
                    mx = np.maximum(mx, (Ex[part == "test"] @ rest[i:i + 4000].T).max(1))
                add("extra-set test photos with an almost identical fitting or tuning photo for %s (cosine above 0.995)" % model, "pass" if not (mx > 0.995).any() else "note", "%d of %d" % (int((mx > 0.995).sum()), len(mx)))
else:
    add("the extra set of people, pets, livestock and rooms", "waiting", "`data/extra/coco-kinds/manifest.csv` was not published when the checks ran.")

# facts from each model's card, for the report's decisions
cards = {}
for model in sorted(os.listdir(os.path.join(root, "lab"))):
    card = json.load(open(os.path.join(root, "lab", model, "card.json"), encoding="utf-8"))
    im = card.get("images") or {}
    def shard_mean(block, *path):
        vals = []
        for k, v in (block or {}).items():
            if k.startswith("shard_") and isinstance(v, dict):
                for q in path:
                    v = v.get(q) if isinstance(v, dict) else None
                if v is not None:
                    vals.append(float(v))
        return round(sum(vals) / len(vals), 2) if vals else None
    cards[model] = {"licence": card.get("licence"), "role": card.get("role"), "params": card.get("params"), "ship": card.get("ship"), "ship_bytes": card.get("ship_bytes"), "ship_sha256": card.get("ship_sha256"),
                    "torch_photos_per_second": shard_mean(im.get(ev.EVALSET), "photos_per_second"), "torch_via": (im.get(ev.EVALSET) or {}).get("via"),
                    "wasm_ms_per_photo": shard_mean(im.get(ev.EVALSET + ".wasm-int8-per-channel"), "latency_ms", "mean"), "wasm_via": (im.get(ev.EVALSET + ".wasm-int8-per-channel") or {}).get("via")}

n_fail = sum(c["verdict"] == "FAIL" for c in checks)
fetched = json.load(open(os.path.join(root, "FETCHED.json"))) if os.path.exists(os.path.join(root, "FETCHED.json")) else {}
ev.write_json(a.out, {"made_by": "tools/eval/checks.py", "inputs": {"branches": fetched}, "failed": n_fail, "checks": checks, "cards": cards})
raise SystemExit(1 if n_fail else 0)
