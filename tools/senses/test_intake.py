#!/usr/bin/env python3
"""Offline intake regressions; recent accepted records are fixtures, never edited."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


GATE = load("submission_gate", HERE / "check_submission.py")
CHECK = GATE.CHECK
EXAMPLES = json.loads((ROOT / "docs/views/research/evidence-intake-examples.json").read_text())
RECENT = json.loads((ROOT / "tools/senses/fixtures/intake-recent.json").read_text())


def recent_bytes(number):
    path = f"docs/views/evidence/desk-d{number}.jsonl"
    local = ROOT / path
    data = local.read_bytes() if local.exists() else b""
    def blob_sha(value):
        return hashlib.sha1(b"blob " + str(len(value)).encode() + b"\0" + value).hexdigest()
    if blob_sha(data) != RECENT["blobs"][path]:
        # A stacked PR may precede these records; a later independent audit may
        # change them. Use the immutable accepted snapshot, never mutable main.
        result = subprocess.run(["git", "-C", str(ROOT), "show", f"{RECENT['commit']}:{path}"],
                                capture_output=True)
        if result.returncode:
            raise RuntimeError(f"Recent fixture missing: git fetch --depth=1 origin {RECENT['commit']}; {path}")
        data = result.stdout
    if blob_sha(data) != RECENT["blobs"][path]:
        raise RuntimeError("Recent fixture hash mismatch: " + path)
    return data


class Intake(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        dest = self.root / "tools/senses"
        dest.mkdir(parents=True)
        for name in ("check.py", "evidence_scope.py", "addlog.py", "check_submission.py"):
            shutil.copyfile(HERE / name, dest / name)
        self.path = "docs/views/evidence/test.jsonl"
        self.log = self.root / self.path
        self.log.parent.mkdir(parents=True)
        self.typed = copy.deepcopy(EXAMPLES[5])
        self.legacy = dict(self.typed)
        self.legacy.pop("evidence_kind")

    def cli(self, script, *args, rows=None):
        return subprocess.run([sys.executable, "-I", str(self.root / "tools/senses" / script), *args],
                              input=None if rows is None else self.text(rows), text=True, capture_output=True)

    @staticmethod
    def text(rows):
        return "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True,
                              text=True, capture_output=True).stdout.strip()

    def baseline(self, rows):
        self.log.write_text(self.text(rows))
        self.git("init", "-q")
        self.git("add", ".")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "baseline")
        return self.git("rev-parse", "HEAD")

    def gate(self, base, *paths):
        return self.cli("check_submission.py", "--base-ref", base, *paths)

    def test_all_worked_examples_append_and_strict_validate(self):
        r = self.cli("addlog.py", "test", rows=EXAMPLES)
        self.assertEqual(r.returncode, 0, r.stderr)
        r = self.cli("check.py", "--require-evidence-kind", str(self.log))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual([json.loads(l) for l in self.log.read_text().splitlines()], EXAMPLES)

    def test_combined_kinds_and_ecological_intake_preserve_legacy(self):
        self.assertEqual({r['evidence_kind'] for r in EXAMPLES}, CHECK.SCOPE.KINDS)
        outcome = next(r for r in EXAMPLES if r['evidence_kind'] == 'ecological_outcome')
        base = self.baseline([self.legacy])
        self.log.write_text(self.text([self.legacy, outcome]))
        result = self.gate(base)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('1 unchanged legacy, 1 new/changed', result.stdout)
        for field in ('evidence_kind', 'measured_endpoint', 'experimental_unit',
                      'intervention', 'comparator', 'mechanism_limit'):
            incomplete = dict(outcome); incomplete.pop(field)
            self.log.write_text(self.text([self.legacy, incomplete]))
            self.assertNotEqual(self.gate(base).returncode, 0, field)
        for trait in ('behaviour_vision', 'colour_vision', 'sense_hearing'):
            self.log.write_text(self.text([self.legacy, dict(outcome, trait=trait)]))
            self.assertNotEqual(self.gate(base).returncode, 0, trait)

    def test_actual_melotte_candidates_pass_delta_gate_without_admission(self):
        fixture = ROOT / 'tools/senses/fixtures/melotte-2018/evidence.jsonl'
        candidates = [json.loads(line) for line in fixture.read_text().splitlines()]
        self.assertEqual(len(candidates), 8)
        base = self.baseline([self.legacy])
        self.log.write_text(self.text([self.legacy] + candidates))
        result = self.gate(base)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn('1 unchanged legacy, 8 new/changed', result.stdout)
        for candidate in candidates:
            untyped = dict(candidate); untyped.pop('evidence_kind')
            self.log.write_text(self.text([self.legacy, untyped]))
            self.assertNotEqual(self.gate(base).returncode, 0)

    def test_untyped_append_rejects_entire_batch_without_writing(self):
        self.log.write_text(self.text([self.legacy]))
        before = self.log.read_bytes()
        r = self.cli("addlog.py", "test", rows=[self.typed, self.legacy])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("new functional records require evidence_kind", r.stderr)
        self.assertEqual(self.log.read_bytes(), before)

    def test_append_preserves_legacy_bytes(self):
        self.log.write_text(self.text([self.legacy]))
        before = self.log.read_bytes()
        r = self.cli("addlog.py", "test", rows=[self.typed])
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertTrue(self.log.read_bytes().startswith(before))
        self.assertEqual(self.cli("check.py", str(self.log)).returncode, 0)
        self.assertNotEqual(self.cli("check.py", "--require-evidence-kind", str(self.log)).returncode, 0)

    def test_direct_write_new_functional_record_requires_kind(self):
        base = self.baseline([self.legacy])
        self.log.write_text(self.text([self.legacy, dict(self.legacy, value="new result")]))
        before = self.log.read_bytes()
        r = self.gate(base)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("1 unchanged legacy, 1 new/changed", r.stdout)
        self.assertEqual(self.log.read_bytes(), before)
        self.log.write_text(self.text([self.legacy, self.typed]))
        self.assertEqual(self.gate(base).returncode, 0)

    def test_changed_qualification_requires_classification(self):
        base = self.baseline([self.legacy])
        for field in ("note", "conditions", "quote", "method", "value"):
            with self.subTest(field=field):
                self.log.write_text(self.text([dict(self.legacy, **{field: "changed finding"})]))
                self.assertNotEqual(self.gate(base).returncode, 0)

    def test_reordering_and_formatting_do_not_reclassify_legacy(self):
        other = dict(self.legacy, value="second old result")
        base = self.baseline([self.legacy, other])
        self.log.write_text("\n" + json.dumps(other, sort_keys=True) + "\n" + json.dumps(self.legacy, sort_keys=True) + "\n")
        r = self.gate(base, self.path)
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("2 unchanged legacy, 0 new/changed", r.stdout)

    def test_duplicate_multiplicity_is_not_a_legacy_escape(self):
        base = self.baseline([self.legacy])
        self.log.write_text(self.text([self.legacy, self.legacy]))
        self.assertNotEqual(self.gate(base).returncode, 0)

    def test_untracked_and_corrected_outputs_are_checked(self):
        base = self.baseline([self.legacy])
        for path in ("docs/views/evidence/new.jsonl", "docs/views/audit/corrected/test.jsonl"):
            p = self.root / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(self.text([self.legacy]))
            r = self.gate(base)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn(path, r.stdout)
            p.unlink()

    def test_invalid_base_and_missing_or_invalid_paths_fail_closed(self):
        base = self.baseline([self.legacy])
        for ref, path in (("missing-ref", self.path), (base, "docs/views/evidence/missing.jsonl"),
                          (base, "../outside.jsonl"), (base, "/tmp/records.jsonl")):
            self.assertNotEqual(self.gate(ref, path).returncode, 0)

    def test_invalid_json_and_field_types_fail_without_traceback(self):
        base = self.baseline([self.legacy])
        for text in ('{"broken":', '[]\n', self.text([dict(self.typed, evidence_kind=[])]),
                     self.text([dict(self.typed, trait=None)])):
            self.log.write_text(text)
            r = self.gate(base)
            self.assertNotEqual(r.returncode, 0)
            self.assertNotIn("Traceback", r.stderr)

    def test_invalid_and_anatomy_misfiled_kinds_rejected(self):
        for kind in ("unknown", "behavioral_response", "anatomical_measurement"):
            self.assertTrue(CHECK.problems(dict(self.typed, evidence_kind=kind), require_evidence_kind=True))

    def test_exact_mandatory_trait_boundary(self):
        self.assertTrue(CHECK.problems(dict(self.legacy, trait="behaviour_vision"), require_evidence_kind=True))
        self.assertTrue(CHECK.problems(dict(self.legacy, trait="sense_new", note="new trait: test"), require_evidence_kind=True))
        self.assertFalse(CHECK.problems(dict(self.legacy, trait="polarization"), require_evidence_kind=True))

    def test_recent_accepted_33_ordinary_pass_32_need_kind_if_refiled(self):
        total = required = 0
        for number in range(250, 255):
            path = ROOT / f"docs/views/evidence/desk-d{number}.jsonl"
            before = recent_bytes(number)
            rows = GATE.records(before.decode(), str(path))
            self.assertEqual(GATE.compare(rows, rows)[0], [])
            for _, row in rows:
                self.assertNotIn("evidence_kind", row)
                self.assertEqual(CHECK.problems(row), [])
                bad = CHECK.problems(row, require_evidence_kind=True)
                if CHECK.SCOPE.functional_trait(row["trait"]):
                    self.assertEqual(bad, ["new functional records require evidence_kind"])
                    required += 1
                else:
                    self.assertEqual(bad, [])
                    self.assertEqual(row["trait"], "polarization")
                total += 1
            self.assertEqual(recent_bytes(number), before)
        self.assertEqual((total, required), (33, 32))

    def test_representative_typed_copies_preserve_scientific_payload(self):
        # Format replays, NOT source-verified classifications or audit decisions.
        for unit, line, kind in ((250, 1, "behavioural_response"), (251, 6, "transduction"),
                                 (252, 2, "behavioural_response")):
            original = json.loads(recent_bytes(unit).decode().splitlines()[line-1])
            typed = dict(original, evidence_kind=kind)
            self.assertEqual(CHECK.problems(typed, require_evidence_kind=True), [])
            self.assertEqual(self.cli("addlog.py", "test", rows=[typed]).returncode, 0)
            recovered = json.loads(self.log.read_text().splitlines()[-1])
            recovered.pop("evidence_kind")
            self.assertEqual(recovered, original)


if __name__ == "__main__":
    unittest.main()
