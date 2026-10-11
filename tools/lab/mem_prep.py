"""Inputs for the memory runs (ci/lab/mem.sh): test photos as pixels, and the shipped file in other forms.

  python3 tools/lab/mem_prep.py pixels --manifest CSV --photos DIR --out DIR [--select 320] [--take 24]
      The first <take> of the <select> test rows that device.py select picks (every k-th test row), so their ids are the
      first ones in the published vectors on pub/model-bioclip2-l14 (vectors/hybrid-fc2-w8.alachua-2025-test320.*).
      Pixels as the laboratory states BioCLIP 2's preprocessing (parts.json): shortest side to 224 with PIL bicubic, the
      other side int(224 * long / short), centre crop with Python round. Writes u8.bin (uint8 N,3,224,224), ids.json,
      norm.json, and sel_manifest.csv (the rows, for the photo fetcher).
  python3 tools/lab/mem_prep.py ort --model ONNX --out ORT [--level basic|disabled]
      The same graph in ORT format, saved by onnxruntime (Python) after the chosen optimization level.
  python3 tools/lab/mem_prep.py preopt --model ONNX --out ONNX2 [--level extended] [--external NAME]
      The graph after onnxruntime's (Python, CPU) optimizations up to the chosen level, saved as ONNX, its weights
      optionally in an external data file NAME beside it.
  python3 tools/lab/mem_prep.py external --model ONNX --out GRAPH --weights NAME
      The same graph with every tensor of 1 kB or more in one external data file NAME beside GRAPH.
"""
import argparse
import csv
import json
import pathlib
import subprocess
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
MEAN = [0.48145466, 0.4578275, 0.40821073]
STD = [0.26862954, 0.26130258, 0.27577711]


def pixels(a):
    from PIL import Image

    rows = [r for r in csv.DictReader(open(a.manifest, newline="", encoding="utf-8")) if r.get("split") == "test"]
    step = max(1, len(rows) // a.select)
    sel = rows[::step][:a.select][:a.take]
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    with open(out / "sel_manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in sel:
            w.writerow(r)
    subprocess.run([sys.executable, str(ROOT / "tools/lab/fetch_photos.py"), str(out / "sel_manifest.csv"), a.photos], check=False)
    S = 224
    ids, bad = [], []
    with open(out / "u8.bin", "wb") as fh:
        for r in sel:
            p = pathlib.Path(a.photos) / ("%s.jpg" % r["id"])
            try:
                im = Image.open(p)
                im.load()
                im = im.convert("RGB")
            except Exception as e:  # noqa: BLE001
                bad.append([r["id"], str(e)[:100]])
                continue
            W, H = im.size
            if W <= H:
                nw, nh = S, int(S * H / W)
            else:
                nw, nh = int(S * W / H), S
            im = im.resize((nw, nh), Image.BICUBIC)
            left, top = int(round((nw - S) / 2.0)), int(round((nh - S) / 2.0))
            im = im.crop((left, top, left + S, top + S))
            fh.write(np.ascontiguousarray(np.asarray(im, dtype=np.uint8).transpose(2, 0, 1)).tobytes())
            ids.append(r["id"])
    (out / "ids.json").write_text(json.dumps(ids))
    (out / "norm.json").write_text(json.dumps({"mean": MEAN, "std": STD, "size": S, "layout": "uint8 NCHW, RGB", "count": len(ids),
                                               "skipped": bad, "select": a.select, "step": step}))
    print("pixels: %d photos (%d skipped), every %d-th test row" % (len(ids), len(bad), step))


def to_ort(a):
    import onnxruntime as ort

    so = ort.SessionOptions()
    so.graph_optimization_level = {"disabled": ort.GraphOptimizationLevel.ORT_DISABLE_ALL,
                                   "basic": ort.GraphOptimizationLevel.ORT_ENABLE_BASIC}[a.level]
    so.optimized_model_filepath = a.out
    so.add_session_config_entry("session.save_model_format", "ORT")
    ort.InferenceSession(a.model, so, providers=["CPUExecutionProvider"])
    print("ORT format (%s, onnxruntime %s): %d bytes" % (a.level, ort.__version__, pathlib.Path(a.out).stat().st_size))


def preopt(a):
    import onnxruntime as ort

    so = ort.SessionOptions()
    so.graph_optimization_level = {"basic": ort.GraphOptimizationLevel.ORT_ENABLE_BASIC,
                                   "extended": ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED}[a.level]
    so.optimized_model_filepath = a.out
    if a.external:
        so.add_session_config_entry("session.optimized_model_external_initializers_file_name", a.external)
        so.add_session_config_entry("session.optimized_model_external_initializers_min_size_in_bytes", "1024")
    ort.InferenceSession(a.model, so, providers=["CPUExecutionProvider"])
    g = pathlib.Path(a.out)
    print("optimized ONNX (%s, onnxruntime %s): graph %d bytes%s" % (a.level, ort.__version__, g.stat().st_size,
          (", %s %d bytes" % (a.external, (g.parent / a.external).stat().st_size)) if a.external else ""))


def external(a):
    import onnx

    m = onnx.load(a.model)
    onnx.save_model(m, a.out, save_as_external_data=True, all_tensors_to_one_file=True, location=a.weights, size_threshold=1024)
    g = pathlib.Path(a.out)
    print("external data: graph %d bytes, %s %d bytes" % (g.stat().st_size, a.weights, (g.parent / a.weights).stat().st_size))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pixels")
    p.add_argument("--manifest", required=True)
    p.add_argument("--photos", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--select", type=int, default=320)
    p.add_argument("--take", type=int, default=24)
    o = sub.add_parser("ort")
    o.add_argument("--model", required=True)
    o.add_argument("--out", required=True)
    o.add_argument("--level", default="basic", choices=["basic", "disabled"])
    q = sub.add_parser("preopt")
    q.add_argument("--model", required=True)
    q.add_argument("--out", required=True)
    q.add_argument("--level", default="extended", choices=["basic", "extended"])
    q.add_argument("--external", default="")
    e = sub.add_parser("external")
    e.add_argument("--model", required=True)
    e.add_argument("--out", required=True)
    e.add_argument("--weights", required=True)
    a = ap.parse_args()
    {"pixels": pixels, "ort": to_ort, "preopt": preopt, "external": external}[a.cmd](a)


if __name__ == "__main__":
    main()
