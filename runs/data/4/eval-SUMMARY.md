# Evaluation photos: alachua-2025

Made by `tools/species/build_eval.py` on 2026-10-11 from GBIF (iNaturalist research-grade observations, dataset `50c9509d-22c7-4a22-a47d-8c48425ef4a7`), region GADM area `USA.10.1_1`, observations dated 2025-01-01 to 2026-10-11, seed `seen-back/alachua-2025/v1`. Rerun it to check any number here.

Every row is dated after 2024-12-31 (the species list's `records_through`) and after 2024-05-01 (the GBIF snapshot behind BioCLIP 2's training data).

## Size

- Rows: **6000** (val 1803, test 4197), from a pool of 69705 eligible observations (71020 read).
- Distinct species: 1402 (val 752, test 1170).
- Left out of the pool: not identified to a GBIF species (rank GENUS): 1170, not identified to a GBIF species (rank FAMILY): 145.

## Coverage by the species list

The share of rows whose species a recognizer restricted to the list could name at all: the ceiling of its accuracy.

| Species list restricted to | Rows covered | Share | Test rows covered | Share of test |
|---|---:|---:|---:|---:|
| all species (n at least 1) | 5949 | 99.2% | 4161 | 99.1% |
| n at least 3 | 5872 | 97.9% | 4103 | 97.8% |
| n at least 10 | 5667 | 94.5% | 3965 | 94.5% |

## By kind of eye

| Kind | Rows | Share |
|---|---:|---:|
| cat | 15 | 0.2% |
| dog | 7 | 0.1% |
| squirrel | 50 | 0.8% |
| deer | 57 | 0.9% |
| rabbit | 44 | 0.7% |
| hawk | 108 | 1.8% |
| wader | 539 | 9.0% |
| bird | 767 | 12.8% |
| alligator | 166 | 2.8% |
| reptile | 374 | 6.2% |
| frog | 137 | 2.3% |
| bee | 178 | 3.0% |
| insect | 1400 | 23.3% |
| plant | 1743 | 29.1% |
| other | 415 | 6.9% |

## By class

| Class | Rows | Share |
|---|---:|---:|
| Animalia / Insecta | 1578 | 26.3% |
| Animalia / Aves | 1414 | 23.6% |
| Plantae / Magnoliopsida | 1241 | 20.7% |
| Plantae / Liliopsida | 421 | 7.0% |
| Animalia / Squamata | 292 | 4.9% |
| Animalia / Arachnida | 208 | 3.5% |
| Animalia / Mammalia | 200 | 3.3% |
| Animalia / Crocodylia | 166 | 2.8% |
| Animalia / Amphibia | 142 | 2.4% |
| Animalia / Testudines | 82 | 1.4% |
| Plantae / Polypodiopsida | 59 | 1.0% |
| Fungi / Agaricomycetes | 57 | 0.9% |
| Animalia / (none) | 26 | 0.4% |
| Animalia / Gastropoda | 21 | 0.3% |
| Plantae / Pinopsida | 19 | 0.3% |
| Fungi / Arthoniomycetes | 18 | 0.3% |
| Animalia / Malacostraca | 16 | 0.3% |
| Animalia / Diplopoda | 14 | 0.2% |
| Fungi / Lecanoromycetes | 7 | 0.1% |
| Animalia / Chilopoda | 7 | 0.1% |
| Plantae / Jungermanniopsida | 2 | 0.0% |
| Fungi / Leotiomycetes | 1 | 0.0% |
| Fungi / Exobasidiomycetes | 1 | 0.0% |
| Fungi / Laboulbeniomycetes | 1 | 0.0% |
| Protozoa / Protosteliomycetes | 1 | 0.0% |
| Fungi / Sordariomycetes | 1 | 0.0% |
| Plantae / Zygnematophyceae | 1 | 0.0% |
| Protozoa / Myxomycetes | 1 | 0.0% |
| Fungi / Dacrymycetes | 1 | 0.0% |
| Fungi / Tremellomycetes | 1 | 0.0% |
| Animalia / Collembola | 1 | 0.0% |

## By month

| Month | Pool | Rows |
|---|---:|---:|
| 2025-01 | 1562 | 134 |
| 2025-02 | 2204 | 190 |
| 2025-03 | 3371 | 290 |
| 2025-04 | 6595 | 568 |
| 2025-05 | 3239 | 279 |
| 2025-06 | 2875 | 247 |
| 2025-07 | 3423 | 295 |
| 2025-08 | 3671 | 316 |
| 2025-09 | 4138 | 356 |
| 2025-10 | 3613 | 311 |
| 2025-11 | 4244 | 365 |
| 2025-12 | 1987 | 171 |
| 2026-01 | 1980 | 170 |
| 2026-02 | 2137 | 184 |
| 2026-03 | 4363 | 376 |
| 2026-04 | 5775 | 497 |
| 2026-05 | 3056 | 263 |
| 2026-06 | 2691 | 232 |
| 2026-07 | 2990 | 257 |
| 2026-08 | 2553 | 220 |
| 2026-09 | 3238 | 279 |

## By licence (of the image)

| Licence | Rows | Share |
|---|---:|---:|
| CC-BY-NC-4.0 | 5317 | 88.6% |
| CC-BY-4.0 | 476 | 7.9% |
| CC0-1.0 | 204 | 3.4% |
| CC-BY-NC-ND-4.0 | 3 | 0.1% |

## English names

- Rows with an English name: 5855 (97.6%).

## Labels: GBIF species against the name given on iNaturalist

Rows are labelled with the GBIF backbone species of the record. For 331 rows (5.5%) the species the iNaturalist community named (the record's `taxonID`, looked up in iNaturalist's taxonomy archive) has another name in the backbone; 5669 rows agree; 0 could not be looked up. 63 distinct pairs; the most frequent (iNaturalist name: GBIF label, rows):

- *Gallinula galeata*: *Gallinula chloropus*, 49
- *Antigone canadensis*: *Grus canadensis*, 44
- *Asimina angustifolia*: *Asimina longifolia*, 19
- *Nannopterum auritum*: *Phalacrocorax auritus*, 15
- *Ardea ibis*: *Bubulcus ibis*, 14
- *Rhus copallinum*: *Rhus copallina*, 12
- *Heraclides cresphontes*: *Papilio cresphontes*, 12
- *Woodwardia areolata*: *Lorinseria areolata*, 10
- *Eriobotrya japonica*: *Rhaphiolepis bibas*, 9
- *Asimina incana*: *Asimina speciosa*, 9
- *Hexagonia hydnoides*: *Cerrena hydnoides*, 7
- *Eurytides marcellus*: *Protographium marcellus*, 7
- *Cirsium nuttallii*: *Cirsium nuttalii*, 7
- *Corthylio calendula*: *Regulus calendula*, 6
- *Paroxya clavuliger*: *Paroxya clavuligera*, 6
- *Anasaitis canosus*: *Anasaitis canosa*, 6
- *Megisto cymela*: *Euptychia cymela*, 6
- *Bos bison*: *Bison bison*, 5
- *Woodwardia virginica*: *Anchistea virginica*, 5
- *Eurema nicippe*: *Abaeis nicippe*, 5
- *Euphorbia cyathophora*: *Euphorbia heterophylla*, 5
- *Ponometia candefacta*: *Acontia candefacta*, 4
- *Sapindus marginatus*: *Sapindus saponaria*, 4
- *Smilax smallii*: *Smilax maritima*, 4
- *Camphora officinarum*: *Cinnamomum camphora*, 4

A recognizer that answers with iNaturalist's names needs this mapping before it is scored against `sci`/`key`.

## Checks

    records read: 71020 unique (0 seen twice); days re-read: 0; days still short: 0 []; months whose day counts differ from the month count: none
    GADM level-2 area of every record read: {'USA.10.1_1': 71020}
    eligible: 69705 of 71020; left out: {'not identified to a GBIF species (rank GENUS)': 1170, 'not identified to a GBIF species (rank FAMILY)': 145}; photo hosts: {'inaturalist-open-data.s3.amazonaws.com': 71020}; date/month disagreements: 0

Problems found: none
