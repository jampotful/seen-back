#!/usr/bin/env python3
"""Offline safety/receipt tests, not a test of scientific interpretation accuracy."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("preflight", HERE / "scientific_preflight.py")
preflight = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preflight)


def candidate():
    # Synthetic record: no scientific assertion about a real taxon or paper.
    return {"taxon": "Test taxon", "trait": "sense_chemical",
            "value": "Treatment increased final proportion; onset was unchanged",
            "method": "Controlled assay", "conditions": "Same sampling endpoint",
            "note": "Synthetic test only", "source": {"doi": "test:paper", "access": "open"},
            "quote": "Synthetic quote", "grade": "m", "opened": True}


def review(records):
    rows = preflight.template(records)
    for paper in rows:
        paper.update(access={"kind": "full_text", "inspected": ["Synthetic Methods and Table 1"],
                             "unavailable": []},
                     design="Treated and control groups assessed at the same time",
                     metrics="Final proportion is distinct from onset time",
                     results=[{"where": "Synthetic Table 1", "finding": "Proportion increased; onset unchanged"}],
                     reconciliation="Synthetic abstract and Table 1 agree on both outcomes")
        for entry in paper["records"]:
            entry.update(decision="ready", claim_check="Value and conditions preserve both outcomes")
    return rows


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.records = {1: candidate()}
        self.reviews = review(self.records)

    def errors(self):
        return "\n".join(preflight.problems(self.records, self.reviews))

    def test_skeleton_cannot_certify_anything(self):
        self.reviews = preflight.template(self.records)
        self.assertIn("held or undecided", self.errors())
        self.assertIn("missing located results", self.errors())

    def test_complete_receipt_and_canonical_hash(self):
        self.assertEqual(self.errors(), "")
        reordered = dict(reversed(list(self.records[1].items())))
        self.assertEqual(preflight.digest(reordered), preflight.digest(self.records[1]))

    def test_edit_to_conditions_invalidates_receipt(self):
        self.records[1]["conditions"] = "Onset was faster"
        self.assertIn("stale record", self.errors())

    def test_coverage_cannot_be_skipped_or_duplicated(self):
        self.records[3] = candidate()
        self.assertIn("line 3: missing scientific review", self.errors())
        self.reviews.append(deepcopy(self.reviews[0]))
        self.assertIn("duplicate receipt", self.errors())
        self.reviews[1]["records"][0]["line"] = 99
        self.assertIn("unknown candidate line 99", self.errors())

    def test_other_paper_receipt_is_rejected(self):
        self.reviews[0]["source"] = "test:other"
        self.assertIn("source mismatch", self.errors())

    def test_unread_table_cannot_be_claimed_as_full_text_verification(self):
        self.reviews[0]["access"]["unavailable"] = ["Table 2 unreadable"]
        self.assertIn("use incomplete", self.errors())
        self.reviews[0]["access"]["kind"] = "incomplete"
        self.assertIn("restricted access requires limited", self.errors())

    def test_limited_claim_must_preserve_limitation_in_record(self):
        paper = self.reviews[0]
        paper["access"] = {"kind": "incomplete", "inspected": ["Results prose"],
                           "unavailable": ["Table 2 image unreadable"]}
        entry = paper["records"][0]
        entry.update(decision="limited", limitation="Table 2 unverified; only the prose claim is reported.")
        self.assertIn("preserve the exact limitation", self.errors())
        self.records[1]["note"] += "; " + entry["limitation"]
        entry["sha256"] = preflight.digest(self.records[1])
        self.assertEqual(self.errors(), "")

    def test_abstract_only_requires_both_status_fields(self):
        limitation = "Abstract only; Methods, tables and full Results unavailable."
        self.records[1]["note"] = limitation
        paper = self.reviews[0]
        paper["access"] = {"kind": "abstract_only", "inspected": ["Publisher abstract"],
                           "unavailable": ["Full text inaccessible"]}
        entry = paper["records"][0]
        entry.update(decision="limited", limitation=limitation,
                     sha256=preflight.digest(self.records[1]))
        self.assertIn("abstract-only needs", self.errors())
        self.records[1]["source"]["access"] = "abstract"
        self.records[1]["partial"] = True
        entry["sha256"] = preflight.digest(self.records[1])
        self.assertEqual(self.errors(), "")

    def test_held_claim_does_not_submit(self):
        self.reviews[0]["records"][0]["decision"] = "hold"
        self.assertIn("held or undecided", self.errors())

    def test_abstract_cannot_bypass_status_check_as_incomplete(self):
        self.records[1]["source"]["access"] = "abstract"
        self.reviews[0]["access"]["kind"] = "incomplete"
        self.assertIn("abstract-only source requires", self.errors())

    def test_malformed_review_fields_fail_without_crashing(self):
        for field, value in [("access", None), ("results", [None]), ("records", [None])]:
            with self.subTest(field=field):
                rows = deepcopy(self.reviews)
                rows[0][field] = value
                self.assertTrue(preflight.problems(self.records, rows))
        self.records[1]["source"] = "malformed"
        self.assertIn("source mismatch", self.errors())

    def test_cli_is_read_only_and_preserves_physical_line_numbers(self):
        with tempfile.TemporaryDirectory() as tmp:
            candidates = Path(tmp) / "candidates.jsonl"
            receipt = Path(tmp) / "review.jsonl"
            raw = "\n" + json.dumps(candidate()) + "\n"
            candidates.write_text(raw)
            command = [sys.executable, "-I", str(HERE / "scientific_preflight.py"), str(candidates)]
            skeleton = subprocess.run(command + ["--template"], capture_output=True, text=True)
            self.assertEqual(skeleton.returncode, 0, skeleton.stderr)
            self.assertEqual(json.loads(skeleton.stdout)["records"][0]["line"], 2)
            receipt.write_text(json.dumps(review({2: candidate()})[0]) + "\n")
            before = receipt.read_bytes()
            result = subprocess.run(command + ["--review", str(receipt)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("documentation only", result.stdout)
            self.assertEqual(candidates.read_text(), raw)
            self.assertEqual(receipt.read_bytes(), before)
            receipt.write_text("[]\n")
            result = subprocess.run(command + ["--review", str(receipt)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("Traceback", result.stderr)

    def test_completed_but_false_assurance_is_not_detected(self):
        # Explicit boundary: the gate has no source text and no semantic oracle.
        self.reviews[0]["results"][0]["finding"] = "An incorrect human interpretation"
        self.assertEqual(self.errors(), "")


if __name__ == "__main__":
    unittest.main()
