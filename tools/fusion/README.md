# The recognizer's scoring, in one place

`fuse.py` is the plain-numpy reference of what the page computes in `fuseWith` (`src/cam.rec.js`, reached as `pocket.fuse`): from the
scores of the kind rows and the species rows, the month, the slot's manifest and its species table, to
`{kind, kindP, kinds, species, named, offers}`. Its interface is at the top of the file. `python3 -I tools/fusion/fuse.py` reruns five
cases whose answers the page gave (the stand-in slot under `test/rec/models/standin`) and exits 1 if any differs.

## State on 11 October 2026, 01:15 Eastern (build 7)

The page and the reference now compute the same thing for everything a manifest can ask for: sentence-made heads and trained heads
(`kinds.bias`, `species.bias_url`, rows that are not unit vectors), both combination rules (`fusion.rule`), and `fusion.guard`.
Numbers made with `fuse.py` are "as shipped" from build 7 on. Build 6 (live until build 7 is merged) ignores biases, `rule` and `guard`.

`parity.py` with `test/rec/fuse_page.js` holds the two together. Last run (headless Chromium, this sandbox, build 7):

- 2,073 score cases, all the same in kind, order of kinds, top five, name, offers and which kinds the species list speaks for; the
  largest difference in any probability was 5.1e-16. Of these, 409 go into the stand-in slot as the page loaded it (product rule, no
  biases; the cases of build 6's check), and 1,664 go into 128 made-up settings handed to the page through the same readers a real slot
  passes: each rule (832 cases each), biases for the kinds, the species, both or neither (1,144 cases with a bias), temperatures from
  1e-4 to 1e5, weights of 0 and 1, `prior_floor` 0, 1e-3, 1e-6 or absent, `guard` 1e-30, 1e-9, 1e-3 or absent, `offer_any_kind`,
  thresholds of 0 and above 1; tables with a row that has no monthly weights, a row never recorded, a row given as an object, a kind no
  page knows, a person, a month in which no row has a record, one row only, or no table; labels that lack kinds the table has; every
  score equal, every score zero, no month known, one head sure against the other, two kinds tied, the species head left out.
- 9 photos through the stand-in's trained-head slot (`manifest.trained.json`: rows of several lengths, `kinds.bias`,
  `species.bias_url`, rule `mix`) from pixels to answer in the page. The reference recomputed the row scores from the page's own
  embedding and the slot's files (largest difference 1.1e-7; the page's scores are single precision) and the answer from the page's row
  scores (largest difference in a probability 2.2e-16).

One thing learned on the way: numpy's `sum` pairs terms up and the page adds them left to right, which differs in the last place and
broke one exact tie the other way round. The reference now adds left to right too (`total`). `np.exp` and the browser's `Math.exp` may
still differ in the last place; no case has shown it.

To rerun (any free port; 8782 is the default):

    node test/rec/serve.js 8783 &
    python3 -I tools/fusion/parity.py make /tmp/cases.json
    PORT=8783 NODE_PATH=<where playwright lives> node test/rec/fuse_page.js /tmp/cases.json /tmp/page.json
    python3 -I tools/fusion/parity.py check /tmp/cases.json /tmp/page.json

`test/rec/check_rec.js trained` asks the browser, through the page's ordinary flow, for the answers the reference gave for each test
photo under the trained-head slot (`expect.json`, written by `test/rec/make_standin.py`), and checks that a rule the page does not
know and a bias file cut short are refused in words.

## For whoever tunes the settings

    from fuse import fuse, dots, load_slot
    slot = load_slot("path/to/slot")          # or the path of a manifest file inside a slot
    out = fuse(slot["manifest"], slot["table"], month, dots(slot["kinds"], e), dots(slot["species"], e),
               kind_bias=slot["kind_bias"], species_bias=slot["species_bias"])

- `load_slot` reads the rows from the half-precision files, so what it scores is what the phone scores. Rows made in double precision
  and scored without that round trip are not "as shipped".
- `month` is 0 to 11, or `None` (no prior). The page uses the month of the device's clock at the moment of the photo.
- To try settings, copy the manifest and change `manifest["fusion"]`; pass the same `table` object each time (it is prepared once
  and kept by identity, with its priors).
- A trained head: the score of a row is `t * (row . e) + bias`, `e` the unit image vector. A head trained as `W e + b` ships as rows
  `W`, bias `b` and `t = 1`. Biases for kinds are a JSON list in the manifest (`kinds.bias`, one for each label, in order); for species
  a file of little-endian float32 (`species.bias_url`, one for each row). Rows are float16 in the file: weights beyond about 65,000, or
  differences below one part in two thousand of a weight, do not survive it.
- The page refuses a slot whose manifest has a `fusion.rule` other than `"product"` or `"mix"`, a `kinds.bias` that is not one number
  for each label, a `fusion.guard` that is not a positive number, or a bias file of the wrong length ("The recognizer's files do not fit
  this build of the page." / "The recognizer's file arrived damaged."), and then asks the person to type the name. `fuse()` raises
  `ValueError` on an unknown rule.

## What is computed

1. Kinds: `z_k = t_kind * (row_k . e) + bias_k` (bias 0 for a sentence-made head), `p = softmax(z)`. `e` is the unit image vector.
2. Species, if the slot has them: `z_i = t_species * (row_i . e) + bias_i + alpha_prior * log(max(share_i, prior_floor))`, `s = softmax(z)`.
   `share_i` is species i's part of all records of that calendar month in the table (rows without twelve monthly weights count as zero).
   The prior is left out when the month has no records at all, when no month is known, and when `alpha_prior` is 0.
   `prior_floor` defaults to 1e-6.
3. `q_k` = the sum of `s` over the species of kind k. The species list "speaks for" a kind if at least one species in the table is of
   that kind; for `none` it never does, and for `person` only if the table lists a person. A species of a kind that is not among the
   labels counts toward no label.
4. The combination, chosen by `fusion.rule`:
   - `"product"` (the default, and the only rule of build 6): for a kind the list speaks for,
     `score_k = w_kind * log(max(p_k, guard)) + (1 - w_kind) * log(max(q_k, guard))`; for any other kind, `score_k = log(max(p_k, guard))`;
     then `c = softmax(score)`. `guard` is `fusion.guard`, 1e-9 if absent.
     Its weakness: with a large temperature both heads put nearly everything on one answer, and when they disagree each side's score is
     `w * log(1) + (1 - w) * log(guard)` or the mirror of it, so the result depends on `guard` and `w_kind` alone and not on how sure either
     head was. (`check_rec.js fuse` shows it: at temperature 100, kinds sure of a plant against a list sure of a heron, `w_kind` 0.7,
     gives the plant 0.9997 with guard 1e-9 and 0.846 with guard 1e-3; the mix gives it 0.7 and the heron's kind 0.3.)
   - `"mix"`: let `A` be the sum of `p_k` over the kinds the list speaks for. For such a kind, `c_k = w_kind * p_k + (1 - w_kind) * A * q_k`;
     for any other kind, `c_k = p_k`; then the `c_k` are divided by their sum (which is 1 unless the table has species of kinds outside
     the labels; if the sum is 0, `c = p`). The species head can only re-divide the share the kinds head gave to the kinds it can speak
     for, and can move at most `1 - w_kind` of it, however sure it is; there is no logarithm and no guard. When both heads are sure and
     disagree, the kinds head's choice gets `w_kind` and the species head's `1 - w_kind`, so `w_kind` above one half means the kinds head
     wins such a clash and below one half the species list does; at exactly one half it is a coin's edge and should be avoided.
   - `w_kind = 1` gives the kinds alone under both rules.
5. The kind is the largest `c_k` (ties: the earlier label). If it is `none` or `person`, no species is named or offered.
6. Otherwise the likeliest species is named if its `s` is at least `name_at` and its kind is the winning kind. If not, the three likeliest
   species of the winning kind (of any kind, with `offer_any_kind`) are the offers, provided their `s` together reach `offer_at`.
   (`s` is the species head's own probability with the prior; the combination rule changes the kind, never `s`.)

Nothing here chooses a threshold or a rule: every number comes from `manifest["fusion"]`, and both rules are there to be compared on
the validation photos.
