"""The kind decision with people, pets, livestock and rooms in the picture.

The wildlife photos hold no people, no photos with nothing alive in them and almost no pets, so a kind decision tuned
on them alone has never been asked about a person or an empty room. The extra set data/extra/coco-kinds (COCO 2017:
`person`, `cat`, `dog`, grazing animals filed under `deer`, and `none`) fills that gap:

  its `train` rows are cut in two by a hash of the row id: two thirds may be used to fit a kind head ("fit"), and
    one third joins the wildlife tuning photos whenever a setting of the kind decision is chosen ("tune");
  its `test` rows are reported beside the wildlife `test` photos and are used for nothing else.

A COCO row carries no date that means anything for a season (the manifest's date is the day COCO collected the file),
so each row is given a calendar month by a hash of its id, and the prior is averaged over the year that way.

The number a kind decision is tuned on is the mean of two shares: the share of wildlife tuning photos whose kind is
right, and the mean over the extra set's kinds of the share right for that kind. Nobody knows how many of the photos a
phone meets are of people or of rooms, so the two sets count the same and neither can be bought with the other.
"""
import hashlib, os
import numpy as np

import ev

EXTRA = "coco-kinds"
WASM = ".wasm-int8-per-channel"
EXTRA_KINDS = ("person", "none", "cat", "dog", "deer")
BARS = (0.90, 0.95, 0.98)          # an asserted kind has to be right at least this often on the tuning photos
BAR = 0.95                         # the bar whose level becomes fusion.kind_at
GRID = np.round(np.arange(0.20, 0.9951, 0.01), 2)


def _h(s):
    return int(hashlib.sha256(s.encode()).hexdigest()[:8], 16)


def part_of(row):
    """`fit`, `tune` or `test` for a row of the extra set."""
    if row["split"] == "test":
        return "test"
    return "fit" if _h(row["id"]) % 3 < 2 else "tune"


def month_of(row_id):
    return _h("month|" + row_id) % 12


def load(root, model, want_wasm=False):
    """The extra set's vectors for one model, cut into fit, tune and test, or None when they are not published.
    With want_wasm the test rows come from the vectors the browser's WASM runtime computed, when those exist."""
    man = os.path.join(root, "data", "extra", EXTRA, "manifest.csv")
    if not os.path.exists(man):
        return None
    X, ids = ev.load_images(root, model, EXTRA)
    if X is None:
        return None
    by = {r["id"]: r for r in ev.read_manifest(root, "extra/" + EXTRA)}

    def cut(X_, ids_, name):
        rows = [by[i] for i in ids_]
        part = np.array([part_of(r) for r in rows])
        eyes = np.array([r["eyes"] for r in rows])
        month = np.array([month_of(i) for i in ids_])
        return {p: {"X": X_[part == p], "eyes": eyes[part == p], "month": month[part == p], "ids": [i for i, q in zip(ids_, part) if q == p], "vectors": "images/" + name} for p in ("fit", "tune", "test")}

    out = cut(X, ids, EXTRA)
    out.update(set=EXTRA, rows_in_manifest=len(by), rows_with_vectors=len(ids))
    if want_wasm:
        Xw, idw = ev.load_images(root, model, EXTRA + WASM)
        if Xw is not None:
            w = cut(Xw, idw, EXTRA + WASM)["test"]
            if len(w["ids"]):
                out["test_original"] = out["test"]
                out["test"] = w
    return out


def balanced(right_w, right_x=None, eyes_x=None):
    """The tuning number: (mean of the two shares, wildlife share, mean share over the extra set's kinds)."""
    a = float(np.mean(right_w))
    if right_x is None or not len(right_x):
        return a, a, None
    c = float(np.mean([right_x[eyes_x == k].mean() for k in sorted(set(eyes_x.tolist()))]))
    return 0.5 * (a + c), a, c


def level(conf, hit, floor, least=30):
    """The lowest level from which every higher level keeps the share right at or above `floor`, for one set of photos;
    None when even the highest levels with at least `least` photos fall short."""
    good = None
    for tau in GRID[::-1]:
        m = conf >= tau
        if m.sum() < least:
            continue
        if hit[m].mean() >= floor:
            good = float(tau)
        else:
            break
    return good


def kind_at(sets, floor=BAR):
    """fusion.kind_at: the lowest level at which an asserted kind is right at least `floor` of the time on every one of
    the tuning sets taken by itself (each is a pair: winning kind's probability, was it right). None if no level does it."""
    levels = [level(c, h, floor) for c, h in sets if len(c)]
    if not levels or any(l is None for l in levels):
        return None
    return max(levels)


def outcome(said, prob, three, truth, tau):
    """What the page does for one set of photos when it asserts a kind only from probability tau on.
    said: the winning kind; prob: its probability; three: does the true kind sit among the three likeliest."""
    right = said == truth
    sure = prob >= tau if tau is not None else np.ones(len(said), bool)
    return {"photos": int(len(said)), "kind_right": ev.ci(right), "asserted": ev.ci(sure), "asserted_right": ev.ci(right[sure]),
            "not_sure": ev.ci(~sure), "not_sure_true_kind_among_three": ev.ci(three[~sure]), "true_kind_among_three": ev.ci(three),
            "wrong_and_asserted": ev.ci(sure & ~right)}


def table(said, prob, three, truth, tau, named=None, order=None):
    """One row a true kind: photos, share right, share asserted, right when asserted, the true kind among the three
    when not sure, a species named, and the commonest wrong answer."""
    rows = []
    sure = prob >= tau if tau is not None else np.ones(len(said), bool)
    for k in (order or sorted(set(truth.tolist()))):
        m = truth == k
        if not m.any():
            continue
        wrong = said[m][said[m] != k]
        vals, cnt = np.unique(wrong, return_counts=True) if len(wrong) else ([], [])
        rows.append({"kind": k, "n": int(m.sum()), "right": ev.ci(said[m] == k), "asserted": float(sure[m].mean()),
                     "asserted_right": (float((said[m] == k)[sure[m]].mean()) if sure[m].any() else None),
                     "not_sure_true_kind_among_three": (float(three[m][~sure[m]].mean()) if (~sure[m]).any() else None),
                     "said_person": float((said[m] == "person").mean()), "said_none": float((said[m] == "none").mean()),
                     "named": (float(named[m].mean()) if named is not None else None),
                     "commonest_wrong": ("%s (%d)" % (vals[int(np.argmax(cnt))], int(cnt.max())) if len(wrong) else "")})
    return rows
