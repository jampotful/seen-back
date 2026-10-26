# recheck-reg55: registry run 55 against the evidence and wanted logs

Registry run 55 (`ci` branch, `runs/crossref/55/crossref.jsonl.gz`) returned 317 distinct DOIs of the 321 lines in `ci/crossref/dois.txt` (the list holds 4 repeats). 288 records come from Crossref, 26 from DataCite and 3 are 404 errors. 43 of the DOIs are cited by live evidence records (3585 live records); 302 are cited by 331 wanted lines. Live means not retracted in `docs/views/audit/ALL.jsonl`; every superseded copy already appears there.

## Evidence records corrected (94 proposed; 73 merged, see the desk note at the end)

Files: `docs/views/recheck/recheck-reg55.jsonl` (94 rows, action `correct`), `docs/views/evidence/recheck-reg55-fixed.jsonl` (94 records, only `source` changed; `check.py` reports 0 problems), `docs/tracks/codex-findings/2026-10-26-audit-lines-reg55.jsonl` (94 retract lines for the superseded copies, to be appended to `ALL.jsonl` by the desk).

| DOI | Records | Field | Logged | Registry |
|---|---|---|---|---|
| 10.25365/thesis.30387 | oa-1:5735 onward (72) | authors | Abdel Keream M | Abdel KM (family Abdel, given Keream Mohamed; DataCite) |
| 10.1093/aob/mct279 | oa-9:319 to 339 (21) | year | 2014 | 2013 (no record note gives an online or print date) |
| 10.5061/dryad.n7140 | sweep-15:14 (1) | authors | Tyrrell LP, Fernandez-Juricic E | Tyrrell LP, Fernández-Juricic E (accent) |

## DOI mismatches (title similarity under 0.6)

Evidence: none. Every live evidence record that has a registry title scores 0.72 or higher against it (the lowest, 0.72, is a Dryad dataset title with a file note appended; the rest score 0.95 to 1.0). The three 404 DOIs have no registry title.

Wanted: 15 lines fall under 0.6, listed in the last section. In each the registry title names the same work as the DOI (a book chapter or dataset whose logged title carries the book name, chapter number or file description), except `canon-20:1`, whose DOI is a supplement component with no registry title. None needs a person to decide which work the DOI names.

## Registry errors (HTTP 404, nothing to compare)

| DOI | Where cited |
|---|---|
| 10.6620/zs.2022.61-18 | evidence intake-6:16, 17, 18, 19; wanted web-mammals:8 |
| 10.1007/s00122-021-03905-5 | evidence sweep-14:3 |
| 10.17660/actahort.2015.1088.51 | evidence sweep-40:13 |

## Left unchanged, with the reason

- 10.25675/3.021717 (intake-5:36 and one more record): logged author Wang H-H. The registry lists four more names (Madl J, Gionfriddo J, Byers S, Vigh J) on a master's thesis; they look like committee members and would misstate the authorship, so a person should decide.
- 10.5061/dryad.nzs7h44v8 (63 records): the registry author list is first names only (Johnson R, Rutowski R); the logged list (Johnson RA, Rutowski RL) holds middle initials the registry lacks, so no change.
- Dataset and thesis DOIs whose journal field names the paper or the degree (10.5061/dryad.1zcrjdfq7, 10.5061/dryad.n7140, 10.5061/dryad.nzs7h44v8, 10.5519/4q5uvvpa, 10.6084/m9.figshare.5126077, the thesis DOIs): the registry journal is the repository or university, so the logged string carries more than the registry and stays.
- 10.2326/osj.22.35 (2 records): the registry gives no pages; the logged pages 35-44 stay.
- 10.3389/fpls.2017.00188 (3 records): volume 8 only; the registry gives no issue or article number.
- Every other live record already matches the registry in authors, year and journal (volume, issue, pages or article number).

## Wanted lines: corrections from the registry (table only; no wanted file edited)

One row per wanted line whose authors, year or title differ from the registry. Authors are in "Family Initials" style, copied from the registry output. Registry oddities are kept as printed: Crossref prints some family names in capitals (birds-met:7) and gives "Peichlcu" for Peichl (cat-dog:13, Crossref record 10.1002/cne.903240412); a person should judge these before any wanted file is edited. For titles, the registry title is shown with HTML tags removed; annotations in the logged title (dataset file names, chapter numbers) are not part of the registry title.

| Wanted line | DOI | Authors | Year | Title |
|---|---|---|---|---|
| audit-48:1 | 10.1111/j.1447-073x.2008.00230.x | Rahman ML, Aoyama M, Sugita S |  |  |
| audit-54:1 | 10.1111/j.1399-3054.1989.tb05467.x | Martin G, Josserand SA, Bornman JF, Vogelmann TC |  |  |
| audit-54:2 | 10.1034/j.1399-3054.1994.910415.x | Myers DA, Vogelmann TC, Bornman JF |  |  |
| audit-62:1 | 10.1159/000341901 | Coimbra JP, Nolan PM, Collin SP, Hart NS |  |  |
| audit-62:2 | 10.1098/rspb.2005.3156 | Osorio D, Vorobyev M |  |  |
| audit-63:5 | 10.1098/rspb.1983.0088 | Horridge GA, Marčelja L, Jahnke R |  |  |
| audit-63:6 | 10.1016/0022-1910(64)90064-2 | Smith JC, Kimeldorf DJ |  |  |
| birds-met:5 | 10.1242/jeb.094870 | Gilman C |  |  |
| birds-met:6 | 10.1007/bf01134539 | Katzir G, Martin GR |  |  |
| birds-met:7 | 10.1111/j.1474-919x.1998.tb04554.x | KATZIR G, MARTIN GR |  |  |
| birds-met:11 | 10.1046/j.1365-2435.2002.00652.x | Guillemain M, Martin GR, Fritz H |  |  |
| birds-met:13 | 10.1002/ar.1092290214 | Inzunza O, Bravo H, Smith RL, Angel M |  |  |
| birds-met:18 | 10.1016/j.cobeha.2019.05.003 | Kelber A |  |  |
| birds-met:23 | 10.1111/ibi.12528 | Potier S, Bonadonna F, Martin GR, Isard P, Dulaurent T, Mentek M, Duriez O |  |  |
| birds-met:24 | 10.1642/auk-15-230.1 | Ochs MF, Zamani M, Gomes GMR, de Oliveira Neto RC, Kane SA | 2017 |  |
| birds-met:25 | 10.1647/2012-032 | Kuhn SE, Jones MP, Hendrix DVH, Ward DA, Baine KH |  |  |
| birds-met:26 | 10.1638/2013-0245r.1 | Kuhn SE, Hendrix DVH, Sims MH, Ward DA, Jones MP, Baine KH |  |  |
| canon-13:1 | 10.1007/s10265-016-0785-4 | Li FW, Mathews S |  |  |
| canon-19:1 | 10.1016/0022-1910(82)90145-7 | Eguchi E, Watanabe K, Hariyama T, Yamamoto K |  |  |
| canon-2:1 | 10.5061/dryad.3xsj3txq7 | Ausprey I, Ritland S |  | Eye morphology contributes to the ecology and evolution of the avian tree of life |
| canon-3:7 | 10.1007/s00359-014-0964-5 |  | 2014 |  |
| canon-4:2 | 10.5061/dryad.4b8gtht8x |  |  | Data from: Photoperiod sensitive plants have lower levels of flowering time advancement |
| canon-5:1 | 10.5061/dryad.1zcrjdfq7 |  |  | Eye size and investment in frogs and toads correlate with adult habitat, activity pattern and breeding ecology |
| canon-7:1 | 10.1093/biolinnean/blac095 | Thomas KN, Rich C, Quock RC, Streicher JW, Gower DJ, Schott RK, Fujita MK, Douglas RH, Bell RC |  | Diversity and evolution of amphibian pupil shapes |
| canon:26 | 10.1007/s00359-014-0964-5 |  | 2014 |  |
| canon:48 | 10.5061/dryad.5rs50 | Li FW, Melkonian M, Rothfels CJ, Villarreal JC, Stevenson DW, Graham SW, Wong GKS, Pryer KM, Mathews S |  |  |
| canon:49 | 10.1007/s10265-016-0785-4 | Li FW, Mathews S |  |  |
| canon:50 | 10.1038/s41586-019-1693-2 | One Thousand Plant Transcriptomes Initiative |  |  |
| canon:54 | 10.5061/dryad.3xsj3txq7 |  |  | Eye morphology contributes to the ecology and evolution of the avian tree of life |
| cat-dog:13 | 10.1002/cne.903240412 | Peichlcu L |  |  |
| cat-dog:18 | 10.1017/s095252380623342x | AHNELT PK, SCHUBERT C, KÜBBER-HEISS A, SCHIVIZ A, ANGER E |  |  |
| cat-dog:19 | 10.1093/acprof:oso/9780199581139.003.0005 | Land MF, Nilsson DE |  |  |
| cat-dog:21 | 10.1093/acprof:oso/9780199581139.003.0009 | Land MF, Nilsson DE |  |  |
| fish-shark:14 | 10.1007/978-3-319-21059-9_15 |  | 2016 |  |
| ground-invertebrates:7 | 10.1007/978-3-642-70348-5_18 |  |  | Neurobiology of a Circadian Clock in the Visual System of Scorpions |
| ground-invertebrates:8 | 10.1016/j.cub.2016.06.032 | Bok MJ, Nilsson DE |  |  |
| ground-invertebrates:9 | 10.1016/j.anbehav.2011.11.014 | Gaffin DD, Bumm LA, Taylor MS, Popokina NV, Mann S |  |  |
| ground-invertebrates:10 | 10.1016/j.anbehav.2007.12.022 | Blass GRC, Gaffin DD |  |  |
| ground-invertebrates:16 | 10.1111/j.1463-6395.2008.00341.x | Willemart RH, Farine J, Gnaspini P | 2009 |  |
| ground-invertebrates:20 | 10.1017/cbo9780511565649.007 |  |  | Sensory responses and related behaviour |
| harvest-12:2 | 10.4236/ajps.2013.43061 |  |  | &lt;i&gt;Pinus taeda&lt;/i&gt; cDNA Microarray as a Tool for Candidate Gene Identification for Local Red/Far-Red Light Adaptive Response in &lt;i&gt;Pinus sylvestris&lt;/i&gt; |
| harvest-13:1 | 10.1080/03014223.2020.1792945 | Hadden PW, Pas AE, Cassidy SB, Ober WC |  |  |
| harvest-18:1 | 10.21273/jashs.134.2.261 | Garris A, Clark L, Owens C, McKay S, Luby J, Mathiason K, Fennell A |  |  |
| harvest-20:1 | 10.2326/osj.22.35 | Nishimura H, Nakamuta N, Yamamoto Y |  |  |
| harvest-20:2 | 10.1085/jgp.21.2.223 | Crozier WJ, Wolf E, Zerrahn-Wolf G |  |  |
| harvest-20:3 | 10.1085/jgp.21.4.463 | Crozier WJ, Wolf E, Zerrahn-Wolf G |  |  |
| harvest-29:46 | 10.1093/iob/obab008 | Duncan AB, Salazar BA, Garcia SR, Brandley NC |  |  |
| harvest-30:18 | 10.17660/actahortic.2002.589.33 | Woolley DJ, Karno DJ, Nichols MA |  |  |
| harvest-30:19 | 10.17660/actahortic.1994.368.18 | Siomos AS, Sfakiotakis E, Dogras C |  |  |
| harvest-4:1 | 10.1007/s00359-009-0488-6 |  | 2009 |  |
| harvest-49:3 | 10.1159/000341901 | Coimbra JP, Nolan PM, Collin SP, Hart NS |  |  |
| harvest-49:9 | 10.1007/s10071-024-01878-2 | Berardo C, Holland R, Schaffer A, Lopez Caicoya A, Liebal K, Valsecchi P, Amici F |  |  |
| harvest-50:1 | 10.1007/s13127-015-0212-z | Martin GJ, Lord NP, Branham MA, Bybee SM |  |  |
| harvest-51:3 | 10.1007/s10682-016-9863-2 | Gaskett AC, Endler JA, Phillips RD |  |  |
| harvest-51:4 | 10.1007/s00114-009-0611-0 | Gaskett AC, Herberstein ME |  |  |
| harvest-51:12 | 10.1186/s13028-020-00551-1 | Muramoto C, Cardoso-Brito V, Raposo AC, Pires TT, Oriá AP |  |  |
| herps-met:4 | 10.1002/cne.902090402 | Kolb H, Jones J |  |  |
| herps-met:5 | 10.1016/0042-6989(85)90191-9 | Neumeyer C, Jäger J |  |  |
| herps-met:8 | 10.1016/0042-6989(68)90128-4 | Liebman PA, Entine G |  |  |
| herps-met:9 | 10.1016/0042-6989(76)90140-1 | Bowmaker JK, Loew ER |  |  |
| herps-met:18 | 10.1016/0042-6989(83)90051-2 | Nowak LM, Green DG |  |  |
| herps-met:21 | 10.1002/cne.902830412 | Wong ROL |  |  |
| herps-met:26 | 10.1007/978-3-319-53214-1_7 | Weyand B, Israelowitz M, Reuter M, Bohlmann S, Wagner R, Rizvi SWH, Gille C, Reimers K, Vogt P, von Schroeder HP |  |  |
| herps-met:27 | 10.1002/cne.901820505 | Kass L, Loop MS, Hartline PH |  |  |
| herps-met:28 | 10.1016/s0003-3472(89)80072-7 | Alberts AC |  |  |
| herps-met:29 | 10.2307/1445821 | Schaeffel F, de Queiroz A |  |  |
| herps:15 | 10.1016/j.bbr.2004.01.020 | Safer AB, Grace MS |  |  |
| herps:17 | 10.1038/nature08943 | Gracheva EO, Ingolia NT, Kelly YM, Cordero-Morales JF, Hollopeter G, Chesler AT, Sánchez EE, Perez JC, Weissman JS, Julius D |  |  |
| herps:19 | 10.1007/s00359-001-0262-x | Bartol S, Musick J, Ochs A |  |  |
| insect:6 | 10.1007/s00359-007-0223-0 | Olberg RM, Seaman RC, Coats MI, Henry AF |  |  |
| insect:16 | 10.1007/s13127-015-0212-z | Martin GJ, Lord NP, Branham MA, Bybee SM |  |  |
| insect:22 | 10.1007/s13127-012-0090-6 | Bybee SM, Johnson KK, Gering EJ, Whiting MF, Crandall KA |  |  |
| jumper:8 | 10.26021/9304 |  |  | Optical cues and vision-based discrimination mechanisms underlying predatory versatility in jumping spiders (Araneae: Salticidae). |
| jumper:13 | 10.1007/bf01342702 | Blest AD, McIntyre P, Carter M |  |  |
| jumper:19 | 10.1016/j.anbehav.2012.08.032 | Bednarski JV, Taylor P, Jakob EM |  |  |
| jumper:22 | 10.1093/acprof:oso/9780199581139.003.0009 | Land MF, Nilsson DE |  |  |
| jumper:27 | 10.1016/j.beproc.2022.104603 | Aguilar-Arguello S, Taylor AH, Nelson XJ |  |  |
| mammal-groups:9 | 10.1007/bf00612586 | Simmons JA, Kick SA, Lawrence BD, Hale C, Bard C, Escudi� B |  |  |
| mammal-groups:15 | 10.1016/j.cub.2015.11.003 | Danilovich S, Krishnan A, Lee WJ, Borrisov I, Eitan O, Kosa G, Moss CF, Yovel Y |  |  |
| mammal-groups:16 | 10.1007/s00359-026-01813-5 | Lemus K, Meyers R, Ellis S, Belova E, Nichols S, Reagan T, Hastcoat C, Webster C, Smotherman M |  |  |
| mammal-groups:17 | 10.1007/s00359-020-01436-4 | Strobel SM, Moore BA, Freeman KS, Murray MJ, Reichmuth C |  |  |
| mammals-met:4 | 10.1016/0304-3762(80)90068-1 | Hutson GD |  |  |
| mammals-met:10 | 10.1016/j.applanim.2013.04.012 | Sugnaseelan S, Prescott NB, Broom DM, Wathes CM, Phillips CJC |  |  |
| mammals-met:15 | 10.1016/0042-6989(75)90189-3 | Sivak JG, Allen DB |  |  |
| mammals-met:17 | 10.1159/000309074 | François J, Wouters L, Victoria-Troncoso V, de Rouck A, van Gerven A |  |  |
| methods:7 | 10.1242/jeb.151183 | Caves EM, Sutton TT, Johnsen S |  |  |
| methods:10 | 10.1093/acprof:oso/9780199581139.003.0007 | Land MF, Nilsson DE |  |  |
| methods:11 | 10.1093/acprof:oso/9780199581139.003.0009 | Land MF, Nilsson DE |  |  |
| methods:12 | 10.1093/acprof:oso/9780199581139.003.0008 | Land MF, Nilsson DE |  |  |
| plant-fungus-slime:2 | 10.1007/978-3-642-67648-2_50 | Eger-Hummel G |  |  |
| plant-fungus-slime:4 | 10.1007/BF00391846 | L�ning K, Dring MJ |  |  |
| sea-invertebrates:5 | 10.1007/bf00603733 | Zeil J, Nalbach G, Nalbach HO |  |  |
| sea-invertebrates:6 | 10.1073/pnas.1612239113 | Gagnon YL, Osorio DC, Wardill TJ, Marshall NJ, Chung WS, Temple SE |  |  |
| sea-invertebrates:12 | 10.1071/bi9610487 | Briggs M |  |  |
| sea-invertebrates:15 | 10.1016/j.cub.2012.02.031 | Nilsson DE, Warrant EJ, Johnsen S, Hanlon R, Shashar N |  |  |
| sea-invertebrates:16 | 10.1038/30380 | Shashar N, Hanlon RT, Petz AD |  |  |
| sea-invertebrates:18 | 10.1007/978-90-481-3299-7_15 |  | 2010 |  |
| sea-invertebrates:20 | 10.1007/s00359-002-0291-0 | Cronin T, Caldwell R, Erdmann M |  |  |
| spider:16 | 10.1007/BF00619783 | Kl�rner D, Barth FG |  |  |
| spider:24 | 10.1007/BF00394375 | Schröer WD |  | Zum mechanismus der analyse polarisierten lichtes bei Agelena gracilens C. L. Koch (Araneae, Agelenidae) |
| spider:26 | 10.1111/j.1439-0310.1975.tb01996.x |  | 2010 | Die Bedeutung der Haupt- und Nebenaugen für die photomenotaktische Orientierung der Trichterspinne Agelena labyrinthica (Cl.)1 |
| squirrel-deer-rabbit:18 | 10.1016/0006-8993(71)90219-8 | Lane R |  |  |
| sweep-1:5 | 10.1111/j.1474-919X.2008.00860.x | FERNÁNDEZ‐JURICIC E, GALL MD, DOLAN T, TISDALE V, MARTIN GR |  |  |
| sweep-10:5 | 10.3390/f9020074 | Kwak M, Je S, Cheng H, Seo S, Park J, Baek S, Khaine I, Lee T, Jang J, Li Y, Kim H, Lee J, Kim J, Woo S |  |  |
| sweep-106:1 | 10.1111/vop.12221 |  | 2014 |  |
| sweep-11:2 | 10.1660/062.123.0307 | de Queiroz AR, Maricle BR |  | Effects of Low Light on Development of Ageratina altissima and Rudbeckia laciniata (Asteraceae), Species of the Tallgrass Prairie |
| sweep-17:1 | 10.1643/0045-8511(2007)7[169:AASOTV]2.0.CO;2 |  |  | An Anatomical Study of the Visual Capabilities of the Green Turtle, Chelonia mydas |
| sweep-17:3 | 10.5061/dryad.n7140 |  |  | Data from: The hawk-eyed songbird: retinal morphology, eye shape, and visual fields of an aerial insectivore |
| sweep-18:3 | 10.2326/osj.23.45 | Nishimura H, Nakamuta N, Yamamoto Y |  |  |
| sweep-22:3 | 10.1660/062.122.0311 | de Queiroz AR, Maricle BR |  | Effects of light levels on germination of five Asteraceae species native to the tallgrass prairie |
| sweep-3:3 | 10.1016/j.phytochem.2009.09.029 | Webster B, Gezan S, Bruce T, Hardie J, Pickett J |  |  |
| sweep-3:4 | 10.1093/icb/43.3.459 | Schmitt J |  | The Adaptive Evolution of Plasticity: Phytochrome-Mediated Shade Avoidance Responses |
| sweep-32:1 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-33:5 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-34:2 | 10.1093/aob/mcx203 | Chapurlat E, Anderson J, Ågren J, Friberg M, Sletvold N |  | Diel pattern of floral scent emission matches the relative importance of diurnal and nocturnal pollinators in populations of Gymnadenia conopsea |
| sweep-36:1 | 10.1093/aob/mct279 |  | 2013 |  |
| sweep-37:2 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-37:3 | 10.1126/science.1259923 | Tanaka J, Yano K, Aya K, Hirano K, Takehara S, Koketsu E, Ordonio RL, Park SH, Nakajima M, Ueguchi-Tanaka M, Matsuoka M |  |  |
| sweep-37:4 | 10.1016/S0176-1617(11)80291-9 | Kagawa T, Michizo S |  |  |
| sweep-39:3 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-40:1 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-44:2 | 10.5519/4q5uvvpa | Thomas KN, Rich C, Quock R, Streicher J, Gower DJ, Schott RK, Fujita MK, Bell RC |  | Diversity and evolution of amphibian pupil shapes |
| sweep-46:3 | 10.1007/BF00391816 | L�ning K, Neushul M |  |  |
| sweep-47:1 | 10.1093/aob/mcn212 |  | 2008 |  |
| sweep-47:2 | 10.1674/0003-0031-169.2.259 | Lay CR, Linhart YB, Diggle PK |  | Variation among Four Populations of Erysimum Capitatum in Phenotype, Pollination and Herbivory over an Elevational Gradient |
| sweep-5:1 | 10.5061/dryad.bzkh189g3 | Caves E, Fernandez-Juricic E, Kelley LA |  | Ecological and Morphological Correlates of Acuity in Birds |
| sweep-50:2 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-53:2 | 10.1093/biolinnean/blac095 |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-54:3 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-55:3 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-55:5 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-56:1 | 10.1007/s003590000121 | Hart NS, Partridge JC, Bennett ATD, Cuthill IC |  |  |
| sweep-63:2 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-75:3 | 10.5519/4q5uvvpa |  |  | Diversity and evolution of amphibian pupil shapes |
| sweep-75:4 | 10.1016/j.cub.2020.04.061 | Simões BF, Gower DJ, Rasmussen AR, Sarker MAR, Fry GC, Casewell NR, Harrison RA, Hart NS, Partridge JC, Hunt DM, Chang BS, Pisani D, Sanders KL |  |  |
| sweep-9:9 | 10.5281/zenodo.161177 | Żuraw B, Rysiak K, Szymczak G |  |  |
| sweep-91:3 | 10.1016/j.brainresbull.2007.10.055 | Němec P, Cveková P, Benada O, Wielkopolska E, Olkowicz S, Turlejski K, Burda H, Bennett NC, Peichl L |  | The visual system in subterranean African mole-rats (Rodentia, Bathyergidae): Retina, subcortical visual nuclei and primary visual cortex |
| sweep-97:2 | 10.1016/j.envexpbot.2010.10.025 | Flores J, Jurado E, Chapa-Vargas L, Ceroni-Stuva A, Dávila-Aranda P, Galíndez G, Gurvich D, León-Lobos P, Ordóñez C, Ortega-Baes P, Ramírez-Bullón N, Sandoval A, Seal CE, Ullian T, Pritchard HW |  |  |
| web-birds:48 | 10.1007/s00359-008-0395-2 |  | 2008 |  |
| web-birds:50 | 10.1080/00071660600753870 | Barber CL, Prescott NB, Jarvis JR, Sueur CL, Perry GC, Wathes CM |  |  |
| web-insects:6 | 10.1007/s00359-002-0380-0 |  | 2002 |  |
| web-insects:23 | 10.1007/BF00340950 | H�glund G, Struwe G |  |  |
| web-mammals:1 | 10.25675/3.021717 | Wang HH, Madl J, Gionfriddo J, Byers S, Vigh J |  |  |

## Wanted lines under 0.6 title similarity

| Wanted line | DOI | Logged title | Registry title | Registry type |
|---|---|---|---|---|
| canon-20:1 | 10.1371/journal.pone.0173235.s001 | S1 Table of: Avian binocular vision: It’s not just about what birds can see, it’s also about what they can’t | (none) | component |
| canon-7:1 | 10.1093/biolinnean/blac095 | Diversity and evolution of amphibian pupil shapes (data set: Amphibian pupil data, 1293 records, CSV 366,853 bytes, with ReadMe and referenc | Diversity and evolution of amphibian pupil shapes | journal-article |
| cat-dog:19 | 10.1093/acprof:oso/9780199581139.003.0005 | Animal Eyes, 2nd edition: chapter 5, Lens eyes on land | Lens eyes on land | book-chapter |
| cat-dog:21 | 10.1093/acprof:oso/9780199581139.003.0009 | Animal Eyes, 2nd edition: chapter 9, Movements of the eyes | Movements of the eyes | book-chapter |
| ground-invertebrates:1 | 10.1093/oso/9780195084344.003.0003 | Eyes and vision (chapter in Scorpion Biology and Research) | Eyes and Vision | book-chapter |
| jumper:22 | 10.1093/acprof:oso/9780199581139.003.0009 | Movements of the eyes (chapter in Animal Eyes, second edition) | Movements of the eyes | book-chapter |
| methods:10 | 10.1093/acprof:oso/9780199581139.003.0007 | Apposition compound eyes (chapter 7 of Animal Eyes, 2nd edition) | Apposition compound eyes | book-chapter |
| methods:11 | 10.1093/acprof:oso/9780199581139.003.0009 | Movements of the eyes (chapter 9 of Animal Eyes, 2nd edition) | Movements of the eyes | book-chapter |
| methods:12 | 10.1093/acprof:oso/9780199581139.003.0008 | Superposition eyes (chapter 8 of Animal Eyes, 2nd edition) | Superposition eyes | book-chapter |
| spider:8 | 10.1007/978-3-031-96011-6 | Spider Biology, chapter 4: Neurobiology, pp. 87-136 | Spider Biology | book |
| spider:26 | 10.1111/j.1439-0310.1975.tb01996.x | [Role of the principal and accessory eyes in the photomenotactic orientation of the funnel spider Agelena labyrinthica (CL.)] | Die Bedeutung der Haupt- und Nebenaugen für die photomenotaktische Orientierung der Trichterspinne Agelena labyrinthica (Cl.)1 | journal-article |
| sweep-32:1 | 10.5519/4q5uvvpa | Diversity and evolution of amphibian pupil shapes (data set: Amphibian pupil data CSV, 1,293 species, and References for pupil data) | Diversity and evolution of amphibian pupil shapes | Dataset |
| sweep-34:2 | 10.1093/aob/mcx203 | Diel pattern of floral scent emission in populations of Gymnadenia conopsea (Annals of Botany paper behind the Botany One post of 6 June 201 | Diel pattern of floral scent emission matches the relative importance of diurnal and nocturnal pollinators in populations of Gymnadenia cono | journal-article |
| sweep-5:1 | 10.5061/dryad.bzkh189g3 | Ecological and morphological correlates of acuity in birds: data deposited with the paper (Bird_Acuity_Data.csv, 94 species from 38 families | Ecological and Morphological Correlates of Acuity in Birds | Dataset |
| sweep-53:2 | 10.1093/biolinnean/blac095 | Diversity and evolution of amphibian pupil shapes: supplementary data (images and references for each species' pupil shape), Natural History | Diversity and evolution of amphibian pupil shapes | journal-article |

Desk note (26 Oct): the 21 Annals of Botany 10.1093/aob/mct279 corrections were left out: Crossref gives the online year 2013, the records cite the issue year 2014 (113(3)), which stays.
