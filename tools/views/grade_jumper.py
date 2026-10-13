#!/usr/bin/env python3
"""Grades every parameter of views/jumper.json from the parameter table in docs/views/drafts/jumper.md (sections 1a to 1d and 2)
and the figures in docs/ENGINE.md. Log lines (L38 and so on) are lines of docs/views/evidence/jumper.jsonl on research/jumper.
Usage: python3 -I tools/views/grade_jumper.py   (rewrites views/jumper.json in place; the values themselves are left unchanged)
"""
import json, pathlib, subprocess

root = pathlib.Path(__file__).resolve().parents[2]
p = root / "views" / "jumper.json"
s = json.loads(p.read_text(encoding="utf-8"))
T = "drafts/jumper.md "
# path: (grade, invented, sources, range, note)
G = {
    "params.fov": ("m", False, [T + "1a whole animal", "log L41, L87"], [180, 360], "the side eyes cover about 360 degrees; 350 is where the squeeze stops"),
    "params.cpd": ("m", False, [T + "1a PLE sharpness", "log L37, L193"], [0.1, 4], "rear side eyes, Land 1969"),
    "params.glow": ("i", True, [T + "1a ALE and PLE", "log L56 (Land 1971: the side eyes answer only to movement)"], [0, 2], "how brightly movement glows is the app's choice"),
    "params.living": ("i", True, [], [0, 3], "no extra weight for living movement outside the front side eyes"),
    "params.glowC": ("i", True, [], [0, 1], "the glow's colour"),
    "zones.front.deg": ("g", False, [T + "1a ALE field", "log L100, L116, L115, L5"], [40, 180], "both front side eyes, Phidippus audax"),
    "zones.front.soft": ("i", True, [], [0, 0.5], None),
    "zones.front.cpd": ("m", False, [T + "1a ALE sharpness", "log L114, L36, L193"], [0.2, 4], "Phidippus"),
    "zones.front.living": ("i", True, [T + "1b looming and living motion", "log L113, L196, L1, L145, L147"], [0, 4], "the preference is measured; its weight is the app's"),
    "zones.gaze.deg": ("m", True, [T + "1b width and height", "log L38, L39"], [0.5, 40], "2 by 21 degrees measured; drawn 2.5 wide for the screen"),
    "zones.gaze.tilt": ("m", False, [T + "1a AME overlap", "log L57, L58", "Land 1969"], [0, 45], "the cross's arms"),
    "zones.gaze.gap": ("m", False, [T + "1a AME overlap", "log L57, L58"], [0, 5], None),
    "zones.gaze.tip": ("g", True, [T + "1a AME sharpness (the edge is coarser)", "Williams and McIntyre 1980"], [0, 1], None),
    "zones.gaze.soft": ("i", True, [], [0, 0.1], None),
    "zones.gaze.cpd": ("m", False, [T + "1a AME sharpness", "Land 1969; Harland and colleagues 2012"], [0.5, 15], "Phidippus 3.3 to 3.8"),
    "zones.gaze.uv": ("i", True, [T + "1a AME colour as drawn", "log L255, L256, L197"], [0, 2], "a phone records almost no ultraviolet; the guess is the app's"),
    "zones.gaze.uvR": ("i", True, [T + "1a AME colour as drawn"], [0, 1], None),
    "zones.gaze.glow": ("i", True, [], [0, 2], "no glow inside the strip"),
    "zones.gaze.living": ("i", True, [], [0, 4], None),
    "zones.gaze.mag": ("m", True, [T + "1d magnification", "log L26, L73"], [1, 2], "1.25 in Plexippus; using it as screen magnification is invented"),
    "zones.fovea.deg": ("i", True, [T + "1a Habronattus colour classes"], [1, 20], "the red-filtered patch's size is invented"),
    "zones.fovea.soft": ("i", True, [], [0, 0.1], None),
    "zones.fovea.cpd": ("m", False, [T + "1a AME sharpness"], [0.5, 15], None),
    "zones.fovea.uv": ("i", True, [T + "1a AME colour as drawn"], [0, 2], None),
    "zones.fovea.uvR": ("i", True, [T + "1a AME colour as drawn"], [0, 1], None),
    "zones.fovea.glow": ("i", True, [], [0, 2], None),
    "zones.fovea.living": ("i", True, [], [0, 4], None),
    "zones.fovea.mag": ("m", True, [T + "1d magnification", "log L26, L73"], [1, 2], None),
    "gaze.saccade": ("m", True, [T + "1b jump speed", "log L49"], [0, 200], "40 ms plus 4 ms a degree; faster than the measured 150 degrees a second floor"),
    "gaze.sweep": ("m", False, [T + "1c scanning sweeps", "log L50", "Land 1969"], [0, 10], "2 degrees, 1.2 s"),
    "gaze.twist": ("m", False, [T + "1c scanning rotation", "Land 1969"], [0, 8000], "25 degrees, 2 s to turn, 3.5 s at each end"),
    "gaze.examine": ("m", True, [T + "1c scanning bout", "log L52"], [500, 60000], "5 to 94 s measured; shortened to 4 to 12 s for the screen"),
    "gaze.hold": ("m", False, [T + "1c dwell after a jump", "log L55"], [0, 5000], "1 to 2 s"),
    "gaze.back": ("m", False, [T + "1c dwell after a jump", "log L55"], [0, 5], "a 10 degree return in 10 to 15 s"),
    "gaze.pursuit": ("m", False, [T + "1b smoothly following", "log L54, L111"], [0, 40], None),
    "gaze.ior": ("m", False, [T + "1c time a place is ignored", "log L7, L190", "Ferrante and colleagues 2024"], [0, 15000], "about 5 s"),
    "gaze.iorDeg": ("i", True, [], [1, 30], "the size of the ignored place"),
    "gaze.habit": ("m", True, [T + "1c habituation at one place", "Land 1971"], [0, 1], "the fact is measured; 0.75 is the app's"),
    "gaze.surround": ("m", True, [T + "1b what starts a jump", "Zurek and colleagues 2010"], [0, 1], "gratings start nothing; the weight is the app's"),
    "gaze.any": ("i", True, [], [0, 2], "the pull of any movement"),
    "gaze.living": ("i", True, [T + "1b looming and living motion"], [0, 4], "the pull of living movement"),
    "gaze.distract": ("m", True, [T + "1c fewer gaze shifts while examining", "log L184, L195, L196", "Bruce and colleagues 2021"], [1, 4], "the rise is invented"),
    "gaze.wander": ("m", True, [T + "1c idle sweeps", "log L53"], [1000, 60000], "spacing kept within the camera's picture"),
    "gaze.floor": ("i", True, [], [0, 0.5], "the faintest movement that calls the gaze"),
    "gaze.trackDeg": ("m", False, [T + "1b best speed", "log L96"], [1, 81], "strongest at 9 degrees a second"),
    "gaze.sleep.after": ("i", True, [], [500, 20000], None),
    "gaze.sleep.bout": ("m", True, [T + "1d sleep-like retinal bouts", "Roessler and colleagues 2022"], [1000, 120000], "a median 77 s measured; shortened for the screen"),
    "gaze.sleep.gap": ("m", True, [T + "1d sleep-like retinal bouts", "Roessler and colleagues 2022"], [5000, 1200000], "a median 17 min measured; shortened for the screen"),
    "by.genus.Portia.zones.gaze.cpd": ("m", False, [T + "1a AME sharpness", "Williams and McIntyre 1980"], [0.5, 15], "Portia fimbriata 12.4"),
    "by.genus.Portia.zones.gaze.deg": ("i", True, [], [0.5, 40], None),
    "by.genus.Portia.zones.fovea.cpd": ("m", False, [T + "1a AME sharpness", "Williams and McIntyre 1980"], [0.5, 15], None),
    "by.genus.Habronattus.zones.fovea.uvR": ("i", True, [], [0, 1], None),
}
MATS = {
    "SIDE_GREEN": ("m", True, [T + "1a ALE and PLE colour classes", "log L30, L78, L161"], "one green class, measured; the tint is the app's"),
    "UV_GREEN": ("g", True, [T + "1a AME colour as drawn", "research/methods receptor fits"], "two classes near 370 and 532 nm (Phidippus); the display mapping is the app's"),
    "UV_GREEN_RED": ("m", True, [T + "1a Habronattus colour classes", "log L104 to L108, L126, L155"], "three classes at the centre; the display mapping is the app's"),
}
seen = set()


def walk(x, path):
    if isinstance(x, dict):
        if "grade" in x and "value" in x:
            key = ".".join(path)
            if key in G:
                g, inv, src, rng, note = G[key]
                x.update(grade=g, invented=inv, src=src)
                v = x["value"]
                if rng and all(rng[0] <= n <= rng[1] for n in (v if isinstance(v, list) else [v])):
                    x["range"] = rng
                if note:
                    x["note"] = note
                seen.add(key)
            return
        for k, v in x.items():
            walk(v, path + [k])
    elif isinstance(x, list):
        for i, v in enumerate(x):
            walk(v, path + [v.get("id", str(i)) if isinstance(v, dict) else str(i)])


walk({"params": s["params"], "zones": s["zones"], "gaze": s["gaze"], "by": s.get("by", {})}, [])
for n, (g, inv, src, note) in MATS.items():
    if n in s["matrices"]:
        s["matrices"][n].update(grade=g, invented=inv, src=src, note=note)
missing = [k for k in G if k not in seen]
s["modules"] = ["zones", "light", "salience", "gaze"]
# Drawing options (docs/views/ATLAS.md entries 1, 5, 9 and 10), switched with &draw=<name>; the first of each list is the default.
# Every one is a way of drawing chosen by the app, so every one is invented.
s["draw"] = {
    "gaze": [{"name": "stamps", "invented": True, "note": "the hunting strip; each past fixation stays as a sharp thumbnail where it was taken and fades over gaze.ior"},
             {"name": "strip", "invented": True, "note": "the hunting strip alone"},
             {"name": "face", "invented": True, "note": "the front camera, so the person is the one looked at"}],
    "sharpness": [{"name": "paint", "invented": True, "note": "while a thumb is held on the picture the strip follows it; when it lifts the movement map leads again"}],
    "colour": [{"name": "two", "invented": True, "note": "the strip carries the principal eyes' two classes and the surround the side eyes' one; the classes are measured, the display mapping is the app's"},
               {"name": "palm", "invented": True, "note": "adds the guessed ultraviolet under the strip felt in the hand: vibration where the browser allows it (Android), a fine moving grain otherwise (iOS)"}],
    "surround": [{"name": "glow", "invented": True, "note": "the coarse green picture with movement glowing faintly"},
                 {"name": "pond", "invented": True, "note": "still things fade out of the surround, and only movement and the strip remain"}],
}
s["falls_back_to"] = "spider"
s["applies_to"] = {"family": ["Salticidae"]}
fmt = subprocess.run(["node", "-e", "const {fmt}=require(process.argv[1]);let d='';process.stdin.on('data',c=>d+=c).on('end',()=>process.stdout.write(fmt(JSON.parse(d))+'\\n'))",
                      str(root / "tools" / "views" / "fmt.js")], input=json.dumps(s, ensure_ascii=False), capture_output=True, text=True, check=True).stdout
p.write_text(fmt, encoding="utf-8")
print("graded", len(seen), "parameters;", "not found:", missing)
