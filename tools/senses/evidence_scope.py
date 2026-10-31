"""Claim scope is independent of taxonomic grade and source completeness.

See docs/views/research/SENSORY-ANATOMY.md. No method-word guessing: legacy
restrictions are reviewed, fingerprinted annotations, not rewritten records.
"""
import hashlib
import json
from pathlib import Path

ANATOMY = "sensory_anatomy"
ANATOMICAL = frozenset(("anatomical_presence", "anatomical_measurement"))
NONFUNCTIONAL = ANATOMICAL | {"mechanical_response", "inferred_function"}
KINDS = NONFUNCTIONAL | {"transduction", "physiological_response", "behavioural_response"}
RULES = """Sensory evidence has a claim scope separate from m/g/i/x. sensory_anatomy
records support only the named structure and measurement. Organ counts, passive
deflection and inferred function do not establish hearing, airflow, vibration or
other detection. Transduction establishes the recorded physiological response;
behaviour establishes the tested response, including nulls, not subjective
experience. Never transfer a modality from an organ's name or a related species.
An anatomy-grounded drawing is an invention: grade i, invented true, with the
anatomical basis and the untested functional assumption stated separately.
Read evidence_kind and sensory_use_limit even when a record is graded m.
"""


def functional_trait(trait):
    return trait.startswith("sense_") or trait == "behaviour_vision"


def fingerprint(record):
    """Match scientific content across raw and audit-corrected copies, not line offsets."""
    fields = {k: record.get(k) for k in ("taxon", "trait", "value", "units", "method", "conditions", "quote")}
    fields["doi"] = (record.get("source") or {}).get("doi", "")
    return hashlib.sha256(json.dumps(fields, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def load_limits(root):
    path = Path(root) / "docs/views/sensory-use-limits.jsonl"
    if not path.exists():
        return {}
    limits = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        limits[entry["fingerprint"]] = entry
    return limits


def apply_limit(record, limits):
    """A use restriction is not scientific acceptance or a replacement of the finding."""
    entry = limits.get(fingerprint(record))
    if entry:
        record = dict(record, sensory_use_limit=entry["reason"])
    return record


def restricted(record):
    kind = record.get("evidence_kind")
    return (record.get("trait") == ANATOMY or bool(record.get("sensory_use_limit"))
            or kind in {"mechanical_response", "inferred_function"}
            or (functional_trait(record.get("trait", "")) and kind in ANATOMICAL)
            or (kind is not None and kind not in KINDS))


def supports_trait(record, trait):
    """Legacy untyped records retain their status unless a reviewed limit applies."""
    actual = record.get("_trait", record.get("trait"))
    return actual == trait and not (functional_trait(trait) and restricted(record))


def problems(record):
    out = []
    kind = record.get("evidence_kind")
    trait = record.get("trait", "")
    if kind is not None and kind not in KINDS:
        out.append("unknown evidence_kind %r" % kind)
    if trait == ANATOMY:
        if kind not in ANATOMICAL:
            out.append("sensory_anatomy requires anatomical_presence or anatomical_measurement")
        for field in ("structure", "measurement", "method", "conditions"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                out.append("sensory_anatomy needs %s" % field)
        if kind == "anatomical_measurement" and not record.get("units"):
            out.append("anatomical_measurement needs units")
    if functional_trait(trait) and kind in ANATOMICAL:
        out.append("anatomy belongs in sensory_anatomy, not a functional trait")
    return out
