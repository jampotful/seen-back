#!/usr/bin/env python3
"""Read-only intake gate: strict for new/changed records, ordinary for legacy.

  python3 -I tools/senses/check_submission.py --base-ref <accepted-main-sha> [paths ...]

Paths are repository-relative evidence or audit/corrected JSONL files. With no
paths, inspect changed and untracked logs. The desk supplies a trusted accepted
main commit, never the candidate's own commit. No classification is inferred.
"""
import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("intake_check", Path(__file__).with_name("check.py"))
CHECK = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CHECK)
PREFIXES = ("docs/views/evidence/", "docs/views/audit/corrected/")


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if result.returncode:
        raise ValueError(result.stderr.strip() or "git command failed")
    return result.stdout


def records(text, label):
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except ValueError as exc:
            raise ValueError(f"{label}:{n}: invalid JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{label}:{n}: record must be an object")
        rows.append((n, row))
    return rows


def identity(row):
    # All fields count, including notes, provenance, audit flags and evidence kind.
    # Whitespace, object-key order and line reordering do not change a record.
    return json.dumps(row, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def compare(current, baseline):
    previous = Counter(identity(row) for _, row in baseline)
    errors, counts = [], Counter()
    for n, row in current:
        key = identity(row)
        legacy = previous[key] > 0
        if legacy:
            previous[key] -= 1
        counts["legacy" if legacy else "new_or_changed"] += 1
        try:
            problems = CHECK.problems(row, require_evidence_kind=not legacy)
        except (TypeError, AttributeError) as exc:
            problems = [f"malformed record fields: {exc}"]
        errors.extend(f"line {n}: {problem}" for problem in problems)
    return errors, counts


def log_path(path):
    p = Path(path)
    return (not p.is_absolute() and ".." not in p.parts and
            path.endswith(".jsonl") and path.startswith(PREFIXES))


def run(root, base_ref, paths):
    base = git(root, "rev-parse", "--verify", "--end-of-options", base_ref + "^{commit}").strip()
    if not paths:
        changed = git(root, "diff", "--name-only", "-z", base, "--", *PREFIXES)
        untracked = git(root, "ls-files", "--others", "--exclude-standard", "-z", "--", *PREFIXES)
        paths = sorted({p for p in (changed + untracked).split("\0") if p and log_path(p)})
    errors, total = [], Counter()
    print(f"intake base: {base}")
    for path in paths:
        if not log_path(path):
            errors.append(f"{path}: expected a repository-relative evidence/corrected JSONL path")
            continue
        try:
            if (root / path).is_symlink():
                raise ValueError("symbolic-link logs are not supported")
            current = records((root / path).read_text(encoding="utf-8"), path)
            exists = git(root, "ls-tree", "--name-only", base, "--", path).strip()
            old = records(git(root, "show", f"{base}:{path}"), f"{base}:{path}") if exists else []
            problems, counts = compare(current, old)
            errors.extend(f"{path}: {p}" for p in problems)
            total.update(counts)
            print(f"{path}: {counts['legacy']} unchanged legacy, {counts['new_or_changed']} new/changed, {len(problems)} problems")
        except (OSError, ValueError) as exc:
            errors.append(f"{path}: {exc}")
    for error in errors:
        print(error)
    print(f"{len(paths)} files; {total['legacy']} unchanged legacy; {total['new_or_changed']} new/changed; {len(errors)} problems")
    return 1 if errors else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-ref", required=True, help="trusted accepted-main SHA recorded at launch/review")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()
    try:
        return run(ROOT, args.base_ref, args.paths)
    except (OSError, ValueError) as exc:
        print(f"intake check failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
