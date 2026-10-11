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
| TinyCLIP (Microsoft) | MIT | `https://raw.githubusercontent.com/microsoft/Cream/main/TinyCLIP/LICENSE`, read 10 October 2026 | candidate |
| CLIP ViT-B/32 (OpenAI) | MIT for the code and weights repository; the model card adds that deployed use is "currently out of scope" | `https://raw.githubusercontent.com/openai/CLIP/main/LICENSE`, read 10 October 2026 | measured for comparison |
| BioCLIP (Imageomics) | MIT | `https://raw.githubusercontent.com/Imageomics/bioclip/main/LICENSE`, read 10 October 2026 | candidate |
| BioCLIP 2 (Imageomics) | MIT | `https://raw.githubusercontent.com/Imageomics/bioclip-2/main/LICENSE`, read 10 October 2026 | candidate |
| BioCLIP 2.5 Huge (Imageomics) | MIT according to its model card; no licence file in the repository | `https://huggingface.co/imageomics/bioclip-2.5-vith14`, read 10 October 2026 | candidate |
| SigLIP 2 base (Google) | Apache 2.0 according to its model card | `https://huggingface.co/google/siglip2-base-patch16-224`, read 10 October 2026 | measured for comparison |
| MobileCLIP2 (Apple) | not read; assumed the same research-only terms as MobileCLIP | | **will not ship**; measured for comparison |
| ONNX Runtime Web 1.30.0 (Microsoft) | MIT | `vendor/ort/LICENSE`, the LICENSE file of github.com/microsoft/onnxruntime at tag v1.30.0; the npm package states MIT in package.json | ships |

## Data

| Thing | Licence | Read at | State |
|---|---|---|---|
| GBIF occurrence counts | Each dataset's own; the iNaturalist research-grade dataset is CC BY-NC 4.0 | *to read* | used to build species lists; cite the download or query |
| iNaturalist photos used for evaluation | Each photo's own Creative Commons licence, recorded per row in the manifest | manifest column `licence` | downloaded when an evaluation runs; never redistributed here |
| TreeOfLife-200M (training data of BioCLIP 2) | Compilation CC0; images under their own licences | `https://huggingface.co/datasets/imageomics/TreeOfLife-200M`, read 10 October 2026 | not used directly; its GBIF snapshot date (2024-05-01) sets our evaluation window |
