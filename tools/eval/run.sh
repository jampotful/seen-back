#!/bin/bash
# Everything in one command: fetch, checks, Study 1, Study 2, export of the chosen heads, the as-shipped scoring, the report.
#
#   bash tools/eval/run.sh ROOT [TRAIN]
#
# ROOT is the working directory for the published files (made if missing). TRAIN is `val` (the stand-in, the default)
# or the name of a published training set such as `alachua-pre2025`.
# Environment: STORE=<git dir> reads the pub branches from an existing clone instead of downloading them;
# SKIP_FETCH=1 and SKIP_STUDY1=1 leave those steps out; MODELS="a b c" names the models of Study 2;
# MERGE=1 keeps the other models' results in the study's file when only some are run again.
set -e
ROOT=$1
TRAIN=${2:-val}
MODELS=${MODELS:-tinyclip-39m-16 tinyclip-8m-16 bioclip2-l14}
cd "$(dirname "$0")/../.."
[ -n "$SKIP_FETCH" ] || python3 -I tools/eval/fetch.py "$ROOT" ${STORE:+--store "$STORE"}
python3 -I tools/eval/checks.py "$ROOT" > /dev/null || echo "A check failed: read docs/eval/checks.md."
[ -n "$SKIP_STUDY1" ] || python3 -I tools/eval/study1.py "$ROOT"
python3 -I tools/eval/study2.py "$ROOT" --train "$TRAIN" --models "$(echo $MODELS | tr ' ' ',')" --save "$ROOT/heads/$TRAIN" ${MERGE:+--merge}
for m in $MODELS; do
  if [ -f "$ROOT/heads/$TRAIN/$m.npz" ]; then
    python3 -I tools/eval/export_heads.py "$ROOT" --head "$ROOT/heads/$TRAIN/$m.npz" --out "$ROOT/slots/$TRAIN/$m"
    python3 -I tools/eval/shipped.py "$ROOT" "$ROOT/slots/$TRAIN/$m" --name "$TRAIN-$m"
  fi
done
python3 -I tools/eval/decide.py || echo "The pocket decision could not be computed."
python3 -I tools/eval/report.py
