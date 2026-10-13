"""Writes views/<key>.json for crab, mammal, salamander, worm, bat, flyingfox and tick (burst 3).
Run from the repository root: python3 tools/views/make_specs_b.py [path to ground-invertebrates.md]
Rows are taken from the sheets' own row lines (docs/views/sheets/<group>.md, section 2) and the worm rows from the
ground-invertebrates draft (section 2.4); each row's sources are the author and year citations in its Source line.
Parameters are entered here with their grade, source, range and invented flag. Every spec is a draft."""
import json, os, re, sys

def P(v, g, inv, src=(), rng=None, note=None, floor=None):
    d = {"value": v, "grade": g, "invented": inv, "src": list(src)}
    if rng is not None: d["range"] = rng
    d["floor"] = floor
    if note: d["note"] = note
    return d
def mat(rows, g, inv, src, note=None):
    d = {"rows": rows, "grade": g, "invented": inv, "src": list(src)}
    if note: d["note"] = note
    return d
def write(key, spec):
    spec.setdefault("version", 1); spec.setdefault("zones", []); spec.setdefault("matrices", {}); spec.setdefault("by", {})
    spec.setdefault("inputs", {"motion": "none", "sound": "none", "haptic": "none"})
    spec["draft"] = True
    with open(os.path.join("views", key + ".json"), "w") as f: json.dump(spec, f, indent=2, ensure_ascii=False); f.write("\n")

S = "docs/views/sheets/"
CITE = re.compile(r"([A-Z][A-Za-zöüéá\-’']+(?: and [A-Z][A-Za-zöüéá\-]+| and colleagues)?),? (\d{4})")
ROW = re.compile(r"\['([mgix])', '(.*?)', '(.*)'\]\s*,?`?\s*$")

def rows_between(path, start, end, links, where, first_src=None):
    """Rows from the lines between the first line containing start and the next line containing end."""
    lines = open(path, encoding="utf-8").read().split("\n")
    i0 = next(i for i, l in enumerate(lines) if start in l)
    i1 = next((i for i in range(i0 + 1, len(lines)) if end in lines[i]), len(lines))
    out = []
    for i in range(i0, i1):
        m = ROW.search(lines[i].strip().lstrip("0123456789. ").strip("`").strip())
        if not m: continue
        g, title, text = m.groups()
        text = text.replace("\\'", "'")
        srcline = ""
        for j in range(i + 1, min(i + 6, i1)):
            if re.match(r"\s*(Source|Log):", lines[j]): srcline = lines[j]; break
        cites = []
        for a, y in CITE.findall(srcline):
            c = "%s %s" % (a, y)
            if c not in cites and a not in ("Source", "Log"): cites.append(c)
        src = [where + ": " + title] + cites[:6] + ["param:" + p for p in links.get(title, [])]
        out.append([g, title, text, src])
    return out

def check_rows(name, rows):
    assert rows, name
    for r in rows:
        assert "—" not in r[2] and "—" not in r[1], r[1]
    return rows

# ------------------------------------------------------------------ crab (with woodlouse and horseshoe crab variants)
CR = S + "crab.md"
crab_rows = check_rows("crab", rows_between(CR, "### The crab view", "### The woodlouse view", {
    "All around": ["fov"], "Sharpness": ["cpd"], "Colour": ["M"], "Ultraviolet": ["sheen"], "Pace": ["rate"]}, S + "crab.md#2 crab"))
wl_rows = check_rows("woodlouse", rows_between(CR, "### The woodlouse view", "### A horseshoe crab entry, for later", {
    "No picture": ["field", "pupil"], "Colour": ["sat"]}, S + "crab.md#2 woodlouse"))
hs_rows = check_rows("horseshoe", rows_between(CR, "### A horseshoe crab entry, for later", "## 3.", {
    "Sharpness": ["cpd"], "Colour": ["sat"]}, S + "crab.md#2 horseshoe"))
write("crab", {"key": "crab", "chip": "Crab, crayfish, shrimp", "who": "a crab", "falls_back_to": None,
 "applies_to": {"order": ["Decapoda", "Stomatopoda"]},
 "cue": "Hold the phone low, a hand above the sand or mud, and turn slowly. A crab sees the whole way around at once.", "modules": [],
 "params": {
  "fov": P(360, "g", True, [S+"crab.md#2 All around: Zeil and Hemmi 2006; Zeil and Al-Mutairi 1996"], [180, 360], "the sources give a panoramic field and no number; the engine compresses it to half scale"),
  "cpd": P(.4, "g", False, [S+"crab.md#2 Sharpness: Zeil and Al-Mutairi 1996 (0.39 cycles per degree, Uca lactea annulipes)"], [.1, 10], "measured in one fiddler crab and drawn for every decapod"),
  "pupil": P("none", "i", True, [], None, "no source describes a pupil; matches the bee and insect entries"),
  "M": P("crab_protan", "g", True, [S+"crab.md#2 Colour: Bruno, Mote and Goldsmith 1973; Jordao, Cronin and Oliveira 2007"], None, "one main pigment near 500 nm, so reds go dark; the engine's two-cone model stands in and is the app's choice"),
  "sheen": P(.5, "i", True, [S+"crab.md#2 Ultraviolet: Detto and Backwell 2009"], [0, 1], "a violet sheen for the ultraviolet a phone cannot record; the strength is the app's"),
  "rate": P(.8, "g", False, [S+"crab.md#2 Pace: Brodrick, How and Hemmi 2022 (73.6 Hz, light-adapted by day)"], [.3, 1.2], "60 over 73.6 is 0.82; a crayfish's movement fibres follow only about 10 Hz and were not used")},
 "matrices": {"crab_protan": mat([[0.11238, 0.88762, 0], [0.11238, 0.88762, 0], [0.00401, -0.00401, 1]], "g", True, [S+"crab.md#3 M"], "Vienot, Brettel and Mollon 1999, as in the squirrel view; entered from memory")},
 "variants": {
  "woodlouse": {"note": "Woodlouse, pill bug (Isopoda, Oniscidea): about twenty facets to an eye, so no picture, only light and from where. The same picture as the other entry.",
   "applies_to": {"order": ["Isopoda"]},
   "cue": "Hold the phone close to the ground and turn it slowly. A woodlouse heads for the darker side.",
   "params": {"field": P(1, "i", True, [S+"crab.md#2 woodlouse No picture"], [0, 1], "inferred from facet counts; no resolution is measured in a woodlouse"),
             "sat": P(0, "i", True, [S+"crab.md#2 woodlouse Colour"], [0, 1], "no colour measurement was found"),
             "pupil": P("none", "i", True)},
   "rows": wl_rows},
  "horseshoe": {"note": "Horseshoe crab, sketched for later in the sheet.",
   "applies_to": {"subphylum": ["Chelicerata"], "genus": ["Limulus"]},
   "params": {"cpd": P(.1, "m", False, [S+"crab.md#2 horseshoe Sharpness: Herzog and Barlow 1992"], [.05, 1]),
             "sat": P(0, "m", False, [S+"crab.md#2 horseshoe Colour: Chapman and Lall 1967; Battelle 2014"], [0, 1]),
             "pupil": P("none", "i", True)},
   "rows": hs_rows + [["i", "Pupil", "No source describes a pupil in a horseshoe crab's eye, so none is drawn.", ["param:pupil"]]]}},
 "notes": [
  {"need": "anisotropic blur", "why": "A fiddler crab resolves vertical detail about five times finer than horizontal (0.25 against 1.33 degrees). The engine blurs the same in both directions. Easy with a new blur."},
  {"need": "topoS", "why": "Two streaks at the horizon (Bagheri 2020) and a band held level on a slope (Zeil 1990). topoS draws one band at the horizon; the sheet leaves it unset because 15 percent of decapod records are measured without the band."},
  {"need": "adaptM", "why": "The eye about a thousand times more sensitive at night (Brodrick 2022): the clock could raise gain and lower rate after dark. Easy, but the size of the lift would be invented."},
  {"need": "polarization", "why": "Polarization contrast on mud and water. No phone input records it."},
  {"need": "mask", "why": "Horseshoe crab: two windows aimed sideways, each about 60 percent of its half of the world. The aperture mask could take a two-window shape."}],
 "rows": crab_rows})

# ------------------------------------------------------------------ mammal (raccoon and mole as variants)
MA = S + "mammal.md"
mam_rows = check_rows("mammal", rows_between(MA, "### `mammal` (two kinds of cone)", "### `raccoon`", {
    "Colour": ["M"], "Sharpness": ["cpd"], "Dim light": ["gain"], "Field of view and pupil": ["pupil"]}, S + "mammal.md#2 mammal"))
rac_rows = check_rows("raccoon", rows_between(MA, "### `raccoon`", "### `mole`", {
    "Colour": ["M"], "Dim light": ["gain"], "Sharpness, field and pupil": ["cpd", "pupil"], "Drawn as": ["M"]}, S + "mammal.md#2 raccoon"))
mole_rows = check_rows("mole", rows_between(MA, "### `mole`", "## 3.", {"Light and dark": ["field", "sat"], "Eyes": ["pupil"]}, S + "mammal.md#2 mole"))
write("mammal", {"key": "mammal", "chip": "Bear, kangaroo, pig", "who": "a mammal", "falls_back_to": "other",
 "applies_to": {"class": ["Mammalia"]},
 "cue": "Two kinds of colour sensor, and less detail than yours.", "modules": [],
 "params": {
  "cpd": P(5, "g", True, [S+"mammal.md#2 Sharpness: Hemmi and Mark 1998 (4.8, tammar); Veilleux and Kirk 2014 (11.2, western grey kangaroo); Shyan-Norwalt 2010"], [.5, 12], "measured values run from about 0.6 (African elephant) to 11.2; the pick of 5 is the app's"),
  "pupil": P("o", "i", True, [], None, "no measurement of pupil or field was found"),
  "M": P("mammal_deutan", "g", True, [S+"mammal.md#2 Colour: Neitz and Jacobs 1989 (pig); Heyward 2021 (black bear)"], None, "two cone types; the engine's two-cone model that keeps the long cone stands in, which is the app's reading"),
  "gain": P(1.2, "i", True, [S+"mammal.md#2 Dim light: tapetum lucidum 2004"], [1, 3], "no dim-light ratio was found; lower than the dog's 1.3 and the cat's 1.7")},
 "matrices": {"mammal_deutan": mat([[0.29275, 0.70725, 0], [0.29275, 0.70725, 0], [-0.02234, 0.02234, 1]], "g", True, [S+"mammal.md#3 M"], "Vienot, Brettel and Mollon 1999, as in the cat and dog views; entered from memory")},
 "variants": {
  "raccoon": {"note": "Raccoon, opossum, armadillo, sloth, anteater, pangolin: one kind of cone or none, so a grey picture weighted to yellow-green, with the shadows lifted.",
   "applies_to": {"family": ["Procyonidae", "Didelphidae", "Dasypodidae", "Bradypodidae", "Megalonychidae", "Myrmecophagidae", "Manidae"]},
   "cue": "One kind of colour sensor, or none. The world in greys, with the shadows lifted.",
   "params": {"cpd": P(4, "i", True, [], [.5, 12], "no acuity was found for any member; below the mammal value because these are night eyes"),
             "pupil": P("o", "i", True),
             "M": P("raccoon_grey561", "g", True, [S+"mammal.md#2 raccoon Colour: Jacobs and Deegan 1992; Jacobs and Williams 2010 (561 nm)"], None, "weights toward red and green stand in for one cone near 561 nm; the weights are the app's"),
             "gain": P(1.6, "i", True, [S+"mammal.md#2 raccoon Dim light"], [1, 3], "carnivores and marsupials have a reflecting layer; the amount is the app's, just under the cat's 1.7")},
   "matrices": {"raccoon_grey561": mat([[.4, .55, .05], [.4, .55, .05], [.4, .55, .05]], "g", True, [S+"mammal.md#3 raccoon M"])},
   "rows": rac_rows},
  "mole": {"note": "Mole (Talpidae): eyes under the skin; light from dark and nothing more. The same picture as the other entry.",
   "applies_to": {"family": ["Talpidae"]}, "cue": "",
   "params": {"field": P(1, "g", True, [S+"mammal.md#2 mole Light and dark: Slonaker; Animal Diversity Web"], [0, 1]),
             "sat": P(0, "g", True, [S+"mammal.md#2 mole Light and dark"], [0, 1]),
             "pupil": P("none", "i", True)},
   "rows": mole_rows + [["i", "The picture", "A grey field of light and shade is the app's way of showing light without an image. The sources give no more than light and dark.", ["param:field", "param:sat", "param:pupil"]]]}},
 "notes": [
  {"need": "adaptM", "why": "Rod-only eyes (armadillos, sloths) would wash out to white in bright day. A new field that compresses highlights; it waits on a source."},
  {"need": "topoA", "why": "The black bear has a cone-dense area centralis (Heyward 2021); kangaroos may have a band. A separate bear entry would draw it once kangaroo topography is sourced."},
  {"need": "touch", "why": "Mole: the touch screen could light a small patch under the finger in a dark field. It would be an invention."}],
 "rows": mam_rows})

# ------------------------------------------------------------------ salamander
SA = S + "salamander.md"
sal_rows = check_rows("salamander", rows_between(SA, "## 2. The rows", "## 3.", {
    "Ultraviolet": ["sheen"], "Colour": ["M"], "Distance": ["dof"],
    "Ultraviolet tint, sharpness, field and pupil": ["sheen", "fov", "cpd", "pupil"]}, S + "salamander.md#2"))
write("salamander", {"key": "salamander", "chip": "Salamander, newt", "who": "a salamander or newt", "falls_back_to": "other",
 "applies_to": {"order": ["Caudata"]},
 "cue": "Tap what you would catch to bring it into focus. Colours stay, with a violet tint for ultraviolet.", "modules": [],
 "params": {
  "fov": P(260, "i", True, [S+"salamander.md#3 fov: Wiggers 1995 (forward eyes in tongue-shooters)"], [180, 360], "no field was found for any salamander; below the frog's 340 because some have forward eyes"),
  "cpd": P(4, "i", True, [], [.5, 10], "no acuity was found; repeats the frog's guess"),
  "pupil": P("o", "i", True, [], None, "no source on pupil shape was opened"),
  "dof": P(12, "g", True, [S+"salamander.md#2 Distance: Werner and Himstedt 1984 (fire salamander)"], [0, 30], "the eye focuses on prey to judge distance, which tap-to-focus can suggest; the strength is the app's, half the alligator's 24"),
  "sheen": P(.6, "i", True, [S+"salamander.md#2 Ultraviolet: Ma 2001; Korenyak and Govardovskii 2013; Martin 2016"], [0, 1], "a violet sheen for the ultraviolet cones, which a phone cannot record; matches the reptile and wader entries")},
 "notes": [
  {"need": "gate", "why": "Left unset on purpose: no test of whether a salamander ignores still prey was found (Kundey 2016 used fixed marks in a maze). First open question in the sheet."},
  {"need": "magnetometer", "why": "The eastern newt's magnetic compass swings a quarter turn under light above 500 nm (Phillips 2001). A faint line along the field could be drawn from the phone's compass; not drawn."},
  {"need": "dof band", "why": "The tongue-shooters keep a band of sharp focus at the tongue's reach. dof with a tap already moves the focus; the fixed distance would be invented."},
  {"need": "lateral line", "why": "Ripples around near movement for water-dwellers, from frame motion. Medium work, invented."},
  {"need": "caecilian, olm", "why": "Caecilians and the olm stay out and would take light-only settings (field 1) once they have rows of their own."}],
 "rows": sal_rows})

# ------------------------------------------------------------------ worm (draft: ground-invertebrates 2.4)
GI = sys.argv[1] if len(sys.argv) > 1 else "/tmp/gi.md"
W = "research/ground-invertebrates:docs/views/drafts/ground-invertebrates.md#2.4"
worm_rows = check_rows("worm", rows_between(GI, "### 2.4 `worm`", "**The picture.**", {
    "No eyes": ["cpd"], "Flatworms": ["cpd"], "The picture": ["M", "cpd"]}, W))
write("worm", {"key": "worm", "chip": "Worm", "who": "a worm or leech", "falls_back_to": "other",
 "applies_to": {"phylum": ["Annelida", "Platyhelminthes", "Nemertea"]},
 "cue": "Hold still and let a hand pass over the phone. There is no picture, only light, its direction and the shock of a shadow.", "modules": [],
 "params": {
  "cpd": P(.014, "g", True, [W+" cpd: Land and Nilsson 2012 (35 degrees, planarian cup eye); Kirwan 2018 (73 degrees, Schmidtea lugubris)"], [.005, .05], "1 over 2 times 35 gives .014; earthworms have no eyes and the gradient stands for the directional windows in their skin, which is the draft's reading"),
  "pupil": P("none", "i", True, [], None, "no eye with a pupil to draw"),
  "M": P("worm_blue", "g", True, [W+" M: Paskin 2014 (planarians flee ultraviolet most); Stowasser 2019 (leech underside)"], None, "blue weighted most because blue is the nearest colour the camera records to ultraviolet; the weights are the app's")},
 "matrices": {"worm_blue": mat([[0, .3, .7], [0, .3, .7], [0, .3, .7]], "g", True, [W+" M"], "weights invented")},
 "notes": [
  {"need": "adaptM", "why": "Dim light and bright light (Hess 1923): in near darkness the field leans toward the bright side and in ordinary light it leans away. Easy; the draft's thresholds are invented."},
  {"need": "shadow alarm", "why": "A sudden fall in brightness (a third within a third of a second) closes the field to a point and reopens it over two or three seconds, as a fan worm withdraws (Bok 2017). Needs a brightness trigger the engine lacks."},
  {"need": "sound", "why": "A mole digging: a low rumble raises and brightens the field, as an earthworm surfaces (Catania 2008). Needs the microphone's low band, with consent."},
  {"need": "zones", "why": "A leech's body of eyes: with the phone flat and face up, the top half leans green and the bottom half blue (Stowasser 2019). Needs zones and device orientation."},
  {"need": "split", "why": "The draft proposes separate millipede and centipede views; until they exist the word table sends them here."}],
 "rows": worm_rows})

# ------------------------------------------------------------------ bat and flying fox
BA = S + "bat.md"
bat_rows = check_rows("bat", rows_between(BA, "### `bat` (every family except Pteropodidae)", "### `flyingfox` (Pteropodidae)", {
    "Calls": ["hold", "thrust"], "Sharpness": ["cpd"], "Dim light": ["gain"], "Colour": ["sat"]}, S + "bat.md#2 bat"))
ff_rows = check_rows("flyingfox", rows_between(BA, "### `flyingfox` (Pteropodidae)", "## 3.", {
    "Sharpness": ["cpd"], "Colour": ["M", "sat"], "Dim light": ["gain"], "Field, focus and pupil": ["pupil"]}, S + "bat.md#2 flyingfox"))
write("bat", {"key": "bat", "chip": "Bat", "who": "a bat", "falls_back_to": "other",
 "applies_to": {"order": ["Chiroptera"], "not_family": ["Pteropodidae"]},
 "cue": "Each call brings back one snapshot, so the picture holds, then jumps.", "modules": [],
 "params": {
  "cpd": P(.6, "g", False, [S+"bat.md#2 Sharpness: Cechetto 2020 (Myotis daubentonii, 0.6 from ganglion cell density); Brokaw 2024 (about 0.35, rufous horseshoe bat)"], [.2, 2], "the lowest cpd in use is 1 (bees); at .6 check the value on a phone"),
  "hold": P(110, "i", True, [S+"bat.md#2 Calls: Moss and Surlykke 2010"], [0, 300], "milliseconds; the heron's held gaze reused as a call-by-call snapshot, a 140 ms cycle with thrust gives about 7 a second, inside the search rate of 5 to 10"),
  "thrust": P(30, "i", True, [S+"bat.md#2 Calls: Moss and Surlykke 2010"], [0, 100], "milliseconds; see hold"),
  "sat": P(.25, "i", True, [S+"bat.md#2 Colour: Muller 2009 (cones are 2 to 4 percent of receptors in leaf-nosed bats)"], [0, 1], "the amount of drain is the app's"),
  "gain": P(1.6, "i", True, [S+"bat.md#2 Dim light: Boonman 2013"], [1, 3], "the amount is the app's"),
  "pupil": P("o", "i", True, [], None, "no source was found; with dof unset it changes nothing")},
 "notes": [
  {"need": "depth image", "why": "The main sense of a calling bat is an echo picture: brightness from echo strength, refreshed call by call, in a cone of 60 to 90 degrees. Needs a depth source (LiDAR or a depth model) and a new drawing mode. Hard. Until then the entry draws the coarse eyes with the call-rate hold."},
  {"need": "topo", "why": "Daubenton's bat has its sharp area in the upper retina, which looks at the lower field (the sheet's inference). The engine places sharpness only at the centre or along the horizon."},
  {"need": "compass", "why": "Big brown bats steer by the magnetic field (Holland 2006). Reading the sensor is easy; there is no basis yet for drawing it."}],
 "rows": bat_rows})
write("flyingfox", {"key": "flyingfox", "chip": "Flying fox, fruit bat", "who": "a flying fox", "falls_back_to": "other",
 "applies_to": {"family": ["Pteropodidae"]},
 "cue": "The picture is coarse and muted, and the shadows are lifted.", "modules": [],
 "params": {
  "cpd": P(4, "m", False, [S+"bat.md#2 flyingfox Sharpness: Cechetto 2020 (Pteropus poliocephalus, P. alecto, Rousettus aegyptiacus about 4)"], [1, 10], "Brokaw 2024 gives about 2 for the Indian flying fox"),
  "pupil": P("o", "i", True, [], None, "no source was found"),
  "M": P("flyingfox_deutan", "g", True, [S+"bat.md#2 flyingfox Colour: Muller 2007 (Pteropus has two cone types)"], None, "the engine's two-cone model, following the cat, dog and deer; which human model fits depends on where the long-wave cone peaks (open question 4 in the sheet)"),
  "sat": P(.7, "i", True, [S+"bat.md#2 flyingfox Colour: Muller 2007 (cones about one in two hundred receptors)"], [0, 1], "the amount of drain is the app's"),
  "gain": P(1.5, "i", True, [S+"bat.md#2 flyingfox Dim light: Brokaw 2024"], [1, 3], "the amount is the app's")},
 "matrices": {"flyingfox_deutan": mat([[0.29275, 0.70725, 0], [0.29275, 0.70725, 0], [-0.02234, 0.02234, 1]], "g", True, [S+"bat.md#3 flyingfox M"], "Vienot, Brettel and Mollon 1999, as in the cat and dog views; entered from memory")},
 "variants": {"one_cone": {"note": "Rousettus, Eidolon and Epomophorus have only the green cone and no blue (Muller 2007): the picture would be grey. The sheet follows the flying foxes and leaves this for a genus override.",
   "applies_to": {"genus": ["Rousettus", "Eidolon", "Epomophorus"]},
   "params": {"sat": P(0, "g", True, [S+"bat.md#2 flyingfox One cone: Muller 2007"], [0, 1])}}},
 "notes": [
  {"need": "uv", "why": "The Formosan flying fox's blue cone gene points to ultraviolet (Wang 2004). No sheen is drawn: several bat lineages have lost the cone."},
  {"need": "sound", "why": "Rousettes echolocate with tongue clicks (Yovel 2011); no echoes are drawn."}],
 "rows": ff_rows})

# ------------------------------------------------------------------ tick
TI = S + "tick.md"
tick_rows = check_rows("tick", rows_between(TI, "## 2. The rows", "## 3.", {
    "Shapes": ["cpd"], "Colour": ["M"]}, S + "tick.md#2"))
write("tick", {"key": "tick", "chip": "Tick", "who": "a tick", "falls_back_to": "other",
 "applies_to": {"order": ["Ixodida"]},
 "cue": "Hold the phone at the height of the grass tips and tilt it up. Only large shadows remain.", "modules": [],
 "params": {
  "cpd": P(.1, "g", True, [S+"tick.md#3 cpd: Kaltenrieder 1990 (Hyalomma dromedarii, 4.8 degree dark disc)"], [.03, .5], "a detection threshold read as half a cycle; the conversion is the sheet's own step, and the threshold is lower in the camel tick than in the bont tick, so it may flatter the commoner ticks"),
  "pupil": P("none", "i", True, [], None, "no source describes a pupil in tick eyes; gives the same output as o"),
  "M": P("tick_blue_green", "g", True, [S+"tick.md#2 Colour: Kaltenrieder, Labhart and Hess 1989 (single peak near 480 nm, Amblyomma variegatum)"], None, "grey from the camera's blue and green; the weights are the app's")},
 "matrices": {"tick_blue_green": mat([[.05, .45, .5], [.05, .45, .5], [.05, .45, .5]], "g", True, [S+"tick.md#3 M"], "weights invented")},
 "notes": [
  {"need": "mask", "why": "Two eyes aimed up and out (39 degrees out and 33 up in the bont tick). The aperture mask could take a two-window shape; the outer parts would be invented."},
  {"need": "heat, breath", "why": "Haller's organ reads radiant heat and carbon dioxide (Carr and Salgado 2019; Steullet and Guerin 1992). No phone input a web page can read stands in. The sheet recommends against painting warmth on skin colours; a body-detector spot is the closer stand-in and would be graded i."},
  {"need": "persist", "why": "Left unset on purpose: the plant's averaging would erase the passing shadow that ticks respond to."}],
 "rows": tick_rows})
print("wrote crab mammal salamander worm bat flyingfox tick")
