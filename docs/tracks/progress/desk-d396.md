# desk-d396 progress

Angle: remaining new species of ZooKeys 1221: 205-277 (not filed by desk-d395), then a second open Pensoft Salticidae paper. 45 records (log docs/views/evidence/desk-d396.jsonl). check.py: 0 problems, also with --require-evidence-kind.

## Filed
- ZooKeys 1221: 205-277 (10.3897/zookeys.1221.135640; Wang C, Mi X, Li S, Xu X, 2024): Cheliceroides jinxini (male), Mintonia shiwandashan (male), Pancorius medog (female), Piranthus maddisoni (male); AME, ALE, PLE; 12 records.
- ZooKeys 1192: 141-178 (10.3897/zookeys.1192.114589; Wang C, Mi X, Li S, 2024; Crossref vor CC BY 4.0, page prints CC BY 4.0): Attulus jimani, Colaxes cibagou, Epeus pengi, Evarcha zayu, Pancorius nyingchi (male and female each), Icius zang (male); 33 records.
- All records sensory_anatomy: the sentences print 'Eye sizes', the Methods define no eye dimension. Values checked by script against the number printed for the eye label; no zeros.

## Weak spots
- The fetch tool summarises and cuts at 125 characters; type lines and neighbouring sentences are tool-returned pieces, not page copies. Neither paper says which type specimen was measured.
- ZooKeys 1221: the publisher preview text ends inside the male description of Piranthus maddisoni, so the 1221 species after it (Simaetha hainan, Stertinius lhoba, Synagelides kongmingi, S. xuandei, S. yunchangi, S. yidei, S. zilongi, Yaginumaella daweishan, Y. moinba, Y. pingbian) and the P. maddisoni female were not reachable. Only four of the remaining new species were reachable, not six; Okinawicius nepalicus (comb. nov.) and Padillothorax exilis are not new species and were not filed.
- WSC species pages opened for all but Mintonia shiwandashan and Piranthus maddisoni (UNCHECKED); family pages not opened.
- Pancorius medog and Piranthus maddisoni: the 'Results' heading above the family heading was not read separately for them (taken from the paper's single Results section).

## Not filed and why
- ZooKeys 1192: Icius zang female (printed 'ALE 0.26 PLE 0.19' without a comma); Synagelides medog female and Phintella longapophysis female (fetch returned identical sentences, possible tool error); Stertinius liqingae, Synagelides tianquan, Yaginumaella erlang (type lines returned only as paraphrase, not verbatim). Leads for a later unit.

## Desk disposition after audits 629-634 (2 November 2026)
All 45 lines were audited by fresh Opus agents (audits 629 to 634). Counted errors: 6 lines. Lines 4-6 were filed as Mintonia shiwandashan; WSC (spec-data/70904) lists the accepted name Protaeus shiwandashan (transferred by Ni, Yu & Zhang 2025b), so the auditor's replacement files them under Protaeus shiwandashan and they are merged. Lines 9-12 (Pancorius medog PLE, Piranthus maddisoni AME/ALE/PLE, ZooKeys 1221) were HELD OUT by audit 630 (the publisher XML it could open stopped before those treatments, and the conditions named the holotype as the measured specimen although the paper never says which specimen was measured) and are dropped. Remaining 41 lines merged with the auditors' corrected text: Cheliceroides jinxini, Protaeus shiwandashan, Pancorius medog (AME, ALE) from ZooKeys 1221; Attulus jimani, Colaxes cibagou, Epeus pengi, Evarcha zayu, Icius zang (male), Pancorius nyingchi from ZooKeys 1192. Faults corrected: figure references on species headings ("Figs 5, 6, 22B"), "the sentence before the eye sentence", Methods heading wording, omitted "Methods followed Wang et al. (2024)." (ZooKeys 1221 only; ZooKeys 1192 Methods read whole, no diameter definition, no deferral). Trait stays sensory_anatomy. Leads: Pancorius medog PLE and Piranthus maddisoni (ZooKeys 1221) need a reachable publisher page; Wang et al. (2024) may define eye size. Crossref vor unchecked by auditors.
