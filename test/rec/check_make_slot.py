#!/usr/bin/env python3
"""A check of test/rec/make_slot.py's names: python3 -I test/rec/check_make_slot.py   (exits 1 on a failure)

Builds a three-species laboratory directory from the stand-in's files, a species list and an inat.json in the documented shape
(docs/CONTRACTS.md), runs make_slot.py on it with and without --inat, and reads the slot back as the page does (tools/fusion/fuse.py).
"""
import json, pathlib, subprocess, sys, tempfile
import numpy as np

here = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(here.parents[1] / "tools" / "fusion"))
from fuse import load_slot  # noqa: E402

standin = here / "models" / "standin"
m = json.loads((standin / "manifest.json").read_text(encoding="utf-8"))
W = m["width"]
rows = [  # the label set as the laboratory writes it: GBIF's names
    {"key": 5228199, "sci": "Gallinula chloropus", "en": "Eurasian Moorhen", "eyes": "wader"},   # GBIF lumps Florida's gallinule into this
    {"key": 2480962, "sci": "Ardea herodias", "en": "", "eyes": "wader"},                       # English name only in the species list
    {"key": 3189866, "sci": "Bidens  alba", "en": "Beggarticks", "eyes": "plant"},              # not in inat.json at all
    {"key": 7777777, "sci": "Lumped species", "en": "Label name", "eyes": "insect"},            # iNaturalist's taxon holds a small share of its records
]
species_list = {"species": [{"key": 2480962, "sci": "Ardea herodias", "en": "Great Blue Heron", "m": [5] * 12}, {"key": 5228199, "sci": "Gallinula chloropus", "en": "Eurasian Moorhen", "m": list(range(12))}]}
inat = {"5228199": {"inat_id": 1, "sci": "Gallinula galeata", "en": "Common Gallinule", "share": 0.98},
        "2480962": {"inat_id": 2, "sci": "Ardea herodias", "en": "", "share": 1.0},
        "7777777": {"inat_id": 3, "sci": "Split species", "en": "Split name", "share": 0.4}}
bad = []
with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp); lab = tmp / "lab"; (lab / "onnx").mkdir(parents=True); (lab / "text").mkdir()
    (lab / "card.json").write_text(json.dumps({"id": "check", "licence": "none", "width": W, "input": {"size": m["vision"]["size"], "mean": m["vision"]["mean"], "std": m["vision"]["std"]}}))
    (lab / "onnx" / "vision.int8.onnx").write_bytes((standin / "vision.int8.onnx").read_bytes())
    k = np.fromfile(standin / "kinds.f16.bin", dtype="<f2").reshape(-1, W)
    np.save(lab / "text" / "kinds.f16.npy", k); (lab / "text" / "kinds.labels.json").write_text(json.dumps({"labels": m["kinds"]["labels"]}))
    np.save(lab / "text" / "sp.f16.npy", k[:len(rows)]); (lab / "text" / "sp.labels.json").write_text(json.dumps({"labels": rows}))
    (tmp / "list.json").write_text(json.dumps(species_list)); (tmp / "inat.json").write_text(json.dumps(inat))
    run = lambda out, *more: subprocess.run([sys.executable, "-I", str(here / "make_slot.py"), str(lab), str(tmp / out), "--species", "sp", "--list", str(tmp / "list.json")] + list(more), check=True, capture_output=True, text=True).stdout
    said = run("with", "--inat", str(tmp / "inat.json")); run("without"); run("share", "--inat", str(tmp / "inat.json"), "--inat-min-share", "0.5")
    t = {name: json.loads((tmp / name / "species.json").read_text(encoding="utf-8")) for name in ("with", "without", "share")}
    want = {
        "with": [["Gallinula galeata", "Common Gallinule", "wader", list(range(12))], ["Ardea herodias", "Great Blue Heron", "wader", [5] * 12], ["Bidens alba", "Beggarticks", "plant", None], ["Split species", "Split name", "insect", None]],
        "without": [["Gallinula chloropus", "Eurasian Moorhen", "wader", list(range(12))], ["Ardea herodias", "Great Blue Heron", "wader", [5] * 12], ["Bidens alba", "Beggarticks", "plant", None], ["Lumped species", "Label name", "insect", None]],
        "share": [["Gallinula galeata", "Common Gallinule", "wader", list(range(12))], ["Ardea herodias", "Great Blue Heron", "wader", [5] * 12], ["Bidens alba", "Beggarticks", "plant", None], ["Lumped species", "Label name", "insect", None]],
    }
    for name in want:
        if t[name]["species"] != want[name]: bad.append((name, t[name]["species"]))
        if t[name]["keys"] != [r["key"] for r in rows]: bad.append((name, "keys", t[name]["keys"]))
    if t["with"]["names"] != "inat" or t["without"]["names"] != "labels": bad.append(("names", t["with"]["names"], t["without"]["names"]))
    slot = load_slot(tmp / "with")                                      # and the slot reads back as the page reads it
    if slot["species"].shape != (len(rows), W) or slot["table"][0][1] != "Common Gallinule": bad.append(("read back", slot["species"].shape))
    print(said.strip().splitlines()[-2])
print("make_slot names:", "ok" if not bad else "FAILED %r" % (bad,))
raise SystemExit(1 if bad else 0)
