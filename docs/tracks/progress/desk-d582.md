# desk-d582 progress

Angle: sensory anatomy (nostril, ear opening, tympanum, eyelid, iris, pupil in text) from open-licence (CC BY) Pensoft descriptions; the OLD-ANGLE paragraph was ignored. 13 records (docs/views/evidence/desk-d582.jsonl), trait sensory_anatomy; evidence_kind anatomical_presence except two anatomical_measurement (Boulenophrys youran TD/ED 0.62; Rhacophorus medogensis tympanum diameter 2.2 mm). One record per finding. About 39 WebSearches; no Crossref, no proxy hosts; every WebFetch URL came from my own search results. check.py: 0 problems for this file (plain and --require-evidence-kind).

## Filed (licence sentence read on each publisher article_preview page; authority page opened from my own search)
- Scincella jinchuanensis, ZSE 102(2): 575-588 (10.3897/zse.102.184613): ear opening oval and size against palpebral window and eye diameter; tympanic membrane recessed (same whole 38-word sentence, two records); lower-eyelid transparent disc; nostril centred in the oval nasal. Reptile Database page.
- Boulenophrys youran, ZSE 102(1): 53-70 (10.3897/zse.102.175092): pupil vertically diamond-shaped; nostril lateral, closer to snout than eye; TD/ED 0.62; iris copper-brown (in life). Opening of the long description sentences with cuts marked. ASW page.
- Rhacophorus medogensis, ZSE 101(2): 437-447 (10.3897/zse.101.142297): pupil horizontal; nostrils oval, lateral, slightly protuberant, nearer snout tip; tympanum diameter 2.2 mm; iris orange brown (in life). ASW page.
- Cyrtodactylus awalriyantoi, ZooKeys 1168: 367-386 (10.3897/zookeys.1168.98724): nares oval, bordered by rostral, supranasals, internasals and first supralabial (whole sentence). Reptile Database page.

## Weak spots
- All text came through the WebFetch page reader (about 100 characters per piece); long semicolon sentences were reassembled from numbered pieces and quoted from the sentence start with the cut marked. Auditors should re-read quotes on the publisher pages.
- Scincella jinchuanensis: the preservation sentence came back only as two quoted fragments; the Methods define no ear-opening or eye character; the heading path reported by the reader prints no 'Taxonomic account' heading.
- Boulenophrys youran: no table prints TD/ED, so 0.62 cannot be checked against a table; TD is read as tympanum diameter from the Methods 'TYD (maximal tympanum diameter)'; 'an distinct margin' is the printed wording.
- Rhacophorus medogensis: Methods do not define ED or TD (inline expansions only); holotype TD 2.2 mm agrees with the table values the reader returned; the pupil and nostril clauses sit deep in a roughly 208-word sentence.
- Cyrtodactylus awalriyantoi: the nares sentence is under 'Description (and variation)', not tied to the holotype alone.

## Not filed and why
- Dasypeltis albigularis (Herpetozoa 39: 343-366), Ovophis langbianus (Herpetozoa 39: 325-342; short pupil, nostril and iris sentences read), Acanthosaura aurantiogularis (ZooKeys 1290), Trachischium lalremsangai, Oligodon churahensis, Scincella dabieshanensis, Plagiopholis yangi: no Reptile Database species page appeared in my own searches.
- Scincella maerkangensis (same paper as S. jinchuanensis): sensory sentences over 40 words.
- Calamaria incredibilis, Gekko tesselatus, Gekko wuzhengjuni, Leptobrachella xinshaoensis, Cyrtodactylus makwanpurgadhiensis, C. peninsularis: species already on main (evidence rows).
- Kaloula discordia and K. laosensis (Herpetozoa 37: 391-420): the preview text ends before the species descriptions.
- Leptobrachella yachangensis: no article_preview reached; XML cut before the description.
- Gracixalus liusanjieae (ZSE 101(4)) and G. huaping (ZSE 101(1)): not on main, titles reached, texts not opened (leads).

## Desk disposition after audits 1138, 1139 and 1140 (4 November 2026)
Two pupil-shape lines (Boulenophrys youran, Rhacophorus medogensis) were moved to trait pupil_shape by the auditors; two iris-colour-in-life lines were dropped because no trait fits. Fixable faults (title, heading path, conditions, grep list, preservation note) were corrected with the auditors replacement text. 11 of 13 merged. Ruling for later units: file no iris colour.
