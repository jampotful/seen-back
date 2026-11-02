# desk-d341 progress

Angle: multi-species tables, second pass. 11 records filed (target 10), all from one paper, trait eye_diameter_mm, about 33 WebSearch/WebFetch calls. check.py: 0 problems.

## Filed (docs/views/evidence/desk-d341.jsonl)

Schweikert et al. 2022, Front. Ecol. Evol. 10: 787315, 10.3389/fevo.2022.787315, Table 1 rows (species-mean eye diameter, mm; n in units): Deosergestes corniculum 1.1 (n 18), D. henseni 1.0 (58), Allosergestes sargassi 0.7 (38), Sergestes atlanticus 0.8 (15), Parasergestes vigilax 0.6 (17), P. armatus 0.7 (30), Gardinerosergia splendens 1.2 (42), Robustosergia regalis 1.4 (38), R. robusta 1.8 (23), Challengerosergia talismani 1.1 (32), C. hansjacobi 1.2 (43). Conditions carry the column order, the fresh/paraformaldehyde/ethanol mix and the paper's preservation-effect result (as in d320, audits 431/432).

## Weak spots

- Quotes are the rows as WebFetch rendered the table, which stripped the bracketed citation numbers (d320 kept them). A second fetch asking for brackets refused. Auditor should compare with the page.
- Licence: page text returned shows no licence sentence; Crossref CC BY 4.0 vor (read this session). Accepted route per rules.
- Names: WoRMS not openable. OBIS pages (WoRMS AphiaIDs) for corniculum, henseni, sargassi, atlanticus, regalis; Vereshchaka et al. 2014 (PLoS ONE) via core.ac.uk for splendens, robusta, talismani, hansjacobi; Plazi titles only for the two Parasergestes. Status fields were usually not shown.
- R. robusta is mentioned in d320's conditions text (range of means) but has no record on main.

## Not filed

- Neosergestes edwardsii (spelling edwardsi/edwardsii differs in sources; row n 7, 0.6 mm); Table 1 other columns (depths) are literature values.
- Anuran eye-size paper fevo.2021.755818 (Chen et al.): species data only in a supplement. Ocular lens frog paper (PMC only).
- No other page-printed multi-species table was reached within budget.
