#!/usr/bin/env python3
"""python3 -I tools/views/test_rows.py : checks tools/views/rows.py with no API call: the request for each row, the draft checks, a run
against a stand-in for the API (a first draft that breaks the voice, then a good one), the output files and `apply`."""
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib.util  # noqa: E402

spec = importlib.util.spec_from_file_location("rows", os.path.join(HERE, "rows.py"))
rows = importlib.util.module_from_spec(spec)
sys.modules["rows"] = rows
spec.loader.exec_module(rows)

# ---- the number check
assert rows.supported(60, [58.0]) and rows.supported(200, [210.0]) and rows.supported(5, [4.9])
assert rows.supported(110, [108.0]) and not rows.supported(300, [108.0]) and not rows.supported(40, [108.0])
assert rows.numbers_of([1, 2.5, "about 12 and 3,400"], []) == [1.0, 2.5, 12.0, 3400.0]

# ---- the request for each row, from the real evidence
system, jobs, nrec = rows.prepare(rows.ROOT, ["cat", "spider"])
assert nrec > 10000 and "docs/views/VOICE.md" in system and "If you are a barn owl" in system
assert "cat__pupil" in jobs and "spider__eyes" in jobs and not any(k.startswith("cat__how") for k in jobs)
pupil = jobs["cat__pupil"]
assert pupil["row"]["grade"] == "m" and pupil["row"]["species"][0]["sci"] == "Felis catus"
assert "RECORDS you may cite" in pupil["user"] and "R1 |" in pupil["user"]
assert all(r["_id"] in pupil["ids"].values() for r in pupil["row"]["records"])
assert "colour" not in " ".join(k for k in jobs), list(jobs)

# ---- views behind ?try=: rows from try-rows.json, species from try-species.json, a row about one group, a row not sent
tsys, tjobs, _ = rows.prepare(rows.ROOT, ["mammal", "bigcat", "fungus"])
assert "mammal__elephants" in tjobs and "bigcat__pupil" in tjobs and not any("being-tried" in k or "guesses" in k for k in tjobs), list(tjobs)
ele = tjobs["mammal__elephants"]["row"]["species"]
assert ele and all(s["family"] == "Elephantidae" for s in ele), [s["sci"] for s in ele][:5]
assert len(tjobs["mammal__color"]["row"]["species"]) > len(ele)
assert tjobs["bigcat__lens"].get("skip") and not tjobs["bigcat__pupil"].get("skip")
assert rows.try_meta(rows.ROOT, "fungus", "No eyes")["live"] == "No picture" and rows.live_grade(rows.ROOT, "fungus", "No eyes") == "g"
assert rows.view_species(rows.ROOT, "owl", rows.GAPS.Tax())[0]["sci"] == "Bubo virginianus"


# ---- the draft checks
def good(job, text, cites=("R1",)):
    return rows.check_draft({"text": text, "cites": list(cites)}, job["row"], job["ids"])


assert good(pupil, "If you are a domestic cat, your pupil closes to an upright slit.") == []
errs = good(pupil, "A person sees a round pupil.")
assert any("humans" in e for e in errs), errs
assert any("not one of the records" in e for e in good(pupil, "Your pupil is a slit.", ("R99",)))
assert any("has no cited record" in e for e in good(pupil, "Your pupil shrinks 135 times.", ()))
assert any("is in none of the cited records" in e for e in good(pupil, "Your pupil shrinks 400 times.", ("R1",)))
assert any("phone" in e or "app" in e for e in good(pupil, "Your pupil is a slit. The phone draws it that way."))
assert any("no text" in e for e in rows.check_draft({"cites": []}, pupil["row"], pupil["ids"]))
assert good(pupil, "A human reads about 30 cycles a degree, and you very likely read less.") == []   # human constants need no record
low = [r for r in pupil["row"]["records"] if r.get("grade") != "m"]
if low:
    rid = [k for k, v in pupil["ids"].items() if v == low[0]["_id"]][0]
    assert any("graded m" in e for e in good(pupil, "Your pupil is a slit.", (rid,)))

# ---- a run against a stand-in for the API
calls = []


def fake_call(method, path, body=None, raw=False, tries=6):
    calls.append(len(body["messages"]))
    first = len(body["messages"]) == 1
    text = "A person sees well." if first and len(calls) % 2 == 1 else "If you are a domestic cat, you very likely have a slit. Nobody has measured more."
    return {"content": [{"type": "tool_use", "name": "submit_row", "input": {"text": text, "cites": ["R1"], "note": ""}}],
            "stop_reason": "tool_use", "usage": {"input_tokens": 100, "output_tokens": 20, "cache_read_input_tokens": 50}}


rows.EX.call = fake_call
rows.EX.set_model("claude-sonnet-5-5")
with tempfile.TemporaryDirectory() as d:
    class A:
        views, out, model, direct, max_usd, wait_min = "cat", d, "claude-sonnet-5-5", True, 5.0, 1
    assert rows.cmd_run(A) == 0
    draft = json.load(open(os.path.join(d, "cat.rows_draft.json")))
    stats = json.load(open(os.path.join(d, "stats.json")))
    assert draft["version"] == 1 and draft["model"] == "claude-sonnet-5-5"
    assert len(draft["rows"]) + len(draft["failed"]) == 7, (len(draft["rows"]), len(draft["failed"]))
    assert any(r["attempt"] == 2 for r in draft["rows"]) and any(r["attempt"] == 1 for r in draft["rows"])
    assert all("person" not in r["text"] for r in draft["rows"])
    assert stats["requests"] == 7 and stats["spent_usd"] > 0
    assert any(c == 3 for c in calls), calls                  # the retry carries the first draft and the errors

    # ---- apply writes rows_draft and nothing over the live rows
    tmp_root = os.path.join(d, "root")
    os.makedirs(os.path.join(tmp_root, "views"))
    src_spec = os.path.join(rows.ROOT, "views", "cat.json")
    shutil.copy(src_spec, os.path.join(tmp_root, "views", "cat.json"))
    before = json.load(open(src_spec))
    before.pop("rows_draft", None)                            # the repository's own copy may already hold a draft
    rows.ROOT = tmp_root

    class B:
        views, src = "cat", d
    assert rows.cmd_apply(B) == 0
    after = json.load(open(os.path.join(tmp_root, "views", "cat.json")))
    assert after["rows"] == before["rows"] and after.get("trial") == before.get("trial")
    assert after["rows_draft"]["rows"] and "failed" not in after["rows_draft"]
    assert after["rows_draft"]["rows"][0]["text"].startswith("A person") is False
    del after["rows_draft"]
    assert after == before
print("test_rows: ok")
