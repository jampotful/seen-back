#!/usr/bin/env bash
# The larger model from the live address on a build machine (test/engines/big.js, test/engines/big_page.js). PART says which browsers:
#   linux: Chromium (with the home-screen questions), then Firefox (headed on Xvfb), then WebKit, one after another
#   mac-ws: Playwright's WebKit, then real Safari through safaridriver;  mac-sim: Safari on an iPhone simulator through safaridriver
# First the four parts with curl (headers, a preflight, redirects, bytes and seconds, sha256 against the manifest). Memory of the
# browser processes is sampled once a second into out/mem.jsonl by ci/engines/memwatch.py. Everything goes into out/log.txt.
set -uo pipefail
# run/engines/bigwm*: the webkitmem trial (ci/engines/bigwm.sh), one variant of the page after another in WebKit and Safari
case "${GITHUB_REF_NAME:-}" in run/engines/bigwm*) exec bash ci/engines/bigwm.sh ;; esac
ROOT="$PWD"; OUT="$ROOT/out"; mkdir -p "$OUT"
exec > >(tee -a "$OUT/log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
limit() { local s=$1; shift; "$@" & local p=$!; ( sleep "$s"; kill "$p" 2>/dev/null ) & local w=$!; wait "$p"; local rc=$?; kill "$w" 2>/dev/null; return $rc; }
SITE="${SITE:-https://jampotful.github.io/seen-back/}"; PW=/tmp/pw; PWV=1.56.0; PART="${PART:-linux}"
# run/engines/big-wk*: only WebKit (Linux, and macOS through Playwright), after run engines/35
case "${GITHUB_REF_NAME:-}" in run/engines/big-wk*) ONLY_WK=1 ;; *) ONLY_WK=0 ;; esac
# run/engines/big-lx-<browser>-*: only that browser, on Linux (the macOS jobs do not start)
ONLY_LX=$(printf '%s' "${GITHUB_REF_NAME:-}" | sed -n -E 's#^run/engines/big-lx-(chromium|firefox|webkit)-.*#\1#p')
if [ "$ONLY_WK" = 1 ] && [ "$PART" = mac-sim ]; then echo "nothing for $PART on ${GITHUB_REF_NAME}"; exit 0; fi
step "machine ($PART)"; uname -a; (command -v free >/dev/null && free -m) || (sysctl -n hw.memsize hw.ncpu; sw_vers); node --version; df -h /tmp | tail -1
step "the larger model's manifest from the live address, and its parts with curl"
curl -s -f "${SITE}models/naturalist/manifest.json" -o "$OUT/naturalist-manifest.json"; echo "manifest: exit $?, $(wc -c < "$OUT/naturalist-manifest.json") bytes"
python3 -I -c "
import json,sys
m=json.load(open(sys.argv[1])); v=m['vision']
print('whole', v.get('bytes'), v.get('sha256'))
for p in v.get('parts',[]): print('part', p['url'], p['bytes'], p['sha256'])" "$OUT/naturalist-manifest.json" | tee /tmp/parts.txt
mkdir -p /tmp/parts; : > /tmp/parts/list
grep '^part ' /tmp/parts.txt | while read -r _ u b h; do
  f=/tmp/parts/$(basename "$u"); echo "--- $(basename "$u") (manifest: $b bytes)"
  curl -s -o "$f" -D - -H 'Accept-Encoding: gzip, deflate, br' -H 'Origin: https://jampotful.github.io' -w 'curl: http %{http_code}, bytes on the wire %{size_download}, %{time_total} s, redirects %{num_redirects}, %{speed_download} bytes/s\n' "$u" \
    | grep -i -E '^HTTP|content-encoding|content-length|content-type|access-control|cache-control|etag|x-cache|via:|age:|location|timing-allow|^curl:'
  got=$( (command -v sha256sum >/dev/null && sha256sum "$f" || shasum -a 256 "$f") | cut -d' ' -f1); echo "sha256 $( [ "$got" = "$h" ] && echo matches || echo "DIFFERS: $got") the manifest; $(wc -c < "$f") bytes"
  echo "$f" >> /tmp/parts/list
  echo "--- preflight for it (OPTIONS, as a request with a custom header would cause)"
  curl -s -o /dev/null -X OPTIONS -H 'Origin: https://jampotful.github.io' -H 'Access-Control-Request-Method: GET' -H 'Access-Control-Request-Headers: x-test' -D - -w 'curl: http %{http_code}\n' "$u" | grep -i -E '^HTTP|access-control|^curl:'
done
whole=$(grep '^whole ' /tmp/parts.txt | cut -d' ' -f3); got=$(cat $(cat /tmp/parts/list) | (command -v sha256sum >/dev/null && sha256sum || shasum -a 256) | cut -d' ' -f1)
echo "the parts joined: sha256 $( [ "$got" = "$whole" ] && echo matches || echo "DIFFERS: $got") the manifest's whole ($whole)"; rm -rf /tmp/parts
step "photos"; python3 -I ci/engines/big_photos.py /tmp/bigphotos
step "playwright $PWV"
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -1)
export NODE_PATH="$PW/node_modules"
python3 -I ci/engines/memwatch.py "$OUT/mem.jsonl" & MW=$!
run() { local B=$1 s=$2; shift 2; step "the larger model in $B"; ( export BROWSER=$B OUT="$OUT" PHOTOS=/tmp/bigphotos/photos.json SITE="$SITE" "$@"; limit "$s" node test/engines/big.js ); echo "big.js $B: exit $?"; }
case "$PART" in
  linux)
    for B in chromium firefox webkit; do for t in 1 2; do timeout 300 node "$PW/node_modules/playwright/cli.js" install --with-deps $B > "$OUT/install-$B.txt" 2>&1 && break; done; done
    sudo apt-get install -y -q xvfb > /dev/null 2>&1; Xvfb :99 -screen 0 1280x1024x24 > /dev/null 2>&1 & export DISPLAY=:99
    if [ -n "$ONLY_LX" ]; then if [ "$ONLY_LX" = firefox ]; then run firefox 1500 HEADED=1; else run "$ONLY_LX" 1500; fi
    else
    [ "$ONLY_WK" = 1 ] || run chromium 1500
    # Playwright's build of Firefox runs WebAssembly about fifteen times slower than Mozilla's builds (docs/ENGINES.md, 18 October, Firefox),
    # so its times say nothing about Firefox itself; run/engines/ffx-g<label> runs the page's flow in Mozilla's build, started by hand
    [ "$ONLY_WK" = 1 ] || run firefox 1300 HEADED=1
    run webkit 1300
    fi ;;
  mac-ws)
    node "$PW/node_modules/playwright/cli.js" install webkit 2>&1 | grep -v -E "[0-9]+%" | tail -2
    run webkit 1300
    if [ "$ONLY_WK" != 1 ]; then sudo safaridriver --enable 2>&1; safaridriver -p 4444 > "$OUT/safaridriver-log.txt" 2>&1 & sleep 2; run safari 1300; fi ;;
  mac-sim)
    UDID=$(xcrun simctl list devices available -j | python3 -I -c "
import json, sys
d = json.load(sys.stdin)['devices']
c = sorted((rt, x['udid']) for rt, xs in d.items() for x in xs if x['name'].startswith('iPhone') and x.get('isAvailable', True))
print(c[-1][1] if c else '')")
    echo "iPhone simulator: ${UDID:-none found}"; xcrun simctl list devices available | grep -i iphone | head -5
    [ -n "$UDID" ] && xcrun simctl boot "$UDID" 2>&1; [ -n "$UDID" ] && limit 300 xcrun simctl bootstatus "$UDID" -b 2>&1 | tail -2
    for k in RemoteAutomationEnabled WebKitRemoteAutomationEnabled WebDriverEnabled; do xcrun simctl spawn "$UDID" defaults write com.apple.mobilesafari $k -bool YES 2>&1; done
    sudo safaridriver --enable 2>&1; safaridriver -p 4444 > "$OUT/safaridriver-log.txt" 2>&1 & sleep 2
    run sim 1500 UDID="$UDID"
    xcrun simctl io "$UDID" screenshot "$OUT/big-sim-screen.png" > /dev/null 2>&1
    xcrun simctl shutdown "$UDID" 2>&1 || true ;;
esac
kill $MW 2>/dev/null
step "summary"; python3 -I ci/engines/bigsum.py "$OUT" | tee "$OUT/big-summary.txt"
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -q pillow && /tmp/venv/bin/python -I ci/engines/shrink.py "$OUT"; du -sh "$OUT"; ls -la "$OUT"
