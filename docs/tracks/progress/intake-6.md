# Intake 6 progress note (round 2 Drive intake)

Branch: research/intake-6, cut from main. Launch prompt: docs/tracks/prompts/round2-intake.md; brief: docs/views/research/BRIEF.md.
Status: in progress. Ten files downloaded and extracted to text (scratch only, nothing from Drive committed). Records not yet logged.

## Files (ten named in the launch prompt, keyed by sha1 of the Drive id)
| sha1 key | file | DOI | wanted unit (matched line) | status |
|---|---|---|---|---|
| fa9f9ad5a54c | Mitchell 2013 giraffe orbit orientation (no DOI) | none | web-mammals (giraffe, Giraffa camelopardalis) | text extracted, 7 pp |
| f19f1ae82bf4 | Schusterman 1971 sea lion acuity (PARTIAL) | 10.1111/j.1749-6632.1971.tb13088.x | mammal-groups (seal) | text extracted, 8 pp, abstract and refs only |
| f10b5d8101d3 | Miyazaki 2022 nutria eye | 10.6620/ZS.2022.61-18 | web-mammals (Myocastor coypus) | text extracted, 14 pp |
| 54a86759cc3c | Odeen 2013 UV sensitivity in birds | 10.1186/1471-2148-13-36 | birds-met (Aves); also canon | text extracted, 10 pp |
| d70be66c7a6e | Mueller 2003 Scutigera compound eye | 10.1007/s00435-003-0085-0 | ground-invertebrates (centipede) | text extracted, 19 pp |
| 2d0990d5553e | Duelli 1978 jumping spider posterolateral eyes | 10.1007/bf00656387 | jumper | text extracted, 12 pp |
| 3 f9ab27dd8023 | Inger 2014 flickering artificial light | 10.1371/journal.pone.0098631 | methods (also canon) | text extracted, 11 pp |
| f226c7a88a64 | Roell 2001 gecko retina and foveae | 10.1016/s0042-6989(01)00093-1 | herps (gecko) | text extracted, 14 pp |
| 14183a19367b | Wallace 2013 rat overhead binocular field | 10.1038/nature12153 | squirrel-deer-rabbit (mouse line) | text extracted, 5 pp |
| b06043ac29f9 | Warrant 1999 seeing better at night | 10.1016/s0042-6989(98)00262-4 | methods | text extracted, 20 pp |

Each file is well under 10 MB (largest 5.2 MB, Miyazaki).
Download note: the Drive tool saves each result to a JSON file on disk, which decode.py turns into a PDF in the scratchpad.

## Next
1. Read around the matches and log records (evidence/intake-6.jsonl), run quotecheck and check.py.
2. Failures to evidence/intake-6-failed.jsonl.
3. drive.jsonl lines for the ten files (none existed before).
4. Wanted lines for reference-list papers (only Schusterman is partial).
