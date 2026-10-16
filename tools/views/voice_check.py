#!/usr/bin/env python3
"""The mechanical voice check: every row of every view against the rules of docs/views/VOICE.md that a script can see.

    python3 -I tools/views/voice_check.py            # prints the counts and writes docs/views/voice/REPORT.md
    python3 -I tools/views/voice_check.py --no-report
    python3 -I tools/views/voice_check.py --view cat --list    # also prints every finding of one view

A row is [grade, title, text, ...] in `rows` or in `trial.rows` of views/<key>.json (a `rows_draft` block holds the drafts of
tools/views/rows.py and is checked by rows.py itself, with this module's `check_text`). A row found in both places counts once.

The rules (the names are the ones in the report):
  humans      the word "people", "person" or "persons" (VOICE 2: humans are "humans" or "a human")
  app         the app, the phone, the screen, the camera, "this view", drawing words, the trial, or a last sentence about the view (VOICE 3)
  voice_words "answers" and "reports" for what cells and eyes do, "responds" is allowed (VOICE 4)
  banned      the owner's list of banned words and phrases (the standing rules), as whole words
  contrast    "not X, but Y" and "Y, not X" and "It isn't X, it's Y" and "not just/only" (VOICE 10)
  fragment    a sentence with no verb that the script knows, by a simple heuristic (VOICE 10)
  spelling    Canadian or British spelling (VOICE 10: US English)
  length      more than three sentences, or none (VOICE 5)
  numbers     a decimal, or a whole number of 20 or more that is not a multiple of 5 or 10 (VOICE 6: round it, or drop it); the script
              cannot see whether a number has a job, so these are the ones to read
  dash        an em dash or an en dash used as one (VOICE 10: rare)
  hedge       a vague credit ("studies suggest"), praise, or an exclamation mark (VOICE 8)
  grade_words a `g` row without "very likely", an `i` row that does not say that nobody knows (VOICE 8)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
REPORT = os.path.join(ROOT, "docs", "views", "voice", "REPORT.md")

RULES = ["humans", "app", "voice_words", "banned", "contrast", "fragment", "spelling", "length", "numbers", "dash", "hedge", "grade_words"]

# ---------------------------------------------------------------- sentences

ABBR = re.compile(r"(?:\b(?:e\.g|i\.e|vs|approx|ca|Dr|Mr|Mrs|St|No|sp|spp|cf|etc|al|fig|Fig|Prof)|\b[A-Z])\.$")


def sentences(text):
    """Split into sentences at . ! ? followed by a space and a capital letter or quote, except after an abbreviation."""
    t = " ".join(str(text).split())
    out, start = [], 0
    for m in re.finditer(r"[.!?][\"')”’]*\s+(?=[\"'(“‘A-Z0-9])", t):
        piece = t[start:m.end()].strip()
        if ABBR.search(piece.rstrip("\"')”’ ")):
            continue
        out.append(piece)
        start = m.end()
    tail = t[start:].strip()
    if tail:
        out.append(tail)
    return out


# ---------------------------------------------------------------- the word lists

HUMANS = re.compile(r"\b(?:people|peoples|persons?|person['’]s|people['’]s|folks?|man|men|woman|women)\b", re.I)
HUMANS = re.compile(r"\b(?:people|peoples|persons?|folks)\b|\bperson['’]s\b|\bpeople['’]s\b", re.I)

APP_WORDS = re.compile(r"\b(?:app|apps|phones?|screens?|cameras?|smartphones?|tap|taps|tapped|tapping|swipe|slider|buttons?|"
                       r"viewer|viewers|views|trial|trials|tuning|panel|pixels?|filters?|draws?|drawn|drawing|drawings|"
                       r"rendered|renders?|simulat\w+|colou?red in|tinted|tint)\b", re.I)
VIEW_WORD = re.compile(r"(?<!field of )(?<!point of )(?<!points of )(?<!in )(?<!line of )\bviews?\b", re.I)
APP_PHRASES = re.compile(r"&draw=|&sense=|\?try=|\bthis view\b|\bthe view\b|\bin this view\b|\bbeing tried\b|\bparam:", re.I)
LAST_ABOUT_VIEW = re.compile(r"\b(?:this view|the view|the app|your phone|the phone|the screen|the picture|this picture|the image|"
                             r"a phone camera|phone cameras?|the camera|draws?|drawn)\b", re.I)

VOICE_WORDS = re.compile(r"\banswers?\b|\breports?\b|\breported\b|\breporting\b|\bthe surround\b", re.I)

BANNED = ["load-bearing", "load bearing", "metabolize", "metabolise", "delve", "delves", "delving", "tapestry", "testament to",
          "navigate", "navigates", "navigating", "underscore", "underscores", "underscored", "crucial", "vital", "rich", "nuanced",
          "interplay", "boasts", "leverage", "leverages", "leveraging", "robust", "seamless", "seamlessly", "realm", "landscape",
          "in the realm of", "it's worth noting", "it’s worth noting", "it's important to note", "it’s important to note",
          "at its core", "speaks to", "resonates", "resonate", "deeply", "profound", "profoundly", "myriad", "multifaceted",
          "ever-evolving", "fast-paced", "dive into", "unpack", "unpacks", "weave", "weaves", "woven", "intricate", "the heart of",
          "genuine", "genuinely", "decorative", "failure mode", "structural", "structurally"]
BANNED_RE = re.compile(r"(?<![\w-])(?:" + "|".join(re.escape(w) for w in sorted(BANNED, key=len, reverse=True)) + r")(?![\w-])", re.I)

# "not X, but Y" in its forms
CONTRAST = [
    re.compile(r"\bnot\b[^.;:!?]{1,100}?[,;]?\s+but\b", re.I),
    re.compile(r"\bnot\s+(?:just|only|merely|simply)\b", re.I),
    re.compile(r"\b(?:is|are|was|were|does|do|did|has|have|can|could|will|would)(?:n['’]t| not)\b[^.;!?]{1,80}[,;]\s*(?:it|they|he|she|this|that|you)(?:['’]s|['’]re| is| are| was| were)?\b", re.I),
    re.compile(r"[,;]\s+not\b", re.I),
    re.compile(r"[,;]\s+never\s+(?:a|an|the)\b", re.I),
    re.compile(r"\binstead of\b", re.I),
]
CONTRAST_NAMES = ["not X, but Y", "not just/only", "isn't X, it's Y", "Y, not X", "Y, never X", "instead of"]

SPELLING_WORDS = ["colour", "colours", "coloured", "colouring", "colourful", "colourless", "discolour", "grey", "greys", "greyish", "greying",
                  "centre", "centres", "centred", "centring", "metre", "metres", "millimetre", "millimetres", "nanometre", "nanometres",
                  "kilometre", "kilometres", "micrometre", "micrometres", "centimetre", "centimetres", "dioptre", "dioptres", "litre", "litres",
                  "fibre", "fibres", "theatre", "behaviour", "behaviours", "behavioural", "favour", "favours", "favourite", "neighbour",
                  "neighbours", "labour", "honour", "flavour", "harbour", "humour", "rumour", "odour", "odours", "vapour", "armour",
                  "defence", "offence", "licence", "mould", "moulds", "moulded", "mouldy", "plough", "sceptic", "sceptical", "tyre",
                  "jewellery", "ageing", "programme", "programmes", "catalogue", "analyse", "analysed", "analyses", "paralyse",
                  "paralysed", "travelled", "travelling", "traveller", "labelled", "labelling", "modelled", "modelling", "signalled",
                  "signalling", "fuelled", "levelled", "cancelled", "totalled", "channelled", "marvellous", "fulfil", "skilful", "enrol",
                  "practise", "practised", "manoeuvre", "manoeuvres", "oestrogen", "haemoglobin", "anaemia", "foetus", "faeces",
                  "encyclopaedia", "paediatric", "diarrhoea", "aluminium", "cosy", "pyjamas", "storey", "whilst", "amongst", "learnt",
                  "spelt", "burnt", "dreamt", "leapt", "spoilt", "artefact", "artefacts", "draught", "grey-scale", "greyscale"]
SPELLING_RE = re.compile(r"\b(?:" + "|".join(SPELLING_WORDS) + r")\b", re.I)
SPELLING_PATTERNS = re.compile(r"\b(?:real|recogn|organ|polar|special|summar|util|emphas|minim|maxim|categor|character|visual|general|normal|"
                               r"stabil|synchron|critic|apolog|memor|sensit|optim|crystall|colon|hypothes|mobil|harmon|author|final|neutral|"
                               r"custom|priorit|familiar|capital|standard|symbol|equal|local|ion|magnet|hyperpolar|depolar|pigment|"
                               r"fertil|steril|energ|ox[iy]d|fossil|bacteri|vaccin|sanit|socia?l|digit|mineral|tranquil)"
                               r"(?:ise|ised|ises|ising|isation|isations)\b|\b(?:an|paral|catal|electrol|hydrol)ys(?:e|ed|es|ing)\b", re.I)
HEDGES = re.compile(r"\b(?:studies (?:suggest|show|indicate|say)|research (?:suggests|shows|indicates)|scientists (?:think|believe|say|suggest)|"
                    r"experts (?:think|believe|say)|it is (?:thought|believed|said)|some say|many believe|researchers (?:think|believe|say)|"
                    r"amazing|amazingly|remarkable|remarkably|incredible|incredibly|astonishing|stunning|wonderful|fascinating|"
                    r"extraordinary|impressive|impressively|marvel\w*|spectacular|awesome)\b", re.I)

AUX = set("""is are was were be been being am have has had do does did can cannot could will would shall should may might must
isn't aren't wasn't weren't hasn't haven't hadn't doesn't don't didn't can't couldn't won't wouldn't shouldn't""".split())
VERBS = set("""see sees saw seen look looks looked watch watches watched sense senses sensed feel feels felt hear hears heard smell smells
find finds found tell tells told turn turns turned take takes took taken make makes made give gives gave given hold holds held keep keeps
kept get gets got go goes went gone come comes came run runs ran move moves moved grow grows grew bend bends bent fall falls fell rise rises
rose peak peaks peaked pick picks picked pack packs packed cover covers covered reach reaches reached lie lies lay lain sit sits sat
stand stands stood close closes closed open opens opened widen widens widened narrow narrows narrowed blur blurs blurred smear smears
smeared fade fades faded crowd crowds crowded track tracks tracked catch catches caught follow follows followed flash flashes flashed
flicker flickers flickered fuse fuses fused stop stops stopped start starts started begin begins began end ends ended need needs needed
use uses used want wants wanted know knows knew known say says said show shows showed shown mean means meant let lets put puts set sets
read reads seem seems seemed become becomes became remain remains remained stay stays stayed lose loses lost lack lacks lacked
carry carries carried contain contains contained hold detect detects detected respond responds responded tell differ differs differed
agree agrees agreed match matches matched measure measures measured guess guesses guessed expect expects expected call calls called
point points pointed face faces faced block blocks blocked pass passes passed let absorb absorbs absorbed reflect reflects reflected
bounce bounces bounced work works worked live lives lived eat eats ate feed feeds fed hunt hunts hunted fly flies flew swim swims
swam crawl crawls crawled climb climbs climbed jump jumps jumped land lands landed hide hides hid rest rests rested sleep sleeps slept
wake wakes woke dive dives dove hang hangs hung drop drops dropped lift lifts lifted press presses pressed push pushes pushed pull pulls
pulled shut shuts drain drains drained brighten brightens brightened darken darkens darkened pool pools pooled sharpen sharpens
sharpened lock locks locked tune tunes tuned scan scans scanned judge judges judged compare compares compared outnumber outnumbers
outnumbered exceed exceeds exceeded cut cuts shape shapes shaped form forms formed rely relies relied depend depends depended
vary varies varied change changes changed shift shifts shifted rotate rotates rotated roll rolls rolled slide slides slid tilt tilts
tilted stretch stretches stretched spread spreads spread sink sinks sank float floats floated glow glows glowed shine shines shone
wiggle wiggles wiggled bob bobs bobbed lurch lurches lurched dart darts darted thrust thrusts search searches searched ask asks asked
think thinks thought believe believes believed learn learns learned remember remembers remembered forget forgets forgot sort sorts
sorted tell lack surround surrounds surrounded fill fills filled leave leaves left enter enters entered exit exits arrive arrives
arrived add adds added build builds built grasp grasps grasped touch touches touched taste tastes tasted echo echoes echoed ring rings
rang click clicks clicked buzz buzzes buzzed beat beats thump thumps thumped bite bites bit sting stings stung grab grabs grabbed
spot spots spotted spit spits dodge dodges dodged chase chases chased freeze freezes froze flee flees fled escape escapes escaped
glide glides glided soar soars soared hover hovers hovered perch perches perched nest nests nested lay lays laid hatch hatches
hatched molt molts molted breathe breathes breathed swallow swallows swallowed digest digests digested drink drinks drank
bloom blooms bloomed open wilt wilts wilted germinate germinates germinated sprout sprouts sprouted reproduce reproduces""".split())

NUM = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+(?:\.\d+)?)(?![\w])")
SPELLED = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}


# ---------------------------------------------------------------- the rules

def _fragments(sents):
    out = []
    for s in sents:
        words = re.findall(r"[A-Za-z’']+", s)
        if not words:
            continue
        low = [w.lower().replace("’", "'") for w in words]
        has_verb = any(w in AUX or w in VERBS or (w.endswith("ed") and len(w) > 4) for w in low)
        if has_verb:
            continue
        # a sentence the script cannot find a verb in: short, or opening with a word that needs a main clause after it
        if len(words) <= 7 or low[0] in ("which", "whose", "where", "when", "while", "although", "because", "since", "unless", "if", "and", "but", "or", "with", "without", "like", "unlike", "as", "so"):
            out.append(s)
    return out


def check_text(text, grade=None, title=None):
    """Return a list of (rule, detail) for one row's text. `grade` is m, g, i or x; `title` is not checked."""
    found = []
    t = " ".join(str(text).split())
    sents = sentences(t)
    for m in HUMANS.finditer(t):
        found.append(("humans", m.group(0)))
    for m in APP_WORDS.finditer(t):
        found.append(("app", m.group(0)))
    for m in VIEW_WORD.finditer(t):
        found.append(("app", m.group(0)))
    for m in APP_PHRASES.finditer(t):
        found.append(("app", m.group(0)))
    if sents and LAST_ABOUT_VIEW.search(sents[-1]) and len(sents) > 1:
        found.append(("app", "last sentence: " + sents[-1][:60]))
    for m in VOICE_WORDS.finditer(t):
        found.append(("voice_words", m.group(0)))
    for m in BANNED_RE.finditer(t):
        found.append(("banned", m.group(0)))
    for s in sents:
        for rx, name in zip(CONTRAST, CONTRAST_NAMES):
            if rx.search(s):
                found.append(("contrast", name + ": " + s[:70]))
                break
    for s in _fragments(sents):
        found.append(("fragment", s[:70]))
    for m in SPELLING_RE.finditer(t):
        found.append(("spelling", m.group(0)))
    for m in SPELLING_PATTERNS.finditer(t):
        if not SPELLING_RE.fullmatch(m.group(0)):
            found.append(("spelling", m.group(0)))
    if len(sents) > 3:
        found.append(("length", "%d sentences" % len(sents)))
    elif not sents:
        found.append(("length", "no sentence"))
    for m in NUM.finditer(t):
        s = m.group(1).replace(",", "")
        v = float(s)
        if "." in s and not re.search(r"\.0+$", s):
            found.append(("numbers", s))
        elif 1900 <= v <= 2100 and re.search(r"\b(?:in|since|by|of)\s+" + s, t):
            continue
        elif v >= 20 and v % 5 != 0:
            found.append(("numbers", s))
    for m in re.finditer("—|–|--", t):
        found.append(("dash", m.group(0)))
    for m in HEDGES.finditer(t):
        found.append(("hedge", m.group(0)))
    if "!" in t:
        found.append(("hedge", "exclamation mark"))
    if grade == "g" and not re.search(r"\bvery likely\b", t, re.I):
        found.append(("grade_words", "a g row without 'very likely'"))
    if grade == "i" and not re.search(r"\b(?:nobody|no one|nothing is known|not known|unknown|no measurement|has not been|have not been|guess)\b", t, re.I):
        found.append(("grade_words", "an i row that does not say that nobody knows"))
    return found


def rows_of(spec):
    """Yield (section, index, row) for the rows of a view spec: its own rows and the rows of its trial block."""
    for i, r in enumerate(spec.get("rows") or []):
        yield "rows", i, r
    for i, r in enumerate((spec.get("trial") or {}).get("rows") or []):
        yield "trial", i, r


def load_views(directory=None):
    d = directory or os.path.join(ROOT, "views")
    out = {}
    for name in sorted(os.listdir(d)):
        if not name.endswith(".json") or name == "index.json":
            continue
        try:
            spec = json.load(open(os.path.join(d, name), encoding="utf-8"))
        except ValueError:
            continue
        if isinstance(spec, dict):
            out[name[:-5]] = spec
    return out


def check_views(views):
    """Return (findings, nrows) where findings is a list of dicts {view, section, index, grade, title, rule, detail, text}.
    A row whose text appears in both `rows` and `trial.rows` of one view is checked once."""
    findings, seen, nrows = [], set(), 0
    for key in sorted(views):
        for section, i, r in rows_of(views[key]):
            if not isinstance(r, list) or len(r) < 3:
                continue
            grade, title, text = r[0], r[1], r[2]
            if (key, text) in seen:
                continue
            seen.add((key, text))
            nrows += 1
            for rule, detail in check_text(text, grade, title):
                findings.append({"view": key, "section": section, "index": i, "grade": grade, "title": title, "rule": rule,
                                 "detail": detail, "text": text})
    return findings, nrows


def tally(findings):
    per_rule, per_view, per_view_rows = {}, {}, {}
    for f in findings:
        per_rule[f["rule"]] = per_rule.get(f["rule"], 0) + 1
        per_view.setdefault(f["view"], {}).setdefault(f["rule"], 0)
        per_view[f["view"]][f["rule"]] += 1
        per_view_rows.setdefault(f["view"], set()).add(f["text"])
    return per_rule, per_view, {k: len(v) for k, v in per_view_rows.items()}


def markdown(findings, nrows, views, label="Voice check"):
    per_rule, per_view, flagged_rows = tally(findings)
    rows_with = len({(f["view"], f["text"]) for f in findings})
    lines = ["## %s" % label, "",
             "`tools/views/voice_check.py` read %d rows in %d views (a row held in both a view's own list and its trial list counts once)." % (nrows, len(views)),
             "%d rows (%.0f%%) break at least one rule that a script can see; %d findings in all." % (rows_with, 100.0 * rows_with / max(1, nrows), len(findings)), "",
             "### By rule", "", "| rule | findings |", "|---|---:|"]
    for r in RULES:
        lines.append("| %s | %d |" % (r, per_rule.get(r, 0)))
    lines += ["", "### By view", "", "| view | rows flagged | " + " | ".join(RULES) + " |", "|---|---:|" + "---:|" * len(RULES)]
    for k in sorted(per_view, key=lambda k: -sum(per_view[k].values())):
        lines.append("| %s | %d | " % (k, flagged_rows.get(k, 0)) + " | ".join(str(per_view[k].get(r, "")) for r in RULES) + " |")
    clean = sorted(set(views) - set(per_view))
    if clean:
        lines += ["", "Views with no finding: " + ", ".join(clean) + "."]
    return "\n".join(lines) + "\n"


def write_block(path, name, body):
    """Put `body` in the file between the markers for `name`, keeping the rest. Creates the file when it is missing."""
    start, end = "<!-- %s:start -->" % name, "<!-- %s:end -->" % name
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else "# The rows pass: voice check and drafts\n\nWritten by `tools/views/voice_check.py` and `tools/views/rows.py`; each tool owns one block.\n"
    block = "%s\n%s%s\n" % (start, body.rstrip("\n") + "\n", end)
    if start in old and end in old:
        new = old[:old.index(start)] + block + old[old.index(end) + len(end) + 1:]
    else:
        new = old.rstrip("\n") + "\n\n" + block
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8").write(new)


def main(argv):
    views = load_views()
    findings, nrows = check_views(views)
    per_rule = tally(findings)[0]
    print("rows read: %d in %d views; findings: %d" % (nrows, len(views), len(findings)))
    for r in RULES:
        print("  %-12s %d" % (r, per_rule.get(r, 0)))
    if "--list" in argv:
        shown = findings
        if "--view" in argv:
            shown = [f for f in findings if f["view"] == argv[argv.index("--view") + 1]]
        for f in shown:
            print("%s %s[%d] %s | %s | %s" % (f["view"], f["section"], f["index"], f["rule"], f["detail"], f["title"]))
    if "--no-report" not in argv:
        write_block(REPORT, "voice-check", markdown(findings, nrows, views))
        print("wrote", os.path.relpath(REPORT, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
