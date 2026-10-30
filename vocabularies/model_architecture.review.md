# Review: `model_architecture` coded into model families

Interactive page: https://claude.ai/artifact/PTAbREBP3WuAH93kBzAwTn

## What is being reviewed and how

<!-- doc-counts: accept-start counts from the 2026-10-30 runs on this clone - a record, not a claim about the present -->
The extracted field `model_architecture` is free text, with 900 distinct
values across the review's papers on 2026-10-30. To count papers per kind of
model (the explorer's How often panel), the values were coded into 13 fixed
families with `normalise`'s `categories` option, on the APFS clone
`/Users/simonb/src/phd/reviews/big-five-nlp-models-20261030`. The real
review is unchanged.

For each family: approve or flag it, and move any member that is wrong. For
each value left unassigned: pick its family, or leave it as written. Answer
the one decision.

## Runs

All anthropic `claude-sonnet-5`, on the clone, 2026-10-30:

- Pass 1, spelling merge, effort low: 900 values sent, 25968 input and 21574
  output tokens, $0.27. 42 groups, 534 unassigned. Kept in `pass1/`.
- Pass 2, spelling merge of the 534 leftovers, effort medium: 17367 input
  and 27466 output tokens, $0.31. 40 more placed, 494 unassigned. Kept in
  `pass2/`. A spelling merge does not group distinct systems, so it was
  replaced by family coding.
- Family coding, effort low: 900 values sent, 26519 input and 17570 output
  tokens, $0.23. 783 values in 13 families, 117 unassigned. This is the
  proposal under review: `vocabularies/model_architecture.proposed.json`.

Total spent: $0.81. The clone's `config.py` sets `llm.anthropic.max_tokens`
to 32768 (LitRev's cap; pass 1's answer would not fit in 16384), adds the
`model_architecture` vocabulary with its `categories`, and adds
`normalise.instructions` describing each family.
<!-- doc-counts: accept-end -->

## Automatic checks

- Pass: every member is one of the values sent. The validator dropped 2
  invented values ("Sequence-to-sequence encoder-decoder", "Semi-supervised
  hybrid loss with confidence-based pseudo-labeling").
- Pass: every label is one of the 13 categories.
- Pass: no value sits in two families.

## The items

The families, with their meaning, are on the page; each lists every member
and its paper count. Of the 117 unassigned values, 99 start with a
prediction setup ("per-trait models (...)", "multi-output (...)"), and 26
of those also name a model. Each unassigned value carries a recommended
family from the model or setup it names.

## Decisions

### D1: how to code a value that names both a prediction setup and a model

- **What is being decided:** whether "per-trait models (five separate binary
  SVMs, one per Big Five trait)" is coded by its model (`svm`) or as
  `prediction_setup`.
- **Background:** this review's extraction lists how the traits are predicted
  in the same field as the models. `prediction_setup` exists for values that
  name no model.
- **What it affects:** paper counts per family, and which papers count as
  using each kind of model. The raw field keeps its full text either way.
- **Options:**
  - **Code by the model it names (recommended):** only a value naming no
    model goes to `prediction_setup`; the family counts show the models
    papers use. The unassigned picks are recommended on this basis.
  - **Code every setup value as `prediction_setup`:** the setup count is
    complete, but those papers' models drop out of the model families; the
    affected picks are recoded when the answers are applied.

## Answers

Answered 2026-10-30 on the page, read back the same day:

- Every family: approved, no comment. No member moved.
- D1: code by the model it names (the recommended option).
- Every unassigned value: its recommended family (117 picks, none left as
  written).

Applied 2026-10-30: `vocabularies/model_architecture.json` holds the
proposal's entries plus the picks, on the clone only.

Adopted 2026-10-30 into this review, with the clone's `config.py` changes;
backup `output/backup-pre-models-20261030`. The pass 1 and pass 2 proposals
stay on the clone.
