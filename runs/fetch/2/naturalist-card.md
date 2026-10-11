---
license: mit
library_name: onnxruntime
tags:
  - image-classification
  - clip
  - bioclip
  - on-device
  - onnx
  - mobile
base_model: imageomics/bioclip
---

# Sylva · BioCLIP v1 (image encoder, int8) + text-embedding table

On-device model package for the **Sylva** naturalist app (fungi & plants
identification). This repo hosts a swappable model package consumed via a
[manifest](./manifest.json); the app downloads only what the manifest lists.

## Contents

| File | What |
|---|---|
| `image_encoder.onnx` | BioCLIP v1 **image encoder only** (OpenCLIP ViT-B/16), fp16 weights with **fp32 input/output** (~173 MB). Feed a plain float32 `[1,3,224,224]` tensor; boundary Cast nodes handle fp16 internally. |
| `text_embeddings_v1.safetensors` | Precomputed, L2-normalised text embeddings for the candidate species (fp16, 512-dim). |
| `species_index.json` | `species_id → row` mapping into the table. |
| `manifest.json` | Model manifest (architecture, preprocessing, files + sha256). |
| `registry.json` | Registry entry the app lists in Settings → Models. |

The text encoder is **not** shipped: the candidate list is fixed, so species
names are encoded once offline into the table above. **The table is
model-specific** — v1 embeddings are not compatible with a v2 encoder.

## Inference (how the app uses it)

1. Preprocess per `manifest.preprocess` (CLIP normalisation, 224×224 center crop).
2. Run the image encoder → 512-d embedding, L2-normalise.
3. Cosine similarity against `text_embeddings` → softmax (`logit_scale`) → top-N.
4. Join `species_id` to the app's curated species/toxicity DB.

## Provenance & quality

- Derived from [`imageomics/bioclip`](https://huggingface.co/imageomics/bioclip)
  (OpenCLIP ViT-B/16). Only the image tower is exported.
- Precision: **fp16**. Validated cosine similarity of embeddings fp16-vs-fp32 on
  control inputs = **1.000** (target ≥ 0.99).
- A compact high-accuracy **int8** encoder (static/QDQ with a calibration set,
  or a distilled tower) is planned follow-up: plain dynamic int8 on this ViT
  lands at ~0.97 cosine, below the quality bar, so v1 ships fp16 (§13).

## ⚠️ Safety

This model outputs a **taxon only**. It is **not** a source of edibility
information and must never be used to decide whether something is safe to eat.
Fungi identification is error-prone (fine-grained, deadly look-alikes). The
Sylva app keeps toxicity in a separate curated layer and always shows warnings
and look-alikes. Consult an expert before consuming any wild organism.

The candidate species list in this v1 package is a small **seed** for the MVP
and will be expanded (regional/frequency-based) in later revisions without an
app update.
