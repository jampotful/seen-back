# Quantized vectors against the original model's vectors

_This file is written by `tools/eval/report.py` from `docs/eval/study1.json`. Rerun the script to change it._

The same 4197 test photos, the same settings as for the original vectors. `int8*` vectors were computed by onnxruntime on a build machine; `wasm-int8-per-channel` vectors were computed by the browser's WASM runtime, which is what a phone runs. Differences are paired over photos.

| Model | Vectors | Mean cosine to original | 1st percentile | Kind from phrases | Difference (points) | Species top-1 with prior | Difference (points) |
|---|---|---:|---:|---:|---:|---:|---:|
| bioclip-b16 | int8-per-tensor | 0.9592 | 0.8717 | 46.5% (45.0 to 47.9) | +1.0 (+0.2 to +1.8) | 65.5% (64.0 to 66.9) | -4.1 (-4.8 to -3.3) |
| tinyclip-39m-16 | int8 | 0.9967 | 0.9927 | 77.5% (76.1 to 78.8) | -0.1 (-0.6 to +0.3) | 34.9% (33.5 to 36.4) | -0.3 (-0.8 to +0.1) |
| tinyclip-39m-16 | int8-per-channel | 0.9965 | 0.9921 | 77.2% (76.0 to 78.5) | -0.4 (-0.8 to +0.1) | 34.5% (33.1 to 36.0) | -0.7 (-1.2 to -0.3) |
| tinyclip-39m-16 | int8-per-tensor | 0.9957 | 0.9903 | 77.2% (75.9 to 78.5) | -0.4 (-0.8 to +0.1) | 34.8% (33.4 to 36.2) | -0.4 (-0.9 to +0.1) |
| tinyclip-39m-16 | wasm-int8-per-channel | 0.9984 | 0.9965 | 77.3% (76.0 to 78.7) | -0.2 (-0.6 to +0.1) | 34.8% (33.3 to 36.2) | -0.5 (-0.9 to -0.1) |
| tinyclip-8m-16 | int8 | 0.9971 | 0.9937 | 71.9% (70.5 to 73.4) | -0.1 (-0.6 to +0.4) | 26.2% (25.0 to 27.5) | -0.1 (-0.6 to +0.3) |
| tinyclip-8m-16 | int8-per-channel | 0.9971 | 0.9937 | 71.9% (70.5 to 73.4) | -0.1 (-0.6 to +0.4) | 26.2% (25.0 to 27.5) | -0.1 (-0.6 to +0.3) |
| tinyclip-8m-16 | int8-per-tensor | 0.9958 | 0.9909 | 72.1% (70.8 to 73.6) | +0.1 (-0.4 to +0.6) | 25.7% (24.4 to 27.0) | -0.7 (-1.2 to -0.1) |
| tinyclip-8m-16 | wasm-int8-per-channel | 0.9980 | 0.9956 | 72.4% (71.0 to 73.8) | +0.4 (-0.1 to +0.9) | 26.1% (24.8 to 27.4) | -0.3 (-0.7 to +0.2) |
| tinyclip-61m-32 | int8 | 0.9929 | 0.9857 | 72.0% (70.6 to 73.5) | -0.6 (-1.1 to +0.0) | 27.6% (26.3 to 29.0) | -0.2 (-0.7 to +0.2) |
| tinyclip-61m-32 | int8-per-channel | 0.8579 | 0.7851 | 72.5% (71.1 to 73.8) | -0.1 (-0.9 to +0.7) | 22.9% (21.6 to 24.2) | -5.0 (-5.9 to -4.1) |
| tinyclip-61m-32 | int8-per-tensor | 0.9896 | 0.9772 | 72.1% (70.7 to 73.5) | -0.5 (-1.1 to +0.1) | 27.2% (25.9 to 28.6) | -0.6 (-1.1 to -0.1) |
| tinyclip-40m-32 | int8 | 0.9919 | 0.9838 | 69.4% (68.0 to 70.9) | +0.1 (-0.5 to +0.7) | 25.8% (24.6 to 27.2) | -0.9 (-1.4 to -0.4) |
| tinyclip-40m-32 | int8-per-channel | 0.9919 | 0.9838 | 69.4% (68.0 to 70.9) | +0.1 (-0.5 to +0.7) | 25.8% (24.6 to 27.2) | -0.9 (-1.4 to -0.4) |
| tinyclip-40m-32 | int8-per-tensor | 0.9851 | 0.9659 | 69.0% (67.5 to 70.4) | -0.4 (-1.0 to +0.3) | 25.6% (24.3 to 27.0) | -1.1 (-1.7 to -0.5) |
