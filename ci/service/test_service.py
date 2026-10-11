"""Test the species service at an address, exactly as the page's browser would call it.

Usage: python3 ci/service/test_service.py --base http://127.0.0.1:7860 --manifest data/eval/alachua-2025/manifest.csv
           --out out [--n 20] [--wait 900] [--head service/heads/us-fl-alachua --lab-images ... --lab-ids ...]

Checks, in order: health (waiting up to --wait seconds for it), the cross-origin preflight from the page's origin,
a preflight and a call from another origin (both must be refused), twenty test photos from the evaluation manifest
sent with their months in Gradio's two steps (POST .../gradio_api/call/identify, then the event stream), top-1 against
the manifest's species, timings, the refusals (too large, not an image, a bad month, an unknown region), and an answer
with no region. With --head and the laboratory's vectors it also says whether each answer matches what the laboratory's
own vectors give under the same head. Writes results.json and summary.txt into --out. Exit 0 when everything passed.
"""
import argparse
import base64
import csv
import io
import json
import os
import statistics
import time

import numpy as np
import requests
from PIL import Image

PAGE_ORIGIN = "https://jampotful.github.io"
OTHER_ORIGIN = "https://example.org"
S = requests.Session()
S.headers["User-Agent"] = "seen-back-ci-test"


def now_ms(t0):
    return int(round((time.perf_counter() - t0) * 1000))


def call(base, data, origin=PAGE_ORIGIN, timeout=240):
    """Gradio's two steps, as a browser makes them. Returns (result or None, info)."""
    url = base.rstrip("/") + "/gradio_api/call/identify"
    t0 = time.perf_counter()
    info = {}
    try:
        r = S.post(url, json={"data": data}, headers={"Origin": origin, "Content-Type": "application/json"}, timeout=60)
    except requests.RequestException as e:
        info["post_error"] = type(e).__name__
        return None, info
    info["ms_post"] = now_ms(t0)
    info["post_status"] = r.status_code
    info["post_acao"] = r.headers.get("access-control-allow-origin")
    if r.status_code != 200:
        info["post_body"] = r.text[:300]
        return None, info
    try:
        eid = r.json()["event_id"]
    except Exception:
        info["post_body"] = r.text[:300]
        return None, info
    result, event, events = None, None, []
    try:
        g = S.get(url + "/" + eid, headers={"Origin": origin, "Accept": "text/event-stream"}, stream=True, timeout=(20, timeout))
        info["get_status"] = g.status_code
        info["get_acao"] = g.headers.get("access-control-allow-origin")
        info["get_type"] = g.headers.get("content-type")
        for line in g.iter_lines(decode_unicode=True):
            if not line:
                continue
            if line.startswith("event:"):
                event = line[6:].strip()
                events.append(event)
            elif line.startswith("data:"):
                payload = line[5:].strip()
                if event == "complete":
                    v = json.loads(payload)
                    result = v[0] if isinstance(v, list) and v else v
                    break
                if event == "error":
                    info["error_event"] = payload[:300]
                    break
        g.close()
    except requests.RequestException as e:
        info["get_error"] = type(e).__name__
    info["events"] = events
    info["ms_total"] = now_ms(t0)
    return result, info


def photo_b64(url):
    r = S.get(url, timeout=40)
    r.raise_for_status()
    raw = r.content
    im = Image.open(io.BytesIO(raw))
    resized = False
    if im.format != "JPEG" or max(im.size) > 512:
        im = im.convert("RGB")
        im.thumbnail((512, 512), Image.BICUBIC)
        b = io.BytesIO()
        im.save(b, "JPEG", quality=90)
        raw, resized = b.getvalue(), True
    return base64.b64encode(raw).decode("ascii"), len(raw), im.size, resized


def lab_expectations(head_dir, images, ids_path, wanted):
    import pathlib
    d = pathlib.Path(head_dir)
    m = json.loads((d / "manifest.json").read_text())
    rows = np.fromfile(d / m["species"]["url"], dtype="<f2").astype(np.float64).reshape(-1, m["width"])
    t = json.loads((d / m["species"]["table"]).read_text())
    W = np.array([r[3] for r in t["species"]], dtype=np.float64)
    tot = W.sum(0)
    lp = np.log(np.maximum(np.divide(W, tot, out=np.zeros_like(W), where=tot > 0), m["fusion"].get("prior_floor", 1e-6)))
    lp[:, tot <= 0] = 0
    ids = json.loads(open(ids_path).read())
    ids = ids.get("ids") or ids.get("rows") if isinstance(ids, dict) else ids
    pos = {x: i for i, x in enumerate(ids)}
    E = np.load(images).astype(np.float64)
    out = {}
    for rid, month in wanted:
        if rid not in pos:
            continue
        e = E[pos[rid]] / np.linalg.norm(E[pos[rid]])
        z = m["fusion"]["t_species"] * (rows @ e) + m["fusion"]["alpha_prior"] * lp.T[month - 1]
        p = np.exp(z - z.max())
        p /= p.sum()
        j = int(p.argmax())
        out[rid] = {"key": t["keys"][j], "p": float(p[j])}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--wait", type=int, default=900)
    ap.add_argument("--head")
    ap.add_argument("--lab-images")
    ap.add_argument("--lab-ids")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    base = a.base.rstrip("/")
    res = {"base": base, "checks": {}}
    lines = []

    def say(s):
        print(s, flush=True)
        lines.append(s)

    # 1. health
    t0 = time.perf_counter()
    health, last = None, None
    while time.perf_counter() - t0 < a.wait:
        try:
            r = S.get(base + "/v1/health", timeout=15)
            last = r.status_code
            if r.status_code == 200 and r.json().get("ok"):
                health = r.json()
                break
        except Exception as e:
            last = type(e).__name__
        time.sleep(2)
    res["health"] = health
    res["seconds_to_health"] = round(time.perf_counter() - t0, 1)
    res["checks"]["health"] = health is not None
    say("health: %s after %.1f s (%s)" % ("ok" if health else "NOT OK, last %s" % last, res["seconds_to_health"], json.dumps(health)))
    if not health:
        json.dump(res, open(os.path.join(a.out, "results.json"), "w"), indent=1)
        open(os.path.join(a.out, "summary.txt"), "w").write("\n".join(lines) + "\n")
        raise SystemExit(1)
    r = S.get(base + "/v1/health", headers={"Origin": PAGE_ORIGIN}, timeout=15)
    res["checks"]["health_cors"] = r.headers.get("access-control-allow-origin") == PAGE_ORIGIN
    say("health from the page's origin: %d, Access-Control-Allow-Origin %s" % (r.status_code, r.headers.get("access-control-allow-origin")))

    # 2. preflights
    call_url = base + "/gradio_api/call/identify"
    pre = {}
    for origin in (PAGE_ORIGIN, "http://localhost:8786", OTHER_ORIGIN):
        r = S.options(call_url, headers={"Origin": origin, "Access-Control-Request-Method": "POST",
                                         "Access-Control-Request-Headers": "content-type"}, timeout=20)
        pre[origin] = {"status": r.status_code, "allow_origin": r.headers.get("access-control-allow-origin"),
                       "allow_methods": r.headers.get("access-control-allow-methods"),
                       "allow_headers": r.headers.get("access-control-allow-headers"),
                       "max_age": r.headers.get("access-control-max-age")}
        say("preflight from %s: %s" % (origin, json.dumps(pre[origin])))
    res["preflight"] = pre
    res["checks"]["preflight_page"] = (pre[PAGE_ORIGIN]["allow_origin"] == PAGE_ORIGIN
                                       and "POST" in (pre[PAGE_ORIGIN]["allow_methods"] or "")
                                       and "content-type" in (pre[PAGE_ORIGIN]["allow_headers"] or "").lower())
    res["checks"]["preflight_localhost"] = pre["http://localhost:8786"]["allow_origin"] == "http://localhost:8786"
    res["checks"]["preflight_other_refused"] = not pre[OTHER_ORIGIN]["allow_origin"]

    # 3. a call from another origin
    r = S.post(call_url, json={"data": ["", 1, "us-fl-alachua", 5]}, headers={"Origin": OTHER_ORIGIN}, timeout=20)
    res["other_origin_call"] = {"status": r.status_code, "allow_origin": r.headers.get("access-control-allow-origin"), "body": r.text[:200]}
    res["checks"]["other_origin_refused"] = r.status_code == 403 and not r.headers.get("access-control-allow-origin")
    say("call from %s: %d %s" % (OTHER_ORIGIN, r.status_code, r.text[:160]))

    # 4. twenty photos
    rows = [r for r in csv.DictReader(open(a.manifest, encoding="utf-8")) if r["split"] == "test"]
    rows.sort(key=lambda r: r["id"])
    picks, used = [], set()
    for i in range(a.n):
        j = int(i * len(rows) / a.n)
        picks.append(j)
    photos = []
    for j in picks:
        for k in range(j, min(j + 4, len(rows))):
            if k in used:
                continue
            row = rows[k]
            try:
                b64, nbytes, size, resized = photo_b64(row["photo_url"])
            except Exception as e:
                say("photo %s not fetched (%s); trying the next row" % (row["id"], type(e).__name__))
                used.add(k)
                continue
            used.add(k)
            photos.append((row, b64, nbytes, size, resized))
            break
    answers = []
    for n, (row, b64, nbytes, size, resized) in enumerate(photos):
        result, info = call(base, [b64, int(row["month"]), "us-fl-alachua", 5])
        ok = isinstance(result, dict) and "species" in result
        top = result["species"][0] if ok and result["species"] else {}
        keys5 = [s.get("key") for s in result["species"]] if ok else []
        ans = {"id": row["id"], "month": int(row["month"]), "truth_key": int(row["key"]), "truth_sci": row["sci"],
               "truth_eyes": row["eyes"], "bytes": nbytes, "size": list(size), "resized": resized,
               "answered": ok, "top1_key": top.get("key"), "top1_sci": top.get("sci"), "top1_en": top.get("en"),
               "top1_eyes": top.get("eyes"), "top1_p": top.get("p"),
               "top1_right": ok and top.get("key") == int(row["key"]), "top5_right": int(row["key"]) in keys5,
               "kind_right": ok and bool(result.get("kinds")) and result["kinds"][0]["key"] == row["eyes"],
               "server_ms": result.get("ms") if ok else None, "device": result.get("device") if ok else None,
               "error": (result or {}).get("error") if isinstance(result, dict) else None, **info}
        answers.append(ans)
        say("%2d %s %-32s -> %-32s p %.3f %s  %d ms total, %s ms in the service, ACAO post %s get %s"
            % (n + 1, row["id"], row["sci"][:32], (top.get("sci") or str(ans["error"]))[:32], top.get("p") or 0,
               "RIGHT" if ans["top1_right"] else "wrong", info.get("ms_total", -1), ans["server_ms"],
               info.get("post_acao"), info.get("get_acao")))
    res["photos"] = answers
    got = [x for x in answers if x["answered"]]
    tot = [x["ms_total"] for x in got]
    srv = [x["server_ms"] for x in got if x["server_ms"] is not None]
    warm = tot[1:] if len(tot) > 1 else tot
    res["summary"] = {
        "photos": len(answers), "answered": len(got),
        "top1": sum(x["top1_right"] for x in answers), "top5": sum(x["top5_right"] for x in answers),
        "kind_top1": sum(x["kind_right"] for x in answers),
        "first_call_ms": tot[0] if tot else None,
        "total_ms_median": statistics.median(tot) if tot else None, "total_ms_worst": max(tot) if tot else None,
        "warm_total_ms_median": statistics.median(warm) if warm else None, "warm_total_ms_worst": max(warm) if warm else None,
        "server_ms_median": statistics.median(srv) if srv else None, "server_ms_worst": max(srv) if srv else None,
        "acao_on_every_call": all(x.get("post_acao") == PAGE_ORIGIN and x.get("get_acao") == PAGE_ORIGIN for x in got),
        "event_stream_type": got[0].get("get_type") if got else None,
    }
    res["checks"]["photos_answered"] = len(got) >= max(1, a.n - 2)
    res["checks"]["acao_on_calls"] = res["summary"]["acao_on_every_call"]
    say("photos: %(answered)d of %(photos)d answered, top-1 right %(top1)d, top-5 %(top5)d, kind of eye %(kind_top1)d; "
        "first call %(first_call_ms)s ms; total per photo median %(total_ms_median)s ms, worst %(total_ms_worst)s ms; "
        "warm (2nd on) median %(warm_total_ms_median)s, worst %(warm_total_ms_worst)s; in the service median %(server_ms_median)s, worst %(server_ms_worst)s"
        % res["summary"])

    # 5. parity with the laboratory's vectors
    if a.head and a.lab_images and a.lab_ids:
        exp = lab_expectations(a.head, a.lab_images, a.lab_ids, [(x["id"], x["month"]) for x in answers])
        same, dp = 0, []
        for x in answers:
            e = exp.get(x["id"])
            if e and x["answered"]:
                x["lab_top1_key"], x["lab_top1_p"] = e["key"], round(e["p"], 4)
                same += e["key"] == x["top1_key"]
                dp.append(abs(e["p"] - (x["top1_p"] or 0)))
        res["summary"]["same_top1_as_lab_vectors"] = same
        res["summary"]["lab_compared"] = len(dp)
        res["summary"]["max_abs_p_difference_vs_lab"] = round(max(dp), 4) if dp else None
        say("parity with the laboratory's own vectors under the same head: same top-1 on %d of %d, largest difference in p %s"
            % (same, len(dp), res["summary"]["max_abs_p_difference_vs_lab"]))

    # 6. refusals and the empty region
    first = photos[0] if photos else None
    cases = [
        ("too_large", ["A" * 2_100_000, 5, "us-fl-alachua", 5]),
        ("not_image", [base64.b64encode(b"this is not a photograph, only words").decode(), 5, "us-fl-alachua", 5]),
        ("bad_month", [first[1] if first else "", 13, "us-fl-alachua", 5]),
        ("unknown_region", [first[1] if first else "", 5, "xx-nowhere", 5]),
    ]
    ref = {}
    for want, data in cases:
        result, info = call(base, data)
        code = result.get("code") if isinstance(result, dict) else None
        ref[want] = {"code": code, "error": result.get("error") if isinstance(result, dict) else None,
                     "ms_total": info.get("ms_total"), "post_status": info.get("post_status"), "error_event": info.get("error_event")}
        say("refusal %s: got %s, %r" % (want, code, ref[want]["error"]))
    res["refusals"] = ref
    res["checks"]["refusals"] = all(v["code"] == k for k, v in ref.items())
    if first:
        result, info = call(base, [first[1], int(first[0]["month"]), "", 3])
        res["no_region"] = {"region": result.get("region") if isinstance(result, dict) else None,
                            "note": result.get("note") if isinstance(result, dict) else None,
                            "top1": (result.get("species") or [{}])[0] if isinstance(result, dict) else None}
        res["checks"]["no_region"] = isinstance(result, dict) and result.get("region") == "" and bool(result.get("note"))
        say("no region: %s" % json.dumps(res["no_region"]))
    res["passed"] = all(res["checks"].values())
    say("checks: " + ", ".join("%s %s" % (k, "pass" if v else "FAIL") for k, v in res["checks"].items()))
    json.dump(res, open(os.path.join(a.out, "results.json"), "w"), indent=1)
    open(os.path.join(a.out, "summary.txt"), "w").write("\n".join(lines) + "\n")
    raise SystemExit(0 if res["passed"] else 1)


if __name__ == "__main__":
    main()
