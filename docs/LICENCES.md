# Licences

This file lists every model, data set, library and font that ships in the app or was used to build or measure it, with its licence, where the licence was read, and its status. The status is one of: ships, used for measurement only, used to fit or build, or will not ship. "Not read" means that nobody working on this project has read the licence text. A tag on a model card is recorded as a tag.

This file describes build 9 (commit `013bb77`), as it stood on 11 October 2026.

## Models

| Model | Licence | Where the licence was read | Status |
|---|---|---|---|
| TinyCLIP 39M/16 (Microsoft), `wkcn/TinyCLIP-ViT-39M-16-Text-19M-YFCC15M` on Hugging Face | MIT, Copyright (c) Microsoft Corporation | `https://raw.githubusercontent.com/microsoft/Cream/main/TinyCLIP/LICENSE`, read 10 October 2026 (`runs/fetch/2/cream-LICENSE.txt` on the `ci` branch) | **ships**: its image encoder, int8, 41.0 MB, is the pocket recognizer in `models/pocket/`, with heads fitted on its vectors of openly licensed photos (below) |
| BioCLIP 2, ViT-L/14 (Imageomics), `imageomics/bioclip-2` | MIT, Copyright (c) 2023-2026 Imageomics Institute and others named in the file. The model card says the weights are fine-tuned from `laion/CLIP-ViT-L-14-laion2B-s32B-b82K`, whose own licence was not read | `https://raw.githubusercontent.com/Imageomics/bioclip-2/main/LICENSE`, read 10 October 2026 (`runs/fetch/2/bioclip2-gh-LICENSE.txt`) | **ships** as the larger model in `models/naturalist/` (int8 recipe `hybrid-fc2-w8`, 309.8 MB in four parts), downloaded only if the person agrees; also the model of the undeployed service in `service/`. Its rows are made from text (scientific names and phrases for the kinds of eye), so no photo was fitted on for them (`evaluation` in `models/naturalist/manifest.json`) |
| TinyCLIP 8M/16, 40M/32 and 61M/32 (Microsoft) | MIT, the same licence file as TinyCLIP 39M/16 | as above | used for measurement only; 8M/16 was a candidate for the pocket recognizer |
| BioCLIP, ViT-B/16 (Imageomics), `imageomics/bioclip` | MIT | `https://raw.githubusercontent.com/Imageomics/bioclip/main/LICENSE`, read 10 October 2026 (`runs/fetch/2/bioclip-gh-LICENSE.txt`) | used for measurement only |
| BioCLIP 2.5 Huge, ViT-H/14 (Imageomics), `imageomics/bioclip-2.5-vith14` | MIT according to its model card; the repository has no licence file | the model card, `https://huggingface.co/imageomics/bioclip-2.5-vith14`, read 10 October 2026 | used for measurement only. Its card does not date its training data, so no claim the app makes uses its numbers (`docs/EVAL.md`) |
| A third party's distillation of BioCLIP 2.5 to a mobile FastViT (its address is in `tools/lab/models.json`) | MIT according to its card's tag and text; no licence file | its model card, read 10 October 2026 | used for measurement only; it has no text half, so only fitted heads could score it |
| CLIP ViT-B/32 (OpenAI) | MIT for the code and weights repository; the model card puts any deployed use of the model out of scope | `https://raw.githubusercontent.com/openai/CLIP/main/LICENSE` and `model-card.md` in the same repository, read 10 October 2026 | used for measurement only |
| SigLIP 2 base (Google), `google/siglip2-base-patch16-224` | Apache 2.0 according to its model card's tag; the repository has no licence file | the model card, read 10 October 2026 | used for measurement only |
| MobileCLIP (Apple) | Apple Machine Learning Research Model License: use "exclusively for Research Purposes", which "does not include any commercial exploitation, product development or use in any commercial product or service" | `https://raw.githubusercontent.com/apple/ml-mobileclip/main/LICENSE_MODELS`, read 10 October 2026 | **will not ship** |
| MobileCLIP2-S0 (Apple) | not read; taken to carry the same research-only terms as MobileCLIP | | used for measurement only; **will not ship** |

The laboratory's own record of each model, with the licence texts it quotes, is `tools/lab/models.json`.

## In the page

| Thing | Licence | Where the licence was read | Status |
|---|---|---|---|
| ONNX Runtime Web 1.30.0 (Microsoft) | MIT | `vendor/ort/LICENSE`, the LICENSE file of github.com/microsoft/onnxruntime at the tag v1.30.0; the npm package states MIT in its `package.json` and in the header of each script (`vendor/ort/README.txt`) | **ships** in `vendor/ort/`; the laboratory also ran the same package in Node on build machines (`ci/lab/device.sh`) |
| Instrument Serif (typeface) | SIL Open Font License 1.1 | `fonts/OFL-Instrument-Serif.txt` in this repository | **ships** in `fonts/` |
| This project's own code | none chosen yet | | ships without a licence; the choice waits on the owner |

## Data

| Data | Licence | Where the licence was read | Status |
|---|---|---|---|
| The species list for Alachua County and its monthly counts, from GBIF's occurrence API (dataset `50c9509d-22c7-4a22-a47d-8c48425ef4a7`, iNaturalist research-grade observations, records through 2024); English names follow iNaturalist's taxonomy (`data/regions/us-fl-alachua/inat.json`) | not read, for the GBIF dataset and for iNaturalist's taxonomy. An earlier version of this file gave CC BY-NC 4.0 for the dataset without having read it | | **ships** in derived form: names, kinds of eye and monthly weights in `models/pocket/species.json` and `models/naturalist/species.json`. The query is in `data/regions/us-fl-alachua/species.json` (`source.doi_or_query`) |
| The evaluation photos `alachua-2025`: 6,000 research-grade iNaturalist photos dated 2025 and 2026 | each photo's own licence, one per row in the manifest's `licence` column: CC BY-NC 4.0 for 88.6%, CC BY 4.0 for 7.9%, CC0 for 3.4%, CC BY-NC-ND 4.0 for 3 photos (`data/eval/alachua-2025/SUMMARY.md`) | the manifest's `licence` column | used for measurement, and the 1,803 `val` photos also to choose the recognizers' settings. No row of the pocket heads in build 9 was fitted on them (`fitted_on.not_listed` in `models/pocket/manifest.json`); two thirds of the `val` photos fitted the pocket heads of build 8. Photos are downloaded on build machines when a run needs them and are never committed or republished |
| The training photos `train/alachua-pre2025`: 84,808 photos of 5,467 species, from iNaturalist's open-data files, all dated before 2025 | each photo's own licence: CC BY-NC for 73.9%, CC BY 16.0%, CC0 6.3%, CC BY-NC-ND 3.0%, CC BY-NC-SA 0.5%, CC BY-ND 0.2%, CC BY-SA 0.2% (`data/train/alachua-pre2025/SUMMARY.md`). The open-data README says: "Unless the photo license specifies the photo is in the public domain, all photographers retain copyright of their photos, and the license under which the photo is shared dictates how the photo can be used." The licence of the open-data metadata files was not read | `https://raw.githubusercontent.com/inaturalist/inaturalist-open-data/main/README.md`, read 11 October 2026 (fetch run 6, `runs/fetch/6/inat-open-data-readme.md` on `ci`) | used to fit heads: the 81,566 photos that the licence rule admits fitted the pocket heads that ship in build 9 (below). The manifest is on the branch `pub/data-alachua`; no photo is committed |
| COCO 2017: the extra set `coco-kinds`, 10,240 images of people, cats, dogs, horses, cows, sheep and rooms | annotations: Creative Commons Attribution 4.0. Images: "The COCO Consortium does not own the copyright of the images. Use of the images must abide by the Flickr Terms of Use." Each image carries a Flickr licence in COCO's annotation file: of the 9,000 train rows, 2,537 are CC BY-NC-SA 2.0, 2,428 CC BY-NC-ND 2.0, 1,504 CC BY 2.0, 1,219 CC BY-NC 2.0, 828 CC BY-SA 2.0, 463 CC BY-ND 2.0 and 21 "no known copyright restrictions" (`data/extra/coco-kinds/SUMMARY.md`). Flickr's terms of use were not read | COCO's terms of use, `dataset/termsofuse.htm` in github.com/cocodataset/cocodataset.github.io at commit `5e1c4da7`, read 11 October 2026 | used to fit and test the kind decision. The pocket heads in build 9 were fitted on 1,782 train rows that the licence rule admits; those of build 8 were fitted on train rows of every licence. The manifest lists addresses only, and no image is committed or republished |
| TreeOfLife-200M, the training data of BioCLIP 2 | compilation CC0; images under their own licences | `https://huggingface.co/datasets/imageomics/TreeOfLife-200M`, read 10 October 2026 | not used directly. Every evaluation photo is dated after its GBIF snapshot of 2024-05-01, so none can be among BioCLIP 2's training photos (`docs/EVAL.md`) |

## Which photos heads may be fitted on: the rule of 11 October 2026

On 11 October 2026 the coordinator of the overnight work set a rule for the photos a recognizer's heads may be fitted on. The rule is still the coordinator's, and it waits on the owner's decision.

- Heads that ship are fitted only on photos in the public domain (CC0, "no known copyright restrictions", United States Government work) or under CC BY or CC BY-NC.
- Photos under any NoDerivatives (ND) or ShareAlike (SA) licence are left out of fitting.
- The app stays free of charge.
- A list of the photos used (id, address, licence) is published beside the heads as the attribution.

The pocket heads in build 9 ("pocket v3") were fitted under the rule, on 83,348 photos. The `fitted_on` block of `models/pocket/manifest.json` counts them by licence:

| Licence | Photos | From |
|---|---:|---|
| CC BY-NC | 62,694 | the training photos |
| CC BY | 13,555 | the training photos |
| CC0 | 5,317 | the training photos |
| CC BY 2.0 | 974 | COCO |
| CC BY-NC 2.0 | 795 | COCO |
| No known copyright restrictions | 13 | COCO |

That makes 81,566 training photos and 1,782 COCO photos. The rule admits 2,744 of the 9,000 COCO train rows; a third of the extra set's train rows was kept for choosing settings, and nothing was fitted on that third (the same block's `not_listed`). The list of the 83,348 photos, each with its address and licence, is `fitted_on.csv` (about 10 MB) on the branch `pub/heads-pocket-v3` at commit `f0c2544`, a commit that the branch `pin/heads-pocket-v3-f0c2544` keeps alive. The manifest gives the list's address in `fitted_on.list`, and the page's About block links to it (`src/cam.c2.js`). The heads of build 8 predated the rule and did not meet it, because their kind rows were fitted on COCO train rows of every licence, ND and SA ones among them; build 9 replaced them.

## If the app were ever to earn money

The rule admits CC BY-NC photos only while the app stays free of charge. A commercial turn would take the CC BY-NC photos out of the fitting set and leave the 19,859 photos in the public domain or under CC BY (18,872 training photos and 987 COCO photos, `docs/eval/study2-alachua-pre2025-by.json`). Heads fitted on those alone were measured on 11 October (`docs/LOG.md`, 05:06; `docs/eval/shipped-alachua-pre2025-by-tinyclip-39m-16.json`). On the 4,197 test photos they get the kind of eye right for 86.0% (3,609) against 89.1% for pocket v3, put the right species first for 43.8% against 53.8%, and name a species for 509 photos, right for 453 of them (89.0%), where pocket v3 names 845 and is right for 788 (93.3%). The licences of the GBIF dataset behind the species list, of iNaturalist's taxonomy and of the open-data metadata files were not read, and a commercial turn would need them read. BioCLIP 2's own licence is MIT, and the licence of the LAION CLIP weights it was fine-tuned from was not read.

## Tools used to build and measure

None of these ships in the app. Their licences were not read.

| Tool | Used for |
|---|---|
| Playwright, with Chromium, Firefox and WebKit | the browser checks under `test/` and on build machines |
| PyTorch 2.8.0, torchvision 0.23.0, open_clip_torch, timm, transformers, onnx, onnxruntime, onnxconverter-common, huggingface_hub, safetensors | the laboratory on build machines (`.github/workflows/lab.yml`) |
| numpy, Pillow, requests | the evaluation and the data scripts under `tools/` |
| Gradio and the `spaces` package | the species service in `service/`, built and undeployed |
