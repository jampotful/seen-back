#!/usr/bin/env python3
"""Summarize the accepted d384-d386 observations without deriving visual performance.

python3 -I tools/views/spider_eye_transfer.py
Read-only: output is an inventory, not new evidence or an audit disposition.
"""
import collections
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def summary():
    rows, batches, groups = [], [], []
    for unit in ("desk-d384", "desk-d385", "desk-d386"):
        path = ROOT / "docs/views/evidence" / (unit + ".jsonl")
        data = path.read_bytes()
        records = [json.loads(line) for line in data.decode().splitlines() if line.strip()]
        batches.append({"unit": unit, "records": len(records), "sha256": hashlib.sha256(data).hexdigest()})
        # These files file four labelled eye types per description, in source order.
        # A group is a description, not an assertion of four independent animals.
        assert len(records) % 4 == 0
        for i in range(0, len(records), 4):
            block = records[i:i+4]
            assert len({r["taxon"] for r in block}) == 1
            assert {r["eye"] for r in block} == {"AME", "ALE", "PME", "PLE"}
            groups.append({"unit": unit, "lines": [i+1, i+4], "taxon": block[0]["taxon"],
                           "context": block[0]["measurement"], "mm": {r["eye"]: r["value"] for r in block}})
        rows.extend(records)
    families = []
    for name in sorted({r["family"] for r in rows}):
        rs = [r for r in rows if r["family"] == name]
        families.append({"family": name, "records": len(rs), "species": len({r["taxon"] for r in rs}),
                         "min_mm": min(r["value"] for r in rs), "max_mm": max(r["value"] for r in rs),
                         "traits": dict(collections.Counter(r["trait"] for r in rs))})
    return {"records": len(rows), "species": len({r["taxon"] for r in rows}),
            "genera": len({r["taxon"].split()[0] for r in rows}), "description_groups": len(groups),
            "papers": sorted({r["source"]["doi"] for r in rows}),
            "evidence_kind": dict(collections.Counter(r["evidence_kind"] for r in rows)),
            "traits": dict(collections.Counter(r["trait"] for r in rows)),
            "batches": batches, "families": families, "groups": groups}


if __name__ == "__main__":
    print(json.dumps(summary(), ensure_ascii=False, indent=2))
