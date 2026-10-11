"""The lab's own photo fetcher (fallback for tools/species/fetch_photos.py, same interface).

Usage: python3 tools/lab/fetch_photos.py <manifest.csv> <dir> [--shard i/n] [--mode block|mod] [--rows N] [--limit N] [--threads T]
Saves <dir>/<id>.jpg for each row's photo_url; skips files already present; never stops on one bad download.
Shards are contiguous blocks of rows, matching tools/lab/lab.py.
"""
import argparse
import concurrent.futures as cf
import csv
import math
import pathlib
import sys
import time
import urllib.request

UA = "seen-back-lab/1 (research; github.com/jampotful/seen-back)"


def get(url, dest, tries=4):
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                body = r.read()
            if len(body) < 200:
                raise IOError("short body (%d bytes)" % len(body))
            tmp = dest.with_suffix(".part")
            tmp.write_bytes(body)
            tmp.rename(dest)
            return None
        except Exception as e:  # noqa: BLE001 - report and keep going
            last = "%s: %s" % (type(e).__name__, e)
            if "404" in last:
                break
            time.sleep(1.5 * (k + 1))
    return last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("dir")
    ap.add_argument("--shard")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--rows", type=int, help="use only the first ROWS rows of the manifest (before sharding)")
    ap.add_argument("--mode", choices=["block", "mod"], default="block", help="shards: contiguous blocks, or index modulo n")
    ap.add_argument("--threads", type=int, default=24)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.manifest, newline="", encoding="utf-8")))
    if a.rows:
        rows = rows[:a.rows]
    if a.shard:
        i, n = (int(x) for x in a.shard.split("/"))
        if a.mode == "mod":
            rows = rows[i::n]
        else:
            per = math.ceil(len(rows) / n) if rows else 0
            rows = rows[i * per:(i + 1) * per]
    if a.limit:
        rows = rows[:a.limit]
    out = pathlib.Path(a.dir)
    out.mkdir(parents=True, exist_ok=True)
    todo = [(r["id"], r["photo_url"]) for r in rows if r.get("photo_url") and not (out / ("%s.jpg" % r["id"])).exists()]
    t0 = time.time()
    fails = []
    with cf.ThreadPoolExecutor(a.threads) as ex:
        futs = {ex.submit(get, url, out / ("%s.jpg" % rid)): rid for rid, url in todo}
        for k, f in enumerate(cf.as_completed(futs), 1):
            err = f.result()
            if err:
                fails.append((futs[f], err))
            if k % 200 == 0:
                print("fetched %d/%d (%.1fs)" % (k, len(todo), time.time() - t0), flush=True)
    print("photos: %d rows, %d to fetch, %d failed, %.1fs" % (len(rows), len(todo), len(fails), time.time() - t0))
    for rid, err in fails[:100]:
        print("  failed %s: %s" % (rid, err))
    return 0


if __name__ == "__main__":
    sys.exit(main())
