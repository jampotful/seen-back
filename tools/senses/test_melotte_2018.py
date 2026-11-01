#!/usr/bin/env python3
"""Offline PR #49/#50 compatibility checks; no scientific acceptance or generation.

This integration reuses the PR #50 tests with isolated, commit-pinned fixture
copies. It does not place the eight candidate records in accepted evidence.
Run on the combined classification tree:
  python3 -I tools/senses/test_melotte_2018.py --require-classification

On PR #50 alone the two preservation checks run and classification checks skip.
The explicit flag refuses that skip, so integration validation cannot silently
pass without PR #49. Temporary raw/corrected logs below are test fixtures only.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "tools/senses/fixtures/melotte-2018/evidence.jsonl"
CURVES = ROOT / "tools/senses/fixtures/melotte-2018/audiograms.json"
ROWS = [json.loads(line) for line in LOG.read_text(encoding="utf-8").splitlines()]
HAS_CLASSIFICATION = (ROOT / "tools/senses/evidence_scope.py").exists()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


if HAS_CLASSIFICATION:
    CHECK = load("melotte_check", "tools/senses/check.py")
    G = load("melotte_gaps", "tools/views/gaps.py")
    R = load("melotte_rows", "tools/views/rows.py")
    C = load("melotte_compile", "tools/views/compile.py")


def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def species(name):
    # The core carry rule is tested without assigning an offered view. The
    # current fish view has no hearing row; no row or taxonomy mapping is added.
    return dict(sci=name, genus=name.split()[0], family="Serrasalmidae",
                order="Characiformes", view="", records=1)


class PreservationTests(unittest.TestCase):
    def test_only_evidence_kind_was_added_to_original_recovery(self):
        original = LOG.read_bytes()
        insertion = b' "evidence_kind": "transduction",'
        self.assertEqual(original.count(insertion), 8)
        # Original PR #50 at 6c4b7468847c6f5342730ebe70102f5b23243750.
        # Scientific changes after independent audit require a reviewed baseline.
        self.assertEqual(blob_sha(original.replace(insertion, b"")),
                         "03f1362ceb26f1b4ba0412e00e015ba995856aac")
        self.assertEqual([r["grade"] for r in ROWS], ["g", "m", "m", "g", "m", "m", "m", "m"])

    def test_structured_curves_are_the_unchanged_candidate_companion(self):
        self.assertEqual(blob_sha(CURVES.read_bytes()), "18c85866e2e55825e0f1b70dd71bf07894d2fe47")
        data = json.loads(CURVES.read_text(encoding="utf-8"))
        self.assertIn("not yet accepted", data["status"])
        self.assertEqual(len(data["curves"]), 8)
        self.assertEqual(sum(v is not None for c in data["curves"]
                             for v in c["mean_threshold_db_re_1_uPa"]), 107)
        for record, curve in zip(ROWS, data["curves"]):
            self.assertEqual(record["taxon"], curve["source_taxon"])
            self.assertEqual(record["grade"], curve["grade"])


@unittest.skipUnless(HAS_CLASSIFICATION, "requires PR #49 on the integration tree")
class ClassificationCompatibilityTests(unittest.TestCase):
    def test_strict_validation_and_untyped_negative_control(self):
        for row in ROWS:
            self.assertEqual(CHECK.problems(row, require_evidence_kind=True), [])
            untyped = dict(row); untyped.pop("evidence_kind")
            self.assertIn("new functional records require evidence_kind",
                          CHECK.problems(untyped, require_evidence_kind=True))
            self.assertTrue(CHECK.SCOPE.supports_trait(row, "sense_hearing"))
            self.assertFalse(CHECK.SCOPE.supports_trait(row, "behaviour_vision"))

    def test_real_append_cli_accepts_typed_and_atomically_rejects_untyped(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "tools/senses"; dest.mkdir(parents=True)
            for name in ("check.py", "addlog.py", "evidence_scope.py"):
                shutil.copyfile(ROOT / "tools/senses" / name, dest / name)
            log = Path(tmp) / "docs/views/evidence/test.jsonl"
            def append(records):
                return subprocess.run([sys.executable, "-I", str(dest / "addlog.py"), "test"],
                                      input="".join(json.dumps(r) + "\n" for r in records),
                                      text=True, capture_output=True)
            untyped = dict(ROWS[-1]); untyped.pop("evidence_kind")
            result = append(ROWS[:-1] + [untyped])
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("require evidence_kind", result.stderr)
            self.assertFalse(log.exists())
            result = append(ROWS)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual([json.loads(s) for s in log.read_text().splitlines()], ROWS)

    def test_loaders_keep_every_original_field(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / "docs/views/evidence/melotte-2018.jsonl"
            raw.parent.mkdir(parents=True); raw.write_bytes(LOG.read_bytes())
            loaders = (lambda tax: G.load_evidence(tmp, tax, set())[0],
                       lambda tax: R.load_evidence(tmp, tax)[0])
            for loader in loaders:
                loaded = loader(G.Tax())
                self.assertEqual(len(loaded), 8)
                for before, after in zip(ROWS, loaded):
                    self.assertEqual({k: after[k] for k in before}, before)
            corrected = Path(tmp) / "docs/views/audit/corrected/melotte-2018.jsonl"
            corrected.parent.mkdir(parents=True); corrected.write_bytes(LOG.read_bytes())
            loaded = R.load_evidence(tmp, G.Tax())[0]
            self.assertEqual(len(loaded), 8)  # corrected copy takes precedence
            for before, after in zip(ROWS, loaded):
                self.assertEqual({k: after[k] for k in before}, before)

    def test_gap_core_does_not_upgrade_identity_or_carry_hearing(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = Path(tmp) / "docs/views/evidence/melotte-2018.jsonl"
            raw.parent.mkdir(parents=True); raw.write_bytes(LOG.read_bytes())
            for loader in (lambda tax: G.load_evidence(tmp, tax, set())[:2],
                           lambda tax: R.load_evidence(tmp, tax)[:2]):
                tax = G.Tax(); recs, index = loader(tax)
                def cell(name):
                    return G.cell(species(name), "sense_hearing", "none", index,
                                  G.order_evidence(recs), tax, [])
                for row in ROWS:
                    self.assertEqual(cell(row["taxon"])["state"], "m" if row["grade"] == "m" else "i")
                for name in ("Piaractus orinoquensis", "Myloplus schomburgkii", "Myloplus sauron",
                             "Myloplus aylan", "Serrasalmus rhombeus", "Pygocentrus cariba"):
                    self.assertEqual(cell(name)["state"], "i", name)

    def test_writer_inputs_keep_curves_protocol_and_identity_qualifications(self):
        for row in ROWS:
            rendered = R.record_line("R1", dict(row, _trait=row["trait"]))
            compiled = json.loads(C.record_line(dict(row, _id="R1", _inside=True, _audit="not audited")))
            for field in ("method", "conditions", "note", "where", "quote"):
                self.assertIn(row[field], rendered, (row["taxon"], field))
                self.assertEqual(compiled[field], row[field])
            self.assertIn("evidence_kind=transduction", rendered)
            self.assertEqual(compiled["evidence_kind"], "transduction")
            self.assertEqual(compiled["check"], "not audited")

    def test_compiler_selection_retains_eight_records_and_unaudited_status(self):
        job = dict(taxa=[r["taxon"] for r in ROWS], logs=[str(LOG)])
        candidates, _ = C.collect_records(job, str(ROOT / "unused"), {})
        picked = C.choose(candidates)
        self.assertEqual(len(picked), 8)
        before = {r["taxon"]: r for r in ROWS}
        for record in picked:
            self.assertEqual(record["_audit"], "not audited")
            self.assertEqual({k: record[k] for k in before[record["taxon"]]}, before[record["taxon"]])


if __name__ == "__main__":
    if "--require-classification" in sys.argv:
        sys.argv.remove("--require-classification")
        if not HAS_CLASSIFICATION:
            sys.exit("PR #49 is required for this integration run; no skips allowed")
    unittest.main()
