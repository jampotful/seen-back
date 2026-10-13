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

bad = copy.deepcopy(good); bad["spec"]["rows"][0][2] = "The color of it is set by params.fov."
e, _ = run(bad)
ok(any("American spelling" in x for x in e) and any("code name" in x for x in e), "American spelling and code names are refused")

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

print("%d failed" % len(fails))
sys.exit(1 if fails else 0)
