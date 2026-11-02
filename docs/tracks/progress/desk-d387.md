# desk-d387 progress

Angle: Wang L-Y / Zhang Z-S / Xu Y-Q group (Southwest University) Xizang spider papers with the printed sentence 'Eye sizes and interdistances'. 24 records from two open Pensoft papers (log docs/views/evidence/desk-d387.jsonl). check.py: 0 problems.

## Filed
- ZooKeys 1240: 239-256 (10.3897/zookeys.1240.146399; Zhang X-Y, Zhang Z-S, Wang L-Y, 2025; Lycosidae): Acantholycosa zang and Acantholycosa zhangi, male holotype and female paratype each, AME/ALE/PME/PLE, 16 records, trait sensory_anatomy (sentence prints 'Eye sizes'; Methods give no diameter definition, said in method and note).
- ZooKeys 1217: 195-213 (10.3897/zookeys.1217.127555; Thomisidae): Thomisus yarang, male holotype and female paratype, 8 records, eye_diameter_mm (Methods sentence 'Eye sizes were measured as the maximum dorsal diameter.' returned by the fetch tool).

## Weak spots
- Fetch tool cuts sentences over 125 characters; each eye sentence is joined from two consecutive pieces. Methods and neighbouring sentences are tool-returned pieces (Acantholycosa neighbours cut to 100 characters).
- Thomisus yarang female: type list prints paratype codes SWUC-T-THO-06-02 and SWUC-T-THO-06-02-03, the description heading prints SWUC-T-THO-06-03; both reported.
- Acantholycosa zang female: heading prints SWUC-T-LY-25-02, type list gives 25-02~05 as 3 males and 1 female without saying which is female; both reported.
- Acantholycosa zhangi female: heading prints no code; the single paratype in the type list is SWUC-T-LY-26-02 (by elimination, stated).
- Acantholycosa species heading text ('sp. nov.' suffix) not read verbatim; 'where' uses species names after the printed 'Taxonomy', family and genus headings. Licence sentence for ZooKeys 1240 came as a paraphrase (CC BY 4.0); ZooKeys 1217 sentence verbatim. Crossref vor not reached for either paper (UNCHECKED).
- WSC: A. zang species page 65470 and Thomisus yarang pages 70634 and 64161 opened; A. zhangi species page and family pages for Lycosidae/Thomisidae not opened (UNCHECKED; owner question: confirm validity of A. zhangi).

## Not filed and why
- Pharta xizang (ZooKeys 1217): no type material; description headings 'Male (Fig. 3C)' and 'Female (Fig. 3D)' carry no code and the material examined lists specimens from several localities, so no code can be tied to the measured specimens. The female line prints 'PLE, 0.19' with a comma.
- Zoica medogensis (ZooKeys 1249.152933): named in docs/tracks/progress/desk-d357.md and desk-d381.md; skipped as already listed.
- Sinahahnia yintiaoling: search reached only ZooKeys 1197.119935 (three other Sinahahnia species, already on main); no page for yintiaoling.
- Tricholathys xizangensis (ZooKeys 1185, 2023): search reached only Plazi/XML copies, no publisher page. Xizang Theridiidae (ZooKeys 1251.164206, single author, not this group): only an aggregator page reached. Yaginumia medog / Synagelides medog (ZooKeys 1192): PMC and aggregator pages only. Platnickina and Spartaeus skipped as instructed.
- Searches for further Korean and Chinese 2024 to 2026 spider papers returned only Plazi/Zenodo/aggregator copies or papers already on main.

## Desk disposition after audits 580-582 (2 November 2026)
All 24 lines were audited by fresh Opus agents (audits 580, 581, 582). All 24 lines carried errors in the where, conditions, note or grep-claim fields; values, quotes, bibliography and licence were confirmed. Each line was replaced with the auditor's corrected text and merged. Nothing dropped. Trait stays sensory_anatomy for Acantholycosa (no eye dimension defined in the Methods) and eye_diameter_mm for Thomisus yarang. Crossref version of record unchecked.
