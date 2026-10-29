# Review: a report.md that can become the manuscript

Interactive page: <https://claude.ai/artifact/LLDqXWDDQHnqrvaY1pfVfE>

## What is being reviewed and how

On 2026-10-28 the operator noted that `output/report/report.pdf` runs to
hundreds of pages, which is fine as a record but cannot be the basis of a
publishable paper. LitRev's paper spec (`agents/specs/report/paper.md`,
2026-09-14) meant `report.md` to be the manuscript and `supplementary.md` the
material a journal hosts but does not print. At 171 included studies the
per-study sections overwhelm it. A clone was used to measure a
manuscript-shaped split. Four decisions follow; answer each on the page,
where every answer saves as it is made.

<!-- doc-counts: accept-start figures measured on 2026-10-28 - a record, not a claim about the present -->
## Automatic checks

- pass: the measurement ran on the APFS clone
  `big-five-nlp-manuscript-20261028`, with only its two templates changed;
  `report` exited 0 with no warning or error.
- pass: every section still appears in one of the two documents; only the
  routing changed.
- look: the manuscript-shaped `report.md` cross-references no supplementary
  table or figure, so a reader is not pointed at the per-study material.
- look: Methods says nothing about risk of bias. The sentence naming the
  appraising model, its prompt hash and the worst-domain rule sits at the top
  of the `riskofbias` section, so it moves with that section.

## The items

Where today's main document spends its length (words in `report.md`):

| Section | Words | Kind |
|---|---|---|
| Appendix B: records excluded at title/abstract | 49,421 | one row per excluded record |
| Characteristics of included studies | 24,858 | one row per study, three tables |
| Results by dataset | 16,076 | one row per study result, per dataset |
| Risk of bias in included studies | 8,858 | one row per study, five tables |
| References | 5,744 | 171 included studies |
| Appendix E: value normalisation | 5,591 | vocabulary tables |
| Meta-analysis | 2,607 | six analyses |
| Distribution of study features | 1,769 | eleven frequency tables |
| Appendix D: PRISMA 2020 checklist | 1,705 | |
| everything else | about 1,300 | |

`report.pdf` is 403 pages and `supplementary.pdf` 2,754.

Measured split (main keeps abstract, introduction, methods, study selection,
agreement, evidence base, study features with the five summary charts,
meta-analysis, discussion, limitations, conclusions, declarations and
references; everything else goes to supplementary): `report.md` 11,452 words,
of which references are 5,744; `report.pdf` 52 pages; 26 tables and 15
figures. `supplementary.pdf` 3,107 pages.

Not decisions, for the record:

- Abstract, introduction, discussion, limitations and conclusions are empty
  placeholders. By the paper spec's rule they are the author's prose, kept in
  `narrative/`, and LitRev never writes them.
- Two forest-plot rows are labelled by DOI, not author and year:
  `doi:10.1093/pnasnexus/pgae231` and `doi:10.1609/icwsm.v11i1.14963`. Cause
  not yet checked.
- `report.html` holds both documents whatever the split, so the interactive
  page keeps everything.

## Decisions

### D1. Make report.md the manuscript?

- **Decided**: whether the per-study sections and the appendices move from
  `report.md` to `supplementary.md`.
- **Background**: the review's split was
  `supplementary_sections: ['synthesis', 'studies', 'exclusions']` by
  2026-09-16. Sections LitRev added later (appendices B to E) stayed in the
  main document because that list did not name them, not by a recorded
  choice. On 2026-10-13 the split moved into `templates/report.md.j2`,
  keeping the same result.
- **Affects**: both templates; `report.pdf` from 403 to 52 pages;
  supplementary from 2,754 to 3,107. Nothing is dropped.
- **Options**:
  - **Move** (recommended): `report.md.j2` keeps the sections listed above;
    characteristics, results by dataset, per-study risk of bias, synthesis
    and appendices B to E go to `supplementary.md.j2`. The risk-of-bias
    method sentence goes with them, so the author's Methods prose has to
    state it.
  - **Keep the current split**: the 403-page document stays, and the
    manuscript is written by hand outside LitRev.

### D2. How should the meta-analysis appear in the manuscript?

- **Decided**: how the six pooled analyses (average and each trait) are
  shown in `report.md`.
- **Background**: each analysis renders an overall table, a by-dataset table,
  a forest plot and, for four of them, a by-dataset forest plot: 12 tables
  and 9 figures, more than most journals allow in a whole paper. A
  `section('metaanalysis', analyses=[...])` template call already chooses
  which analyses a document shows. LitRev has no table summarising every
  analysis in one, one row per analysis.
- **Affects**: LitRev (a spec amendment and code) for the first option; the
  templates only for the others.
- **Options**:
  - **Spec a summary table** (recommended): amend LitRev's report spec for one
    table with a row per analysis (estimate, CI, prediction interval,
    studies, rows, heterogeneity). The manuscript shows that table and the
    average forest plot, and each analysis's detail goes to supplementary.
    The spec comes to you for approval first; the templates use the next
    option until it lands.
  - **Templates only**: the manuscript shows the average analysis in full;
    the five trait analyses go to supplementary. No LitRev change, but the
    trait estimates then appear only in the supplement.
  - **Keep all six**: the 12 tables and 9 figures stay in the manuscript.

### D3. The descriptive tables

- **Decided**: where the 3 evidence-base tables (year, publication type,
  source) and the 11 study-feature frequency tables go.
- **Background**: the five charts (modality, datasets, accuracy by trait,
  two risk-of-bias summaries) already carry the main message. A
  `section('frequencies', fields=[...])` call can keep only chosen fields;
  name them in the comment box if you want some kept.
- **Affects**: the templates; 14 of the manuscript's 26 tables.
- **Options**:
  - **Charts in the manuscript, tables to supplementary** (recommended).
  - **Keep the tables in the manuscript**.

### D4. Should LitRev's default split change?

- **Decided**: whether to file the finding in LitRev's `TODO.md`.
- **Background**: LitRev's default `report.supplementary_sections` keeps
  characteristics, results by dataset and per-study risk of bias in the
  main document. That suits a review of 20 or 30 studies; at 171 the paper
  spec's aim, a `report.md` that reads as a submittable review, is not met
  by default.
- **Affects**: LitRev's `TODO.md` now; later its defaults and guide
  chapter 8.
- **Options**:
  - **File it** (recommended): a TODO item for a manuscript-shaped default
    (or a guide recipe), with these measurements.
  - **Leave LitRev as it is**: only this review is configured.
<!-- doc-counts: accept-end -->

## Answers

<!-- doc-counts: accept-start figures from applying the 2026-10-28 answers - a record, not a claim about the present -->
**2026-10-28, on the page**: every decision answered as recommended, no
comments.

- D1 Move: `templates/report.md.j2` and `templates/supplementary.md.j2`
  rewritten, rehearsed on the clone, then `report` run on the real review
  (backup `output/backup-pre-manuscript-20261028-report`). The real outputs
  are identical to the rehearsal, and the two documents together carry the
  same section and analysis headings as before. `report.pdf` is now 26
  pages: 7,269 words, about 5,700 of them references, 3 tables and 7
  figures. `supplementary.pdf` is 3,134 pages.
- D2 Spec a summary table: the manuscript shows only `r_average` and the
  five trait analyses are in the supplement until the LitRev spec amendment
  lands.
- D3 Charts in the manuscript: the evidence-base and frequency tables are in
  the supplement; the five charts stay in the manuscript under template
  headings.
- D4 File it: filed in LitRev's `TODO.md`.

**2026-10-29, D2 applied**: LitRev's summary table (report HTML 1.1) landed
at LitRev `5f04ea7f`. `templates/report.md.j2` now calls
`section('metaanalysis', summary=True)`, then `r_average` in full with
`heading=False`. Rehearsed on the clone, then run for real (backup
`output/backup-pre-summary-20261029-report`); the real outputs equal the
rehearsal's. The manuscript gains one table with every analysis (average and
each trait); `supplementary.md` is unchanged. `report.pdf` is 27 pages.
<!-- doc-counts: accept-end -->
