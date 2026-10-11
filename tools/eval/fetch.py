#!/usr/bin/env python3
"""Fetch the published data and model vectors into one directory that every study reads.

  python3 -I tools/eval/fetch.py <root> [--store <git dir>] [--prefix refs/remotes/origin/pub/] [--remote <address>]

Without --store it keeps a bare git store at <root>/pub.git and fetches every pub/* branch of the remote into it
(depth 1; this downloads the ONNX files too, about 1 GB). With --store it reads the pub branches of a clone that
already has them (it runs `git fetch` there first), which is what the evaluation agent does on its own machine.

It then extracts, for every branch pub/lab-<model>, the files the studies need (card.json, _made.txt, _files.json,
images/, text/, onnx/parity.json) into <root>/lab/<model>/, and the whole of pub/data-alachua into <root>/data/.
<root>/FETCHED.json records the commit and the _made.txt of every branch, so that a report can say what it was made from.
"""
import argparse, io, json, os, pathlib, subprocess, sys, tarfile

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("--store")
ap.add_argument("--prefix")
ap.add_argument("--remote", default="https://github.com/jampotful/seen-back")
a = ap.parse_args()
root = pathlib.Path(a.root)
root.mkdir(parents=True, exist_ok=True)


def git(*args, binary=False):
    r = subprocess.run(["git", "--git-dir", str(store)] + list(args), capture_output=True)
    if r.returncode:
        raise SystemExit("git %s failed: %s" % (" ".join(args), r.stderr.decode()[-400:]))
    return r.stdout if binary else r.stdout.decode()


if a.store:
    store = pathlib.Path(a.store)
    prefix = a.prefix or "refs/remotes/origin/pub/"
    git("fetch", "--quiet", "origin", "+refs/heads/pub/*:" + prefix + "*")
else:
    store = root / "pub.git"
    prefix = a.prefix or "refs/heads/pub/"
    if not store.exists():
        subprocess.run(["git", "init", "--quiet", "--bare", str(store)], check=True)
    git("fetch", "--quiet", "--depth", "1", a.remote, "+refs/heads/pub/*:" + prefix + "*")

WANT = ("card.json", "_made.txt", "_files.json", "images", "text", "onnx/parity.json")
fetched = {}
for line in git("for-each-ref", "--format=%(objectname) %(refname)", prefix).splitlines():
    sha, ref = line.split()
    name = ref[len(prefix):]
    if name.startswith("lab-"):
        out = root / "lab" / name[4:]
        have = set(git("ls-tree", "-r", "--name-only", sha).splitlines())
        paths = sorted({p.split("/")[0] if p.split("/")[0] in WANT else p for p in have if p in WANT or p.split("/")[0] in WANT})
    elif name.startswith("data-"):
        out = root / "data"
        paths = []
    else:
        continue
    out.mkdir(parents=True, exist_ok=True)
    data = git("archive", "--format=tar", sha, *paths, binary=True)
    with tarfile.open(fileobj=io.BytesIO(data)) as t:
        t.extractall(out, filter="data")
    made = {}
    try:
        for ln in git("show", sha + ":_made.txt").splitlines():
            if "=" in ln:
                k, v = ln.split("=", 1)
                made[k] = v
    except SystemExit:
        pass
    fetched["pub/" + name] = {"commit": sha, **made}
    print("pub/" + name, sha[:12], made.get("made_at", ""), "->", out)
(root / "FETCHED.json").write_text(json.dumps(fetched, indent=1, sort_keys=True) + "\n", encoding="utf-8")
print("wrote", root / "FETCHED.json", "with", len(fetched), "branches")
