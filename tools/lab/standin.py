"""Stand-in data in the formats of docs/CONTRACTS.md, for use until pub/data-alachua exists.

Usage: python3 tools/lab/standin.py <out dir>
Writes <out>/eval/standin/manifest.csv (recent research-grade Alachua County observations from GBIF, one photo each)
and <out>/regions/us-fl-alachua/species.json (thirty species chosen by hand, taxonomy filled from the GBIF backbone).
Needs the network (GBIF API); runs on a build machine.
"""
import csv
import hashlib
import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request

API = "https://api.gbif.org/v1"
DATASET = "50c9509d-22c7-4a22-a47d-8c48425ef4a7"
UA = {"User-Agent": "seen-back-lab/1 (research; github.com/jampotful/seen-back)"}

HAND = [
    ("Ardea herodias", "Great Blue Heron"), ("Ardea alba", "Great Egret"), ("Eudocimus albus", "White Ibis"),
    ("Antigone canadensis", "Sandhill Crane"), ("Aramus guarauna", "Limpkin"), ("Buteo lineatus", "Red-shouldered Hawk"),
    ("Pandion haliaetus", "Osprey"), ("Cardinalis cardinalis", "Northern Cardinal"), ("Mimus polyglottos", "Northern Mockingbird"),
    ("Cathartes aura", "Turkey Vulture"), ("Alligator mississippiensis", "American Alligator"), ("Anolis carolinensis", "Green Anole"),
    ("Anolis sagrei", "Brown Anole"), ("Trachemys scripta", "Pond Slider"), ("Hyla cinerea", "Green Treefrog"),
    ("Sciurus carolinensis", "Eastern Gray Squirrel"), ("Odocoileus virginianus", "White-tailed Deer"), ("Sylvilagus floridanus", "Eastern Cottontail"),
    ("Procyon lotor", "Common Raccoon"), ("Didelphis virginiana", "Virginia Opossum"), ("Apis mellifera", "Western Honey Bee"),
    ("Xylocopa virginica", "Eastern Carpenter Bee"), ("Danaus plexippus", "Monarch"), ("Agraulis vanillae", "Gulf Fritillary"),
    ("Romalea microptera", "Eastern Lubber Grasshopper"), ("Quercus virginiana", "Southern Live Oak"), ("Tillandsia usneoides", "Spanish Moss"),
    ("Magnolia grandiflora", "Southern Magnolia"), ("Trichonephila clavipes", "Golden Silk Orbweaver"), ("Felis catus", "Domestic Cat"),
]


def get(url):
    for k in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            print("retry %s: %s" % (url, e), flush=True)
            time.sleep(2 * (k + 1))
    raise SystemExit("GBIF unreachable: " + url)


def eyes(t):
    """docs/CONTRACTS.md, first match wins."""
    g, f, o, c, k = (t.get(x) or "" for x in ("genus", "family", "order", "class", "kingdom"))
    if g == "Homo":
        return "person"
    if f == "Felidae":
        return "cat"
    if f == "Canidae":
        return "dog"
    if o == "Rodentia":
        return "squirrel"
    if o == "Lagomorpha":
        return "rabbit"
    if f in ("Cervidae", "Bovidae", "Equidae", "Antilocapridae", "Camelidae", "Giraffidae"):
        return "deer"
    if o in ("Accipitriformes", "Falconiformes"):
        return "hawk"
    if f in ("Ardeidae", "Threskiornithidae", "Ciconiidae", "Gruidae", "Aramidae", "Rallidae") or o in ("Columbiformes", "Galliformes"):
        return "wader"
    if c == "Aves":
        return "bird"
    if o == "Crocodylia" or c == "Crocodylia":
        return "alligator"
    if c in ("Reptilia", "Squamata", "Testudines", "Sphenodontia") or o in ("Squamata", "Testudines", "Sphenodontia"):
        return "reptile"
    if o == "Anura":
        return "frog"
    if o == "Hymenoptera" and f != "Formicidae":
        return "bee"
    if c == "Insecta":
        return "insect"
    if k == "Plantae":
        return "plant"
    return "other"


def main():
    out = pathlib.Path(sys.argv[1])
    species = []
    for sci, en in HAND:
        m = get(API + "/species/match?" + urllib.parse.urlencode({"name": sci, "strict": "true"}))
        row = {"key": m.get("speciesKey") or m.get("usageKey"), "sci": m.get("species") or sci, "en": en,
               "en_source": "hand", "kingdom": m.get("kingdom", ""), "phylum": m.get("phylum", ""),
               "class": m.get("class", ""), "order": m.get("order", ""), "family": m.get("family", ""),
               "genus": m.get("genus", ""), "n": 0, "m": [0] * 12}
        row["eyes"] = eyes(row)
        species.append(row)
    sj = {"region": {"id": "us-fl-alachua", "name": "Alachua County, Florida", "gadm": "USA.10.1_1"},
          "source": {"dataset": "STAND-IN: thirty species chosen by hand by the lab, taxonomy from the GBIF backbone (species/match)",
                     "datasetKey": None, "retrieved": time.strftime("%Y-%m-%d"), "records_through": None, "doi_or_query": "tools/lab/standin.py"},
          "species": species}
    p = out / "regions" / "us-fl-alachua" / "species.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(sj, indent=1) + "\n")
    q = {"datasetKey": DATASET, "gadmGid": "USA.10.1_1", "mediaType": "StillImage", "year": "2025,2026", "limit": 60,
         "taxonRank": "SPECIES"}
    res = get(API + "/occurrence/search?" + urllib.parse.urlencode(q))
    rows = []
    for o in res.get("results", []):
        media = [x for x in o.get("media", []) if x.get("type") == "StillImage" and "/original." in (x.get("identifier") or "")]
        if not media or not o.get("speciesKey"):
            continue
        mm = media[0]
        gid = str(o["gbifID"])
        split = "val" if int(hashlib.sha256(gid.encode()).hexdigest(), 16) % 10 < 3 else "test"
        t = {x: o.get(x, "") for x in ("kingdom", "phylum", "class", "order", "family", "genus")}
        rows.append({"id": "s%06d" % (len(rows) + 1), "gbif_id": gid, "obs_url": o.get("occurrenceID", ""),
                     "key": o.get("speciesKey"), "sci": o.get("species", ""), "en": o.get("vernacularName", ""),
                     "kingdom": t["kingdom"], "class": t["class"], "order": t["order"], "family": t["family"],
                     "eyes": eyes(t), "date": (o.get("eventDate") or "")[:10], "month": o.get("month", ""),
                     "photo_url": mm["identifier"].replace("/original.", "/medium."), "licence": mm.get("license", ""),
                     "split": split})
        if len(rows) >= 40:
            break
    p = out / "eval" / "standin" / "manifest.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    cols = ["id", "gbif_id", "obs_url", "key", "sci", "en", "kingdom", "class", "order", "family", "eyes", "date",
            "month", "photo_url", "licence", "split"]
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print("stand-in: %d species, %d photos" % (len(species), len(rows)))


if __name__ == "__main__":
    main()
