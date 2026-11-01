#!/usr/bin/env python3
"""Offline claim-scope regressions. --corpus also verifies current-main records.

The proposal contains complete corrected records and reversible field deltas, so
unit tests also run on the stacked PR before its current-main data are merged.
"""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
CORPUS = "--corpus" in sys.argv
if CORPUS:
    sys.argv.remove("--corpus")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


CHECK = load("ecology_check", "tools/senses/check.py")
S = CHECK.SCOPE
G = load("ecology_gaps", "tools/views/gaps.py")
R = load("ecology_rows", "tools/views/rows.py")
C = load("ecology_compile", "tools/views/compile.py")
LEDGER_PATH = "tools/senses/fixtures/recheck-ecological-350.jsonl"
LEDGER = [json.loads(x) for x in (ROOT / LEDGER_PATH).read_text().splitlines()]
LIMITS = S.load_limits(ROOT)


def original(audit):
    record = dict(audit["corrected_record"])
    for field in audit["added_fields"]:
        del record[field]
    record.update(audit["original_fields"])
    return record


def write(root, path, records):
    target = Path(root) / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))


def species(record):
    return dict(sci=record["taxon"], genus=record["taxon"].split()[0],
                family=record["family"], order=record["order"], view="", records=1)


def indexed(record):
    return dict(record, _id="test#1", _trait=record["trait"],
                _names=[record["taxon"]], _genus=record["taxon"].split()[0],
                _family=record["family"], _order=record["order"])


class EcologicalOutcomeTests(unittest.TestCase):
    def test_proposals_preserve_findings_and_original_identity(self):
        self.assertEqual(len(LEDGER), 5)
        for audit in LEDGER:
            before, after = original(audit), audit["corrected_record"]
            self.assertEqual(S.fingerprint(before), audit["original_fingerprint"])
            self.assertIn(audit["original_fingerprint"], LIMITS)
            self.assertEqual(CHECK.problems(after, require_evidence_kind=True), [])
            for key in ("taxon", "rank", "family", "order", "value", "units", "grade", "source", "method", "conditions", "where", "quote", "opened"):
                self.assertEqual(before.get(key), after.get(key), (audit["id"], key))
            self.assertEqual(after["grade"], "m")
            self.assertEqual(audit["verdict"], "correct")
        turtle = LEDGER[0]["corrected_record"]
        for number in ("70 pairs", "14 in control", "6 in illuminated", "0.039"):
            self.assertIn(number, turtle["conditions"])
        self.assertIn("59.5%", turtle["value"])

    def test_new_outcomes_require_scope_and_cannot_be_renamed_as_vision(self):
        record = LEDGER[0]["corrected_record"]
        for field in ("evidence_kind", "measured_endpoint", "experimental_unit", "intervention", "comparator", "mechanism_limit", "method", "conditions", "units"):
            bad = dict(record); bad.pop(field)
            self.assertTrue(CHECK.problems(bad), field)
        for trait in ("behaviour_vision", "colour_vision", "motion", "lambda_max_nm", "sense_hearing"):
            bad = dict(record, trait=trait, _trait=trait)
            self.assertTrue(CHECK.problems(bad))
            self.assertFalse(S.supports_trait(bad, trait))

    def test_originals_stay_unchanged_and_changed_findings_do_not_inherit_limit(self):
        for audit in LEDGER:
            before = original(audit)
            limited = S.apply_limit(before, LIMITS)
            self.assertTrue(S.ecological(limited))
            self.assertTrue(S.restricted(limited))
            self.assertFalse(S.supports_trait(limited, before["trait"]))
            self.assertEqual({k: v for k, v in limited.items() if k not in ("sensory_use_limit", "sensory_use_scope")}, before)
            self.assertNotIn("sensory_use_limit", before)
            self.assertNotIn("sensory_use_limit", S.apply_limit(dict(before, value="different endpoint"), LIMITS))

    def test_legacy_and_refiled_records_in_both_loaders(self):
        for audit in LEDGER:
            before, after = original(audit), audit["corrected_record"]
            for loader in (G.load_evidence, lambda rt, tx, _: R.load_evidence(rt, tx)[:2]):
                for folder in ("evidence", "audit/corrected"):
                    # gaps consumes raw evidence only; rows handles both paths.
                    if loader == G.load_evidence and folder == "audit/corrected":
                        continue
                    with self.subTest(id=audit["id"], folder=folder), tempfile.TemporaryDirectory() as root:
                        path = "docs/views/" + folder + "/case.jsonl"
                        write(root, path, [before])
                        tax = G.Tax(); recs, index = loader(root, tax, set())
                        self.assertEqual(G.cell(species(before), before["trait"], "none", index, G.order_evidence(recs), tax, [])["state"], "m")
                        write(root, "docs/views/ecological-use-limits.jsonl", [LIMITS[audit["original_fingerprint"]]])
                        recs, index = loader(root, tax, set())
                        self.assertEqual(G.cell(species(before), before["trait"], "none", index, G.order_evidence(recs), tax, [])["state"], "i")
                        self.assertEqual(recs[0]["value"], before["value"])
                        write(root, path, [after])
                        recs, index = loader(root, tax, set())
                        self.assertEqual(G.cell(species(after), S.OUTCOME, "none", index, G.order_evidence(recs), tax, [])["state"], "m")
                        self.assertEqual(G.cell(species(after), before["trait"], "none", index, G.order_evidence(recs), tax, [])["state"], "i")
                        relative = dict(species(after), sci=after["taxon"].split()[0] + " other")
                        self.assertEqual(G.cell(relative, S.OUTCOME, "order", index, G.order_evidence(recs), tax, [])["state"], "i")

    def test_controlled_behaviour_and_nulls_are_not_blanket_excluded(self):
        for audit in LEDGER:
            record = dict(original(audit), value="Synthetic controlled behavioural null", evidence_kind="behavioural_response")
            self.assertFalse(S.restricted(S.apply_limit(record, LIMITS)))
            self.assertTrue(S.supports_trait(record, record["trait"]))
            self.assertEqual(CHECK.problems(record, require_evidence_kind=True), [])

    def test_writers_keep_full_context_for_legacy_and_refiled_outcomes(self):
        for record in (S.apply_limit(original(LEDGER[0]), LIMITS), LEDGER[0]["corrected_record"]):
            record = indexed(record)
            record.update(_inside=True, _audit="test", note=record["note"] + " " * 2 + "Late causal restriction must survive.")
            row_line = R.record_line("R1", record)
            compiler_line = json.loads(C.record_line(record))
            for field in ("method", "conditions", "where", "note"):
                self.assertIn(record[field], row_line)
                self.assertEqual(compiler_line[field], record[field])
            for field in ("measured_endpoint", "experimental_unit", "intervention", "comparator", "mechanism_limit"):
                if field in record:
                    self.assertIn(record[field], row_line)
                    self.assertEqual(compiler_line[field], record[field])

    def test_functional_rows_reject_outcomes_but_factual_outcome_rows_survive(self):
        record = indexed(LEDGER[0]["corrected_record"])
        row = dict(records=[record], traits=["behaviour_vision"], grade="m", title="Vision", species=[species(record)])
        draft = dict(text="You see green lights.", cites=["R1"])
        for traits in (["behaviour_vision"], ["colour_vision"], ["motion"], [], [S.OUTCOME, "behaviour_vision"]):
            row["traits"] = traits
            self.assertTrue(any("ecological outcome" in e for e in R.check_draft(draft, row, {"R1": "test#1"})))
        row.update(traits=[S.OUTCOME], title="Net illumination")
        draft["text"] = "Green turtle bycatch decreased in illuminated nets. The mechanism was not isolated."
        self.assertEqual(R.check_draft(draft, row, {"R1": "test#1"}), [])

    def test_compiler_blocks_measurements_calculations_and_generic_rows(self):
        specs = C.all_specs(); schema = C.schema_facts(specs)
        old = dict(S.apply_limit(original(LEDGER[0]), LIMITS), _id="R1", _file="desk-d254.jsonl", _inside=True, _audit="test")
        new = dict(LEDGER[0]["corrected_record"], _id="R1", _file="desk-d254.jsonl", _inside=True, _audit="test")
        other = dict(old, _id="R2", trait="receptor_classes", evidence_kind="transduction", value=3)
        for field in ("sensory_use_scope", "sensory_use_limit"):
            other.pop(field, None)
        for record in (old, new):
            for src in (["R1"], ["R1", "R2"]):
                reply = dict(spec=dict(key="test", who="a green turtle", chip="Test", cue="Light moves.",
                    params=dict(glow=dict(value=0.595, grade="g", invented=True, src=src)),
                    rows=[["m", "Vision", "You see green lights.", ["R1"], []]], matrices={}, draw={}),
                    claims=[dict(path="params.glow", records=src, kind="calculation", how="59.5 divided by 100")],
                    quotes=[dict(record=k, quote=record["quote"]) for k in src])
                job = dict(key="test", taxa=["Chelonia"], like="reptile")
                errors, *_ = C.check_reply(job, schema, {"R1": record, "R2": other}, copy.deepcopy(reply), specs["reptile"], {})
                self.assertTrue(any("ecological outcomes cannot establish a measured engine parameter" in e for e in errors), errors)
                self.assertTrue(any("explicitly scoped outcome-row path" in e for e in errors), errors)
                reply["spec"]["params"]["glow"].update(grade="i", src=[])
                reply["spec"]["rows"] = [["i", "Drawing", "The glow is invented.", [], []]]
                reply.update(claims=[], quotes=[])
                errors, *_ = C.check_reply(job, schema, {"R1": record}, copy.deepcopy(reply), specs["reptile"], {})
                self.assertFalse(any("ecological outcome" in e for e in errors), errors)

    def test_existing_audit_application_preserves_history(self):
        for unit in {a["unit"] for a in LEDGER}:
            selected = [a for a in LEDGER if a["unit"] == unit]
            records = [original(selected[0]) for _ in range(max(a["line"] for a in selected))]
            for audit in selected:
                records[audit["line"] - 1] = original(audit)
            with tempfile.TemporaryDirectory() as root:
                path = f"{unit}.jsonl"; write(root, path, records)
                out = Path(root) / "corrected.jsonl"
                result = subprocess.run([sys.executable, "-I", str(ROOT / "tools/views/apply_audit.py"), str(Path(root) / path),
                    "--all", str(ROOT / LEDGER_PATH), "--out", str(out)], text=True, capture_output=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                changed = [json.loads(l) for l in out.read_text().splitlines()]
                for audit in selected:
                    record = changed[audit["line"] - 1]
                    self.assertEqual(record["audit"]["was"]["trait"], audit["trait"])
                    self.assertEqual(record["value"], audit["value"])
                    self.assertEqual(record["source"], original(audit)["source"])

    @unittest.skipUnless(CORPUS, "requires current-main corpus overlay; pass --corpus")
    def test_actual_main_and_compiler_loader(self):
        for audit in LEDGER:
            path = ROOT / f'docs/views/evidence/{audit["unit"]}.jsonl'
            raw = json.loads(path.read_text().splitlines()[audit["line"] - 1])
            self.assertEqual(raw, original(audit))
        job = dict(taxa=["Chelonia"], logs=["docs/views/evidence/desk-d254.jsonl"])
        candidates, _ = C.collect_records(job, str(ROOT / "unused"), {})
        self.assertEqual(len(candidates), 1)
        self.assertTrue(S.ecological(candidates[0]))
        self.assertEqual(candidates[0]["value"], original(LEDGER[0])["value"])
        # Other same-species behavioural evidence is not withdrawn with this DOI.
        tax = G.Tax(); recs, index = G.load_evidence(str(ROOT), tax, set())
        self.assertEqual(G.cell(species(original(LEDGER[0])), "behaviour_vision", "none", index, G.order_evidence(recs), tax, [])["state"], "m")
        choice = [r for r in recs if r["_id"] == "desk-d193#2"]
        self.assertEqual(len(choice), 1)
        self.assertTrue(S.supports_trait(choice[0], "behaviour_vision"))


if __name__ == "__main__":
    unittest.main()
