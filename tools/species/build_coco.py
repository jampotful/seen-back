#!/usr/bin/env python3
"""Build data/extra/coco-kinds/manifest.csv and its SUMMARY.md from COCO 2017's instance annotations.

The kind-of-eye head is trained on local wildlife photos, which hold no people, no rooms and almost no house cats,
dogs or livestock. This set adds those kinds, and photos with nothing alive in them, from COCO 2017 (format:
docs/CONTRACTS.md, "Photos for kinds the wildlife records lack"). COCO's train annotations give the `train` rows and
its val annotations the `test` rows, so no image is in both.

Rules, applied to each image's instance annotations ("largest" compares the annotated `area` of annotations that are
not crowd regions; "annotated" counts every annotation, crowd regions included):
- person: the largest annotation is a person covering at least a fifth of the image, and no animal is annotated.
- cat, dog: the largest annotation is a cat (a dog).
- deer (the app's grazing-animal eyes): the largest annotation is a horse, a cow or a sheep. The three are taken in
  turn by rank (horse, cow, sheep, horse, ...), so each gets an even share while it lasts.
- none: at least one annotation, no person, no animal and no potted plant annotated, and every annotation in COCO's
  indoor supercategories (furniture, electronic, appliance, kitchen, food, indoor), so that no lawn or tree stands
  in the background being called nothing.
Within each kind and split, images are ranked by sha256("<seed>|<image id>") and the first ones are taken, so the
same annotations and seed give the same choice. Rows are ordered train first, then by that rank, so kinds are mixed
and any prefix of a split is a fair sample of it.

Columns: `id` is "c" and the six-digit COCO image id; `gbif_id`, `key`, `sci`, `en` and the taxonomy columns are
empty; `eyes` holds the kind or `none`; `obs_url` is the image's Flickr address as COCO gives it (else its page on
cocodataset.org); `photo_url` is COCO's own copy; `date` and `month` come from COCO's `date_captured`; `licence` is
read from the annotation file's licence table. Nothing is downloaded but the annotations; no image is redistributed.

Usage: python3 tools/species/build_coco.py --zip annotations_trainval2017.zip [--out data/extra/coco-kinds] [--scheme https]
"""
import argparse
import csv
import datetime
import hashlib
import io
import json
import statistics
import sys
import time
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_eval import COLUMNS, rank_of  # noqa: E402

KINDS = ("person", "cat", "dog", "deer", "none")
WANT = {"person": (2000, 400), "cat": (1500, 150), "dog": (1500, 150), "deer": (1500, 200), "none": (2500, 500)}
GRAZERS = ("horse", "cow", "sheep")
INDOOR = {"furniture", "electronic", "appliance", "kitchen", "food", "indoor"}
PERSON_SHARE = 0.2
SPLITS = (("train", "train2017"), ("test", "val2017"))
OTHER_LICENCES = {"flickr.com/commons/usage": "no-known-copyright-restrictions",
                  "usa.gov/copyright": "us-government-work"}


def licence_id(url, name):
    """CC-BY-NC-SA-2.0 style for Creative Commons addresses; a short slug for COCO's two other licences."""
    import re
    m = re.search(r"creativecommons\.org/licenses/([a-z-]+)/([0-9.]+)", url or "", re.I)
    if m:
        return "CC-%s-%s" % (m.group(1).upper(), m.group(2))
    for frag, slug in OTHER_LICENCES.items():
        if frag in (url or ""):
            return slug
    return (name or url or "unknown").strip()


def classify(img, anns, cats):
    """(kind or None, reason, detail) for one image; detail is the grazing animal's name for `deer`."""
    if not anns:
        return None, "no annotations", ""
    names = {cats[a["category_id"]]["name"] for a in anns}
    supers = {cats[a["category_id"]]["supercategory"] for a in anns}
    solid = [a for a in anns if not a.get("iscrowd")]
    top = max(solid, key=lambda a: (a["area"], -a["id"])) if solid else None
    tname = cats[top["category_id"]]["name"] if top else ""
    share = top["area"] / float(img["width"] * img["height"]) if top else 0.0
    if tname == "person":
        if "animal" in supers:
            return None, "person largest, an animal annotated", ""
        if share < PERSON_SHARE:
            return None, "person largest, under a fifth of the image", ""
        return "person", "", ""
    if tname in ("cat", "dog"):
        return tname, "", ""
    if tname in GRAZERS:
        return "deer", "", tname
    if "person" in supers or "animal" in supers:
        return None, "a person or an animal annotated, not the largest of the wanted kinds", ""
    if "potted plant" in names:
        return None, "potted plant annotated", ""
    if not supers <= INDOOR:
        return None, "an outdoor or vehicle annotation (%s)" % ",".join(sorted(supers - INDOOR)), ""
    return "none", "", ""


def take_in_turn(groups, n):
    """Take n items from ranked lists, one from each in turn, while each lasts."""
    out, i = [], 0
    while len(out) < n and any(i < len(g) for g in groups):
        for g in groups:
            if i < len(g) and len(out) < n:
                out.append(g[i])
        i += 1
    return out


def load(zf, split_dir):
    with zf.open("annotations/instances_%s.json" % split_dir) as f:
        return json.load(io.TextIOWrapper(f, encoding="utf-8"))


def pctl(xs, q):
    if not xs:
        return float("nan")
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--zip", required=True, help="annotations_trainval2017.zip")
    ap.add_argument("--out", default="data/extra/coco-kinds")
    ap.add_argument("--seed", default="seen-back/coco-kinds/v1")
    ap.add_argument("--scheme", default="http", choices=("http", "https"), help="scheme of photo_url (COCO gives http)")
    ap.add_argument("--zip-url", default="http://images.cocodataset.org/annotations/annotations_trainval2017.zip")
    args = ap.parse_args()
    t0 = time.time()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    h = hashlib.sha256()
    with open(args.zip, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    zsha, zsize = h.hexdigest(), Path(args.zip).stat().st_size
    rows, problems, shortfalls, largest = [], [], [], {}
    pools, reasons, lic_tables, shares, deer_mix, chosen_mix = {}, {}, {}, defaultdict(list), {}, {}
    with zipfile.ZipFile(args.zip) as zf:
        for split, sdir in SPLITS:
            d = load(zf, sdir)
            cats = {c["id"]: c for c in d["categories"]}
            lic = {l["id"]: l for l in d["licenses"]}
            lic_tables[split] = lic
            by_img = defaultdict(list)
            for a in d["annotations"]:
                by_img[a["image_id"]].append(a)
            pool, why, grazer = defaultdict(list), Counter(), {}
            for img in d["images"]:
                kind, reason, detail = classify(img, by_img.get(img["id"], []), cats)
                if kind:
                    pool[kind].append(img)
                    if detail:
                        grazer[img["id"]] = detail
                else:
                    why[reason] += 1
            pools[split] = {k: len(v) for k, v in pool.items()}
            reasons[split] = why
            deer_mix[split] = Counter(grazer.values())
            idx = 0 if split == "train" else 1
            for kind in KINDS:
                ranked = sorted(pool[kind], key=lambda im: rank_of(args.seed, im["id"]))
                want = WANT[kind][idx]
                if kind == "deer":
                    groups = [[im for im in ranked if grazer[im["id"]] == g] for g in GRAZERS]
                    pick = take_in_turn(groups, want)
                    chosen_mix[split] = Counter(grazer[im["id"]] for im in pick)
                else:
                    pick = ranked[:want]
                if len(pick) < want:
                    note = "%s %s: %d wanted, %d there are" % (split, kind, want, len(pick))
                    shortfalls.append(note)     # reported in the summary; the set is still published
                for im in pick:
                    anns = [a for a in by_img[im["id"]] if not a.get("iscrowd")]
                    top_name, top_share = "", 0.0
                    if anns:
                        top = max(anns, key=lambda a: (a["area"], -a["id"]))
                        top_name, top_share = cats[top["category_id"]]["name"], top["area"] / float(im["width"] * im["height"])
                        shares[(split, kind)].append(top_share)
                    largest["c%06d" % im["id"]] = (top_name, top_share, len(by_img[im["id"]]),
                                                   sum(1 for a in by_img[im["id"]] if a.get("iscrowd")))
                    l = lic.get(im.get("license"), {})
                    date = (im.get("date_captured") or "")[:10]
                    photo = im["coco_url"]
                    if args.scheme == "https" and photo.startswith("http://"):
                        photo = "https://" + photo[len("http://"):]
                    rows.append({
                        "id": "c%06d" % im["id"], "gbif_id": "", "key": "", "sci": "", "en": "",
                        "obs_url": im.get("flickr_url") or "https://cocodataset.org/#explore?id=%d" % im["id"],
                        "kingdom": "", "class": "", "order": "", "family": "", "eyes": kind,
                        "date": date, "month": int(date[5:7]) if len(date) >= 7 else "",
                        "photo_url": photo, "licence": licence_id(l.get("url"), l.get("name")), "split": split,
                        "_rank": rank_of(args.seed, im["id"]), "_dir": sdir,
                    })
            del d, by_img
    rows.sort(key=lambda r: (r["split"] != "train", r["_rank"]))
    # ---- checks
    checks = []
    ids = [r["id"] for r in rows]
    if len(set(ids)) != len(ids):
        problems.append("duplicate ids")
    if len({r["photo_url"] for r in rows}) != len(rows):
        problems.append("duplicate photo addresses")
    wrong = [r["id"] for r in rows if ("/%s/" % r["_dir"]) not in r["photo_url"]]
    if wrong:
        problems.append("%d rows whose photo is not in their split's folder" % len(wrong))
    tr = {r["id"] for r in rows if r["split"] == "train"}
    te = {r["id"] for r in rows if r["split"] == "test"}
    checks.append("ids unique: %s; photo addresses unique: %s; images in both splits: %d; rows whose photo is outside "
                  "their split's folder: %d" % (len(set(ids)) == len(ids), len({r['photo_url'] for r in rows}) == len(rows),
                                                len(tr & te), len(wrong)))
    with open(out / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(COLUMNS)
        for r in rows:
            w.writerow([r[c] for c in COLUMNS])
    with open(out / "largest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["id", "split", "eyes", "largest", "largest_share", "annotations", "crowd_regions"])
        for r in rows:
            nm, sh, na, nc = largest[r["id"]]
            w.writerow([r["id"], r["split"], r["eyes"], nm, "%.4f" % sh, na, nc])
    # ---- summary
    got = Counter((r["split"], r["eyes"]) for r in rows)
    L = ["# Extra photos: kinds the wildlife records lack (COCO 2017)", "",
         "Built by `tools/species/build_coco.py` on %s (UTC) from `%s` (%d bytes, sha256 `%s`), seed `%s`. %d rows: "
         "%d train (from COCO's train2017 annotations), %d test (from val2017)." % (
             datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M"), args.zip_url, zsize, zsha, args.seed,
             len(rows), len(tr), len(te)), "",
         "The manifest lists addresses only. Photos are downloaded when a laboratory or evaluation run needs them and "
         "are never committed or republished.", "",
         "`largest.csv` (same ids, same order) gives each image's largest annotation, the share of the image it covers, "
         "and how many annotations the image has, so a training run can leave out images whose subject is small "
         "(the rules set no minimum size for cats, dogs and grazing animals) without rebuilding this set.", "",
         "## Rules", ""]
    L += ["- `person`: the largest annotation (by annotated area, crowd regions left out) is a person covering at least "
          "a fifth of the image, and no animal is annotated.",
          "- `cat`, `dog`: the largest annotation is a cat (a dog).",
          "- `deer`: the largest annotation is a horse, a cow or a sheep; the three are taken in turn by rank.",
          "- `none`: at least one annotation; no person, animal or potted plant annotated; every annotation in COCO's "
          "indoor supercategories (furniture, electronic, appliance, kitchen, food, indoor).",
          "- Each kind and split is ranked by sha256(seed|image id) and the first images are taken.", "",
          "## Counts", "", "| kind | eligible in train2017 | train rows | wanted | eligible in val2017 | test rows | wanted |",
          "|---|---:|---:|---:|---:|---:|---:|"]
    for k in KINDS:
        L.append("| %s | %d | %d | %d | %d | %d | %d |" % (k, pools["train"].get(k, 0), got[("train", k)], WANT[k][0],
                                                      pools["test"].get(k, 0), got[("test", k)], WANT[k][1]))
    if shortfalls:
        L += ["", "Fewer than wanted, so all there are: " + "; ".join(shortfalls) + "."]
    dates = sorted(r["date"] for r in rows if r["date"])
    if dates:
        L += ["", "`date` and `month` are COCO's `date_captured`, which runs only from %s to %s here: it is not when the "
              "photos were taken, so no month prior applies to these rows." % (dates[0], dates[-1])]
    L += ["", "Grazing animals among the `deer` rows: train %s; test %s (eligible: train %s; test %s)." % (
        dict(chosen_mix.get("train", {})), dict(chosen_mix.get("test", {})), dict(deer_mix["train"]), dict(deer_mix["test"])), "",
        "## How much of the image the largest annotation covers", "",
        "| split | kind | 10th percentile | median | 90th percentile |", "|---|---|---:|---:|---:|"]
    for split, _ in SPLITS:
        for k in KINDS:
            xs = shares.get((split, k), [])
            if xs:
                L.append("| %s | %s | %.2f | %.2f | %.2f |" % (split, k, pctl(xs, 0.1), statistics.median(xs), pctl(xs, 0.9)))
    L += ["", "## Licences", "", "The licence of each image as COCO's annotation file gives it (the `licenses` table, "
          "identical in both files: %s)." % (lic_tables["train"] == lic_tables["test"]), "",
          "| COCO id | licence column | name in COCO's table | address | train rows | test rows |", "|---:|---|---|---|---:|---:|"]
    lc = Counter((r["split"], r["licence"]) for r in rows)
    for lid, l in sorted(lic_tables["train"].items()):
        code = licence_id(l.get("url"), l.get("name"))
        L.append("| %d | %s | %s | %s | %d | %d |" % (lid, code, l.get("name"), l.get("url"), lc[("train", code)], lc[("test", code)]))
    L += ["", "What COCO's terms of use say (the page's source, `dataset/termsofuse.htm` in "
          "github.com/cocodataset/cocodataset.github.io, read 2026-10-11 at commit 5e1c4da7): \"The annotations in this "
          "dataset along with this website belong to the COCO Consortium and are licensed under a Creative Commons "
          "Attribution 4.0 License.\" \"The COCO Consortium does not own the copyright of the images. Use of the images "
          "must abide by the Flickr Terms of Use. The users of the images accept full responsibility for the use of the "
          "dataset, including but not limited to the use of any copies of copyrighted images that they may create from "
          "the dataset.\"", "",
          "What this project does with them: it downloads the photos on build machines to compute vectors for training "
          "and testing the kind-of-eye head, and redistributes no photo; the manifest carries each photo's licence and "
          "Flickr address, which lead to the attribution. Most rows carry a NonCommercial licence and some a NoDerivs "
          "licence. Whether a model trained on such photos may ship is not settled by those licences' text; the "
          "`licence` column lets a training run keep only CC-BY-2.0, CC-BY-SA-2.0 and "
          "no-known-copyright-restrictions rows if the owner decides so (train rows of those licences here: %d)." % (
              sum(1 for r in rows if r["split"] == "train" and r["licence"] in ("CC-BY-2.0", "CC-BY-SA-2.0", "no-known-copyright-restrictions"))),
          ]
    L += ["", "## Checks", ""] + ["- " + c for c in checks]
    L += ["", "## Images left out (train2017 and val2017 together)", "", "| reason | images |", "|---|---:|"]
    left = reasons["train"] + reasons["test"]
    for why, n in left.most_common(12):
        L.append("| %s | %d |" % (why, n))
    if problems:
        L += ["", "## Problems", ""] + ["- " + p for p in problems]
    (out / "SUMMARY.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("wrote %s: %d rows %s; %.0fs" % (out / "manifest.csv", len(rows), dict(sorted(got.items())), time.time() - t0), flush=True)
    if problems:
        print("PROBLEMS:\n  " + "\n  ".join(problems), flush=True)
        sys.exit(2)


if __name__ == "__main__":
    main()
