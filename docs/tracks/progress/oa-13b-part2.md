# oa-13b, part 2: whole-unit recheck of oa-13 lines 854 to 1095 (26 October 2026)

Scope: every record in lines 854 to 1095 of `docs/views/evidence/oa-13.jsonl` on `origin/research/oa-13-read` at 80e4a889 (242 records from 60 papers, entries 97 to 294). The sample audit (`docs/tracks/progress/audit-oa-13.md`) found 4 errors in 55 non-table records (7.3%), so the unit is rechecked whole. Rules: `docs/tracks/prompts/oa-audit.md`, `oa-read.md` (quote and grade rules), audits 31 and 39, BRIEF, and desk-screen points 9 and 10 (owner's readings of 25 October). No new key, no run branch and no fetch: the decrypted run 25 texts on the build machine (`/tmp/oar13key/txt/oa-13-<entry>.txt`) were read in place, entries matched through `/tmp/oar13-lookup.jsonl` by DOI (by title for the two theses, entries 113 and 154). No paper text, key or PDF enters this branch, and no DOI, author or year was typed from memory. The branch's own evidence file is untouched.

Method: each record's quote was run through `python3 -I tools/views/quotecheck.py` against its text, the sentence or table row around it was read, and value, taxon, grade, partial flag and trait were compared with it. Table units were checked by script as well as by eye: the 20 pan-trap rows of entry 147 (each row's cells regrouped into the logged value and summed against the row's totals and the record's stated count, 20 of 20 equal), the Table 1 rows of entry 112 and the Table 4-1 rows of entry 113 (common names checked against the thesis's own species list).

## Output

`docs/views/evidence/oa-13b-part2.jsonl`: 241 records (every record except the one retracted), `"unit": "oa-13b-part2"`, all other fields as in the original and the `source` object untouched, with the fixes below applied. `python3 -I tools/senses/check.py` reports 0 problems; all 241 quotes pass `quotecheck.py` (240 verbatim, 1 table row: line 990, the Polyommatus icarus row of entry 147, which the text holds only in its layout part).

## Counts

| verdict | records |
|---|---|
| confirm | 209 |
| requote | 29 |
| correct | 3 |
| retract | 1 |
| **all** | **242** |

Errors (requote, correct, retract): 33 of 242, 13.6%. Wrong value, taxon, grade, partial or trait (correct and retract only): 4 of 242, 1.7%. The rate is higher than the sample's 7.3% because every value was read against its quote word by word: 23 of the 29 requotes are values that carry a word or two from a neighbouring sentence, the fault the sample audit named as pattern 1.

## Verdicts other than confirm

Line numbers are those of `oa-13.jsonl` at 80e4a889.

| line | entry | taxon / trait | verdict | reason and fix |
|---|---|---|---|---|
| 864 | 101 | Aedes aegypti / behaviour_vision | requote | value said 'vertical bar'; the quote says 'the feature' |
| 865 | 101 | Aedes aegypti / behaviour_vision | requote | value said 'vertical bar'; the quote says 'the feature' |
| 868 | 103 | Orgyia antiqua / filter_pigments | requote | value added '(screening-pigment and clear-zone changes)', which the quote lacks |
| 873 | 106 | Locusta migratoria / interommatidial_deg | requote | quote opened with a cut ('… our values …'), mid-sentence |
| 874 | 106 | Locusta migratoria / interommatidial_deg | requote | quote opened with a cut ('… our values …'), mid-sentence (sample audit's fault) |
| 875 | 106 | Dissosteira carolina / interommatidial_deg | requote | quote opened with a cut ('… while males'), mid-sentence |
| 876 | 106 | Spharagemon equale / interommatidial_deg | requote | quote opened with a cut ('… while males'), mid-sentence |
| 890 | 109 | Sirex noctilio / receptor_classes | requote | value added '(UV and green receptors only)' from the next sentence, which the quote lacks |
| 941 | 127 | Oecophylla smaragdina / diel | requote | value said 'diurnal forager', a word from the next numbered finding; the quote says only that it forages in full light |
| 960 | 139 | Polyspilota / depth_cue | requote | value named peering, side-to-side movement and motion parallax; the quote gave only amplitude and velocity. Quote now carries the peering sentence; 'side-to-side' and 'motion parallax' dropped |
| 961 | 139 | Mantis religiosa / depth_cue | requote | as 960 |
| 1022 | 157 | Calonectris borealis / behaviour_vision | requote | value said 'over white light' and 'over blue light', pairings the quote does not state |
| 1023 | 157 | Calonectris borealis / behaviour_vision | requote | as 1022 |
| 1036 | 208 | Epilobium / sense_light_nonvisual | requote | value added 'longer intervals reduce the effect' from the next sentence, past the quote's closing cut |
| 1037 | 208 | Boenninghausenia / sense_light_nonvisual | requote | as 1036 |
| 1046 | 211 | Hypericum perforatum / sense_light_nonvisual | requote | value added '(a systemic response)' from the next sentence |
| 1049 | 223 | Primula forbesii / sense_chemical | retract | the ethylene treatment was applied to flowers sampled from the plant and incubated in a closed container (Methods), a chemical treatment of cut flowers, which point 10a excludes from plant sense_chemical |
| 1053 | 229 | Rumex confertus / sense_chemical | requote | value listed the blend (green leaf volatiles, esters, terpenes) and the small emission of uninjured plants, both from later sentences |
| 1054 | 229 | Apion miniatum / sense_chemical | requote | value added 'males not attracted' from the next sentence |
| 1056 | 230 | Rumex confertus / sense_chemical | requote | value named the six as three green leaf volatiles and three terpenes, from the previous sentence |
| 1067 | 236 | Lerista / receptor_classes | requote | quote stopped with a cut before the gene list, which the value named; quote now carries RH1 and the four cone opsins (sample audit's fault on 1068) |
| 1068 | 236 | Ctenotus / receptor_classes | requote | as 1067 (the sample audit's requote) |
| 1069 | 243 | Bicyclus anynana / tapetum | requote | the quote only listed the species studied; the value's tapetal mirror below the rhabdom and in-vivo observation were not in it. Quote now adds the tapetal-mirror sentence; 'below the rhabdom' and 'in vivo' dropped |
| 1070 | 243 | Heliconius melpomene / tapetum | requote | the quote only listed the species studied; the value's tapetal mirror below the rhabdom and in-vivo observation were not in it. Quote now adds the tapetal-mirror sentence; 'below the rhabdom' and 'in vivo' dropped |
| 1071 | 243 | Pieris rapae / tapetum | requote | the quote only listed the species studied; the value's tapetal mirror below the rhabdom and in-vivo observation were not in it. Quote now adds the tapetal-mirror sentence; 'below the rhabdom' and 'in vivo' dropped |
| 1072 | 243 | Lycaena phlaeas / tapetum | requote | the quote only listed the species studied; the value's tapetal mirror below the rhabdom and in-vivo observation were not in it. Quote now adds the tapetal-mirror sentence; 'below the rhabdom' and 'in vivo' dropped |
| 1075 | 248 | Testudines / sense_hearing | correct | the sentence is about land tortoises ('tortues terrestres', named in the preceding sentence), logged as Testudines for all turtles; quote extended to name the subject |
| 1076 | 253 | Milvus migrans / fovea | requote | value said depth 'increases' with eye size and named the central fovea; the quote says only that depth was related to eye size |
| 1079 | 257 | Buteo lagopus / behaviour_vision | requote | the quote said only 'the same ability'; the UV vole marks were in an earlier sentence. Quote now carries it |
| 1080 | 257 | Anas platyrhynchos domesticus / spectral_range_nm | correct | a peak of spectral sensitivity was logged under spectral_range_nm, which records the range seen; moved to behaviour_vision, and the quote now names ducks and turkeys |
| 1081 | 257 | Meleagris gallopavo gallopavo / spectral_range_nm | correct | a peak of spectral sensitivity was logged under spectral_range_nm, which records the range seen; moved to behaviour_vision, and the quote now names ducks and turkeys |
| 1084 | 266 | Rumex trisetifer / sense_light_nonvisual | requote | value named 'the five Polygonaceae', which the quote does not |
| 1085 | 266 | Rumex obtusifolius / sense_light_nonvisual | requote | as 1084 |

## Entries the sample flagged

- Entry 106 (lines 869 to 876): the four Oedipodinae records and their values hold against the Results and Discussion (98 individuals, 1.09° and 2.17°, female species means 0.94°–1.00° and 2.09°–2.21°, the flattest region of the eye). Lines 873 to 876 opened mid-sentence and are requoted to start where their sentences start, within 40 words.
- Entry 236 (lines 1067 and 1068): the value (all five opsin genes present and intact) holds; the quote now carries RH1 and the four cone opsins, and the value drops "named in the abstract". Grade `g` (gene presence predicts pigments) stands.

## Fault patterns

1. **Value outruns the quote** (23 records: 864, 865, 868, 890, 941, 960, 961, 1022, 1023, 1036, 1037, 1046, 1053, 1054, 1056, 1069 to 1072, 1076, 1079, 1084, 1085). A neighbouring sentence lends the value a word the quote lacks: a composition ("three green leaf volatiles and three terpenes"), a sequel ("males not attracted"), a comparison ("over white light"), or a gloss ("a systemic response", "diurnal"). The values are true in each paper; the quotes do not show them. Most fixes trim the value; seven (960, 961, 1069 to 1072, 1079) carry the missing sentence into the quote with a marked cut.
2. **Leading cut** (873 to 876): a quote opening "… our values" or "… while males", as in the sample's line 874. `quotecheck.py` cannot catch it; a lint for quotes starting with "…" would.
3. **Closing cut that drops what the value names** (1067, 1068), as in the sample.
4. **Taxon taken from the paragraph instead of the sentence** (1075): a French review's "Leur acuité auditive" refers to "les tortues terrestres" (land tortoises), logged as Testudines.
5. **Trait key** (1080, 1081): a peak of spectral sensitivity under `spectral_range_nm`, moved to `behaviour_vision`. Looser keys of the kind the sample audit listed without counting (plant germination under `sense_thermal`, a starch rhythm under `diel` at line 1091, an all-opsin count under `receptor_classes` at line 949) are confirmed here, as in the sample.
6. **Owner's reading 10a** (1049): ethylene given to flowers sampled from the plant counts as a treatment of cut flowers.

Not counted: entry 1's lamp table is outside this part; the light-trap and pan-trap comparisons here (939, 940, 945, 946, 982 to 1003) are pooled or colour-choice records under `behaviour_vision`, which point 10c allows.
