#!/usr/bin/env python3
"""Sample the resident memory of browser processes once a second: python3 -I ci/engines/memwatch.py <out.jsonl>
One JSON line a sample: t (epoch ms), total (kB, all matching processes), top (the five largest: kB, pid, name).
Works with the ps of Linux and of macOS (ps -A -o pid=,rss=,args=). Stop it by its process id."""
import json, re, subprocess, sys, time
PAT = re.compile(r"chrom|headless_shell|firefox|Web Content|WebContent|WebKit|Safari|GPU|Networking|RDD Process|Socket Process|Isolated Web|MiniBrowser|pw_run", re.I)
out = open(sys.argv[1], "a")
while True:
    try:
        rows = []
        for line in subprocess.run(["ps", "-A", "-o", "pid=,rss=,args="], capture_output=True, text=True, timeout=10).stdout.splitlines():
            parts = line.strip().split(None, 2)
            if len(parts) < 3 or not PAT.search(parts[2]) or "memwatch" in parts[2] or "node " in parts[2][:40]:
                continue
            name = parts[2].split(" --")[0]
            name = name.split("/")[-1] if len(name) < 200 else name[-120:]
            kind = re.search(r"--type=([\w-]+)|-contentproc.*?\b(tab|rdd|socket|gpu|utility)\b", parts[2])
            if kind: name += " " + (kind.group(1) or kind.group(2))
            rows.append((int(parts[1]), int(parts[0]), name[:80]))
        rows.sort(reverse=True)
        out.write(json.dumps({"t": int(time.time() * 1000), "total": sum(x[0] for x in rows), "top": rows[:5]}) + "\n"); out.flush()
    except Exception as e:
        out.write(json.dumps({"t": int(time.time() * 1000), "error": str(e)[:200]}) + "\n"); out.flush()
    time.sleep(1)
