# The recognizer's scoring, in one place

`fuse.py` is the plain-numpy reference of what the page computes in `pocket.fuse` (`src/cam.rec.js`): from the scores of the kind rows
and the species rows, the month, the slot's manifest and its species table, to `{kind, kindP, kinds, species, named, offers}`.
Its interface is at the top of the file. `python3 -I tools/fusion/fuse.py` reruns five cases whose answers the page gave
(build 6, the stand-in slot under `test/rec/models/standin`) and exits 1 if any differs.

## State on 11 October 2026, 00:40 Eastern: read this before relying on it

- **Same as the page (build 6):** the `product` rule with no biases. Checked only on those five cases, to the four decimal places recorded
  from the page. The parity check asked for (random and adversarial cases, both sides, agreement to 1e-6) is **not written yet**.
- **In the reference only, not in the page yet:** a trained head's biases (`kind_bias`, `species_bias`), and the `mix` rule.
  A manifest that carries a bias or `"rule": "mix"` is scored by the reference as described here and by build 6 as if neither were there.
  Numbers made with them are therefore "as proposed", not "as shipped", until the page follows.

## What is computed

1. Kinds: `z_k = t_kind * (row_k . e) + bias_k` (bias 0 for a sentence-made head), `p = softmax(z)`. `e` is the unit image vector.
2. Species, if the slot has them: `z_i = t_species * (row_i . e) + bias_i + alpha_prior * log(max(share_i, prior_floor))`, `s = softmax(z)`.
   `share_i` is species i's part of all records of that calendar month in the table (rows without monthly weights count as zero);
   if the month has no records at all, the prior is left out. `prior_floor` defaults to 1e-6.
3. `q_k` = the sum of `s` over the species of kind k. A kind "has rows" if at least one species in the table is of that kind;
   `none` and `person` never do.
4. The combination, chosen by `fusion.rule`:
   - `"product"` (the default, and what build 6 does): for a kind with rows, `score_k = w_kind * log(max(p_k, guard)) + (1 - w_kind) * log(max(q_k, guard))`;
     for a kind without rows, `score_k = log(max(p_k, guard))`; then `c = softmax(score)`. `guard` is 1e-9 (in the page it is a constant; the reference reads `fusion.guard`).
     Its weakness: with a large temperature both heads put nearly everything on one answer, and when they disagree the result depends on `guard` alone.
   - `"mix"` (proposed): let `A` be the sum of `p_k` over the kinds with rows. For a kind with rows, `c_k = w_kind * p_k + (1 - w_kind) * A * q_k`;
     for a kind without rows, `c_k = p_k`. The `c_k` sum to 1. The species head can only re-divide the share the kinds head gave to the kinds it can speak for,
     and can move at most `1 - w_kind` of it, however sure it is; there is no logarithm and no guard. `w_kind = 1` gives the kinds alone under both rules.
5. The kind is the largest `c_k` (ties: the earlier label). If it is `none` or `person`, no species is named or offered.
6. Otherwise the likeliest species is named if its `s` is at least `name_at` and its kind is the winning kind. If not, the three likeliest species
   of the winning kind (of any kind, with `offer_any_kind`) are the offers, provided their `s` together reach `offer_at`.

Nothing here chooses a threshold: every number comes from `manifest["fusion"]`.
