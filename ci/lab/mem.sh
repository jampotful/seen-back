#!/usr/bin/env bash
# One memory job: how much memory BioCLIP 2's shipped device file (pub/model-bioclip2-l14, recipe hybrid-fc2-w8) needs in
# onnxruntime-web 1.30.0's WASM build, for each listed route (a way of creating the session), in Node, one fresh process
# a route (tools/lab/mem_node.mjs), under /usr/bin/time -v for the process's own peak.
# Usage: bash ci/lab/mem.sh <tag> <routes as JSON> <model commit>
# A route: {"name", "form": "onnx" (the shipped file) | "ort-basic" | "ort-disabled" (ORT format) | "external" (weights in an
#           external data file), "options": session options, "drop_js": bool, "photos": n}
# Writes ret/routes/<name>.json, <name>.f32 (vectors), <name>.time.txt and ret/log.txt.
set -uo pipefail
tag="$1"; routes="$2"; commit="${3:-462ecdc327746ec5990c416bb51246b99faba0cb}"
mkdir -p ret/routes model
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
say "memory job $tag; model commit $commit"
nproc >> "$L"; free -m >> "$L"; node --version >> "$L"
# the shipped file, from the commit the live page reads, checked part by part and whole
curl -fsSL --retry 4 -o model/parts.json "https://raw.githubusercontent.com/jampotful/seen-back/$commit/parts.json" || { say "no parts.json"; exit 1; }
for k in 00 01 02 03; do
  curl -fsSL --retry 4 -o "model/part$k" "https://raw.githubusercontent.com/jampotful/seen-back/$commit/vision.int8.onnx.part$k" || { say "part $k failed"; exit 1; }
done
cat model/part00 model/part01 model/part02 model/part03 > model/vision.int8.onnx && rm -f model/part0*
python3 - <<'PY' 2>&1 | tee -a "$L"
import hashlib, json
p = json.load(open("model/parts.json"))
h = hashlib.sha256(open("model/vision.int8.onnx", "rb").read()).hexdigest()
want = p.get("sha256") or (p.get("file") or {}).get("sha256")
print("whole file sha256", h, "parts.json says", want, "OK" if h == want else "MISMATCH")
PY
ls -l model >> "$L"
(mkdir -p ortweb && cd ortweb && npm init -y >/dev/null && npm install --no-audit --no-fund onnxruntime-web@1.30.0) >> "$L" 2>&1
python3 -m pip install --quiet numpy pillow 2>&1 | tail -1
python3 tools/lab/mem_prep.py pixels --manifest data_in/manifest.csv --photos photos --out pix 2>&1 | tail -3 | tee -a "$L"
cp pix/ids.json ret/ids.json; cp pix/norm.json ret/norm.json
forms=$(python3 -c "import json,sys;print(' '.join(sorted({r.get('form','onnx') for r in json.loads(sys.argv[1])})))" "$routes")
if echo "$forms" | grep -q -E "ort-|external|pre-"; then
  python3 -m pip install --quiet onnx "onnxruntime==1.30.0" 2>&1 | tail -1 || python3 -m pip install --quiet onnx onnxruntime 2>&1 | tail -1
  python3 -c "import onnxruntime, onnx; print('python onnxruntime', onnxruntime.__version__, 'onnx', onnx.__version__)" 2>&1 | tee -a "$L"
fi
for f in $forms; do
  case "$f" in
    ort-basic) python3 tools/lab/mem_prep.py ort --model model/vision.int8.onnx --out model/vision.basic.ort --level basic 2>&1 | tail -3 | tee -a "$L" ;;
    ort-disabled) python3 tools/lab/mem_prep.py ort --model model/vision.int8.onnx --out model/vision.disabled.ort --level disabled 2>&1 | tail -3 | tee -a "$L" ;;
    external) mkdir -p model/ext && python3 tools/lab/mem_prep.py external --model model/vision.int8.onnx --out model/ext/vision.graph.onnx --weights vision.weights.bin 2>&1 | tail -3 | tee -a "$L" ;;
    pre-extended) mkdir -p model/pre && python3 tools/lab/mem_prep.py preopt --model model/vision.int8.onnx --out model/pre/vision.pre.onnx --level extended 2>&1 | tail -3 | tee -a "$L" ;;
    pre-extended-ext) mkdir -p model/prex && python3 tools/lab/mem_prep.py preopt --model model/vision.int8.onnx --out model/prex/vision.pre.onnx --level extended --external vision.pre.weights.bin 2>&1 | tail -3 | tee -a "$L" ;;
  esac
done
ls -l model model/ext model/pre model/prex 2>/dev/null >> "$L"
n=$(python3 -c "import json,sys;print(len(json.loads(sys.argv[1])))" "$routes")
fail=0
for i in $(seq 0 $((n - 1))); do
  python3 - "$routes" "$i" > route.json <<'PY'
import json, sys
r = json.loads(sys.argv[1])[int(sys.argv[2])]
form = r.get("form", "onnx")
r["model"] = {"onnx": "model/vision.int8.onnx", "ort-basic": "model/vision.basic.ort", "ort-disabled": "model/vision.disabled.ort",
              "external": "model/ext/vision.graph.onnx", "pre-extended": "model/pre/vision.pre.onnx",
              "pre-extended-ext": "model/prex/vision.pre.onnx"}[form]
if form == "external":
    r["external"] = "model/ext/vision.weights.bin"; r["external_name"] = "vision.weights.bin"
if form == "pre-extended-ext":
    r["external"] = "model/prex/vision.pre.weights.bin"; r["external_name"] = "vision.pre.weights.bin"
r.setdefault("photos", 24)
print(json.dumps(r))
PY
  name=$(python3 -c "import json;print(json.load(open('route.json'))['name'])")
  say "route $name: $(cat route.json)"
  tv=(); [ -x /usr/bin/time ] && tv=(/usr/bin/time -v -o "ret/routes/$name.time.txt")
  "${tv[@]}" timeout 1500 node --expose-gc tools/lab/mem_node.mjs ortweb route.json pix ret/routes >> "$L" 2>&1 || { say "route $name failed"; fail=1; }
  grep -E "Maximum resident|Elapsed" "ret/routes/$name.time.txt" 2>/dev/null | tee -a "$L"
done
say "memory job done, fail=$fail"
exit $fail
