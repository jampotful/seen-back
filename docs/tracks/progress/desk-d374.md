# desk-d374 progress

Angle: multi-species taxonomic papers (mygalomorph, linyphiid). 32 records from two papers, about 42 search/fetch calls. check.py run on the log.

## Filed (docs/views/evidence/desk-d374.jsonl)
- European Journal of Taxonomy 1022: 19-50 (10.5852/ejt.2025.1022.3079; page-printed CC BY 4.0 on the journal download copy): Neischnocolus (Theraphosidae) moraspungo (female holotype), samonellaacademy (male holotype), tiputini (female holotype), AME/ALE/PME/PLE each, sensory_anatomy (Methods define no eye measure, no "diameter") (12). WSC pages 72730-72732 opened.
- ZooKeys 1253: 243-254 (10.3897/zookeys.1253.165585; XML prints CC BY 4.0): Linyphiidae of Hunan, Gongylidioides heimifengensis (male holotype, female paratype), Gongylidium subbifurcatum, G. trapezium, Nippononeta anchorata (female holotypes), 'Eye sizes and interdistances' sentences, sensory_anatomy (20). WSC pages 72706-72709 opened.

## Weak spots
- All text came through fetch-tool summaries, long sentences in consecutive pieces and rejoined.
- Neischnocolus samonellaacademy: a full stop was returned between PME-PLE and AlE-PLE inside the "Eyes:" entry; recorded as returned. All three entries print "AlE-PLE". Type line for N. tiputini returned as "ZSFQ-20415" in the line and "ZSFQ-i20415" elsewhere.
- Neischnocolus: "no other eye sentence" is the tool's report, stated as such; the heading "holotype" was returned only for moraspungo.
- Hunan: Diagnosis and remarks were not read; minus sign in interdistances is U+2212 as returned.

## Not filed
- EJT 1007 (10.5852/ejt.2025.1007.2999) Ecuadorian Microstigmatidae, six new species (Pastaza, Spelocteniza): full-text download URL refused/failed, not read. Lead for the next unit.
- Latouchia (ZooKeys 1265.175629): eye values sit inside one 'Measurements:' sentence far over 40 words; not quotable.
- Oedothorax simianensis, Sinartoria (1244): not opened.
