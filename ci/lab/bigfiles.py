#!/usr/bin/env python3
"""Files too large for GitHub (it refuses a file over 100 MiB; lab run 39 failed so, on a world-fit array of 192 MiB)
are kept in parts on the pub/ branches: <file>.part00, <file>.part01, ... beside <file>.parts.json, which gives the
length and sha256 of every part and of the whole.

  python3 -I ci/lab/bigfiles.py split DIR    every file under DIR over 99 MiB is replaced by its parts (90 MiB each)
  python3 -I ci/lab/bigfiles.py join DIR     every split file under DIR is put back together, checked, and its parts removed

A file of 99 MiB or less is left whole, so that every branch published before parts existed reads as it did.
ci/lab/publish.sh joins what a branch holds before merging into it and splits before publishing; whoever reads a
pub/lab-* branch joins after fetching (ci/world/head.sh, ci/world/encoders.sh).
"""
import argparse
import hashlib
import json
import os
import sys

LIMIT = 99 * 1024 * 1024
PART = 90 * 1024 * 1024


def digest(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 22), b""):
            h.update(b)
    return h.hexdigest()


def split(top, limit=LIMIT, part=PART):
    n = 0
    for root, dirs, files in os.walk(top):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in sorted(files):
            p = os.path.join(root, f)
            if f.endswith(".parts.json") or os.path.islink(p) or os.path.getsize(p) <= limit:
                continue
            size, whole, parts = os.path.getsize(p), digest(p), []
            with open(p, "rb") as fh:
                for i, b in enumerate(iter(lambda: fh.read(part), b"")):
                    name = "%s.part%02d" % (f, i)
                    with open(os.path.join(root, name), "wb") as w:
                        w.write(b)
                    parts.append({"file": name, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()})
            with open(p + ".parts.json", "w") as w:
                json.dump({"file": f, "bytes": size, "sha256": whole, "parts": parts, "made_by": "ci/lab/bigfiles.py"}, w, indent=1)
                w.write("\n")
            os.remove(p)
            n += 1
            print("split %s (%d bytes) into %d parts" % (os.path.relpath(p, top), size, len(parts)), flush=True)
    return n


def join(top):
    n = 0
    for root, dirs, files in os.walk(top):
        dirs[:] = [d for d in dirs if d != ".git"]
        for f in sorted(files):
            if not f.endswith(".parts.json"):
                continue
            meta = json.load(open(os.path.join(root, f)))
            out = os.path.join(root, meta["file"])
            h = hashlib.sha256()
            with open(out + ".joining", "wb") as w:
                for q in meta["parts"]:
                    with open(os.path.join(root, q["file"]), "rb") as r:
                        b = r.read()
                    if len(b) != q["bytes"] or hashlib.sha256(b).hexdigest() != q["sha256"]:
                        sys.exit("part %s of %s is damaged" % (q["file"], meta["file"]))
                    w.write(b); h.update(b)
            if os.path.getsize(out + ".joining") != meta["bytes"] or h.hexdigest() != meta["sha256"]:
                sys.exit("%s joined to the wrong file" % meta["file"])
            os.replace(out + ".joining", out)
            for q in meta["parts"]:
                os.remove(os.path.join(root, q["file"]))
            os.remove(os.path.join(root, f))
            n += 1
            print("joined %s (%d bytes) from %d parts" % (os.path.relpath(out, top), meta["bytes"], len(meta["parts"])), flush=True)
    return n


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("what", choices=("split", "join"))
    ap.add_argument("dir")
    ap.add_argument("--limit", type=int, default=LIMIT)
    ap.add_argument("--part", type=int, default=PART)
    a = ap.parse_args()
    n = split(a.dir, a.limit, a.part) if a.what == "split" else join(a.dir)
    print("%s: %d file(s)" % (a.what, n))


if __name__ == "__main__":
    main()
