#!/usr/bin/env python3
"""Real photographs with nothing alive in them, for tools/world/nonlife.py (track nonlife2, 18 October 2026).

tools/world/NONLIFE.md found that the pocket head calls drawn coins, stones, stains and rust "this creature" about half the time
with the head alone, and that drawn pictures cannot say how it treats a phone's photo of the same things. This script gathers
real photographs of the non-living subjects people point phones at, from Wikimedia Commons, on a build machine
(.github/workflows/nonlife.yml), keeps the licence and source of every photo, and makes the vectors both models need.

Subcommands:
  manifest OUT          search Wikimedia Commons (the API's full-text search over File: pages) for each family's queries, keep
                        JPEG photographs licensed CC0, CC BY (any version, no SA, NC or ND) or public domain, at least 500
                        pixels wide, whose title, description and categories name no living thing, at most PER_ARTIST from one
                        author in a family, and up to --per a family, taken in turn from the family's queries in search order (each query read
                        until it has given twice --per over the number of queries, or 500 results).
                        Writes OUT/manifest.csv (id, family, set, query, title, source, photo_url, licence, licence_url,
                        artist, width, height) and OUT/summary.json. The set (tune or test) is fixed here by a hash of the id,
                        half and half, before any photo is fetched or measured.
  pocket DIR            the pocket encoder's vectors (models/pocket, onnxruntime on the CPU after the worker's own resize and
                        crop, as tools/world/nonlife_make.py does) of DIR/photos/<id>.jpg: DIR/nonlife-made.f16.npy and
                        DIR/nonlife-made.ids.json, which nonlife.py --made reads beside DIR/manifest.csv.
  bigvec DIR            BioCLIP 2's vectors (the larger model's encoder, tools/lab/lab.py's bioclip2-l14, the original weights
                        in torch) of the same photos: DIR/big.f16.npy and DIR/big.ids.json.
  big DIR --slot S      the larger model's answers on them with the page's arithmetic (fuseWith of src/cam.rec.js for a slot
                        with a kinds head, through tools/species/everyday_build.py's Slot) on the full database as the page
                        downloads it (models/naturalist/manifest.json; the files in S), with no time zone and in Alachua
                        County's: DIR/big.json. It chooses nothing.

Usage (as the workflow runs it):
  python3 -I tools/world/nonlife_real.py manifest work/real [--per 105]
  python3 -I tools/species/fetch_photos.py work/real/manifest.csv work/real/photos --workers 8
  python3 -I tools/world/nonlife_real.py pocket work/real
  python3 -I tools/world/nonlife_real.py bigvec work/real
  python3 -I tools/world/nonlife_real.py big work/real --slot work/slot
"""
import argparse
import csv
import hashlib
import html
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
API = "https://commons.wikimedia.org/w/api.php"
UA = "seen-back-nonlife/1 (+https://github.com/jampotful/seen-back; research photo set, one request at a time)"
PER_ARTIST = 6
COLUMNS = ["id", "family", "set", "query", "title", "source", "photo_url", "licence", "licence_url", "artist", "width", "height"]

# The families of tools/world/NONLIFE.md's drawn photos that real photos can stand for, and the other subjects people point a
# phone at. Each query is CirrusSearch syntax; a leading minus excludes a word.
FAMILIES = {
    "coins": ["pile of coins", "coins on table", "loose change coins", "old coins", "coins heap"],
    "stones": ["pebbles", "pebble beach stones", "gravel", "river stones", "rocks closeup"],
    "rust": ["rust texture", "rusty metal", "rusted iron", "rusty steel surface"],
    "stains": ["stain on fabric -glass", "coffee stain -glass", "stain on carpet -glass", "water stain ceiling -glass",
               "oil stain concrete -glass", "stain on wall -glass"],
    "bricks": ["brick wall", "brickwork", "red bricks", "brick pavement"],
    "food": ["food on plate", "plate of food", "dish served on plate", "meal on a plate"],
    "toys": ["toy cars", "lego bricks", "toy blocks", "plastic toys", "toy train"],
    "clothing": ["folded clothes", "clothes on hanger", "pile of clothes", "pair of shoes", "knitted sweater"],
    "furniture": ["chair", "sofa living room", "wooden table furniture", "bookshelf", "bedroom bed"],
    "screens": ["computer monitor screen", "television screen", "smartphone screen", "laptop screen"],
    "cars": ["parked car", "car parked street", "automobile"],
    "signs": ["street sign", "road sign", "shop sign", "traffic sign"],
    "sky": ["clouds sky", "cumulus clouds", "blue sky", "overcast sky", "cirrus clouds"],
    "floors": ["floor tiles", "wooden floor", "carpet floor", "concrete floor", "linoleum floor"],
    "walls": ["white wall", "concrete wall texture", "plaster wall", "painted wall", "stone wall"],
}

# A photo whose title, description or categories name one of these is left out: a living thing (or a likeness of one, or its
# remains) may be in it, and the set is meant to hold nothing alive. Coins keep their portraits: a coin is the case at issue.
LIVING = re.compile(r"\b(" + "|".join([
    "birds?", "dogs?", "cats?", "kittens?", "pupp(y|ies)", "horses?", "cows?", "cattle", "sheep", "goats?", "pigs?", "chickens?",
    "ducks?", "geese", "goose", "pigeons?", "gulls?", "insects?", "butterfl(y|ies)", "moths?", "bees?", "wasps?", "ants?", "beetles?",
    "flies", "spiders?", "fish(es)?", "animals?", "pets?", "wildlife", "zoo", "people", "persons?", "man", "men", "woman", "women",
    "girls?", "boys?", "child(ren)?", "kids?", "bab(y|ies)", "portraits?", "selfie", "faces?", "hands?", "players?", "crowds?",
    "tourists?", "visitors?", "workers?", "family", "flowers?", "trees?", "plants?", "gardens?", "leaf", "leaves", "moss(es)?",
    "lichens?", "fung(us|i)", "mushrooms?", "snails?", "lizards?", "frogs?", "squirrels?", "deer", "rabbits?", "grass", "forests?",
    "woods", "algae", "seaweed", "mou?ld", "vegetation", "ivy", "crabs?", "shells?", "corals?", "fossils?", "bones?", "skulls?",
    "feathers?", "nests?", "statues?", "sculptures?", "figurines?", "dolls?", "plush", "teddy", "stuffed", "dinosaurs?",
    "paintings?", "drawings?", "illustrations?", "engravings?", "diagrams?", "maps?", "logos?", "icons?", "screenshots?",
    "jesus", "saints?", "madonna", "mural", "graffiti",
]) + r")\b", re.I)


def unit_id(set_of):
    return "tune" if int(hashlib.sha256(("nonlife|" + set_of).encode()).hexdigest()[:8], 16) % 2 == 0 else "test"


def plain(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


def licence_ok(lic, short):
    lic, short = (lic or "").strip().lower(), (short or "").strip().lower()
    if lic in ("cc0", "pd", "cc-pd", "cc-pd-mark", "public domain") or lic.startswith("pd-") or lic.startswith("pd "):
        return True
    if re.fullmatch(r"cc-by-\d(\.\d)?", lic):
        return True
    return not lic and (short.startswith("public domain") or short in ("cc0", "pd"))


def search(sess, q, offset):
    p = {"action": "query", "format": "json", "formatversion": "2", "generator": "search",
         "gsrsearch": q + " filemime:image/jpeg", "gsrnamespace": "6", "gsrlimit": "50", "gsroffset": str(offset),
         "prop": "imageinfo", "iiprop": "url|size|mime|extmetadata", "iiurlwidth": "500",
         "iiextmetadatafilter": "License|LicenseShortName|LicenseUrl|Artist|ImageDescription|Categories"}
    for k in range(6):
        try:
            r = sess.get(API, params=p, timeout=60)
            if r.status_code == 200:
                return r.json()
            print("  HTTP %d for %r at %d" % (r.status_code, q, offset), flush=True)
        except Exception as e:  # keep trying: one bad answer should not lose a family
            print("  %s for %r at %d" % (type(e).__name__, q, offset), flush=True)
        time.sleep(2 + 3 * k)
    return {}


def manifest(a):
    import requests
    os.makedirs(a.out, exist_ok=True)
    sess = requests.Session(); sess.headers.update({"User-Agent": UA})
    seen, rows, why = set(), [], Counter()
    for fam, queries in FAMILIES.items():
        pools, want = {}, -(-2 * a.per // len(queries))
        for q in queries:
            pool, off = [], 0
            while off is not None and off < a.depth and len(pool) < want:
                d = search(sess, q, off)
                pages = sorted((d.get("query") or {}).get("pages") or [], key=lambda x: x.get("index", 0))
                for pg in pages:
                    ii = (pg.get("imageinfo") or [{}])[0]
                    em = {k: (v or {}).get("value", "") for k, v in (ii.get("extmetadata") or {}).items()}
                    if ii.get("mime") != "image/jpeg":
                        why["not jpeg"] += 1; continue
                    if (ii.get("width") or 0) < 500 or (ii.get("height") or 0) < 300 or not ii.get("thumburl"):
                        why["too small"] += 1; continue
                    if not licence_ok(em.get("License"), em.get("LicenseShortName")):
                        why["licence"] += 1; continue
                    text = " ".join([pg.get("title", ""), plain(em.get("ImageDescription")), (em.get("Categories") or "").replace("|", " ")])
                    if LIVING.search(text.replace("_", " ")):
                        why["names a living thing"] += 1; continue
                    pool.append({"pageid": pg["pageid"], "title": pg.get("title", ""), "source": ii.get("descriptionurl", ""),
                                 "photo_url": ii["thumburl"], "licence": em.get("LicenseShortName") or em.get("License"),
                                 "licence_url": em.get("LicenseUrl", ""), "artist": plain(em.get("Artist"))[:200],
                                 "width": ii.get("thumbwidth"), "height": ii.get("thumbheight"), "query": q})
                off = (d.get("continue") or {}).get("gsroffset")
                time.sleep(0.5)
            pools[q] = pool
            print("%s / %r: %d usable" % (fam, q, len(pool)), flush=True)
        took, per_artist, k = [], Counter(), 0
        while len(took) < a.per and any(k < len(p) for p in pools.values()):
            for q in queries:
                if k < len(pools[q]) and len(took) < a.per:
                    r = pools[q][k]
                    art = r["artist"].lower() or r["source"]
                    if r["pageid"] in seen or per_artist[art] >= PER_ARTIST:
                        continue
                    seen.add(r["pageid"]); per_artist[art] += 1
                    pid = "c%d" % r["pageid"]
                    took.append(dict(r, id=pid, family=fam, set=unit_id(pid)))
            k += 1
        rows += took
        print("%s: %d taken" % (fam, len(took)), flush=True)
    with open(os.path.join(a.out, "manifest.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    summ = {"photos": len(rows), "by_family": dict(Counter(r["family"] for r in rows)), "by_set": dict(Counter(r["set"] for r in rows)),
            "by_licence": dict(Counter(r["licence"] for r in rows).most_common()), "left_out": dict(why), "per_artist": PER_ARTIST,
            "source": "Wikimedia Commons, the API's search over File: pages (%s)" % API}
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    print(json.dumps(summ, indent=1))


def read_manifest(d):
    return list(csv.DictReader(open(os.path.join(d, "manifest.csv"), encoding="utf-8")))


def pocket(a):
    import numpy as np
    import onnxruntime as ort
    from PIL import Image
    sys.path.insert(0, HERE)
    from nonlife_make import prepare
    man = json.load(open(os.path.join(ROOT, "models", "pocket", "manifest.json")))
    sess = ort.InferenceSession(os.path.join(ROOT, "models", "pocket", man["vision"]["url"]), providers=["CPUExecutionProvider"])
    ids, vecs, bad = [], [], []
    for r in read_manifest(a.dir):
        p = os.path.join(a.dir, "photos", r["id"] + ".jpg")
        try:
            im = Image.open(p).convert("RGB")
        except Exception as e:
            bad.append([r["id"], type(e).__name__]); continue
        e = sess.run([man["vision"]["output"]], {man["vision"]["input"]: prepare(im, man)})[0][0].astype(np.float64)
        vecs.append(e / (np.linalg.norm(e) or 1)); ids.append(r["id"])
    np.save(os.path.join(a.dir, "nonlife-made.f16.npy"), np.array(vecs, dtype=np.float16))
    json.dump(ids, open(os.path.join(a.dir, "nonlife-made.ids.json"), "w"))
    json.dump(bad, open(os.path.join(a.dir, "pocket-missing.json"), "w"))
    print("pocket vectors: %d photos, %d missing or unreadable" % (len(ids), len(bad)))


def bigvec(a):
    import numpy as np
    sys.path.insert(0, os.path.join(ROOT, "tools", "lab"))
    import lab
    rows = read_manifest(a.dir)
    m = lab.load(lab.model_entry("bioclip2-l14"))
    ids, X, bad, el = lab.embed_rows(m, rows, os.path.join(a.dir, "photos"))
    np.save(os.path.join(a.dir, "big.f16.npy"), X.astype(np.float16))
    json.dump(ids, open(os.path.join(a.dir, "big.ids.json"), "w"))
    print("BioCLIP 2 vectors: %d photos, %d missing or unreadable, %.0f s" % (len(ids), len(bad), el))


def big(a):
    import numpy as np
    sys.path.insert(0, os.path.join(ROOT, "tools", "species"))
    import everyday_build as EB
    mpath = os.path.join(ROOT, "models", "naturalist", "manifest.json")
    man = json.load(open(mpath))
    Q, sc, table, pr, zones = EB.read_slot(a.slot, man)
    Qb = Q.astype(np.float32); Qb *= sc[:, None]
    rows = table["species"]
    home = np.zeros(len(rows))
    for r, s in table.get("home") or []:
        home[int(r)] = float(s)
    K = np.frombuffer(open(os.path.join(os.path.dirname(mpath), man["kinds"]["url"]), "rb").read(), np.float16)
    K = K.reshape(len(man["kinds"]["labels"]), man["width"]).astype(np.float32)
    sl = EB.Slot(Qb, None, rows, pr, zones, man, K, home=home)
    X = np.load(os.path.join(a.dir, "big.f16.npy")).astype(np.float32)
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    ids = json.load(open(os.path.join(a.dir, "big.ids.json")))
    meta = {r["id"]: r for r in read_manifest(a.dir)}
    labels = man["kinds"]["labels"]
    out = {"slot": "models/naturalist (the files its manifest names)", "kind_at": man["fusion"]["kind_at"], "photos": len(ids), "conditions": {}}
    detail = []
    for cond, zone in (("no zone", ""), ("Alachua's zone", "America/New_York")):
        kinds, kps, sures, tops, tps = [], [], [], [], []
        for b0 in range(0, len(ids), 100):
            Xb = X[b0:b0 + 100]
            sd = sl.dots(Xb)
            L0 = np.stack([sl.logshare0(zone)] * len(Xb))
            top, tp, q = sl.at(sl.split(sd, L0), 1.0)
            kind, kp, sure, named = sl.kinds(Xb, q, top, tp)
            kinds.append(kind); kps.append(kp); sures.append(sure); tops.append(top); tps.append(tp)
        kind, kp, sure, top, tp = (np.concatenate(v) for v in (kinds, kps, sures, tops, tps))
        lab_of = np.array(labels, dtype=object)[kind]
        living = sure & ~np.isin(lab_of, ["none", "person"])
        res = {}
        for part in ("tune", "test", "all"):
            sel = np.array([part == "all" or meta[i]["set"] == part for i in ids])
            res[part] = {"photos": int(sel.sum()), "living_kind": int(living[sel].sum()), "share": round(float(living[sel].mean()), 4),
                         "none_sure": int((sure & (lab_of == "none"))[sel].sum()), "not_sure": int((~sure)[sel].sum()),
                         "kinds": dict(Counter(lab_of[sel & living]).most_common())}
        fam = defaultdict(lambda: [0, 0])
        for i, x in enumerate(ids):
            fam[meta[x]["family"]][0] += 1; fam[meta[x]["family"]][1] += int(living[i])
        res["by_family"] = {f: {"photos": n, "living_kind": k} for f, (n, k) in sorted(fam.items())}
        out["conditions"][cond] = res
        for i, x in enumerate(ids):
            if cond == "no zone":
                detail.append({"id": x, "family": meta[x]["family"], "set": meta[x]["set"]})
            detail[i][cond] = [labels[kind[i]], round(float(kp[i]), 3), bool(sure[i]), rows[top[i]][1] or rows[top[i]][0], round(float(tp[i]), 3)]
        print(cond, json.dumps(res["all"]), flush=True)
    json.dump(out, open(os.path.join(a.dir, "big.json"), "w"), indent=1)
    with open(os.path.join(a.dir, "big-photos.jsonl"), "w") as f:
        for d in detail:
            f.write(json.dumps(d) + "\n")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    m = sp.add_parser("manifest"); m.add_argument("out"); m.add_argument("--per", type=int, default=105); m.add_argument("--depth", type=int, default=500)
    p = sp.add_parser("pocket"); p.add_argument("dir")
    v = sp.add_parser("bigvec"); v.add_argument("dir")
    b = sp.add_parser("big"); b.add_argument("dir"); b.add_argument("--slot", required=True)
    a = ap.parse_args()
    {"manifest": manifest, "pocket": pocket, "bigvec": bigvec, "big": big}[a.cmd](a)


if __name__ == "__main__":
    main()
