"""Is the Hugging Face account behind HF_TOKEN older than 30 days, and how many Spaces does it host already?

Usage: python3 ci/service/account.py <out dir>
Prints yes or no with the age in days, from two independent sources: the public user overview's `createdAt`, and the
creation time inside the account's id (a MongoDB ObjectId begins with its creation time in seconds). Also says whether
the account is PRO, whether its e-mail is verified, whether a payment method is on file (`canPay`), and how many of
its Spaces run on ZeroGPU. Never prints the token or the account name. Writes eligible=yes|no and days=N to
$GITHUB_OUTPUT when that is set.
"""
import datetime as dt
import json
import os
import sys
import urllib.request

TOKEN = os.environ.get("HF_TOKEN", "").strip()
OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
os.makedirs(OUT, exist_ok=True)


def get(url, auth=True, timeout=25):
    h = {"User-Agent": "seen-back-ci"}
    if auth:
        h["Authorization"] = "Bearer " + TOKEN
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
        return json.load(r)


def say(lines, s):
    print(s, flush=True)
    lines.append(s)


def main():
    lines, facts = [], {}
    now = dt.datetime.now(dt.timezone.utc)
    if not TOKEN:
        say(lines, "HF_TOKEN missing")
        sys.exit(1)
    who = get("https://huggingface.co/api/whoami-v2")
    name = who.get("name") or ""
    facts["is_pro"] = who.get("isPro")
    facts["email_verified"] = who.get("emailVerified")
    facts["can_pay"] = who.get("canPay")
    facts["type"] = who.get("type")
    ages = {}
    oid = str(who.get("id") or "")
    try:
        t = dt.datetime.fromtimestamp(int(oid[:8], 16), tz=dt.timezone.utc)
        ages["id_timestamp"] = (now - t).total_seconds() / 86400
    except ValueError:
        say(lines, "account id is not an ObjectId; no age from it")
    overview = {}
    try:
        overview = get("https://huggingface.co/api/users/%s/overview" % name, auth=False)
        c = overview.get("createdAt")
        if c:
            t = dt.datetime.fromisoformat(c.replace("Z", "+00:00"))
            ages["overview_createdAt"] = (now - t).total_seconds() / 86400
        else:
            say(lines, "overview has no createdAt; its fields: " + ", ".join(sorted(overview)))
    except Exception as e:
        say(lines, "overview not read: %s" % type(e).__name__)
    facts["num_spaces_overview"] = overview.get("numSpaces")
    zero, hw_counts = 0, {}
    try:
        spaces = get("https://huggingface.co/api/spaces?author=%s&limit=100" % name)
        for s in spaces:
            try:
                rt = get("https://huggingface.co/api/spaces/%s/runtime" % s["id"])
                hw = (rt.get("hardware") or {}).get("current") or (rt.get("hardware") or {}).get("requested") or "none"
            except Exception:
                hw = "unread"
            hw_counts[hw] = hw_counts.get(hw, 0) + 1
            if str(hw).startswith("zero"):
                zero += 1
        facts["spaces_listed"] = len(spaces)
        facts["spaces_by_hardware"] = hw_counts
        facts["zero_gpu_spaces"] = zero
    except Exception as e:
        say(lines, "spaces not listed: %s" % type(e).__name__)
    days = min(ages.values()) if ages else None
    eligible = days is not None and days > 30
    for k, v in ages.items():
        say(lines, "account age by %s: %.1f days" % (k, v))
    say(lines, "account older than 30 days: %s" % ("yes" if eligible else ("no" if days is not None else "unknown")))
    for k, v in facts.items():
        say(lines, "%s: %s" % (k, v))
    res = {"older_than_30_days": eligible, "age_days": None if days is None else round(days, 1),
           "ages": {k: round(v, 1) for k, v in ages.items()}, **facts, "checked_at": now.isoformat(timespec="seconds")}
    with open(os.path.join(OUT, "account.json"), "w") as f:
        json.dump(res, f, indent=1)
    gho = os.environ.get("GITHUB_OUTPUT")
    if gho:
        with open(gho, "a") as f:
            f.write("eligible=%s\ndays=%s\n" % ("yes" if eligible else "no", "" if days is None else int(days)))


if __name__ == "__main__":
    main()
