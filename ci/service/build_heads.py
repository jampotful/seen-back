"""Make the species service's head for one region from the laboratory's label rows and the species list.

Usage: python3 ci/service/build_heads.py --rows text/species_sci.f16.npy --labels text/species_sci.labels.json
           --species data/regions/us-fl-alachua/species.json [--inat inat.json] [--card card.json] --out service/heads/us-fl-alachua
           [--t 100] [--alpha 0.8333] [--smooth 0.5]

Writes, in the layout of the page's models/<slot>/:
  manifest.json     id, source, licence, width, species {url, table, count}, fusion {t_species, alpha_prior, prior_floor}
  species.f16.bin   raw little-endian float16 rows, unit length, in the order of the species list
  species.json      {"species": [[scientific, English, kind, [twelve monthly weights]], ...], "keys": [GBIF keys]}
The monthly weights are the list's record counts plus `smooth`, so that the page's prior rule (each species' share of
the month's weights, floored) reproduces the first-look script's (M + 0.5) arithmetic. Temperature 100 with prior weight 0.8333 ranks every species exactly as the
first-look setting (30, 0.25) does, since only the ratio of the two decides the order; 100 is where the negative
log-likelihood on the val split is lowest (ci/service/calibrate.py). At 30 the probabilities are so flat that the
species summed by kind of eye pick the right kind on only 44% of photos. Settings are provisional until the
evaluation agent hands over tuned ones.
"""
import argparse
import hashlib
import json
import pathlib

import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", required=True)
    ap.add_argument("--labels", required=True)
    ap.add_argument("--species", required=True)
    ap.add_argument("--inat")
    ap.add_argument("--card")
    ap.add_argument("--out", required=True)
    ap.add_argument("--rowset", default="species_sci")
    ap.add_argument("--t", type=float, default=100.0)
    ap.add_argument("--alpha", type=float, default=round(0.25 * 100 / 30, 4))
    ap.add_argument("--smooth", type=float, default=0.5)
    a = ap.parse_args()

    sp = json.loads(pathlib.Path(a.species).read_text(encoding="utf-8"))
    species = sp["species"]
    region = sp.get("region", {})
    labels = json.loads(pathlib.Path(a.labels).read_text(encoding="utf-8"))
    labels = labels.get("labels") if isinstance(labels, dict) else labels
    rows = np.load(a.rows).astype(np.float32)
    if rows.shape[0] != len(species) or len(labels) != len(species):
        raise SystemExit("rows %s, labels %d, species %d: they must agree" % (rows.shape, len(labels), len(species)))
    for i, (lab, s) in enumerate(zip(labels, species)):
        if int(lab["key"]) != int(s["key"]):
            raise SystemExit("row %d: label key %s, species key %s: the orders differ" % (i, lab["key"], s["key"]))
    norms = np.linalg.norm(rows, axis=1)
    rows = rows / norms[:, None]

    inat = {}
    if a.inat and pathlib.Path(a.inat).exists():
        inat = json.loads(pathlib.Path(a.inat).read_text(encoding="utf-8"))
    n_inat = 0
    table, keys = [], []
    for s in species:
        en = s.get("en") or ""
        i = inat.get(str(s["key"])) or {}
        if i.get("en"):
            en, n_inat = i["en"], n_inat + 1
        m = s.get("m") if isinstance(s.get("m"), list) and len(s["m"]) == 12 else [0] * 12
        table.append([s["sci"], en, s.get("eyes") or "other", [round(float(x) + a.smooth, 3) for x in m]])
        keys.append(int(s["key"]))

    card = json.loads(pathlib.Path(a.card).read_text(encoding="utf-8")) if a.card else {}
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    blob = rows.astype("<f2").tobytes()
    (out / "species.f16.bin").write_bytes(blob)
    (out / "species.json").write_text(json.dumps({"species": table, "keys": keys}, ensure_ascii=False, separators=(",", ":")),
                                      encoding="utf-8")
    manifest = {
        "id": card.get("id", "bioclip2-l14"),
        "source": card.get("source", "hf-hub:imageomics/bioclip-2"),
        "source_url": card.get("source_url", "https://huggingface.co/imageomics/bioclip-2"),
        "licence": card.get("licence", "MIT"),
        "licence_url": card.get("licence_url", ""),
        "region": region.get("id", out.name),
        "region_name": region.get("name", ""),
        "width": int(rows.shape[1]),
        "species": {"url": "species.f16.bin", "table": "species.json", "count": len(species),
                    "rowset": a.rowset, "sha256": hashlib.sha256(blob).hexdigest()},
        "fusion": {"t_species": a.t, "alpha_prior": a.alpha, "prior_floor": 1e-6},
        "prior_weights": "monthly record counts through %s plus %g" % (sp.get("source", {}).get("records_through", "?"), a.smooth),
        "names": "English names from iNaturalist for %d species, from the species list for the rest" % n_inat,
        "provisional": True,
        "note": "Provisional: the first-look ranking (temperature 30, prior weight 0.25) at temperature 100 and prior weight 0.8333, the same order with the lowest val negative log-likelihood (ci/service/calibrate.py); the evaluation agent's tuned rows and settings replace them.",
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    print("head %s: %d species x %d, row norms before %.4f..%.4f, iNaturalist names %d, t %g, alpha %g"
          % (out, rows.shape[0], rows.shape[1], norms.min(), norms.max(), n_inat, a.t, a.alpha))


if __name__ == "__main__":
    main()
