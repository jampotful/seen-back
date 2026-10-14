#!/usr/bin/env python3
"""Draw the seeded sample of the audit's grade changes and cut each record's source passage.

    python3 -I tools/views/audit_sample.py --lit CHECKOUT_OF_pub/lit-t1 --kind mg --n 120 --out SAMPLE_DIR
    python3 -I tools/views/audit_sample.py --lit ... --kind gm --n 30 --out SAMPLE_DIR

--kind mg takes the corrections from m to g, gm those from g to m. The sample is stratified by unit (proportional,
at least two a unit where the unit has two) and, inside a unit, spread across traits. The seed is fixed (9).
Writes <out>/<kind>.jsonl: one row per sampled record with its id, the record, the audit's reason and passage_quote,
and the passage (about 5,200 characters around the quote, cut the way the second pass cut it).
"""
import argparse, collections, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "lit"))
import audit as A          # noqa: E402
import extract as E        # noqa: E402


def draw(rows, n, seed=9):
    rnd = random.Random(seed)
    by_unit = collections.defaultdict(list)
    for r in rows:
        by_unit[r["unit"]].append(r)
    total = len(rows)
    quota = {u: min(len(v), max(2, round(n * len(v) / total))) for u, v in by_unit.items()}
    out = []
    for u in sorted(by_unit):
        by_trait = collections.defaultdict(list)
        for r in by_unit[u]:
            by_trait[r["trait"]].append(r)
        for v in by_trait.values():
            rnd.shuffle(v)
        traits = sorted(by_trait, key=lambda t: (-len(by_trait[t]), t))
        picked = []
        while len(picked) < quota[u]:
            for t in traits:
                if by_trait[t] and len(picked) < quota[u]:
                    picked.append(by_trait[t].pop())
        out += picked
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lit", required=True)
    ap.add_argument("--all", default=os.path.join(HERE, "..", "..", "docs", "views", "audit", "ALL.jsonl"))
    ap.add_argument("--kind", choices=["mg", "gm"], default="mg")
    ap.add_argument("--n", type=int, default=120)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    old, new = ("m", "g") if a.kind == "mg" else ("g", "m")
    rows = [json.loads(l) for l in open(a.all, encoding="utf-8") if l.strip()]
    rows = [r for r in rows if r["verdict"] == "correct" and r.get("grade") == old and r.get("grade_final") == new]
    sample = draw(rows, a.n)
    topics = [t for t in sorted(os.listdir(a.lit)) if os.path.exists(os.path.join(a.lit, t, "index.jsonl"))]
    items = E.plan_works(a.lit, topics)
    idx = {E.norm_doi(it["w"].get("doi")): it for it in items if E.norm_doi(it["w"].get("doi"))}
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, a.kind + ".jsonl"), "w", encoding="utf-8") as f:
        for r in sample:
            rec = r["corrected_record"]
            it = A.find_source(idx, rec)
            passage, how = (A.passage_for(it, dict(rec, quote=rec.get("quote"))) if it else (None, "source not found"))
            f.write(json.dumps({"id": r["id"], "unit": r["unit"], "trait": r["trait"], "taxon": r["taxon"], "value": r["value"],
                                "quote": rec.get("quote"), "where": rec.get("where"), "note": rec.get("note"),
                                "title": (rec.get("source") or {}).get("title"), "reason": r.get("reason"),
                                "passage_quote": r.get("passage_quote"), "how": how, "passage": passage}, ensure_ascii=False) + "\n")
    print("%d of %d sampled; %s" % (len(sample), len(rows), collections.Counter(s["unit"] for s in sample)))


if __name__ == "__main__":
    main()
