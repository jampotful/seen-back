#!/usr/bin/env python3
"""Offline tests of the spec compiler's checks (tools/views/compile.py). No key and no table needed: python3 -I tools/views/test_compile.py"""
import copy, importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("compile_mod", os.path.join(HERE, "compile.py"))
C = importlib.util.module_from_spec(spec)
sys.modules["compile_mod"] = C
spec.loader.exec_module(C)

specs = C.all_specs()
F = C.schema_facts(specs)
fails = []


def ok(cond, what):
    print(("ok   " if cond else "FAIL ") + what)
    if not cond:
        fails.append(what)


ok("fov" in F["params"] and "cpd" in F["params"] and "gate" in F["params"], "schema: parameters are read from cam.a.js (%d)" % len(F["params"]))
ok("field" in F["draw"] and "wedge" in F["draw"]["field"], "schema: draw options include the field modes")
ok("strip" in F["shapes"] and "cpd" in F["zone_keys"], "schema: zone shapes and keys")
ok("spectrum" in F["blocks"] and "haptic" in F["blocks"], "schema: the blocks the viewer resolves")
ok("Rules of the format" in C.format_text(), "format text is section 3 of the design")
ok(len(C.system_text(F)) > 5000, "system part is built")

job = {"key": "testview", "chip": "Test", "who": "a test animal", "applies_to": {"family": ["Salticidae"]}, "like": "spider"}
rec = lambda i, **k: dict({"_id": "R%d" % i, "_file": "t.jsonl", "_inside": True, "taxon": "Menemerus", "trait": "fov_h_deg", "value": 350, "grade": "m",
                          "quote": "The visual field of the animal extends 350 degrees.", "source": {"authors": "Smith J", "year": 2020}}, **k)
records = {"R1": rec(1), "R2": rec(2, value=330, quote="A second measurement gave 330 degrees."),
           "R3": rec(3, trait="acuity_cpd", value=2.0, quote="Acuity was 2.0 cycles per degree."),
           "R4": rec(4, trait="acuity_cpd", value=1.0, grade="g", _inside=False, taxon="Lycosa", quote="Wolf spiders reach 1.0 cycles per degree.")}


def P(value, grade, invented, src, **kw):
    return dict({"value": value, "grade": grade, "invented": invented, "src": src}, **kw)


good = {
    "spec": {"key": "testview", "chip": "Test", "who": "a test animal", "cue": "Things that move glow.", "modules": [], "falls_back_to": "spider",
             "params": {"fov": P(350, "m", False, ["R1"]), "cpd": P(1.5, "g", False, ["R3", "R4"]), "glow": P(0.9, "i", True, [])},
             "matrices": {}, "draw": {},
             "rows": [["m", "Wide eyes", "The side eyes cover almost all the way round.", ["R1"], ["params.fov"]],
                      ["i", "Glow", "How brightly movement glows is the app's choice.", [], ["params.glow"]]]},
    "claims": [{"path": "params.fov", "records": ["R1"], "kind": "value", "how": "R1's value"},
               {"path": "params.cpd", "records": ["R3", "R4"], "kind": "range_middle", "how": "between R4 (1.0) and R3 (2.0)"}],
    "quotes": [{"record": "R1", "quote": "extends 350 degrees"}, {"record": "R3", "quote": "Acuity was 2.0 cycles per degree"},
               {"record": "R4", "quote": "reach 1.0 cycles per degree"}],
}


def run(reply):
    r = C.check_reply(job, F, records, copy.deepcopy(reply), specs["spider"], {})
    return r[0], r[1]


e, w = run(good)
ok(not e, "a faithful reply passes (%s)" % e)

bad = copy.deepcopy(good); bad["spec"]["params"]["fov"]["value"] = 360
e, _ = run(bad)
ok(any("fov" in x and "not a cited record's value" in x for x in e), "an m value no record states is refused")

bad = copy.deepcopy(good); bad["spec"]["params"]["cpd"]["grade"] = "m"; bad["spec"]["params"]["cpd"]["value"] = 1.0; bad["spec"]["params"]["cpd"]["src"] = ["R4"]; bad["claims"][1]["records"] = ["R4"]
e, _ = run(bad)
ok(any("graded m, and no cited record is graded m" in x for x in e), "m on a wider taxon's record is refused")

bad = copy.deepcopy(good); bad["quotes"][0]["quote"] = "extends 351 degrees"
e, _ = run(bad)
ok(any("not in that record's quote" in x for x in e), "a quote the record does not hold is refused")

bad = copy.deepcopy(good); bad["spec"]["params"]["fov"]["src"] = ["R99"]
e, _ = run(bad)
ok(any("R99" in x for x in e), "a record id that was not sent is refused")

bad = copy.deepcopy(good); bad["claims"] = bad["claims"][1:]
e, _ = run(bad)
ok(any("graded m with no claim" in x for x in e), "m without a claim is refused")

bad = copy.deepcopy(good); bad["spec"]["params"]["glow"]["invented"] = False
e, _ = run(bad)
ok(any("invented" in x for x in e), "an i parameter that is not marked invented is refused")

bad = copy.deepcopy(good); bad["spec"]["rows"][0][2] = "It is wide — very wide, not narrow but broad."
e, _ = run(bad)
ok(any("em dash" in x for x in e) and any("not X but Y" in x for x in e), "an em dash and a not-but sentence are refused")

bad = copy.deepcopy(good); bad["spec"]["rows"][0][2] = "The colour of it is set by params.fov."
e, _ = run(bad)
ok(any("British spelling" in x for x in e) and any("code name" in x for x in e), "British spelling and code names are refused (rows are in US English)")
bad = copy.deepcopy(good); bad["spec"]["rows"][0][2] = "You see more color than most people do."
e, _ = run(bad)
ok(any("humans" in x for x in e) and not any("spelling" in x for x in e), "rows say humans, never people (VOICE.md rule 2)")

bad = copy.deepcopy(good); bad["spec"]["rows"][0][3] = ["R4"]
e, _ = run(bad)
ok(any("cites no record graded m" in x for x in e), "an m row that cites no m record is refused")

bad = copy.deepcopy(good); bad["spec"]["params"]["fov"]["value"] = 500
e, _ = run(bad)
ok(any("outside" in x for x in e), "a value outside the schema range is refused")

bad = copy.deepcopy(good); bad["spec"]["params"]["bogus"] = P(1, "i", True, [])
e, _ = run(bad)
ok(any("bogus" in x for x in e), "a parameter the engine does not read is refused")

bad = copy.deepcopy(good); bad["spec"]["draw"] = {"field": [{"name": "wedge", "invented": False}, {"name": "nonsense"}]}
e, _ = run(bad)
ok(any("nonsense" in x for x in e), "a draw option the engine does not know is refused")

bad = copy.deepcopy(good); bad["claims"][0]["kind"] = "calculation"
e, _ = run(bad)
ok(any("calculation" in x for x in e), "a calculated value cannot be m")

out = C.rewrite_ids(copy.deepcopy(good["spec"]), records)
ok(out["params"]["fov"]["src"] == ["t.jsonl:Smith 2020"] and out["draft"] is True, "record ids are rewritten to file and source")

ok(C.value_supported(1.5, [records["R3"], records["R4"]]) is True and C.value_supported(9, [records["R3"], records["R4"]]) is False, "value_supported brackets")
# a reply whose spec string runs on into the claims is read; unnamed invented parameters get one plain row
run_on = {"spec": json.dumps(good["spec"]) + ', "claims": ' + json.dumps(good["claims"]), "claims": [], "quotes": good["quotes"]}
n = C.normalize_reply(run_on)
ok(isinstance(n["spec"], dict) and len(n["claims"]) == 2, "a spec string that runs on into the claims is read")
bad = copy.deepcopy(good); bad["spec"]["params"]["dof"] = P(0.2, "i", True, []); bad["spec"]["rows"][1][4] = ["params.glow"]
e, w = run(bad)
ok(not e and any("Settings the app chose" in x for x in w), "an invented parameter no row names gets the catch-all row (%s)" % (e or w))

records["R5"] = rec(5, trait="lambda_max_nm", value=344, quote="UV receptor peaks at 344 nm.")
bad = copy.deepcopy(good)
bad["spec"]["matrices"] = {"X": {"from_pigments": [344, 440], "grade": "m", "invented": True, "src": ["R5"]}}
e, _ = run(bad)
ok(any("peak 440" in x and "344 nm (R5)" in x for x in e) and not any("peak 344" in x for x in e), "a pigment peak no record gives is refused and the available peaks are listed")
bad["spec"]["matrices"]["X"]["from_pigments"] = [344]
out = C.rewrite_ids(copy.deepcopy(bad["spec"]), records); C.PG.fill(out["matrices"])
ok(len(out["matrices"]["X"]["rows"]) == 3, "rows are computed for a matrix given by pigment peaks")

pairq = {"value": "sweeps of 2 degrees", "quote": "sweeps with an amplitude of 2 degrees and a period of 1.2 s"}
ok(C.value_supported([2, 1.2], [pairq]) is True and C.value_supported([3, 1.2], [pairq]) is False, "numbers written in a record's quote support a pair worked from one sentence")

# the glossary (views/PARAMS.md)
G = C.read_glossary()
whole, zone = G.get("Whole-picture settings", {}), G.get("Zone keys", {})
missing = [n for n in F["params"] if n not in whole]
ok(not missing, "glossary: every whole-picture setting the engine reads has an entry (missing: %s)" % ", ".join(missing))
missing = [k for k in F["zone_keys"] if "zones." + k not in zone]
ok(not missing, "glossary: every zone key has an entry (missing: %s)" % ", ".join(missing))
ok("zones.cpd" in zone and "eye" in zone["zones.cpd"] and "gaze.saccade" in G.get("Gaze keys", {}), "glossary: zone and gaze entries are read")
gt = C.glossary_text(G)
ok("THE GLOSSARY" in gt and "- cpd:" in gt and "\u2014" not in gt, "glossary: the text sent has the entries and no em dash")
ut = C.user_text({"key": "t", "who": "a test animal"}, "spider", specs["spider"], [], G)
ok(ut.index("THE GLOSSARY") < ut.index("THE NEAREST EXISTING SPEC"), "glossary: sent with each view's request, before the example")

# sharpness: units, direction and which eye (burst 9)
S = lambda **k: rec(0, trait="acuity_cpd", **k)
ok(C.as_cpd(S(value=42, units="arcmin (minimum separable angle)"))[0] == [0.714], "as_cpd: minutes of arc are inverted (30 / angle)")
ok(C.as_cpd(S(value=0.13, units="degrees"))[0] == [3.846], "as_cpd: degrees are inverted with the factor 2")
ok(C.as_cpd(rec(0, trait="interommatidial_deg", value=1.9, units="deg"))[0] == [0.263], "as_cpd: an interommatidial angle is converted")
ok(C.as_cpd(S(value=3.6, units="cycles/radian"))[0] == [0.063], "as_cpd: cycles per radian are divided by 57.3")
ok(C.as_cpd(S(value="20/249", units="Snellen fraction"))[0] == [2.41], "as_cpd: Snellen 20/x is 600 / x")
ok(C.as_cpd(S(value=1.5, units="decimal acuity (source's unit, not cycles/degree)"))[0] == [45.0], "as_cpd: decimal acuity is 30 x value")
ok(C.as_cpd(S(value=25, units="percent higher spatial resolution than honeybees"))[0] is None, "as_cpd: a percentage is unreadable")
ok(C.as_cpd(S(value=0.26, units="cycles/degree")) == ([0.26], ""), "as_cpd: cycles per degree pass as they are")
ok(C.as_cpd(S(value="anterior lateral eyes 0.3 to 1.3 cycles/degree", units=""))[0] == [0.3, 1.3], "as_cpd: figures written in a value of words count")
ok(C.as_cpd(S(value=5, units=""))[0] is None and C.as_cpd(S(value=5, units="", quote="about 5 cycles per degree"))[0] == [5], "as_cpd: no units counts only when the quote says cycles per degree")

records["R6"] = rec(6, trait="acuity_cpd", value=42, units="arcmin (minimum separable angle)", quote="The minimum separable angle was 42 arcmin.")
records["R7"] = rec(7, trait="acuity_cpd", value=12.4, units="cycles/degree", eye="AME", quote="The principal eyes resolve 12.4 cycles per degree.")
records["R8"] = rec(8, trait="interommatidial_deg", value=0.5, units="degrees", quote="Neighboring receptors lie 0.5 degrees apart.")
records["R9"] = rec(9, trait="fov_h_deg", value=150, eye="monocular", quote="Each eye sees 150 degrees.")
records["R10"] = rec(10, trait="acuity_cpd", value=25, units="percent higher than honeybees", quote="25 percent higher resolution")


def with_cpd(value, grade, src, kind="value", invented=False, zone=False):
    r = copy.deepcopy(good)
    r["spec"]["params"]["cpd"] = P(value, grade, invented, src)
    r["claims"][1] = {"path": "params.cpd", "records": src, "kind": kind, "how": "test"}
    r["quotes"] += [{"record": i, "quote": records[i]["quote"]} for i in src]
    if invented:
        r["spec"]["rows"][1][4] = ["params.glow", "params.cpd"]; r["spec"]["rows"][1][0] = "g"
    return r


e, _ = run(with_cpd(42, "m", ["R6"]))
ok(any("raw figure of R6" in x and "smaller angle is sharper" in x for x in e), "units: an angle read as cycles per degree is caught (%s)" % e[:1])
e, _ = run(with_cpd(0.714, "m", ["R6"]))
ok(any("only after a conversion" in x for x in e), "units: a converted figure graded m as a value is caught")
e, _ = run(with_cpd(0.714, "g", ["R6"], kind="calculation", invented=True))
ok(not e, "units: a converted figure as a calculation, g and invented, passes (%s)" % e)
e, _ = run(with_cpd(2.0, "g", ["R8"], kind="calculation", invented=True))
ok(any("1 / (2 x angle)" in x for x in e), "direction: an angle inverted without the factor 2 is caught (%s)" % e[:1])
e, _ = run(with_cpd(12.4, "m", ["R7"]))
ok(any("small pair of eyes" in x and "zone" in x for x in e), "which eye: the principal eyes' acuity in params.cpd is caught")
z = with_cpd(2.0, "m", ["R3"]); z["spec"]["zones"] = [{"id": "front", "shape": "strip", "cpd": P(12.4, "m", False, ["R7"])}]
z["claims"].append({"path": "zones[0].cpd", "records": ["R7"], "kind": "value", "how": "R7"}); z["quotes"].append({"record": "R7", "quote": records["R7"]["quote"]})
e, _ = run(z)
ok(not any("cpd" in x for x in e), "which eye: the same figure in a zone passes (%s)" % [x for x in e if "cpd" in x][:1])
e, _ = run(with_cpd(25, "m", ["R10"]))
ok(any("cannot be read as cycles per degree" in x or "comparison" in x for x in e), "units: a percentage supports no sharpness (%s)" % e[:1])
f = copy.deepcopy(good); f["spec"]["params"]["fov"] = P(150, "m", False, ["R9"]); f["claims"][0]["records"] = ["R9"]; f["quotes"].append({"record": "R9", "quote": "Each eye sees 150 degrees."})
e, _ = run(f)
ok(any("one eye's field" in x for x in e), "field of view: one eye's field as the whole field is caught")
ok(not C.SMALL_EYE.search("parvocellular LGN neurons, parafovea") and C.SMALL_EYE.search("median ocellus") and C.SMALL_EYE.search("AME"), "which eye: ocelli and principal eyes are named, parvocellular is not")
ok("1 / (2 x the angle in degrees)" in C.system_text(F) and "US spelling" in C.system_text(F), "prompt: the sharpness rules and US spelling are sent")
ok(any(x.startswith("as_cpd") or '"as_cpd":0.714' in C.record_line(dict(records["R6"], _audit="t")) for x in ["as_cpd"]), "record line: carries as_cpd")

print("%d failed" % len(fails))
sys.exit(1 if fails else 0)
