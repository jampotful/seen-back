"""Create or update the Space `seen-back-naturalist` on ZeroGPU, wait for it, and test it at its public address.

Usage: python3 ci/service/deploy.py <bundle dir> <out dir> <eval manifest>
Money: the only hardware ever requested is ZeroGPU (`zero-a10g`). After the create, after the upload and at every poll
the Space's hardware and storage are read back; anything that is not ZeroGPU (or CPU basic while it is first assigned)
or any persistent storage, and the Space is deleted at once and the job fails. Nothing here subscribes, upgrades or
touches billing. If the create is refused, the server's words are written to refusal.txt (the account name, if it
appears, replaced by <account>) and the job stops. The token is never printed.
"""
import json
import os
import subprocess
import sys
import time

import requests
from huggingface_hub import HfApi

BUNDLE, OUT, MANIFEST = sys.argv[1], sys.argv[2], sys.argv[3]
NAME = "seen-back-naturalist"
ZERO = "zero-a10g"
FREE_CURRENT = {None, "cpu-basic", ZERO}
TOKEN = os.environ["HF_TOKEN"].strip()
os.makedirs(OUT, exist_ok=True)
LOG = open(os.path.join(OUT, "deploy.txt"), "a")
api = HfApi(token=TOKEN)
T0 = time.time()


def say(s):
    s = "[%6.1f s] %s" % (time.time() - T0, s.replace(TOKEN, "<token>"))
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def save(name, obj):
    with open(os.path.join(OUT, name), "w") as f:
        json.dump(obj, f, indent=1)


def logs(repo, kind, seconds=12, keep=250):
    """The Space's build or run log (server-sent events), last lines only, token scrubbed."""
    try:
        r = requests.get("https://huggingface.co/api/spaces/%s/logs/%s" % (repo, kind),
                         headers={"Authorization": "Bearer " + TOKEN}, stream=True, timeout=(10, seconds))
        out, t = [], time.time()
        for line in r.iter_lines(decode_unicode=True):
            if line and line.startswith("data:"):
                try:
                    out.append(json.loads(line[5:]).get("data", "").rstrip())
                except Exception:
                    out.append(line[5:].rstrip())
            if time.time() - t > seconds:
                break
        r.close()
    except Exception as e:
        out = ["(log not read: %s)" % type(e).__name__]
    text = "\n".join(out[-keep:]).replace(TOKEN, "<token>")
    with open(os.path.join(OUT, "space-%s-log.txt" % kind), "w") as f:
        f.write(text + "\n")
    return text


def guard(repo, label):
    rt = api.get_space_runtime(repo)
    cur, req = rt.hardware, rt.requested_hardware
    cur = None if cur is None else str(getattr(cur, "value", cur))
    req = None if req is None else str(getattr(req, "value", req))
    say("%s: stage %s, hardware %s, requested %s, storage %s, sleep %s" % (label, rt.stage, cur, req, rt.storage, rt.sleep_time))
    bad = (req is not None and req != ZERO) or (cur not in FREE_CURRENT) or bool(rt.storage)
    if bad:
        say("hardware or storage that could cost money: deleting the Space now")
        api.delete_repo(repo, repo_type="space", missing_ok=True)
        save("hardware.json", {"stage": rt.stage, "hardware": cur, "requested": req, "storage": rt.storage, "deleted": True})
        sys.exit(3)
    return rt, cur, req


def main():
    user = api.whoami()["name"]
    repo = "%s/%s" % (user, NAME)
    res = {"space": NAME}
    existed = api.repo_exists(repo, repo_type="space")
    say("Space exists already: %s" % existed)
    if existed:
        guard(repo, "before update")
    else:
        try:
            api.create_repo(repo, repo_type="space", space_sdk="gradio", space_hardware=ZERO, private=False, exist_ok=False)
        except Exception as e:
            resp = getattr(e, "response", None)
            text = resp.text if resp is not None else str(e)
            status = resp.status_code if resp is not None else None
            red = text.replace(TOKEN, "<token>")
            redacted = user in red
            red = red.replace(user, "<account>")
            with open(os.path.join(OUT, "refusal.txt"), "w") as f:
                f.write("HTTP %s\n%s\n" % (status, red))
            save("deploy.json", {"created": False, "refused": True, "http_status": status, "refusal": red,
                                 "account_name_redacted": redacted, "exception": type(e).__name__})
            say("create refused: HTTP %s: %s" % (status, red))
            sys.exit(2)
        say("created")
    guard(repo, "after create")
    t_up = time.time()
    api.upload_folder(repo_id=repo, repo_type="space", folder_path=BUNDLE, ignore_patterns=["site/*", "__pycache__/*", ".gitignore"],
                      commit_message="Seen Back naturalist: Gradio app, BioCLIP 2 head for Alachua County")
    say("uploaded in %.1f s" % (time.time() - t_up))
    guard(repo, "after upload")
    t_built = None
    stage = None
    while time.time() - t_up < 20 * 60:
        rt, cur, req = guard(repo, "poll")
        stage = rt.stage
        if stage == "RUNNING":
            t_built = time.time()
            break
        if stage in ("BUILD_ERROR", "RUNTIME_ERROR", "CONFIG_ERROR", "NO_APP_FILE", "PAUSED", "STOPPED", "DELETING"):
            say("stage %s: %s" % (stage, json.dumps(rt.raw.get("errorMessage"))[:1500]))
            break
        time.sleep(15)
    res["stage"] = stage
    res["seconds_upload_to_running"] = None if t_built is None else round(t_built - t_up, 1)
    logs(repo, "build", seconds=10)
    if stage != "RUNNING":
        logs(repo, "run", seconds=10)
        save("deploy.json", res)
        say("not running after %.0f s; stopping" % (time.time() - t_up))
        sys.exit(4)
    info = api.space_info(repo)
    host = getattr(info, "host", None)
    if not host:
        doms = (api.get_space_runtime(repo).raw.get("domains") or [{}])
        host = "https://" + doms[0].get("domain", "")
    res["address"] = host
    say("running at %s after %.0f s from upload" % (host, t_built - t_up))
    t_h = time.time()
    ok = False
    while time.time() - t_h < 300:
        try:
            r = requests.get(host + "/v1/health", timeout=20)
            if r.status_code == 200 and r.json().get("ok"):
                ok = True
                res["health"] = r.json()
                break
        except Exception:
            pass
        time.sleep(3)
    res["seconds_running_to_health"] = round(time.time() - t_h, 1)
    say("health %s after %.1f s more: %s" % ("ok" if ok else "NOT OK", res["seconds_running_to_health"], json.dumps(res.get("health"))))
    rc = subprocess.call([sys.executable, "ci/service/test_service.py", "--base", host, "--manifest", MANIFEST,
                          "--out", os.path.join(OUT, "remote"), "--wait", "120"] + sys.argv[4:])
    res["remote_test_exit"] = rc
    rt, cur, req = guard(repo, "after test")
    res["hardware"] = {"current": cur, "requested": req, "storage": rt.storage, "sleep_time": rt.sleep_time, "stage": rt.stage}
    logs(repo, "run", seconds=8)
    res["service_json"] = {"api": "gradio", "call": host.rstrip("/") + "/gradio_api/call/identify",
                           "health": host.rstrip("/") + "/v1/health", "region": "us-fl-alachua", "model": "bioclip2-l14"}
    save("service.json", res["service_json"])
    save("deploy.json", res)
    say("done: test exit %d" % rc)
    sys.exit(0 if rc == 0 else 5)


if __name__ == "__main__":
    main()
