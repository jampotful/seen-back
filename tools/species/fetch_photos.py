#!/usr/bin/env python3
"""Download the photos of an evaluation manifest.

Usage: python3 tools/species/fetch_photos.py <manifest.csv> <dir> [--shard i/n] [--workers 16] [--strict]

- Each row's photo_url is saved as <dir>/<id>.jpg (the name is fixed; the bytes are whatever the bucket serves).
- --shard i/n takes the rows whose position in the manifest (0-based, header excluded) modulo n equals i,
  with 0 <= i < n. Example: four jobs use 0/4, 1/4, 2/4 and 3/4.
- Resumable: a file already present with image content is kept. Downloads go to a .part file first.
- At most 16 downloads at once; retries with backoff on network errors, 429 and 5xx; 403 and 404 are final.
- Failures are printed and written to <dir>/_failures.tsv (id, url, reason), or _failures-<i>-of-<n>.tsv for a shard. The exit status is 0 even when
  some photos fail (a manifest row that could not be fetched is expected to be skipped by the evaluation), unless
  --strict is given; it is 1 when nothing at all could be fetched, and 2 for bad arguments.
"""
import argparse
import concurrent.futures as cf
import csv
import os
import random
import sys
import threading
import time
from collections import Counter
from pathlib import Path

import requests

UA = "seen-back-eval/1 (+https://github.com/jampotful/seen-back; evaluation photo fetcher)"
MAGIC = (b"\xff\xd8\xff", b"\x89PNG\r\n\x1a\n", b"GIF87a", b"GIF89a")
_local = threading.local()


def is_image(head):
    return head.startswith(MAGIC) or (head[:4] == b"RIFF" and head[8:12] == b"WEBP")


def session():
    s = getattr(_local, "s", None)
    if s is None:
        s = requests.Session()
        s.headers.update({"User-Agent": UA})
        _local.s = s
    return s


def fetch(row, outdir, tries, timeout):
    dest = outdir / ("%s.jpg" % row["id"])
    if dest.exists() and dest.stat().st_size > 0:
        with open(dest, "rb") as f:
            if is_image(f.read(16)):
                return row["id"], "kept", 200, ""
    part = dest.with_name(dest.name + ".part")
    delay, last, code = 1.0, "", 0
    for attempt in range(1, tries + 1):
        try:
            r = session().get(row["photo_url"], timeout=timeout)
            code = r.status_code
            if code == 200:
                body = r.content
                if not is_image(body[:16]):
                    last = "not an image (%d bytes, %s)" % (len(body), r.headers.get("Content-Type", ""))
                else:
                    part.write_bytes(body)
                    os.replace(part, dest)
                    return row["id"], "fetched", code, ""
            elif code in (403, 404, 410):
                return row["id"], "failed", code, "HTTP %d" % code
            else:
                last = "HTTP %d" % code
        except requests.RequestException as e:
            last = "%s: %s" % (type(e).__name__, e)
        if attempt < tries:
            time.sleep(delay + random.random() * delay)
            delay = min(delay * 2, 30)
    return row["id"], "failed", code, last


def main():
    ap = argparse.ArgumentParser(description="Download the photos of an evaluation manifest.")
    ap.add_argument("manifest")
    ap.add_argument("dir")
    ap.add_argument("--shard", default="0/1", help="i/n, 0 <= i < n (default 0/1: every row)")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--tries", type=int, default=5)
    ap.add_argument("--timeout", type=float, default=40)
    ap.add_argument("--strict", action="store_true", help="exit 1 if any photo failed")
    args = ap.parse_args()
    try:
        i, n = (int(x) for x in args.shard.split("/"))
        if not (n >= 1 and 0 <= i < n):
            raise ValueError
    except ValueError:
        print("--shard must be i/n with 0 <= i < n, got %r" % args.shard, file=sys.stderr)
        sys.exit(2)
    workers = max(1, min(args.workers, 16))
    with open(args.manifest, newline="", encoding="utf-8") as f:
        rows = [r for k, r in enumerate(csv.DictReader(f)) if k % n == i]
    outdir = Path(args.dir)
    outdir.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    tally, codes, failures = Counter(), Counter(), []
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(fetch, r, outdir, args.tries, args.timeout) for r in rows]
        by_id = {r["id"]: r for r in rows}
        for k, fu in enumerate(cf.as_completed(futs), 1):
            rid, state, code, why = fu.result()
            tally[state] += 1
            codes[code] += 1
            if state == "failed":
                failures.append((rid, by_id[rid]["photo_url"], why))
            if k % 500 == 0:
                print("  %d/%d %s (%.0fs)" % (k, len(rows), dict(tally), time.time() - t0), flush=True)
    for p in outdir.glob("*.jpg.part"):
        p.unlink()
    fail_path = outdir / ("_failures.tsv" if n == 1 else "_failures-%d-of-%d.tsv" % (i, n))
    if failures:
        with open(fail_path, "w", encoding="utf-8") as f:
            f.write("id\turl\treason\n")
            for rid, url, why in sorted(failures):
                f.write("%s\t%s\t%s\n" % (rid, url, why))
    elif fail_path.exists():
        fail_path.unlink()
    print("shard %d/%d: %d rows; fetched %d, kept %d, failed %d; HTTP status of the last attempt: %s; %.0fs" % (
        i, n, len(rows), tally["fetched"], tally["kept"], tally["failed"], dict(codes), time.time() - t0), flush=True)
    for rid, url, why in sorted(failures)[:20]:
        print("  failed %s %s: %s" % (rid, url, why))
    if rows and tally["fetched"] + tally["kept"] == 0:
        sys.exit(1)
    if failures and args.strict:
        sys.exit(1)


if __name__ == "__main__":
    main()
