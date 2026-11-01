# desk-d291: adult ant and termite eye counts and sizes in Pensoft CC BY papers, 15 records

Branch research/desk-d291 from origin/main. About 40 WebSearches (2 extended) plus fetches. `python3 -I tools/senses/check.py | grep 'd291\.'`: 15 records, 0 problems. Crossref read for all six DOIs (author order matches the pages; all CC BY 4.0 vor). Every page URL fetched was returned by a WebSearch first. Whole-docs grep on main and all research/desk-* and audit-* evidence, audit and progress files, by genus and DOI: no repeats for the filed species. New traits ommatidia_count (used by d271) and eye_diameter_mm are marked "new trait" in the notes.

Filed (docs/views/evidence/desk-d291.jsonl):
1-2. Carebara colobopsis, major worker 5-6 ommatidia; minor worker 1 ommatidium (JHR 91). Types are one holotype and two paratype majors, four paratype minors.
3-6. Carebara eguchii (major 2-3, minor 2) and C. bifida (major "ten ommatidia visible", minor 1), Deutsche Entomologische Zeitschrift 72(2). Full title includes the family parenthesis.
7-8. Platythyrea homasawini (7 or 8) and P. janyai (11): ommatidia along the longest axis of the eye (a linear count; units say so), ZooKeys 1115. P. janyai was described earlier; this paper gives its worker description.
9-12. Brachyponera myops (5 ommatidia across maximum diameter, ED 0.07 mm) and B. candida (11, ED 0.17 mm), ZooKeys 1230. ED in parentheses is the holotype value; paratype ranges 0.06-0.07 and 0.15-0.17 are in conditions. One ommatidia_count and one eye_diameter_mm line per species, same sentence.
13. Ooceraea joshii, two ommatidia, ZooKeys 1010.
14. Ooceraea decamera, "Eyes absent.", single holotype worker, eye_type none (sentence names no species; `where` gives the treatment).
15. Rugitermes tinto, imago eye diameter 0.32 mm, one damaged female imago, ZooKeys 963. The sentence reached the tool in two pieces within one fetch (128 characters); stitched, flagged in the note. Order printed Isoptera.

Dropped:
- On main already (d270, d274 and others): Arge similis (Insects 13(2)), Ceratosolen gravelyi (Insects 16(7)), Tomicus yunnanensis (Biology 14(8)).
- Meranoplus siamensis and M. tanomtongi (ZooKeys 1210): eye sentences only reachable as two quoted halves split mid-sentence; dropped.
- Cryptotermes pugnus (ZooKeys, imago eye maximum diameter 0.23): the measurements sentence is 39 words and only a fragment was returned.
- Apharinodes baixiensis (BDJ 12): "about 20 facets" sits in a long head sentence the tool would not return whole.
- Nocticola (ZooKeys 1232, Subterranean Biology 19): eyes "reduced to a few ommatidia" without a number; N. gonzalezi "3-4 facets" is for nymphs. Brachyponera/Carebara laeviceps (ZooKeys 1190): "Eyes minute", no count. Leptanillinae monograph (ZooKeys 1189): ommatidia statements are clauses; L. acherontia no eye sentence. Earwigs from Brazilian caves (ZooKeys 790): eye statements are Introduction review claims. Hospitalitermes, Acangaobitermes, Tauritermes: no number. Lymantria xylina (Insects 16(11)): male count only inside a comparison sentence. Crematogaster with one ommatidium (Acta Entomol. Mus. Nat. Pragae): no licence sentence on the page. Oxyepoecus myops and similar: Zootaxa.
- Bee, wasp (parasitoid), fly, bug, cricket and beetle searches: no short readable eye-number sentence in an open journal; Plazi, Zenodo and repository copies not used.

Names: no checklist opened; Platythyrea janyai and Carebara oni group names rest on the cited papers.
