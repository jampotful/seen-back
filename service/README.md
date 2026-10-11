---
title: Seen Back naturalist
colorFrom: green
colorTo: gray
sdk: gradio
sdk_version: 6.30.0
python_version: "3.10"
app_file: app.py
pinned: false
short_description: Names the species in a photo for the Seen Back app
models:
  - imageomics/bioclip-2
---

# Seen Back naturalist

The species service for [Seen Back](https://jampotful.github.io/seen-back/), a web app in which you photograph a living
thing and your phone's camera view changes toward that creature's way of seeing. The app decides the kind of eye on the
phone itself; when the person agrees to send the photo, this service names the species.

## What it does

It runs [BioCLIP 2](https://huggingface.co/imageomics/bioclip-2) (ViT-L/14, MIT licence,
[licence text](https://raw.githubusercontent.com/Imageomics/bioclip-2/main/LICENSE)) on the photo and scores the result
against the 5,911 species recorded in Alachua County, Florida, by their scientific names, weighted by how often each
species was recorded in the photo's month. The species list and its monthly counts come from iNaturalist research-grade
observations through GBIF, recorded through 2024. The settings (temperature 30, prior weight 0.25) are provisional.

On ZeroGPU the image encoder runs on a GPU for a fraction of a second per photo; elsewhere it runs on the processor.

## Photos are not kept

Each photo is read in memory, answered, and dropped. Nothing is written to disk. The log holds a running count of
requests and the time each took, nothing about the photo.

## API

One endpoint, `identify`, called in Gradio's two steps:

```
POST https://<this space>.hf.space/gradio_api/call/identify
     {"data": [<photo as a base64 JPEG string>, <month 1-12>, <"us-fl-alachua" or "">, <how many species, at most 10>]}
  -> {"event_id": "..."}
GET  https://<this space>.hf.space/gradio_api/call/identify/<event_id>
  -> server-sent events; the `complete` event's data is [result]
```

The result:

```json
{"model": "bioclip2-l14", "region": "us-fl-alachua", "ms": 180, "device": "cuda", "provisional": true,
 "species": [{"key": 9630752, "sci": "Ardea herodias", "en": "Great Blue Heron", "eyes": "wader", "p": 0.83}],
 "kinds": [{"key": "wader", "p": 0.97}]}
```

`key` is the GBIF species key, `eyes` the kind of eye the app uses for that species, `kinds` the species probabilities
summed by kind of eye. An empty region answers from the same list without the month's weights and adds a `note`.
A refusal is a result with `error` (a plain sentence) and `code`: `too_large` (over 1.5 MB), `not_image`, `no_image`,
`bad_month`, `unknown_region`, `rate_limited`.

`GET /v1/health` answers at once: `{"ok": true, "ready": true, "model": "bioclip2-l14", "species": 5911, ...}`.

## Manners

It answers pages from `https://jampotful.github.io` and from `http://localhost` and `http://127.0.0.1`, and this Space's
own page; requests from other pages are refused. At most two photos are worked on at once, with a short queue, and
one address may send at most thirty photos a minute.

## Source

The code lives in the `service/` folder of [jampotful/seen-back](https://github.com/jampotful/seen-back). The label rows
and species table under `heads/` are made by `ci/service/build_heads.py` there from the project's species list and the
model's text embeddings of the scientific names.
