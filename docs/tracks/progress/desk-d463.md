# desk-d463 progress

Angle: eye-size records, wider net, round 45 (spider unit). 34 records from two open Pensoft ZooKeys papers already partly on main (log docs/views/evidence/desk-d463.jsonl). check.py: desk-d463.jsonl 0 problems, also with --require-evidence-kind (other files on main carry older problems, untouched).

## Filed
- ZooKeys 1245: 269-287 (10.3897/zookeys.1245.152487; Kong J-X, Mu Y-N, Zhu B-C, Lu W, Zhang Z-S, Wang L-Y, 2025; Amaurobiidae; CC BY 4.0 sentence read on the preview page): Amaurobius foping (female holotype SWUC-T-AM-24-01), A. pingwu (male holotype SWUC-T-AM-25-01, female paratype SWUC-T-AM-25-02), A. yushen (male holotype SWUC-T-AM-26-01, female paratype SWUC-T-AM-26-02); AME/ALE/PME/PLE each, 20 records, eye_diameter_mm because the Methods print 'Eye sizes were measured as the maximum dorsal diameter.' Only the seven Sinoamaurobius species of this paper were on main (desk-d380, desk-d405).
- ZooKeys 1249: 371-385 (10.3897/zookeys.1249.152933; Lu J-Z, Marusik YM, Zhang Z-S, Wang L-Y, 2025; Lycosidae; CC BY 4.0 sentence read on the preview page): Zoica dulong male holotype AME, ALE, PLE and female paratype x4 (no code in the heading, none recorded); Z. thailandica male holotype AME, ALE, PLE and female paratype SWUC-T-LY-30-02 x4; 14 records, sensory_anatomy (label 'Eye sizes', no eye definition in Methods; as desk-d357). Main held only the male PME of dulong and thailandica.
- WSC species pages spec-data/72199, 72200, 72201 (Amaurobius) and 72509, 72511 (Zoica) opened from search results: all accepted, original descriptions in these papers.

## Weak spots
- Page text came through the fetch tool's summarising step; eye sentences arrive in two pieces (split at the semicolon) and are rejoined; values were re-read identically (three readings for ZooKeys 1245, two for 1249).
- Crossref version of record not read (UNCHECKED); licence read on the preview page only.
- The Amaurobius pingwu and yushen species heading lines were read through the fetch tool answering a direct question (no separate Genus line); the female MOA sentence of A. pingwu prints 'back with' (sic).

## Not filed
- Zoica medogensis (male sentence prints PME 0.01 and run-together interdistances; no WSC species page reached) and Z. oculata (no specimen code).
- Dolomedes rotundus (PeerJ 12: e16781): fetched text ended before it (twice). Pardosa armeniaca (ZooKeys 1180): no eye sentence. ZooKeys 1251 Moneta, 1174 Gnaphosidae, 1181 Liocranidae, 1125 Tetragnatha, 1072 Araneidae, 1278 Calommata hangzhica, JoTT 17(8) and 13(12): already on main or no numeric eye values. Leviana (Evolutionary Systematics 6(2)): no eye diameters. Poeciloneta (ZooKeys 1296), Batanta, Harpactocrates trenti: no publisher page reached.
- Leads: other species of already-mined papers whose main lines hold only one eye or one sex (check per-eye coverage in the jsonl before choosing a paper); Moneta linzhi and M. yinae (ZooKeys 1251) have only the male PME on main.

## Desk disposition after audits 934-938 (3 November 2026)
Audited by five fresh Opus agents. 27 of 34 records merged; 7 dropped as repeats of main: the conditions text of the desk-d357 rows already prints the Zoica dulong male AME 0.05, ALE 0.05, PLE 0.11 and female PME 0.12, and the Zoica thailandica male AME/ALE/PLE (lines 21-23, 26, 28-30). Audits 936 and 937 kept them and raised the question; the desk applies the standing rule that findings carried only in a main row's note count as repeats (as in audits 268 and 289). Remaining faults (headings dropping the printed Chinese family and subfamily names, note wording about main, the omitted Variation sentence) fixed with the auditors' replacement text. Amaurobius lines (1-20) passed with the note about main corrected.
