# Encoder speed in headless Chromium

Made by `tools/world/speed.mjs`: session.run wall time per photo, batch 1, 224 x 224, onnxruntime-web 1.30.0 (vendor/ort, the WASM build the page loads); Chromium 141.0.7390.37, headless; 4 cores (AMD EPYC 9V74 80-Core Processor), 15.6 GB; the page cross-origin isolated: true. 30 timed photos a measurement after 2 to warm up, 3 rounds taking turns. The input is a fixed made-up picture: the encoders do the same work whatever the picture shows.

| Model file | bytes | threads | median ms a photo | 90th percentile | medians of the rounds | session made in ms |
|---|---:|---:|---:|---:|---|---|
| bioclip-b16 | 89,802,361 | 1 | 586.5 | 590.8 | 587.4, 587.8, 586 | 504.1, 286.7, 276.4 |
| bioclip-b16 | 89,802,361 | 4 | 305.2 | 320.9 | 306.1, 306.4, 303.3 | 548.9, 534.6, 534.3 |
| tinyclip-39m-16 | 40,978,137 | 1 | 296.3 | 298.6 | 296.2, 296.4, 296.5 | 172.3, 176.7, 181.7 |
| tinyclip-39m-16 | 40,978,137 | 4 | 152.7 | 160.7 | 156.6, 152.1, 152.7 | 423.8, 435, 435.4 |

Against TinyCLIP 39M/16 at the same thread count:
- bioclip-b16, 1 thread(s): 1.98 times as long (586.5 ms against 296.3 ms).
- bioclip-b16, 4 thread(s): 2.00 times as long (305.2 ms against 152.7 ms).
