#!/usr/bin/env python3
"""Read-only completeness gate; never a scientific correctness classifier.

python3 -I tools/views/scientific_preflight.py candidates.jsonl --template
python3 -I tools/views/scientific_preflight.py candidates.jsonl --review review.jsonl
See docs/tracks/prompts/scientific-preflight.md. No existing evidence is migrated.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def digest(record):
    data = json.dumps(record, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def source_key(record):
    source = record.get("source")
    if not isinstance(source, dict):
        return ""
    value = source.get("doi") or source.get("url")
    return value.strip() if isinstance(value, str) else ""


def text(value):
    return isinstance(value, str) and bool(value.strip())


def text_list(value, nonempty=False):
    return (isinstance(value, list) and (bool(value) or not nonempty)
            and all(text(item) for item in value))


def read_jsonl(path):
    rows = {}
    for line, raw in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw, parse_constant=lambda s: (_ for _ in ()).throw(ValueError(s)))
        except ValueError as exc:
            raise ValueError(f"{path}:{line}: invalid JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{line}: expected JSON object")
        rows[line] = row
    return rows


def template(records):
    papers = {}
    for line, record in records.items():
        key = source_key(record)
        if not key:
            raise ValueError(f"candidate line {line}: missing source DOI/URL")
        paper = papers.setdefault(key, {
            "source": key,
            "access": {"kind": "", "inspected": [], "unavailable": []},
            "design": "", "metrics": "", "results": [], "reconciliation": "",
            "records": [],
        })
        paper["records"].append({"line": line, "sha256": digest(record),
                                 "decision": "hold", "claim_check": "", "limitation": ""})
    return list(papers.values())


def problems(records, reviews):
    errors, seen = [], set()
    for n, paper in enumerate(reviews, 1):
        label = f"review {n}"
        if not isinstance(paper, dict):
            errors.append(f"{label}: expected object")
            continue
        for field in ("source", "design", "metrics", "reconciliation"):
            if not text(paper.get(field)):
                errors.append(f"{label}: missing {field}")
        access = paper.get("access")
        if not isinstance(access, dict):
            access = {}
        kind = access.get("kind")
        if kind not in ("full_text", "abstract_only", "incomplete"):
            errors.append(f"{label}: invalid access.kind")
        if not text_list(access.get("inspected"), nonempty=True):
            errors.append(f"{label}: name the source sections actually inspected")
        gaps = access.get("unavailable")
        if not text_list(gaps, nonempty=kind in ("abstract_only", "incomplete")):
            errors.append(f"{label}: list unavailable material and reasons")
        if kind == "full_text" and gaps:
            errors.append(f"{label}: use incomplete for relevant unread material")
        results = paper.get("results")
        if not isinstance(results, list) or not results:
            errors.append(f"{label}: missing located results")
        else:
            for result in results:
                if (not isinstance(result, dict) or not text(result.get("where"))
                        or not text(result.get("finding"))):
                    errors.append(f"{label}: each result needs where and finding")
        entries = paper.get("records")
        if not isinstance(entries, list) or not entries:
            errors.append(f"{label}: missing record receipts")
            continue
        for entry in entries:
            if not isinstance(entry, dict):
                errors.append(f"{label}: record receipt must be an object")
                continue
            line = entry.get("line")
            if type(line) is not int or line not in records:
                errors.append(f"{label}: unknown candidate line {line!r}")
                continue
            loc = f"{label}, candidate line {line}"
            if line in seen:
                errors.append(f"{loc}: duplicate receipt")
            seen.add(line)
            record = records[line]
            if not source_key(record) or paper.get("source") != source_key(record):
                errors.append(f"{loc}: source mismatch")
            if entry.get("sha256") != digest(record):
                errors.append(f"{loc}: stale record; reread changes before renewing receipt")
            decision = entry.get("decision")
            if decision not in ("ready", "limited"):
                errors.append(f"{loc}: held or undecided; exclude from submission")
            if not text(entry.get("claim_check")):
                errors.append(f"{loc}: missing final claim check")
            if kind in ("abstract_only", "incomplete") and decision != "limited":
                errors.append(f"{loc}: restricted access requires limited decision")
            if decision == "limited":
                limitation = entry.get("limitation")
                if not text(limitation) or not any(
                    isinstance(record.get(field), str) and limitation in record[field]
                    for field in ("note", "conditions")
                ):
                    errors.append(f"{loc}: preserve the exact limitation in note or conditions")
            source = record.get("source")
            if not isinstance(source, dict):
                source = {}
            if kind == "abstract_only" and (
                source.get("access") != "abstract" or record.get("partial") is not True
            ):
                errors.append(f"{loc}: abstract-only needs source.access=abstract and partial=true")
            if source.get("access") == "abstract" and kind != "abstract_only":
                errors.append(f"{loc}: abstract-only source requires abstract_only review")
    for line in records.keys() - seen:
        errors.append(f"candidate line {line}: missing scientific review")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidates")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--template", action="store_true")
    action.add_argument("--review")
    args = parser.parse_args()
    try:
        records = read_jsonl(args.candidates)
        if args.template:
            for row in template(records):
                print(json.dumps(row, ensure_ascii=False))
            return 0
        errors = problems(records, list(read_jsonl(args.review).values()))
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    for error in errors:
        print(error)
    print(f"{len(records)} candidate records; {len(errors)} preflight problems. "
          "Checks documentation only; scientific correctness requires independent audit.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
