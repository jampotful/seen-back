#!/usr/bin/env bash
# One device job: export <model>'s image encoder, make the listed recipes, and run each through onnxruntime-web 1.30.0's
# WASM build on the chosen test photos (four single-thread processes for the vectors; then, on the idle machine, one
# process with one thread and one with four threads on the first six photos for the time a photo takes).
# Usage: bash ci/lab/device.sh <model> <comma-separated recipes> [photos]
# Writes small results into ret/ (returned to ci) and the same plus the ONNX files into art/ (the publish job's input).
set -uo pipefail
model="$1"; recipes="$2"; nphotos="${3:-320}"
mkdir -p ret art photos
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
run() { say "+ $*"; "$@" >> "$L" 2>&1; local rc=$?; say "exit $rc"; return $rc; }
fail=0
say "device job: model=$model recipes=$recipes photos=$nphotos"
cat data_in/source.txt >> "$L" 2>/dev/null
man=data_in/manifest.csv
run python3 tools/lab/device.py select --manifest "$man" --split test --n "$nphotos" --out ret/rows.json || exit 1
python3 - "$man" ret/rows.json sel_manifest.csv <<'PY' >> "$L" 2>&1
import csv, json, sys
ids = set(json.load(open(sys.argv[2]))["ids"])
rows = list(csv.DictReader(open(sys.argv[1], newline="", encoding="utf-8")))
with open(sys.argv[3], "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader()
    for r in rows:
        if r["id"] in ids: w.writerow(r)
print("sub-manifest:", len(ids), "rows")
PY
run python3 tools/lab/fetch_photos.py sel_manifest.csv photos || fail=1
if [ ! -d ortweb/node_modules/onnxruntime-web ]; then
  (mkdir -p ortweb && cd ortweb && npm init -y >/dev/null && npm install --no-audit --no-fund onnxruntime-web@1.30.0) >> "$L" 2>&1
fi
run python3 -u tools/lab/device.py make --model "$model" --manifest "$man" --rows ret/rows.json --photos photos --recipes "$recipes" \
  --work work --pix pix --summary ret/device_summary.json --ref-n 24 || fail=1
cp work/torch_ref.npy work/torch_ref.ids.json ret/ 2>/dev/null
cnt=$(python3 -c "import json;print(len(json.load(open('pix/ids.json'))))" 2>/dev/null || echo 0)
say "pixels for $cnt photos"
IFS=, read -r -a rlist <<< "$recipes"
for r in "${rlist[@]}"; do
  f="work/vision.$r.onnx"
  [ -f "$f" ] || { say "no $f (recipe failed; see device_summary.json)"; fail=1; continue; }
  n="$cnt"; procs=4
  if [ "$r" = fp16 ]; then n=$(( cnt < 24 ? cnt : 24 )); procs=2; fi
  per=$(( (n + procs - 1) / procs )); ok=1; pids=()
  say "wasm $r: $n photos in $procs single-thread processes ($(stat -c %s "$f") bytes)"
  for k in $(seq 0 $((procs - 1))); do
    a=$((k * per)); b=$(( (k + 1) * per < n ? (k + 1) * per : n ))
    timeout 2400 node tools/lab/wasm_embed.mjs ortweb "$f" pix "wasm_$r.$k.f32" "wasm_$r.$k.json" 1 "$a" "$b" >> "$L" 2>&1 & pids+=($!)
  done
  for pid in "${pids[@]}"; do wait "$pid" || ok=0; done
  if [ "$ok" = 1 ]; then
    cat $(for k in $(seq 0 $((procs - 1))); do echo "wasm_$r.$k.f32"; done) > "wasm_$r.f32"
    python3 - "$r" "$procs" "$n" <<'PY' >> "$L" 2>&1 || fail=1
import json, sys
import numpy as np
r, procs, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
parts = [json.load(open("wasm_%s.%d.json" % (r, k))) for k in range(procs)]
d = parts[0]["width"]
e = np.fromfile("wasm_%s.f32" % r, dtype=np.float32).reshape(-1, d)
ids = json.load(open("pix/ids.json"))[:n]
assert len(e) == len(ids), (len(e), len(ids))
u = e / np.linalg.norm(e, axis=1, keepdims=True)
np.save("ret/wasm_%s.f16.npy" % r, u.astype(np.float16))
json.dump(ids, open("ret/wasm_%s.ids.json" % r, "w"))
ms = [x for p in parts for x in p["ms"]]
json.dump({"runtime": parts[0]["runtime"], "node": parts[0]["node"], "threads": 1, "processes": procs, "count": len(ids),
           "load_ms": [p.get("load_ms") for p in parts], "ms": ms,
           "note": "%d single-thread processes shared the machine; these times are not single-photo latencies" % procs},
          open("ret/wasm_%s.bulk.json" % r, "w"))
print("wasm %s: %d vectors, bulk mean %.0f ms" % (r, len(ids), float(np.mean(ms))))
try:
    ref = np.load("work/torch_ref.npy"); rid = json.load(open("work/torch_ref.ids.json"))
    k = min(len(rid), len(ids)); c = (u[:k] * ref[:k]).sum(1)
    print("cosine to the original model (same machine, first %d photos): mean %.5f min %.5f" % (k, c.mean(), c.min()))
except Exception as ex:
    print("no same-machine reference:", ex)
PY
  else
    say "WASM bulk run failed for $r"; fail=1
  fi
  rm -f wasm_"$r".*.f32 "wasm_$r.f32"
  m6=$(( cnt < 6 ? cnt : 6 ))
  for th in 1 4; do
    if timeout 900 node tools/lab/wasm_embed.mjs ortweb "$f" pix "lat_$r.f32" "ret/wasm_$r.latency_$th.json" "$th" 0 "$m6" > "lat_$r.$th.log" 2>&1; then
      say "latency $r threads=$th: $(tail -1 "lat_$r.$th.log")"
    else
      say "latency $r threads=$th failed"; tail -c 600 "lat_$r.$th.log" > "ret/wasm_$r.latency_$th.err"
    fi
    cat "lat_$r.$th.log" >> "$L"
  done
  if [ -f "lat_$r.f32" ] && [ -f "ret/wasm_$r.f16.npy" ]; then
    python3 - "$r" <<'PY' >> "$L" 2>&1
import sys, numpy as np
r = sys.argv[1]
a = np.fromfile("lat_%s.f32" % r, dtype=np.float32); b = np.load("ret/wasm_%s.f16.npy" % r).astype(np.float32)
d = b.shape[1]; a = a.reshape(-1, d); a /= np.linalg.norm(a, axis=1, keepdims=True); k = len(a)
print("four-thread vectors vs single-thread vectors (first %d photos): min cosine %.6f" % (k, float((a * b[:k]).sum(1).min())))
PY
  fi
  rm -f "lat_$r.f32"
  [ "$r" != fp16 ] && mv "$f" art/
done
cp ret/*.json ret/*.npy art/ 2>/dev/null
ls -la art >> "$L"
say "device job done, fail=$fail"
cp "$L" art/log.txt
exit $fail
