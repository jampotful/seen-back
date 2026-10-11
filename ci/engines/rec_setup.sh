#!/usr/bin/env bash
# A real recognizer slot for the checks, made on the build machine: the laboratory's tinyclip-8m-16 branch, turned into a slot by
# test/rec/make_slot.py (with its species head), and the photos it is tried on, with Python's own answers for them (expect.json).
# Leaves ci-rec/slot and ci-rec/photos under the repository root, and prints RECQ: the self-test's address part for them.
set -uo pipefail
ROOT="$PWD"; LAB="${LAB:-pub/lab-tinyclip-8m-16}"
python3 -m venv /tmp/recvenv && /tmp/recvenv/bin/pip install -q numpy onnxruntime pillow && /tmp/recvenv/bin/python -c "import onnxruntime, PIL, numpy; print('python', onnxruntime.__version__, PIL.__version__, numpy.__version__)"
rm -rf /tmp/lab && git clone -q --depth 1 --branch "$LAB" "https://github.com/${GITHUB_REPOSITORY:-jampotful/seen-back}" /tmp/lab && ls -la /tmp/lab/onnx | head -4
/tmp/recvenv/bin/python -I ci/engines/make_photos.py ci-rec/photos
/tmp/recvenv/bin/python -I test/rec/make_slot.py /tmp/lab ci-rec/slot --species species_com --photos ci-rec/photos
