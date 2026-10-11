"""Fetch each address in a list and save it as a file. HTML is also saved as plain text beside the original.

Usage: python3 fetch.py <list file> <output directory>
A line is: <address> [file name]. Lines starting with # are skipped. Each download is capped at 8 MB.
"""
import html
import pathlib
import re
import sys
import urllib.request
import time

CAP = 8 * 1024 * 1024
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)


def as_text(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</(p|div|li|tr|h[1-6]|section|article)>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"[ \t\r\f\v]+", " ", raw)
    return re.sub(r"\n\s*\n+", "\n\n", raw).strip()


n = 0
for line in src.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = line.split(None, 1)
    url = parts[0]
    n += 1
    time.sleep(1.5)  # iNaturalist asks for about one request a second
    name = parts[1].strip() if len(parts) > 1 else "%02d-%s" % (n, re.sub(r"[^A-Za-z0-9.]+", "-", url.split("//", 1)[-1])[:80].strip("-"))
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "seen-back-ci/1 (research; github.com/jampotful/seen-back)", "Accept": "*/*"})
        with urllib.request.urlopen(req, timeout=40) as r:
            body = r.read(CAP + 1)
            kind = r.headers.get("Content-Type", "")
            code = r.status
    except Exception as e:  # keep going; one dead address should not lose the rest
        print("FAIL %s -> %s: %s" % (url, type(e).__name__, e))
        continue
    cut = len(body) > CAP
    body = body[:CAP]
    (out / name).write_bytes(body)
    note = ""
    if "html" in kind.lower() or body[:200].lower().lstrip().startswith((b"<!doctype html", b"<html")):
        (out / (name + ".txt")).write_text(as_text(body.decode("utf-8", "replace")), encoding="utf-8")
        note = " (+ .txt)"
    print("OK %s %s -> %s, %d bytes%s%s" % (code, url, name, len(body), ", cut at 8 MB" if cut else "", note))
