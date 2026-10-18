#!/usr/bin/env python3
"""Memory of browser processes, about four times a second, with each process's own peak: python3 -I ci/engines/memwatch2.py <out dir>
Writes <out>/mem2.jsonl, one line a sample: t (epoch ms) and p, a list of [pid, name, rss kB, footprint kB, peak kB, threads] for every
matching process with more than 20 MB resident.
  macOS: footprint is the physical footprint (what iOS's memory limit counts) and peak is its lifetime maximum, both from proc_pid_rusage;
         threads from proc_pidinfo.
  Linux: footprint is RssAnon + RssShmem and peak is VmHWM (the peak of the resident size), from /proc/<pid>/status.
On a new high of the largest process (200 MB above its last breakdown, at most one every 4 s) it writes a breakdown of that process to
<out>/mem2-snap.jsonl: on macOS the region summary of `vmmap -summary` (Playwright's WebKit allows it; Safari's processes refuse it), on
Linux each mapping of /proc/<pid>/smaps with more than 8 MB resident. Stop it by its process id."""
import ctypes, json, os, re, subprocess, sys, time
PAT = re.compile(r"WebContent|WPEWebProcess|WPENetworkProcess|WebKitWebProcess|WebKitNetworkProcess|Networking|GPU|WebKit|Safari|MiniBrowser|chrom|headless_shell|firefox", re.I)
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
f = open(os.path.join(out, "mem2.jsonl"), "a"); fs = open(os.path.join(out, "mem2-snap.jsonl"), "a")
MAC = sys.platform == "darwin"
if MAC:
    lib = ctypes.CDLL("/usr/lib/libproc.dylib", use_errno=True)
    buf = ctypes.create_string_buffer(1024); tbuf = ctypes.create_string_buffer(256)
    def stats(pid):
        if lib.proc_pid_rusage(pid, 4, buf) != 0: return None
        q = [int.from_bytes(buf.raw[16 + 8 * i: 24 + 8 * i], "little") for i in range(35)]
        thr = 0
        if lib.proc_pidinfo(pid, 4, ctypes.c_uint64(0), tbuf, 96) >= 96: thr = int.from_bytes(tbuf.raw[84:88], "little")
        return q[6] // 1024, q[7] // 1024, q[28] // 1024, thr        # resident, phys_footprint, lifetime max phys_footprint (bytes to kB)
    def procs():
        r = subprocess.run(["ps", "-A", "-o", "pid=,comm="], capture_output=True, text=True, timeout=10).stdout.splitlines()
        for line in r:
            a = line.strip().split(None, 1)
            if len(a) == 2 and PAT.search(a[1]) and "memwatch" not in a[1]: yield int(a[0]), a[1].split("/")[-1][:60]
    def snap(pid):
        try:
            r = subprocess.run(["sudo", "-n", "vmmap", "-summary", str(pid)], capture_output=True, text=True, timeout=40)
            txt = r.stdout; i = txt.find("Physical footprint"); j = txt.find("REGION TYPE")
            return (txt[i:i + 200] + "\n" + txt[j:j + 9000]) if j >= 0 else ("vmmap failed: " + (r.stderr or txt)[:400])
        except Exception as e: return "vmmap failed: " + str(e)[:200]
else:
    def stats(pid):
        try: s = open("/proc/%d/status" % pid).read()
        except Exception: return None
        g = lambda k: int((re.search(r"^%s:\s+(\d+)" % k, s, re.M) or [0, 0])[1])
        return g("VmRSS"), g("RssAnon") + g("RssShmem"), g("VmHWM"), g("Threads")
    def procs():
        for d in os.listdir("/proc"):
            if not d.isdigit(): continue
            try: cmd = open("/proc/%s/cmdline" % d, "rb").read().replace(b"\0", b" ").decode("utf-8", "replace")
            except Exception: continue
            name = cmd.split(" ")[0].split("/")[-1]
            if name and PAT.search(name) and "memwatch" not in cmd and "python" not in name: yield int(d), name[:60]
    def snap(pid):
        rows, cur = [], None
        try:
            for line in open("/proc/%d/smaps" % pid):
                if re.match(r"^[0-9a-f]+-[0-9a-f]+ ", line):
                    if cur and cur["rss"] > 8192: rows.append(cur)
                    a = line.split(); cur = {"range": a[0], "perm": a[1], "path": a[5] if len(a) > 5 else "", "size": 0, "rss": 0, "anon": 0}
                elif cur:
                    m = re.match(r"^(Size|Rss|Anonymous):\s+(\d+)", line)
                    if m: cur[{"Size": "size", "Rss": "rss", "Anonymous": "anon"}[m.group(1)]] = int(m.group(2))
            if cur and cur["rss"] > 8192: rows.append(cur)
        except Exception as e: return "smaps failed: " + str(e)[:200]
        rows.sort(key=lambda r: -r["rss"]); return rows[:40]
known, last_list, last_snap, snap_at = {}, 0, {}, 0
while True:
    t = time.time()
    try:
        if t - last_list > 1.0: known = dict(procs()); last_list = t
        rows = []
        for pid, name in known.items():
            s = stats(pid)
            if s and s[0] > 20480: rows.append([pid, name] + list(s))
        rows.sort(key=lambda r: -r[2])
        f.write(json.dumps({"t": int(t * 1000), "p": rows[:8]}) + "\n"); f.flush()
        if rows and t - snap_at > 4.0:
            pid, name, rss = rows[0][0], rows[0][1], rows[0][2]
            if rss > last_snap.get(pid, 307200) + 204800:
                last_snap[pid] = rss; snap_at = time.time()
                fs.write(json.dumps({"t": int(t * 1000), "pid": pid, "name": name, "rss": rss, "foot": rows[0][3], "snap": snap(pid)}) + "\n"); fs.flush()
    except Exception as e:
        f.write(json.dumps({"t": int(t * 1000), "error": str(e)[:200]}) + "\n"); f.flush()
    time.sleep(max(0.05, 0.25 - (time.time() - t)))
