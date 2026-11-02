# desk-d379 progress

Angle: multi-species spider papers with per-species eye sentences. 43 records from four papers, about 45 search/fetch calls. Every value was re-read against its quote by script (regex on the eye's own label, interdistance labels excluded); quote word counts are all under 40. All text came through fetch-tool summaries returned in segments and rejoined; notes say so.

## Filed (docs/views/evidence/desk-d379.jsonl), all eye_diameter_mm (each paper's Methods: "Eye sizes were measured as the maximum dorsal diameter.")
- ZooKeys 1200: 183-198 (10.3897/zookeys.1200.120528; licence sentence read whole): Asceua chayu (female holotype, 4), Cydrela linzhiensis (female and male, non-type specimens, 8). Zodariidae. Cydrela WSC species/43365 opened (accepted). Asceua chayu WSC page NOT opened (spec-data/69615 refused): name unchecked, owner question in each note.
- ZooKeys 1254: 217-224 (10.3897/zookeys.1254.154722; CC BY 4.0 tag read, rest of licence sentence paraphrased by the tool): Hahnia dabashan (male holotype; AME, ALE, PME only, 3) and Sinahahnia chengkou (male holotype 4, female paratype 4). Hahniidae. WSC spec-data 72772, 72773 opened.
- BDJ 13: e155306 (10.3897/BDJ.13.e155306; CC BY 4.0 tag read, rest paraphrased): Neoantistea yintiaoling (male holotype, 4). WSC spec-data/71833 opened.
- ZooKeys 1197: 249-259 (10.3897/zookeys.1197.119935; licence sentence read whole): Sinahahnia eyu and S. fanjingshan (male holotype and female paratype each, 16). WSC spec-data 69578, 69579 opened.

## Weak spots
- Hahnia dabashan PLE is printed "0.0.05" (confirmed on preview and XML); no PLE record filed.
- Sinahahnia chengkou female: the Description names paratype SWUC-T-HA-09-02, which is not in the printed paratype list (HA-17-02 to -18); followed as printed, flagged in conditions.
- Cydrela linzhiensis: the Description does not say which specimen (SWUC-ZCL-01 female, -02 male) was measured; male line prints no date.
- Hahnia dabashan and Neoantistea diagnoses: Hahnia's came only as a paraphrase; conditions say so. Crossref not queried for ZooKeys 1254, BDJ, or ZooKeys 1197.
- Female eye sentences print "PLE, 0.xx" with a comma; copied as printed.

## Not filed
- Uaica: EJT 989 describes five species (abstract and list read), all filed by d378; nothing left. Heteropoda EJT 1022 has three new species, all filed by d378.
- Sinahahnia yintiaoling (female only, ZooKeys 1197), Asceua/Mallinella female sentences of ZooKeys 1200 species already on main in conditions text: not filed.
- Pseudopoda xiaozhua/yangae/ying (unreachable), Platnickina, Latouchia, Ischnothyreus, Trilacuna, Gamasomorpha, Zora, Wangaraneus, Shaanxinus, Poeciloneta, Parazygiella, Oedothorax simianensis, EJT 1007: not opened. The Wang LY / Zhang ZS Hahniidae and Zodariidae papers use the same labelled one-sentence format and are the easiest further leads.

## Desk disposition after audits 535-540 (2 November 2026)
All 43 records merged with the auditors' replacement lines. 35 of 43 in error (81%), all in note and conditions text; no value, quote, trait or taxon changed, no record repeats main, and no line was dropped. Audit 535 (Asceua chayu, Cydrela linzhiensis female): 8 of 8 (Asceua clypeus and carapace sentences and the Cydrela female "other characters same as male" sentence omitted). Audit 536 (Cydrela male, Hahnia dabashan, Sinahahnia chengkou): 7 of 8 (the "Carapace brown." and clypeus sentences omitted; the Hahnia notes wrongly said the MOA sentence has a double full stop; Hahnia's PLE does print as "0.0.05", so filing no PLE is right). Audit 537 (S. chengkou, Neoantistea yintiaoling): 1 of 8 (the yintiaoling conditions placed "female unknown" in the abstract; it is in the Description). Audit 538 (S. chengkou, S. eyu): 8 of 8 (Clypeus-height and chelicerae/genus "Eight eyes." sentences omitted, 8 wrong grep statements, line 32's female sex not tied to the Fig. 3 caption). Audit 539 (S. fanjingshan): 8 of 8 (Clypeus-height, genus "Eight eyes." and carapace sentences omitted, "Maxi’ao" misprinted). Audit 540 (S. fanjingshan, last 3): 3 of 3 (Description start misstated, "Clypeus height 0.08." omitted, a straight apostrophe in Maxi’ao, and the false claim that desk-d296 and audit-387 contain DOI 119935). Owner questions: Asceua chayu is unchecked on the World Spider Catalog (page refused); Sinahahnia chengkou's female paratype HA-09-02 does not match the printed paratype list (confirmed, kept as printed).
