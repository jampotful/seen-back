#!/usr/bin/env python3
"""python3 -I tools/views/test_voice_check.py : checks tools/views/voice_check.py on sentences that break each rule, on sentences that
do not, and on the fifteen example rows of docs/views/VOICE.md, which must come out clean."""
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import voice_check as vc  # noqa: E402


def rules(text, grade=None):
    return sorted({r for r, _ in vc.check_text(text, grade)})


def has(text, rule, grade=None):
    assert rule in rules(text, grade), (rule, text, vc.check_text(text, grade))


def lacks(text, rule, grade=None):
    assert rule not in rules(text, grade), (rule, text, vc.check_text(text, grade))


# humans
has("A human sees less than people do.", "humans")
has("What a person sees is blurred.", "humans")
has("A person’s eye is round.", "humans")
lacks("A human sees about 30 cycles a degree.", "humans")
lacks("Humans stop seeing flicker at about 60 flashes a second.", "humans")

# the app
has("This view bends the picture at its edges.", "app")
has("A phone camera sees less than a quarter of that.", "app")
has("You see more. The screen shows a violet tint.", "app")
has("Your eyes face forward. Tap the screen to move the focus.", "app")
has("With &draw=air the view shows breath.", "app")
has("You see a wide field. The camera cannot match it.", "app")
lacks("Your field of view is about 300 degrees.", "app")
lacks("An eastern red-eared slider has camera-type eyes and filter pigments that tint its lens.", "app")
lacks("You see all the way around you without turning your head.", "app")
has("Your eyes sit on the sides of your head. The picture is drawn to suggest it.", "app")

# the words of rule 4
has("Your cells answer to blue light.", "voice_words")
has("Your eyes report the brightness.", "voice_words")
lacks("Your cells sense blue light.", "voice_words")

# the owner's banned words
for w in ["Your eye is a testament to evolution.", "Vision is crucial to you.", "You navigate by sight.", "The rich colors help you.",
          "A myriad of cells line your retina.", "It's worth noting that you see blue.", "You leverage motion.", "The interplay of rods and cones matters.",
          "Light is woven into the picture.", "You are deeply sensitive to blue."]:
    has(w, "banned")
lacks("Your lens focuses light on the retina.", "banned")
lacks("You see a vivid blue.", "banned")

# not X, but Y and its relatives
has("Your eyes are for movement, not detail.", "contrast")
has("You do not see red, but you see blue.", "contrast")
has("It is not a blur but a sharp strip.", "contrast")
has("It isn't a slit, it's a circle.", "contrast")
has("You see not only blue but also green.", "contrast")
has("You sense light, not shapes.", "contrast")
lacks("You do not have a fovea.", "contrast")
lacks("Nobody has measured how sharply you see.", "contrast")
lacks("You see blue and green, where a human sees blue, green and red.", "contrast")

# fragments
has("Eight eyes. You have eight eyes.", "fragment")
has("You turn to face it. Because of the front eyes.", "fragment")
has("An upright strip of cells.", "fragment")
lacks("You have eight eyes.", "fragment")
lacks("Nobody yet knows how your brain combines what your eyes see.", "fragment")
lacks("If something knocks you over, your stem bends until its top points straight up again within a few hours.", "fragment")

# spelling
has("You see color and colour.", "spelling")
has("Your eye is about a millimetre wide.", "spelling")
has("A grey heron stands still.", "spelling")
has("You recognise movement.", "spelling")
has("Your pupil is centred.", "spelling")
has("Slime mould grows toward food.", "spelling")
lacks("You see color and gray.", "spelling")
lacks("Your eye is about a millimeter wide and you exercise caution near a porpoise.", "spelling")
lacks("A mold grows toward food at the center of the dish.", "spelling")

# length
has("One. Two. Three. Four.", "length")
lacks("You see well. You see far. You see in the dark.", "length")
lacks("A peak near 4.9 in e.g. a sparrow is low. You see less.", "length")

# numbers
has("Your cones peak at 437 nanometers.", "numbers")
has("A sparrow reads 4.9 cycles a degree.", "numbers")
has("It follows flicker up to 108 times a second.", "numbers")
lacks("You can see flicker even when it flashes 200 times a second, where a human stops at about 60.", "numbers")
lacks("Your strip is about 10 degrees wide and two or three times as tall.", "numbers")

# dashes, hedges, grade words
has("You see blue — and green.", "dash")
has("Studies suggest you see blue.", "hedge")
has("This is a remarkable eye.", "hedge")
has("You see blue!", "hedge")
has("Deer see two colors, and you see them too.", "grade_words", "g")
lacks("Deer see two colors, and you very likely do too.", "grade_words", "g")
has("Your eyes see two colors.", "grade_words", "i")
lacks("Nobody has measured how sharply you see.", "grade_words", "i")
lacks("Your eyes see two colors.", "grade_words", "m")

# the fifteen example rows of VOICE.md are clean
voice = open(os.path.join(HERE, "..", "..", "docs", "views", "VOICE.md"), encoding="utf-8").read()
examples = re.findall(r"^- `([mgix])` (.+)$", voice, re.M)
assert len(examples) == 15, len(examples)
for grade, body in examples:
    title, text = body.split(". ", 1)
    found = vc.check_text(text, grade, title)
    assert not found, (grade, body, found)

# a small directory of views: counts, one count for a row held twice, and the report block
with tempfile.TemporaryDirectory() as d:
    import json
    spec = {"key": "t", "rows": [["m", "A", "A person sees well."], ["m", "B", "You see well."]],
            "trial": {"rows": [["m", "A", "A person sees well."], ["m", "C", "You see colour."]]}}
    json.dump(spec, open(os.path.join(d, "t.json"), "w"))
    json.dump([], open(os.path.join(d, "index.json"), "w"))
    views = vc.load_views(d)
    assert list(views) == ["t"]
    findings, n = vc.check_views(views)
    assert n == 3, n                                         # the row held twice counts once
    assert sorted(f["rule"] for f in findings) == ["humans", "spelling"], findings
    report = os.path.join(d, "REPORT.md")
    vc.write_block(report, "voice-check", vc.markdown(findings, n, views))
    vc.write_block(report, "other", "kept\n")
    vc.write_block(report, "voice-check", vc.markdown([], n, views))
    text = open(report).read()
    assert text.count("<!-- voice-check:start -->") == 1 and "kept" in text and "break at least one rule" in text

print("test_voice_check: ok")
