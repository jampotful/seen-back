# Training photos: around Alachua County, observations through 2024-12-31

Built by `tools/species/build_train_s3.py` on 2026-10-11 07:11 (UTC) from iNaturalist's open-data files of Sun, 27 Sep 2026 16:10:27 GMT. 84808 rows from 5467 of the list's 5911 species, at most 60 a species.

Rows are in order of each photo's rank within its species, so the first rows hold every species' first photo.

The manifest is published only on the branch `pub/data-alachua` as `train/alachua-pre2025/manifest.csv`.

This route differs from the species list's in three ways: the region is a bounding box (latitude 29.42 to 29.95, longitude -82.66 to -82.05), which takes in a strip of the neighbouring counties; iNaturalist blurs the place of some threatened species, so a few are missed or misplaced; and species are matched to the list by scientific name, so a species GBIF files under another name has no training photos here.

## Checks

- photos attached to more than one observation: 312; observations whose first photo is one of them and which use their next own photo: 18; observations left with no photo of their own: 254
- evaluation photos found in the open-data photos file: 5921 of 6000 (keys: 1390); keys whose photos sit mostly under another iNaturalist name: 57; names used as aliases: 56
- observations in the box, research grade: 264412; kept: 181774 (through an alias: 7570); left out: {'not identified to a species': 1124, 'species not in the species list by name': 5308, 'dated after 2024-12-31': 76206}
- photo rows read: 443078; kept observations with a photo: 181612 of 181774
- rows dated after 2024-12-31: 0; photos shared with the evaluation manifest (6000 rows) and left out: 0
- scientific names carried by two keys in the species list (the more recorded key keeps the photos): Salvia azurea

## Photos a species

| photos | species |
|---|---:|
| 60 | 659 |
| 30 to 59 | 419 |
| 10 to 29 | 1018 |
| 5 to 9 | 801 |
| 2 to 4 | 1289 |
| 1 | 1281 |
| none | 444 |

## By kind of eye

| eyes | rows | share |
|---|---:|---:|
| insect | 32404 | 38.2% |
| plant | 28509 | 33.6% |
| other | 8380 | 9.9% |
| bird | 6886 | 8.1% |
| bee | 2472 | 2.9% |
| reptile | 2313 | 2.7% |
| wader | 1580 | 1.9% |
| frog | 912 | 1.1% |
| hawk | 603 | 0.7% |
| squirrel | 201 | 0.2% |
| deer | 180 | 0.2% |
| rabbit | 124 | 0.1% |
| cat | 96 | 0.1% |
| dog | 88 | 0.1% |
| alligator | 60 | 0.1% |

## By class

| class | rows | share |
|---|---:|---:|
| Insecta | 34876 | 41.1% |
| Magnoliopsida | 21889 | 25.8% |
| Aves | 9069 | 10.7% |
| Liliopsida | 5010 | 5.9% |
| Agaricomycetes | 2632 | 3.1% |
| Arachnida | 2412 | 2.8% |
| Squamata | 1723 | 2.0% |
| Mammalia | 1139 | 1.3% |
| Amphibia | 1041 | 1.2% |
| Polypodiopsida | 986 | 1.2% |
| (none) | 900 | 1.1% |
| Testudines | 590 | 0.7% |
| Gastropoda | 522 | 0.6% |
| Pinopsida | 346 | 0.4% |
| Diplopoda | 231 | 0.3% |
| Lecanoromycetes | 202 | 0.2% |
| Malacostraca | 165 | 0.2% |
| Myxomycetes | 102 | 0.1% |
| Sordariomycetes | 96 | 0.1% |
| Chilopoda | 91 | 0.1% |
| Bryopsida | 87 | 0.1% |
| Arthoniomycetes | 72 | 0.1% |
| Tremellomycetes | 66 | 0.1% |
| Protosteliomycetes | 61 | 0.1% |
| Lycopodiopsida | 61 | 0.1% |
| Crocodylia | 60 | 0.1% |
| Collembola | 53 | 0.1% |
| Cycadopsida | 47 | 0.1% |
| Bivalvia | 38 | 0.0% |
| Sphagnopsida | 31 | 0.0% |

## By licence

| licence | rows | share |
|---|---:|---:|
| CC-BY-NC | 62694 | 73.9% |
| CC-BY | 13555 | 16.0% |
| CC0 | 5317 | 6.3% |
| CC-BY-NC-ND | 2569 | 3.0% |
| CC-BY-NC-SA | 387 | 0.5% |
| CC-BY-ND | 156 | 0.2% |
| CC-BY-SA | 130 | 0.2% |

## Rows by rank within species

| first rows | cover ranks below |
|---:|---:|
| 5467 | 1 |
| 19274 | 5 |
| 31010 | 10 |
| 47670 | 20 |
| 59775 | 30 |
| 73806 | 45 |
| 84808 | 60 |

## The most recorded species with no training photo here

| records in the list | species | English name |
|---:|---|---|
| 244 | *Hermeuptychia hermes* | Hermes Satyr |
| 148 | *Samea ecclesialis* | Assembly Moth |
| 118 | *Limenitis astyanax* |  |
| 101 | *Acontia onagrus* |  |
| 81 | *Pyrgus oileus* | Tropical Checkered-Skipper |
| 62 | *Atteva punctella* |  |
| 40 | *Carphephorus paniculatus* |  |
| 39 | *Platycotis vittatus* | Oak Treehopper |
| 37 | *Atrytone delaware* |  |
| 32 | *Aethiopocassis scripta* |  |
| 31 | *Porphyrio porphyrio* | Western Swamphen |
| 31 | *Enodia portlandia* | Southern Pearly-eye |
| 30 | *Argyria nivalis* |  |
| 28 | *Hydrocharis spongia* | American spongeplant |
| 26 | *Spargaloma perditalis* |  |
| 26 | *Gnatocerus cornutus* | Broadhorned Flour Beetle |
| 26 | *Citrus aurantium* | sour orange |
| 21 | *Vaccinium corymbosum* | Northern highbush blueberry |
| 21 | *Liodytes pygaea* | Black Swamp Snake |
| 20 | *Graminella villicus* |  |
| 20 | *Cocculus carolinus* | Carolina coralbead |
| 19 | *Kalanchoe houghtonii* |  |
| 18 | *Irpiciporus pachyodon* | marshmallow polypore |
| 18 | *Cistothorus platensis* | Grass Wren |
| 18 | *Carya alba* | mockernut hickory |
| 16 | *Eubotrys racemosa* | fetterbush |
| 16 | *Edessa bifida* |  |
| 16 | *Cyrtolobus tuberosa* |  |
| 15 | *Panus neostrigosus* |  |
| 15 | *Achatia mucens* |  |

## List species matched through another iNaturalist name

From the evaluation photos (see the top of `tools/species/build_train_s3.py`).

| GBIF name (list) | iNaturalist name | observations kept | rows |
|---|---|---:|---:|
| *Gallinula chloropus* | *Gallinula galeata* | 961 | 60 |
| *Grus canadensis* | *Antigone canadensis* | 750 | 60 |
| *Phalacrocorax auritus* | *Nannopterum auritum* | 514 | 60 |
| *Rhus copallina* | *Rhus copallinum* | 421 | 60 |
| *Asimina longifolia* | *Asimina angustifolia* | 365 | 60 |
| *Bubulcus ibis* | *Ardea ibis* | 324 | 60 |
| *Papilio cresphontes* | *Heraclides cresphontes* | 280 | 60 |
| *Anasaitis canosa* | *Anasaitis canosus* | 263 | 60 |
| *Anisota virginiensis* | *Anisota pellucida* | 210 | 60 |
| *Drymaeus dormani* | *Antidrymaeus dormani* | 209 | 60 |
| *Cantinoa mutabilis* | *Hyptis mutabilis* | 171 | 60 |
| *Favolus tenuiculus* | *Favolus brasiliensis* | 166 | 60 |
| *Euphorbia heterophylla* | *Euphorbia cyathophora* | 161 | 60 |
| *Lorinseria areolata* | *Woodwardia areolata* | 158 | 60 |
| *Rhaphiolepis bibas* | *Eriobotrya japonica* | 157 | 60 |
| *Protographium marcellus* | *Eurytides marcellus* | 154 | 60 |
| *Nuttallanthus canadensis* | *Linaria canadensis* | 150 | 60 |
| *Bison bison* | *Bos bison* | 147 | 60 |
| *Cinnamomum camphora* | *Camphora officinarum* | 146 | 60 |
| *Cirsium nuttalii* | *Cirsium nuttallii* | 139 | 60 |
| *Asimina speciosa* | *Asimina incana* | 138 | 60 |
| *Cerrena hydnoides* | *Hexagonia hydnoides* | 135 | 60 |
| *Argyria pusillalis* | *Argyria gonogramma* | 127 | 60 |
| *Abaeis nicippe* | *Eurema nicippe* | 123 | 60 |
| *Urbanus dorantes* | *Cecropterus dorantes* | 120 | 60 |
| *Circus cyaneus* | *Circus hudsonius* | 115 | 60 |
| *Regulus calendula* | *Corthylio calendula* | 113 | 60 |
| *Smilax maritima* | *Smilax smallii* | 99 | 60 |
| *Euptychia cymela* | *Megisto cymela* | 78 | 60 |
| *Anchistea virginica* | *Woodwardia virginica* | 77 | 60 |
| *Carphephorus odoratissimus* | *Trilisa odoratissima* | 69 | 60 |
| *Cicindela punctulata* | *Cicindelidia punctulata* | 68 | 60 |
| *Paroxya clavuligera* | *Paroxya clavuliger* | 64 | 60 |
| *Clogmia albipunctatus* | *Clogmia albipunctata* | 63 | 60 |
| *Lactarius hygrophoroides* | *Lactifluus hygrophoroides* | 53 | 53 |
| *Persea palustris* | *Tamala palustris* | 31 | 31 |
| *Persea borbonia* | *Tamala borbonia* | 29 | 29 |
| *Fixsenia favonius* | *Satyrium favonius* | 23 | 23 |
| *Corydalis micrantha* | *Corydalis halei* | 23 | 23 |
| *Ganoderma resinaceum* | *Ganoderma sessile* | 22 | 22 |
| *Nicrophorus carolinus* | *Nicrophorus carolina* | 20 | 20 |
| *Cartrema americana* | *Cartrema americanum* | 20 | 20 |
| *Phellinus gilvus* | *Fuscoporia gilva* | 20 | 20 |
| *Lentinus levis* | *Pleurotus levis* | 16 | 16 |
| *Dioprosopa clavatus* | *Dioprosopa clavata* | 13 | 13 |
| *Cicindela trifasciata* | *Cicindelidia trifasciata* | 12 | 12 |
| *Sapindus saponaria* | *Sapindus marginatus* | 10 | 10 |
| *Acontia candefacta* | *Ponometia candefacta* | 9 | 9 |
| *Endodeca serpentaria* | *Aristolochia serpentaria* | 8 | 8 |
| *Pyramica eggersi* | *Strumigenys eggersi* | 6 | 6 |
| *Dacrymyces spathularius* | *Dacrymyces spathularia* | 6 | 6 |
| *Panicum gymnocarpon* | *Phanopyrum gymnocarpon* | 4 | 4 |
| *Calligrapha suturella* | *Calligrapha suturalis* | 3 | 3 |
| *Callisia graminea* | *Cuthbertia graminea* | 3 | 3 |
| *Macrosiagon cruentum* | *Macrosiagon cruenta* | 3 | 3 |
| *Eudociminus mannerheimi* | *Eudociminus mannerheimii* | 1 | 1 |
