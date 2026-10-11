"""A large open_clip image encoder for the device: ONNX files made several ways, measured through onnxruntime-web's WASM
build (the runtime the page uses), the best int8 file cut into parts for a browser to fetch.

  python3 tools/lab/device.py select --manifest CSV --split test --n 320 --out rows.json
  python3 tools/lab/device.py make   --model ID --manifest CSV --rows rows.json --photos DIR --recipes a,b --work DIR --pix DIR
  python3 tools/lab/device.py score  --manifest CSV --ref-npy F --ref-ids F --slot DIR --runs DIR... --out results.json
  python3 tools/lab/device.py parts  --file F --size 90000000 --out DIR --meta results.json --name vision.int8.onnx

Recipes (each a file made from the exported float32 encoder):
  int8-per-channel   dynamic int8 (activations quantized at run time), signed 8-bit weights per output channel
  uint8-per-channel  the same with unsigned 8-bit weights
  int8-per-tensor    dynamic int8, one scale per weight matrix
  w8-float           8-bit weights per output column stored with a DequantizeLinear; float activations and arithmetic
  hybrid-fc2-w8      dynamic int8 per channel everywhere except each block's second MLP layer (mlp.c_proj), whose input
                     (after GELU) carries the outliers that per-tensor activation scales handle worst; that layer keeps
                     8-bit weights with float arithmetic, so the file stays the size of the int8 file
  w4-block32         MatMulNBits, 4-bit weights in blocks of 32 along the input (weights only; float activations)
  fp16               float16 throughout (convert_float_to_float16, keep_io_types)
Pixels are written exactly as the model's own preprocessing makes them (open_clip: torchvision Resize and CenterCrop on
the PIL image), as uint8, so that the WASM run sees what the original model saw.
"""
import argparse
import hashlib
import json
import math
import os
import pathlib
import sys
import time

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import lab  # noqa: E402  (tools/lab/lab.py)

HOW = {
    "int8-per-channel": "onnxruntime.quantization.quantize_dynamic: MatMul and Gemm with constant weights, weight_type QInt8, per_channel=True, reduce_range=False, MatMulConstBOnly; activations quantized at run time (DynamicQuantizeLinear + MatMulInteger)",
    "uint8-per-channel": "as int8-per-channel with weight_type QUInt8 (unsigned 8-bit weights)",
    "int8-per-tensor": "as int8-per-channel with per_channel=False",
    "w8-float": "every MatMul with a constant 2-D weight: symmetric 8-bit weights, one scale per output column, DequantizeLinear in front; activations and arithmetic stay float32",
    "hybrid-fc2-w8": "int8-per-channel for every MatMul except the 24 blocks' mlp.c_proj (second MLP layer), which get w8-float",
    "w4-block32": "onnxruntime MatMulNBitsQuantizer: 4-bit symmetric weights in blocks of 32 (MatMulNBits); activations float",
    "fp16": "onnxruntime.transformers.float16.convert_float_to_float16(keep_io_types=True)",
}
INT8_FAMILY = ("int8-per-channel", "uint8-per-channel", "int8-per-tensor", "w8-float", "hybrid-fc2-w8")


def sha256(p):
    return lab.sha256(p)


def select(args):
    rows = [r for r in lab.read_manifest(args.manifest) if r.get("split") == args.split]
    step = max(1, len(rows) // args.n)
    sel = rows[::step][:args.n]
    pathlib.Path(args.out).write_text(json.dumps({"manifest_rows_in_split": len(rows), "step": step, "split": args.split,
                                                  "ids": [r["id"] for r in sel]}) + "\n")
    print("selected %d of %d %s rows (every %d-th)" % (len(sel), len(rows), args.split, step))


def fc2_nodes(path):
    import onnx

    m = onnx.load(str(path), load_external_data=False)
    names = [nd.name for nd in m.graph.node if nd.op_type in ("MatMul", "Gemm") and "mlp/c_proj" in nd.name]
    return names


def make_recipe(tag, fp32, dst, work):
    from onnxruntime.quantization import QuantType, quantize_dynamic

    common = dict(op_types_to_quantize=["MatMul", "Gemm"], extra_options={"MatMulConstBOnly": True})
    info = {"how": HOW.get(tag, tag)}
    if tag == "int8-per-channel":
        quantize_dynamic(str(fp32), str(dst), weight_type=QuantType.QInt8, per_channel=True, reduce_range=False, **common)
    elif tag == "uint8-per-channel":
        quantize_dynamic(str(fp32), str(dst), weight_type=QuantType.QUInt8, per_channel=True, reduce_range=False, **common)
    elif tag == "int8-per-tensor":
        quantize_dynamic(str(fp32), str(dst), weight_type=QuantType.QInt8, per_channel=False, reduce_range=False, **common)
    elif tag == "w8-float":
        lab.weight_only_int8(fp32, dst)
    elif tag == "hybrid-fc2-w8":
        ex = fc2_nodes(fp32)
        info["kept_float_arithmetic"] = len(ex)
        info["example_node"] = ex[0] if ex else None
        if not ex:
            raise SystemExit("hybrid: no mlp/c_proj MatMul found by node name")
        mid = pathlib.Path(work) / "_hybrid_mid.onnx"
        quantize_dynamic(str(fp32), str(mid), weight_type=QuantType.QInt8, per_channel=True, reduce_range=False,
                         nodes_to_exclude=ex, **common)
        lab.weight_only_int8(mid, dst)
        mid.unlink()
    elif tag == "w4-block32":
        import onnx

        try:
            from onnxruntime.quantization.matmul_nbits_quantizer import MatMulNBitsQuantizer as Q
        except ModuleNotFoundError:
            # onnxruntime's NBits quantizer imports onnx_ir, which is not among its own requirements
            import subprocess
            subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "onnx-ir"], check=False)
            from onnxruntime.quantization.matmul_nbits_quantizer import MatMulNBitsQuantizer as Q
        q = Q(onnx.load(str(fp32)), block_size=32, is_symmetric=True)
        q.process()
        q.model.save_model_to_file(str(dst), use_external_data_format=False)
    elif tag == "fp16":
        import onnx

        try:
            from onnxruntime.transformers.float16 import convert_float_to_float16
        except Exception:
            from onnxconverter_common.float16 import convert_float_to_float16
        onnx.save(convert_float_to_float16(onnx.load(str(fp32)), keep_io_types=True), str(dst))
    else:
        raise SystemExit("unknown recipe %s" % tag)
    ops, opset = lab.onnx_ops(dst)
    info.update({"bytes": dst.stat().st_size, "mb": round(dst.stat().st_size / 1e6, 2), "sha256": sha256(dst), "ops": ops})
    return info


def openclip_pixels(m, im):
    """The model's own transforms up to (not including) ToTensor and Normalize, on the PIL image; returns uint8 CHW and a
    record of the sizes, for checking the written-down rule against what the transforms did."""
    from PIL import Image  # noqa: F401

    w0, h0 = im.size
    rec = {"w": w0, "h": h0}
    for t in m.preprocess.transforms:
        name = type(t).__name__
        if name in ("ToTensor", "MaybeToTensor", "Normalize"):
            continue
        if name == "CenterCrop":
            rec["resized"] = list(im.size)
            cs = t.size[0] if isinstance(t.size, (list, tuple)) else t.size
            W, H = im.size
            # the rule as written in parts.json: top = round((H - S) / 2), left = round((W - S) / 2), Python's round
            left, top = int(round((W - cs) / 2.0)), int(round((H - cs) / 2.0))
            want = np.asarray(im.crop((left, top, left + cs, top + cs)))
            im = t(im)
            rec["crop_rule_ok"] = bool(np.array_equal(want, np.asarray(im)))
            continue
        im = t(im)
    a = np.asarray(im, dtype=np.uint8)
    if a.ndim != 3 or a.shape[2] != 3:
        raise SystemExit("pixels: expected HxWx3 after the transforms, got %s" % (a.shape,))
    return np.ascontiguousarray(a.transpose(2, 0, 1)), rec


def make(args):
    import torch

    entry = lab.model_entry(args.model)
    if entry["loader"] != "open_clip":
        raise SystemExit("device.py make: open_clip models only")
    work, pix = pathlib.Path(args.work), pathlib.Path(args.pix)
    work.mkdir(parents=True, exist_ok=True)
    pix.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    m = lab.load(entry)
    card = lab.base_card(entry, m)
    size = card["input"]["size"]
    summary = {"model": entry["id"], "source": entry["source"], "source_url": entry.get("source_url"),
               "licence": entry.get("licence"), "licence_url": entry.get("licence_url"), "params": card["params"],
               "input": card["input"], "preprocess_detail": card["preprocess_detail"], "software": lab.versions(),
               "cpu": lab.cpu_info(), "recipes": {}, "timings": {}}
    fp32 = work / "vision.fp32.onnx"
    t1 = time.time()
    lab.export_onnx(m, fp32, size, 17)
    summary["timings"]["export_s"] = round(time.time() - t1, 1)
    summary["fp32"] = {"bytes": fp32.stat().st_size, "sha256": sha256(fp32)}
    lab.log("exported fp32: %.1f MB in %.1fs" % (fp32.stat().st_size / 1e6, time.time() - t1))
    for tag in [r for r in args.recipes.split(",") if r]:
        t1 = time.time()
        dst = work / ("vision.%s.onnx" % tag)
        try:
            info = make_recipe(tag, fp32, dst, work)
            info["seconds"] = round(time.time() - t1, 1)
        except BaseException as e:  # noqa: BLE001 - one recipe failing must not cost the others
            info = {"how": HOW.get(tag, tag), "error": "%s: %s" % (type(e).__name__, str(e)[:1500])}
        summary["recipes"][tag] = info
        lab.log("%s: %s" % (tag, json.dumps({k: v for k, v in info.items() if k != "ops"})))
    # pixels for the chosen rows, as uint8, and the original model's vectors for the first few (a same-machine check of
    # the published vectors and of the pixel path)
    sel = json.loads(pathlib.Path(args.rows).read_text())["ids"]
    ok, bad = lab.iter_photos([{"id": i} for i in sel], args.photos)
    ids, recs = [], []
    with open(pix / "u8.bin", "wb") as fh:
        for rid, p in ok:
            try:
                u, rec = openclip_pixels(m, lab.open_rgb(p))
            except Exception as e:  # noqa: BLE001
                bad.append((rid, "unreadable: %s" % type(e).__name__))
                continue
            if u.shape != (3, size, size):
                bad.append((rid, "shape %s" % (u.shape,)))
                continue
            fh.write(u.tobytes())
            ids.append(rid)
            recs.append(rec)
    mean, std = card["input"]["mean"], card["input"]["std"]
    (pix / "ids.json").write_text(json.dumps(ids))
    (pix / "skipped.json").write_text(json.dumps(bad))
    (pix / "norm.json").write_text(json.dumps({"mean": mean, "std": std, "size": size, "layout": "uint8 NCHW, RGB", "count": len(ids)}))
    summary["pixels"] = {"photos": len(ids), "skipped": bad, "crop_rule_ok": sum(1 for r in recs if r.get("crop_rule_ok")),
                         "crop_rule_checked": sum(1 for r in recs if "crop_rule_ok" in r), "examples": recs[:5]}
    k = min(args.ref_n, len(ids))
    if k:
        u8 = np.fromfile(pix / "u8.bin", dtype=np.uint8, count=k * 3 * size * size).reshape(k, 3, size, size)
        x = (u8.astype(np.float32) / 255.0 - np.array(mean, np.float32)[None, :, None, None]) / np.array(std, np.float32)[None, :, None, None]
        ims = [lab.open_rgb(pathlib.Path(args.photos) / ("%s.jpg" % i)) for i in ids[:k]]
        pv = m.pixel_values(ims).numpy().astype(np.float32)
        summary["pixels"]["max_abs_diff_vs_model_transform"] = float(np.abs(pv - x).max())
        with torch.no_grad():
            ref = m.encode_pixels(torch.from_numpy(pv))
        np.save(work / "torch_ref.npy", lab.unit(ref).astype(np.float32))
        (work / "torch_ref.ids.json").write_text(json.dumps(ids[:k]))
    summary["timings"]["total_s"] = round(time.time() - t0, 1)
    pathlib.Path(args.summary).write_text(json.dumps(summary, indent=1) + "\n")
    fp32.unlink()


def score(args):
    sys.path.insert(0, str(lab.ROOT / "tools" / "fusion"))
    import fuse as F

    rows = {r["id"]: r for r in lab.read_manifest(args.manifest)}
    ref_v = np.load(args.ref_npy).astype(np.float64)
    ref_ids = json.loads(pathlib.Path(args.ref_ids).read_text())
    ref = {i: ref_v[k] for k, i in enumerate(ref_ids)}
    slot = F.load_slot(args.slot)
    man, table = slot["manifest"], slot["table"]

    def judge(vecs):
        top1 = top5 = named = named_ok = 0
        for rid, e in vecs:
            r = rows[rid]
            month = int(r["month"]) - 1 if (r.get("month") or "").isdigit() else None
            out = F.fuse(man, table, month, F.dots(slot["kinds"], e), F.dots(slot["species"], e),
                         kind_bias=slot["kind_bias"], species_bias=slot["species_bias"])
            sp = [s["sci"] for s in out["species"]]
            top1 += sp[0] == r["sci"]
            top5 += r["sci"] in sp
            if out["named"] is not None:
                named += 1
                named_ok += out["named"]["sci"] == r["sci"]
        n = len(vecs)
        return {"n": n, "top1": round(100.0 * top1 / max(n, 1), 2), "top5": round(100.0 * top5 / max(n, 1), 2),
                "top1_count": int(top1), "top5_count": int(top5), "named": named, "named_right": named_ok}

    runs = {}
    for d in args.runs:
        d = pathlib.Path(d)
        for sj in d.rglob("device_summary.json"):
            s = json.loads(sj.read_text())
            for tag, info in s.get("recipes", {}).items():
                vf = sj.parent / ("wasm_%s.f16.npy" % tag)
                rec = dict(info)
                rec["job"] = sj.parent.name
                if vf.exists():
                    v = np.load(vf).astype(np.float64)
                    ids = json.loads((sj.parent / ("wasm_%s.ids.json" % tag)).read_text())
                    rec["_vecs"] = list(zip(ids, v))
                for lat in ("latency_1", "latency_4"):
                    lf = sj.parent / ("wasm_%s.%s.json" % (tag, lat))
                    if lf.exists():
                        L = json.loads(lf.read_text())
                        ms = L.get("ms", [])
                        rec[lat] = {"threads": L.get("threads"), "photos": len(ms), "mean_ms": round(float(np.mean(ms)), 1) if ms else None,
                                    "median_ms": round(float(np.median(ms)), 1) if ms else None, "min_ms": round(float(np.min(ms)), 1) if ms else None,
                                    "load_ms": L.get("load_ms"), "runtime": L.get("runtime"), "node": L.get("node")}
                    elif (sj.parent / ("wasm_%s.%s.err" % (tag, lat))).exists():
                        rec[lat] = {"error": (sj.parent / ("wasm_%s.%s.err" % (tag, lat))).read_text()[-600:]}
                runs[tag] = rec
    full = [t for t, r in runs.items() if r.get("_vecs") and len(r["_vecs"]) >= args.min_photos]
    common = set(ref)
    for t in full:
        common &= {i for i, _ in runs[t]["_vecs"]}
    order = {i: k for k, i in enumerate(rows)}
    common = sorted(common, key=lambda i: order[i]) if common else []
    res = {"photos_common": len(common), "about": "species scored with tools/fusion/fuse.py against the published server rows "
           "(slot %s) with its fusion settings and the month prior; cosine is to the original model's published vectors "
           "(pub/lab-%s images/%s)" % (args.slot_name, args.model, args.ref_name), "slot_fusion": man.get("fusion"),
           "original": judge([(i, ref[i]) for i in common]) if common else None, "recipes": {}}
    for t, r in runs.items():
        rec = {k: v for k, v in r.items() if k not in ("_vecs", "ops")}
        vecs = r.get("_vecs") or []
        if vecs:
            got = {i: e for i, e in vecs}
            cos = [float(np.dot(lab.unit(got[i]), lab.unit(ref[i]))) for i in got if i in ref]
            rec["cosine_to_original"] = {"photos": len(cos), "mean": round(float(np.mean(cos)), 5), "min": round(float(np.min(cos)), 5),
                                         "p05": round(float(np.percentile(cos, 5)), 5)} if cos else None
            rec["photos_run"] = len(vecs)
            if t in full:
                rec["species_on_common_photos"] = judge([(i, got[i]) for i in common])
            else:
                rec["species_on_its_photos"] = judge([(i, got[i]) for i in got if i in ref])
                rec["species_original_on_same_photos"] = judge([(i, ref[i]) for i in got if i in ref])
        res["recipes"][t] = rec
    # the choice: among int8-sized recipes run on every photo, the fastest single-thread one whose species top-1 is within
    # one point of the original's on the same photos and whose mean cosine is at least 0.99; failing that, the best top-1
    orig = res["original"]["top1"] if res["original"] else None
    cands = []
    for t in full:
        r = res["recipes"][t]
        if t not in INT8_FAMILY or "species_on_common_photos" not in r:
            continue
        ms = (r.get("latency_1") or {}).get("median_ms") or 1e9
        ok = orig is not None and r["species_on_common_photos"]["top1"] >= orig - 1.0 and (r.get("cosine_to_original") or {}).get("mean", 0) >= 0.99
        cands.append((t, ok, ms, r["species_on_common_photos"]["top1"], (r.get("cosine_to_original") or {}).get("mean", 0)))
    good = [c for c in cands if c[1]]
    if args.choose:
        best, why = args.choose, "chosen by name in the run file (device.choose), after reading the numbers"
    elif good:
        fastest = min(c[2] for c in good)
        tie = [c for c in good if c[2] <= 1.1 * fastest]
        best = max(tie, key=lambda c: (c[4], c[3]))[0]
        why = ("of the recipes within one point of the original's top-1 with mean cosine >= 0.99, those within 10% of the "
               "fastest median single-thread time; of those, the highest mean cosine to the original")
    elif cands:
        best = max(cands, key=lambda c: (c[3], c[4]))[0]
        why = "no recipe was within one point of the original with cosine >= 0.99; the best top-1 (then cosine) was taken"
    else:
        best, why = None, "no int8-sized recipe ran on every photo"
    res["best"], res["best_why"] = best, why
    res["candidates"] = [{"recipe": c[0], "qualifies": c[1], "median_ms_1thread": c[2], "top1": c[3], "cosine_mean": c[4]} for c in cands]
    pathlib.Path(args.out).write_text(json.dumps(res, indent=1) + "\n")
    print(json.dumps({"best": best, "original": res["original"], "candidates": res["candidates"]}, indent=1))


def parts(args):
    f = pathlib.Path(args.file)
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    meta = json.loads(pathlib.Path(args.meta).read_text()) if args.meta else {}
    total, plist = f.stat().st_size, []
    with open(f, "rb") as fh:
        k = 0
        while True:
            b = fh.read(args.size)
            if not b:
                break
            name = "%s.part%02d" % (args.name, k)
            (out / name).write_bytes(b)
            plist.append({"name": name, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()})
            k += 1
    meta.update({"file": args.name, "bytes": total, "sha256": sha256(f), "part_size_max": args.size, "parts": plist,
                 "join": "fetch the parts in order and concatenate them; the result's bytes and sha256 are those above"})
    (out / "parts.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False) + "\n")
    print("%d parts, %d bytes, %s" % (len(plist), total, meta["sha256"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("select")
    s.add_argument("--manifest", required=True)
    s.add_argument("--split", default="test")
    s.add_argument("--n", type=int, default=320)
    s.add_argument("--out", required=True)
    mk = sub.add_parser("make")
    mk.add_argument("--model", required=True)
    mk.add_argument("--manifest", required=True)
    mk.add_argument("--rows", required=True)
    mk.add_argument("--photos", required=True)
    mk.add_argument("--recipes", required=True)
    mk.add_argument("--work", required=True)
    mk.add_argument("--pix", required=True)
    mk.add_argument("--summary", required=True)
    mk.add_argument("--ref-n", type=int, default=24)
    sc = sub.add_parser("score")
    sc.add_argument("--model", default="bioclip2-l14")
    sc.add_argument("--manifest", required=True)
    sc.add_argument("--ref-npy", required=True)
    sc.add_argument("--ref-ids", required=True)
    sc.add_argument("--ref-name", default="alachua-2025.f16.npy")
    sc.add_argument("--slot", required=True)
    sc.add_argument("--slot-name", default="pub/heads-sentences-bioclip2-l14")
    sc.add_argument("--min-photos", type=int, default=250)
    sc.add_argument("--runs", nargs="+", required=True)
    sc.add_argument("--out", required=True)
    sc.add_argument("--choose", default="", help="publish this recipe whatever the rule says (recorded as such)")
    pt = sub.add_parser("parts")
    pt.add_argument("--file", required=True)
    pt.add_argument("--size", type=int, default=90_000_000)
    pt.add_argument("--out", required=True)
    pt.add_argument("--meta")
    pt.add_argument("--name", default="vision.int8.onnx")
    a = ap.parse_args()
    {"select": select, "make": make, "score": score, "parts": parts}[a.cmd](a)


if __name__ == "__main__":
    main()
