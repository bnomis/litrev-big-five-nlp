# Big Five personality detection from natural language

A systematic literature review, run with
[LitRev](../../litrev/README.md).

**Review question.** How has the Big Five (five-factor) personality model
been predicted from human language - written text and spoken language - and
with what data, methods and results?

**What is extracted from every included paper**, and the reason the review
exists rather than a reading list:

- the datasets used,
- the accuracy, error or correlation reported,
- how the modelling was done.

Everything in `config.py` follows from those three. Its docstring carries
the scope decisions and the reasoning behind each screening criterion; this
file is how to run it.

## Setup

The API key is never written into `config.py` - LitRev rejects it there,
because a config file is expected to be committed.

```shell
export LITREV_LLM_ANTHROPIC_API_KEY=...
export LITREV_PROJECT=/Users/simonb/src/phd/reviews/big-five-nlp
```

With `LITREV_PROJECT` exported, no command below needs `--project`.

Optional, and worth setting before a long pass:

| Variable | What it buys |
|----------|--------------|
| `NCBI_API_KEY` | Raises the PubMed rate limit from 3 to 10 requests a second |
| `CROSSREF_MAILTO` | Crossref's polite pool - faster and less likely to be throttled |
| `SEMANTIC_SCHOLAR_API_KEY` | Only needed if `semantic_scholar` is added to `search.sources` |

`download.unpaywall_email` is commented out in `config.py`. The `unpaywall`
resolver needs it, and without it that resolver is the one link in the
chain that cannot run.

## The pass

Run from the LitRev checkout, since `bin/litrev.sh` lives there:

```shell
cd ../../litrev
```

| Stage | Command | Produces | Where you may need to intervene |
|-------|---------|----------|-------------------------------|
| Search | `bin/litrev.sh search` | `output/<source>.json` per source | A source that errors is reported, not silently skipped - check the log before moving on |
| Filter | `bin/litrev.sh filter` | `output/filtered.json`, `output/rejected.json` | Read `rejected.json` once. A keyword doing more work than intended shows up here and nowhere else |
| Screen | `bin/litrev.sh screen` | `output/assessments/screening.json` | The first real cost. Check a handful of `exclude` decisions against their reasons before trusting the rest |
| Download | `bin/litrev.sh download` | `output/downloads/` + manifest | Paywalled papers fail here by design. The manifest records why, per paper |
| Convert | `bin/litrev.sh convert` | `output/markdown/<slug>/paper.md` | Slow, and the first run pulls docling's models. Spot-check one converted results table |
| Assess | `bin/litrev.sh assess` | `output/assessments/eligibility.json` | Where `require_dual: True` would stop for you - see below |
| Extract | `bin/litrev.sh extract` | `output/extractions/` | The deliverable. Every field carries a verbatim supporting quote - use them |
| Store | `bin/litrev.sh store` | `output/litrev.db` | |
| Cite | `bin/litrev.sh cite` | `output/citations/references.{md,bib,json}` | |
| PRISMA | `bin/litrev.sh prisma` | `output/prisma/` | The flow diagram and its machine-readable counts |

A paper that was collected by hand rather than downloaded goes in
`output/downloads/` and is picked up by `bin/litrev.sh scan`, which
identifies it and renames it to the title-slug convention.

## Reading the extractions

The extraction fields are grouped to build three tables:

- **Datasets** - `datasets`, `dataset_is_new`, `sample_size`,
  `data_language`, `text_genre`, `modality`, `ground_truth_method`.
- **Modelling** - `task_formulation`, `features_or_representation`,
  `model_architecture`, `traits_modelled_jointly`.
- **Results** - `evaluation_metrics`, `headline_results`,
  `reports_per_trait_results`, `baseline_comparison`,
  `validation_scheme`, `code_or_data_available`.

Two of these are there to catch problems rather than to fill a column, and
both are worth reading before any results are compared:

- `ground_truth_method` separates self-report questionnaire labels from
  labels derived from a user profile or annotated by a crowd. Accuracy
  figures from these are not comparable, and papers rarely say so.
- `validation_scheme` asks whether the split is by subject or by document.
  A document-level split leaks whenever one person contributes several
  documents, which is the normal case in this field, and it inflates
  reported accuracy.

Query the database directly for anything the reference list does not
answer - see [Querying with the `sqlite3` binary](../../litrev/README.md#querying-with-the-sqlite3-binary).

## Two things this review is not yet

**It is single-reviewer.** `screen.require_dual` and `assess.require_dual`
are both `False`, so the LLM's verdict is final and every decision records
`single_reviewer`. Measured over LitRev's own demonstration corpus, a
single-reviewer pass admitted 8 papers in 42 that the adjudicated review
excludes - 19% of its own included set. That is a reasonable trade for a
first pass whose job is to show the shape of the corpus, and the wrong one
for the review that goes in the thesis. Turning it round: set
`assess.require_dual` to `True`, re-run `assess`, fill in
`output/assessments/eligibility-worklist.md`, then run
`bin/litrev.sh adjudicate`.

**Its later stages are stale, as of 2026-09-20.** A snowball round ran
against the 70 papers this review had already included, and everything up
to and including `assess` has been re-run over what it found. Nothing after
`assess` has.

What happened, in order: `snowball` followed the 70 included papers'
references and citers and found 2,364 new candidates; `filter` took
`filtered.json` from 303 to 855; `screen` judged the 605 new records and
`screened.json` grew from 112 to 355; `download` retrieved 69 of those and
`convert` turned all 69 into markdown; `assess` read the full text of the
69 and included 48 of them. `included.json` therefore holds **118** papers -
the original 70 plus 48 - and `eligibility.json` holds 167 assessments.

So `extract`, `appraise`, `store`, `cite`, `prisma` and `report` all still
describe the 70-paper review. **The 48 new papers have no extractions**, so
the synthesis tables, the PRISMA counts and the reference list are each a
record of a smaller review than the one `included.json` now names. Re-run
them in that order before reading anything under `output/report/` as
current.

Two cautions on that re-run, both learned the hard way on 2026-09-20:

- **Back up `output/assessments/` first.** `assess` rewrites
  `eligibility.json` and `included.json` from the papers its own pass
  covers, and a pass after a `convert` that skipped already-converted
  papers covers only the new ones - so it silently replaced 98 assessments
  with 69 and 70 inclusions with 48. Recovered from a backup and repaired
  by hand; see LitRev's `TODO.md`, first item.
- **A worklist from an earlier pass will stop the run.** `screen` and
  `assess` both refuse a worklist whose keys are not in the current pass,
  which any re-run over a grown record set produces. Neither worklist here
  has ever been filled in, so archiving it and letting the stage write a
  fresh one costs nothing - but check for answers before you move one.

The pre-run and post-`assess` backups are in `output/backup-*/`.
