# audit-434: desk-d322, evidence lines 9 and 10

Audited 1 November 2026 from the desk-d322 files present untracked in the worktree (docs/views/evidence/desk-d322.jsonl, 10 lines, and docs/tracks/progress/desk-d322.md; neither committed here, neither edited). This audit covers 1-based file lines 9 (Leptonetela jingde) and 10 (Mysidella hoshinoi) only; lines 1 to 8 go to another auditor. HEAD equals origin/main (0b0742023). `python3 -I tools/senses/check.py docs/views/evidence/desk-d322.jsonl`: "10 records, 0 problems". Quote lengths (`len(q.split())`): line 9 is 20 words, line 10 is 21, both within 40.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article/136555/download/xml/ (two passes), zookeys.pensoft.net/article/9924/download/xml/ (two passes), wsc.nmbe.ch/spec-data/70725, zenodo.org/records/12774316 (two passes). Crossref single-DOI lookups api.crossref.org/v1/works/ for both DOIs, each answered on the first call. WoRMS not tried (refused per rules.md). 5 WebSearches.

## Bibliographic and licence

- Line 9 (Li, Chen, Tong 2024). XML byline: Shuhui Li, Qiang Chen, Yanfeng Tong; Crossref the same order; World Spider Catalog reference "Li, S. H., Chen, Q. & Tong, Y. F. (2024)". "Li S, Chen Q, Tong Y" matches the printed given names. Title verbatim. ZooKeys 1218, no issue printed, fpage 99, lpage 119; published online 18 Nov 2024; Crossref issued 2024-11-18. DOI 10.3897/zookeys.1218.136555 confirmed. Licence: XML prints "This is an open access article distributed under the terms of the Creative Commons Attribution License (CC BY 4.0),"; Crossref CC BY 4.0, vor, delay 0; relation empty, no update-to. Accepted.
- Line 10 (Shimomura 2016). Sole author Michitaka Shimomura (XML and Crossref). Title verbatim. ZooKeys 620, no issue printed, 21-32; epub 29 September 2016; Crossref issued 2016-09-29. DOI 10.3897/zookeys.620.9924 confirmed. Licence: same CC BY 4.0 sentence in the XML; Crossref CC BY 4.0, vor, delay 0; relation empty. Accepted.

The unit did not consult Crossref; both lookups agree with the page, so nothing follows from that. Bibliographic faults 0; licence faults 0; access "open" right.

## Names and higher taxa

- Leptonetela jingde: World Spider Catalog "Leptonetela jingde Tong, 2024", "ACCEPTED", "Leptonetidae Simon, 1890". The XML taxon classification blocks list Animalia, Araneae, Leptonetidae; "Arachnida" appears nowhere in the text (tool reading). Order and family right; class blank right.
- Mysidella hoshinoi: WoRMS not reachable here. Wittmann's 2024 Mysidella treatment (Zenodo record of the European Journal of Taxonomy 940 paper) lists "M. hoshinoi Shimomura, 2016" among the "18 species acknowledged", with Order Mysida and Family Mysidae. The source XML treatment blocks list Kingdom Animalia, Order Mysida, Family Mysidae; no class rank; "Malacostraca" absent. Order and family right; class blank right.

## Repeats

`git grep -il` on origin/main (0b0742023) over the whole docs/ tree for jingde, 1218.136555, hoshinoi, 620.9924, Mysidella: no hits. Leptonetela is on main only as L. paragamiani and L. arvanitidisi (desk-d283, ZooKeys 569), other species and another paper. No repeats.

## Per line

### Line 9, Leptonetela jingde, PME 0.07 mm (male holotype)

Taxonomy, "Leptonetela jingde Tong, sp. nov.", "Male (holotype). Habitus as in Fig. 7A, B. Total length 1.25." ... "Eye sizes and interdistances: ALE 0.08, PLE 0.08, PME 0.07; ALE–PME 0.08, PLE–PLE 0.08, PLE–PME 0.03; AER 0.14, PER 0.17." **Quote MATCH**, whole sentence, one section, 20 words, contains 0.07; no cut. Unit: the quote prints bare numbers; Material and methods print "All measurements were taken using an Olympus BX51 compound microscope and are in millimeters.", and the note quotes that sentence, so mm is supported (audit 370 precedent). Abbreviations list "PME = posterior median eyes;" supports the `structure` and `eye` fields. Scope: holotype male, as `measurement` and `conditions` say. Type material: "Holotype China • ♂ (SYNU-1172)"; "Paratype: China • 4 ♂ 1 ♀ (SYNU-1173–1177), same data as holotype"; 240 m; Tu'er Mountain, Jingde County, Anhui: matches. Female line "Eye sizes and interdistances: ALE 0.08, PLE 0.07, PME 0.07; ..." supports the conditions' contrast (female PME 0.07, PLE 0.07 against male PLE 0.08). Methods "Specimens used in this study were collected by sifting forest leaf litter ..."; no cave in Methods or type material: matches. "All specimens are preserved in 75% ethanol." supports "preserved specimen". Diagnosis has no eye statement (similar to L. microdonta; chelicera teeth, palp, sclerite, chevron stripes); the key's eye couplet (3, eyes present/absent) does not single out L. jingde, and its couplet 8 uses chevron stripes and teeth: nothing contrary dropped. No Remarks section. sensory_anatomy with anatomical_measurement and units "mm" follows evidence_scope.py.

**Line 9 OK.**

### Line 10, Mysidella hoshinoi, eye developed, cornea nearly half of eye (holotype)

Heading "Description of the holotype."; after the carapace sentence: "Eye (Fig. 2A, C) developed; cornea well-pigmented, globular, wider than eyestalk, occupying nearly half of eye; eyestalk with posterodorsal finger-like papilla." Next begins "Antennula (Fig. 2A, H): ...". **Quote MATCH**, whole sentence (read in two pieces that join), 21 words, value inside it, no cut; the figure reference is kept. Holotype "adult male, 4.0 mm, KMNH IvR 500893", Akino-hama, Izu-Oshima Island, 35 m: matches. Paratypes: adult female 500894, immature female 500895, immature male 500896, adult female 500897, immature female 500898, immature male 500899, so "4 females, 2 immature males" is right. Female paratype description has no eye or cornea sentence: confirmed. "ectocommensal": Distribution and habitat "The new species live in ectocommensal association with sea anemones of the family [Haloclavidae]"; Methods collected by scooping seawater on a Haloclavidae anemone: matches. Remarks: "differs from all the congeners in having a posterodorsal finger-like papilla on the eyestalk"; comparison "occupying nearly half of eye (nearly one third)" for M. incisa; Key couplet 1 "Eye rudimentary, without cornea" (M. typhlops): the note reports all three correctly. Methods "All specimens obtained were fixed and preserved in 80% ethanol." supports "preserved holotype". anatomical_presence with sensory_anatomy and empty units passes evidence_scope.py (units are required only for anatomical_measurement); the value is a text state with no number, so no unit is owed.

**Line 10 OK.**

## Result

| Line | Record | Verdict | Errors |
|---|---|---|---|
| 9 | Leptonetela jingde, PME 0.07 mm | OK | 0 |
| 10 | Mysidella hoshinoi, eye and cornea | OK | 0 |

Errors: 0 in 2 records (0%). Error lines: none.

## Replacement

None required.

## Optional fixes (not counted)

Line 10, `note`: the subphylum rank is only an XML tag; the visible text prints Crustacea with no rank, and acceptance can be cited.
- "Class is not printed (Crustacea appears as subphylum)." -> "Class is not printed (Crustacea appears only in the title, with no rank in the text; the XML tags it as subphylum). Wittmann 2024 (European Journal of Taxonomy 940, Mysidella treatment) lists M. hoshinoi among 18 accepted species."
- "Crossref was not consulted for this DOI." -> "Crossref (audit 434): CC BY 4.0, vor, delay 0; issued 2016-09-29; relation empty."

Line 9, `note`:
- "Crossref was not consulted for this DOI." -> "Crossref (audit 434): CC BY 4.0, vor, delay 0; issued 2024-11-18; relation empty. World Spider Catalog: Leptonetela jingde Tong, 2024, ACCEPTED."
