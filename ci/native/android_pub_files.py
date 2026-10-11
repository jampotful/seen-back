"""Write built.json and README.md beside seen-back-debug.apk for the branch pub/app-android.

Usage: python3 -I ci/native/android_pub_files.py <dir holding seen-back-debug.apk> <out/android/gate.json> <src/cam.a.js>
The page's build number is read from `var BUILD = '<n>'` in src/cam.a.js; the commit and run come from GitHub's variables.
"""
import datetime
import hashlib
import json
import os
import re
import sys

d, gate_path, cam_a = sys.argv[1:4]
apk = os.path.join(d, "seen-back-debug.apk")
m = re.search(r"var BUILD = '([^']+)'", open(cam_a, encoding="utf-8").read())
if not m:
    sys.exit("no BUILD in " + cam_a)
build = m.group(1)
h = hashlib.sha256()
with open(apk, "rb") as f:
    for b in iter(lambda: f.read(1 << 20), b""):
        h.update(b)
size = os.path.getsize(apk)
commit = os.environ.get("GITHUB_SHA", "")
gate = json.load(open(gate_path))
st = gate.get("selftest") or {}
now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
repo = "jampotful/seen-back"
raw = "https://raw.githubusercontent.com/%s/pub/app-android/seen-back-debug.apk" % repo
built = {
    "file": "seen-back-debug.apk",
    "bytes": size,
    "sha256": h.hexdigest(),
    "commit": commit,
    "page_build": build,
    "built_at": now,
    "workflow_run": os.environ.get("GITHUB_RUN_NUMBER", ""),
    "ref": os.environ.get("GITHUB_REF_NAME", ""),
    "signed_with": "a debug key made by Gradle on the build machine for this build and not kept",
    "emulator": {"selftest_checks": st.get("checks"), "selftest_ok": st.get("ok"),
                 "published_file_opened": (gate.get("published_open") or {}).get("screen"),
                 "published_file_begin": (gate.get("published_begin") or {}).get("src")},
}
json.dump(built, open(os.path.join(d, "built.json"), "w"), indent=1)

readme = """# Seen Back for Android: a debug build

`seen-back-debug.apk` is the Seen Back page of build {build} inside a plain Android WebView. The page's files are packed in the app, and the app serves them to its WebView from inside itself. It was built on a GitHub build machine from commit `{commit}` of https://github.com/{repo} and signed there with a debug key that Gradle made for this one build. The key was thrown away with the machine, and it is in no repository.

The file is for trying the page on one's own phone. It is a debug build and has not been through Google Play or any other store.

| | |
|---|---|
| File | `seen-back-debug.apk`, {size:,} bytes |
| SHA-256 | `{sha}` |
| Page | build {build} |
| Commit | `{commit}` |
| Built | {now} (workflow run {run}) |
| Needs | Android 7.0 or later, and the camera |

## Before it was published

The same build, with the page's check files added, ran in an Android 14 emulator on the build machine: the page's self-test finished with {checks} checks and {nfail} failed. Then this file, without the check files, was installed in the same emulator, opened at its first screen and reached the camera after Begin. Apart from their signature files, the two APKs differ only in the check files; the comparison, the self-test's report and the screenshots are on the repository's `ci` branch under `runs/native/{run}-pub/android/`. Nothing here has run on a real phone.

## How to install it

1. On the phone, open this address in the browser: {raw}
2. The browser downloads the file. It may warn that this kind of file can harm the device; choose to download it anyway.
3. Open the downloaded file. Android asks whether the browser may install unknown apps. Turn that on for the browser in the setting it shows, go back and press Install.
4. Google Play Protect is likely to warn that it does not recognize the app's developer, because a debug key belongs to no developer it knows, and it may offer to scan the app first. Its dialog has a way to install the app anyway, sometimes under "More details".
5. Open Seen Back. The first time you press Begin, Android asks for the camera.

The larger model (309,812,341 bytes) is not in the file. As on the web, the page offers to fetch it and then keeps it in the app's own storage.

## Updates

The app does not update itself. A newer build appears at the same address, signed with a different throwaway key, so Android will refuse to install it over this one: uninstall Seen Back first (the kept larger model goes with it), then install the new file.

To check a downloaded file on a computer, compare the output of `sha256sum seen-back-debug.apk` with the SHA-256 above, or with `built.json` beside it.
""".format(build=build, commit=commit, repo=repo, size=size, sha=h.hexdigest(), now=now,
           run=os.environ.get("GITHUB_RUN_NUMBER", "?"), checks=st.get("checks"), nfail=len(st.get("fails") or []), raw=raw)
open(os.path.join(d, "README.md"), "w", encoding="utf-8").write(readme)
print("wrote built.json and README.md: build %s, %d bytes, sha256 %s" % (build, size, h.hexdigest()))
