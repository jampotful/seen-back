ONNX Runtime Web 1.30.0, copied unchanged from the npm package onnxruntime-web@1.30.0 (directory dist/).

  ort.wasm.min.js                 sha256 faece07e84faa9001f5104bbe4e5c70861d06cb2376a0dea1fa0ad33a67adc81   the runtime's JavaScript, WebAssembly backend only
  ort-wasm-simd-threaded.mjs      sha256 e13f7f94fc51b4ca72b12faeb1ee95f4ace6dfbc8939bc718aabdc0a27c4299b   the loader for the WebAssembly file
  ort-wasm-simd-threaded.wasm     sha256 3398c10d07d229bd91b364548e130e0e51a8e5704b88c7c083ebbeb78842dee2   the runtime itself (CPU, with SIMD)

Licence: MIT, Copyright (c) Microsoft Corporation. The npm package states "license": "MIT" in its package.json and in the
header of each script, and carries no licence file of its own; LICENSE here is the file of that name from
https://github.com/microsoft/onnxruntime at the tag v1.30.0.

To move to another release: replace the three files, change ORT.v and ORT.wasmBytes in src/cam.rec.js and ORT_V in src/sw.template.js.
