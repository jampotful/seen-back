# Evidence compatibility fixtures

These files exercise validators and consumers. They are not accepted evidence,
independent scientific dispositions, or source texts. Production evidence loaders
do not discover this directory. Tests write temporary logs only in disposable
directories.

- `anatomy-d208.jsonl`: byte-identical to the four proposed records in PR #49 at
  `d5552710fb4cfca16dd02f85c9512d709168e67a`, originally
  `docs/views/evidence/anatomy-d208.jsonl`. Admission remains pending.
- `melotte-2018/evidence.jsonl` and `melotte-2018/audiograms.json`: byte-identical
  copies from PR #50 at `ef1bac785f8f1db5e3aad2814c0b19ea4197a19d`, originally
  `docs/views/evidence/melotte-2018.jsonl` and
  `docs/views/sources/melotte-2018-audiograms.json`. All eight candidates still need
  independent audit; the two modern-species identity restrictions remain intact.
  `test_melotte_2018.py` reuses that PR's eight compatibility tests, changing only
  the fixture locations and this integration-specific description.
- `intake-recent.json` pins the accepted legacy snapshot used by PR #51's tests.
  It does not type, migrate or edit those records.

`recheck-ecological-350.jsonl` is a byte-identical fixture of the five PR #52
proposed corrections at `bce567d9d31d73e800208c3a890480397c832b62`, originally
`docs/views/recheck/recheck-ecological-350.jsonl`. The original proposal remains
on PR #52 for independent disposition. The fixture is
not loaded as accepted evidence and is not applied by the test suite outside
temporary directories. The conservative fingerprint limits restrict use of the
original findings without changing their content or historical audits.
