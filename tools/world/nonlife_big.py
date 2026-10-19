#!/usr/bin/env python3
"""The pocket probe's verdict applied to the larger model's answers (build 40, tools/world/NONLIFE.md, "The larger model").

For each photo in the sets below it computes (a) the larger model's answer as the page gives it (tools/world/nonlife_real.py big:
models/naturalist, the page's arithmetic in numpy) and (b) the pocket probe's probability of nothing alive (fusion.nonlife of
models/pocket/manifest.json) on the pocket encoder's unit vector of the same photo. Then, for a level `at`, a larger-model answer
that asserts a living kind is turned into "not sure" where the probe is at least `at`.

Sets (test photos only, plus the tuning halves where a level is chosen): the 1,000 reviewed real photos with nothing alive
(pub/nonlife-real, tune and test by hash of id), Alachua 2025 test photos (wild creatures; Alachua's zone), the world test photos that
the laboratory holds BioCLIP 2 vectors for (no zone), and COCO's test cats, dogs and farm animals (filed as `deer`) and rooms.

Usage: python3 -I tools/world/nonlife_big.py ROOT SLOTDIR OUT.json
  ROOT holds b/ (pub/lab-bioclip2-l14), t/ (pub/lab-tinyclip-39m-16 with its wasm vectors), real/ (pub/nonlife-real manifest and
  pocket vectors), ci/runs/nonlife/2-big (BioCLIP 2's vectors of the real photos), da/ (pub/data-alachua eval and extra), dw/ (pub/data-world).
"""
import csv, json, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(REPO, "tools", "species"))
import everyday_build as EB  # noqa: E402


def unit(X):
    X = X.astype(np.float32)
    return X / np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-12)


def rd(path):
    return list(csv.DictReader(open(path, newline="", encoding="utf-8")))


def vec(d, name):
    return unit(np.load(os.path.join(d, name + ".f16.npy"))), json.load(open(os.path.join(d, name + ".ids.json")))


def main():
    root, slotdir, out = sys.argv[1:4]
    man = json.load(open(os.path.join(REPO, "models", "naturalist", "manifest.json")))
    Q, sc, table, pr, zones = EB.read_slot(slotdir, man)
    Qb = Q.astype(np.float32); Qb *= sc[:, None]
    rows = table["species"]
    home = np.zeros(len(rows))
    for r, s in table.get("home") or []:
        home[int(r)] = float(s)
    K = np.frombuffer(open(os.path.join(REPO, "models", "naturalist", man["kinds"]["url"]), "rb").read(), np.float16)
    K = K.reshape(len(man["kinds"]["labels"]), man["width"]).astype(np.float32)
    sl = EB.Slot(Qb, None, rows, pr, zones, man, K, home=home)
    labels = man["kinds"]["labels"]
    pm = json.load(open(os.path.join(REPO, "models", "pocket", "manifest.json")))["fusion"]["nonlife"]
    w, b = np.array(pm["w"], np.float64), float(pm["b"])

    def probe(X):
        return 1 / (1 + np.exp(-(X.astype(np.float64) @ w + b)))

    def big(X, zone):
        k_, kp_, s_ = [], [], []
        for b0 in range(0, len(X), 100):
            Xb = X[b0:b0 + 100]
            sd = sl.dots(Xb)
            L0 = np.stack([sl.logshare0(zone)] * len(Xb))
            top, tp, q = sl.at(sl.split(sd, L0), 1.0)
            kind, kp, sure, named = sl.kinds(Xb, q, top, tp)
            k_.append(kind); kp_.append(kp); s_.append(sure)
            print("  ", b0 + len(Xb), "of", len(X), flush=True)
        kind = np.concatenate(k_)
        return np.array(labels, dtype=object)[kind], np.concatenate(kp_), np.concatenate(s_)

    res = {}

    def add(name, ids, Xb, Xp, zone, extra):
        lab, kp, sure = big(Xb, zone)
        pz = probe(Xp)
        res[name] = {"ids": ids, "kind": [str(x) for x in lab], "p": [round(float(x), 4) for x in kp], "sure": [bool(x) for x in sure],
                     "probe": [round(float(x), 5) for x in pz], **extra}

    # real photos with nothing alive
    rm = {r["id"]: r for r in rd(os.path.join(root, "real", "manifest.csv"))}
    review = {r["id"]: r["verdict"] for r in csv.DictReader(open(os.path.join(REPO, "tools", "world", "nonlife-real-review.csv"), encoding="utf-8"))}
    Xp, idp = unit(np.load(os.path.join(root, "real", "nonlife-made.f16.npy"))), json.load(open(os.path.join(root, "real", "nonlife-made.ids.json")))
    Xb, idb = unit(np.load(os.path.join(root, "ci/runs/nonlife/2-big", "big.f16.npy"))), json.load(open(os.path.join(root, "ci/runs/nonlife/2-big", "big.ids.json")))
    pi = {j: i for i, j in enumerate(idp)}
    keep = [j for j in idb if j in pi and review.get(j) == "keep"]
    bi = {j: i for i, j in enumerate(idb)}
    for zname, zone in (("real", ""), ("real_alachua_zone", "America/New_York")):
        add(zname, keep, Xb[[bi[j] for j in keep]], Xp[[pi[j] for j in keep]], zone,
            {"set": [rm[j]["set"] for j in keep], "family": [rm[j]["family"] for j in keep]})

    # Alachua 2025 test photos (wild creatures; the county's time zone)
    am = {r["id"]: r for r in rd(os.path.join(root, "da", "eval", "alachua-2025", "manifest.csv"))}
    Xt, idt = vec(os.path.join(root, "t", "images"), "alachua-2025.wasm-int8-per-channel")
    Xo, ido = vec(os.path.join(root, "b", "images"), "alachua-2025")
    oi = {j: i for i, j in enumerate(ido)}
    ids = [j for j in idt if j in oi and j in am and am[j]["split"] in ("test", "val")]
    ti = {j: i for i, j in enumerate(idt)}
    add("alachua", ids, Xo[[oi[j] for j in ids]], Xt[[ti[j] for j in ids]], "America/New_York",
        {"set": ["test" if am[j]["split"] == "test" else "tune" for j in ids], "eyes": [am[j]["eyes"] for j in ids]})

    # world photos (iNaturalist, every continent) held in both encoders' vectors
    wm = {r["id"]: r for r in rd(os.path.join(root, "dw", "lab", "world-eval", "manifest.csv"))}
    Xt, idt = vec(os.path.join(root, "t", "images"), "world-eval.wasm-int8-per-channel")
    Xo, ido = vec(os.path.join(root, "b", "images"), "world-species")
    oi = {j: i for i, j in enumerate(ido)}; ti = {j: i for i, j in enumerate(idt)}
    ids = [j for j in idt if j in oi and j in wm]
    print("world photos in both:", len(ids), flush=True)
    add("world", ids, Xo[[oi[j] for j in ids]], Xt[[ti[j] for j in ids]], "",
        {"set": [wm[j]["set"] for j in ids], "group": [wm[j]["group"] for j in ids]})

    # COCO test photos: cats, dogs, farm animals (filed as deer), rooms with nothing alive
    cm = {r["id"]: r for r in rd(os.path.join(root, "da", "extra", "coco-kinds", "manifest.csv"))}
    Xt, idt = vec(os.path.join(root, "t", "images"), "coco-kinds.wasm-int8-per-channel")
    Xo, ido = vec(os.path.join(root, "b", "images"), "coco-kinds")
    oi = {j: i for i, j in enumerate(ido)}; ti = {j: i for i, j in enumerate(idt)}
    ids = [j for j in idt if j in oi and j in cm and cm[j]["split"] == "test" and cm[j]["eyes"] in ("cat", "dog", "deer", "none")]
    add("coco", ids, Xo[[oi[j] for j in ids]], Xt[[ti[j] for j in ids]], "",
        {"eyes": [cm[j]["eyes"] for j in ids]})
    json.dump(res, open(out, "w"))
    print({k: len(v["ids"]) for k, v in res.items()})


if __name__ == "__main__":
    main()
