"""Writes views/<key>.json for the first eight groups (fungus, slime, fish, shark, spider, snail, sealife).
Run from the repository root: python3 tools/views/make_specs_a.py. Each value is entered with its grade, source and range."""
import json, os
def P(v, g, inv, src=(), rng=None, note=None, floor=None):
    d = {"value": v, "grade": g, "invented": inv, "src": list(src)}
    if rng is not None: d["range"] = rng
    d["floor"] = floor
    if note: d["note"] = note
    return d
def R(g, title, text, *src): return [g, title, text, list(src)]
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
# ---------------------------------------------------------------- fungus
write("fungus", {"key": "fungus", "chip": "Mushroom, lichen", "who": "a fungus", "falls_back_to": "plant",
 "applies_to": {"kingdom": ["Fungi"]},
 "cue": "There is no picture here, only how much blue and green light, and from where, slowly.", "modules": ["slow"],
 "params": {
  "field": P(1, "g", True, [S+"fungus.md#2 No picture: He and Liu 2005; Sanz 2009"], [0, 1], "the plant's coarse light-only drawing"),
  "pupil": P("none", "i", True, [], None, "follows from No picture"),
  "M": P("fungus_blue_green", "g", True, [S+"fungus.md#2 Colour: Schwalb and Shanler 1974; Moore 2016"], None, "red dropped, blue weighted over green; the weights are the app's"),
  "gain": P(2, "i", True, [], [1, 4], "stands for sensitivity to faint light (Galland and Russo 1984 give the threshold)"),
  "persist": P(20, "i", True, [], [0, 60], "seconds; real responses take minutes to hours, so this falls far short")},
 "matrices": {"fungus_blue_green": mat([[0, .4, .6], [0, .4, .6], [0, .4, .6]], "g", True, [S+"fungus.md#3"])},
 "notes": [{"need": "slow", "why": "A fungus answers over minutes to hours; persist cannot hold more than a few seconds (the 0.2 floor without float textures). A low-rate frame store (module 12) would show the real pace."},
           {"need": "motion", "why": "Gravity: a stem rights itself in 3 to 4 hours; the phone's tilt could turn the picture back. Not drawn."},
           {"need": "field", "why": "The whole field could lean slowly toward the brightest region. Not drawn."}],
 "rows": [
  R("g", "No picture", "A fungus has no eye. Its cells read how much light there is, mostly blue and green, and which way it comes from.", S+"fungus.md#2", "param:field", "param:pupil"),
  R("m", "Colour", "The young stalk of the split gill mushroom bends toward violet and green light and ignores orange and red. Another gilled mushroom, Coprinopsis cinerea, needs a little blue light to form a mushroom, and in the dark it grows a long stem under an unfinished top.", "Schwalb and Shanler 1974", "Moore 2016", "Terashima 2005", "param:M"),
  R("g", "Red", "Some moulds read red as well. Aspergillus nidulans uses phytochrome, the red receptor of plants, and red light holds back its sexual spores. The picture follows the mushrooms and leaves red dark.", "Blumenstein 2005"),
  R("g", "Faint light", "The stalk of the pin mould Phycomyces turns toward light as faint as a billionth of a watt on a square metre, and it still steers in light ten billion times brighter.", "Galland and Russo 1984", "Sanz 2009", "Shropshire 1962", "param:gain"),
  R("m", "Down", "A mushroom stem laid on its side starts to turn up in about 25 minutes, and its tip is upright again within 3 to 4 hours. The gills of a field mushroom turn back toward straight down within an hour, so the spores fall clear.", "Kher 1992", "Moore 1996", "Moore 1994"),
  R("g", "Pace", "Genes that light switches on in the mould Neurospora peak 15 to 30 minutes later, and the pin mould stalk starts to bend within 5 minutes. Your eyes follow flicker to about 60 a second.", "He and Liu 2005", "Sanz 2009", "Inger 2014"),
  R("m", "Lichens", "A lichen is a fungus with algae living inside it, and the algae make food from light. The orange lichen Xanthoria parietina makes a pigment, parietin, in its outer layer, and the pigment soaks up blue light and some ultraviolet.", "Gauslaa and Ustvedt 2003", "Lange 1986"),
  R("x", "Water", "A lichen with green algae can wake from damp air alone, and one with blue-green algae needs liquid water. The picture does not show how wet anything is.", "Lange 1986"),
  R("x", "Food", "The threads of a wood-rotting fungus grow across soil to new wood and remember the side that faced it. The picture has nothing for this.", "Fukasawa 2020"),
  R("i", "Colour and time", "Green counts for less than blue, dim light is lifted, and changes are averaged over about 20 seconds. A fungus answers light over minutes to hours, far slower than this. These choices are the app's own.", "param:M", "param:gain", "param:persist")]})
# ---------------------------------------------------------------- slime
write("slime", {"key": "slime", "chip": "Slime mould", "who": "a slime mould", "falls_back_to": "plant",
 "applies_to": {"phylum": ["Mycetozoa"]},
 "cue": "There is no picture here, only how much light, what colour, and from where.", "modules": ["slow"],
 "params": {
  "field": P(1, "g", True, [S+"fungus.md#2 slime No picture: Nakagaki 2000; Hato 1976"], [0, 1]),
  "pupil": P("none", "i", True),
  "noGreen": P(1, "i", True, [], [0, 1], "red and blue both steer it (Hato 1976); green was untested"),
  "persist": P(6, "i", True, [], [0, 30], "seconds; its body pulses every 1 to 2 minutes (Kuroda 2015)")},
 "notes": [{"need": "field", "why": "A well-fed plasmodium moves away from light and a starved one toward it. The whole field could lean away from or toward the brightest region. Not drawn."}],
 "rows": [
  R("g", "No picture", "A slime mould is one huge cell, from a kingdom apart from the fungi. It has no eye, and it reads how much light falls on it and of what colour.", "Nakagaki 2000", "Hato 1976", "param:field", "param:pupil"),
  R("m", "Colour", "Physarum polycephalum crawls away from blue light and far-red light, and toward red light.", "Hato 1976"),
  R("m", "Hunger", "Well fed, it moves away from light. Short of food, it moves toward light, and after several days without food, light turns it into spore heads.", "Leitner 2002", "Masui 2025"),
  R("x", "Food", "It stretches tubes between pieces of food and finds the shortest route between them through a maze. The picture has no sense of food.", "Nakagaki 2000"),
  R("m", "Pace", "Its body swells and thins every one to two minutes, and its speed rises and falls over about 20 minutes. Your eyes follow flicker to about 60 a second.", "Kuroda 2015", "Inger 2014"),
  R("i", "Colour and time", "Green is removed and changes are averaged over about 6 seconds. Both choices are the app's own.", "param:noGreen", "param:persist")]})
# ---------------------------------------------------------------- fish
FL = S+"fish.md#3"; D = "docs/views/drafts/fish-shark.md"
write("fish", {"key": "fish", "chip": "Fish", "who": "a fish", "falls_back_to": None,
 "applies_to": {"clade": ["Actinopterygii"]},
 "cue": "Detail is coarse and the field is wide. Tap the screen to move the focus.", "modules": [],
 "params": {
  "fov": P(335, "g", False, [D+"#fish log 86: Pita 2015 (Golden Shiner)"], [180, 360]),
  "cpd": P(4, "g", True, [D+"#fish logs 84, 38, 88: Northmore 2007; Spratte 2021; Pita 2015"], [.5, 10], "inside the measured 2.9 to 5"),
  "topoA": P(1, "g", False, [D+"#fish logs 40, 89"], [0, 1]),
  "topoS": P(.5, "g", True, [D+"#fish log 40"], [0, 1], "the mix of the two is the app's"),
  "fall": P(1.4, "g", True, [D+"#fish log 88: peak 2.86, edge 1.18"], [0, 3], "2.86 over 1.18 is 2.4 times coarser; fall is the engine's convention"),
  "pupil": P("o", "i", True, [], None, "a fish iris mostly does not move (log 104); the round shape is the app's"),
  "dof": P(8, "i", True, [D+"#fish log 104"], [0, 30], "a wide-open eye is shallow in depth of field; strength is the app's"),
  "sheen": P(.5, "i", True, [D+"#fish logs 112, 114"], [0, 1], "invented violet sheen for ultraviolet cones"),
  "rate": P(1, "i", True, [D+"#fish log 68"], [.3, 1.2], "the measured mean (46 Hz) sits below 60, so the person's pace is kept")},
 "matrices": {"sunfish_no_blue": mat([[1, 0, 0], [0, 1, 0], [0, 1, 0]], "g", True, [S+"fish.md#2 Colour: Mitchem 2019"], "blue takes the green signal: blue goes dark, yellow goes pale")},
 "by": {"family": {"Centrarchidae": {"params": {"M": P("sunfish_no_blue", "g", True, [S+"fish.md#2 Colour: Mitchem 2019"]), "sheen": P(0, "g", False, [S+"fish.md#2 Ultraviolet: Mitchem 2019"])}},
                   "Pomacentridae": {"params": {"cpd": P(2, "g", True, [D+"#reef logs 90, 91"], [.5, 10]), "sheen": P(.6, "i", True, [D+"#reef logs 62, 110"], [0, 1]), "rate": P(.86, "g", True, [D+"#reef log 65: 60 over 70"], [.3, 1.2])}}},
        "order": {"Siluriformes": {"params": {"cpd": P(2, "i", True, [D+"#fish catfish setting"], [.5, 10]), "gain": P(1.3, "i", True, [D+"#fish log 60"], [1, 3])}}}},
 "variants": {"reef": {"note": "Sea fish, from the engine agent's prototype TRY.reef (agent/engine, src/cam.a.js) and the draft's reef entry; the prototype adds two independent gazes and water colour, which need modules.",
   "params": {"cpd": P(2, "g", True, [D+"#reef logs 90, 91"], [.5, 10]), "fall": P(1.6, "i", True, [], [0, 3]), "topoS": P(.4, "g", True, [D+"#reef log 144"], [0, 1]), "rate": P(.86, "g", True, [D+"#reef log 65"], [.3, 1.2]), "sheen": P(.6, "i", True, [D+"#reef logs 62, 110"], [0, 1])},
   "matrix": {"rows": [[.35, 0, 0], [0, 1, 0], [0, 0, 1]], "grade": "g", "invented": True, "src": [D+"#reef logs 108, 110"]}}},
 "notes": [{"need": "zones", "why": "Reef fish have two eyes that look their own ways, each with a small sharp centre (TRY.reef draws them as two gazing zones)."},
           {"need": "field", "why": "Snell's window: looking up, the sky is pressed into a circle about 97 degrees across (Sabbah 2006)."},
           {"need": "light", "why": "Water colour by distance and depth: reds fade within 10 to 20 m in the sea; fresh water in Florida is often tea-coloured (logs 71, 72, 132)."}],
 "rows": [
  R("m", "Sharpness", "A bluegill resolves about 5 cycles per degree and a pumpkinseed about 3.6, against your 60. The screen is blurred to what such an eye would keep of it.", "Northmore 2007", "Spratte 2021", "param:cpd"),
  R("m", "Colour", "Largemouth bass have two cone types, near 535 and 614 nanometres, and none for blue. Trained bass confused blue with black and yellow-green with white, so for sunfish blue goes dark and yellow goes pale.", "Mitchem 2019"),
  R("g", "Field", "A golden shiner sees about 335 degrees around itself, 31 of them with both eyes, and is blind only in a wedge of 25 degrees behind. The camera holds a slice of it, and the rest is invented.", "Pita 2015", "param:fov"),
  R("g", "Where it is sharp", "A golden shiner sees most sharply a little ahead and above, at 2.9 cycles per degree, and at 1.2 toward the edges.", "Pita 2015", "param:topoA", "param:fall"),
  R("g", "Pace", "A spiny damselfish follows flicker to 89 a second, and the bony fish in one survey average 46. You stop near 60, so the picture keeps your pace.", "Chung 2014", "Inger 2014"),
  R("x", "Looking up", "Under calm water the whole sky is squeezed into a circle about 97 degrees across. The picture leaves it out for now.", "Sabbah 2006"),
  R("x", "Water moving", "Sensors along the body feel the flow and pressure of the water, and fish steer by them in the dark. The picture leaves it out.", "Zhai 2020"),
  R("x", "Ultraviolet", "Clownfish and goldfish have a cone for it, and a clownfish tells colours apart better with it. Bass have none.", "Mitchell 2024", "Joselevitch 2010"),
  R("i", "How it is drawn", "The round pupil, the shallow focus, the violet sheen and the choice of 4 cycles per degree are the app's own settings, set inside the measured range.", "param:pupil", "param:dof", "param:sheen", "param:rate", "param:cpd", "param:topoS")]})
# ---------------------------------------------------------------- shark
write("shark", {"key": "shark", "chip": "Shark, ray", "who": "a shark or ray", "falls_back_to": "fish",
 "applies_to": {"class": ["Chondrichthyes"]},
 "cue": "There is no colour, only light and dark, and movement leaves trails.", "modules": [],
 "params": {
  "fov": P(300, "i", True, [D+"#shark log 93"], [180, 360], "eyes on the sides with small overlaps; the total was not opened"),
  "cpd": P(5, "g", False, [D+"#shark logs 11, 24, 97"], [.2, 10]),
  "topoS": P(1, "g", False, [D+"#shark logs 98, 102, 103"], [0, 1], "horizontal streaks"),
  "fall": P(1.5, "i", True, [], [0, 3]),
  "pupil": P("o", "i", True, [D+"#shark log 105"], None, "shark pupils vary in shape"),
  "dof": P(14, "i", True, [D+"#shark log 157"], [0, 30]),
  "M": P("shark_grey", "g", True, [D+"#shark logs 19, 20, 141"], None, "every channel takes green, so the picture is grey"),
  "gain": P(1.3, "g", True, [D+"#shark logs 106, 107"], [1, 3], "the amount is the app's"),
  "persist": P(.04, "g", False, [D+"#shark log 67: 1/26.1 s; logs 122, 123"], [0, .3])},
 "matrices": {"shark_grey": mat([[0, 1, 0], [0, 1, 0], [0, 1, 0]], "g", True, [D+"#shark logs 19, 20, 141"])},
 "variants": {"ray": {"note": "Rays differ: two or three cone types, a field up to the whole circle, and cpd .2 (logs 15, 94, 95). Skates have rods only (logs 27, 125).", "params": {"fov": P(360, "i", True, [], [180, 360]), "cpd": P(.2, "g", False, [D+"#ray log 15"], [.05, 10]), "persist": P(.08, "g", False, [D+"#ray log 124"], [0, .3])}}},
 "notes": [{"need": "zones", "why": "A near band where the electric sense works (TRY.shark glows moving things in the lower band); the head's sideways sweep (TRY.shark sweep). Neither is drawn with today's fields."},
           {"need": "field", "why": "Snell's window, as for fish."}],
 "rows": [
  R("m", "Colour", "Every shark studied so far has only one kind of colour-sensing cell, so sharks are probably colour blind. They can tell apart shades of brightness that differ by less than 2 percent. This view shows the world in shades of grey.", "Hart 2011", "Hart 2020", "param:M"),
  R("m", "Sharpness", "Sharks see between a twentieth and a sixth as much detail as you do. Fast hunters of open water are at the sharp end and bottom-dwelling night hunters at the coarse end. This view uses the middle of that range.", D+"#shark logs 11, 24, 97", "param:cpd"),
  R("m", "Sharpest band", "Many sharks, such as the lemon shark, see most sharply along a band level with the horizon, which lets them scan the sea floor or the open water without moving their eyes. This view sharpens a band along the horizon.", D+"#shark logs 98, 102, 103", "param:topoS"),
  R("m", "Pace", "Sharks follow a flickering light up to 16 to 31 flashes a second, a quarter to a half of your rate, so quick movement smears. This view leaves trails behind anything that moves.", D+"#shark log 67", "Inger 2014", "param:persist"),
  R("m", "Electric sense", "Sharks feel the faint electric fields around living animals through gel-filled pores on the snout. The picture leaves this out; no phone can sense an electric field.", "Kalmijn 1971"),
  R("i", "Field and the rest", "The field of view, the falloff from the sharp band, the pupil, the depth of focus and the dim-light lift are the app's own settings.", "param:fov", "param:fall", "param:pupil", "param:dof", "param:gain", "param:M"),
  R("x", "Smell first", "A hunting shark usually smells its prey first and follows the scent upstream, then turns to sight, the lateral line, the electric sense and touch as it closes in. The picture leaves smell out.", D+"#shark")]})
# ---------------------------------------------------------------- spider
SP = S+"spider.md#3"
write("spider", {"key": "spider", "chip": "Spider", "who": "a spider", "falls_back_to": None,
 "applies_to": {"order": ["Araneae"]},
 "cue": "Hold still, as a spider holds its web. Only what moves reaches you.", "modules": ["motion", "sound"],
 "inputs": {"motion": "optional", "sound": "optional", "haptic": "none"},
 "params": {
  "fov": P(300, "i", True, [S+"spider.md#3 fov: Land and Barth 1992"], [180, 360]),
  "cpd": P(.5, "g", False, [S+"spider.md#2 Sharpness: Land and Barth 1992 (Cupiennius salei)"], [.1, 5]),
  "pupil": P("o", "i", True),
  "gate": P(1, "i", True, [], [0, 1], "stands in for the web, which the engine cannot draw"),
  "persist": P(.15, "g", False, [S+"spider.md#2 Pace: Fenk and Schmid 2011"], [0, .5], "seconds; between 1/8.6 and 1/4.3")},
 "notes": [{"need": "motion", "why": "The web's shaking is the main sense of the commonest spiders (Landolfa and Barth 1996). A knock on the phone, read from the accelerometer at 60 a second or more, could send ripples from the side it came from. TRY.spider has a prototype (ripple, senses.jolt)."},
           {"need": "sound", "why": "A bridge spider's web works as a listening surface (Zhou 2022); a low sound band from the microphone could stand in. TRY.spider has senses.mic."}],
 "rows": [
  R("m", "The web", "A Golden Silk Spider feels its prey through the silk, and a trapped insect shakes the web 5 to 30 times a second. The shaking arrives ten to thirty times stronger on some legs than on others, which gives the direction.", "Landolfa and Barth 1996"),
  R("g", "Eyes", "Most spiders have eight eyes and few see well. Most register little more than changes between light and dark, and spiders that build webs lean on the shaking of the silk.", "Australian Museum", "Stafstrom and Hebets 2016", "Clemente 2005"),
  R("g", "Sharpness", "A wandering spider resolves nothing finer than about 2 degrees, under a hundredth of your sharpness. The picture borrows that figure for web builders.", "Land and Barth 1992", "param:cpd"),
  R("g", "Pace", "A wandering spider stops following flicker between 4.3 and 8.6 times a second, a seventh of your rate or less, so movement smears into trails.", "Fenk and Schmid 2011", "param:persist"),
  R("g", "Colour", "Orb weavers of the yellow garden spider's genus carry ultraviolet, blue and green receptors in some of their eyes. Colour is left as the camera gives it, and their ultraviolet is not drawn.", "Morehouse 2020"),
  R("i", "Drawn as", "The picture cannot draw the shaking of the web. Only what moves is shown in its place, so hold the phone as still as a spider holds its web. The field of view and the round pupil are the app's own.", "param:gate", "param:fov", "param:pupil"),
  R("x", "Hearing through silk", "A bridge spider turns toward a loudspeaker three metres away, because its web moves with the air and works as a listening surface up to 10,000 times larger than its body. The picture has no sound.", "Zhou 2022"),
  R("x", "Wolf spiders", "Wolf spiders have four large rear eyes backed by a mirror layer, which shines back in a flashlight beam and helps them spot movement in dim light. This picture leaves that out.", "Australian Museum")]})
# ---------------------------------------------------------------- snail
SN = S+"snail.md#3"
write("snail", {"key": "snail", "chip": "Snail", "who": "a snail or slug", "falls_back_to": None,
 "applies_to": {"class": ["Gastropoda", "Polyplacophora", "Scaphopoda"]},
 "cue": "Hold the phone close to the ground and move it slowly. Only the largest patches of light and dark remain.", "modules": [],
 "params": {
  "cpd": P(.035, "g", True, [S+"snail.md#2 Sharpness: Serb and Eernisse 2008 (14.5 degrees, Helix); Irwin 2022 (52 degrees, Arion)"], [.01, .06], "1 over 2 times 14.5; the red slug's 52 degrees gives .010, the eyed chiton's 9 degrees gives .056"),
  "pupil": P("o", "g", True, [S+"snail.md#2 Eyes: Shepeleva 2023"], None, "with dof unset the shape is not seen"),
  "M": P("snail_blue_grey", "m", True, [S+"snail.md#2 Colour: Matsuo 2023 (480 nm dark, 420 nm light)"], None, "grey weighted to blue; the weights are the app's")},
 "matrices": {"snail_blue_grey": mat([[.05, .3, .65], [.05, .3, .65], [.05, .3, .65]], "m", True, [S+"snail.md#3"])},
 "by": {"family": {"Strombidae": {"params": {"cpd": P(1, "g", True, [S+"snail.md#2 Sea snails: Irwin 2022 (1.06 degrees)"], [.1, 3])}}}},
 "notes": [{"need": "field", "why": "Light sensed outside the eyes (the blinded slug, the pond snail's skin) is a whole-field glow that follows overall brightness. Not drawn."},
           {"need": "zones", "why": "The chiton's dome of shell eyes, and two eyes on moving tentacles. Not drawn."}],
 "rows": [
  R("m", "Eyes", "A land snail or slug has a small eye with a lens at the tip of each upper tentacle. In the White-lipped Snail each eye is about a quarter of a millimetre across.", "Nishiyama 2019", "Shepeleva 2023"),
  R("m", "Sharpness", "The garden snail's eye resolves about 15 degrees, so it keeps under a thousandth of the detail you see. Behaviour tests put a red slug's resolution at about 52 degrees.", "Serb and Eernisse 2008", "Irwin 2022", "param:cpd"),
  R("m", "Colour", "A slug's eye is most sensitive to blue near 480 nanometres in the dark and to violet near 420 in daylight. The picture is drawn in grey weighted to blue.", "Matsuo 2023", "Nishiyama 2019", "param:M"),
  R("m", "Light without eyes", "A slug whose eyes have been removed still crawls away from bright light, which it senses with its brain.", "Nishiyama 2019"),
  R("g", "Shadows", "A pond snail pulls back into its shell when a shadow falls on it. It feels the shadow through its skin, most strongly in blue-green light near 490 nanometres.", "Sunada 2012"),
  R("g", "Sea slugs", "A nudibranch's eyes lie deep under the skin behind its rhinophores. Even so, one nudibranch crawled toward a black stripe placed outside its arena.", "Rudman 1999", "Quinlan 2021"),
  R("m", "Chitons", "One Caribbean chiton has hundreds of tiny eyes in its shell, with lenses of the mineral aragonite, and it clamps down when a dark disc 9 degrees wide appears overhead.", "Speiser 2011", "Kingston 2018"),
  R("g", "Sea snails", "One conch reacts to objects about 1 degree across, and a periwinkle's eye holds detail of about 4 degrees. Both see far more than this picture shows.", "Irwin 2022"),
  R("x", "Smell", "A giant African land snail finds a smell on the air with its upper tentacles and follows a slime trail with its lower ones. This reaches no camera.", "Chase and Croll 1981"),
  R("i", "How it is drawn", "Choosing the garden snail's figure over the coarser slug figure, and the blue-heavy grey, are the app's own settings. The round pupil is the app's too.", "param:cpd", "param:M", "param:pupil")]})

# ---------------------------------------------------------------- sealife (starfish and sea urchin as a variant)
SE = S+"sealife.md#"
write("sealife", {"key": "sealife", "chip": "Coral, anemone, jellyfish, clam", "who": "a sea creature", "falls_back_to": "plant",
 "applies_to": {"phylum": ["Cnidaria", "Mollusca", "Porifera", "Echinodermata", "Bryozoa", "Ctenophora", "Chordata"]},
 "cue": "No picture here. Only how much light there is and where it comes from. Pass your hand over the lens to cast a shadow.", "modules": ["light"],
 "params": {
  "field": P(1, "i", True, [SE+"2 Shadows: Kennedy 1960", SE+"2 Moon jellies: Nakanishi 2009"], [0, 1]),
  "pupil": P("none", "i", True, [], None, "as for the plant"),
  "M": P("sea_blue_green", "i", True, [SE+"2 Full moon: Levy 2007", SE+"2 Blue moonlight: Grawunder 2015", SE+"2 Shadows: Kennedy 1960"], None, "grey weighted to blue and green; no colour discrimination is claimed")},
 "matrices": {"sea_blue_green": mat([[.05, .4, .55], [.05, .4, .55], [.05, .4, .55]], "i", True, [SE+"3"])},
 "variants": {"starfish": {"note": "Starfish, sea urchin (and for now sea cucumbers and brittle stars): a grey field of a few soft patches that runs slow.",
   "params": {"fov": P(300, "i", True, [], [180, 360]), "cpd": P(.06, "g", True, [SE+"2 Sharpness: Petie 2016 (8 degrees); Yerramilli and Johnsen 2010"], [.03, .2]),
              "sat": P(0, "g", False, [SE+"2 Grey and slow: Garm and Nilsson 2014"], [0, 1]), "persist": P(.6, "i", True, [], [0, 2], "from 1 to 2 flashes a second; the flicker figure is secondary"), "pupil": P("none", "i", True), "field": P(0, "i", True, [], [0, 1])}}},
 "notes": [{"need": "light", "why": "A shadow as an event (a flinch when the frame darkens), and the moon's phase from the date (Lin 2021; Levy 2007). Not drawn; graded i if added."},
           {"need": "zones", "why": "Starfish look out from each arm at once (a flat band 100 by 30 degrees each); scallops and giant clams have rows of small eyes. Not drawn."}],
 "rows": [
  R("i", "No picture", "Sea anemones and corals have no eyes. The picture keeps only how much light there is, what colour it is and where it comes from.", "param:field", "param:pupil", "param:M"),
  R("m", "Full moon", "A reef coral makes more of one blue-light pigment on full-moon nights than on new-moon nights. Hundreds of kinds of coral spawn together on a few nights each year, and moonlight helps set those nights.", "Levy 2007"),
  R("m", "The dark hour", "One reef coral spawns after the moon starts rising late, leaving a stretch of darkness after sunset. A dim light of about 0.3 lux at night held its spawning back.", "Lin 2021"),
  R("m", "Blue moonlight", "A small sea anemone released its eggs and sperm in step only when blue light, standing in for a full moon, shone through five nights of each month. White light did little.", "Grawunder 2015"),
  R("g", "Shadows", "A surf clam has a nerve that senses light by itself. When a shadow falls, the nerve fires a burst and the clam pulls in its siphon.", "Kennedy 1960"),
  R("m", "Moon jellies", "A moon jelly has small cups of light-sensing cells around its rim, and it swims faster in brighter light. Without those cups it no longer does.", "Nakanishi 2009 (secondary: Wikipedia, Rhopalium)"),
  R("x", "Scallops and giant clams", "A scallop has up to 200 eyes along the edge of its shell, each focusing light with a mirror, and a giant clam has several hundred pinhole eyes. This view does not draw them.", "Palmer 2017", "Land 2003"),
  R("x", "Box jellyfish", "Box jellyfish have 24 eyes, some with lenses, and one kind looks up through the water to steer by the trees above it. This view does not draw them.", "Garm 2011", "Nilsson 2005"),
  R("g", "Eyes at the arm tips", "A starfish has an eye at the tip of each arm. In the crown-of-thorns starfish each eye has about 250 tiny facets and looks out sideways over a patch about 100 degrees wide and 30 high.", "Petie 2016"),
  R("g", "Grey and slow", "The blue sea star is colour blind, and its eyes follow flicker only up to 1 or 2 times a second, against about 60 for yours. The starfish picture is grey, and anything that moves smears.", "Garm and Nilsson 2014 (the 1 to 2 hertz is secondary)"),
  R("m", "Sea urchins", "A purple sea urchin has no eyes, yet it turned toward or away from a dark disc 10 degrees wide and ignored one 6.5 degrees wide. Its spines shade the light-sensitive cells between them.", "Yerramilli and Johnsen 2010", "Ullrich-Luter 2011"),
  R("i", "How it is drawn", "The grey weights, the choice of a light-only picture for animals that have no eyes, and the slow pace of the starfish picture are the app's own.", "param:M", "param:field")]})
print("ok")
