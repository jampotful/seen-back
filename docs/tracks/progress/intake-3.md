# Intake 3 progress note (round 2 Drive intake)

Branch: research/intake-3, cut from main. Launch prompt: docs/tracks/prompts/round2-intake.md.
Status: complete for this prompt (ten files read, records logged, drive.jsonl written, wanted lines added).

## Files (ten named in the launch prompt, keyed by sha1 of the Drive id)
All ten downloaded, decoded, and run through pdftotext -layout. None over 10 MB (largest 2.6 MB). Titles from the Drive names match the launch prompt's labels.

| sha1 key | file | DOI | wanted unit | logged | status |
|---|---|---|---|---|---|
| e61667cd6e3d | Chatterjee 2020 | 10.1007/s00359-020-01429-3 | insects-met | 9 | read in full |
| 101b48fd7a6c | Cervino 2021 | 10.1098/rspb.2021.1402 | herps-met | 4 | read in full |
| e3ec00e406be | Odeen 2003 | 10.1093/molbev/msg108 | birds-met | 12 | read in full |
| dd1efaef2dfe | Martinez 2022 Ophthalmology of Crocodilia | 10.1007/978-3-030-71302-7_15 | herps-met | 1 | PARTIAL (abstract and reference list) |
| 78d5a3419d9c | Hebel 1976 | 10.1007/bf00346285 | mammals-met | 10 | read in full |
| 611f5baf89d7 | Gaffney 2003 | 10.1016/s0042-6989(03)00304-3 | birds-met | 2 | read in full |
| 321a986fc9c5 | Entsu 1992 | 10.1016/s0168-1591(05)80052-8 | mammals-met | 4 | read in full |
| cbf0d73ac4c0 | Porter 2014 | 10.1242/jeb.108456 | birds-met | 9 | read in full |
| 5c425bae3a47 | Nakagaki 1996 | 10.1111/j.1751-1097.1996.tb01847.x | plant-fungus-slime | 3 | PARTIAL (name ends "(partial)"; abstract and reference list) |
| 9e9b56a8ddba | Braekevelt 1990 | none | none by DOI (duck view by species) | 0 | read in full; 3 records held (see below) |

drive.jsonl: ten lines appended. No key was present on main before this run.

## Records
- evidence/intake-3.jsonl: 54 records, all pass quotecheck (verbatim or table) and the repo checker (tools/senses/check.py: 0 problems).
- Partial files: 4 records carry "partial": true (Martinez 1, Nakagaki 3). Grade "abstract only" is not a valid grade for check.py (m, g, i, x only), so these are graded m or g and the abstract-only status is written in each note.
- Held: 3 Braekevelt records (photoreceptor ratio 1:2:1; single-cone oil droplet about 4.0 um; no rod oil droplet). All passed quotecheck. check.py refuses them because the source has no DOI or URL. Log them once the owner supplies a locator (for example the journal page or a PubMed record). Not written to evidence/ so the global checker stays clean.

## Issues for the owner
- Braekevelt 1990: the ratio "about 1:2:1" has no stated order. Read as rods:single:double it makes single cones twice the rods, but the paper also says single cones "appear to be as plentiful as rod photoreceptors". Ambiguous; flagged in the record note.
- Entsu 1992: converting the printed minimum angles (12 to 22 arcmin) with 1/(2 x degrees) gives 1.4 to 2.5 cycles per degree. The wanted line's review gives 2.6 to 5. The two do not agree; not resolved here.
- Chatterjee 2020: the wanted line expected the monarch (Danaus plexippus) and a Pieris/Vanessa set. The paper measured Danaus chrysippus, Papilio polytes, P. demoleus, Catopsilia pyranthe, Hasora chromus and family-level figures. Logged as measured; no monarch, Pieris rapae or Vanessa cardui values.
- Odeen 2003: no record for Corvus brachyrhynchos, Cyanocitta cristata, Falco sparverius or Buteo jamaicensis; the table does not list them. Kestrel and red-tailed hawk still need a source.
- Cervino 2021: the wanted line's focal frogs (Dryophytes cinereus, D. squirellus, Lithobates catesbeianus, Osteopilus septentrionalis) do not appear in the text read; scores are in Appendix S2, which is not in the PDF.
- Martinez 2022 (partial): abstract's diel statement is general; the chapter text was not read.
- Gaffney 2003 and Entsu 1992 are both behavioural or electrophysiological single-study values from very few animals (nine kestrels; three cattle).

## Wanted lines added (docs/views/wanted/intake-3.jsonl, 11 lines)
Reference-list papers from the two partial files, which the owner does not have: Ueda 1988, Rakoczy 1965 and 1973 (slime); Wald 1957, Kalberer and Pedler 1963, Laurens and Detwiler 1921, Fleishman et al. 1988, Whittaker et al. 1996, Dieterich and Dieterich 1978, Reger 1966 (DOI 10.1002/ar.1091550207 as printed), Derobert et al. 1999 (alligator). Emerling 2017 was already on the list. Citations are as printed in the chapter or article reference lists, not opened; volumes flagged where the print looks wrong (Kalberer and Pedler).

## Next
1. Owner supplies a locator for Braekevelt 1990, then the three held records are logged.
2. Owner can check the Kalberer and Pedler volume against the journal.
3. Monarch, Pieris rapae and Vanessa cardui flicker values still open (not in Chatterjee 2020).
