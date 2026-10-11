"""Turn ci/lab/run.json into the build matrix for .github/workflows/lab.yml.

run.json: {"models": [...ids...], "stages": [...] or {"<id>": [...], "*": [...]}, "data": "auto|pub/data-alachua|standin",
           "shards": {"<id>": n}, "max_parallel": 10}
Stages: text-kinds, text-species, images, export, images-onnx-int8, images-onnx-fp16.
Image stages and text-species are split into shards (contiguous blocks of manifest or species rows); the other stages
run on shard 0.
Prints GitHub step outputs: work=<json matrix>, models=<json list>, max_parallel=<n>.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
run = json.loads(pathlib.Path(sys.argv[1]).read_text())
slate = {m["id"]: m for m in json.loads((ROOT / "tools/lab/models.json").read_text())["models"]}
work, models = [], []
for mid in run.get("models", []):
    if mid not in slate:
        raise SystemExit("unknown model %s" % mid)
    st = run["stages"]
    stages = st.get(mid, st.get("*", [])) if isinstance(st, dict) else list(st)
    if slate[mid]["loader"] == "onnx":
        stages = [s for s in stages if s not in ("export", "text-kinds", "text-species") and not s.startswith("images-onnx")]
    if not stages:
        continue
    img = [s for s in stages if s.startswith("images") or s == "text-species"]
    other = [s for s in stages if s not in img]
    n = int(run.get("shards", {}).get(mid, 1)) if img else 1
    rows = run.get("rows", {})
    rows = rows.get(mid, rows.get("*", "")) if isinstance(rows, dict) else rows
    subset = run.get("shard_subset", {}).get(mid)
    for i in range(n):
        if subset is not None and i not in subset:
            continue
        s_i = (other if i == 0 else []) + img
        work.append({"model": mid, "shard": i, "nshards": n, "stages": ",".join(s_i), "tag": "%s-s%d" % (mid, i),
                     "rows": str(rows or ""), "mode": run.get("shard_mode", "block"),
                     "wasm_procs": str(run.get("wasm_procs", 1)), "wasm_split": run.get("wasm_split", "")})
    models.append(mid)
print("work=" + json.dumps({"include": work}))
print("has_work=%s" % ("true" if work else "false"))
print("models=" + json.dumps(models))
print("has_models=%s" % ("true" if models and run.get("publish", True) else "false"))
print("guard=" + json.dumps(run.get("guard") or {}))
print("has_guard=%s" % ("true" if run.get("guard") else "false"))
print("manifest=%s" % run.get("manifest", ""))
print("max_parallel=%d" % int(run.get("max_parallel", 10)))
print("publish_after=%s" % (run.get("publish_after_run") or ""))
# device runs: {"device": {"model": id, "jobs": [[recipe, ...], ...], "photos": 320, "branch": "pub/model-<id>", "max_parallel": n}}
dev = run.get("device") or {}
dwork = [{"model": dev["model"], "recipes": ",".join(j), "tag": "device-%s" % j[0], "photos": str(dev.get("photos", 320))}
         for j in dev.get("jobs", [])]
print("device=" + json.dumps({"include": dwork}))
print("has_device=%s" % ("true" if dwork else "false"))
print("device_model=%s" % dev.get("model", ""))
print("device_branch=%s" % dev.get("branch", ""))
print("device_max=%d" % int(dev.get("max_parallel", max(len(dwork), 1))))
print("count=%d" % (len(work) + len(models) + len(dwork)), file=sys.stderr)
