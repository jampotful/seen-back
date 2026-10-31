#!/usr/bin/env python3
"""Offline regressions for sensory anatomy, gap/row eligibility and engine claims."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


CHECK = load("scope_check", "tools/senses/check.py")
S = CHECK.SCOPE
G = load("scope_gaps", "tools/views/gaps.py")
R = load("scope_rows", "tools/views/rows.py")
C = load("scope_compile", "tools/views/compile.py")
WASP = [json.loads(line) for line in (ROOT / "docs/views/evidence/anatomy-d208.jsonl").read_text().splitlines()]
SPECIES = dict(sci="Megaphragma viggianii", genus="Megaphragma", family="Trichogrammatidae",
               order="Hymenoptera", view="insect", en="microwasp", records=1)


def write(root, path, records):
    p = Path(root) / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("".join(json.dumps(r) + "\n" for r in records))


class EvidenceScopeTests(unittest.TestCase):
    def test_counts_are_retained_as_four_separate_anatomical_measurements(self):
        self.assertEqual([r["value"] for r in WASP], [19, 95, 5, 20])
        self.assertEqual(len({(r["structure"], r["measurement"]) for r in WASP}), 4)
        for r in WASP:
            self.assertEqual(CHECK.problems(r, require_evidence_kind=True), [])
            self.assertEqual(r["grade"], "m")
            self.assertTrue(r["partial"])
            self.assertTrue(S.restricted(r))

    def test_anatomy_cannot_be_renamed_to_hearing(self):
        r = dict(WASP[0], trait="sense_hearing")
        self.assertIn("anatomy belongs in sensory_anatomy, not a functional trait", CHECK.problems(r))
        self.assertFalse(S.supports_trait(r, "sense_hearing"))
        for missing in ("structure", "measurement", "method", "conditions", "units", "evidence_kind"):
            r = dict(WASP[0]); r.pop(missing)
            self.assertTrue(CHECK.problems(r), missing)

    def test_new_functional_records_need_a_kind_but_legacy_is_readable(self):
        r = dict(WASP[0], trait="sense_hearing"); r.pop("evidence_kind")
        self.assertEqual(CHECK.problems(r), [])
        self.assertIn("new functional records require evidence_kind", CHECK.problems(r, require_evidence_kind=True))
        r["evidence_kind"] = "unknown"
        self.assertTrue(CHECK.problems(r))
        self.assertFalse(S.supports_trait(r, "sense_hearing"))

    def test_gap_remains_open_for_anatomy_mechanics_and_inference(self):
        for kind in S.NONFUNCTIONAL:
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as root:
                # Even a wrongly filed m record cannot close a detection gap.
                write(root, "docs/views/evidence/test.jsonl", [dict(WASP[0], trait="sense_hearing", evidence_kind=kind)])
                tax = G.Tax(); recs, index = G.load_evidence(root, tax, set())
                cell = G.cell(SPECIES, "sense_hearing", "order", index, G.order_evidence(recs), tax, [])
                self.assertEqual(cell["state"], "i")

    def test_transduction_and_behaviour_can_support_their_own_trait(self):
        for kind in ("transduction", "physiological_response", "behavioural_response"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as root:
                write(root, "docs/views/evidence/test.jsonl", [dict(WASP[0], trait="sense_hearing", evidence_kind=kind)])
                tax = G.Tax(); recs, index = G.load_evidence(root, tax, set())
                cell = G.cell(SPECIES, "sense_hearing", "none", index, G.order_evidence(recs), tax, [])
                self.assertEqual(cell["state"], "m")
                self.assertFalse(S.supports_trait(recs[0], "sense_airflow"))

    def test_anatomy_cannot_close_senses_or_travel_to_congeners(self):
        with tempfile.TemporaryDirectory() as root:
            write(root, "docs/views/evidence/test.jsonl", WASP)
            tax = G.Tax(); recs, index = G.load_evidence(root, tax, set())
            oe = G.order_evidence(recs)
            for trait in ("sense_hearing", "sense_airflow", "sense_vibration"):
                self.assertEqual(G.cell(SPECIES, trait, "none", index, oe, tax, [])["state"], "i")
            self.assertEqual(G.cell(SPECIES, S.ANATOMY, "none", index, oe, tax, [])["state"], "m")
            relative = dict(SPECIES, sci="Megaphragma mymaripenne")
            self.assertEqual(G.cell(relative, S.ANATOMY, "order", index, oe, tax, [])["state"], "i")

    def test_restrictions_block_genus_and_order_paths(self):
        with tempfile.TemporaryDirectory() as root:
            examples = [dict(WASP[0], trait="sense_airflow", evidence_kind="mechanical_response",
                             taxon="Megaphragma other"),
                        dict(WASP[0], trait="sense_airflow", evidence_kind="anatomical_measurement",
                             taxon="Apis mellifera", family="Apidae")]
            write(root, "docs/views/evidence/test.jsonl", examples)
            tax = G.Tax(); recs, index = G.load_evidence(root, tax, set())
            for cls in ("genus", "order"):
                self.assertEqual(G.cell(SPECIES, "sense_airflow", cls, index, G.order_evidence(recs), tax, [])["state"], "i")

    def test_legacy_limits_match_content_and_preserve_original(self):
        limits = S.load_limits(ROOT)
        self.assertEqual(len(limits), 9)
        for entry in limits.values():
            n = int(entry["id"].split(":")[-1])
            original = json.loads((ROOT / entry["copy"]).read_text().splitlines()[n - 1])
            limited = S.apply_limit(original, limits)
            self.assertTrue(S.restricted(limited))
            self.assertFalse(S.supports_trait(limited, limited["trait"]))
            self.assertNotIn("sensory_use_limit", original)
            self.assertEqual({k: v for k, v in limited.items() if k != "sensory_use_limit"}, original)
            self.assertNotIn("sensory_use_limit", S.apply_limit(dict(original, value="changed finding"), limits))

    def test_limits_applied_to_raw_and_corrected_loaders(self):
        original = dict(WASP[0], trait="sense_hearing"); original.pop("evidence_kind")
        limit = dict(fingerprint=S.fingerprint(original), reason="Anatomical count only")
        with tempfile.TemporaryDirectory() as root:
            write(root, "docs/views/evidence/test.jsonl", [original])
            write(root, "docs/views/audit/corrected/test.jsonl", [original])
            write(root, "docs/views/sensory-use-limits.jsonl", [limit])
            for loader in (G.load_evidence, lambda rt, tx, _: R.load_evidence(rt, tx)[:2]):
                tax = G.Tax(); recs, index = loader(root, tax, set())
                self.assertIn("sensory_use_limit", recs[0])
                self.assertEqual(G.cell(SPECIES, "sense_hearing", "none", index, G.order_evidence(recs), tax, [])["state"], "i")

    def test_functional_row_cannot_cite_anatomy_even_if_given_it(self):
        r = dict(WASP[0], _id="anatomy#1", _trait=S.ANATOMY)
        row = dict(records=[r], traits=["sense_hearing"], grade="m", title="Hearing", species=[SPECIES])
        errors = R.check_draft(dict(text="You hear sounds.", cites=["R1"]), row, {"R1": "anatomy#1"})
        self.assertTrue(any("cannot support a functional row" in e for e in errors))
        row.update(traits=[S.ANATOMY], title="Antennae")
        errors = R.check_draft(dict(text="Your antenna has 19 sensory units.", cites=["R1"]), row, {"R1": "anatomy#1"})
        self.assertFalse(any("cannot support a functional row" in e for e in errors))

    def test_specific_optical_geometry_remains_eligible(self):
        # Existing anatomical optics are not generic sensory_anatomy. Their
        # dedicated trait/parameter mappings and conversion checks still apply.
        r = dict(WASP[0], trait="interommatidial_deg", units="degrees", value=1)
        self.assertFalse(S.restricted(r))
        self.assertTrue(S.supports_trait(r, "interommatidial_deg"))
        self.assertFalse(S.supports_trait(r, "sense_hearing"))

    def test_typed_sensory_row_keeps_full_scientific_context(self):
        # Qualifications can follow a long curve; neither a character limit nor
        # a method prefix is a safe boundary for a scientific claim.
        for kind in ("transduction", "physiological_response", "behavioural_response"):
            r = dict(WASP[0], trait="sense_hearing", _trait="sense_hearing", evidence_kind=kind,
                     method="Experimental protocol. " * 8 + "No behavioural task was tested.",
                     conditions="Underwater pressure; particle motion was not quantified.",
                     note="Reported curve and sample counts. " * 20 + "Historic species identity is unresolved.",
                     where="Table 1, specified species column; Methods.",
                     quote=("A complete qualifying sentence. " * 10).strip())
            line = R.record_line("R1", r)
            for field in ("method", "conditions", "note", "where", "quote"):
                self.assertIn(r[field], line, (kind, field))

    def test_typed_sensory_compiler_keeps_full_note_and_locator(self):
        r = dict(WASP[0], trait="sense_hearing", evidence_kind="transduction",
                 _id="R1", _inside=True, _audit="not audited",
                 note="Curve, dispersion and frequency-specific N. " * 20 + "No modern-species assignment.",
                 where="Table 1, specified species column; Methods.")
        line = json.loads(C.record_line(r))
        for field in ("method", "conditions", "note", "where", "quote", "evidence_kind"):
            self.assertEqual(line[field], r[field])
        self.assertEqual(line["check"], "not audited")

    def test_compiler_preserves_structure_identity_and_legacy_limits(self):
        a = dict(WASP[0], _inside=True, _from="log", _audit="test")
        b = dict(a, structure="central antennal chordotonal organ")
        self.assertEqual(len(C.choose([a, b])), 2)
        job = dict(taxa=["Hemiscyllium"], logs=["docs/views/audit/corrected/fish-shark.jsonl"])
        candidates, _ = C.collect_records(job, str(ROOT / "unused"), {})
        pore = [r for r in candidates if r.get("trait") == "sense_electric"]
        self.assertTrue(pore)
        self.assertTrue(any(r.get("sensory_use_limit") for r in pore))

    def test_anatomy_cannot_justify_unmapped_engine_parameter(self):
        specs = C.all_specs(); schema = C.schema_facts(specs)
        record = dict(WASP[0], _id="R1", _file="anatomy-d208.jsonl", _inside=True, _audit="test")
        parameter = dict(value=0.19, grade="g", invented=True, src=["R1"])
        reply = dict(spec=dict(key="test", who="a microwasp", chip="Test", cue="Light moves.",
                              params=dict(glow=parameter), rows=[["i", "Drawing", "The glow is invented.", [], ["params.glow"]]],
                              matrices={}, draw={}),
                     claims=[dict(path="params.glow", records=["R1"], kind="calculation", how="19 divided by 100")],
                     quotes=[dict(record="R1", quote=record["quote"])])
        job = dict(key="test", taxa=["Megaphragma"], like="spider")
        errors, *_ = C.check_reply(job, schema, {"R1": record}, copy.deepcopy(reply), specs["spider"], {})
        self.assertTrue(any("cannot establish a measured engine parameter" in e for e in errors))
        reply["spec"]["params"]["glow"].update(grade="i", src=[])
        reply.update(claims=[], quotes=[])
        errors, *_ = C.check_reply(job, schema, {"R1": record}, copy.deepcopy(reply), specs["spider"], {})
        self.assertFalse(any("cannot establish a measured engine parameter" in e for e in errors))
        self.assertIn('"evidence_kind":"anatomical_measurement"', C.record_line(record))
        self.assertIn("untested functional assumption", C.system_text(schema))


if __name__ == "__main__":
    unittest.main()
