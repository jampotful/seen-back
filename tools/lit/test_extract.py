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


if __name__ == "__main__":
    unittest.main()
