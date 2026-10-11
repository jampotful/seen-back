#!/usr/bin/env bash
# One lab job: one model, one shard, some stages. Writes the model's files into art/<model>/ and a small report into ret/.
# Usage: bash ci/lab/job.sh <model> <shard> <nshards> <comma-separated stages>
set -uo pipefail
model="$1"; shard="$2"; n="$3"; stages=",$4,"
out="art/$model"; mkdir -p "$out" ret photos
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
run() { say "+ $*"; "$@" >> "$L" 2>&1; local rc=$?; say "exit $rc"; return $rc; }
has() { [[ "$stages" == *",$1,"* ]]; }
fail=0
say "job: model=$model shard=$shard/$n stages=$4"
cat data_in/source.txt >> "$L" 2>/dev/null
ename=$(cat data_in/evalname.txt)
man=data_in/manifest.csv
fetcher=tools/lab/fetch_photos.py
[ -f data_in/fetch_photos_species.py ] && say "data branch carries tools/species/fetch_photos.py; the lab uses its own fetcher (same interface)"
rowsarg=(); [ -n "${ROWS:-}" ] && rowsarg=(--rows "$ROWS")
mode="${SHARD_MODE:-block}"
if [[ "$stages" == *",images"* ]]; then
  run python3 "$fetcher" "$man" photos --shard "$shard/$n" --mode "$mode" "${rowsarg[@]}" || fail=1
elif has export; then
  run python3 "$fetcher" "$man" photos --limit 48 || fail=1
fi
if has quant-lab; then
  [ -n "$(ls photos 2>/dev/null | head -1)" ] || run python3 "$fetcher" "$man" photos --limit 48
  if run python3 -u tools/lab/lab.py quant-lab --model "$model" --manifest "$man" --photos photos --work "ql_$model" --out-json ret/quant_lab.json; then
    if [ ! -d ortweb/node_modules/onnxruntime-web ]; then
      (mkdir -p ortweb && cd ortweb && npm init -y >/dev/null && npm install --no-audit --no-fund onnxruntime-web@1.30.0) >> "$L" 2>&1
    fi
    WASM_ALL=1 run node tools/lab/wasm_check.mjs ortweb "ql_$model" "ql_$model/wasm" ret/quant_lab_wasm.json || fail=1
  else fail=1; fi
fi
if has text-kinds; then run python3 -u tools/lab/lab.py text --model "$model" --labelset kinds --out "$out" || fail=1; fi
if has text-species; then run python3 -u tools/lab/lab.py text --model "$model" --labelset species --species-json data_in/species.json --shard "$shard/$n" --out "$out" || fail=1; fi
if has export; then
  if run python3 -u tools/lab/lab.py export --model "$model" --manifest "$man" --photos photos --out "$out" --work "work_$model"; then
    if [ ! -d ortweb/node_modules/onnxruntime-web ]; then
      (mkdir -p ortweb && cd ortweb && npm init -y >/dev/null && npm install --no-audit --no-fund onnxruntime-web@1.30.0) >> "$L" 2>&1
    fi
    # the WASM check needs every variant, including any too large to publish
    mkdir -p "work_$model/all"; cp "$out"/onnx/*.onnx "work_$model/all/" 2>/dev/null; cp "work_$model"/vision.*.onnx "work_$model/all/" 2>/dev/null
    if run node tools/lab/wasm_check.mjs ortweb "work_$model/all" "work_$model/wasm" "work_$model/wasm.json"; then
      python3 - "$out/onnx/parity.json" "work_$model/wasm.json" <<'PY' >> "$L" 2>&1
import json, sys
p = json.load(open(sys.argv[1])); w = json.load(open(sys.argv[2]))
p["wasm"] = w
json.dump(p, open(sys.argv[1], "w"), indent=1)
print("wasm results merged into parity.json")
PY
    else fail=1; fi
  else fail=1; fi
fi
if has images; then run python3 -u tools/lab/lab.py images --model "$model" --manifest "$man" --photos photos --shard "$shard/$n" --shard-mode "$mode" "${rowsarg[@]}" --evalname "$ename" --out "$out" || fail=1; fi
for v in int8 int8-per-tensor int8-per-channel fp16; do
  if has "images-onnx-$v"; then
    f="$out/onnx/vision.$v.onnx"
    if [ ! -f "$f" ]; then
      mkdir -p prev && git fetch -q --depth 1 origin "pub/lab-$model" && git --work-tree=prev checkout FETCH_HEAD -- onnx && f="prev/onnx/vision.$v.onnx"
    fi
    run python3 -u tools/lab/lab.py images-onnx --model "$model" --variant "$v" --onnx "$f" --manifest "$man" --photos photos --shard "$shard/$n" --shard-mode "$mode" "${rowsarg[@]}" --evalname "$ename" --out "$out" || fail=1
  fi
done
for v in int8-per-channel int8-per-tensor int8; do
  if has "images-wasm-$v"; then
    f="$out/onnx/vision.$v.onnx"
    if [ ! -f "$f" ]; then
      mkdir -p prev && git fetch -q --depth 1 origin "pub/lab-$model" && git --work-tree=prev checkout FETCH_HEAD -- onnx && f="prev/onnx/vision.$v.onnx"
    fi
    if [ ! -d ortweb/node_modules/onnxruntime-web ]; then
      (mkdir -p ortweb && cd ortweb && npm init -y >/dev/null && npm install --no-audit --no-fund onnxruntime-web@1.30.0) >> "$L" 2>&1
    fi
    osha=$(sha256sum "$f" | cut -d' ' -f1)
    say "wasm $v: $f sha256 $osha"
    splitarg=(); [ -n "${WASM_SPLIT:-}" ] && splitarg=(--split "$WASM_SPLIT")
    if run python3 -u tools/lab/lab.py pixels --model "$model" --manifest "$man" --photos photos --shard "$shard/$n" --shard-mode "$mode" "${rowsarg[@]}" "${splitarg[@]}" --pix "pix_$v"; then
      procs="${WASM_PROCS:-1}"; ok=1
      if [ "$procs" -le 1 ]; then
        run node tools/lab/wasm_embed.mjs ortweb "$f" "pix_$v" "wasm_$v.f32" "wasm_$v.json" 1 || ok=0
      else
        # several single-thread processes on one machine: same arithmetic (WASM is deterministic), shared cores, so the
        # recorded times are not single-photo latencies
        cnt=$(python3 -c "import json;print(len(json.load(open('pix_$v/ids.json'))))"); per=$(( (cnt + procs - 1) / procs ))
        say "wasm: $cnt photos in $procs processes"
        pids=()
        for k in $(seq 0 $((procs - 1))); do
          node tools/lab/wasm_embed.mjs ortweb "$f" "pix_$v" "wasm_$v.$k.f32" "wasm_$v.$k.json" 1 $((k * per)) $(((k + 1) * per)) >> "$L" 2>&1 & pids+=($!)
        done
        for pid in "${pids[@]}"; do wait "$pid" || ok=0; done
        cat $(for k in $(seq 0 $((procs - 1))); do echo "wasm_$v.$k.f32"; done) > "wasm_$v.f32"
        python3 - "$procs" "$v" <<'PY' >> "$L" 2>&1 || ok=0
import json, sys
n, v = int(sys.argv[1]), sys.argv[2]
parts = [json.load(open("wasm_%s.%d.json" % (v, k))) for k in range(n)]
out = dict(parts[0]); out["ms"] = [x for p in parts for x in p["ms"]]; out["count"] = sum(p["count"] for p in parts)
out["processes"] = n; out["note"] = "%d single-thread processes shared the machine; times are not single-photo latencies" % n
json.dump(out, open("wasm_%s.json" % v, "w"))
print("wasm parts merged:", out["count"])
PY
      fi
      if [ "$ok" = 1 ]; then
        run python3 -u tools/lab/lab.py wasm-collect --model "$model" --variant "$v" --manifest "$man" --evalname "$ename" --shard "$shard/$n" --pix "pix_$v" --emb "wasm_$v.f32" --lat "wasm_$v.json" --onnx-name "onnx/vision.$v.onnx" --onnx-sha "$osha" --out "$out" || fail=1
      else fail=1; fi
    else fail=1; fi
    rm -rf "pix_$v" wasm_"$v"*.f32
  fi
done
cp "$out/card.json" ret/ 2>/dev/null; cp "$out/onnx/parity.json" ret/ 2>/dev/null
(cd "$out" && find . -type f -printf '%s %p\n' | sort -k2) > ret/files.txt 2>/dev/null
say "job done, fail=$fail"
mkdir -p "$out/_ci" && cp "$L" "$out/_ci/log.txt"
exit $fail
