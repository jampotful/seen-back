#!/usr/bin/env bash
# Publish the shipped device file in another form (one ci/lab/mem.sh has measured) to a new branch, in parts of at most
# 90,000,000 bytes with parts.json, then fetch every published file back from raw.githubusercontent.com at the new
# commit and check its sha256. Runs inside a mem job, after mem.sh (model/ holds the forms it made).
# Usage: bash ci/lab/mem_pub.sh <form: external | ort-basic> <branch> <route name whose measurement goes into parts.json>
set -uo pipefail
form="$1"; branch="$2"; route="$3"
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
case "$branch" in pub/model-bioclip2-l14|pin/*|main|ci|gh-pages) say "refusing to publish to $branch"; exit 2;; esac
rm -rf pubb && mkdir -p pubb
case "$form" in
  external) big=model/ext/vision.weights.bin; small=model/ext/vision.graph.onnx ;;
  ort-basic) big=model/vision.basic.ort; small="" ;;
  *) say "unknown form $form"; exit 2 ;;
esac
[ -f "$big" ] || { say "no $big"; exit 1; }
python3 - "$form" "$big" "$small" "$route" <<'PY' 2>&1 | tee -a "$L"
import hashlib, json, os, pathlib, sys
form, big, small, route = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3], sys.argv[4]
out = pathlib.Path("pubb")
h = lambda b: hashlib.sha256(b).hexdigest()
orig = json.load(open("model/parts.json"))
meta = {k: orig[k] for k in ("model", "source", "source_url", "licence", "licence_url", "licence_note", "recipe", "recipe_how",
                             "params_image_encoder", "input", "output", "preprocessing") if k in orig}
meta["runtime"] = "onnxruntime-web 1.30.0, WASM backend"
meta["from"] = {"branch": "pub/model-bioclip2-l14", "commit": os.environ.get("MODEL_COMMIT", ""), "file": "vision.int8.onnx",
                "bytes": orig.get("bytes"), "sha256": orig.get("sha256")}
if form == "external":
    g = pathlib.Path(small).read_bytes()
    (out / "vision.graph.onnx").write_bytes(g)
    meta["form"] = ("the shipped file's graph with every tensor of 1 kB or more moved, unchanged, into one external data file "
                    "(onnx.save_model with save_as_external_data); the runtime copies the weights into its heap once")
    meta["graph"] = {"file": "vision.graph.onnx", "bytes": len(g), "sha256": h(g)}
    meta["load"] = ("ort.InferenceSession.create(<vision.graph.onnx bytes>, {executionProviders: ['wasm'], "
                    "externalData: [{path: 'vision.weights.bin', data: <the joined parts>}]})")
    name = "vision.weights.bin"
else:
    meta["form"] = "the shipped file in ORT format, saved by onnxruntime (Python) after the basic graph optimizations"
    meta["load"] = "ort.InferenceSession.create(<the joined parts>, {executionProviders: ['wasm']})"
    name = "vision.basic.ort"
total, plist, whole = big.stat().st_size, [], hashlib.sha256()
with open(big, "rb") as fh:
    k = 0
    while True:
        b = fh.read(90000000)
        if not b:
            break
        pn = "%s.part%02d" % (name, k)
        (out / pn).write_bytes(b)
        whole.update(b)
        plist.append({"name": pn, "bytes": len(b), "sha256": h(b)})
        k += 1
meta.update({"file": name, "bytes": total, "sha256": whole.hexdigest(), "part_size_max": 90000000, "parts": plist,
             "join": "fetch the parts in order and concatenate them; the result's bytes and sha256 are those above"})
try:
    meta["measured"] = json.load(open("ret/routes/%s.json" % route))
    meta["measured"].pop("ids", None)
except Exception as e:  # noqa: BLE001
    meta["measured"] = {"error": str(e)}
meta["made_by"] = {"workflow": os.environ.get("GITHUB_WORKFLOW"), "run_number": os.environ.get("GITHUB_RUN_NUMBER"), "commit": os.environ.get("GITHUB_SHA")}
(out / "parts.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False) + "\n")
print("cut %s into %d parts, %d bytes, %s" % (name, len(plist), total, meta["sha256"]))
PY
cp pubb/parts.json ret/pub_parts.json
echo "made $(date -u +%FT%TZ) by lab run ${GITHUB_RUN_NUMBER:-?} (commit ${GITHUB_SHA:-?}) from pub/model-bioclip2-l14 at ${MODEL_COMMIT:-?}" > pubb/_made.txt
bash ci/put_branch.sh "$branch" pubb "lab: BioCLIP 2's device file as $form, in parts" >> "$L" 2>&1 || { say "publishing failed"; exit 1; }
sha=$(git ls-remote origin "refs/heads/$branch" | cut -f1)
say "published $branch at $sha"
echo "$sha" > ret/pub_branch_commit.txt
# every file back from the address a page would use, checked against parts.json
python3 - "$sha" <<'PY' 2>&1 | tee -a "$L"
import hashlib, json, sys, time, urllib.request
sha = sys.argv[1]
meta = json.load(open("pubb/parts.json"))
files = [(p["name"], p["sha256"]) for p in meta["parts"]] + ([(meta["graph"]["file"], meta["graph"]["sha256"])] if "graph" in meta else [])
ok = True
for name, want in files:
    url = "https://raw.githubusercontent.com/jampotful/seen-back/%s/%s" % (sha, name)
    for k in range(6):
        try:
            b = urllib.request.urlopen(urllib.request.Request(url, headers={"Origin": "https://jampotful.github.io"}), timeout=120).read()
            break
        except Exception as e:  # noqa: BLE001
            b = b""; time.sleep(10)
    got = hashlib.sha256(b).hexdigest()
    print("%s: %d bytes, sha256 %s" % (name, len(b), "matches" if got == want else "DIFFERS"))
    ok = ok and got == want
print("all published files match parts.json" if ok else "SOME FILES DIFFER")
PY
