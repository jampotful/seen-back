# OA audit 1020, 18 October 2026

Scope: the 444 evidence lines that branch `oa-ctl-1018b` at `6a302bea` adds to `docs/views/evidence/oa-12.jsonl`, compared with `main` at `23da898` (the file is absent on `main`, so every line of it is new). The lines were listed in file order (`oa-12:1` to `oa-12:444`), then `random.seed(1020)` and `random.sample(lines, 40)`.

## Sample (written before any record was checked)

oa-12:58, oa-12:13, oa-12:237, oa-12:397, oa-12:208, oa-12:299, oa-12:92, oa-12:152, oa-12:400, oa-12:308, oa-12:138, oa-12:187, oa-12:213, oa-12:267, oa-12:269, oa-12:142, oa-12:158, oa-12:210, oa-12:25, oa-12:230, oa-12:66, oa-12:24, oa-12:310, oa-12:382, oa-12:254, oa-12:95, oa-12:216, oa-12:301, oa-12:336, oa-12:64, oa-12:48, oa-12:79, oa-12:200, oa-12:207, oa-12:47, oa-12:321, oa-12:249, oa-12:1, oa-12:204, oa-12:116

They come from 17 of the 38 papers behind the 444 lines.

## Method

Texts are the build machine's copies already on this machine, `/tmp/oa-shared/oa-12/oa-12-<entry>.txt`, with its `lookup.jsonl` beside them. Before use, each of the 41 texts there was hashed and compared with its entry's `text_sha256` in `lookup.jsonl`: all 41 match. Records were matched to entries by DOI; each of the 40 matched exactly one. No key was made, no `run/oa` branch was pushed, and no text is in the repository.

For each record: `python3 -I tools/views/quotecheck.py` on its text; then a stricter pass of my own that normalises whitespace and nothing else, finds each part of the quote in order, measures the gap at each "…", and prints the characters on either side of the quote, to show that it starts and ends at a sentence or row boundary; then the sentence or table row read in place, with the caption, footnotes, Methods and reference entry that define the value, its `conditions` and whether it is the paper's own.

Rules, as the launch prompt gives them. Grade: `m` for a value on the record's own taxon (a named species measured, own or cited; or the group the record names, stated as a whole); `g` for a taxon mismatch (a wider group's finding applied to a narrower record, a subset or one species standing for a group, a relative) and for a value the paper predicts or presumes (`docs/views/audit/SAMPLE.md`, "The rule decided"; BRIEF lines 62 and 170). `partial` for a cited, review or compiled value and for a value read off a figure (`oa-read.md`). A quote is verbatim, cut only with a marked "…" inside one sentence, holds the value and has at most 40 words; table rows may come from the layout text. Where the paper names the organism only by a common name, the pairing with the record's scientific name was checked. Errors are `requote`, `correct` and `retract`; metadata faults are listed and not counted (audit 31). The interval is Clopper-Pearson, as in audit 39 and OA audit 1019.

## Verdicts

| # | id (file:line) | taxon / trait | value | grade | quotecheck | verdict | reason |
|---|---|---|---|---|---|---|---|
| 1 | oa-12:58 | Plantae / sense_light_nonvisual | increased UV-B can lower photosynthesis by 3%... | m, partial | verbatim | correct | the sentence gives the 3–90% range for "different plants", the unnamed species of refs 23 and 24, and never states it for plants as a whole; a subset standing for the kingdom is `g` (grade m to g). Quote (leading cut marked, one sentence), value and `partial` stand |
| 2 | oa-12:13 | Hesperiidae / diel | crepuscular (many species) | g, partial | verbatim | confirm | Fig. 5 caption sentence whole; "many Hesperiidae" is part of the family, so `g`; diel activity was scored from published information (Methods), so `partial` |
| 3 | oa-12:237 | Cucumis sativus / sense_light_nonvisual | red light alone reduces photosynthetic capaci... | m, partial | verbatim | confirm | whole Discussion sentence; "cucumber plants" pairs with Cucumis sativus; cited Miao et al. 2019, `m` with `partial` |
| 4 | oa-12:397 | Sorghum bicolor / sense_light_nonvisual | light or temperature cycles alone drive a dai... | m | verbatim | confirm | whole abstract sentence; conditions match the text (three 12-h photoperiods at 26 °C, or three 12-h 31/22 °C thermoperiods under constant light); own data |
| 5 | oa-12:208 | Corvus brachyrhynchos / binocular_deg | 42.0 | m, partial | verbatim | confirm | Table 1 row exact; footnote 8 is Fernandez-Juricic, O'Rourke and Pitlik 2010 (J Comp Physiol A 196: 879–888), so `m` with `partial` |
| 6 | oa-12:299 | Valeriana jatamansi / sense_light_nonvisual | maximum leaf fresh weight 1.42 g, under red l... | m | verbatim | confirm | whole abstract sentence; conditions match the Methods (MS + 1 mg/L BAP, 25 ± 2 °C, 16 h light, 150 µmol m-2 s-1, red 650–670 nm, 2 months) |
| 7 | oa-12:92 | Arabidopsis thaliana / sense_light_nonvisual | ROS and nitric oxide accumulation increased i... | m, partial | verbatim | confirm | whole sentence; "Arabidopsis hypocotyls" is the genus name for the study plant; cited Iglesias et al. 2024 |
| 8 | oa-12:152 | Selasphorus rufus / binocular_deg | [35, 38] | g | verbatim | confirm | whole Results sentence; the Results pool Anna's and rufous hummingbirds ("pooling data"), so `g` (audit 39 graded the Calypte anna row of this paper the same way); stated in text, no `partial` |
| 9 | oa-12:400 | Sorghum bicolor / sense_light_nonvisual | dim, far-red-enriched light reproduced the ph... | m | verbatim | confirm | whole abstract sentence; "This treatment" is the dim, far-red-enriched light of the sentence before; conditions match the Methods (29 µmol m-2 s-1, R:FR 0.75 against 225 and 1.42) |
| 10 | oa-12:308 | Valeriana jatamansi / sense_light_nonvisual | highest root total flavonoid content 211.79 µ... | m | verbatim | confirm | whole Discussion sentence; Table 1 agrees (white, root 211.79 ± 2.46, the highest root TFC); the note flags the Results fold changes that run the other way |
| 11 | oa-12:138 | Lacerta vigilis / colour_vision | discriminates a wide range of colours across ... | m, partial | verbatim | confirm | whole sentence; named species in a cited study (Wagner 1932), `m` with `partial`; the name is as the review prints it (see faults) |
| 12 | oa-12:187 | Plantae / sense_thermal | phyB senses temperature through thermal rever... | g, partial | verbatim | confirm | whole sentence; the paragraph frames the claim with Arabidopsis, and the next sentence names three species (Arabidopsis, potato, maize) for the conserved mechanism; the passage gives no statement for plants as a whole, so `g` stands |
| 13 | oa-12:213 | Corvus moneduloides / behaviour_vision | its tool grip is determined by the visual pro... | m | verbatim | confirm | whole Results sentence ("the visual properties of a hole alone are sufficient to determine the tool grip"); NC crow is C. moneduloides in Table 1; own experiment |
| 14 | oa-12:267 | Sorghum bicolor / sense_light_nonvisual | in long days, SbCN15 (ortholog of rice Hd3a, ... | m | verbatim | confirm | one sentence, the figure references cut and marked; ~60-fold in LD; "ortholog of rice Hd3a (FT)" is the abstract's wording; conditions match the Methods (7-day entrainment, every 3 h, three biological replicates) |
| 15 | oa-12:269 | Sorghum bicolor / sense_light_nonvisual | phyB-deficient line 58 M shows shade-avoidanc... | m, partial | verbatim | confirm | whole Discussion sentence citing [7]; `m` with `partial` |
| 16 | oa-12:142 | Tarentola chazaliae / diel | nocturnal | m, partial | verbatim | confirm | whole sentence, "a nocturnal gecko, Tarentola chazaliae"; review, `partial` |
| 17 | oa-12:158 | Melospiza melodia / eye_movement | eye movement amplitude about 36° | m, partial | verbatim | confirm | one sentence, leading cut marked; "Song Sparrow, ~36°" pairs correctly with Melospiza melodia (Passerellidae); cited Moore et al. and Baumhardt et al. |
| 18 | oa-12:210 | Passeriformes / binocular_deg | [35, 51] | g, partial | verbatim | confirm | Table 1 row; seven passerines other than Corvus stand for the order, so `g`; collated from the literature (Methods), so `partial` |
| 19 | oa-12:25 | Cucumis sativus / sense_light_nonvisual | seedlings expressing the shade-avoidance resp... | m, partial | verbatim | confirm | one sentence; the first cut marks the page number "8" inside it, the second the citation tail; cited McGuire and Agrawal 2005 |
| 20 | oa-12:230 | Scutellaria baicalensis / sense_light_nonvisual | monochromatic red light (R4B0) gave the lowes... | m | verbatim | confirm | whole Results sentence; R4B0 is monochromatic red, 660 nm; conditions match the Methods (120 days, 12-h photoperiod, 22 ± 2 °C, 100 µmol m-2 s-1, UV-A at 10); stated in text, no `partial` |
| 21 | oa-12:66 | Gerygone igata / sws1_type | VS (violet-sensitive) | g, partial | verbatim | confirm | Table 1 layout row exact; caption: host rows adapted from Aidala et al. (2012), so `partial`; predicted from sequence, so `g` |
| 22 | oa-12:24 | Nicotiana longiflora / sense_light_nonvisual | reflected far-red light enhanced herbivory by... | m, partial | verbatim | confirm | whole sentence; cited Izaguirre et al. 2006 |
| 23 | oa-12:310 | Valeriana jatamansi / sense_light_nonvisual | highest root total phenolic content 126.30 µg... | m | verbatim | confirm | whole Discussion sentence; Table 1 agrees (yellow, root 126.30 ± 2.18, GAE) |
| 24 | oa-12:382 | Elymus sibiricus / sense_light_nonvisual | leaf flavonoid level significantly elevated a... | m | verbatim | confirm | whole Results sentence; leaves are the tissue sampled (Results 2.2 gives proanthocyanidins "in leaves", 2.3 "Leaf samples"); conditions match the Methods (2 months' growth, 20 °C, 12 h : 12 h, UV-C filtered, 10:30–14:30, 288 KJ/m2, 120% of plateau); SC0202-A1 is the tolerant genotype |
| 25 | oa-12:254 | Sorghum bicolor / sense_light_nonvisual | photoperiod-sensitive line 100 M (PHYB) flowe... | m | verbatim | confirm | whole sentence; LD from the sentence before; "photoperiod sensitive" and the summer greenhouse at 14 h LD are in the Results; own data |
| 26 | oa-12:95 | Lactuca sativa / sense_light_nonvisual | low R:FR decreased SOD activity and increased... | m, partial | verbatim | confirm | sentence start, citation tail cut and marked; "lettuce plants" pairs with Lactuca sativa; cited |
| 27 | oa-12:216 | Asparagus officinalis / sense_thermal | acquires freezing tolerance in fall acclimati... | m, partial | verbatim | confirm | first abstract sentence, background for the study, so `partial` |
| 28 | oa-12:301 | Valeriana jatamansi / sense_light_nonvisual | lowest leaf fresh weight 0.62 g, under blue l... | m | verbatim | confirm | whole Discussion sentence; own data |
| 29 | oa-12:336 | Anoectochilus roxburghii / sense_light_nonvisual | yellow light considerably elevated soluble su... | m, partial | verbatim | confirm | whole sentence; cited Wang et al. 2018 |
| 30 | oa-12:64 | Chrysococcyx lucidus / sws1_type | VS (violet-sensitive) | g | verbatim | confirm | Table 1 layout row exact; sequenced in this paper (HM159121); S86, S90, T93 predict VS, so `g`, no `partial` |
| 31 | oa-12:48 | Phalacrocoracidae / behaviour_vision | visual control of the beak used to turn fish ... | m, partial | verbatim | confirm | whole sentence stating it for cormorants as a group; pairing right; cited [13] |
| 32 | oa-12:79 | Zea mays / sense_light_nonvisual | height response to low R:FR varies among hybr... | m, partial | verbatim | confirm | sentence start, citation tail cut and marked; "corn" pairs with Zea mays; cited four studies |
| 33 | oa-12:200 | Corvus monedula / binocular_deg | 45.7 | m | verbatim | confirm | Table 1 row exact; one of the five non-tool-using Corvus species measured in this study |
| 34 | oa-12:207 | Corvus frugilegus / eye_movement | maximum eye-movement amplitude 29.2° | m | verbatim | confirm | Table 1 row exact, the eye-movement column; own data |
| 35 | oa-12:47 | Phoenicopteridae / behaviour_vision | adults can see their beak tips, used for fine... | m, partial | verbatim | confirm | whole sentence stating it for adult flamingos as a group; pairing right; cited [49] |
| 36 | oa-12:321 | Vaccinium ashei / sense_light_nonvisual | enhanced fresh weight 251.4-292.5 mg per expl... | m, partial | verbatim | confirm | whole sentence; cited Hung et al. 2016 |
| 37 | oa-12:249 | Ficus carica / sense_light_nonvisual | leaf FcFT1 expression rose immediately upon e... | m | verbatim | confirm | sentence start, tail cut and marked; Fig. 7 caption gives leaves and the three photoperiods; Methods: 3-year-old seedlings in an artificial weather chamber; stated in text |
| 38 | oa-12:1 | Avena sativa / sense_light_nonvisual | phototropism: bending of plants toward a ligh... | m, partial | verbatim | confirm | one sentence, the middle cut marked; oat named; Darwin's experiments cited (Darwin 1880) |
| 39 | oa-12:204 | Corvus corax / binocular_deg | 43.2 | m | verbatim | confirm | Table 1 row exact; own data |
| 40 | oa-12:116 | Ctenophorus / fovea | fovea | g, partial | verbatim | confirm | whole sentence; "these species" are the six Ctenophorus species of Nagloo et al. (2020) named in the sentences before, standing for the genus, so `g`; review, `partial` |

## Error count and rate

| | sampled | verifiable | requote | correct | retract | errors | rate | exact 95% interval |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| seed 1020 | 40 | 40 | 0 | 1 | 0 | 1 | 2.5% | 0.1% to 13.2% |

All 40 records could be checked against their texts. The one error turns on reading the grade rule: if a range "of different plants" is taken as a statement about plants as a whole, oa-12:58 confirms and the count is 0 of 40, 0.0% (0.0% to 8.8%). Under either reading the upper end of the interval is above 5%, so 40 records cannot show the pool is under 5%; with no error found, 72 records would be needed for that.

## Metadata and other faults (not counted)

| id | fault |
|---|---|
| oa-12:321, oa-12:336 | `family` and `order` absent (Vaccinium ashei: Ericaceae, Ericales; Anoectochilus roxburghii: Orchidaceae, Asparagales). A scan of the whole file finds 38 species records without either: oa-12:315 to 336 (entry 63), 363 to 375 (entry 65) and 385 to 386 (entry 72), all species named in cited studies |
| oa-12:13 | rank `family` with no `family` field (Hesperiidae); the same in oa-12:6, 7 and 9 to 12 |
| oa-12:299, 301, 308, 310, 321, 336 | `source.authors` gives the second author as "- K"; the preprint prints the single name "kanika" (Crossref stores it as family "-", given "kanika"), so the field should read "Kanika". All 41 lines from entry 63 carry it |
| `docs/views/sources/oa-12.jsonl` line 3 | title "Light signaling as a central component of crop-weed competition", taken from the URL; the paper prints "a principal component", as the evidence records have it |
| oa-12:138 | "Lacerta vigilis" is the review's name, kept with a note saying so. I cannot match it to a species in current use; Wagner (1932), Z. vergl. Physiol. 18: 378–392 (doi 10.1007/BF00340648), would settle which lizard was trained |
| oa-12:210 | the quote is the row's first printed line; the row label continues "(excluding Corvus spp.)" on the next lines. The note states the exclusion and the grade is `g`, so it is not counted |
| oa-12:116, oa-12:400 | the quote's subject is a referent ("all of these species", "This treatment") named in the sentence before; the value itself is in the quote, so neither is counted |
| oa-12:29 (outside the sample) | the taxon is "Cardamine hirsute", the review's misprint of Cardamine hirsuta (the note says "Printed as"). Seen in a scan of the notes, not audited |

## Fault patterns

1. The counted error is a grade at kingdom rank. Of the 11 kingdom-rank lines in the file, 9 are `m` and 2 `g`; the control room graded oa-12:292 ("in many species") `g` and oa-12:58 ("of different plants") `m`, two passages that both give a value for part of the plants. A pass over the 37 higher-rank `m` lines (family 12, kingdom 9, suborder 8, genus 4, order 2, class 1, superfamily 1) for passages that name only part of the group ("many", "different", "some", "tested") would find any others; the eight other kingdom `m` lines were not audited.
2. Quotes are clean. All 40 match their texts with whitespace normalised and nothing else, every cut is marked and sits inside one sentence, and each quote starts and ends at a sentence or row boundary. Across the whole file, all 444 quotes pass `quotecheck.py` as verbatim and none is over 40 words; OA audit 1019 had four typographic failures.
3. Grades otherwise hold under the rule as given. Every sampled `g` is a prediction from sequence (oa-12:64, 66), a subset standing for its group (13, 116, 210), a pooled two-species value (152) or a claim resting on one species' work with no statement for the whole group (187). Every sampled `m` on a group states the value for that group as a whole (47 flamingos, 48 cormorants), apart from 58.
4. `partial` is right on all 40: set on cited sentences, review statements, the compiled Table 1 rows and the adapted host rows; absent on the papers' own data, including values stated in text that cite a figure (230, 249, 382).
5. Common-name pairings are right: Song Sparrow (158), cucumber (237, 25), corn (79), lettuce (95), flamingos (47), cormorants (48), NC crow (213, named in Table 1), and "Arabidopsis" for A. thaliana (92). A scan of the 42 notes in the file that record a printed common name ("Printed as", "only as") found no wrong pairing.
6. Values sometimes carry words from the sentence before or from the Methods (254 "in long days", 267 "ortholog of rice Hd3a", 400 "dim, far-red-enriched light", 249 "leaf"). Each was checked against the text and is right, so none is counted.
7. Metadata: cited-study species logged without family and order (38 lines in three papers), family-rank lines without the family field (7 lines), and one mononymous author rendered "- K" (41 lines). All three are fixable by script.

## Rows written

`docs/views/recheck/recheck-oa-1020.jsonl`: one row, the `correct` of oa-12:58 (grade `m` to `g`), in the recheck-5 schema (the full corrected record with `unit`, `supersedes`, `action` and `reason`) with `field`, `old` and `new` added, as in OA audit 1019. The note gains one sentence giving the reason for `g`; quote, value, taxon and `partial` are unchanged. The row passes `tools/senses/check.py` with no problem and `quotecheck.py` as verbatim. The metadata faults above have no rows. No evidence file was edited, and no paper text or key is in the repository.
