#!/usr/bin/env python3
"""Make the head files for the larger model on the device (models/naturalist) from a slot that was already scored.

  python3 -I tools/eval/naturalist.py <slot dir> --shipped docs/eval/shipped-<name>.json --out <dir> [--bar 0.98] [--variant docs/eval/variant-<label>.json ...]

The slot's rows, table and kinds file are copied as they are. In the manifest, name_at and offer_at are set to the
levels that tools/eval/shipped.py found on `val` for a named species right at least `bar` of the time (98 in 100 by
default: a name shown to a person should hold), kind_at is kept, and the `vision` block is filled from the laboratory's
parts.json when --parts and --parts-commit are given (otherwise it is left for whoever assembles the slot). Results on the int8 vectors (tools/eval/variant.py) are
recorded in the manifest's `evaluation` block. This script does not write into models/.
"""
import argparse, json, os, shutil

ap = argparse.ArgumentParser()
ap.add_argument("slot")
ap.add_argument("--shipped", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--bar", type=float, default=0.98)
ap.add_argument("--variant", action="append", default=[])
ap.add_argument("--parts", help="the laboratory's parts.json of the int8 file (branch pub/model-bioclip2-l14)")
ap.add_argument("--parts-commit", help="the commit of that branch, for addresses on raw.githubusercontent.com")
ap.add_argument("--repo", default="jampotful/seen-back")
a = ap.parse_args()
man = json.load(open(os.path.join(a.slot, "manifest.json"), encoding="utf-8"))
sh = json.load(open(a.shipped, encoding="utf-8"))
lv = next(l for l in sh["numbers"]["levels"] if abs(l["right_at_least"] - a.bar) < 1e-9)
if lv.get("name_at") is None:
    raise SystemExit("no level reached %g on val for this slot" % a.bar)
os.makedirs(a.out, exist_ok=True)
for n in os.listdir(a.slot):
    if n != "manifest.json":
        shutil.copy2(os.path.join(a.slot, n), os.path.join(a.out, n))
man["fusion"]["name_at"] = lv["name_at"]
man["fusion"]["offer_at"] = lv["offer_at"] if lv.get("offer_at") is not None else 2.0
man["fusion_thresholds_note"] = ("name_at is the level from which a named species was right at least %d times in 100 on val, and offer_at the level from which the three offered species held the right one nine times in ten "
                                 "for the photos left without a name (tools/eval/shipped.py through tools/fusion/fuse.py; 2 means never). On the test photos with the original model's vectors: a species named for %.1f%% and right for %.1f%% of those." % (
                                     round(100 * a.bar), 100 * lv["named"][0], 100 * lv["named_right"][0]))
man["vision"] = {"note": "to be filled from parts.json on the laboratory's branch pub/model-bioclip2-l14 (parts, bytes, sha256, input and output names)", "size": man["vision"].get("size"), "mean": man["vision"].get("mean"), "std": man["vision"].get("std"),
                 "resize": "shortest-bicubic-antialias", "crop": "center"}
if a.parts and a.parts_commit:
    # the image encoder as the laboratory published it, cut into parts that a browser fetches one after another and joins
    pj = json.load(open(a.parts, encoding="utf-8"))
    pre = pj.get("preprocessing", {})
    man["vision"] = {"parts": [{"url": "https://raw.githubusercontent.com/%s/%s/%s" % (a.repo, a.parts_commit, q.get("name") or q.get("url")), "bytes": q["bytes"], "sha256": q["sha256"]} for q in pj["parts"]],
                     "bytes": pj["bytes"], "sha256": pj["sha256"], "from": "pub/model-bioclip2-l14 at %s (recipe %s)" % (a.parts_commit[:12], pj.get("recipe", "")),
                     "input": pj["input"]["name"], "output": pj["output"]["name"], "size": pre.get("size", 224), "mean": pre.get("mean"), "std": pre.get("std"),
                     "resize": "shortest-bicubic-antialias", "crop": "center",
                     "preprocessing_as_the_laboratory_states_it": {"resize": pre.get("resize"), "crop": pre.get("crop")},
                     "note": "The laboratory's crop rounds half the spare pixels to even where the page's `center` rule takes the floor; the two differ by at most one pixel on some photos, which this evaluation has not measured."}
    man["licence"] = pj.get("licence", man.get("licence"))
    man["source"] = pj.get("source_url", man.get("source"))
man["evaluation"]["as_shipped"] = {"from": os.path.basename(a.shipped), "test_photos": sh["numbers"]["test_photos"], "kind_right": sh["numbers"]["kind_right"], "species_top1": sh["numbers"]["species_top1"],
                                   "named": lv["named"], "named_right": lv["named_right"], "offered": lv.get("offered"), "offered_holds_species": lv.get("offered_holds_species")}
man["evaluation"]["int8"] = []
for v in a.variant:
    d = json.load(open(v, encoding="utf-8"))
    man["evaluation"]["int8"].append({k: d[k] for k in ("name", "vectors", "test_photos", "cosine_to_original", "original", "variant", "paired_difference", "same_top_species")})
with open(os.path.join(a.out, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(man, f, indent=1)
    f.write("\n")
print("naturalist-ready head files in", a.out, "| name_at", man["fusion"]["name_at"], "| offer_at", man["fusion"]["offer_at"], "| kind_at", man["fusion"].get("kind_at"))
