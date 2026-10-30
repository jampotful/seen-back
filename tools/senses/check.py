#!/usr/bin/env python3
"""Check evidence logs: python3 -I tools/senses/check.py [docs/views/evidence/<unit>.jsonl ...]

With no arguments, checks every log in docs/views/evidence/. Prints one line per problem and a count per file;
exits 1 if any record has a problem. addlog.py runs the same checks on each record before appending it.
"""
import glob, json, os, sys

NEED = ("taxon", "trait", "value", "source", "where", "quote", "grade")
GRADES = ("m", "g", "i", "x")
TRAITS = {
    "eyes_count", "eye_type", "eye_role", "fov_h_deg", "fov_v_deg", "binocular_deg", "acuity_cpd", "interreceptor_deg",
    "interommatidial_deg", "acceptance_deg", "fovea", "eye_movement", "receptor_classes", "lambda_max_nm",
    "spectral_range_nm", "colour_vision", "oil_droplets", "filter_pigments", "cff_hz", "corner_hz", "f_number",
    "rhabdom_um", "tapetum", "diel", "absolute_sensitivity", "polarization", "depth_cue", "motion",
    "sense_vibration", "sense_airflow", "sense_hearing", "sense_echolocation", "sense_electric", "sense_magnetic",
    "sense_infrared", "sense_thermal", "sense_chemical", "sense_touch", "sense_light_nonvisual", "behaviour_vision",
}
# Evidence length is a word count, not a WebFetch output/character limit.
# Scientific support and faithful quotation also require source review (BRIEF.md).
MAX_QUOTE_WORDS = 40


def problems(r):
    out = []
    miss = [k for k in NEED if k not in r]
    if miss:
        out.append("missing " + ", ".join(miss))
    if r.get("grade") not in GRADES:
        out.append("grade must be one of m, g, i, x")
    t = r.get("trait", "")
    if t not in TRAITS and "new trait" not in str(r.get("note", "")).lower():
        out.append("unknown trait %r (say 'new trait' in note to add one)" % t)
    src = r.get("source")
    if not isinstance(src, dict):
        out.append("source must be an object")
    else:
        if not (src.get("doi") or src.get("url")):
            out.append("source needs a doi or a url")
        if not src.get("authors") or not src.get("year"):
            out.append("source needs authors and year")
        if src.get("access") not in ("open", "abstract", "closed", "book"):
            out.append("source.access must be open, abstract, closed or book")
    q = str(r.get("quote", ""))
    if not q.strip():
        out.append("quote is empty")
    if len(q.split()) > MAX_QUOTE_WORDS:
        out.append("quote is %d words (at most %d)" % (len(q.split()), MAX_QUOTE_WORDS))
    if r.get("opened") is not True and r.get("grade") != "i":
        out.append("opened must be true unless the record is a guess (grade i)")
    return out


def main(paths):
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    paths = paths or sorted(glob.glob(os.path.join(root, "docs", "views", "evidence", "*.jsonl")))
    bad_total = 0
    for p in paths:
        n = bad = 0
        for i, line in enumerate(open(p, encoding="utf-8"), 1):
            if not line.strip():
                continue
            n += 1
            try:
                r = json.loads(line)
            except ValueError as e:
                print("%s:%d not JSON: %s" % (p, i, e)); bad += 1; continue
            for pr in problems(r):
                print("%s:%d %s" % (p, i, pr)); bad += 1
        print("%s: %d records, %d problems" % (os.path.relpath(p, root), n, bad))
        bad_total += bad
    sys.exit(1 if bad_total else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
