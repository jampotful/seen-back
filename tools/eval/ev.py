"""Shared pieces of the evaluation: reading the published files, the place-and-season prior, ranks, intervals.

Everything here is plain numpy in float32. <root> is the directory made by tools/eval/fetch.py:
<root>/data/ (the published data) and <root>/lab/<model>/ (the published vectors).
"""
import csv, hashlib, json, os, pathlib
import numpy as np

# The order of the laboratory's kind rows (text/kinds.labels.json); "none" means nothing alive.
KINDS = ["cat", "dog", "squirrel", "deer", "rabbit", "hawk", "wader", "bird", "alligator", "reptile", "frog", "bee", "insect", "plant", "person", "other", "none"]
RESAMPLES = 2000          # bootstrap resamples over photos
SEED = 20261011
REGION = "us-fl-alachua"
EVALSET = "alachua-2025"
FREQ_BINS = [("not in the list", 0, 0), ("1 or 2 records", 1, 2), ("3 to 9", 3, 9), ("10 to 49", 10, 49), ("50 to 199", 50, 199), ("200 or more", 200, 10 ** 9)]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def read_manifest(root, name="eval/" + EVALSET):
    with open(os.path.join(root, "data", name, "manifest.csv"), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_species(root):
    with open(os.path.join(root, "data", "regions", REGION, "species.json"), encoding="utf-8") as f:
        return json.load(f)["species"]


def read_ids(path):
    with open(path, encoding="utf-8") as f:
        ids = json.load(f)
    return ids.get("ids") or ids.get("rows") if isinstance(ids, dict) else ids


def unit(a):
    a = np.asarray(a, dtype=np.float32)
    n = np.linalg.norm(a, axis=1, keepdims=True)
    return a / np.maximum(n, 1e-12)


def load_images(root, model, name=EVALSET):
    """Unit image vectors (float32) and their row ids, or (None, None) when the file is not published."""
    p = os.path.join(root, "lab", model, "images", name)
    if not os.path.exists(p + ".f16.npy"):
        return None, None
    return unit(np.load(p + ".f16.npy")), read_ids(p + ".ids.json")


def load_text(root, model, labelset):
    """Unit label rows (float32) and the labels file's list, or (None, None)."""
    p = os.path.join(root, "lab", model, "text", labelset)
    if not os.path.exists(p + ".f16.npy"):
        return None, None
    with open(p + ".labels.json", encoding="utf-8") as f:
        labels = json.load(f)
    return unit(np.load(p + ".f16.npy")), (labels["labels"] if isinstance(labels, dict) else labels)


class EvalSet:
    """The evaluation manifest joined to the species list, in the order of one model's vector rows."""

    def __init__(self, root, ids=None, manifest="eval/" + EVALSET):
        self.rows_all = read_manifest(root, manifest)
        self.species = read_species(root)
        self.key2i = {s["key"]: i for i, s in enumerate(self.species)}
        by = {r["id"]: r for r in self.rows_all}
        self.rows = [by[i] for i in ids] if ids is not None else self.rows_all
        R = self.rows
        self.y = np.array([self.key2i.get(int(r["key"]), -1) if r["key"] else -1 for r in R])
        self.eyes = np.array([r["eyes"] for r in R])
        self.month = np.array([int(r["month"]) - 1 for r in R])
        self.split = np.array([r["split"] for r in R])
        self.test, self.val = self.split == "test", self.split == "val"
        self.sp_eyes = np.array([s["eyes"] for s in self.species])
        self.M = np.array([s["m"] for s in self.species], dtype=np.float64)       # species x 12, records by calendar month
        self.N = np.array([s["n"] for s in self.species], dtype=np.float64)
        self.n_true = np.where(self.y >= 0, self.N[np.maximum(self.y, 0)], 0)      # records before 2025 of each photo's species


def prior_weights(M, N, lam, c):
    """The twelve monthly weights of each species as the page's table carries them: the month's records,
    plus lam times a twelfth of the year's records, plus c."""
    return M + lam * N[:, None] / 12.0 + c


def log_share(W, keep=None, floor=1e-6):
    """log of each species' share of each month's weight (12 x species), as fuse.py's prior_log computes it.
    Species outside `keep` get minus infinity: they are not in the list at all."""
    W = np.where(keep[:, None], W, 0.0) if keep is not None else W
    lp = np.log(np.maximum(W / W.sum(0, keepdims=True), floor)).T.astype(np.float32)
    if keep is not None:
        lp[:, ~keep] = -np.inf
    return lp


def ranks(Z, y):
    """How many rows score above the true row (ties broken by row order, as argmax does); a large number when the
    species is not in the list or has been cut from it."""
    n, S = Z.shape
    ok = y >= 0
    zt = Z[np.arange(n), np.maximum(y, 0)]
    r = (Z > zt[:, None]).sum(1)
    tie = (Z == zt[:, None]) & (np.arange(S)[None, :] < y[:, None])
    r = r + tie.sum(1)
    r = np.where(ok & np.isfinite(zt), r, S + 1)
    return r


_IDX = {}


def boot_index(n, resamples=RESAMPLES, seed=SEED):
    k = (n, resamples, seed)
    if k not in _IDX:
        if len(_IDX) > 6:
            _IDX.clear()
        _IDX[k] = np.random.default_rng(seed + n).integers(0, n, (resamples, n), dtype=np.int32)
    return _IDX[k]


def ci(x):
    """Mean of x over photos with a 95% percentile interval from a bootstrap over photos: [mean, low, high, n]."""
    x = np.asarray(x, dtype=np.float32)
    n = len(x)
    if n == 0:
        return [None, None, None, 0]
    b = x[boot_index(n)].mean(1)
    lo, hi = np.percentile(b, [2.5, 97.5])
    return [round(float(x.mean()), 4), round(float(lo), 4), round(float(hi), 4), int(n)]


def ci_cluster(x, clusters):
    """As ci(), but resampling whole clusters of photos (for example one species on one day), which are not independent of each other."""
    x = np.asarray(x, dtype=np.float64)
    _, inv = np.unique(np.asarray(clusters), return_inverse=True)
    C = int(inv.max()) + 1
    hits, size = np.bincount(inv, weights=x, minlength=C), np.bincount(inv, minlength=C).astype(np.float64)
    counts = np.random.default_rng(SEED + C).multinomial(C, np.full(C, 1.0 / C), size=RESAMPLES)
    b = (counts @ hits) / (counts @ size)
    lo, hi = np.percentile(b, [2.5, 97.5])
    return [round(float(x.mean()), 4), round(float(lo), 4), round(float(hi), 4), int(len(x)), C]


def softmax_rows(Z):
    Z = Z - Z.max(1, keepdims=True)
    np.exp(Z, out=Z)
    Z /= Z.sum(1, keepdims=True)
    return Z


def write_json(path, obj):
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("wrote", path)
