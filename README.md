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

## What a pass costs and how long it takes

Measured 2026-09-24, on Anthropic `claude-sonnet-5` at that day's published
rates: $2/MTok input and $10/MTok output immediately, half that under batch
dispatch. The LLM figures come from the per-record token counts each stage
writes. Sources:

- `screen` and `assess`: the from-scratch re-run in `../big-five-nlp-rerun`,
  both rounds, the snowball round included.
- `extract` and `appraise`: the full refresh of this review on 2026-09-24.
  All 116 papers were sent again, because the prompt order had changed.

| Stage | Records | Dispatch | Cost | Time |
|-------|---------|----------|------|------|
| Search | 4 sources | - | free | under a minute |
| Filter | | - | free | seconds |
| Screen | 854 abstracts over both rounds | batch | $2.49 | a batch of 550 came back in about 4 minutes; the API allows up to 24 hours |
| Download | 111, then 345 after the snowball round | - | free | 5 and 19 minutes; resolver failures are slow ones |
| Convert | 94, then 70 | - | free | about 6 seconds a paper on this machine (10 and 8 minutes) |
| Assess | 162 full texts | batch | $3.96 | a batch: minutes to hours, up to 24 hours |
| Snowball | 113 seeds | - | free | a few minutes of Semantic Scholar lookups |
| Extract | 116 papers | immediate | $10.17 | 21 minutes |
| Appraise | 116 papers, `combined` | immediate | $9.02 | 21 minutes |
| Store, cite, PRISMA | | - | free | seconds each |
| Report | markdown and both PDFs | - | free | about a minute |
| **Whole pass** | | | **about $26** | **about 2 hours**, plus batch waits |

`extract` and `appraise` carry forward any record whose prompt, provider and
model are unchanged, so a re-run that changes none of those costs nothing.
Editing an extraction field or an appraisal domain re-pays that stage for
every paper. `screen` and `assess` run under batch dispatch (set in
`config.py`) at half price. `extract` and `appraise` run immediately, and
they are most of what a re-run pays for.

Two figures from before these measurements, as a warning against sizing by
eye:

- The re-run spent $36.26, because `appraise` then sent one call per study
  plus one per dataset, $19.77 of it. The `combined` shape has been the
  default since 2026-09-24.
- Estimating from characters divided by four has undercounted every stage
  so far. Size a new run from these per-record figures instead.

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

## The identity migration, 2026-09-22

The assessment artefacts held one paper twice wherever a paper's identity
had moved between search rounds. A paper found only on arXiv was keyed
`csl:arxiv:<id>`, because LitRev's arXiv source recorded no DOI; when the
snowball round found the same paper through Semantic Scholar, which does
carry arXiv's minted `10.48550/arXiv.<id>`, the key became `doi:...` and
the earlier assessment was orphaned under the old one.

What changed here, all of it reversible from
`output/backup-pre-identity-20260922-062428/`:

| | Before | After |
|---|---|---|
| `eligibility.json` rows | 167 | 160 |
| `included.json` keys | 118 | 113 |
| the same paper under two keys | 7 pairs | none |

No paper was dropped and nothing was re-judged: the run made no LLM call
at all. The seven collapsed pairs each held the same verdict on both
copies, so the collapse is bookkeeping rather than a decision. One of them
carried two different exclusion reasons - `not_language_input` was kept
and `personality_not_predicted` dropped - so the exclusion breakdown a
PRISMA diagram reports moves by one.

**`output/arxiv.json` was rewritten** to carry the DOI arXiv mints for
every submission, which the search that produced it did not record. Those
DOIs are derived from the arXiv ids already in the file rather than
fetched, and were checked against the DOIs Crossref and the ACL Anthology
independently hold for the same papers. A later `search` re-run will write
them itself, since the arXiv source now mints them; this brought the
stored record forward so `filter` could see that the two identifiers name
one paper.

`output/identity/register.json` is new and is what remembers that mapping:
one canonical key per paper, with every other identifier as an alias.
`output/assessments/eligibility-worklist-pre-identity-20260922.md.bak` is
the worklist that was archived to let `assess` run - 69 blocks, none of
them answered.

## Restoring the `semantic_scholar` resolver, 2026-09-22

`download.resolvers` was `['direct', 'arxiv', 'doi']`. `semantic_scholar`
had been dropped from LitRev's default chain alongside `unpaywall`, but
only `unpaywall`'s absence was ever explained - and on this corpus the
omission mattered, because most records here came from Semantic Scholar
and carried its landing page as their URL, which `direct` cannot retrieve.

Restoring it and re-running `download`:

| | Before | After |
|---|---|---|
| `all_resolvers_failed` | 173 | 89 |
| `failed` | 11 | 79 |
| PDFs on disk | 167 | 183 |

**16 papers were retrieved that the chain had given up on**, every one of
them won by `semantic_scholar`, and `convert` turned all 16 into markdown
with no OCR, no partial and no failure. The manifest kept all 355 rows and
lost no keys.

Read the middle row before celebrating the first. Of the 84 records that
left `all_resolvers_failed`, only 14 became PDFs; 70 moved to `failed`,
meaning a URL was found and the fetch of it was refused - mostly 403 and
418 from publisher hosts that block automated fetching, and 27 of 74
resolving to a `doi.org` link the `doi` resolver behind it already covers.
Semantic Scholar's `openAccessPdf` reports where an open-access copy is
*claimed* to be, not a file it guarantees you can fetch.

The stage took 26m against 5m27s without the resolver, because it shares
one rate limiter with the searcher's Semantic Scholar source and this
review sets no `search.semantic_scholar.api_key`.

**The downstream stages have not been re-run.** `assess`, `extract`,
`appraise` and everything after them still describe the corpus as it was
before these 16 papers arrived, and catching them up costs LLM calls.

## The quotes migration, 2026-09-22

LitRev's assessor decisions changed from one supporting quote (`quote`) to a
list of them (`quotes`). The new code refuses to read the old shape rather
than treating it as "no quote", so the assessment artefacts were migrated
with `bin/migrate-quotes.sh`:

| File | Decisions rewritten |
|---|---|
| `output/assessments/screening.json` | 855 |
| `output/assessments/eligibility.json` | 160 |

Each old `quote` became a one-item `quotes` list; the 3 screening decisions
with no quote became an empty list. Every quote was checked word for word
against the backup, and no other field in any decision changed. No LLM call
was made and no verdict moved.

`output/appraisals/appraisals.json` and `output/extractions/extractions.json`
also contain `quote` fields. Those belong to `appraise` and `extract`, whose
format did not change, and they were deliberately left alone.

The pre-migration files are in
`output/backup-pre-quotes-20260922-203605/assessments/`.
