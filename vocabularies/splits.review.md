# Review: `splits` vocabulary and new `datasets` names

## What is being reviewed and how

`litrev normalise` ran on 2026-10-10 (anthropic `claude-sonnet-5`, effort
`low`, about $0.09) after the second full `tabulate` run of that day, which
added the results table's `split` column. It proposed a first `splits`
vocabulary, from every value of `tables.json`'s `results.split` column, and
new entries for the existing `datasets` vocabulary, from the dataset names
the re-run introduced. The proposals are `vocabularies/splits.proposed.json`
and `vocabularies/datasets.proposed.json`.

For each proposed cluster: approve it, reject it, or rename its label. For
each unassigned name: assign it to a label (existing or new), or leave it
unassigned. `normalise.require_complete` is off, so a name left unassigned
is grouped as written rather than failing `report`. Decide on the
interactive page, <https://claude.ai/artifact/BuNPi86g7keATdfnSdbzTa>; the answers are copied into the Answers
section and then into `vocabularies/splits.json` and `vocabularies/datasets.json`.
`appraise` and `report` wait for this review.

<!-- doc-counts: accept-start counts taken from the 2026-10-10 proposals - a record of them, not of the review now -->
## Automatic checks

| Check | `datasets` | `splits` |
|-------|-----------|----------|
| Every name sent is in a cluster or unassigned | pass: 17 + 116 = 133 | pass: 66 + 129 = 195 |
| No name both clustered and unassigned | pass | pass |
| Every name found in the review's data | pass | pass |
| Clusters holding only their own name | 3 | 50 |

## The items

### `datasets`: 13 proposed clusters

All recommended for approval. Each folds a spelling or short form into an
existing or new label: "PAN 2015" into PAN-AP-2015, "Fisher" into Fisher
dataset, "WASSA-2022" into WASSA 2022, "ASF developer email corpus" into ASF,
"Twitter (Indonesian dataset)" into Indonesian Twitter Personality Dataset,
and spelling pairs for Cornell Movie-Dialogs, D_HR, D_LR, WASSA 2024 Track 4
and YouTube personality dataset. Backstage, FriendFeed and MaSaC hold only
their own names.

### `datasets`: 116 unassigned names

Recommended left unassigned, except three that match an existing label's
alias:

- "Stream-of-consciousness writing" to Essays
- "YouTube vloggers" to YouTube personality dataset
- "LinkedIn" to LinkedIn profiles

### `splits`: 57 proposed clusters

Recommended for rejection, because each merges conditions a paper reports
apart:

- "English, 10-fold cross-validation", and the Italian and Spanish ones:
  fold "tweet-level" into a user-level condition.
- "70:30 train-test split", "80:20 train-test split": merge two
  preprocessing scenarios.
- "HIGH class", "LOW class": fold a metric on a class ("High class recall")
  into the class.

The other 50 hold only their own name and merge nothing; approving them
fixes the spelling. Forty-two of them are "data type: ..." and "use case:
..." labels from a single paper, which put its own categories into `split`.
They are recommended for approval as harmless, and noted as a `split`
residual rather than fixed here.

### `splits`: 129 unassigned names

Recommended left unassigned: most are one paper's own condition, which
groups correctly as written.
<!-- doc-counts: accept-end -->

## Decisions

Each item above is the decision; the page shows the recommendation beside
each, and a button that accepts the recommendations for the items still
undecided.

## Answers

<!-- doc-counts: accept-start answers given on 2026-10-10 - a record, not a claim about the present -->
**`datasets`, answered 2026-10-10 on the page**: every item as
recommended - the 13 clusters approved, the three names assigned
(Stream-of-consciousness writing to Essays, YouTube vloggers to YouTube
personality dataset, LinkedIn to LinkedIn profiles), the other 113 left
unassigned, no notes. Adopted into `vocabularies/datasets.json` the same
day: 63 labels became 70, 221 aliases 234; it loads and validates.

**`splits`**: not yet answered - none of its 186 items had a decision when
the page was read on 2026-10-10.
<!-- doc-counts: accept-end -->
