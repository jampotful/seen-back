# desk-d371 progress

Angle: non-spider taxa. 8 records from 4 papers, about 44 search/fetch calls. check.py passes on desk-d371.jsonl.

## Filed (docs/views/evidence/desk-d371.jsonl)
- ZooKeys 1282: 17-35 (10.3897/zookeys.1282.194867; CC BY 4.0 vor): Entomobrya cezarae (eyes_count 8, printed "eight eyes"), E. antoniae and Willowsia solanella (eyes_count "8 + 8"), Entomobryidae, holotype females.
- ZooKeys 1284: 357-373 (10.3897/zookeys.1284.199197): Cyta edafosa (Bdellidae), median, anterior lateral and posterior lateral eye diameters, printed in micrometres and converted to mm; quote cut before the interocular distance.
- Zoosystematics and Evolution 101(3): 969-981 (10.3897/zse.101.146451): Brachistosternus pehuenche, 3 lateral ocelli per side; quote cut before the last spacing clause.
- Biodiversity Data Journal 14: e194005 (10.3897/bdj.14.e194005): Lithobius (Ezembius) zebrinus, ocelli 7-9.

## Weak spots
- All text came through fetch-tool summaries, in pieces. The Cyta sentence punctuation (semicolons, comma after 48-52) was confirmed by a direct punctuation question; the XML copy returned a shortened form.
- E. cezarae prints "eight eyes" without "+" notation; per-side status unknown (stated in the note).
- B. pehuenche: the printed licence sentence was not read on the XML copy (Crossref vor CC BY 4.0 used); the preview URL for that id returned a different article.
- No taxon registry page opened for any of the names (stated as unchecked in each note).
- Cyta: the sentence does not say whether 16/18/19 are means or holotype values.

## Not filed
- Triplophysa ZooKeys 1281.186268 (already on main), Gyrinomimus ZooKeys 1279 (already filed), Californiphilus BDJ e199879 (no eye text), Cunaxa BDJ e174602 (no eye text), Rhysida/Alluropus ZSE 101.156915 (text lacks eye sentences), Amolops daorum ZooKeys 1262.172081 (ED per sex in a sentence over 80 words; not new species).
- Not opened: Otostigmus (Subterranean Biology 58.198345), Balitora tiandengensis (ZooKeys 1267.166354), Claea dafangensis (ZSE 102.172325), Trimma (ZooKeys 1255.159341).

## Desk disposition after audit 499 (2 November 2026)
All 8 records merged with the auditor's replacement lines. 3 of 8 were in error (37.5%, 6 faults), all in note and conditions text of the three Collembola lines: "all type material female" was wrong because the ethanol paratypes are unsexed, and the note cited a key, diagnosis and discussion the paper lacks. The Cyta micrometre-to-millimetre conversion was right, and the Brachistosternus pehuenche licence sentence was read on the XML copy and accepted. Owner question: the four new names other than B. pehuenche (Entomobrya cezarae, E. antoniae, Willowsia solanella, Cyta edafosa) are unchecked on registries.
