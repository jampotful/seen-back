#!/usr/bin/env bash
# After the device jobs: score every recipe's WASM vectors (cosine to the original model's published vectors; species
# top-1 and top-5 against the published server rows with the month prior, as tools/fusion/fuse.py scores them), choose
# the int8 file, cut it into parts of at most 90,000,000 bytes, publish the parts with parts.json to <branch>, and check
# the address a browser will fetch them from.
# Usage: bash ci/lab/device_pub.sh <model> <branch>   (dparts/ holds the device jobs' artifacts; data_in/ the manifest)
set -uo pipefail
model="$1"; branch="$2"
mkdir -p ret pub ref slot
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
run() { say "+ $*"; "$@" >> "$L" 2>&1; local rc=$?; say "exit $rc"; return $rc; }
for d in dparts/*/; do [ -f "$d/log.txt" ] && { echo "==== device job log $d"; cat "$d/log.txt"; } >> ret/jobs_log.txt; done
ls -la dparts/* >> "$L" 2>&1
git fetch -q --depth 1 origin "pub/lab-$model" && git --work-tree=ref checkout FETCH_HEAD -- images/alachua-2025.f16.npy images/alachua-2025.ids.json && git reset -q
say "original vectors from pub/lab-$model $(git rev-parse --short FETCH_HEAD)"
git fetch -q --depth 1 origin "pub/heads-sentences-$model" && git --work-tree=slot checkout FETCH_HEAD -- . && git reset -q
slot_sha=$(git rev-parse FETCH_HEAD)
say "server rows from pub/heads-sentences-$model $slot_sha"
run python3 -u tools/lab/device.py score --model "$model" --manifest data_in/manifest.csv --ref-npy ref/images/alachua-2025.f16.npy \
  --ref-ids ref/images/alachua-2025.ids.json --slot slot --slot-name "pub/heads-sentences-$model@${slot_sha:0:12}" --runs dparts/*/ --out ret/device_results.json \
  --choose "${DEVICE_CHOOSE:-}" || exit 1
best=$(python3 -c "import json;print(json.load(open('ret/device_results.json'))['best'] or '')")
[ -n "$best" ] || { say "no int8 recipe qualified to publish"; exit 1; }
f=$(ls dparts/*/vision."$best".onnx 2>/dev/null | head -1)
[ -f "$f" ] || { say "the chosen file vision.$best.onnx is not among the artifacts"; exit 1; }
say "chosen: $best ($f, $(stat -c %s "$f") bytes)"
python3 - "$f" "$best" "$(dirname "$f")/device_summary.json" ret/device_results.json meta.json "$slot_sha" <<'PY' >> "$L" 2>&1 || exit 1
import hashlib, json, os, sys
f, best, sumf, resf, out, slot_sha = sys.argv[1:7]
s = json.load(open(sumf)); res = json.load(open(resf))
h = hashlib.sha256(open(f, "rb").read()).hexdigest()
made = s["recipes"][best]
assert made.get("sha256") == h, "the artifact's file is not the file the job measured"
inp = s["input"]
meta = {
  "model": s["model"], "source": s["source"], "source_url": s["source_url"],
  "licence": "MIT", "licence_url": s["licence_url"], "licence_note": "BioCLIP 2 is released under the MIT licence (model card 'License: MIT'; LICENSE file at the address given); keep the notice",
  "recipe": best, "recipe_how": made.get("how"), "params_image_encoder": s["params"]["image"],
  "input": {"name": "pixel_values", "type": "float32", "shape": [1, 3, inp["size"], inp["size"]]},
  "output": {"name": "image_embeds", "type": "float32", "width": 768, "unit_normalized": False, "note": "normalize to unit length before the dot products"},
  "preprocessing": {
    "size": inp["size"], "mean": inp["mean"], "std": inp["std"],
    "resize": "shortest side to %d, the other side int(%d * long / short) (truncated), bicubic with antialiasing (torchvision Resize on a PIL image, i.e. PIL's BICUBIC)" % (inp["size"], inp["size"]),
    "crop": "centre %d x %d: left = round((W - %d) / 2), top = round((H - %d) / 2) with halves rounded to even (Python round, as torchvision CenterCrop)" % ((inp["size"],) * 4),
    "crop_rule_checked": "the rule reproduced the transforms' output on %s of %s photos" % (s["pixels"]["crop_rule_ok"], s["pixels"]["crop_rule_checked"]),
    "scale": "RGB; v / 255, then (v - mean) / std per channel; NCHW",
    "open_clip_transforms": s["preprocess_detail"].get("transforms"),
  },
  "runtime": "onnxruntime-web 1.30.0, WASM backend (single thread unless the page is cross-origin isolated)",
  "measured": {"about": res["about"], "photos": res["photos_common"], "original": res["original"],
               "chosen": {k: v for k, v in res["recipes"][best].items() if k in ("bytes", "sha256", "cosine_to_original", "species_on_common_photos", "latency_1", "latency_4")},
               "rule": res["best_why"], "all_recipes": "results.json"},
  "server_rows": "pub/heads-sentences-%s@%s" % (s["model"], slot_sha),
  "made_by": {"workflow": os.environ.get("GITHUB_WORKFLOW"), "run_number": os.environ.get("GITHUB_RUN_NUMBER"), "commit": os.environ.get("GITHUB_SHA"),
              "software": s["software"]},
}
json.dump(meta, open(out, "w"), indent=1)
print("meta written")
PY
run python3 tools/lab/device.py parts --file "$f" --size 90000000 --out pub --meta meta.json --name vision.int8.onnx || exit 1
cp ret/device_results.json pub/results.json
cp pub/parts.json ret/
run bash ci/put_branch.sh "$branch" pub "lab: $model for the device ($best, in parts)" || exit 1
sha=$(git ls-remote origin "refs/heads/$branch" | cut -f1)
say "published $branch at $sha"
echo "$sha" > ret/branch_commit.txt
# the address a browser will fetch the parts from, asked as a page on jampotful.github.io would ask it
url="https://raw.githubusercontent.com/jampotful/seen-back/$sha/vision.int8.onnx.part00"
want=$(python3 -c "import json;print(json.load(open('pub/parts.json'))['parts'][0]['sha256'])")
for i in 1 2 3 4 5 6; do
  code=$(curl -sS -D ret/raw_headers.txt -o raw_part00 -w '%{http_code} %{size_download} %{time_total}' -H "Origin: https://jampotful.github.io" "$url" 2>>"$L")
  got=$(sha256sum raw_part00 2>/dev/null | cut -d' ' -f1)
  say "GET $url -> $code; sha256 $( [ "$got" = "$want" ] && echo matches || echo "differs ($got)" )"
  [ "${code%% *}" = 200 ] && break
  sleep 10
done
curl -sS -D ret/raw_range_headers.txt -o /dev/null -r 0-1023 -w '%{http_code}\n' -H "Origin: https://jampotful.github.io" "$url" > ret/raw_range_status.txt 2>>"$L"
curl -sS -D ret/raw_options_headers.txt -o /dev/null -X OPTIONS -w '%{http_code}\n' -H "Origin: https://jampotful.github.io" -H "Access-Control-Request-Method: GET" -H "Access-Control-Request-Headers: range" "$url" > ret/raw_options_status.txt 2>>"$L"
python3 - "$code" "$got" "$want" "$url" <<'PY' > ret/raw_check.json
import json, sys
code, got, want, url = sys.argv[1:5]
def hdr(p):
    out = {}
    try:
        for line in open(p, encoding="latin-1"):
            if ":" in line:
                k, v = line.split(":", 1); out[k.strip().lower()] = v.strip()
            elif line.startswith("HTTP/"):
                out["status_line"] = line.strip()
    except Exception:
        pass
    return out
h = hdr("ret/raw_headers.txt")
print(json.dumps({"url": url, "curl": code, "sha256_matches": got == want, "status_line": h.get("status_line"),
                  "access-control-allow-origin": h.get("access-control-allow-origin"), "content-length": h.get("content-length"),
                  "content-type": h.get("content-type"), "cache-control": h.get("cache-control"), "etag": h.get("etag"),
                  "content-encoding": h.get("content-encoding"),
                  "range_request": {"status": open("ret/raw_range_status.txt").read().strip(), **{k: v for k, v in hdr("ret/raw_range_headers.txt").items() if k in ("status_line", "content-range", "access-control-allow-origin")}},
                  "preflight_options": {"status": open("ret/raw_options_status.txt").read().strip(), **{k: v for k, v in hdr("ret/raw_options_headers.txt").items() if k.startswith("access-control") or k == "status_line"}}},
                 indent=1))
PY
cat ret/raw_check.json >> "$L"
say "device publish done"
