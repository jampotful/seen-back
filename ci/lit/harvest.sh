#!/usr/bin/env bash
# One topic of the literature collection (tools/lit/harvest.py). Called by .github/workflows/lit.yml.
set -uo pipefail
topic="$1"
mkdir -p corpus
python3 -I tools/lit/harvest.py --topics tools/lit/topics.json --topic "$topic" --out corpus 2>&1 | tee "corpus/$topic.log.txt"
exit "${PIPESTATUS[0]}"
