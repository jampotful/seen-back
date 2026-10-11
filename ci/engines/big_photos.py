#!/usr/bin/env python3
"""The photos for test/engines/big.js: python3 -I ci/engines/big_photos.py <dir> -> <dir>/photos.json
First test/rec/photos/heron.png (the small model names no species for it, so the page offers the larger model), then four
evaluation photos from the test split (a heron, a grasshopper, a plant, a tree frog), fetched now from iNaturalist's open-data
bucket and never committed; where one cannot be fetched, a photo from test/rec/photos stands in."""
import csv, json, pathlib, shutil, sys, urllib.request
root = pathlib.Path(__file__).resolve().parents[2]; out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
shutil.copyfile(root / "test/rec/photos/heron.png", out / "heron.png")
L = [{"name": "heron.png", "path": str(out / "heron.png"), "type": "image/png", "truth": "test photo (a heron)"}]
rows = {r["id"]: r for r in csv.DictReader(open(root / "data/eval/alachua-2025/manifest.csv"))}
stand = ["garden.jpg", "stripes.png", "odd.png", "dots.png"]
for i, pid in enumerate(["e000008", "e000001", "e000017", "e000153"]):
    r = rows.get(pid); f = out / (pid + ".jpg")
    try:
        req = urllib.request.Request(r["photo_url"], headers={"User-Agent": "seen-back-engines-check"})
        f.write_bytes(urllib.request.urlopen(req, timeout=30).read())
        L.append({"name": pid + ".jpg", "path": str(f), "type": "image/jpeg", "truth": r["sci"] + " | " + r["en"] + " | " + r["eyes"] + " | " + r["obs_url"] + " | " + r["licence"]})
    except Exception as e:
        s = stand[i]; shutil.copyfile(root / "test/rec/photos" / s, out / s)
        L.append({"name": s, "path": str(out / s), "type": "image/png" if s.endswith(".png") else "image/jpeg", "truth": "stand-in, because " + pid + " could not be fetched: " + str(e)[:120]})
# heron.png is not sure of its kind under pocket v2 (0.382 under kind_at 0.5: run engines/35, Safari), so the page asks for the kind and offers
# nothing; the first evaluation photo (a Little Blue Heron: wader 0.76, no species named) raises the offer when it could be fetched
if not L[1]["truth"].startswith("stand-in"): L[0] = dict(L[1])
json.dump(L, open(out / "photos.json", "w"), indent=1)
for x in L: print(x["name"], pathlib.Path(x["path"]).stat().st_size, x["truth"])
