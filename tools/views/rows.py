#!/usr/bin/env python3
"""The rows pipeline (burst 10): draft the rows of a view from the audited evidence, one request to Claude for each row, and check every draft.

    python3 -I tools/views/rows.py plan  --views bird,insect --out out            # builds the requests and prices them; calls nothing
    python3 -I tools/views/rows.py run   --views bird,insect --out out            # needs ANTHROPIC_API_KEY; batch, direct with --direct
    python3 -I tools/views/rows.py apply --views bird,insect --from out           # writes the drafts into views/<key>.json as `rows_draft`
    python3 -I tools/views/rows.py report --from out                              # writes docs/views/voice/REPORT.md (the pipeline block)
    python3 -I tools/views/rows.py report --from out --block rows-try               # the block for the views behind ?try=

What a row is. A view has rows (rows.json of the gap table, docs/views/gaps/rows.json, for the fourteen offered views, and the SLOTS below
for the jumping spider and the spiders, docs/views/gaps/try-rows.json for the other views behind ?try=, whose species are in
docs/views/gaps/try-species.json, written by tools/views/try_species.py): a title and the evidence traits it rests on. For each row the script
  1. reads the evidence logs with the audit applied (docs/views/audit/corrected/<unit>.jsonl, which holds the corrections and the burst 9
     decisions of tools/views/audit_rule.py, docs/views/audit/decisions.jsonl, and drops the retracted records), and the logs of
     docs/views/evidence that were not audited as units;
  2. takes the species that borrow the view (the gap table's cells, docs/views/gaps/cells.jsonl; the county list for spiders);
  3. computes the grade of every species for every trait by the carry rules of docs/views/research/BRIEF.md ("Round 2"), with the
     research desk's own function (gaps.cell): m measured in that species, g carried by rule 2 or 3, i otherwise (numbers never travel);
     the row's grade for a species is the lowest of its traits, and the row's grade for the view is the one that most of the species'
     records fall under;
  4. sends Claude the species, their grades, the records behind them and docs/views/VOICE.md with its fifteen example rows (the system
     part, cached), and asks for one to three sentences and the records the sentences rest on.
Every draft must pass tools/views/voice_check.py and a check that each number in it appears in a record it cites, for a species of the
view or its relative; a draft that fails is sent once more with the errors, and what still fails is listed. The drafts go to a
`rows_draft` block in the view's JSON and never over the live rows.
"""
import argparse
import collections
import csv
import datetime
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


GAPS = _load("gaps", os.path.join(HERE, "gaps.py"))
VC = _load("voice_check", os.path.join(HERE, "voice_check.py"))
EX = _load("lit_extract", os.path.join(ROOT, "tools", "lit", "extract.py"))

MAX_SPECIES = 32              # species lines in a request
SHOW_SPECIES = 20             # of them the most recorded; the rest are the measured or carried species that follow
MAX_RECORDS = 30              # records in a request
MAX_TOKENS = 3000
MODEL = "claude-sonnet-5-5"
DEFAULT_VIEWS = "bird,insect,spider,jumper,dog,cat,bee,plant"
HUMAN_OK = {60, 30}           # a human's flicker limit and sharpness on a chart, allowed when the text says "human"

# Rows of the views that rows.json does not cover. A title and the evidence traits it rests on.
SLOTS = {
    "jumper": collections.OrderedDict([
        ("Eyes", ["eyes_count", "eye_role", "eye_type"]),
        ("Sharpness", ["acuity_cpd", "interreceptor_deg"]),
        ("Field of view", ["fov_h_deg", "fov_v_deg", "binocular_deg"]),
        ("Eye movement", ["eye_movement", "fovea"]),
        ("Color", ["receptor_classes", "lambda_max_nm", "colour_vision", "spectral_range_nm"]),
        ("Movement", ["motion", "behaviour_vision"]),
        ("Vibration and sound", ["sense_vibration", "sense_hearing"]),
    ]),
    "spider": collections.OrderedDict([
        ("Eyes", ["eyes_count", "eye_type", "eye_role"]),
        ("Sharpness", ["acuity_cpd", "interreceptor_deg"]),
        ("Pace", ["cff_hz"]),
        ("Dim light", ["tapetum", "absolute_sensitivity"]),
        ("Color", ["receptor_classes", "lambda_max_nm", "colour_vision"]),
        ("The web", ["sense_vibration", "sense_airflow"]),
    ]),
}
# Rows of the live views that describe how the app draws something and not the animal, which a row must never do (VOICE.md, rule 3).
SKIP_ROWS = {("bee", "How the colours are shown")}
US_TITLES = (("Colour", "Color"), ("colour", "color"), ("Neighbours", "Neighbors"), ("neighbours", "neighbors"))
WHO = {"jumper": "a jumping spider", "spider": "a spider other than a jumping spider"}
TRY_ROWS = os.path.join("docs", "views", "gaps", "try-rows.json")
TRY_SPECIES = os.path.join("docs", "views", "gaps", "try-species.json")
_TRY = {}


def try_file(root, rel):
    """The rows or species file of the views behind ?try= (empty when missing), read once."""
    key = (root, rel)
    if key not in _TRY:
        p = os.path.join(root, rel)
        _TRY[key] = json.load(open(p, encoding="utf-8")).get("views", {}) if os.path.exists(p) else {}
    return _TRY[key]


# ---------------------------------------------------------------- the evidence, audit applied

def evidence_files(root):
    """[(unit, path)] : the corrected copies of the audited logs, then the logs of docs/views/evidence that are not among them."""
    out, seen = [], set()
    cdir = os.path.join(root, "docs", "views", "audit", "corrected")
    for f in sorted(os.listdir(cdir)) if os.path.isdir(cdir) else []:
        if f.endswith(".jsonl") and not f.endswith("-failed.jsonl"):
            out.append((f[:-6], os.path.join(cdir, f)))
            seen.add(f[:-6])
    edir = os.path.join(root, "docs", "views", "evidence")
    for f in sorted(os.listdir(edir)) if os.path.isdir(edir) else []:
        if f.endswith(".jsonl") and not f.endswith("-failed.jsonl") and f[:-6] not in seen:
            out.append((f[:-6], os.path.join(edir, f)))
    return out


def read_fixes(root):
    """{"<unit>:<line>": {"partial": True}} from docs/views/fixes/*.jsonl, the same file gaps.py reads (the evidence files stay as written)."""
    fixes = {}
    fxdir = os.path.join(root, "docs", "views", "fixes")
    for f in sorted(os.listdir(fxdir)) if os.path.isdir(fxdir) else []:
        if f.endswith(".jsonl"):
            for line in open(os.path.join(fxdir, f), encoding="utf-8"):
                try:
                    fx = json.loads(line)
                except ValueError:
                    continue
                if isinstance(fx, dict) and fx.get("id"):
                    fixes.setdefault(fx["id"], {}).update({k: v for k, v in fx.items() if k == "partial"})
    return fixes


def read_retracted(root):
    """{"<unit>:<line>"} the audit retracted (docs/views/audit/ALL.jsonl). The corrected copies already leave them out; a log that was
    not audited as a unit is read as written, so its retracted lines (a recheck's corrected copy supersedes the original) are dropped here."""
    out = set()
    p = os.path.join(root, "docs", "views", "audit", "ALL.jsonl")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            try:
                v = json.loads(line)
            except ValueError:
                continue
            if isinstance(v, dict) and v.get("verdict") == "retract":
                out.add("%s:%s" % (v.get("unit"), v.get("line")))
    return out


def load_evidence(root, tax):
    recs = []
    fixes = read_fixes(root)
    retracted = read_retracted(root)
    for unit, path in evidence_files(root):
        raw = os.sep + os.path.join("audit", "corrected") + os.sep not in path
        for n, line in enumerate(open(path, encoding="utf-8"), 1):
            line = line.strip()
            if not line:
                continue
            if raw and "%s:%d" % (unit, n) in retracted:
                continue
            try:
                r = json.loads(line)
            except ValueError:
                continue
            if not isinstance(r, dict) or "trait" not in r:
                continue
            r["_id"] = "%s#%d" % (unit, n)
            r.update(fixes.get("%s:%d" % (unit, n), {}))
            recs.append(r)
    index = collections.defaultdict(list)
    for r in recs:
        trait = GAPS.ALIAS.get(r.get("trait"), r.get("trait"))
        r["_trait"] = trait
        lvl, names, genus = GAPS.parse_taxon(r.get("taxon"), r.get("rank"), r.get("family"), r.get("order"), tax)
        r["_lvl"] = lvl
        if lvl is None:
            continue
        fam, order = r.get("family") or "", r.get("order") or ""
        if lvl == "species":
            tax.add(genus, fam, order)
        r["_names"], r["_genus"] = names, genus
        if lvl == "species":
            for nm in names:
                index[("species", nm, trait)].append(r)
            index[("genus", genus, trait)].append(r)
        elif lvl == "genus":
            index[("genus", genus, trait)].append(r)
        elif lvl == "family":
            index[("family", names[0], trait)].append(r)
        elif lvl == "order":
            index[("order", names[0], trait)].append(r)
        r["_family"] = fam if lvl != "family" else names[0]
        r["_order"] = order if lvl != "order" else names[0]
    recs = [r for r in recs if r["_lvl"]]
    GAPS.FAMILY_INDEX.clear()
    for r in recs:
        if r["_lvl"] in ("species", "genus") and r.get("_family"):
            GAPS.FAMILY_INDEX.setdefault((r["_family"], r["_trait"]), []).append(r)
    return recs, index, GAPS.order_evidence(recs)


def read_carry(root):
    out = []
    p = os.path.join(root, "docs", "views", "carry.jsonl")
    for line in open(p, encoding="utf-8") if os.path.exists(p) else []:
        try:
            e = json.loads(line)
        except ValueError:
            continue
        names = set(re.findall(r"[A-Z][a-z]+(?: [a-z]+)?", e.get("from", "") + " " + e.get("to", "")))
        out.append({"from": e.get("from", ""), "to": e.get("to", ""), "traits": e.get("traits", []), "names": names})
    return out


# ---------------------------------------------------------------- the views, their rows and species

def view_rows(root, view):
    rj = json.load(open(os.path.join(root, "docs", "views", "gaps", "rows.json"), encoding="utf-8"))
    if view in rj["views"] and rj["views"][view]:
        return collections.OrderedDict((t, ts) for t, ts in rj["views"][view].items() if (view, t) not in SKIP_ROWS)
    if view in SLOTS:
        return SLOTS[view]
    return collections.OrderedDict((t, e["traits"]) for t, e in try_file(root, TRY_ROWS)[view].items())


def try_meta(root, view, title):
    """The extra fields of a row of try-rows.json ('live', 'taxa'); empty for the views of rows.json and SLOTS."""
    return try_file(root, TRY_ROWS).get(view, {}).get(title, {})


def row_species(root, view, title, species):
    """The species a row is drafted for: all of the view's, or those in the row's 'taxa' (a genus, family or order list) when it has one."""
    taxa = try_meta(root, view, title).get("taxa")
    if not taxa:
        return species
    rank, names = next(iter(taxa.items()))
    sub = [e for e in species if e.get(rank) in names]
    return sub or species


def live_grade(root, view, title):
    """The grade letter of the live row this row stands for (by its 'live' title, or its own), or None."""
    want = try_meta(root, view, title).get("live", title)
    try:
        rows = json.load(open(os.path.join(root, "views", view + ".json"), encoding="utf-8")).get("rows") or []
    except OSError:
        return None
    for r in rows:
        if r[1] == want:
            return r[0]
    return None


def class_of(root):
    rj = json.load(open(os.path.join(root, "docs", "views", "gaps", "rows.json"), encoding="utf-8"))
    cls = {}
    for c, ts in rj["classes"].items():
        for t in ts:
            cls[t] = c
    return cls


def view_species(root, view, tax):
    """[{sci, en, genus, family, order, records}] most recorded first."""
    out = {}
    if view in ("spider", "jumper"):
        for r in csv.DictReader(open(os.path.join(root, "docs", "views", "no-view-us-fl-alachua.csv"), encoding="utf-8")):
            if r["proposed_view"] != "spider":
                continue
            if (r["family"] == "Salticidae") != (view == "jumper"):
                continue
            genus = r["scientific"].split(" ")[0]
            tax.add(genus, r["family"], r["order"])
            out[r["scientific"]] = {"sci": r["scientific"], "en": r["english"], "genus": genus, "family": r["family"], "order": r["order"],
                                    "records": int(r["records"] or 0)}
    elif view in try_file(root, TRY_SPECIES):
        for e in try_file(root, TRY_SPECIES)[view]:
            tax.add(e["genus"], e["family"], e["order"])
            out[e["sci"]] = {"sci": e["sci"], "en": e["en"], "genus": e["genus"], "family": e["family"], "order": e["order"], "records": int(e["records"] or 0)}
    else:
        for line in open(os.path.join(root, "docs", "views", "gaps", "cells.jsonl"), encoding="utf-8"):
            if '"view": "%s"' % view not in line:
                continue
            r = json.loads(line)
            if r["view"] != view or r["taxon"] in out:
                continue
            tax.add(r["genus"], r["family"], r["order"])
            out[r["taxon"]] = {"sci": r["taxon"], "en": r["en"], "genus": r["genus"], "family": r["family"], "order": r["order"],
                               "records": int(r["records"] or 0)}
    return sorted(out.values(), key=lambda e: (-e["records"], e["sci"]))


GRADE_ORDER = {"m": 0, "g": 1, "i": 2}


def row_state(states):
    return max(states, key=lambda s: GRADE_ORDER.get(s, 2)) if states else "i"


def compute_row(root, view, title, traits, species, index, ord_ev, tax, cls_of, carry_exc):
    """-> dict(grade, weights, species=[{sci,en,records,grade,traits:{trait:(state,level,rule,id)}}], records=[...])"""
    sp_out, pool = [], {}
    for e in species:
        cells = {}
        for t in traits:
            c = GAPS.cell(e, GAPS.ALIAS.get(t, t), cls_of.get(t, "none"), index, ord_ev, tax, carry_exc)
            cells[t] = c
        grade = row_state([c["state"] for c in cells.values()])
        sp_out.append({"sci": e["sci"], "en": e["en"], "genus": e["genus"], "family": e["family"], "order": e["order"], "records": e["records"],
                       "grade": grade, "cells": cells})
    weights = collections.Counter()
    for s in sp_out:
        weights[s["grade"]] += s["records"] or 1
    total = float(sum(weights.values())) or 1.0
    shares = {g: round(weights.get(g, 0) / total, 3) for g in "mgi"}
    top = max("mgi", key=lambda g: (shares[g], -GRADE_ORDER[g]))
    # the records behind the cells: measured cells first, then carried ones, then the closest evidence of cells that nothing carries
    cand = []
    for s in sp_out:
        for t, c in s["cells"].items():
            if c["rec"] is not None:
                cand.append((GRADE_ORDER.get(c["state"], 2), -(s["records"] or 0), c["rec"]["_id"], c["rec"]))
    cand.sort(key=lambda x: x[:3])
    n_i = 0
    for rank, _, rid, rec in cand:
        if len(pool) >= MAX_RECORDS:
            break
        if rid in pool:
            continue
        if rank == 2:
            if n_i >= 6:
                continue
            n_i += 1
        pool[rid] = rec
    picked = sorted(pool.values(), key=lambda r: (GRADE_ORDER.get(r.get("grade"), 3), 0 if r["_lvl"] == "species" else 1, r["_id"]))
    return {"title": title, "traits": traits, "grade": top, "shares": shares, "species": sp_out, "records": picked}


# ---------------------------------------------------------------- the request

def short_source(r):
    s = r.get("source")
    if isinstance(s, dict):
        a = (s.get("authors") or "").split(",")[0].split(" ")[0]
        return ("%s %s" % (a, s.get("year") or "")).strip()
    return str(s or "")[:40]


def record_line(rid, r):
    part = " | PARTIAL (read from a compilation, table, appendix, review or abstract)" if r.get("partial") else ""
    v = json.dumps(r.get("value"), ensure_ascii=False)
    q = " ".join(str(r.get("quote") or "").split())
    return "%s | %s | %s | value %s | eye %s | grade %s | %s | \"%s\" | %s%s" % (
        rid, r.get("taxon"), r.get("_trait"), v[:80], r.get("eye") or "-", r.get("grade"), (r.get("method") or "")[:60], q[:220], short_source(r), part)


def rule_text(c):
    if c["state"] == "m":
        if c.get("rec") is not None and c.get("full") is False:
            return "measured in this species, as a review, table or abstract reports it (partial)"
        return "measured in this species"
    if c["state"] == "g":
        return "carried by %s from a relative" % (c.get("rule") or "a rule")
    return "not measured, and no rule carries it" + (" (%s)" % c["note"] if c.get("note") else "")


def user_text(view, chip, who, row):
    lines = ["VIEW: %s (%s), for readers who are %s." % (chip, view, who),
             "ROW TITLE: %s" % row["title"], "EVIDENCE TRAITS OF THIS ROW: %s" % ", ".join(row["traits"]),
             "GRADE OF THIS ROW FOR THE VIEW: %s (shares of the species' records: measured %.0f%%, carried %.0f%%, unknown %.0f%%)" % (
                 row["grade"], 100 * row["shares"]["m"], 100 * row["shares"]["g"], 100 * row["shares"]["i"]), "",
             "SPECIES that borrow this view, most recorded first, with the row's grade for each:"]
    recs = {r["_id"]: "R%d" % (i + 1) for i, r in enumerate(row["records"])}
    shown = row["species"][:SHOW_SPECIES]
    shown += [s for s in row["species"][SHOW_SPECIES:] if s["grade"] in ("m", "g")][:MAX_SPECIES - SHOW_SPECIES]
    for s in shown:
        parts = []
        for t, c in s["cells"].items():
            rid = recs.get(c["rec"]["_id"]) if c["rec"] is not None else None
            parts.append("%s %s%s" % (t, rule_text(c) if c["state"] != "i" else "unknown", (" [%s]" % rid) if rid and c["state"] != "i" else ""))
        lines.append("- %s (%s), row grade %s: %s" % (s["en"], s["sci"], s["grade"], "; ".join(parts)))
    rest = [s for s in row["species"] if s not in shown]
    if rest:
        c = collections.Counter(s["grade"] for s in rest)
        lines.append("- and %d more species with grades %s" % (len(rest), dict(c)))
    lines += ["", "RECORDS you may cite (id | taxon | trait | value | eye | audited grade | method | quote | source):"]
    for r in row["records"]:
        lines.append(record_line(recs[r["_id"]], r))
    lines += ["", "Write the row now, with the submit_row tool."]
    return "\n".join(lines), {v: k for k, v in recs.items()}


def read_voice():
    return open(os.path.join(ROOT, "docs", "views", "VOICE.md"), encoding="utf-8").read()


SYSTEM_RULES = """You draft one row of a view in Regards, a phone app that shows what the world looks like to an animal. A row is one to three sentences about the animal, spoken to the animal as "you". Your text is read by the animal's species when the app is lent to it, so it must be true of the species listed, at the grade given.

THE VOICE is in the file below. Where this prompt differs from it, the file wins. The fifteen example rows at its end are the target.

HOW THE GRADE SHOWS IN THE WORDS (the owner's decision):
- m: say it plainly, and name the species measured: "If you are a barn owl, ...". A figure measured in one species stays with that species.
- g: name the relatives it comes from and say "you very likely": "Deer, cattle, sheep and horses have two kinds of color-sensing cell, and you very likely have two as well."
- i: say what can be said and say plainly what nobody has measured: "Nobody has measured how sharply you see."
- A record marked PARTIAL was read from a compilation, table, appendix, review or abstract. Say so ("a review reports ...") and give only what it states.
- The grade you are given is the one for the species people meet most. If a few species are measured and most are not, say which are measured.

THE CARRY RULES (so you know what the grades mean): numbers never travel from one species to another; photopigments and the number of color classes may travel within an order; optics, fields, sharpness, flicker speed, the sharp spot and the pupil travel only within a genus.

WHAT YOU MAY USE: only the records you are given. Every number must come from a record you cite, and must belong to the species it is stated for or to the relative you name. Round each number to what a reader can hold (a multiple of 5 or 10 above 20; no decimals), or leave it out when it has no job: comparing with a human, picturing something, or being impressed. A human's flicker limit is about 60 flashes a second and a human reads about 30 cycles a degree on an eye chart. Do not state anything that no record supports. Do not invent species names. A record whose quote does not state the value is not support.

HARD LANGUAGE RULES: US spelling. No em dashes. Never "not X, but Y", "Y, not X" or "it isn't X, it's Y". No sentence fragments. No "people" or "person" for humans: write "human" or "a human". Never mention the app, the phone, the screen, the camera, the view, the picture or how anything is drawn. Say "color", "gray", "center", "meter", "mold". Do not use the words load-bearing, metabolize, delve, tapestry, testament, navigate, underscore, crucial, vital, rich, nuanced, interplay, lens (as a metaphor), boasts, leverage, robust, seamless, realm, landscape, resonates, deeply, profound, myriad, multifaceted, unpack, weave, woven, intricate. No exclamation marks and no vague credits ("studies suggest"). Dry humor is welcome only when a fact is funny on its own.

ANSWER with the submit_row tool: "text" is the row (one to three sentences), "cites" lists the record ids (R1, R2, ...) the sentences rest on, and "note" is one short line for the owner if you had to leave a claim out for lack of a record."""

TOOL = {"name": "submit_row", "description": "Submit the drafted row.",
        "input_schema": {"type": "object", "properties": {
            "text": {"type": "string", "description": "The row: one to three sentences, in the voice."},
            "cites": {"type": "array", "items": {"type": "string"}, "description": "Ids of the records the text rests on, such as R3."},
            "note": {"type": "string", "description": "One short line for the owner, or an empty string."}},
            "required": ["text", "cites"]}}


def system_text():
    return SYSTEM_RULES + "\n\n=== docs/views/VOICE.md ===\n" + read_voice()


def build_request(model, system, user, extra=None):
    msgs = [{"role": "user", "content": user}]
    if extra:
        msgs += extra
    return {"model": model, "max_tokens": MAX_TOKENS,
            "system": [{"type": "text", "text": system, "cache_control": {"type": "ephemeral", "ttl": "1h"}}],
            "tools": [TOOL], "tool_choice": {"type": "auto"}, "messages": msgs}


# ---------------------------------------------------------------- the checks

NUMS = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?![\w])")
WORD_NUMS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}


def numbers_of(x, out):
    if isinstance(x, bool) or x is None:
        return out
    if isinstance(x, (int, float)):
        out.append(float(x))
    elif isinstance(x, (list, tuple)):
        for v in x:
            numbers_of(v, out)
    elif isinstance(x, dict):
        for v in x.values():
            numbers_of(v, out)
    elif isinstance(x, str):
        for m in NUMS.finditer(x):
            out.append(float(m.group(1).replace(",", "")))
    return out


def supported(n, pool):
    for v in pool:
        if abs(n - v) <= max(0.15 * abs(v), 0.51) or (v != 0 and abs(v - n) / abs(v) <= 0.2 and n >= 20):
            return True
        if n == round(v, -1) or n == round(v / 5.0) * 5:
            return True
    return False


def related(rec, species):
    """True when the record's taxon is a listed species or a relative of one (same genus, family or order)."""
    names = set(rec.get("_names") or [])
    for s in species:
        if s["sci"] in names or rec.get("_genus") == s["genus"]:
            return True
        if rec.get("_family") and rec["_family"] == s["family"]:
            return True
        if rec.get("_order") and rec["_order"] == s["order"]:
            return True
    return False


def check_draft(draft, row, ids):
    """-> list of error strings. `ids` maps R-ids to record ids; row holds the records and species that were sent."""
    errs = []
    if not isinstance(draft, dict) or not isinstance(draft.get("text"), str) or not draft["text"].strip():
        return ["no text in the reply"]
    text = draft["text"].strip()
    cites = draft.get("cites") or []
    byid = {r["_id"]: r for r in row["records"]}
    cited = []
    for c in cites:
        rid = ids.get(c)
        if rid is None:
            errs.append("cite %s is not one of the records sent" % c)
        else:
            cited.append(byid[rid])
    for rule, detail in VC.check_text(text, row["grade"], row["title"]):
        errs.append("voice check %s: %s" % (rule, detail))
    pool = []
    for r in cited:
        numbers_of(r.get("value"), pool)
        numbers_of(r.get("quote"), pool)
    human = re.search(r"\bhumans?\b", text, re.I)
    for m in NUMS.finditer(text):
        n = float(m.group(1).replace(",", ""))
        if n <= 10 or (human and n in HUMAN_OK):
            continue
        if not cited:
            errs.append("the number %s has no cited record" % m.group(1))
        elif not supported(n, pool):
            errs.append("the number %s is in none of the cited records" % m.group(1))
    species = row["species"]
    for r in cited:
        if not related(r, species):
            errs.append("cite %s (%s) is neither a species of the view nor a relative of one" % (ids_rev(ids, r["_id"]), r.get("taxon")))
    if row["grade"] == "m" and cited and not any(r.get("grade") == "m" for r in cited):
        errs.append("the row is graded m and none of the cited records is graded m")
    return errs


def ids_rev(ids, rid):
    for k, v in ids.items():
        if v == rid:
            return k
    return rid


# ---------------------------------------------------------------- the jobs

def prepare(root, views):
    tax = GAPS.Tax()
    extra = os.path.join(root, "docs", "views", "gaps", "taxonomy-extra.tsv")
    if os.path.exists(extra):
        for r in csv.DictReader(open(extra, encoding="utf-8"), delimiter="\t"):
            tax.add(r["genus"], r["family"], r["order"])
    species = {v: view_species(root, v, tax) for v in views}
    recs, index, ord_ev = load_evidence(root, tax)
    for v in views:
        for e in species[v]:
            e["genus"] = e["sci"].split(" ")[0]
            e["family"] = e["family"] or tax.family(e["genus"])
            e["order"] = e["order"] or tax.order(e["genus"])
    cls_of = class_of(root)
    carry = read_carry(root)
    jobs = {}
    system = system_text()
    for v in views:
        chip, who = v, WHO.get(v, "an animal of this kind")
        try:
            spec = json.load(open(os.path.join(root, "views", v + ".json"), encoding="utf-8"))
            chip, who = spec.get("chip") or v, spec.get("who") or who
        except OSError:
            pass
        for title, traits in view_rows(root, v).items():
            for old, new in US_TITLES:
                title = title.replace(old, new)
            row = compute_row(root, v, title, traits, row_species(root, v, title, species[v]), index, ord_ev, tax, cls_of, carry)
            user, ids = user_text(v, chip, who, row)
            job = {"view": v, "row": row, "user": user, "ids": ids}
            # a row of a view behind ?try= with no record at all is not sent when the live row claims something (m, g or x): the draft could
            # only say that nobody has measured it, and the live row's sources lie outside the evidence logs
            if not row["records"] and v in try_file(root, TRY_ROWS) and live_grade(root, v, title) in ("m", "g", "x"):
                job["skip"] = "no record of %s for these species or their relatives in the evidence logs; the live row is graded %s" % (
                    ", ".join(traits), live_grade(root, v, title))
            jobs["%s__%s" % (v, re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-"))] = job
    return system, jobs, len(recs)


def est_tokens(s):
    return int(len(s) / 3.2)


def cmd_plan(a):
    system, alljobs, nrec = prepare(ROOT, a.views.split(","))
    jobs = {c: j for c, j in alljobs.items() if not j.get("skip")}
    EX.set_model(a.model)
    est_in = sum(est_tokens(j["user"]) for j in jobs.values())
    cost = (est_tokens(system) * len(jobs) * EX.PRICE["cache_read"] + est_in * EX.PRICE["in"] + len(jobs) * 300 * EX.PRICE["out"]) / 1e6 \
        + est_tokens(system) * EX.PRICE["cache_write_1h"] / 1e6
    os.makedirs(a.out, exist_ok=True)
    lines = ["# Rows plan", "", "%d evidence records read; %d requests (one for each row); system part about %d tokens (cached), user parts %d tokens in all." % (
        nrec, len(jobs), est_tokens(system), est_in), "Estimated cost for %s at batch prices with the cache: $%.2f; the retry of failures is extra, at most the same again." % (a.model, cost), ""]
    for cid, j in jobs.items():
        r = j["row"]
        lines.append("- %s: grade %s, shares %s, %d species, %d records" % (cid, r["grade"], r["shares"], len(r["species"]), len(r["records"])))
    for cid, j in alljobs.items():
        if j.get("skip"):
            lines.append("- %s: not sent (%s)" % (cid, j["skip"]))
    open(os.path.join(a.out, "plan.md"), "w").write("\n".join(lines) + "\n")
    json.dump({cid: {"system_chars": len(system), "user": j["user"]} for cid, j in jobs.items()}, open(os.path.join(a.out, "plan-requests.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\n".join(lines))
    return 0


def reply_of(result):
    r = result.get("result") or {}
    if r.get("type") != "succeeded":
        return None, "request %s" % r.get("type"), {}
    m = r["message"]
    u = m.get("usage", {})
    for b in m.get("content", []):
        if b.get("type") == "tool_use":
            return b["input"], None, u
    return None, "no tool call in the reply", u


def run_requests(reqs, a, work):
    res = {}
    if a.direct:
        for cid, p in reqs.items():
            r = EX.call("POST", "/v1/messages", p)
            res[cid] = reply_of({"result": {"type": "succeeded", "message": r}})
        return res
    r = EX.call("POST", "/v1/messages/batches", {"requests": [{"custom_id": c, "params": p} for c, p in reqs.items()]})
    json.dump({"id": r["id"], "n": len(reqs)}, open(os.path.join(work, "batch.json"), "w"))
    print("submitted batch %s with %d requests" % (r["id"], len(reqs)), flush=True)
    states = EX.wait_for([r["id"]], a.wait_min, every=20)
    if states is None:
        sys.exit("the wait ran out; the batch is %s" % r["id"])
    raw = os.path.join(work, "results-%s.jsonl" % r["id"])
    EX.fetch_results(states, raw)
    for l in open(raw, encoding="utf-8"):
        if l.strip():
            x = json.loads(l)
            res[x["custom_id"]] = reply_of(x)
    return res


def cmd_run(a):
    system, jobs, nrec = prepare(ROOT, a.views.split(","))
    EX.set_model(a.model)
    os.makedirs(a.out, exist_ok=True)
    work = os.path.join(a.out, "_work")
    os.makedirs(work, exist_ok=True)
    spent, results, errors_of, prev = 0.0, {}, {}, {}
    pending = {c for c, j in jobs.items() if not j.get("skip")}
    extra = {}
    for attempt in (1, 2):
        if not pending:
            break
        reqs = {cid: build_request(a.model, system, jobs[cid]["user"], extra.get(cid)) for cid in sorted(pending)}
        est = sum(est_tokens(system) + est_tokens(jobs[c]["user"]) for c in reqs) * EX.PRICE["in"] / 1e6 + len(reqs) * 600 * EX.PRICE["out"] / 1e6
        if spent + est > a.max_usd:
            print("the ceiling estimate $%.2f for attempt %d would pass the limit $%.2f; stopping" % (spent + est, attempt, a.max_usd))
            break
        out = run_requests({"%s__a%d" % (c, attempt): p for c, p in reqs.items()}, a, work)
        nxt = set()
        for rid, (reply, why, usage) in out.items():
            cid = rid.rsplit("__a", 1)[0]
            spent += EX.actual_cost(usage or {})
            j = jobs[cid]
            errs = [why] if reply is None else check_draft(reply, j["row"], j["ids"])
            prev[cid] = {"attempt": attempt, "reply": reply, "errors": errs}
            if errs:
                nxt.add(cid)
                extra[cid] = [{"role": "assistant", "content": "My first draft, as the tool call's input:\n" + json.dumps(reply, ensure_ascii=False)[:6000]},
                              {"role": "user", "content": "That draft failed these checks:\n- " + "\n- ".join(errs[:30]) +
                               "\nCall submit_row again with a corrected row. Fix each error; if a number cannot be supported by a record, leave it out."}]
            else:
                results[cid] = {"attempt": attempt, "reply": reply}
        pending = nxt
    write_outputs(a.out, jobs, results, prev, spent, a.model, nrec)
    sent = sum(1 for j in jobs.values() if not j.get("skip"))
    print("spent $%.4f; %d drafts passed (%d on the first attempt), %d failed, %d rows not sent" % (
        spent, len(results), sum(1 for r in results.values() if r["attempt"] == 1), sent - len(results), len(jobs) - sent))
    return 0


def cite_names(job, cites):
    out = []
    for c in cites:
        rid = job["ids"].get(c)
        r = next((x for x in job["row"]["records"] if x["_id"] == rid), None)
        if r:
            out.append({"id": rid, "taxon": r.get("taxon"), "trait": r["_trait"], "grade": r.get("grade"), "source": short_source(r)})
    return out


def write_outputs(out, jobs, results, prev, spent, model, nrec):
    by_view = collections.defaultdict(lambda: {"rows": [], "failed": [], "skipped": []})
    for cid, j in jobs.items():
        r = j["row"]
        base = {"title": r["title"], "traits": r["traits"], "grade": r["grade"], "shares": r["shares"], "species": len(r["species"])}
        if j.get("skip"):
            by_view[j["view"]]["skipped"].append(dict(base, reason=j["skip"]))
        elif cid in results:
            rep = results[cid]["reply"]
            by_view[j["view"]]["rows"].append(dict(base, text=rep["text"].strip(), cites=cite_names(j, rep.get("cites") or []), note=(rep.get("note") or "").strip(),
                                                   attempt=results[cid]["attempt"]))
        else:
            p = prev.get(cid, {})
            by_view[j["view"]]["failed"].append(dict(base, errors=p.get("errors", ["not sent"]), last=(p.get("reply") or {}).get("text") if isinstance(p.get("reply"), dict) else None))
    stamp = datetime.date.today().isoformat()
    for v, d in by_view.items():
        blob = {"version": 1, "model": model, "made": stamp, "rule": "docs/views/VOICE.md", "rows": d["rows"], "failed": d["failed"]}
        if d["skipped"]:
            blob["skipped"] = d["skipped"]
        json.dump(blob, open(os.path.join(out, "%s.rows_draft.json" % v), "w"), ensure_ascii=False, indent=1)
    json.dump({"spent_usd": round(spent, 4), "model": model, "records_read": nrec, "requests": sum(1 for j in jobs.values() if not j.get("skip")),
               "not_sent": sum(1 for j in jobs.values() if j.get("skip")), "passed": len(results),
               "first_attempt": sum(1 for r in results.values() if r["attempt"] == 1)}, open(os.path.join(out, "stats.json"), "w"), indent=1)


# ---------------------------------------------------------------- apply and report

def indent_of(path):
    for line in open(path, encoding="utf-8").read().split("\n")[1:3]:
        m = re.match(r"^( +)\S", line)
        if m:
            return len(m.group(1))
    return 1


def find_draft(srcs, v):
    for d in srcs.split(","):
        p = os.path.join(d, "%s.rows_draft.json" % v)
        if os.path.exists(p):
            return p
    return None


def cmd_apply(a):
    for v in a.views.split(","):
        src = find_draft(a.src, v)
        if src is None:
            print("no draft for", v)
            continue
        draft = json.load(open(src, encoding="utf-8"))
        draft.pop("failed", None)
        draft.pop("skipped", None)
        path = os.path.join(ROOT, "views", v + ".json")
        raw = open(path, encoding="utf-8").read()
        spec = json.loads(raw)
        spec["rows_draft"] = draft
        out = json.dumps(spec, indent=indent_of(path), ensure_ascii=False)
        open(path, "w", encoding="utf-8").write(out + ("\n" if raw.endswith("\n") else ""))
        print("wrote rows_draft into views/%s.json (%d rows)" % (v, len(draft["rows"])))
    return 0


def live_rows(v):
    spec = json.load(open(os.path.join(ROOT, "views", v + ".json"), encoding="utf-8"))
    return spec.get("rows") or []


def first_attempt_failures(srcs, views):
    """{cid: [errors]} for the first attempts that failed, found again by checking the raw batch replies in each source's _work."""
    system, jobs, nrec = prepare(ROOT, views)
    out = {}
    for d in srcs.split(","):
        w = os.path.join(d, "_work")
        for f in sorted(os.listdir(w)) if os.path.isdir(w) else []:
            if not f.startswith("results-"):
                continue
            for line in open(os.path.join(w, f), encoding="utf-8"):
                if not line.strip():
                    continue
                x = json.loads(line)
                if not x["custom_id"].endswith("__a1"):
                    continue
                cid = x["custom_id"][:-4]
                reply, why, usage = reply_of(x)
                if cid in jobs:
                    out[cid] = [why] if reply is None else check_draft(reply, jobs[cid]["row"], jobs[cid]["ids"])
    return {c: e for c, e in out.items() if e}, jobs


def cmd_report(a):
    dirs = a.src.split(",")
    views = sorted({f[:-len(".rows_draft.json")] for d in dirs for f in os.listdir(d) if f.endswith(".rows_draft.json")},
                   key=lambda v: (v not in DEFAULT_VIEWS.split(","), DEFAULT_VIEWS.split(",").index(v) if v in DEFAULT_VIEWS.split(",") else 0, v))
    spent, nreq, nrec, model = 0.0, 0, "?", "?"
    for d in dirs:
        p = os.path.join(d, "stats.json")
        if os.path.exists(p):
            st = json.load(open(p))
            spent += st.get("spent_usd", 0)
            nreq += st.get("requests", 0)
            nrec, model = st.get("records_read", nrec), st.get("model", model)
    failures, jobs = first_attempt_failures(a.src, views)
    trymode = a.block != "rows-pipeline"
    if trymode:
        lines = ["## Rows pipeline, the views behind ?try= (18 October)", "",
                 "`tools/views/rows.py` drafted %d rows of %d views behind `?try=` with %s, from %s evidence records (the audit and the burst 9 decisions applied). Spent $%.2f at batch prices." % (
                     nreq, len(views), model, nrec, spent), "",
                 "The rows and the traits they rest on are `docs/views/gaps/try-rows.json` (every live row about the animal; rows about the drawing or the app's choices are left out), and the species that borrow each view are `docs/views/gaps/try-species.json` (`tools/views/try_species.py`: the 60 most recorded species of the view's world group or taxa, and the measured species of the view). A row about one group (elephants, chitons) is drafted for that group's species. A row with no evidence record at all is not sent when its live row claims something (graded m, g or x), since the draft could only say that nobody has measured it. A draft passes when `voice_check.py` finds nothing in it, every number in it is in a record it cites, and the records cited belong to a species of the view or a relative of one. A draft that fails is sent once more with the errors; what still fails is listed. The live rows, the `offered` flags and the specs are unchanged.", "",
                 "| view | rows | passed first time | passed after the retry | failed | not sent |", "|---|---:|---:|---:|---:|---:|"]
    else:
        lines = ["## Rows pipeline (burst 10)", "",
                 "`tools/views/rows.py` drafted %d rows of %d views with %s, from %s evidence records (the audit and the burst 9 decisions applied). Spent $%.2f at batch prices." % (
                     nreq, len(views), model, nrec, spent), "",
                 "A draft passes when `voice_check.py` finds nothing in it, every number in it is in a record it cites, and the records cited belong to a species of the view or a relative of one. A draft that fails is sent once more with the errors; what still fails is listed. The first eight views are the ones with the most evidence records; the rest followed.", "",
                 "| view | rows | passed first time | passed after the retry | failed |", "|---|---:|---:|---:|---:|"]
    tot, first8 = collections.Counter(), collections.Counter()
    allrows, failed, skipped = [], [], []
    for v in views:
        d = json.load(open(find_draft(a.src, v)))
        p1 = sum(1 for r in d["rows"] if r["attempt"] == 1)
        p2 = sum(1 for r in d["rows"] if r["attempt"] == 2)
        f = len(d["failed"])
        k = len(d.get("skipped", []))
        if trymode:
            lines.append("| %s | %d | %d | %d | %d | %d |" % (v, p1 + p2 + f, p1, p2, f, k))
        else:
            lines.append("| %s | %d | %d | %d | %d |" % (v, p1 + p2 + f, p1, p2, f))
        for c in (tot, first8) if v in DEFAULT_VIEWS.split(",") and not trymode else (tot,):
            c.update(rows=p1 + p2 + f, p1=p1, p2=p2, f=f, k=k)
        allrows += [(v, r) for r in d["rows"]]
        failed += [(v, r) for r in d["failed"]]
        skipped += [(v, r) for r in d.get("skipped", [])]
    for name, c in ((("all", tot),) if trymode else (("the first eight", first8), ("all", tot))):
        n = max(1, c["rows"])
        if trymode:
            lines.append("| %s | %d | %d (%.0f%%) | %d | %d | %d |" % (name, c["rows"], c["p1"], 100.0 * c["p1"] / n, c["p2"], c["f"], c["k"]))
        else:
            lines.append("| %s | %d | %d (%.0f%%) | %d | %d |" % (name, c["rows"], c["p1"], 100.0 * c["p1"] / n, c["p2"], c["f"]))
    n = max(1, tot["rows"])
    lines += ["", "Pass rate on the first attempt: %.0f%%. After the retry: %.0f%%." % (100.0 * tot["p1"] / n, 100.0 * (tot["p1"] + tot["p2"]) / n), ""]
    if failures:
        lines += ["### Rows that failed the first time, and why", "",
                  "The reasons are found again by checking the batch's first replies with the checker as it stands now, which no longer counts 'slider' (a turtle) or 'camera-type eye' as talk about the app; the reptile row that this fixed still shows as passing only on its second attempt in the counts above.", ""]
        for cid, errs in sorted(failures.items()):
            lines.append("- **%s, %s**: %s" % (jobs[cid]["view"], jobs[cid]["row"]["title"], "; ".join(errs[:5])))
        lines.append("")
    if failed:
        lines += ["### Rows that still fail after the retry", ""]
        for v, r in failed:
            lines.append("- **%s, %s** (grade %s): %s" % (v, r["title"], r["grade"], "; ".join(r["errors"][:6])))
            if r.get("last"):
                lines.append("  - last draft: %s" % r["last"].replace("\n", " "))
        lines.append("")
    else:
        lines += ["No row fails after the retry.", ""]
    if skipped:
        lines += ["### Rows not sent", ""]
        for v, r in skipped:
            lines.append("- **%s, %s**: %s" % (v, r["title"], r["reason"]))
        lines.append("")
    lines += ["### Ten drafts beside the live rows", ""]
    pick = [("bird", "Ultraviolet"), ("cat", "Pupil"), ("cat", "Sharpness"), ("dog", "Color"), ("bee", "Speed"), ("insect", "Ultraviolet"),
            ("jumper", "Color"), ("spider", "The web"), ("plant", "Neighbors"), ("deer", "Field of view")]
    if trymode:
        pick = [("owl", "Sharpness"), ("fox", "Pupil"), ("bat", "Calls"), ("shark", "Electric sense"), ("cephalopod", "Color"), ("tick", "Heat"),
                ("fungus", "Down"), ("crab", "Polarized light"), ("whale", "Sharpness"), ("snail", "Eyes")]
    chosen = [(v, r) for v, t in pick for vv, r in allrows if vv == v and r["title"] == t][:10]
    for v, r in chosen:
        live = live_rows(v)
        want = try_meta(ROOT, v, r["title"]).get("live", r["title"]).lower().replace("colour", "color")
        old = next((x for x in live if x[1].lower().replace("colour", "color")[:5] == want[:5]), None)
        lines += ["**%s, %s** (draft grade `%s`; of the species' records %.0f%% measured, %.0f%% carried, %.0f%% unknown)" % (
            v, r["title"], r["grade"], 100 * r["shares"]["m"], 100 * r["shares"]["g"], 100 * r["shares"]["i"]), "",
            "- Draft: %s" % r["text"], "- Live: %s" % (("`%s` %s: %s" % (old[0], old[1], old[2])) if old else "(no live row with this title)"),
            "- Cites: %s" % ", ".join("%s (%s)" % (c["id"], c["taxon"]) for c in r["cites"]), ""]
    VC.write_block(VC.REPORT, a.block, "\n".join(lines))
    print("wrote", os.path.relpath(VC.REPORT, ROOT))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["plan", "run", "apply", "report"])
    ap.add_argument("--views", default=DEFAULT_VIEWS)
    ap.add_argument("--out", default="out")
    ap.add_argument("--from", dest="src", default="out")
    ap.add_argument("--model", default=os.environ.get("ROWS_MODEL", MODEL))
    ap.add_argument("--direct", action="store_true")
    ap.add_argument("--max-usd", dest="max_usd", type=float, default=float(os.environ.get("ROWS_MAX_USD", "6")))
    ap.add_argument("--wait-min", dest="wait_min", type=int, default=int(os.environ.get("ROWS_WAIT_MIN", "180")))
    ap.add_argument("--block", default="rows-pipeline", help="report: the block of REPORT.md to write (rows-try for the views behind ?try=)")
    a = ap.parse_args()
    return {"plan": cmd_plan, "run": cmd_run, "apply": cmd_apply, "report": cmd_report}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
