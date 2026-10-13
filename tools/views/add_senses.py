#!/usr/bin/env python3
"""Burst 4: tilt and heading (module 5) and the long exposure (module 12) in the specs that use them.
Usage: python3 -I tools/views/add_senses.py. Run again safely: each block is replaced, rows are matched by title."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parents[2]


def P(v, rng, note, src=None, grade="i", invented=True):
    return {"value": v, "grade": grade, "invented": invented, "src": src or [], "range": rng, "floor": None, "note": note}


def load(k):
    return json.loads((root / "views" / (k + ".json")).read_text(encoding="utf-8"))


def save(k, s):
    (root / "views" / (k + ".json")).write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def put_rows(rows, new):
    titles = {r[1] for r in new}
    return [r for r in rows if r[1] not in titles] + new


def motion_input(t):
    t["inputs"] = dict(t.get("inputs") or {}, motion="optional")
    t["inputs"]["senses"] = dict((t["inputs"].get("senses") or {}), motion=1)


# Fish: Snell's window when the phone points up (atlas 2; fish.md section 4, item 1)
s = load("fish")
s["tilt"] = {"fromDeg": P(15, [0, 60], "the camera's elevation where the window begins to form"),
             "fullDeg": P(45, [20, 90], "the elevation where it is complete")}
s["draw"] = dict(s.get("draw") or {}, tilt=[{"name": "level", "invented": True, "note": "the view as it was"},
                                            {"name": "snell", "invented": True, "note": "point the phone up and the scene above is pressed into a disc about 97 degrees across, with a dark ring outside it (atlas 2)"}])
motion_input(s)
if "tilt" not in s["modules"]:
    s["modules"].append("tilt")
s["rows"] = put_rows(s["rows"], [["g", "Being tried: looking up", "Under water the whole sky above is pressed into a circle about 97 degrees across, because light bends as it enters the water. With &draw=snell and the motion sensors on, point the phone up to see it. A phone camera fills only the middle of that circle, and the dark ring outside it is the app's.",
                                  ["docs/views/sheets/fish.md#4", "Sabbah 2006", "param:tilt.fromDeg", "param:tilt.fullDeg"]]])
s["notes"] = [n for n in s.get("notes", []) if "Snell" not in json.dumps(n)]
save("fish", s)

# Salamander: the newt's compass (atlas 21; salamander.md section 4)
MAG_DRAW = [{"name": "none", "invented": True, "note": "the view as it was"},
            {"name": "tide", "invented": True, "note": "a faint darkening of the sky that follows the angle between the camera and magnetic north, fading in red or yellow light (atlas 21)"},
            {"name": "grain", "invented": True, "note": "a fine directional grain, like brushed metal, that runs along magnetic north whichever way the phone turns; red light melts it (atlas 21)"}]
s = load("salamander")
s["magnet"] = {"k": P(1, [0, 2], "how strongly the compass is drawn; nobody knows what the sense is like")}
s["draw"] = dict(s.get("draw") or {}, magnet=MAG_DRAW)
motion_input(s)
s["rows"] = put_rows(s["rows"], [["i", "Being tried: north", "With &draw=grain or &draw=tide and the motion sensors on, the picture carries a texture tied to magnetic north. The eastern newt's compass turns a quarter in light longer than about 500 nanometres, so warm light weakens the drawing. Nobody knows what this sense is like, and the drawing is the app's.",
                                  ["docs/views/sheets/salamander.md", "Phillips 2001", "param:magnet.k"]]])
save("salamander", s)

# Bird, as a trial: the songbird's compass, which fails in red or yellow light (birds draft, Wiltschko and colleagues 2021)
s = load("bird")
t = s["trial"]
t["magnet"] = {"k": P(1, [0, 2], "how strongly the compass is drawn; nobody knows what the sense is like")}
t["draw"] = dict(t.get("draw") or {}, magnet=MAG_DRAW)
t["rows"] = put_rows(t["rows"], [["i", "Being tried: north", "Many songbirds and pigeons sense the direction of the earth's magnetic field through their eyes, and the sense fails in red or yellow light. With &draw=grain or &draw=tide and the motion sensors on, the picture carries a texture tied to magnetic north that melts in warm light. The drawing is the app's.",
                                  ["research/birds draft: Wiltschko 2021", "param:magnet.k"]]])
save("bird", s)

# Cat and deer, as trials: the long exposure of a night eye (atlas 7)
for k, who in (("cat", "A cat"), ("deer", "A deer")):
    s = load(k)
    t = s["trial"]
    t["slow"] = {"windowS": P(3, [0.5, 20], "seconds of pooling in the dark; the pooling time is the app's (atlas 7)"),
                 "mix": {"curve": "lux", "points": [[-2, 1], [-0.6, 0]], "grade": "i", "invented": True, "src": [], "range": [0, 1],
                         "note": "how much of the pooled picture is shown, rising as the light falls"}}
    t["draw"] = dict(t.get("draw") or {}, slow=[{"name": "off", "invented": True, "note": "the view as it was"},
                                                {"name": "exposure", "invented": True, "note": "the long exposure: in the dark the view pools light over a few seconds, so still things sharpen and moving things leave ghosts (atlas 7)"}])
    t["rows"] = put_rows(t["rows"], [["i", "Being tried: a long exposure", "%s sees in dim light partly by pooling light over time. With &draw=exposure, in the dark the picture pools the last few seconds, so still things settle and moving things leave ghosts. The pooling time is the app's." % who,
                                      ["docs/views/ATLAS.md#7", "param:slow.windowS", "param:slow.mix"]]])
    save(k, s)
