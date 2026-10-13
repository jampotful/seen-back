#!/usr/bin/env python3
"""Burst 5: modules 8 to 11 (field, overlay, sound, haptic) in the specs that use them, and the new specs they unlock.
Usage: python3 -I tools/views/add_modules8.py. Run again safely: each new spec is rewritten whole, each block replaced, rows matched by title.

Sources: the research branches' drafts, read on 13 October 2026. BIRDS is research/birds docs/views/drafts/birds.md, CATDOG is
research/cat-dog docs/views/drafts/cat-dog.md, GROUND is research/ground-invertebrates docs/views/drafts/ground-invertebrates.md.
A parameter is graded only where the draft states the value; everything else is graded i and marked invented."""
import json, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
BIRDS = "research/birds:docs/views/drafts/birds.md"
CATDOG = "research/cat-dog:docs/views/drafts/cat-dog.md"
GROUND = "research/ground-invertebrates:docs/views/drafts/ground-invertebrates.md"


def P(v, rng, note, src=None, grade="i", invented=True):
    o = {"value": v, "grade": grade, "invented": invented, "src": src or [], "floor": None, "note": note}
    if rng:
        o["range"] = rng
    return o


def load(k):
    return json.loads((root / "views" / (k + ".json")).read_text(encoding="utf-8"))


def save(k, s):
    (root / "views" / (k + ".json")).write_text(json.dumps(s, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def put_rows(rows, new):
    titles = {r[1] for r in new}
    return [r for r in rows if r[1] not in titles] + new


def opt(name, note):
    return {"name": name, "invented": True, "note": note}


OFF = lambda what: opt("off", "the view without " + what)
DEUTAN = {"rows": [[0.29275, 0.70725, 0], [0.29275, 0.70725, 0], [-0.02234, 0.02234, 1]], "grade": "g", "invented": True,
          "src": ["Vienot, Brettel and Mollon 1999"], "note": "a person's red-green colour blindness standing in for two cone classes, entered from memory as in the cat view"}

# ---------- module blocks, with their tuning ranges ----------
SOUND_HEAR = lambda: {"k": P(1, [0, 2], "how strongly sound moves the picture"),
                      "dark": P(.12, [0, 1], "how dark the picture rests between sounds"),
                      "flashS": P(.8, [.1, 3], "seconds a sound's light takes to fade"),
                      "steady": P(.4, [0, 1], "how much steady high sound lifts the dark")}
HAP = lambda on, pat: {"on": on, "pattern": P(pat, None, "the vibration pattern in milliseconds, on and off"),
                       "edge": P(1, [0, 1], "how bright the edge pulses where the phone cannot vibrate")}
HAP_DRAW = [OFF("touch"), opt("buzz", "a short vibration where the browser can vibrate (Android), and a pulse at the picture's edge where it cannot (iOS)"),
            opt("edge", "the pulse at the picture's edge only")]

new = {}

# ---------- owl (BIRDS section 2.2) ----------
new["owl"] = {
    "key": "owl", "version": 1, "chip": "Owl", "who": "an owl", "falls_back_to": "bird",
    "applies_to": {"order": ["Strigiformes"]},
    "cue": "Wait in a dim room and make a small sound. Faint, high sounds light the picture for a moment.",
    "modules": ["sound", "haptic"], "draft": True,
    "params": {
        "fov": P(200, [100, 360], "the whole view across", [BIRDS + "#2.2: Potier et al. 2023 (tawny owl)"], "m", False),
        "cpd": P(10, [1, 40], "between the barn owl's 2.6 to 4 and the seven-owl mean of 21.9", [BIRDS + "#2.2: Harmening et al. 2009; Caves et al. 2023"], "i", True),
        "topoA": P(1, [0, 2], "one forward area of sharpest sight", [BIRDS + "#2.2: Hazan et al. 2015"], "m", True),
        "fall": P(1.0, [0, 3], "how fast sharpness falls away from the centre"),
        "pupil": P("o", None, "no source read on owl pupils"),
        "dof": P(12, [0, 40], "no source read on depth of field"),
        "M": P("OWL", None, "the two cone classes", [BIRDS + "#2.2: Hart 2001 (Strix aluco 463, 555)"], "m", True),
        "sat": P(.5, [0, 1.5], "colour muted, since few cones carry coloured oil", [BIRDS + "#2.2: Hart 2001"], "g", True),
        "gain": P(1.8, [1, 3], "shadows brightened for an eye near the limit of dim-light vision", [BIRDS + "#2.2: Martin 1986; Orlowski et al. 2012"], "g", True),
        "sheen": P(0, [0, 1], "no violet or ultraviolet cone", [BIRDS + "#2.2: Wu et al. 2016"], "m", False),
        "rate": P(1, [.25, 2], "no slowing of time", [BIRDS + "#2.2: Potier et al. 2020"], "g", False),
        "persist": P(.1, [0, 1], "short trails behind moving things"),
    },
    "matrices": {"OWL": {"from_pigments": [463, 555], "grade": "m", "invented": True, "src": [BIRDS + "#2.2: Hart 2001"]}},
    "sound": dict(SOUND_HEAR(), say="This view can show faint, high sounds as light, the way an owl finds prey by ear. Tap to let it listen through the microphone. Nothing is recorded or kept."),
    "haptic": HAP("onset", [18]),
    "draw": {"sound": [opt("hear", "the picture rests dark, and each sound lights it from the centre outward, high sounds most (atlas 17)"),
                       opt("rings", "each sound sends a circle out across a picture that stays lit (atlas 17)"), OFF("sound")],
             "haptic": HAP_DRAW},
    "inputs": {"motion": "none", "sound": "optional", "haptic": "optional"},
    "rows": [
        ["m", "Eyes that face forward", "An owl's eyes face forward, so their views overlap across about 45 degrees in front, more than in most birds. Its whole view spans about 200 degrees.", [BIRDS + "#2.2", "Potier et al. 2023", "Martin 2017", "param:fov"]],
        ["m", "Fixed eyes", "An owl's eyes barely move in their sockets, by less than one degree, so the owl turns its whole head to look, as far as about 270 degrees.", [BIRDS + "#2.2", "Potier et al. 2023", "Sieradzki 2022"]],
        ["m", "Sharpness", "A barn owl sees only a fifteenth to a twentieth as much detail as a person does, and other owls measured average about a third. This view is blurred to about a sixth of a person's sharpness, between the two.", [BIRDS + "#2.2", "Harmening et al. 2009", "Caves et al. 2023", "param:cpd"]],
        ["m", "Night vision", "A tawny owl's eye works close to the limit that any vertebrate eye can reach in dim light. This view brightens the shadows.", [BIRDS + "#2.2", "Martin 1986", "Orlowski et al. 2012", "param:gain"]],
        ["m", "Colour", "Owls have lost the colour-sensing cells for violet and ultraviolet light that other birds have, and only about one cone in ten carries a coloured droplet of oil. This view mutes colours.", [BIRDS + "#2.2", "Wu et al. 2016", "Hart 2001", "param:M", "param:sat"]],
        ["m", "Hearing", "Owls can find and catch prey by sound alone. A barn owl hears faint sounds about 20 decibels quieter than other birds can, and hears pitches above 10,000 vibrations a second.", [BIRDS + "#2.2", "Martin 1986", "Manley and Köppl 2025"]],
        ["i", "Being tried: hearing as light", "With the microphone on, the picture rests dark and each sound lights it for a moment, high sounds most. How an owl's hearing feels is unknown, and the drawing is the app's. Where the phone can vibrate it can also buzz with each sound (&draw=buzz).", [BIRDS + "#2.2 new effect 2", "param:sound.dark", "param:sound.flashS", "param:sound.steady", "param:sound.k", "param:haptic.pattern"]],
        ["i", "Guesses", "The pupil, the depth of focus, the trails and how fast sharpness falls from the centre are the app's guesses.", ["param:pupil", "param:dof", "param:persist", "param:fall"]],
        ["x", "Where sounds come from", "A barn owl can place a sound within about 3 degrees side to side and 8 degrees up and down. A phone's microphone cannot tell direction, so this view leaves direction out.", [BIRDS + "#2.2", "Bala et al. 2007"]],
    ],
}

# ---------- duck (BIRDS section 2.4) ----------
new["duck"] = {
    "key": "duck", "version": 1, "chip": "Duck", "who": "a duck", "falls_back_to": "bird",
    "applies_to": {"order": ["Anseriformes"]},
    "cue": "Hold the phone level. The sky above is pressed into the top of the picture, as a duck keeps it in view with its head down.",
    "modules": ["field"], "draft": True,
    "params": {
        "fov": P(360, [180, 360], "all the way around", [BIRDS + "#2.4: Martin 2017; Cantlay et al. 2023"], "m", False),
        "cpd": P(11, [2, 40], "the median bird, standing in for an unmeasured duck", [BIRDS + "#2.4: Caves et al. 2018"], "g", False),
        "pupil": P("o", None, "unchanged"),
        "M": P("DUCK", None, "four cone classes", [BIRDS + "#2.4: Hart 2001 (Anas platyrhynchos 415, 452, 506, 567)"], "m", True),
        "sat": P(1.1, [0, 1.5], "a slight lift for the fourth cone"),
        "sheen": P(0, [0, 1], "the eye blocks most ultraviolet", [BIRDS + "#2.4: Hart 2001 (eye media 370 to 380)"], "m", False),
        "rate": P(.75, [.25, 2], "from pigeon and chicken", [BIRDS + "#2.4: Boström et al. 2016"], "g", True),
    },
    "matrices": {"DUCK": {"from_pigments": [415, 452, 506, 567], "grade": "m", "invented": True, "src": [BIRDS + "#2.4: Hart 2001"]}},
    "remap": {"fold": P(.8, [0, 2], "how much of what lies above the horizon is pressed into the top"),
              "horizon": P(.05, [-.3, .3], "where the fold begins, in screen heights from the middle"),
              "blindAt": P(180, [0, 360], "the blind area's direction, behind the head", [BIRDS + "#2.4: Guillemain et al. 2002"], "g", False),
              "blindDeg": P(20, [0, 120], "the blind area's width; narrow in geese, none in dabbling ducks"),
              "blindSoft": P(6, [0, 30], "the blind area's soft edge"),
              "band": P(.22, [.1, .5], "the ribbon's height in screen heights"),
              "fadeS": P(60, [5, 600], "seconds a direction stays in the ribbon")},
    "draw": {"field": [opt("fold", "the sky above the horizon pressed into the top of the picture (the draft's new effect)"),
                       opt("ribbon", "a band along the bottom keeps every direction the phone has faced, fading with age, so the whole circle a duck sees fills in as you turn"),
                       opt("wedge", "a goose's narrow blind area behind the head, fixed in the room as you turn the phone"),
                       opt("squeeze", "the view without the field options")]},
    "inputs": {"motion": "optional", "sound": "none", "haptic": "none"},
    "rows": [
        ["m", "All the way around", "A mallard sees all the way around itself and over its head. Its two eyes overlap in a narrow strip, about 22 degrees wide, that runs from the bill up over the crown to the back of the head.", [BIRDS + "#2.4", "Cantlay et al. 2023", "Martin 2017", "param:fov"]],
        ["m", "Below the bill", "A dabbling duck cannot see below the level of its bill. Ducks that feed by filtering water find their food by touch instead, with sensitive tips on their bills.", [BIRDS + "#2.4", "Martin 2017", "Cantlay et al. 2023"]],
        ["m", "Geese differ", "Grazing geese and swans can see their bill tip and keep a blind area behind the head, where dabbling ducks see all around. With &draw=wedge and the motion sensors on, the blind area stays behind where you started as you turn.", [BIRDS + "#2.4", "Cantlay et al. 2023", "Guillemain et al. 2002", "param:remap.blindAt"]],
        ["m", "Colour", "Ducks have four kinds of colour-sensing cells, one more than people, and the fourth responds to violet light. A mallard's eye blocks most ultraviolet light before it reaches those cells, so this view adds no ultraviolet tint.", [BIRDS + "#2.4", "Hart 2001", "param:M", "param:sheen"]],
        ["i", "Sharpness", "This part of the view is a guess. It assumes that a duck sees about a fifth as much detail as a person, the middle value for birds.", [BIRDS + "#2.4", "Caves et al. 2018", "param:cpd"]],
        ["i", "Speed", "This part of the view is a guess. It assumes that a duck sees flicker about as fast as a pigeon or a chicken and runs the picture slightly slow.", [BIRDS + "#2.4", "Boström et al. 2016", "param:rate"]],
        ["i", "Being tried: the sky overhead", "The fold that presses the sky into the top of the picture, the ribbon of every direction faced, the blind area's width and the colour lift are the app's drawings.", ["param:remap.fold", "param:remap.horizon", "param:remap.blindDeg", "param:remap.blindSoft", "param:remap.band", "param:remap.fadeS", "param:sat", "param:pupil"]],
        ["x", "Touch", "Many ducks find food by feel, with the many touch-sensing cells at the tip of the bill. This view cannot show touch.", [BIRDS + "#2.4", "Cantlay et al. 2023"]],
    ],
}

# ---------- bigcat (CATDOG section 2.2) ----------
new["bigcat"] = {
    "key": "bigcat", "version": 1, "chip": "Lion, tiger, leopard", "who": "a big cat", "falls_back_to": "cat",
    "applies_to": {"genus": ["Panthera", "Acinonyx", "Puma", "Neofelis"]},
    "cue": "Out-of-focus things blur evenly in every direction.", "modules": [], "draft": True,
    "params": {
        "cpd": P(12, [2, 40], "cat 8 times the tiger's longer eye (29.4 against 19.75 mm)", [CATDOG + "#2.2: L121, L75, L126"], "i", True),
        "topoA": P(1, [0, 2], "by analogy with the house cat"),
        "fall": P(1.0, [0, 3], "by analogy with the house cat"),
        "pupil": P("o", None, "round pupils in large cats", [CATDOG + "#2.2: L103, L49"], "m", False),
        "dof": P(14, [0, 40], "no source"),
        "M": P("DEUTAN", None, "two cone classes", [CATDOG + "#2.2: L138, L97"], "m", True),
        "gain": P(1.6, [1, 3], "the lion's large tapetum", [CATDOG + "#2.2: L122"], "g", True),
        "sat": P(.8, [0, 1.5], "no source"),
    },
    "matrices": {"DEUTAN": DEUTAN},
    "by": {"genus": {"Acinonyx": {"params": {"cpd": P(23, [2, 40], "the cheetah", [CATDOG + "#2.2: L94"], "m", False)}}}},
    "inputs": {"motion": "none", "sound": "none", "haptic": "none"},
    "rows": [
        ["m", "Pupil", "Lions, tigers and the other large cats have round pupils, like people and dogs, where house cats have upright slits. Out-of-focus things blur evenly in every direction in this view.", [CATDOG + "#2.2", "L103", "L49", "L140", "param:pupil"]],
        ["m", "Lens", "A tiger's lens focuses every colour at the same depth, where a house cat's lens has zones for several. Why the large cats lack those zones is unknown.", [CATDOG + "#2.2", "L49"]],
        ["m", "Colour", "Lions, tigers, leopards and cheetahs have two kinds of colour-sensing cells, as house cats do, where people have three. This view shows colours the way a person with red-green colour blindness sees them.", [CATDOG + "#2.2", "L138", "L97", "L98", "param:M"]],
        ["m", "Cheetah", "A cheetah sees about a third as much detail as a person, and about three times as much as a house cat. Its cones for yellow-green light crowd into a band along the horizon.", [CATDOG + "#2.2", "L94", "L97"]],
        ["i", "Sharpness", "No measurement was found for lions, tigers, leopards or pumas. Their eyes are about one and a half times as long as a house cat's, and longer eyes usually see finer detail, so this view guesses that they see about a fifth as much detail as a person.", [CATDOG + "#2.2", "L121", "L75", "param:cpd"]],
        ["m", "Dim light", "In a study of the eyes of three kinds of wild cat, the lions had the largest tapetum, the mirror-like layer behind the retina that gives light a second pass. This view brightens the shadows to suggest it.", [CATDOG + "#2.2", "L122", "param:gain"]],
        ["i", "Field of view and depth", "No measurement was found for these. This view keeps the field your camera gives and assumes that things lower in the picture are closer. The depth of focus, the colour's strength and the fall of sharpness from the centre are guesses.", ["param:dof", "param:sat", "param:topoA", "param:fall"]],
        ["x", "Ultraviolet", "House cats' lenses let through ultraviolet light, and big cats have not been tested. A phone camera filters out almost all ultraviolet, so this view leaves it out.", [CATDOG + "#2.2", "L100", "L127"]],
    ],
}

# ---------- fox (CATDOG section 2.4) ----------
new["fox"] = {
    "key": "fox", "version": 1, "chip": "Fox", "who": "a fox", "falls_back_to": "dog",
    "applies_to": {"genus": ["Vulpes", "Urocyon"]},
    "cue": "Out-of-focus things smear up and down.", "modules": ["motion"], "draft": True,
    "params": {
        "cpd": P(6, [1, 40], "from maps of the retina's nerve cells, an anatomical estimate", [CATDOG + "#2.4: L173"], "m", False),
        "topoA": P(1, [0, 2], "a sharp centre", [CATDOG + "#2.4: L39, L42"], "g", True),
        "topoS": P(.4, [0, 2], "a weaker band along the horizon", [CATDOG + "#2.4: L39, L41, L42"], "g", True),
        "fall": P(1.2, [0, 3], "no source"),
        "pupil": P("v", None, "a tall, thin oval in bright light", [CATDOG + "#2.4: L51, L141"], "m", False),
        "dof": P(22, [0, 40], "no source"),
        "M": P("DEUTAN", None, "two cone classes, as in dogs", [CATDOG + "#2.4: L110, L111"], "m", True),
        "gain": P(1.6, [1, 3], "a rod-rich retina", [CATDOG + "#2.4: L41"], "g", True),
        "sat": P(.8, [0, 1.5], "no source"),
    },
    "matrices": {"DEUTAN": DEUTAN},
    "magnet": {"k": P(.6, [0, 2], "how strongly the compass is drawn; the fox's sense, if it exists, is not described")},
    "draw": {"magnet": [opt("none", "the view without the compass"),
                        opt("tide", "a faint shade that follows the angle between the camera and magnetic north (the draft's compass arc, drawn with the existing tide)")]},
    "inputs": {"motion": "optional", "sound": "none", "haptic": "none", "senses": {"motion": 1}},
    "rows": [
        ["m", "Pupil", "A red fox's pupil narrows in bright light to a tall, thin oval, close to a house cat's slit, and its lens has zones that bring several colours into focus together. Out-of-focus things smear up and down in this view.", [CATDOG + "#2.4", "L51", "L141", "L54", "param:pupil"]],
        ["m", "Sharpest spot", "A red fox sees most sharply in a small central spot, with a weaker band along the horizon. The Arctic fox, which lives on open tundra, has a stronger band.", [CATDOG + "#2.4", "L39", "L41", "L42"]],
        ["m", "Colour", "Red foxes, Arctic foxes and island gray foxes have the same two kinds of colour-sensing cells as dogs. This view shows colours the way a person with red-green colour blindness sees them.", [CATDOG + "#2.4", "L110", "L115", "L40", "param:M"]],
        ["m", "Night eyes", "A red fox's retina holds more rods for each cone than an Arctic fox's, the mark of an eye built for night in woodland. This view brightens the shadows.", [CATDOG + "#2.4", "L41", "L39"]],
        ["m", "Sharpness", "Maps of the nerve cells in a red fox's retina suggest that it sees about a tenth as much detail as a person. This view is blurred to match.", [CATDOG + "#2.4", "L173", "param:cpd"]],
        ["i", "Being tried: north", "Red foxes hunting mice pounce mostly toward the north-east, and the pounces that succeed cluster toward the north. With &draw=tide and the motion sensors on, a faint shade follows magnetic north. Whether foxes sense the field is unknown, and the drawing is the app's.", [CATDOG + "#2.4", "L117", "L175", "param:magnet.k"]],
        ["i", "Guesses", "The weights of the centre and the band, the depth of focus, the brightening, the colour's strength and the fall of sharpness from the centre are the app's.", ["param:topoA", "param:topoS", "param:fall", "param:dof", "param:gain", "param:sat"]],
        ["x", "Hearing", "A red fox hears sounds from about 51 to 48,000 vibrations a second, and at 4,000 a second its hearing is keener than a house cat's. This view leaves sound out.", [CATDOG + "#2.4", "L174"]],
    ],
}

# ---------- millipede, centipede, harvestman (GROUND sections 2.2, 2.3, 2.6) ----------
new["millipede"] = {
    "key": "millipede", "version": 1, "chip": "Millipede", "who": "a millipede", "falls_back_to": "worm",
    "applies_to": {"class": ["Diplopoda", "Pauropoda"]},
    "cue": "Point the phone at the ground under leaves and turn it slowly. Only the darker side of the scene remains.",
    "modules": ["sound", "haptic"], "draft": True,
    "params": {
        "cpd": P(.018, [.005, 1], "1 / 56: a dark shape about 20 degrees wide", [GROUND + "#2.2: L77 (Kirwan and Nilsson 2019)"], "m", False),
        "sat": P(0, [0, 1], "no millipede spectral measurement"),
        "field": P(0, [0, 1], "1 for the eyeless flat-backed millipedes when the database names the species"),
    },
    "sound": {"k": P(1.4, [0, 3], "how strongly low sound shakes the picture")},
    "haptic": HAP("onset", [40, 30, 40]),
    "draw": {"sound": [OFF("sound"), opt("rumble", "low sounds picked up by the microphone shake the lower picture (atlas 15)")], "haptic": HAP_DRAW},
    "inputs": {"motion": "none", "sound": "optional", "haptic": "optional"},
    "rows": [
        ["m", "Eyes", "Most millipedes have a small cluster of large-faceted eyes on each side of the head. The flat-backed millipedes, among them the greenhouse millipede, which is photographed more than any other, have no eyes at all.", [GROUND + "#2.2", "L79", "L89", "L92", "L93"]],
        ["m", "Sharpness", "In behaviour tests the millipede Cylindroiulus punctatus made out a dark shape about 20 degrees wide, enough to find shelter and little more. A person sees detail about three thousand times finer. This view is blurred to match.", [GROUND + "#2.2", "L77", "L78", "L80", "param:cpd"]],
        ["m", "Light through the skin", "The greenhouse millipede senses light through its skin. Light makes it walk more without steering it anywhere, so it keeps moving until it happens upon a dark place.", [GROUND + "#2.2", "L84"]],
        ["m", "Touch", "A walking millipede taps the ground constantly with the tips of its antennae, and touch shapes most of what it does.", [GROUND + "#2.2", "L90", "L86"]],
        ["m", "Taste and damp", "A millipede tastes food by touching it, and in tests it showed no response to smells. Drying out keeps it walking, and once it settles on damp ground it is slow to move again.", [GROUND + "#2.2", "L87", "L88", "L91"]],
        ["g", "Night", "Many millipedes come out only at night. The luminous millipede Paraspirobolus lucifugus avoids light and keeps a daily clock.", [GROUND + "#2.2", "L83"]],
        ["i", "Colour", "No millipede's colour sense has been measured, so the picture is grey.", ["param:sat", "param:field"]],
        ["i", "Being tried: shaking ground", "A millipede curls into a tight spiral when it is disturbed, and very slight vibrations set it walking. With &draw=rumble and the microphone on, low sounds shake the lower picture, and with &draw=buzz the phone buzzes with each one. The drawing is the app's.", [GROUND + "#2.2", "L86", "param:sound.k", "param:haptic.pattern", "param:haptic.edge"]],
    ],
}

new["centipede"] = {
    "key": "centipede", "version": 1, "chip": "Centipede", "who": "a centipede", "falls_back_to": "insect",
    "applies_to": {"class": ["Chilopoda"]},
    "cue": "Turn toward a dark gap. Large dark shapes stand out.",
    "modules": ["overlay"], "draft": True,
    "params": {
        "cpd": P(.05, [.005, 1], "about 2.8 times a millipede's, from the facet counts"),
        "M": P("BLUE_GREY", None, "one blue peak near 448 nm", [GROUND + "#2.3: L94 (Meyer-Rochow, Müller and Lindström 2006)"], "m", True),
    },
    "matrices": {"BLUE_GREY": {"rows": [[.05, .25, .7], [.05, .25, .7], [.05, .25, .7]], "grade": "m", "invented": True, "src": [GROUND + "#2.3: L94"]}},
    "overlay": {"shadow": P(1, [0, 2], "how dark the ring is when the light falls")},
    "draw": {"overlay": [OFF("rings"), opt("shadow", "when the light falls suddenly, a dark ring runs out from where it fell (atlas 14), for an animal that runs from light toward dark shapes")]},
    "inputs": {"motion": "none", "sound": "none", "haptic": "none"},
    "rows": [
        ["m", "Eyes", "The house centipede has a compound eye of about 150 to 200 facets on each side of its head. Most large tropical centipedes have four simple eyes on each side, and the soil centipedes have none.", [GROUND + "#2.3", "L97", "L98", "L99", "L101", "L100"]],
        ["m", "Colour", "The house centipede's eye is most sensitive to blue light near 448 nanometres and has a second peak in ultraviolet near 350. This view weights its grey toward blue and leaves the ultraviolet out.", [GROUND + "#2.3", "L94", "L95", "L96", "param:M"]],
        ["i", "Sharpness", "No one has measured how much detail a centipede sees. This view assumes the house centipede sees nearly three times as sharply as a millipede, because its eye has about seven times as many facets.", [GROUND + "#2.3", "L77", "L81", "L97", "param:cpd"]],
        ["m", "Dark shapes", "Centipedes run from light and toward dark shapes. The house centipede, the brown centipede and a large Scolopendra all head for a dark screen at the side of an arena.", [GROUND + "#2.3", "L102", "L103"]],
        ["m", "Sunlight as heat", "A large Asian centipede feels sunlight as heat in its antennae, which warm by more than 8 degrees Celsius within ten seconds of strong sun.", [GROUND + "#2.3", "L104", "L105"]],
        ["g", "Soil centipedes", "Soil centipedes are blind. In one of them every known gene for sensing light is missing, while the house centipede keeps those genes.", [GROUND + "#2.3", "L101"]],
        ["i", "Being tried: shadows", "With &draw=shadow, a sudden fall of light sends a dark ring across the picture. The ring is the app's drawing.", ["param:overlay.shadow"]],
        ["x", "Not in the picture", "A centipede finds prey and mates largely by smell and touch through its antennae, and a camera records neither.", [GROUND + "#2.3", "L186", "L187"]],
    ],
}

new["harvestman"] = {
    "key": "harvestman", "version": 1, "chip": "Harvestman", "who": "a harvestman", "falls_back_to": "spider",
    "applies_to": {"order": ["Opiliones"]},
    "cue": "The view looks out to both sides at once, and straight ahead is dim.",
    "modules": ["field", "haptic"], "draft": True,
    "params": {
        "cpd": P(.05, [.005, 1], "a rough picture of light and dark, between the millipede and the tick"),
        "sat": P(0, [0, 1], "no spectral measurement in common species"),
        "gain": P(1.2, [1, 3], "fast lenses in cave species", [GROUND + "#2.6: L59, L60"], "g", True),
    },
    "remap": {"blindAt": P(0, [0, 360], "the dim seam straight ahead, between the two side-facing eyes", [GROUND + "#2.6: L52, L53"], "m", True),
              "blindDeg": P(30, [0, 120], "the seam's width"),
              "blindSoft": P(20, [0, 60], "the seam's soft edge")},
    "haptic": HAP("knock", [25]),
    "draw": {"field": [opt("wedge", "straight ahead stays dim as you turn, since each eye looks out to one side (the draft's two side windows)"), opt("squeeze", "the view without the seam")],
             "haptic": HAP_DRAW},
    "inputs": {"motion": "optional", "sound": "none", "haptic": "optional"},
    "rows": [
        ["m", "Eyes", "A harvestman has a single pair of eyes, set back to back on a small turret in the middle of its body. Each eye looks out to one side.", [GROUND + "#2.6", "L52", "L53", "L66", "param:remap.blindAt"]],
        ["m", "Rough images", "A harvestman's eyes probably give only a rough picture of light and dark. A large dark object makes a species of Leiobunum flee, and in the laboratory harvestmen move away from light.", [GROUND + "#2.6", "L53", "L54", "L55"]],
        ["m", "Hidden eyes", "The most photographed harvestman, Phalangium opilio, also carries two more pairs of eyes inside its body, both shrunk to traces. They may help set its daily clock.", [GROUND + "#2.6", "L65"]],
        ["g", "Colour and dim light", "In two cave harvestmen from New Zealand the eyes respond to ultraviolet, blue and green light, over a range of brightness of at least a hundred thousand to one.", [GROUND + "#2.6", "L62", "L63", "L59", "L60", "param:gain"]],
        ["m", "Touch and taste", "Harvestmen find food, mates and enemies mostly by touching and tasting them with their first pair of legs and their palps, and they sense little from a distance.", [GROUND + "#2.6", "L57", "L58", "L68"]],
        ["i", "Sharpness and field", "No one has measured how much detail a harvestman sees. This view assumes coarse sight of a few large shapes, grey, clearest out to each side. The dim seam's width, and the buzz at a knock (&draw=buzz), are the app's.", [GROUND + "#2.6", "L53", "param:cpd", "param:sat", "param:remap.blindDeg", "param:remap.blindSoft", "param:haptic.pattern", "param:haptic.edge"]],
        ["x", "Not in the picture", "The touch and taste of a harvestman's legs and palps carry most of what it knows, and the camera records neither.", [GROUND + "#2.6", "L57", "L58"]],
    ],
}

# ---------- woodlouse: the crab spec's woodlouse variant made its own view, for the overlays ----------
crab = load("crab")
wl = crab["variants"]["woodlouse"]
w = {"key": "woodlouse", "version": 1, "chip": "Woodlouse", "who": "a woodlouse", "falls_back_to": "crab", "applies_to": wl["applies_to"],
     "cue": wl["cue"], "modules": ["overlay"], "draft": True,
     "params": dict({k: v for k, v in crab["params"].items() if k not in wl["params"]}, **wl["params"]),
     "matrices": crab.get("matrices", {}),
     "overlay": {"shadow": P(1, [0, 2], "how dark the ring is when the light falls")},
     "draw": {"overlay": [OFF("rings"), opt("shadow", "when the light falls suddenly, a dark ring runs out from where it fell (atlas 14); woodlice turn toward dark shelter")]},
     "inputs": {"motion": "none", "sound": "none", "haptic": "none"},
     "rows": wl["rows"] + [["i", "Being tried: shadows", "With &draw=shadow, a sudden fall of light sends a dark ring across the picture. The ring is the app's drawing.", ["param:overlay.shadow"]]]}
new["woodlouse"] = w

for k, s in new.items():
    save(k, s)

# ---------- the modules in specs that exist ----------
s = load("fish")   # Snell's window as a field: always there, centred, with no tilt needed
s["remap"] = {}
s["draw"] = dict(s.get("draw") or {}, field=[opt("squeeze", "the view as it was"), opt("window", "Snell's window always on, centred, as a remap of the field with no tilt needed (atlas 2)")])
s["rows"] = put_rows(s["rows"], [["g", "Being tried: the window as a field", "With &draw=window the sky's disc about 97 degrees across sits in the middle of the picture all the time, so it can be seen with no motion sensors. The dark ring outside it is the app's.", ["docs/views/sheets/fish.md#4", "Sabbah 2006"]]])
save("fish", s)

s = load("spider")   # the web, airflow and a buzz at each knock
s["overlay"] = {"web": P(.8, [0, 1], "how strongly the web is drawn")}
s["sound"] = {"k": P(1, [0, 3], "how strongly moving air ruffles the picture")}
s["haptic"] = HAP("knock", [25])
s["draw"] = dict(s.get("draw") or {}, overlay=[OFF("the web"), opt("web", "spokes and a spiral drawn over the picture; knocks and sounds shake them and make them flash (atlas 15)")],
                 sound=[OFF("airflow"), opt("air", "breath and moving air picked up by the microphone ruffle the picture, as air moves a spider's hairs (atlas 16)")],
                 haptic=HAP_DRAW)
s["rows"] = put_rows(s["rows"], [["i", "Being tried: web and air", "With &draw=web the picture carries a drawn web that shakes and flashes with knocks and sounds. With &draw=air, breath on the microphone ruffles the picture. With &draw=buzz the phone buzzes at a knock. Each drawing is the app's.", ["docs/views/sheets/spider.md#4", "param:overlay.web", "param:sound.k", "param:haptic.pattern", "param:haptic.edge"]]])
save("spider", s)

s = load("worm")   # the shadow alarm
s["overlay"] = {"shadow": P(1, [0, 2], "how dark the ring is when the light falls")}
s["draw"] = dict(s.get("draw") or {}, overlay=[OFF("rings"), opt("shadow", "a sudden fall of light sends a dark ring across the picture, the shadow alarm (atlas 14)")])
s["rows"] = put_rows(s["rows"], [["i", "Being tried: the shadow alarm", "With &draw=shadow, a sudden fall of light, as when a shadow passes, sends a dark ring across the picture. The ring is the app's drawing.", ["docs/views/sheets/worm.md#4", "param:overlay.shadow"]]])
save("worm", s)

s = load("bat")   # clap and see
s["sound"] = {"k": P(1, [0, 2], "how strongly sound moves the picture"), "dark": P(.04, [0, 1], "how dark the picture rests between sounds"),
              "holdS": P(.35, [.05, 2], "seconds the picture stays lit after a sound"), "clickHz": P(0, [0, 8], "clicks a second from the speaker; 0 for none"),
              "say": "This view lights the picture when it hears a clap or a click, as a bat sees by its echoes. Tap to let it listen through the microphone. Nothing is recorded or kept."}
s["draw"] = dict(s.get("draw") or {}, sound=[OFF("sound"), opt("clap", "the picture stays dark until a clap or click lights it for a moment (atlas 18, clap and see)")])
s["rows"] = put_rows(s["rows"], [["i", "Being tried: clap and see", "With &draw=clap and the microphone on, the picture stays dark until you clap or click, and then it shows for a moment. A phone cannot hear echoes the way a bat does, so the drawing stands in for them and is the app's.", ["docs/views/sheets/bat.md#4", "param:sound.dark", "param:sound.holdS", "param:sound.clickHz", "param:sound.k"]]])
save("bat", s)

s = load("mammal")   # the mole's rumble
s["sound"] = {"k": P(1.4, [0, 3], "how strongly low sound shakes the picture")}
s["draw"] = dict(s.get("draw") or {}, sound=[OFF("sound"), opt("rumble", "low sounds picked up by the microphone shake the lower picture first, as through the ground (atlas 15, the mole)")])
s["rows"] = put_rows(s["rows"], [["i", "Being tried: the rumble", "With &draw=rumble and the microphone on, low sounds shake the lower part of the picture, as vibration through the ground reaches a mole. The drawing is the app's.", ["docs/views/sheets/mammal.md#4", "param:sound.k"]]])
save("mammal", s)

for k in ("bee", "insect"):   # polarization, as a trial on the offered views
    s = load(k)
    t = s.setdefault("trial", {})
    t["overlay"] = {"polar": P(.8, [0, 2], "how strongly the polarized band of sky is drawn")}
    t["draw"] = dict(t.get("draw") or {}, overlay=[OFF("the sky's pattern"), opt("polar", "fine strokes over the sky, strongest 90 degrees from the sun, along the direction the light is polarized (atlas 6)")])
    t["inputs"] = dict(t.get("inputs") or {}, motion="optional")
    t["rows"] = put_rows(t.get("rows") or [], [["i", "Being tried: the sky's pattern", "Many insects see the direction in which sky light is polarized, strongest in a band 90 degrees from the sun, and steer by it. With &draw=polar and the motion sensors on, fine strokes show that band from the time, the date and the phone's heading. The latitude is taken as 35 degrees north, and the drawing is the app's.", ["param:overlay.polar"]]])
    save(k, s)
print("wrote", ", ".join(sorted(new)), "and blocks in fish, spider, worm, bat, mammal, bee, insect")
