# Licences

Everything that ships in the app or is used to build it, with its licence and where the licence was read. A row marked *to read* has only been seen as a tag and must be read before the thing ships.

## In the app

| Thing | Licence | Read at | State |
|---|---|---|---|
| Instrument Serif (typeface) | SIL Open Font License 1.1 | `fonts/OFL-Instrument-Serif.txt` in this repository | ships |

## Candidates for recognition

| Thing | Licence | Read at | State |
|---|---|---|---|
| MobileCLIP weights (Apple) | Apple Machine Learning Research Model License: use "exclusively for Research Purposes", which "does not include any commercial exploitation, product development or use in any commercial product or service" | `https://raw.githubusercontent.com/apple/ml-mobileclip/main/LICENSE_MODELS`, read 10 October 2026 | **will not ship**; may be measured for comparison |
| TinyCLIP (Microsoft) | MIT (tag) | *to read* | candidate |
| CLIP ViT-B/32 (OpenAI) | MIT (tag) | *to read* | candidate |
| BioCLIP (Imageomics) | MIT (tag) | *to read* | candidate |
| BioCLIP 2 (Imageomics) | MIT (tag) | *to read* | candidate |
| BioCLIP 2.5 Huge (Imageomics) | MIT (tag) | *to read* | candidate |
| ONNX Runtime Web (Microsoft) | MIT (tag) | *to read* | candidate |

## Data

| Thing | Licence | Read at | State |
|---|---|---|---|
| GBIF occurrence counts | Each dataset's own; the iNaturalist research-grade dataset is CC BY-NC 4.0 | *to read* | used to build species lists; cite the download or query |
| iNaturalist photos used for evaluation | Each photo's own Creative Commons licence, recorded per row in the manifest | manifest column `licence` | downloaded when an evaluation runs; never redistributed here |
| TreeOfLife-200M (training data of BioCLIP 2) | Compilation CC0; images under their own licences | `https://huggingface.co/datasets/imageomics/TreeOfLife-200M`, read 10 October 2026 | not used directly; its GBIF snapshot date (2024-05-01) sets our evaluation window |
