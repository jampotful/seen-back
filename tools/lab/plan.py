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
for mid in run["models"]:
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
    for i in range(n):
        s_i = (other if i == 0 else []) + img
        work.append({"model": mid, "shard": i, "nshards": n, "stages": ",".join(s_i), "tag": "%s-s%d" % (mid, i)})
    models.append(mid)
print("work=" + json.dumps({"include": work}))
print("models=" + json.dumps(models))
print("max_parallel=%d" % int(run.get("max_parallel", 10)))
print("publish_after=%s" % (run.get("publish_after_run") or ""))
print("count=%d" % (len(work) + len(models)), file=sys.stderr)
