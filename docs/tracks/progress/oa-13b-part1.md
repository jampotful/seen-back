# oa-13b part 1: full recheck of oa-13 lines 610 to 853 (26 October 2026)

Scope: every record on lines 610 to 853 of `docs/views/evidence/oa-13.jsonl` on `origin/research/oa-13-read` (244 records from 31 papers, lookup entries 4 to 96). Each record was mapped to its text by DOI or title through `/tmp/oar13-lookup.jsonl`, run through `python3 -I tools/views/quotecheck.py` against `/tmp/oar13key/txt/oa-13-<entry>.txt` (244 of 244 passed before any fix), and then read against the sentence or table row around its quote. The texts were read in place on the build machine; no key was made, no build job ran, and no paper text, PDF or key enters this branch. Rules: `oa-audit.md`, `oa-read.md`, audits 31 and 39, `audit-oa-13.md`, desk-screen points 9 and 10, and BRIEF.

Output: `docs/views/evidence/oa-13b-part1.jsonl` holds the 240 confirmed or fixed records with `"unit": "oa-13b-part1"`, the `source` object untouched. `check.py` reports 0 problems on it, every quote passes `quotecheck.py` verbatim, and no quote opens with a cut.

## Counts

| verdict | records |
|---|---|
| confirm | 217 |
| requote | 22 |
| correct | 1 |
| retract | 4 |
| total | 244 |

Errors (requote, correct and retract): 27 of 244, 11.1%. Wrong value, taxon, grade or partial (correct and retract): 5 of 244, 2.0%. Under the task's definition, a requote is a record whose value says more than its quote; in 19 of the 22 the fix trims the value to the quote's words and leaves the quote as it was, and in 3 (662, 684, 689) the quote is rebuilt from the paper's own sentence so that it carries the value.

The entries the sample audit faulted that fall in this range were read line by line: entry 30 (692 to 697) gives 2 confirms and 4 requotes, and entry 41 (699 to 704) gives 4 confirms, 1 requote and 1 correction. Entry 106 (lines 869 to 876) lies outside this part.

## Records with a verdict other than confirm

| line | entry | taxon / trait | verdict | reason |
|---|---|---|---|---|
| 640 | 13 | Coleoptera / receptor_classes | requote | value glossed SW as "(blue-sensitive)", which the quote does not say; value trimmed |
| 641 | 13 | Blattodea / receptor_classes | requote | value glossed SW as "(blue-sensitive)", which the quote does not say; value trimmed |
| 642 | 13 | Phasmatodea / receptor_classes | requote | value glossed SW as "(blue-sensitive)", which the quote does not say; value trimmed |
| 643 | 13 | Neuroptera / receptor_classes | requote | value glossed SW as "(blue-sensitive)", which the quote does not say; value trimmed |
| 651 | 17 | Trifolium repens / diel | requote | value adds "for a time", which the quote lacks; value trimmed |
| 652 | 17 | Pueraria lobata / diel | requote | value adds "for a time", which the quote lacks; value trimmed |
| 653 | 17 | Lobinia pseudo-acacia / diel | requote | value adds "for a time", which the quote lacks; value trimmed |
| 654 | 17 | Oxalis corniculata / diel | requote | value adds "for a time", which the quote lacks; value trimmed |
| 661 | 19 | Carnivora / tapetum | requote | "holding ordered rodlets" is in the next caption sentence, outside the quote; value trimmed |
| 662 | 19 | Ungulata / tapetum | requote | "extracellular protein fibres" sat in the next caption sentence; quote extended to it, "choroidal" dropped from the value |
| 667 | 19 | Aves / tapetum | requote | value asserted a retinal tapetum for the whole class; the quote says only that needles are the prevalent reflective elements in the RPE; value trimmed |
| 668 | 19 | Reptilia / tapetum | requote | value asserted a retinal tapetum for the whole class; the quote says only that needles are the prevalent reflective elements in the RPE; value trimmed |
| 669 | 19 | Amphibia / tapetum | requote | value asserted a retinal tapetum for the whole class; the quote says only that needles are the prevalent reflective elements in the RPE; value trimmed |
| 683 | 37 | Vaccinium myrtillus / sense_light_nonvisual | requote | the colours (blue, red, far-red) come from the previous abstract sentence, outside the quote; value trimmed to the quote's words (the colours stay in method) |
| 684 | 32 | Dipsacus fullonum / sense_light_nonvisual | requote | the cut removed the words that carry the two behaviours, so the value outran the quote; quote now holds them, value trimmed to them |
| 689 | 32 | Dipsacus fullonum / sense_thermal | requote | the trailing cut dropped the neutral accessions (ETN>LAP>PIE) that the value states; quote extended |
| 693 | 30 | Chenopodium album / sense_light_nonvisual | requote | sample-audit fault: the far-red inhibition is in the next abstract sentence, which does not name C. album; value trimmed to what the quote says |
| 694 | 30 | Amaranthus caudatus / sense_light_nonvisual | requote | "germination inhibited by light" comes from the earlier "light-inhibited" sentence, outside the quote; value trimmed to the quote |
| 696 | 30 | Urtica urens / sense_light_nonvisual | requote | value added "continuous", which the quoted clause does not say; value trimmed |
| 697 | 30 | Amaranthus caudatus / sense_light_nonvisual | requote | value added "continuous", which the quoted clause does not say; value trimmed |
| 699 | 41 | Schistocerca gregaria / polarization | requote | "main-eye PS <4" is in the next sentence, outside the quote, and the value turned "seem to contribute" into "contributing"; value trimmed to the quote |
| 701 | 41 | Schistocerca gregaria / receptor_classes | correct | sample-audit fault: five receptor types include the dorsal-rim blue receptor, which repeats the main eye's blue class; spectral classes are UV, blue, green and blue/green broadband, so 4 |
| 747 | 79 | Valeriana officinalis / sense_light_nonvisual | requote | value said callus "formed fastest" from "leaf explants"; the quote says healing time was shortest and callus quality best at 0 h/d; value trimmed to the quote |
| 755 | 83 | Calliphora vicina / f_number | retract | F = 2 is the authors' model default: the text says that where focal distance is not reported they calculate it with F = 2, and this row's f is exactly 2 × D and f' exactly 1.34 × f, so the F-number is assumed and measures nothing |
| 758 | 83 | Calliphora vicina / f_number | retract | F = 2 is the authors' model default: the text says that where focal distance is not reported they calculate it with F = 2, and this row's f is exactly 2 × D and f' exactly 1.34 × f, so the F-number is assumed and measures nothing |
| 761 | 83 | Musca domestica / f_number | retract | F = 2 is the authors' model default: the text says that where focal distance is not reported they calculate it with F = 2, and this row's f is exactly 2 × D and f' exactly 1.34 × f, so the F-number is assumed and measures nothing |
| 764 | 83 | Musca domestica / f_number | retract | F = 2 is the authors' model default: the text says that where focal distance is not reported they calculate it with F = 2, and this row's f is exactly 2 × D and f' exactly 1.34 × f, so the F-number is assumed and measures nothing |

## Fault patterns

1. **The value glosses or extends the quote (19 records).** The commonest fault is a value that adds a word or clause the quote lacks, usually true elsewhere in the paper: a gloss on a technical term ("SW" as blue-sensitive, 640 to 643), a qualifier ("for a time", 651 to 654; "continuous", 696 and 697), or a clause from the adjacent sentence (661, 683, 693, 694, 699, 747). For the tapetum records 667 to 669 the extension changed the claim: the value said the whole class has a retinal tapetum, where the review says only which reflective elements prevail in the tapeta it describes.
2. **A cut removes the words that carry the value (684, 689).** The internal or trailing ellipsis passes `quotecheck.py`, because each remaining part is present, while the dropped words are the ones the value states. A lint that compares the value's numbers and taxon codes with the quote would catch this.
3. **An author's model default logged as a measurement (755, 758, 761, 764).** In entry 83, Table 2 prints F = 2 for four fly eye regions; the text says that where focal distance is not reported the authors calculate it with F = 2, and in exactly those rows f equals 2 × D and f' equals 1.34 × f. A compiled table can mix reported and assumed columns, and a reader has to check the paper's method sentence before logging each column. The other F values in Tables 2 and 3 follow from the reported f and D (f / D) or come from the cited source, and they stay.
4. **Receptor types counted as spectral classes (701).** The sample audit's correction holds: four spectral classes.

Not counted, as in audit 31: trait keys used loosely (plant germination under `sense_thermal`, melatonin rhythms under `diel`, a colour class with no wavelength under `lambda_max_nm` at 702, string values under `receptor_classes` at 640 to 644), and the review notes at 847 to 853, which name the cited studies by reference number where `oa-read.md` asks for authors and year. In entry 83 the Tenodora fovea row prints F = 8 beside D = 47.5 and f = 205 (f / D would give 4.3); record 791 logs the table's 8 as printed, and the inconsistency belongs to the table.
