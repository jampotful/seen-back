#!/usr/bin/env python3
"""Tests for tools/lit/extract.py that need no API key: python3 -I tools/lit/test_extract.py"""
import json, os, sys, tempfile, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extract as E

TEXT = """Title of a paper

Citation line.

## Abstract
Eyes of the wolf spider Lycosa leuckartii were examined. The inter-receptor an-
gle of the AL eyes was 2.45° and of the AM eyes 1.85° in the central retina.

## Results
The field of view extended 360° around the animal.

## References
1. Somebody (1999). A title. J Thing.
"""


class T(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.d, "topic", "text"))
        with open(os.path.join(self.d, "topic", "text", "a.txt"), "w", encoding="utf-8") as fh:
            fh.write(TEXT)
        works = [
            {"doi": "10.1/aaa", "key": "10.1/aaa", "title": "Wolf eyes", "year": 2010, "authors": ["Jane Q. Doe", "Ann Roe"],
             "venue": "J Eyes", "abstract": "x " * 40, "text": "text/a.txt"},
            {"doi": "https://doi.org/10.1/BBB", "key": "10.1/bbb", "title": "Abstract only", "year": 1999, "authors": ["Bo Li"],
             "venue": "J Abs", "abstract": "Mallard eyes have a lambda max of 415 nm in the violet cone. " + "word " * 30, "text": None},
            {"doi": "10.1/ccc", "key": "10.1/ccc", "title": "No abstract", "year": 2001, "authors": ["C D"], "abstract": None, "text": None},
        ]
        with open(os.path.join(self.d, "topic", "index.jsonl"), "w") as f:
            for w in works:
                f.write(json.dumps(w) + "\n")
        self.check = E.load_check()

    def run_mock(self, replies):
        items = E.plan_works(self.d, ["topic"])
        ps = list(E.build_passages(items))
        raw = os.path.join(self.d, "raw.jsonl")
        with open(raw, "w") as f:
            for p, rep in zip(ps, replies):
                f.write(json.dumps({"custom_id": p["id"], "result": {"type": "succeeded", "message": {
                    "stop_reason": "end_turn", "content": [{"type": "text", "text": rep}],
                    "usage": {"input_tokens": 1000, "output_tokens": 100, "cache_read_input_tokens": 3000}}}}) + "\n")
        return E.check_results(raw, ps, items, ["topic"], self.check), ps

    def test_plan(self):
        items = E.plan_works(self.d, ["topic"])
        self.assertEqual(len(items), 3)
        ps = list(E.build_passages(items))
        self.assertEqual([p["key"] for p in ps], ["10.1/aaa", "10.1/bbb"])      # no abstract, no passage
        self.assertNotIn("Somebody", ps[0]["text"])                                # references cut
        self.assertEqual(E.norm_doi("https://doi.org/10.1/BBB"), "10.1/bbb")

    def test_split(self):
        text = "\n\n".join(" ".join(["w%d" % i] * 400) for i in range(10))
        ps = E.passages_of(text)
        self.assertTrue(all(E.words(p) <= 1600 for p in ps))
        self.assertEqual(sum(E.words(p) for p in ps), 4000)
        one = " ".join(["s."] * 4000)
        self.assertTrue(all(E.words(p) <= 1500 for p in E.passages_of(one)))

    def test_quote_check(self):
        good = {"taxon": "Lycosa leuckartii", "trait": "interreceptor_deg", "value": 2.45, "units": "degrees", "eye": "AL",
                "where": "abstract", "quote": "The inter-receptor angle of the AL eyes was 2.45°", "grade": "m"}
        invented = dict(good, quote="The inter-receptor angle of the AL eyes was 3.10°", value=3.1)
        longq = dict(good, quote=" ".join(["Eyes"] * 41))
        badtrait = dict(good, trait="not_a_trait")
        newtrait = dict(good, trait="pupil_shape", note="new trait: shape of the pupil")
        nogr = dict(good, eye="AM", grade="")
        (out, stats, usage), ps = self.run_mock([json.dumps([good, invented, longq, badtrait, newtrait, nogr, good]), "[]"])
        kept = out["topic"]
        self.assertEqual(len(kept), 3)                          # good, newtrait, nogr (grade set to g); duplicate dropped
        self.assertEqual(stats["dropped_quote_not_found"], 2)   # invented and the 41-word one is not in the text either
        self.assertEqual(stats["dropped_check_py"], 1)
        self.assertEqual(stats["dropped_duplicate"], 1)
        self.assertEqual(stats["grade_set_to_g"], 1)
        g = kept[0]
        self.assertEqual(g["source"]["authors"], "Doe JQ, Roe A")
        self.assertIs(g["checks"]["value_in_quote"], True)
        self.assertEqual(g["source"]["access"], "open")
        self.assertEqual(self.check.problems(g), [])

    def test_parse(self):
        self.assertEqual(E.parse_reply("[]")[0], [])
        self.assertEqual(len(E.parse_reply('```json\n[{"a":1}]\n```')[0]), 1)
        self.assertEqual(len(E.parse_reply('Here you go: [{"a":1}] done')[0]), 1)
        self.assertIsNotNone(E.parse_reply("nothing")[1])

    def test_cut_off_reply_is_salvaged(self):
        recs, err = E.parse_reply('[{"a": 1}, {"b": "two"}, {"c": "thr')
        self.assertEqual(recs, [{"a": 1}, {"b": "two"}])
        self.assertEqual(err, "cut off")
        self.assertEqual(E.parse_reply("[")[0], [])

    def test_url_from_index_record(self):
        self.assertEqual(E.index_url({"doi": "https://doi.org/10.1/X"}), "https://doi.org/10.1/x")
        self.assertEqual(E.index_url({"landing_url": "https://a.b/c"}), "https://a.b/c")
        self.assertEqual(E.index_url({"pmcid": "PMC123"}), "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC123/")
        self.assertEqual(E.index_url({"pmid": "99"}), "https://pubmed.ncbi.nlm.nih.gov/99/")
        self.assertEqual(E.index_url({"openalex": "W5"}), "https://openalex.org/W5")
        self.assertEqual(E.index_url({"epmc_id": "IND1", "source_epmc": "AGR"}), "https://europepmc.org/article/AGR/IND1")
        self.assertEqual(E.index_url({}), "")
        # a work with no doi keeps its record, because check.py accepts the url
        w = {"title": "T", "year": 2000, "authors": ["A B"], "pmid": "99"}
        r = {"taxon": "x", "trait": "motion", "value": "fast", "where": "t", "quote": "q", "grade": "m",
             "source": E.source_of(w, False), "opened": True}
        self.assertEqual(self.check.problems(r), [])

    def test_models_and_prices(self):
        keep = (E.MODEL, E.PRICE)
        try:
            E.set_model("claude-sonnet-5-5")
            self.assertAlmostEqual(E.actual_cost({"output_tokens": 1_000_000}), 5.0)
            with self.assertRaises(SystemExit):
                E.set_model("claude-nothing")
        finally:
            E.MODEL, E.PRICE = keep

    def test_squash_and_numbers(self):
        self.assertEqual(E.squash("inter-\nreceptor ﬁeld"), E.squash("interreceptor field"))
        self.assertTrue(E.value_in_quote([505, 510], "maxima at 505-510 nm"))
        self.assertFalse(E.value_in_quote(2.45, "angle of 2.54"))
        self.assertIsNone(E.value_in_quote("present", "x"))

    def test_cost(self):
        ps = [{"words": 1500}] * 1000
        e = E.estimate(ps)
        self.assertLess(e["expected_usd"], e["ceiling_usd"])
        self.assertAlmostEqual(E.actual_cost({"input_tokens": 1_000_000}), 0.05)

    def test_no_key(self):
        os.environ.pop("ANTHROPIC_API_KEY", None)
        with self.assertRaises(SystemExit):
            E.need_key()


# ---- a stand-in for the API, to run `extract.py run` end to end without a key --------------------------------------
import http.server, threading, re as _re, io, contextlib


class Mock(http.server.BaseHTTPRequestHandler):
    batches = {}
    singles = 0

    def log_message(self, *a):
        pass

    def reply(self, obj, raw=None):
        b = raw if raw is not None else json.dumps(obj).encode()
        self.send_response(200); self.send_header("content-length", str(len(b))); self.end_headers(); self.wfile.write(b)

    @staticmethod
    def model(params):
        user = params["messages"][0]["content"]
        body = user.split("---\n", 1)[1]
        recs = []
        for sent in _re.split(r"(?<=[.!?])\s+", body):
            m = _re.search(r"\d+(?:\.\d+)?", sent)
            if m and len(recs) < 2:
                recs.append({"taxon": "Lycosa", "trait": "interreceptor_deg", "value": float(m.group()), "units": "degrees",
                             "eye": "", "method": "", "conditions": "", "where": "text", "quote": " ".join(sent.split()[:12]),
                             "grade": "m", "note": ""})
        recs.append({"taxon": "x", "trait": "motion", "value": "fast", "units": "", "where": "text",
                     "quote": "this sentence was invented by the mock model", "grade": "m"})
        return json.dumps(recs)

    def usage(self):
        return {"input_tokens": 900, "output_tokens": 120, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 3000}

    def do_POST(self):
        n = int(self.headers["content-length"]); body = json.loads(self.rfile.read(n))
        assert self.headers["x-api-key"] == "test-key"
        if self.path == "/v1/messages":
            Mock.singles += 1
            self.reply({"content": [{"type": "text", "text": self.model(body)}], "usage": self.usage(), "stop_reason": "end_turn"})
        elif self.path == "/v1/messages/batches":
            bid = "msgbatch_%d" % (len(Mock.batches) + 1)
            Mock.batches[bid] = body["requests"]
            self.reply({"id": bid, "processing_status": "in_progress"})
        else:
            self.send_response(404); self.end_headers()

    def do_GET(self):
        host = "http://127.0.0.1:%d" % self.server.server_address[1]
        m = _re.match(r"/v1/messages/batches/(\w+)(/results)?$", self.path)
        if not m or m.group(1) not in Mock.batches:
            self.send_response(404); self.end_headers(); return
        reqs = Mock.batches[m.group(1)]
        if m.group(2):
            lines = [json.dumps({"custom_id": r["custom_id"], "result": {"type": "succeeded", "message": {
                "content": [{"type": "text", "text": self.model(r["params"])}], "usage": self.usage(), "stop_reason": "end_turn"}}})
                for r in reqs]
            self.reply(None, raw="\n".join(lines).encode())
        else:
            self.reply({"id": m.group(1), "processing_status": "ended", "request_counts": {"succeeded": len(reqs)},
                        "results_url": host + self.path + "/results"})


class EndToEnd(unittest.TestCase):
    def test_run_against_mock(self):
        srv = http.server.HTTPServer(("127.0.0.1", 0), Mock)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        E.API = "http://127.0.0.1:%d" % srv.server_address[1]
        os.environ["ANTHROPIC_API_KEY"] = "test-key"
        d = tempfile.mkdtemp()
        os.makedirs(os.path.join(d, "lit", "t", "text"))
        with open(os.path.join(d, "lit", "t", "text", "a.txt"), "w") as f:
            f.write("Intro.\n\nThe inter-receptor angle was 2.45 degrees in the AL eyes. " + "More text here. " * 40)
        with open(os.path.join(d, "lit", "t", "index.jsonl"), "w") as f:
            f.write(json.dumps({"doi": "10.1/aaa", "key": "10.1/aaa", "title": "T", "year": 2010, "authors": ["A B"],
                                "abstract": "x " * 40, "text": "text/a.txt"}) + "\n")
            f.write(json.dumps({"doi": "10.1/bbb", "key": "10.1/bbb", "title": "U", "year": 2011, "authors": ["C D"],
                                "abstract": "The acuity was 1.5 cycles per degree in the posterior eyes. " + "y " * 30, "text": None}) + "\n")
        sys.argv = ["extract.py", "run", "--lit", os.path.join(d, "lit"), "--topics", "t", "--out", os.path.join(d, "out"),
                    "--max-usd", "1", "--wait-minutes", "1"]
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            E.main()
        rows = [json.loads(l) for l in open(os.path.join(d, "out", "t.jsonl"))]
        self.assertEqual(Mock.singles, 1)
        self.assertGreaterEqual(len(rows), 2)
        self.assertTrue(all(r["trait"] == "interreceptor_deg" for r in rows))      # the invented quote never survives
        self.assertIn("dropped_quote_not_found", buf.getvalue() + open(os.path.join(d, "out", "SUMMARY.md")).read())
        self.assertTrue(os.path.exists(os.path.join(d, "out", "_work", "batches.json")))
        srv.shutdown()


if __name__ == "__main__":
    unittest.main()
