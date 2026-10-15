# sweep-92 progress (Round 3 genus sweep, batch sweep-1, 40 genera)

Done 15 October 2026. All 40 genera had two searches each (scientific name plus trait words; common name or family plus trait words) and a search record in `docs/views/searched/sweep-92.jsonl` (41 lines, Mesocricetus has two because its cff_hz cell differs from its field cells).

Logged measurements (`docs/views/evidence/sweep-92.jsonl`, 4 records, all abstract-only so `partial: true`): Mesocricetus auratus has one cone class (about 506 nm; Calderone and Jacobs 1999), with S opsin coexpressed in the same cone (Glosmann and Ahnelt 2002) and no blue or UV opsin found (von Schantz et al. 1997). This closes receptor_classes for Mesocricetus; its binocular_deg, cff_hz and fov_h_deg stay open.

Everything else found no measurement for the genus or a congener. No wanted lines were added, because no unopened paper with a confirmed author, year and DOI bore on an open cell.

Limits on this machine: curl is refused for every host, and PMC, PubMed, Springer, doi.org and ScienceDirect returned a bot check, a 429 or a robots block. Pages not read: Odeen and Hastad 2013 (10.1186/1471-2148-13-36, the SWS1 survey that may list Columbiformes, Megapodiidae and Rallidae), Healy et al. 2013 (10.1016/j.anbehav.2013.06.018, closest record for Mesocricetus cff_hz, so that search record's `chased` says "unchecked"), and Potier et al. 2017 (10.1159/000479783, abstract only, names no species).

Next if resumed: open Odeen and Hastad 2013 and Healy et al. 2013 from a machine that can reach them, then redo the bird genera (Henicophaps, Cryptophaps, Eulipoa, Aepypodius, Mustelirallus) and Mesocricetus cff_hz.
