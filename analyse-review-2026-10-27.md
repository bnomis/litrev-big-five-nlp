# Review: pooling each paper's main condition

Interactive page: <https://claude.ai/artifact/Erw38GmqGqy2r8WuqPbdYi>

## What is being reviewed and how

LitRev's `analyse` gained two settings on 2026-10-27 (LitRev commits
`6f0d503d`, `67e3bce4`, `c746c444`, on `main`, not pushed): `where` now takes
`None` for an empty cell and a list for any of its values, and each analysis
takes `exclude`, a paper key mapped to the reason it is left out. This
review's `config.py` now pools only each paper's main condition
(`'split': [None, 'N_ta=500']`) and excludes Pantheon. `analyse` and `report`
were re-run (backup `output/backup-pre-where-exclude-20261027`). Four
decisions remain; answer each on the page, where every answer saves as it is
made.

<!-- doc-counts: accept-start figures from the 2026-10-27 runs - a record, not a claim about the present -->
## Automatic checks

- pass: rehearsed on the APFS clone `big-five-nlp-where-exclude-20261027`
  first; the real run's `analyses.json` results are identical to it.
- pass: every row the filter dropped is a subset, informant, subsample,
  10-fold, "titles" or N_ta=100 row; `2021.naacl-main.357` is kept at
  N_ta=500.
- pass: Pantheon's matching rows are listed as "excluded by the review" with
  the reason, in openness and extraversion. Its only neuroticism row
  ("controlling for likability and demographics") fails `where` first.

## The items

| Analysis | Studies | Rows used | Pooled r [95% CI] |
|---|---|---|---|
| average | 7 → 7 | 14 → 10 | 0.353 → 0.354 [0.266, 0.435] |
| openness | 17 → 16 | 28 → 20 | 0.482 → 0.447 [0.340, 0.542] |
| conscientiousness | 14 → 14 | 22 → 17 | 0.445 → 0.446 [0.304, 0.568] |
| extraversion | 16 → 15 | 26 → 18 | 0.459 → 0.439 [0.343, 0.526] |
| agreeableness | 14 → 14 | 22 → 17 | 0.381 → 0.379 [0.255, 0.491] |
| neuroticism | 14 → 13 | 22 → 16 | 0.455 → 0.448 [0.310, 0.568] |

## Decisions

### D1. Keep WhiSPA in the pools?

- **Decided**: whether `doi:10.48550/arxiv.2501.16344` (WhiSPA, Rao et al.)
  is excluded from every analysis.
- **Background**: its pooled rows are WhiSPA-394 on HiTOP (n 524) and WTC
  (n 1396), r 0.72-0.83, the highest in every trait pool. They come from its
  Table 2, captioned "Self-Supervised Prediction Accuracies"; the text says
  these compare "our models' predictions to PsychEmb derived values" - a text
  model's trait estimates, not questionnaires. Its self-reported outcomes
  (Table 3) are PTSD and HiTOP scales, not Big Five. So the rows measure
  agreement with another model, as Pantheon's measure agreement with public
  perception.
- **Affects**: `config.py`'s `exclude`; every trait pool loses one study and
  two rows. Measured on the clone: openness 0.447 → 0.414, conscientiousness
  0.446 → 0.395, extraversion 0.439 → 0.401, agreeableness 0.379 → 0.326,
  neuroticism 0.448 → 0.397; average unchanged.
- **Options**:
  - **Exclude** (recommended): add it to `exclude` with that reason, re-run
    `analyse` and `report`.
  - **Keep**: the pools stay as above, with five trait estimates inflated by
    model-to-model agreement.

### D2. Commit the review's `config.py`?

- **Decided**: whether to commit the `where`/`exclude` change (and D1's
  exclusion if chosen) in the review repository.
- **Background**: only `config.py` is changed there; the run logs are
  untracked, as earlier ones are.
- **Options**:
  - **Commit** (recommended): `feat(analyse): pool each paper's main
    condition`, with this review document.
  - **Leave uncommitted**: the outputs then reflect a config no commit
    records.

### D3. Push LitRev's `main`?

- **Background**: `main` is three commits ahead of `origin/main`; hooks and
  the audit pass, and the affected tests pass.
- **Options**:
  - **Push** (recommended): CI runs `make check` on it.
  - **Hold**: the review's config depends on code only this machine has.

### D4. Delete the rehearsal clones?

- **Background**: five APFS clones under `$LITREV_REVIEWS_ROOT/`:
  `big-five-nlp-n-sample-20261026`, `big-five-nlp-n-sample-20261027`,
  `big-five-nlp-normalise-rehearsal-20261027`,
  `big-five-nlp-analyse-mean-20261027`, `big-five-nlp-where-exclude-20261027`.
  Each was a rehearsal now applied to the real review.
- **Options**:
  - **Delete all five** (recommended): nothing in them is not in the real
    review or its backups.
  - **Keep**: they stay; clones share blocks, so the cost is small.
<!-- doc-counts: accept-end -->

## Answers

<!-- doc-counts: accept-start figures from applying the 2026-10-27 answers - a record, not a claim about the present -->
**2026-10-27, on the page**: every decision answered as recommended, no
comments.

- D1 Exclude: WhiSPA added to `exclude` in every analysis; `analyse` and
  `report` re-run, results identical to the clone rehearsal. Trait pools now
  openness 0.414 [0.312, 0.507] (15 studies), conscientiousness 0.395
  [0.281, 0.497] (13), extraversion 0.401 [0.324, 0.473] (14), agreeableness
  0.326 [0.239, 0.409] (13), neuroticism 0.397 [0.286, 0.498] (12); average
  unchanged at 0.354 [0.266, 0.435] (7).
- D2 Commit: `config.py` and this document committed.
- D3 Push: LitRev `main` pushed.
- D4 Delete: the five clones removed.
<!-- doc-counts: accept-end -->
