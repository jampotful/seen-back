#!/usr/bin/env bash
# Photos for the kinds the wildlife records lack (people, pets, livestock, nothing alive) from COCO 2017, built by
# tools/species/build_coco.py, checked, and published INTO pub/data-alachua under extra/coco-kinds/ without disturbing
# what is there (ci/data/merge_pub.sh). Called by .github/workflows/extradata.yml; everything comes back on ci.
set -uo pipefail
mkdir -p out work/coco
LOG=out/log.txt
: > "$LOG"
step() {
  local name="$1"; shift
  echo "=== $(date -u +%FT%TZ) $name" | tee -a "$LOG"
  "$@" 2>&1 | tee -a "$LOG"
  local rc=${PIPESTATUS[0]}
  echo "=== $(date -u +%FT%TZ) $name: exit $rc" | tee -a "$LOG"
  return "$rc"
}
ZIP=http://images.cocodataset.org/annotations/annotations_trainval2017.zip
step "install requests" python3 -m pip install --quiet requests || exit 1

# Which addresses answer, over http and https (HEAD requests; a 200 with an image type is what we want).
probe() { for u in "$@"; do printf '%s ' "$u"; curl -sS -o /dev/null -I --max-time 30 -w '%{http_code} %{content_type} %header{content-length}\n' "$u" || echo "curl failed"; done; }
step "addresses" probe "$ZIP" "${ZIP/http:/https:}" \
  http://images.cocodataset.org/train2017/000000000009.jpg https://images.cocodataset.org/train2017/000000000009.jpg \
  http://images.cocodataset.org/val2017/000000000139.jpg https://images.cocodataset.org/val2017/000000000139.jpg
scheme=http
if grep -q '^https://images.cocodataset.org/train2017/000000000009.jpg 200 image/' "$LOG" && \
   grep -q '^https://images.cocodataset.org/val2017/000000000139.jpg 200 image/' "$LOG"; then scheme=https; fi
echo "photo_url scheme: $scheme" | tee -a "$LOG"

# What COCO says about licences (the site is a script-driven page; its text lives in an .htm file beside it).
for p in termsofuse.htm "#termsofuse"; do
  curl -sSL --max-time 30 "https://cocodataset.org/${p}" -o "out/coco-$(echo "$p" | tr -dc 'a-z').html" 2>>"$LOG" || true
done
python3 - <<'PY' >> "$LOG" 2>&1 || true
import glob, html, re
for p in sorted(glob.glob("out/coco-*.html")):
    t = open(p, encoding="utf-8", errors="replace").read()
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))).strip()
    open(p[:-5] + ".txt", "w", encoding="utf-8").write(t + "\n")
    i = t.lower().find("licens")
    print("%s: %d characters of text; around the first 'licens': %r" % (p, len(t), t[max(0, i - 300):i + 900] if i >= 0 else t[:300]))
PY
rm -f out/coco-*.html

step "annotations" curl -fsSL --retry 5 --retry-delay 5 -o work/coco/annotations_trainval2017.zip "$ZIP" || exit 1
step "zip listing" bash -c 'ls -l work/coco/annotations_trainval2017.zip; unzip -l work/coco/annotations_trainval2017.zip'
step "extra manifest" python3 tools/species/build_coco.py --zip work/coco/annotations_trainval2017.zip \
  --out data/extra/coco-kinds --scheme "$scheme" --zip-url "$ZIP"
rc=$?
cp data/extra/coco-kinds/SUMMARY.md out/coco-SUMMARY.md 2>/dev/null || true
cp data/extra/coco-kinds/manifest.csv out/coco-manifest.csv 2>/dev/null || true
if [ -f data/extra/coco-kinds/manifest.csv ]; then
  # Are the photo addresses served? Every 50th row, through the same fetcher the evaluation uses.
  awk -F, 'NR==1 || (NR-2)%50==0' data/extra/coco-kinds/manifest.csv > work/coco-check.csv
  step "photo address check" python3 tools/species/fetch_photos.py work/coco-check.csv work/coco-check --shard 0/1
  step "photo files" bash -c 'ls work/coco-check | head -3; file work/coco-check/*.jpg 2>/dev/null | head -3; du -sh work/coco-check'
fi
[ "$rc" -eq 0 ] || exit "$rc"
[ "${PUBLISH:-1}" = "1" ] || exit 0

publish() {
  rm -rf stage && mkdir -p stage/extra && cp -R data/extra/coco-kinds stage/extra/
  bash ci/data/merge_pub.sh pub/data-alachua stage "extra photo set coco-kinds" extra/coco-kinds
}
on_branch() { git fetch -q --depth 1 origin pub/data-alachua 2>/dev/null && git cat-file -e FETCH_HEAD:extra/coco-kinds/manifest.csv 2>/dev/null; }
step "publish into pub/data-alachua" publish || exit 1
step "branch after" bash -c 'git fetch -q --depth 1 origin pub/data-alachua && git ls-tree -r -l FETCH_HEAD && git show FETCH_HEAD:_made.txt'
JOB_STATUS=published bash ci/return.sh extradata out || true   # an early copy of the results; the final one follows

# A traindata job built from an older commit publishes with ci/put_branch.sh, which replaces the whole branch. While
# one is queued or running, watch the branch and publish this set again if it disappears; stop when none is left.
for i in $(seq 1 110); do
  busy=$(gh api "repos/${GITHUB_REPOSITORY}/actions/workflows/traindata.yml/runs?per_page=20" \
    --jq '[.workflow_runs[] | select(.status != "completed")] | length' 2>/dev/null || echo "?")
  if on_branch; then here=yes; else here=no; fi
  echo "[$(date -u +%T)] traindata runs not completed: $busy; extra/coco-kinds on the branch: $here" | tee -a "$LOG"
  [ "$here" = yes ] || step "publish again" publish
  [ "$busy" = "0" ] && break
  sleep 60
done
on_branch || step "publish again" publish
step "branch at the end" bash -c 'git fetch -q --depth 1 origin pub/data-alachua && git ls-tree -r -l FETCH_HEAD && git show FETCH_HEAD:_made.txt'
