#!/usr/bin/env python3
"""Checks of tools/species/everyday_build.py that need no network and no model: the rule for synonyms, and the softmax
read with every beta at once against the plain softmax of fuseWith over all rows.

Usage: python3 -I tools/species/test_everyday_build.py
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import everyday_build as eb  # noqa: E402

failed = 0


def check(name, cond):
    global failed
    print(("ok    " if cond else "FAIL  ") + name)
    failed += 0 if cond else 1


# 1. the rule for synonyms (GBIF's answers given, as data/everyday/accepted.json keeps them)
rows = [["Canis lupus", "Domestic Dog", "dog"], ["Sus scrofa", "Wild Boar", "mammal"], ["Felis catus", "Domestic Cat", "cat"],
        ["Rhaphiolepis bibas", "Loquat", "plant"]]
keys = [5219173, 7705930, 2435035, 10786206]
by_key = {k: i for i, k in enumerate(keys)}
by_sci = {r[0]: i for i, r in enumerate(rows)}
sp = [{"gbif_key": "5219200", "sci": "Canis familiaris", "status": "SYNONYM", "accepted_key": "6164210", "en": "Domestic Dog"},
      {"gbif_key": "7792440", "sci": "Sus domesticus", "status": "SYNONYM", "accepted_key": "7705930", "en": ""},
      {"gbif_key": "3024146", "sci": "Eriobotrya japonica", "status": "SYNONYM", "accepted_key": "10786206", "en": "loquat"},
      {"gbif_key": "5816581", "sci": "Mustela furo", "status": "SYNONYM", "accepted_key": "5218913", "en": "Domestic Ferret"},
      {"gbif_key": "2435035", "sci": "Felis catus", "status": "ACCEPTED", "accepted_key": "", "en": "Domestic Cat"}]
cache = {"6164210": {"key": 6164210, "canonicalName": "Canis lupus familiaris", "rank": "SUBSPECIES", "speciesKey": 5219173, "species": "Canis lupus"},
         "7705930": {"key": 7705930, "canonicalName": "Sus scrofa", "rank": "SPECIES", "speciesKey": 7705930, "species": "Sus scrofa"},
         "10786206": {"key": 10786206, "canonicalName": "Rhaphiolepis bibas", "rank": "SPECIES", "speciesKey": 10786206, "species": "Rhaphiolepis bibas"},
         "5218913": {"key": 5218913, "canonicalName": "Mustela putorius furo", "rank": "SUBSPECIES", "speciesKey": 5218911, "species": "Mustela putorius"}}
acc = eb.accepted_rows(sp, rows, by_key, by_sci, cache, lambda s: s["en"])
check("the dog takes the world row of Canis lupus, whose English name is the dog's", acc[5219200]["world_row"] == 0 and acc[5219200]["same_english"])
check("the pig keeps a row of its own (no English name of its own; the world row is Wild Boar)", not acc[7792440]["same_english"])
check("the loquat takes Rhaphiolepis bibas (English names compared without case)", acc[3024146]["same_english"] and acc[3024146]["world_row"] == 3)
check("the ferret keeps a row of its own (the table has no row for Mustela putorius)", acc[5816581]["world_row"] is None and not acc[5816581]["same_english"])
check("an accepted species is not looked up", 2435035 not in acc)

# 2. the softmax read with every beta at once agrees with the plain softmax over all rows
rng = np.random.default_rng(7)
S, n, W = 3000, 9, 32
labels = ["cat", "dog", "plant", "person", "other", "none"]
kinds = ["cat", "dog", "plant", "other"]


class Slot(eb.Slot):
    def __init__(self, home):                      # the parts of eb.Slot the arithmetic reads, without a place file
        self.f = {"t_species": 100.0, "t_kind": 100.0, "alpha_prior": 1.0, "w_kind": 0.5, "name_at": 0.83, "kind_at": 0.5}
        self.labels = labels
        self.K = rng.normal(size=(len(labels), W)).astype(np.float32)
        self.K /= np.linalg.norm(self.K, axis=1, keepdims=True)
        lab_ix = {k: i for i, k in enumerate(labels)}
        self.kind_ix = np.array([lab_ix[kinds[i % len(kinds)]] for i in range(S)], np.int64)
        self.has = np.zeros(len(labels), bool)
        self.has[np.unique(self.kind_ix)] = True
        self.home = home
        self.H = np.nonzero(home > 0)[0]
        self.hH = home[self.H]
        self.OH = np.zeros((S, len(labels)), np.float32)
        self.OH[np.arange(S), self.kind_ix] = 1.0
        self.OH[self.H] = 0.0
        self.OHH = np.zeros((len(self.H), len(labels)), np.float64)
        self.OHH[np.arange(len(self.H)), self.kind_ix[self.H]] = 1.0
        self.noname = np.isin(np.array(labels), ["none", "person"])


home = np.zeros(S)
home[rng.choice(S, 40, replace=False)] = rng.uniform(1e-5, 1e-3, 40)
sl = Slot(home)
Q = rng.normal(size=(S, W)).astype(np.float32)
Q /= np.linalg.norm(Q, axis=1, keepdims=True)
X = rng.normal(size=(n, W)).astype(np.float32)
X /= np.linalg.norm(X, axis=1, keepdims=True)
sd = (X @ Q.T).astype(np.float32)
share0 = rng.dirichlet(np.ones(S), size=n)
L0 = np.log(share0).astype(np.float32)
parts = sl.split(sd, L0)
worst = 0.0
same = True
for b in (0.0, 1.0, 30.0, 1000.0):
    top, tp, q = sl.at(parts, b)
    z = sl.f["t_species"] * sd.astype(np.float64) + np.log(np.exp(L0.astype(np.float64)) + b * home[None, :])
    s = np.exp(z - z.max(1, keepdims=True))
    s /= s.sum(1, keepdims=True)
    qq = np.stack([np.bincount(sl.kind_ix, weights=s[i], minlength=len(labels)) for i in range(n)])
    worst = max(worst, float(np.abs(q - qq).max()), float(np.abs(tp - s.max(1)).max()))
    same = same and bool((top == s.argmax(1)).all())
    k1 = sl.kinds(X, q, top, tp)
    k2 = sl.kinds(X, qq, s.argmax(1), s.max(1))
    same = same and bool((k1[0] == k2[0]).all() and (k1[3] == k2[3]).all())
check("every beta at once: the same first rows, kinds and names as the plain softmax", same)
check("every beta at once: probabilities within 1e-5 of the plain softmax (largest gap %.1e)" % worst, worst < 1e-5)
print("%d failed" % failed)
sys.exit(1 if failed else 0)
