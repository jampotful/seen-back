#!/usr/bin/env bash
# The live address, checked from a build machine: response headers with curl, then the page in Chromium and WebKit
# (test/engines/live.js). Everything goes into out/log.txt; out/live-summary.json holds the answers.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out"; mkdir -p "$OUT"
exec > >(tee -a "$OUT/log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
SITE="${SITE:-https://jampotful.github.io/seen-back/}"; PW=/tmp/pw; PWV=1.56.0
step "response headers, as a browser that accepts gzip and br would get them"
for p in "" index.html sw.js manifest.webmanifest vendor/ort/ort-wasm-simd-threaded.wasm vendor/ort/ort.wasm.min.js vendor/ort/ort-wasm-simd-threaded.mjs vendor/rec-worker.js models/pocket/manifest.json; do
  echo "--- $SITE$p"
  curl -s -o /dev/null -D - -H 'Accept-Encoding: gzip, deflate, br' -w "bytes on the wire: %{size_download}\n" "$SITE$p" | grep -i -E "^HTTP|content-type|content-encoding|content-length|cache-control|etag|last-modified|age:|expires|access-control|cross-origin|bytes on the wire" 
done
MAN=$(curl -s -f "${SITE}models/pocket/manifest.json" || true)
if [ -n "$MAN" ]; then
  VURL=$(printf '%s' "$MAN" | python3 -I -c "import json,sys; print(json.load(sys.stdin)['vision']['url'])" 2>/dev/null || true)
  echo "--- the model named by the manifest: ${SITE}models/pocket/$VURL"
  curl -s -o /dev/null -D - -H 'Accept-Encoding: gzip, deflate, br' -w "bytes on the wire: %{size_download}, in %{time_total} s\n" "${SITE}models/pocket/$VURL" | grep -i -E "^HTTP|content-type|content-encoding|content-length|cache-control|etag|last-modified|expires|age:|x-cache|via|access-control|bytes on the wire"
  echo "--- the same, asked for without compression"
  curl -s -o /dev/null -D - -w "bytes on the wire: %{size_download}, in %{time_total} s\n" "${SITE}models/pocket/$VURL" | grep -i -E "^HTTP|content-encoding|content-length|bytes on the wire"
  echo "--- the same, asked for a byte range (does a resumed download work?)"
  curl -s -o /dev/null -D - -H 'Range: bytes=0-1023' -w "bytes on the wire: %{size_download}\n" "${SITE}models/pocket/$VURL" | grep -i -E "^HTTP|content-range|content-encoding|content-length|bytes on the wire"
  for f in species.f16.bin kinds.f16.bin species.json; do echo "--- ${SITE}models/pocket/$f"; curl -s -o /dev/null -D - -H 'Accept-Encoding: gzip, deflate, br' -w "bytes on the wire: %{size_download}\n" "${SITE}models/pocket/$f" | grep -i -E "^HTTP|content-encoding|content-length|cache-control|bytes on the wire"; done
else echo "no slot yet: ${SITE}models/pocket/manifest.json is not there"; fi
step "playwright $PWV, Chromium, Firefox and WebKit"
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -1)
export NODE_PATH="$PW/node_modules"
node "$PW/node_modules/playwright/cli.js" install --with-deps chromium firefox webkit 2>&1 | grep -v -E "[0-9]+%" | tail -4
step "the page in Chromium, Firefox and WebKit"
OUT="$OUT" SITE="$SITE" BROWSERS=chromium,firefox,webkit timeout 900 node test/engines/live.js; echo "live.js: exit $?"
python3 -I - "$OUT" <<'PY'
import json, glob, os, sys
out = sys.argv[1]; S = {}
for f in sorted(glob.glob(os.path.join(out, "live-*.json"))):
    r = json.load(open(f)); p = (r.get("first") or {}).get("page") or {}
    S[r["browser"]] = {"version": r.get("version"), "status": (r.get("first") or {}).get("status"), "build": p.get("build"), "sw_registered": p.get("swRegistered"), "sw_active": p.get("swActive"),
        "controlled_first": p.get("controlled"), "controlled_second": (r.get("second") or {}).get("controlled"), "crossOriginIsolated": p.get("coi"), "offline": r.get("offline"),
        "slot": r.get("slot"), "ready": r.get("ready"), "readyMs": r.get("readyMs"), "readyFromNav": r.get("readyFromNav"), "readyFromNavMs": r.get("readyFromNavMs"), "loadEventMs": r.get("loadEventMs"),
        "photos": r.get("photos"), "rec_first": p.get("rec"), "about": r.get("about"), "kept": r.get("kept"), "offlineVisits": r.get("offlineVisits"), "proxy": r.get("proxy"), "second": r.get("second"),
        "errors": r.get("pageErrors"), "console": (r.get("console") or [])[:20], "notes": r.get("notes"), "error": r.get("error")}
json.dump(S, open(os.path.join(out, "summary.json"), "w"), indent=1); print(json.dumps(S, indent=1)[:3000])
PY
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -q pillow && /tmp/venv/bin/python -I ci/engines/shrink.py "$OUT"
