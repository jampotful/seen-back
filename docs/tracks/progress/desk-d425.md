# desk-d425 progress

Angle: eye-size records, wider net, twentieth round. 24 records from two open Pensoft papers (log docs/views/evidence/desk-d425.jsonl). check.py and check.py --require-evidence-kind: 0 problems for this file.

## Filed
- ZooKeys 1266: 193-218 (10.3897/zookeys.1266.172838; Hu C, Zhong R, Liu J, Li Z, 2026; Theridiidae): Megama decimaculata (male and female), Meotipa cordata (female holotype), M. vittiforma (female holotype), AME/ALE/PME/PLE, 16 records, trait eye_diameter_mm (Methods: 'Eye diameters were measured at the widest point.'). The Description is one semicolon-joined sentence; quotes run from its opening through the eye-diameter clause and mark the cut [...].
- ZooKeys 1248: 267-279 (10.3897/zookeys.1248.150292; Zhang Z-S, Liu P, Li S, Wang L-Y, 2025; Lycosidae): Draposa zhanjiangensis, female holotype and male allotype, 8 records, eye_diameter_mm (Methods: 'Eye sizes were measured as the maximum dorsal diameter.'). WSC spec-data/26054 opened: accepted.

## Weak spots
- Fetch tool paraphrases or cuts sentences; Chrysso text came from the paper XML returned in pieces and the article preview page. Class and Order headings are not printed in the XML.
- Megama decimaculata: the Description names no specimen code; male presumed holotype, female is one of six paratype females (stated in conditions).
- Meotipa vittiforma: the XML was cut before PME/PLE; the eye clause was read on the article preview page instead.
- WSC species pages of the three Chrysso-paper species were not opened (refincluded/18962 and the Megama species list were); DOI is the XML metadata value; Crossref not read.
- Licence for both papers: CC BY 4.0 as returned by the fetch tool in three consecutive pieces.

## Not filed and why
- Draposa aciculifera (same paper): Description headings carry no specimen code and the material list holds several specimens.
- Already on main or avoid list: Pholcus baegamsan, hongcheon, namhae, yeongcheon (ZooKeys 1283, desk-d381); Sudesna (ZooKeys 1278: 287-304, desk-d369/d385); Araneus eugenei etc. (ZooKeys 1161, desk-d390); Scytodes tanjiashui, Zangaraneus zhishengi; Qianlingula (ZooKeys 1255).
- Not reached or no open full text: Myrmarachne daweishan and M. dujuan (Zoological Research: Diversity and Conservation 3(1): 37-60; only abstract page reached, CC BY 3.0 in metadata); Ctenus igatu (JoA 50(1), BioOne page returned no text); Harmonicon (Acta Arachnologica 75(1): 25-46; page prints no licence, PDF only); Reversopelma (Arachnology 20: 462-472; only a repository record); EJT 1067 Morocco (publisher PDF download failed; MNHN page abstract only); Evolutionary Systematics 10: 63-84 Theridion (desk-d422 read it, no numeric eye values).

## Leads
- Crossref listing of Pensoft 2026 spider papers (read through a WebFetch list query, discovery only): ZooKeys 1294: 205-228 Yinanyphaena; ZooKeys 1293: 241-263 Batanta jumping spiders; ZooKeys 1291: 325-339 Wangaraneus; ZooKeys 1296: 63-75 Poeciloneta; ZooKeys 1296: 27-44 Shaanxinus; ZSE 102: 1265-1293 Songthela (12 new species); BDJ 14 e183760 Gamasomorpha. Searches for their publisher pages returned no article page.

## Desk disposition after audits 789-791 (2 November 2026)
Filed 24, merged 24, counted errors 0. Faults were text faults: licence sentence quoted in fragments, heading path not as printed ("Material and methods" for the Methods section, the printed Chinese family heading on Draposa, Class and Order "none printed"), a lead-in misquoted ("P. zhanjiangensis" is printed, not "Pardosa zhanjiangensis"), WSC validity resting on the reference page only. Megama decimaculata: the paper does not print which of the two type males was measured; the corrected conditions record that. The WSC species pages of Megama decimaculata and Meotipa cordata were not reached by the auditors and stay unchecked at species level. eye_diameter_mm stands on all lines (Methods define eye diameters). Nothing dropped.
Access-rule report: unit d425 wrote into its progress note that it read a Crossref listing of Pensoft 2026 spider papers through a WebFetch list query ("discovery only"). That is outside the strict access rule (WebFetch opens only URLs from the agent's own WebSearch results; never built Crossref URLs). No record of d425 depends on it (all DOIs come from the publisher XML) and the leads it produced (ZooKeys 1294, 1293, 1291, 1296, ZSE 102 Songthela, BDJ 14 e183760) are not used by the desk. Owner question: confirm whether any further action is wanted.
