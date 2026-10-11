#!/usr/bin/env bash
# Copy the built page and the files it fetches into one directory, for a native shell to serve.
# Usage (from the repository root, after `python3 -I build.py`): bash ci/native/bundle.sh <dest>
# TEST=0 leaves out test/assets and test/rec/photos, which only the self-test (?selftest=1) uses.
# The larger model's rows (models/naturalist) are small and go in; its 310 MB encoder comes from the network as on the web.
set -euo pipefail
dest="$1"
rm -rf "$dest"; mkdir -p "$dest/models"
cp index.html sw.js manifest.webmanifest "$dest/"
[ -f selftest.js ] && cp selftest.js "$dest/"
cp -R vendor fonts icons labels "$dest/"
cp -R models/pocket models/naturalist "$dest/models/"
if [ "${TEST:-1}" = 1 ]; then mkdir -p "$dest/test/rec"; cp -R test/assets "$dest/test/"; cp -R test/rec/photos "$dest/test/rec/"; fi
echo "bundle: $(find "$dest" -type f | wc -l | tr -d ' ') files, $(du -sk "$dest" | cut -f1) kB in $dest"
