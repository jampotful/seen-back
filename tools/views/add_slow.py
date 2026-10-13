#!/usr/bin/env python3
"""Adds module 12 (slow) to the fungus spec and the slime mould spec (burst 4). Usage: python3 -I tools/views/add_slow.py"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
SHEET = "docs/views/sheets/%s.md#4"


def P(v, rng, note, src=None, grade="i"):
    return {"value": v, "grade": grade, "invented": True, "src": src or [], "range": rng, "floor": None, "note": note}


def slow_block(sheet):
    return {
        "everyMs": P(3000, [500, 20000], "one frame kept every few seconds, as the sheet proposes", [sheet]),
        "windowS": P(600, [30, 3600], "the store forgets over ten minutes, as the sheet proposes", [sheet]),
        "rightS": P(20, [2, 120], "time constant of the slow righting: a stem's 3 to 4 hours sped up about 600 times; the factor is the app's", [sheet]),
        "stillS": P(8, [2, 60], "seconds left alone before the patient view starts to develop"),
        "developS": P(30, [5, 300], "seconds for the patient view's print to come up fully"),
        "moveK": P(0.03, [0.005, 0.2], "how much the picture may change between light reads and still count as left alone"),
    }


DRAW = [
    {"name": "hour", "invented": True, "note": "the hour in a minute: one frame every few seconds, averaged over ten minutes, so only what stays remains (atlas 24)"},
    {"name": "patient", "invented": True, "note": "the patient view: nothing develops while the person watches; set the phone down and the picture comes up like a print in a tray (atlas 24)"},
    {"name": "righting", "invented": True, "note": "the slow righting: tilt the phone and the picture turns slowly back to true vertical (atlas 24); needs &sense=motion"},
    {"name": "off", "invented": True, "note": "the view as it was before module 12"},
]


def rows(who, sheet):
    return [
        ["i", "Being tried: the hour in a minute", "This trial keeps one picture every three seconds and averages them over ten minutes, so anything that moves fades and what stays remains. %s answers light over minutes to hours. The pace and the window are the app's." % who,
         [sheet, "param:slow.everyMs", "param:slow.windowS"]],
        ["i", "Being tried: the patient view", "With &draw=patient the picture refuses to change while you watch. Set the phone down and leave it, and the picture comes up slowly, like a print in a tray. The waiting times are the app's.",
         [sheet, "param:slow.stillS", "param:slow.developS", "param:slow.moveK"]],
    ]


def add(key, who, righting, sheet_key=None):
    p = root / "views" / (key + ".json")
    s = json.loads(p.read_text(encoding="utf-8"))
    sheet = SHEET % (sheet_key or key)
    s["slow"] = slow_block(sheet)
    if not righting:
        del s["slow"]["rightS"]
    s["draw"] = dict(s.get("draw") or {}, slow=[d for d in DRAW if righting or d["name"] != "righting"])
    if "slow" not in s["modules"]:
        s["modules"].append("slow")
    s["inputs"] = dict(s.get("inputs") or {}, motion="optional" if righting else s.get("inputs", {}).get("motion", "none"))
    if righting:
        s["inputs"]["senses"] = {"motion": 1}
    s["rows"] = [r for r in s["rows"] if not r[1].startswith("Being tried: the")]
    s["rows"] += rows(who, sheet)
    if righting:
        s["rows"].append(["g", "Being tried: which way is down", "A mushroom stem tilted on its side turns upright again over three to four hours, and the gills come to hang straight down. With &draw=righting and the motion sensors on, tilt the phone and the picture turns slowly back to true vertical, about 600 times faster than a stem.",
                          [sheet, "param:slow.rightS"]])
    s["notes"] = [n for n in s.get("notes", []) if n.get("need") not in ("slow", "motion")]
    p.write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


add("fungus", "A fungus", True)
add("slime", "A slime mould", False, "fungus")
