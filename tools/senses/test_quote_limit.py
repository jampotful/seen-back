#!/usr/bin/env python3
"""Offline regression: python3 -I tools/senses/test_quote_limit.py.

Exercise the checker and actual addlog CLI in a disposable repository layout.
The CC BY sentence is Nemoto et al. (2022), doi:10.1371/journal.pone.0272665,
Results. This fixture tests length acceptance, not independent scientific review.
"""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("evidence_check", HERE / "check.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

QUOTE = ("GA3 treatment promoted seed germination (7.8 ± 5.0%), but the germination "
         "rate was not significantly different from that in the Mock treatment group (2.7 ± 1.1%).")


def record(quote=QUOTE):
    return dict(taxon="Toxicodendron vernicifluum", trait="sense_chemical",
                value="GA3 not significantly different from mock", grade="m", opened=True,
                source=dict(authors="Nemoto K, Watanabe A, Yoshida C, Nishihara M",
                            year=2022, doi="10.1371/journal.pone.0272665", access="open"),
                where="Results", quote=quote)


class QuoteLimitTests(unittest.TestCase):
    def test_complete_result_above_125_characters(self):
        self.assertGreater(len(QUOTE), 125)
        self.assertEqual(len(QUOTE.split()), 26)
        self.assertEqual(checker.problems(record()), [])

    def test_word_boundary_including_whitespace(self):
        self.assertEqual(checker.MAX_QUOTE_WORDS, 40)
        self.assertEqual(checker.problems(record(" \n\t".join(["measurement"] * 40))), [])
        self.assertIn("quote is 41 words (at most 40)",
                      checker.problems(record(" ".join(["measurement"] * 41))))

    def test_other_requirements_remain(self):
        for changes, expected in [
            ({"quote": " "}, "quote is empty"),
            ({"opened": False}, "opened must be true"),
            ({"source": {}}, "source needs a doi or a url"),
            ({"grade": "invalid"}, "grade must be"),
        ]:
            with self.subTest(changes=changes):
                self.assertTrue(any(expected in p for p in checker.problems(record() | changes)))

    def test_addlog_and_checker_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dest = root / "tools" / "senses"
            dest.mkdir(parents=True)
            for name in ("check.py", "addlog.py"):
                shutil.copyfile(HERE / name, dest / name)
            def append(rec):
                return subprocess.run([sys.executable, "-I", str(dest / "addlog.py"), "regression"],
                                      input=json.dumps(rec) + "\n", text=True, capture_output=True)
            result = append(record())
            self.assertEqual(result.returncode, 0, result.stderr)
            log = root / "docs" / "views" / "evidence" / "regression.jsonl"
            before = log.read_bytes()
            self.assertEqual(json.loads(before)["quote"], QUOTE)
            result = subprocess.run([sys.executable, "-I", str(dest / "check.py"), str(log)],
                                    text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            result = append(record(" ".join(["measurement"] * 41)))
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("quote is 41 words", result.stderr)
            self.assertEqual(log.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
