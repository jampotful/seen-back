#!/usr/bin/env python3
"""Build Seen Back from its parts. Usage: python3 -I build.py

  index.html                     the app as a standalone page; this is what the web address serves
  sw.js                          the service worker, stamped with this build, so the app opens with no signal
  dist/seen-back.artifact.html   the same page in the shape Claude's artifact publisher wants
  selftest.js                    the self-test, fetched by the page only when its address has ?selftest=1

The parts live in src/. Nothing here needs a network.
"""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent
src = root / "src"
PARTS = ("cam.a.js", "cam.g60.js", "cam.b.js", "cam.c1.js", "cam.r.js", "cam.rec.js", "cam.c2.js")
# The self-test (src/cam.selftest.js) is not part of the page's script. It becomes selftest.js, which the page fetches only for
# ?selftest=1, through a small hook that hands it the page's bindings it reads. Every one of them is set once at start-up and never
# reassigned, so handing over their values is the same as reading them in place. A binding missing here fails the self-test at once.
SELFTEST_READS = ("$", "BUILD", "EYES", "Engine", "HUMAN", "HUMAN_CPD", "ORDER", "S", "calm", "canvas", "clamp", "coarse", "decode",
                  "engine", "fxNow", "go", "hasCamera", "lerp", "makeCanvas", "mix", "paramsOf", "pocket", "setEyes", "showStill", "vid")

head = (src / "cam.head.html").read_text(encoding="utf-8")
js = "".join((src / n).read_text(encoding="utf-8") for n in PARTS)
js += ("  // ---------- self-test hook: with ?selftest=1 the page fetches selftest.js and hands it the bindings it reads (build.py)\n"
       "  if (/[?&]selftest=1(?:&|$)/.test(location.search || '')) {\n"
       "    S.selftest = true;   // at once, as the self-test did when it was part of this script: the page's loop leaves the drawing to it\n"
       "    window.__seenBackSelftest = { " + ", ".join("'%s': %s" % (n, n) for n in SELFTEST_READS) + " };\n"
       "    var selftestScript = document.createElement('script'); selftestScript.src = 'selftest.js?v=' + encodeURIComponent(BUILD);\n"
       "    document.head.appendChild(selftestScript);\n"
       "  }\n")
build = re.search(r"var BUILD = '([^']+)'", js).group(1)
script = "\n<script>\n(function () {\n" + js + "})();\n</script>\n"

# ---- 1. the artifact form: no doctype or head; the typeface comes from Google Fonts, the one font host that viewer allows
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "seen-back.artifact.html").write_text(head + script, encoding="utf-8")
(root / "dist" / "app.js").write_text("(function () {\n" + js + "})();\n", encoding="utf-8")   # for a syntax check

# ---- 2. the standalone form: a real document, the typeface served from this site, and the pieces that make it installable
GOOGLE = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap">'
assert GOOGLE in head
FACES = "<style>\n" + "\n".join(
    '@font-face{font-family:"Instrument Serif";font-style:%s;font-weight:400;font-display:swap;'
    'src:url(fonts/instrument-serif-%s-400-%s.woff2) format("woff2");unicode-range:%s}' % (style, subset, style, rng)
    for style in ("normal", "italic")
    for subset, rng in (("latin-ext", "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"),
                        ("latin", "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"))
) + "\n</style>"
site_head = head.replace(GOOGLE, FACES)
cut = site_head.index('<div id="app"')
head_part, body_part = site_head[:cut], site_head[cut:]
RESET = (":root{color-scheme:light;padding:env(safe-area-inset-top,0px) 0 env(safe-area-inset-bottom,0px)}"
         "body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}")
INSTALL = (
    '<meta name="description" content="Photograph something alive, and your camera takes on its way of seeing.">\n'
    '<link rel="manifest" href="manifest.webmanifest">\n'
    '<meta name="mobile-web-app-capable" content="yes">\n'
    '<meta name="apple-mobile-web-app-capable" content="yes">\n'
    '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n'
    '<meta name="apple-mobile-web-app-title" content="Regards">\n'
    '<link rel="apple-touch-icon" href="icons/icon-180.png">\n'
    '<link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">\n'
)
WORKER = ("<script>\nif ('serviceWorker' in navigator && (location.protocol === 'https:' || /^(localhost|127\\.0\\.0\\.1)$/.test(location.hostname)) && !/[?&]nosw=1/.test(location.search)) {\n"
          "  window.addEventListener('load', function () { navigator.serviceWorker.register('sw.js').catch(function () {}); });\n}\n</script>\n")
standalone = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<meta name=\"theme-color\" content=\"#000000\">\n" + INSTALL +
    "<style>" + RESET + "</style>\n" + head_part + "</head>\n<body>\n" + body_part + script + WORKER + "</body>\n</html>\n"
)
(root / "index.html").write_text(standalone, encoding="utf-8")

# ---- 3. the self-test, fetched on demand
selftest = ("// Seen Back self-test, build " + build + ": fetched by the page only for ?selftest=1. Made by build.py from src/cam.selftest.js.\n"
            "(function (I) {\n  if (!I) return;\n  var " + ", ".join("%s = I['%s']" % (n, n) for n in SELFTEST_READS) + ";\n"
            + (src / "cam.selftest.js").read_text(encoding="utf-8") + "})(window.__seenBackSelftest);\n")
(root / "selftest.js").write_text(selftest, encoding="utf-8")

# ---- 4. the service worker, stamped
sw = (src / "sw.template.js").read_text(encoding="utf-8").replace("__BUILD__", build)
(root / "sw.js").write_text(sw, encoding="utf-8")

print("build", build, "| index.html", len(standalone), "bytes | artifact", len(head + script), "bytes | selftest.js", len(selftest), "bytes")
