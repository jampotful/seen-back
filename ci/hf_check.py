"""Say whether the Hugging Face token in HF_TOKEN is accepted and what it may do. Never prints the token or the account name."""
import json
import os
import urllib.request

req = urllib.request.Request(
    "https://huggingface.co/api/whoami-v2",
    headers={"Authorization": "Bearer " + os.environ["HF_TOKEN"].strip()},
)
try:
    with urllib.request.urlopen(req, timeout=25) as r:
        d = json.load(r)
except Exception as e:  # the reason, never the token
    print("hf token accepted: no (%s)" % type(e).__name__)
else:
    tok = (d.get("auth") or {}).get("accessToken") or {}
    print("hf token accepted: yes")
    print("hf token role:", tok.get("role"))
    fg = tok.get("fineGrained") or {}
    perms = set(fg.get("global") or [])
    for scope in fg.get("scoped") or []:
        perms.update(scope.get("permissions") or [])
    if perms:
        print("hf fine-grained permissions:", ", ".join(sorted(perms)))
    print("hf account kind:", d.get("type"))
    print("hf account is PRO:", d.get("isPro"))
    print("hf e-mail verified:", d.get("emailVerified"))
    print("hf whoami fields:", ", ".join(sorted(d.keys())))
