# Review: report changes, 2026-10-08

## What is being reviewed and how

The big-five-nlp report was regenerated on 2026-10-08 after the `tabulate` re-run (all 171 papers extracted) and the adoption of the first `datasets` vocabulary. This review compares it with the 2026-10-05 build, kept in `output/backup-pre-report-20261008-192013/report/`. Approve or flag each change, and choose an option for each decision, on <https://claude.ai/artifact/5sREbNQkeZREUw8zpW7fkH>; the answers are copied into the Answers section below.

## Automatic checks

| Check | Result |
|-------|--------|
| `report` exits cleanly | pass: exit 0, "Not available: none", "Narrative unsupported 0" |
| Every report section present in both builds is still present | pass: no section removed; one added (Appendix E) |
| PRISMA counts unchanged | pass: every Study selection count matches; only the source column changed |
| Unmapped-key count matches `normalise` | fail: the report states 92, `normalise` finds 136 (see item i4) |

## The items

### i1: Dataset frequencies now count corpora, not spellings

Where: report.md - Distribution of study features.

The datasets vocabulary merges spellings: Essays rises from 28 to 48 studies, myPersonality from 5 (plus 9 as MyPersonality) to 21, Kaggle (PersonalityCafe) from 2 to 15. Values used by one study fall from 208 to 126.

- Before: Essays 28 | MyPersonality 9 | myPersonality 5 | Essays dataset 4 | PANDORA 4 | ... | 208 further values (127 studies)
- After: Essays 48 | myPersonality 21 | Kaggle (PersonalityCafe) 15 | ChaLearn First Impressions 8 | PAN-AP-2015 8 | ... | 126 further values (82 studies)

### i2: Results regrouped under the vocabulary's labels

Where: report.md - Results by dataset.

The same vocabulary keys the grouping. The 23 named groups are now distinct corpora; before, Essays, Essays dataset, Essays Dataset and Stream-of-consciousness essays were four groups. A study naming several datasets still appears under each, so (Vu et al. 2018) shows its FACEBOOK result under Essays: its datasets field lists Twitter, Facebook, YouTube and Essays.

- Before: 24 groups, including Essays / Essays dataset / Essays Dataset / Stream-of-consciousness essays, MyPersonality / myPersonality, Kaggle / Kaggle MBTI dataset / Kaggle (PersonalityCafe)
- After: 24 groups: 23 labels from the vocabulary plus 'Values used by fewer than 2 studies'

### i3: New appendix listing each label and the aliases it merged

Where: report.md - Appendix E: value normalisation (new).

Added by the report's normalisation section (LitRev commit 70767f0c) now that a vocabulary is bound. Table 48 lists every label, the aliases that occurred, and its study count.

- Before: (absent)
- After: Appendix E, Table 48: Labels applied by the datasets vocabulary

### i5: Each study card gains its tabulated results rows

Where: supplementary.md - Included studies.

LitRev commits 2d569b58 and bb8bb221 add table rows to the per-study cards, and today's tabulate re-run completed the 12 papers that had failed. All 171 studies, 8045 rows; supplementary.md grows from 6.5 MB to 10.4 MB.

- Before: Cards with extracted fields only
- After: Each card ends with a 'results' table: row, location, evidence quote

### i6: Supplementary tables numbered S1, S2, ...

Where: supplementary.md - Synthesis, Appendix A.

LitRev commit a500088d numbers supplementary documents with an S prefix, so supplementary Table 1 no longer shares a number with the report's Table 1.

- Before: Table 1. Datasets ... Table 12. Studies excluded at full text
- After: Table S1. Datasets ... Table S12. Studies excluded at full text

### Needing attention

#### i4: Methods sentence reports 92 unmapped keys; normalise counts 136

Where: report.md - Methods.

Checked 2026-10-08: the report's count reads only the extract field `datasets` (92 unmapped), while normalise also reads the results table's `dataset` column (136). The sentence says the vocabulary was applied to `datasets, results.dataset`, so the 44 names found only in table rows are left out of the count it states.

- Before: (absent)
- After: Values of the extract fields datasets, results.dataset were grouped through the datasets vocabulary (digest sha256:ba93356b...); 92 distinct keys were left unmapped.

#### i7: PRISMA source paths are now relative to the review

Where: report.md - Study selection.

No explanation found: the counts are unchanged and only the source column changed, from absolute paths to paths relative to the review directory. The LitRev commit that made this change was not identified.

- Before: /Users/simonb/src/phd/reviews/big-five-nlp/output/rejected.json
- After: output/rejected.json

## Decisions

### d1: The unmapped count leaves out table-column names (item i4)

- **File it in LitRev's TODO.md** (recommended): A report defect: the Methods sentence and Appendix E should count every bound field and column, as normalise does. Fix later.
- **Accept as is**: The count is of extract-field keys only; leave it.

## Answers

Answered 2026-10-08 on the review page; read back from its store.

- **i1-i7:** all approved, with no comments - including i4 and i7, the two needing attention.
- **d1:** file it in LitRev's `TODO.md` - the report's unmapped count, and Appendix E, read only extract fields, not the table columns a vocabulary is bound to.
