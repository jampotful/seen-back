# Contracts

How the pieces of this project fit together, so that several people (or assistants) can work on it at once without stepping on each other. Read this before changing anything.

## Ground rules

- **The repository is public.** No secrets, no private notes, no names of private people, no e-mail addresses. Photographers' names from iNaturalist do not go into this repository; keep the observation address and the licence, which lead to the attribution.
- **Checked, or labelled as unchecked.** A number in a document comes from a script in this repository that anyone can rerun, and the document says which script. A claim about an animal carries a grade and a source.
- **Licences are read before anything ships.** Every model, dataset, font and library is listed in `docs/LICENCES.md` with its licence and the address the licence was read at. Research-only and non-commercial licences do not ship in the app.
- **Photos stay on the device** unless the person has been told where a photo will go and has agreed.
- **Commits** are small and say what changed. `main` holds only work that builds (`python3 -I build.py`) and passes `node --check dist/app.js`.
- **Wording in the app** is plain, in full sentences, and never promises what has not been measured.

## Build machines (GitHub Actions)

The working sandbox cannot reach most of the internet. GitHub's build machines can, so anything that needs the open network runs there.

- **Start a run** by pushing a commit to a branch named `run/<workflow>/<label>`: `git push -f origin HEAD:refs/heads/run/engines/dev`. The workflow file is read from the pushed commit, so a workflow can be developed on a run branch without touching `main`.
- **Results come back** as files on the `ci` branch under `runs/<name>/<run number>[-shard]/`, with a line in `INDEX.txt` (time, path, status, first twelve characters of the commit, branch). Every workflow ends with `bash ci/return.sh <name> <dir> [shard]` under `if: always()`, and writes its own log into the returned directory, because the logs on github.com cannot be read without signing in.
- **Wait for results** with `bash ci/wait.sh <commit sha> [lines expected] [seconds]`, then read them with `git show FETCH_HEAD:runs/...` or a checkout of the `ci` branch.
- **Large or binary outputs** (models, embeddings, data sets) go to their own branch with `bash ci/put_branch.sh <branch> <dir>`, which replaces the branch and keeps no history. Branch names: `pub/lab-<model id>` for a model's files, `pub/data-<name>` for data sets; the branch root mirrors the directory it was published from.
- **Reading a public page** from the sandbox: list addresses in `ci/fetch/list.txt` and push to `run/fetch/<label>`; the text comes back under `runs/fetch/`.
- **Limits**: 20 jobs at once, 5 of them macOS; a job may run six hours; results returned to `ci` stay under 25 MB per job; a file in git stays under 95 MB.
- **A secret named `HF_TOKEN`** (a Hugging Face token with write access) is available to workflows as `${{ secrets.HF_TOKEN }}`. Never print it, never write it to a file that is returned.
- A workflow that never appears on `ci` probably failed to parse. The list of runs at `https://github.com/jampotful/seen-back/actions` is public.

## Who owns which files

To avoid collisions, each area of work owns its files. Change another area's files only by agreement.

| Area | Files |
|---|---|
| Picture engine and its checks | `src/cam.b.js`, `src/cam.c1.js`, `src/cam.selftest.js`, `.github/workflows/engines.yml`, `ci/engines/`, `test/engines/` |
| Recognition in the page | `src/cam.rec.js`, `src/cam.c2.js`, `src/cam.r.js`, `src/cam.head.html`, `src/sw.template.js`, `vendor/`, `models/`, `test/rec/`, `test/check4.js`, `tools/fusion/` |
| Species lists and evaluation photos | `tools/species/`, `.github/workflows/data.yml`, `ci/data/`, `data/` |
| Model laboratory | `tools/lab/`, `.github/workflows/lab.yml`, `ci/lab/`, `labels/` |
| Species service | `service/`, `.github/workflows/service.yml`, `ci/service/` |
| Evaluation | `tools/eval/`, `docs/EVAL.md`, `docs/eval/` |
| Shared | `build.py`, `ci/*.sh`, `docs/`, `README.md` (changed on `main` by the coordinator) |

## The sixteen kinds of eye

`cat, dog, squirrel, deer, rabbit, hawk, wader, bird, alligator, reptile, frog, bee, insect, plant, other, person`. Every recognized species maps to one of them by taxonomy (GBIF backbone ranks). The rules, first match wins:

| Kind | Rule |
|---|---|
| `person` | genus *Homo* |
| `cat` | family Felidae |
| `dog` | family Canidae |
| `squirrel` | order Rodentia |
| `rabbit` | order Lagomorpha |
| `deer` | families Cervidae, Bovidae, Equidae, Antilocapridae, Camelidae, Giraffidae |
| `hawk` | orders Accipitriformes and Falconiformes |
| `wader` | families Ardeidae, Threskiornithidae, Ciconiidae, Gruidae, Aramidae, Rallidae; orders Columbiformes and Galliformes |
| `bird` | any other member of class Aves (owls, ducks, vultures, shorebirds and songbirds included) |
| `alligator` | order Crocodylia (GBIF sometimes ranks it as a class) |
| `reptile` | any other reptile: Squamata, Testudines, Sphenodontia, whether GBIF ranks them as orders of Reptilia or as classes |
| `frog` | order Anura |
| `bee` | order Hymenoptera except family Formicidae |
| `insect` | any other member of class Insecta |
| `plant` | kingdom Plantae |
| `other` | everything else alive: fungi, spiders, fish, snails, salamanders, other mammals |

New World vultures (Cathartiformes) go to `bird`, because the `hawk` model draws sight sharper than a person's and that is not established for vultures.

## Data formats

### Species list: `data/regions/<region>/species.json`

```json
{
  "region": {"id": "us-fl-alachua", "name": "Alachua County, Florida", "gadm": "USA.10.1_1"},
  "source": {"dataset": "iNaturalist research-grade observations via GBIF", "datasetKey": "50c9509d-22c7-4a22-a47d-8c48425ef4a7",
             "retrieved": "2026-10-11", "records_through": "2024-12-31", "doi_or_query": "..."},
  "species": [
    {"key": 2480962, "sci": "Ardea herodias", "en": "Great Blue Heron", "en_source": "inat-taxonomy",
     "kingdom": "Animalia", "phylum": "Chordata", "class": "Aves", "order": "Pelecaniformes", "family": "Ardeidae", "genus": "Ardea",
     "n": 5231, "m": [412, 380, 365, 300, 250, 210, 190, 200, 260, 350, 420, 430], "eyes": "wader"}
  ]
}
```

`key` is the GBIF species key. `n` is the number of records through `records_through`; `m` holds the same count by calendar month, January first. Species are sorted by `n`, largest first. `en` is empty when no English name was found. Records after `records_through` are kept out of the list, so that newer photos can test it fairly.

### Evaluation photos: `data/eval/<name>/manifest.csv`

One row per photo, one photo per observation. Columns:

`id, gbif_id, obs_url, key, sci, en, kingdom, class, order, family, eyes, date, month, photo_url, licence, split`

- `id` is a short stable identifier (`e000001`...). `obs_url` is the observation's address on inaturalist.org.
- `photo_url` is the medium-sized file in iNaturalist's open-data bucket. Photos are downloaded when an evaluation runs and are never committed.
- `date` is the observation date; every row is later than `records_through` of the species list, and later than 2024-05-01, the date of the GBIF snapshot behind BioCLIP 2's training data.
- `split` is `val` (three in ten) or `test`, fixed by a hash of `gbif_id`. Settings are tuned on `val`; reported numbers come from `test`.

### Training photos: `data/train/<name>/manifest.csv`

The same sixteen columns as the evaluation manifest, with `split` set to `train`. Rows come from records through `records_through` of the species list, so no training photo is later than any evaluation photo's cutoff. Up to sixty photos a species, chosen by a hash so the choice can be repeated. Ids start with `t`.

### Photos for kinds the wildlife records lack: `data/extra/<name>/manifest.csv`

People, pets, livestock and photos with nothing alive in them, taken from an openly licensed general data set. The same columns where they apply (`eyes` holds the kind, or `none`), `split` is `train` or `test`, and `key`, `sci`, `en` and the taxonomy columns are empty.

### iNaturalist's own names: `data/regions/<region>/inat.json`

GBIF files some species under names iNaturalist does not use (it lumps Florida's Common Gallinule into *Gallinula chloropus*, for one). For each GBIF species key this file gives the iNaturalist taxon most often attached to its records in the region: `{"<key>": {"inat_id": 0, "sci": "...", "en": "...", "share": 0.98}}`. The species list's `sci` stays GBIF's, because the biology models were trained on GBIF's names; `en` and the name shown to a person follow iNaturalist.

### Labels: `labels/kinds.json` and the lab's label sets

`labels/kinds.json` holds, for each kind of eye and for `none` (nothing alive), a list of noun phrases. The lab turns each phrase into sentences with its templates and averages them into one vector per kind.

### A model's files: branch `pub/lab-<model id>`

```
card.json                 id, source address, licence, licence address, parameter counts, input size, mean, std, resize rule, embedding width
text/<labelset>.f16.npy   one unit vector per label, float16, rows in the order of text/<labelset>.labels.json
images/<evalname>.f16.npy one unit vector per manifest row that could be fetched, float16; images/<evalname>.ids.json gives the row ids
onnx/vision.int8.onnx     the image encoder for the browser (when the model is a candidate for the page)
onnx/vision.fp16.onnx     the same in half precision (when under 95 MB)
onnx/parity.json          how closely each ONNX file reproduces the original model's embeddings on sample photos
```

### The page's recognizer: `models/<slot>/manifest.json`

```json
{
  "id": "tinyclip-vit-40m-32", "licence": "MIT", "source": "https://huggingface.co/...",
  "vision": {"url": "vision.int8.onnx", "bytes": 41234567, "sha256": "...", "input": "pixel_values", "output": "image_embeds",
             "size": 224, "mean": [0.4815, 0.4578, 0.4082], "std": [0.2686, 0.2613, 0.2758], "resize": "shortest-bicubic-antialias", "crop": "center"},
  "width": 512,
  "kinds": {"url": "kinds.f16.bin", "labels": ["cat", "dog", "..."]},
  "species": {"url": "species.f16.bin", "table": "species.json", "count": 2400},
  "fusion": {"t_kind": 100, "t_species": 100, "alpha_prior": 0.5, "w_kind": 0.5, "name_at": 0.6, "offer_at": 0.3}
}
```

Embedding files are raw little-endian float16, row after row, unit length.

Details settled while building it:

- `"crop": "center"` drops `floor(spare / 2)` pixels from the near edge, as the laboratory's image processor does.
- The species table is `{"species": [[scientific, English, kind, [twelve monthly weights]], ...]}`.
- Optional `fusion.prior_floor` (default 1e-6) and `fusion.offer_any_kind` (default false: the three offers come from the winning kind).
- A head may be trained instead of made from sentences. Then its rows are weights, not unit vectors, and it carries a bias: `"kinds": {"url": "...", "labels": [...], "bias": [..]}` and `"species": {..., "bias_url": "species.bias.f32.bin"}`. The score of a row is `t * (row . e) + bias`, with `e` the unit image vector, so a sentence-made head is the case of unit rows and no bias.
- Files are asked for with `?v=<version>` and kept under that address; the manifest itself is asked of the network first. The service worker keeps versioned addresses first and treats unversioned files under `models/`, `vendor/` and `data/` as network-first with the kept copy as fallback.
- `tools/species/fetch_photos.py --shard i/n` counts shards from zero. `species.json` here is the compact table the page needs (scientific name, English name, kind of eye, twelve monthly weights), rows in the same order as the vectors.

## The species service (the naturalist)

A small server that names the species from a photo, for when there is signal. The page never calls it without the person's say-so.

```
POST /v1/identify      multipart form: image (JPEG, longest side at most 512, under 1 MB), month (1-12), region ("us-fl-alachua" or empty), top (at most 10)
  -> 200 {"model": "bioclip2-l14", "region": "us-fl-alachua", "ms": 1234,
          "species": [{"key": 2480962, "sci": "Ardea herodias", "en": "Great Blue Heron", "eyes": "wader", "p": 0.83}],
          "kinds": [{"key": "wader", "p": 0.97}]}
GET  /v1/health        -> {"ok": true, "ready": true, "model": "...", "species": 5911}
```

- It answers browsers from `https://jampotful.github.io` and from localhost, and nobody else's pages.
- It keeps no photo and logs nothing about a photo beyond a count and the time taken.
- It reads its label rows, biases, species table and prior from files in the same layout as the page's recognizer, so a better head is a change of files.
- It runs on the free tier only.
