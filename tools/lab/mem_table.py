"""The table of the memory runs (ci/lab/mem.sh, tools/lab/mem_node.mjs, tools/lab/mem_page.mjs), read from the `ci` branch.

  python3 -I tools/lab/mem_table.py --ref runs/lab/32-mem-base/routes/base --pub <dir with the published vectors> \
      runs/lab/32-mem-base runs/lab/33-mem-a ...

--ref is the shipped file's route (its vectors are the reference for every cosine); --pub, if given, holds
hybrid-fc2-w8.alachua-2025-test320.f16.npy and .ids.json from pub/model-bioclip2-l14 (vectors/), a second reference.
Prints a Markdown table and writes the same numbers as JSON to --json if given.
"""
import argparse
import json
import pathlib
import subprocess

import numpy as np


def show(path, binary=False):
    out = subprocess.run(["git", "show", "origin/ci:" + path], capture_output=True)
    if out.returncode:
        return None
    return out.stdout if binary else out.stdout.decode("utf-8", "replace")


def unit(raw):
    v = np.frombuffer(raw, dtype=np.float32).reshape(-1, 768).astype(np.float64)
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("--ref", required=True)
    ap.add_argument("--pub")
    ap.add_argument("--json")
    a = ap.parse_args()
    ref = unit(show(a.ref + ".f32", True))
    pub = None
    if a.pub:
        pids = json.load(open(pathlib.Path(a.pub) / "hybrid-fc2-w8.alachua-2025-test320.ids.json"))
        pv = np.load(pathlib.Path(a.pub) / "hybrid-fc2-w8.alachua-2025-test320.f16.npy").astype(np.float64)
        pub = (pids, pv / np.linalg.norm(pv, axis=1, keepdims=True))
    rows = []
    for d in a.dirs:
        names = subprocess.run(["git", "ls-tree", "--name-only", "origin/ci", d + "/routes/"], capture_output=True, text=True).stdout.split()
        ids = json.loads(show(d + "/ids.json") or "[]")
        for n in sorted(x for x in names if x.endswith(".json")):
            r = json.loads(show(n))
            name = pathlib.PurePosixPath(n).stem
            row = {"run": d, "route": name}
            raw = show(n[:-5] + ".f32", True)
            if name.startswith("page"):
                ph = r.get("phases", {})
                row.update({"kind": "chromium", "peak_create_mb": (ph.get("session created (worker init, warm-up)") or {}).get("renderer_max_mb"),
                            "peak_photo1_mb": (ph.get("photo 1") or {}).get("renderer_max_mb"), "peak_photo10_mb": (ph.get("photo 10") or {}).get("renderer_max_mb"),
                            "peak_model_in_page_mb": (ph.get("model fetched into the page") or {}).get("renderer_max_mb"),
                            "peak_process_mb": max([p.get("renderer_max_mb", 0) for p in ph.values()] or [0]),
                            "browser_all_mb": max([p.get("browser_all_mb", 0) for p in ph.values()] or [0]),
                            "heap_mb": r.get("heap_mb"), "ready_s": round((r.get("init") or {}).get("ready_ms", 0) / 1000, 1),
                            "photo_s": round(float(np.mean([p["ms"] for p in r.get("photos", [])[1:]] or [0])) / 1000, 2),
                            "error": (r.get("init") or {}).get("fail") or ""})
            else:
                st = {s["step"]: s for s in r.get("steps", [])}
                # the whole run's peak is the highest of the steps' peaks: mem_node.mjs resets the kernel's high-water mark before
                # each step, which also resets what /usr/bin/time reports (that is the last photo's peak only)
                peaks = [s.get("peak_mb") or 0 for s in r.get("steps", [])]
                row.update({"kind": "node", "peak_create_mb": (st.get("session created") or {}).get("peak_mb"),
                            "peak_warm_mb": (st.get("warm-up (empty picture)") or {}).get("peak_mb"),
                            "peak_photo1_mb": (st.get("photo 1") or {}).get("peak_mb"), "peak_photo10_mb": (st.get("photo 10") or {}).get("peak_mb"),
                            "peak_process_mb": max(peaks) if peaks else None,
                            "heap_mb": r.get("heap_final_mb") or (st.get("session failed") or {}).get("heap_mb"),
                            "ready_s": round(r["ready_with_warm_ms"] / 1000, 1) if r.get("ready_with_warm_ms") else None,
                            "create_s": round(r["ready_ms"] / 1000, 1) if r.get("ready_ms") else None,
                            "photo_s": round(r["photo_ms_mean_2_on"] / 1000, 2) if r.get("photo_ms_mean_2_on") else None,
                            "error": r.get("error", "")})
            if raw:
                v = unit(raw)
                k = min(len(v), len(ref))
                c = (v[:k] * ref[:k]).sum(1)
                row.update({"cos_min": float(c.min()), "cos_mean": float(c.mean()), "photos": int(k),
                            "max_abs_diff": float(np.abs(np.frombuffer(raw, dtype=np.float32)[:k * 768] - np.frombuffer(show(a.ref + ".f32", True), dtype=np.float32)[:k * 768]).max())})
                if pub and ids:
                    idx = [pub[0].index(i) for i in ids[:len(v)]]
                    row["cos_pub_min"] = float((v * pub[1][idx]).sum(1).min())
            rows.append(row)
    hdr = "| route | peak resident MB (create / photo 1 / photo 10; whole run) | WASM heap MB | s to ready | s a photo | cosine to shipped (min of %d) |" % len(ref)
    print(hdr)
    print("|---|---|---|---|---|---|")
    for r in rows:
        cos = ("%.7f" % r["cos_min"]) if "cos_min" in r else "n/a"
        print("| %s (%s) | %s / %s / %s; %s | %s | %s | %s | %s |%s" % (r["route"], r["run"].split("/")[-1], r.get("peak_create_mb"), r.get("peak_photo1_mb"),
              r.get("peak_photo10_mb"), r.get("peak_process_mb"), r.get("heap_mb"), r.get("ready_s"), r.get("photo_s"), cos,
              (" error: " + r["error"][:120]) if r.get("error") else ""))
    if a.json:
        pathlib.Path(a.json).write_text(json.dumps(rows, indent=1) + "\n")


if __name__ == "__main__":
    main()
