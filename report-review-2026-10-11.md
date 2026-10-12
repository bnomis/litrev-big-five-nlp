# Review: report changes, 2026-10-11

## What is being reviewed and how

The big-five-nlp report built on 2026-10-11 at 21:01 (after the evening `tabulate` re-send, the third vocabulary pass and LitRev normaliser 1.3) is compared with the build of 2026-10-08 21:19, the last one reviewed (`report-review-2026-10-08.md`; copy in `output/backup-pre-report-20261010-223024/report/`). Each change below is tied to a known cause or marked as having none. For each item, accept it or flag it with a note; for each decision, pick an option. Answer on the interactive page, <https://claude.ai/artifact/96ht4UQC7C9P7V9pe2Dcxo>; the answers are copied into the Answers section.

<!-- doc-counts: accept-start counts taken from the 2026-10-08 and 2026-10-11 builds - a record, not a claim about the present -->
## Automatic checks

| Check | Result | Detail |
|-------|--------|--------|
| report exits cleanly | pass | report-7.log has no ERROR or WARNING line; it ends with the run summary (Studies reported 171, Without CSL 0, Narrative unsupported 0, 'Not available: none') and writes report.md/.tex/.pdf and supplementary.md/.tex/.pdf. The only stderr line is a Python DeprecationWarning (swigvarlink). The log records no exit status, so 'clean' is read from the completed summary. |
| every section present before is present after | pass | report.md: no heading removed; added '### Suicide and Depression (Reddit)' (Results by dataset), '### splits' and '### results.score' (Appendix E). supplementary.md: no heading removed or added at ## / ### level; '#### results' sub-headings rose from 149 to 165 (the per-study results tables). |
| PRISMA / Study selection counts unchanged | pass | All 13 boxes of Table 1 equal: identified 715 + 2364, duplicates 92, automation 1652, other 0, screened 1335, excluded 682, sought 650, not retrieved 411, assessed 240, excluded with reasons 69, included 171, reports 171. Only the Provenance column changed (absolute to relative paths, item r4). |
| Methods unmapped counts equal the Appendix E tables | pass | datasets: Methods says 97 unmapped, 97 kept; Table 50 has 97 rows, all 'kept as written'. splits: Methods says 173 unmapped, 173 kept; Table 52 has 173 rows, all 'kept as written'. Scale: Methods says 2914 rows in 51 studies converted; Table 53 'converted' = 2914, and tables.json has 2914 bounded proportion rows in 51 papers. Table 53's outcomes (4722 + 0 + 0 + 5135 + 2914) sum to 12771 = tables.json rows_kept. Vocabulary digests in the report (fc8aa101..., 6beaf248...) match the committed vocabularies/datasets.json and splits.json. |
| number of included studies unchanged (171) | pass | PRISMA 'Studies included' 171 in both; supplementary has 171 study cards in both, in the same order with the same references; report log 'Studies reported 171'. |
| every study with an extracted results table appears | pass | tables.json: 171 papers, all status 'extracted', 165 with rows, 6 with zero rows (Gjurkovic 2025, Liu 2020, Kumar & Chakraborty 2024, Wang et al. 2018, Rybinski 2026, Iyer 2019). 165 cards carry a results table (149 before). Each card's row count equals its paper's tables.json row count (mapped through the identity register); total 12771 card rows = 12771 tables.json rows. |
| no table or chart cell reads like an error | look | No Traceback, Exception, 'None', 'nan', Jinja or 'undefined' cell in either document. But literal JSON escapes from LLM output are printed as text: 12 '\uXXXX' sequences in report.md (10 before), 204 in supplementary.md (64 before), e.g. Appendix E Table 52 'word count \u2265100 filter' and metric_name 'R (square-root of R\u00b2)'. Also 3 card rows have an empty trait (Karanatsiou et al. 2020) and every card row's score is headed 'score (percent)' even for rmse/pearson_r (items r19, r24, r25). |
| figures and charts referenced exist in output/report/assets | pass | report.md references one image, assets/prisma.svg, which exists; supplementary.md references none. No chart is drawn: the builtin templates make no chart() call, so the new LitRev chart support does not show in this build. |
| converted scores in range | pass | Of 8049 rows with a bounded metric (accuracy, f1, f1_macro, f1_weighted, precision, recall, auc): none has scale empty; no proportion row exceeds 1 (so nothing converts above 100); no percent row is at or below 1; none is negative. The 34 negative r2 rows are out of scope and unconverted. 18 converted rows are below 10, all faithful to a printed 0.00-0.07 (arxiv.2202.10415, icodsa67155.2025.11157636) or a printed 8.92%. |

## Causes

- **1**: results table description and tabulate re-send of 2026-10-10 (review commits 9c51d18-d8b0e98)
- **2**: splits vocabulary and datasets entries adopted 2026-10-10 (d0a4925, 6654be0, 65ec0a8), and the appraise re-run that followed
- **3**: scale column and re-send (262edba)
- **4**: normalise.scales conversion (4dec9a2, widened in 1bd911a)
- **5**: LitRev c28a08a5: tables.json joined through the identity register
- **6**: vocabulary passes of 2026-10-11 and normaliser 1.3 kept lists (00d579c, 80fe01a, 42efdc1, 01a4f96)
- **7**: metric names and results-only rule, re-send of 2026-10-11 evening (1bd911a)
- **8**: LitRev report code changes since 2026-10-08
- **unexplained**: no known cause

## The items

### r1: Datasets normalisation sentence: 136 unmapped keys become 97, all kept as written

Where: report.md - Methods. Cause: 6. Recommendation: **accept**.

The Normalisation paragraph now reports 97 unmapped keys for the datasets vocabulary (was 136), and says all 97 were reviewed and kept as written. The vocabulary digest changed from ba93356b... to fc8aa101....

- Before: ... the datasets vocabulary (digest sha256:ba93356b...); 136 distinct keys were left unmapped.
- After: ... (digest sha256:fc8aa101...); 97 distinct keys were left unmapped, 97 of them reviewed and kept as written.

Follows from the 2026-10-11 adoption passes and the normaliser 1.3 kept list; the figure matches Table 50 row for row.

### r2: New sentence for the splits vocabulary

Where: report.md - Methods. Cause: 2. Recommendation: **accept**.

A second sentence says results.split was grouped through the splits vocabulary (digest 6beaf248...), leaving 173 keys unmapped, all 173 kept as written.

- Before: (absent)
- After: Values of the table column results.split were grouped through the splits vocabulary (...); 173 distinct keys were left unmapped, 173 of them reviewed and kept as written.

The splits vocabulary was bound on 2026-10-10 (d0a4925, 65ec0a8) and its keys kept on 2026-10-11 (cause 6); the count matches Table 52.

### r3: New sentence: bounded scores put on a percent scale

Where: report.md - Methods. Cause: 4. Recommendation: **accept**.

A third sentence says results.score is read on a percent scale for accuracy, f1, f1_macro, f1_weighted, precision, recall and auc, and 2914 rows in 51 studies printed as proportions were multiplied by 100.

- Before: (absent)
- After: ... using the column `results.scale`: 2914 rows in 51 studies printed as proportions were multiplied by 100.

Verified against tables.json: 2914 bounded rows with scale 'proportion' in 51 papers; matches Table 53.

### r4: PRISMA provenance paths are relative again

Where: report.md - Study selection. Cause: unexplained. Recommendation: **accept**.

Every count is unchanged; the Provenance column shows paths relative to the review (output/rejected.json) instead of absolute ones. The vocabulary path in Appendix E changed the same way.

- Before: | Duplicate records removed | 92 | available | /Users/simonb/src/phd/reviews/big-five-nlp/output/rejected.json |
- After: | Duplicate records removed | 92 | available | output/rejected.json |

Not a known cause, but it is display only. logs/log.log shows the path form switching between builds (absolute on 2026-10-08 19:21 and 10-10, relative from 10-11 10:22), so it looks like it follows how the run was invoked, not any code change. The previous review recorded the same switch in the other direction (its i7).

### r5: Twitter rises from 6 to 11 studies; Suicide and Depression (Reddit) becomes a row

Where: report.md - Distribution of study features (Datasets). Cause: 6. Recommendation: **accept**.

Twitter goes from 6 studies (3.5%) to 11 (6.4%). A new row 'Suicide and Depression (Reddit)' has 2 studies (1.2%). The singleton tail falls from 126 values in 82 studies (48.0%) to 119 values in 76 studies (44.4%). No other row changed.

- Before: | Twitter | 6 | 3.5% | ... | 126 further values, each in fewer than 2 studies | 82 | 48.0% |
- After: | Twitter | 11 | 6.4% | ... | Suicide and Depression (Reddit) | 2 | 1.2% | 119 further values ... | 76 | 44.4% |

80fe01a added study-own Twitter collections to the Twitter label, and 00d579c adopted the alias that gives the Reddit label its second study.

### r6: Twitter group grows from 6 to 11 studies; singleton group shrinks from 53 to 50

Where: report.md - Results by dataset. Cause: 6. Recommendation: **accept**.

Twitter gains Fadhilla & Maharani 2025, Kafeza et al. 2014 and Sumner et al. 2012 (moved out of 'Values used by fewer than 2 studies') and Christian et al. 2021 and Rieman et al. 2017 (still also listed under myPersonality and Facebook). Twitter moves up the order, from Table 25 to Table 21.

- Before: Table 25. Results for Twitter - 6 rows; singleton table 53 rows
- After: Table 21. Results for Twitter - 11 rows; singleton table 50 rows

Same vocabulary change as r5; the counts agree with the Distribution table.

### r7: New group 'Suicide and Depression (Reddit)' shows two First Impressions results, both cited as (Amin et al. 2023)

Where: report.md - Results by dataset. Cause: 6. Recommendation: **look**.

A new Table 38 holds 2 rows. They are two different papers that share the citation label (Amin et al. 2023); the review has three Amin et al. 2023 papers. Both rows' headline text is about the First Impressions dataset, not Reddit, because the group lists a study's whole headline result under every dataset it names.

- Before: (absent)
- After: | (Amin et al. 2023) | On the First Impressions personality dataset, the best-performing system ... | (Amin et al. 2023) | On the First Impressions personality dataset, RoBERTa achieved ...

The group is correct under the rules, but a reader sees a 'Reddit' table with two identical-looking citations and no Reddit result. Two things are worth a look: the identical labels (Harvard 2023a/2023b disambiguation is missing; this problem was there before) and whether a 2-study group made only of sibling papers should count as a group. Checked 2026-10-11: the label maps only one name, "Suicide and depression dataset (Reddit, ...)", which both papers list among their datasets; the group shows each paper's headline result, which is on First Impressions. The grouping is right. What reads wrong is two different papers cited identically as (Amin et al. 2023), with no 2023a/2023b.

### r8: Tables renumbered from Table 38 onwards

Where: report.md - all numbered tables. Cause: 6. Recommendation: **accept**.

Inserting the Reddit group moves every later table up by one: WASSA 2022 38 to 39, RoB judgements 42 to 43, Appendix B 47 to 48, Appendix E labels 48 to 49. Appendix E gains Tables 50 to 53. report.md has 54 numbered tables and figures (50 before).

- Before: Table 42. Risk-of-bias judgements by study and domain
- After: Table 43. Risk-of-bias judgements by study and domain

Mechanical; any prose that cites a table by number will need updating.

### r9: 12 studies' per-study risk-of-bias judgements changed

Where: report.md - Risk of bias in included studies (Tables 43-45). Cause: 2. Recommendation: **look**.

12 of 171 rows of the judgement table differ. Predictors: low 95 to 97, some_concerns 35 to 33. Analysis: low 33 to 29, some_concerns 59 to 62, high 78 to 79. Overall: high 152 to 151, some_concerns 15 to 16 (Vegt et al. 2020 high to some_concerns). Examples: Wang et al. 2023 some_concerns/some_concerns to low/high; Celli & Poesio 2014 some_concerns/some_concerns to high/high.

- Before: | (Wang et al. 2023) | some_concerns | some_concerns | high |
- After: | (Wang et al. 2023) | low | high | high |

An appraise re-run (2026-10-10 20:26 UTC, after the datasets vocabulary adoption) re-appraised 25 papers 'after a unit change' (appraisals.json stats: changed 25). This is not in the list of known causes. Only Participants and Outcome are per-unit domains, yet Predictors and Analysis also moved: that is the LLM judging the same paper differently on a re-send, not an effect of the units. Spot-check the 12 rows before quoting the figures.

### r10: Per-unit tables: 279 to 288 units, unit names now vocabulary labels

Where: report.md - Risk of bias (Tables 46-47) and supplementary per-unit evidence. Cause: 2. Recommendation: **accept**.

Both per-unit tables grow from 279 to 288 rows. Units are renamed to vocabulary labels on 110 cards (e.g. MyPersonality to myPersonality 16 times, 'not extracted' to Essays 12 times, Essays dataset to Essays 8 times). Participants: high 159 to 158, no_information 46 to 53, low 23 to 25. Outcome: high 157 to 167, some_concerns 40 to 35, low 71 to 74.

- Before: | MyPersonality | Participants | high |
- After: | myPersonality | Participants | high |

The appraisal now records the datasets vocabulary and carries judgements forward under renamed units; the judgement shifts come from the 25 re-appraised papers in r9.

### r11: Datasets labels table: 63 labels to 71

Where: report.md - Appendix E (Table 49). Cause: 6. Recommendation: **accept**.

71 labels occurred (63 before), with the new aliases (for example Twitter now lists 'Twitter county-level corpus 2012-2014'). The vocabulary path is relative. As before, its Studies column counts the extract field plus results.dataset, so Twitter shows 13 and Facebook 11 here against 11 and 7 in the Distribution table; there were 7 such mismatches before and 3 now.

- Before: Table 48 ... | Twitter | ... | 10 |
- After: Table 49 ... | Twitter | ... | 13 |

Follows from the vocabulary adoptions; the field-versus-column difference is by design and was there before.

### r12: Unmapped datasets keys: 136 to 97 rows, new Decision column

Where: report.md - Appendix E (Table 50). Cause: 6. Recommendation: **accept**.

The unmapped-keys table drops from 136 to 97 rows and gains a Decision column reading 'kept as written' on every row.

- Before: | Unmapped key | Studies |
- After: | Unmapped key | Studies | Decision | ... | X | 1 | kept as written |

LitRev 78c6aeff (kept values shown as decided) and review commit 42efdc1.

### r13: New splits section: 50 labels and 173 kept keys

Where: report.md - Appendix E (Tables 51-52). Cause: 2. Recommendation: **look**.

New Table 51 lists 50 split labels and Table 52 lists 173 kept keys. Labels include languages (English, Italian, Spanish) and 'development set' (3 studies, 14 rows). Two kept keys print literal escapes: 'word count \u2265100 filter' and 'word count \u226575 filter'. Across the table 3224 of 12771 rows (25%) carry a split, with 224 distinct raw values.

- Before: (absent)
- After: | development set | none | 3 | ... | word count \u2265100 filter | 1 | kept as written |

The structure is expected. But the escapes should render as the characters >= (U+2265), and dev-set rows conflict with 'ignore development results when test results are given' unless those papers report only dev results. Liu et al. 2017 also puts a split on all 177 of its rows, leaving no main condition empty.

### r14: New results.score section: outcome of the scale binding

Where: report.md - Appendix E (Table 53). Cause: 4. Recommendation: **accept**.

New Table 53: out_of_scope 4722, not_numeric 0, not_recorded 0, already 5135, converted 2914 (total 12771 rows).

- Before: (absent)
- After: | converted | 2914 |

The figures reconcile with tables.json (8049 bounded rows = 5135 + 2914).

### r15: 16 more studies now show their results rows: 149 to 165 cards, 7194 to 12771 rows

Where: supplementary.md - Included studies (results tables). Cause: 5. Recommendation: **accept**.

14 studies whose rows were in tables.json under another identifier now join through the identity register, e.g. Li et al. 2022 (doi:10.48550/arxiv.2101.02346, rows under doi:10.1016/j.neucom.2022.04.049, 95 rows) and Liu et al. 2017 (csl:acl_anthology:E17-1071, rows under doi:10.18653/v1/e17-1071, 177 rows). Two more, Hasan et al. 2023 and Kulkarni et al. 2017, had 0 rows in the 2026-10-08 table and now have 5 each from the re-send. The 14 joined studies carry 1117 rows today.

- Before: (Liu et al. 2017) card: no results table
- After: (Liu et al. 2017) card: results table, 177 rows

Every card's row count now equals tables.json. The 1107 rows quoted for the fix were measured before the 1bd911a re-send, which changed these papers' row counts (e.g. Hofmann et al. 2025 60 to 149); the 2 extra studies come from cause 7, not the join.

### r16: Sample card: Li et al. 2022 (Neurocomputing) newly shows 95 rows

Where: supplementary.md - card (Li et al. 2022), doi:10.48550/arxiv.2101.02346. Cause: 5. Recommendation: **look**.

95 rows on dataset 'Personality', all scale percent: accuracy, precision, recall, f1 and other at 19 rows each; 85 baseline, 10 proposed. The 19 'other' rows have metric_name 'Average', which is the paper's average column, not a metric.

- Before: (no results table)
- After: dataset: Personality; split: ; model: BERT Single; role: baseline; trait: average; metric: accuracy; ... score (percent): 60.79; scale: percent

The join is right, but 19 rows record a metric called 'Average', a mean over columns the tabulator was told not to compute or keep. Exclude or fix them before any synthesis. A second card, also cited as (Li et al. 2022) (B. Li, PER dataset), has 7 pearson_r rows, 6 of them on 'development set'.

### r17: Sample card: Liu et al. 2017 newly shows 177 rmse rows

Where: supplementary.md - card (Liu et al. 2017), csl:acl_anthology:E17-1071. Cause: 5. Recommendation: **look**.

177 rows, all rmse, dataset 'PAN 2015', every row with a split (for example 'English, tweet-level' 30, 'English, 10-fold cross-validation' 15, 'English' 5); 90 baseline, 44 proposed, 43 prior_work. 84 rows' evidence quote is 'The RMSE user results are presented in Table 1', which does not contain the number.

- Before: (no results table)
- After: dataset: PAN 2015; split: English; model: Average Baseline; role: baseline; trait: E; metric: rmse; metric_name: ; score (percent): 0.166; scale: | Table 1 | > The RMSE user results are presented in Table 1

The rows join correctly, but the score is headed 'score (percent)' on an rmse value (r18), and half the evidence quotes cannot confirm the number they support.

### r18: Row format gains split, metric_name, scale and a 'score (percent)' heading on every row

Where: supplementary.md - every card results row. Cause: 4. Recommendation: **look**.

Each row now reads dataset; split; model; role; trait; metric; metric_name; score (percent); scale. All 12771 rows use the heading 'score (percent)', including the 4722 out-of-scope rows (rmse, mae, mse, pearson_r, spearman, r2, other), whose values are not percentages.

- Before: dataset: FACEBOOK; model: Majumder et al. (2017); role: prior_work; trait: O; metric: accuracy; score: 62.68
- After: dataset: FACEBOOK; split: ; model: Majumder et al. (2017); role: prior_work; trait: O; metric: accuracy; metric_name: ; score (percent): 62.68; scale: percent

The new columns come from 530af32 and 1bd911a. The 'score (percent)' heading on, for example, an rmse of 0.166 or a Pearson r of 0.22 tells a reader they are percentages. That is a LitRev report defect (the heading should apply only to rows the scale binding covers); see decision d4. Confirmed: an rmse row reads "metric: rmse; ... score (percent): 0.87". The heading comes from the binding and is applied to the whole column, though only rows inside its where= are converted (decision d4).

### r19: Sample converted card: Yeo et al. 2025, 216 F1 rows shown on a percent scale

Where: supplementary.md - card (Yeo et al. 2025). Cause: 4. Recommendation: **accept**.

All 216 rows (f1, 168 baseline / 48 proposed, the same as before) were proportions and now show the percent value with the printed value. Model names were shortened to one name per system (BERT (Fine-tuning) to BERT).

- Before: dataset: Essays; model: BERT (Fine-tuning); role: baseline; trait: O; metric: f1; score: 0.59
- After: dataset: Essays; split: ; model: BERT; role: baseline; trait: O; metric: f1; metric_name: ; score (percent): 59.0 (printed 0.59); scale: proportion

The conversion and the '(printed x)' note behave as specified (4dec9a2, LitRev bf6d1239). The model rename is cause 1 (080798b). Across all cards 2914 rows carry '(printed ...)', which equals the converted count.

### r20: Rows re-extracted: role mix shifts sharply toward baseline; 18 papers have no proposed row

Where: supplementary.md - results rows (all cards). Cause: 1. Recommendation: **look**.

On the 149 cards that had results before, rows go from 7194 to 11644 (78 cards grew, 10 shrank, 61 unchanged). Across tables.json, baseline rows rise from 2993 to 8405, proposed fall from 2733 to 2257, prior_work 2186 to 2099, and empty role 133 to 10. Largest changes: Zhang et al. 2025 36 to 360 (all now baseline, splits 'Round 1' ... 'Rounds 1-5'), Sarkar et al. 2014 20 to 270, Sitaraman 2014 39 to 269, Calefato & Lanubile 2021 132 to 78 (all prior_work become baseline). Papers with no 'proposed' row rise from 8 to 18.

- Before: Zhang et al. 2025: 36 rows - proposed 6, prior_work 30
- After: Zhang et al. 2025: 360 rows - baseline 360

More rows is expected: variant and modality rows were pinned in (9c51d18), and 1bd911a added metrics and re-sent all papers (cause 7). But some role flips cannot all be right. A paper that proposes a system yet has only baseline rows (Zhang et al. 2025 before had proposed rows) drops out of any 'proposed systems' comparison. Several of the 18 are LLM-evaluation studies where baseline-only is correct; check the rest.

### r21: New metrics and metric_name: 'other' is now named

Where: supplementary.md - results rows (all cards). Cause: 7. Recommendation: **look**.

New enum values: precision 582 rows / 22 papers, recall 610 / 23, r2 351 / 9, mse 316 / 9, spearman 84 / 3. 'other' falls from 1161 to 1107 rows (31 papers); every one now has a metric_name, and no non-other row has one. There are 45 distinct metric_name values, with variants of one metric: 'Balanced Accuracy' 173 / 'Balanced Accuracy (BA)' 55, 'Zero-one loss' 10 / 'Zero-One Loss' 6, 'disattenuated Pearson correlation (r_dis)' 56 / 'Disattenuated Pearson R' 20, 'weighted precision' 45 / 'Precision (weighted average)' 6. 'Average' (19 rows) is not a metric.

- Before: metric: other; score: ... (no name)
- After: metric: other; metric_name: Balanced Accuracy; ...

The change does what 1bd911a intended, but metric_name is free text with variant spellings, so it cannot yet be grouped. See decisions d1 and d2.

### r22: Bounded metrics filed under 'other' stay on mixed scales

Where: supplementary.md - results rows (scale on out-of-scope metrics). Cause: 4. Recommendation: **look**.

790 'other' rows carry a scale (548 proportion, 242 percent) but are not converted, so for example 'Balanced Accuracy' appears as proportions (125 rows) and percentages (48 rows) across 4 papers, from 0.5156 to 64.6. One paper (doi:10.1145/2659522.2659526) prints r2 as percent (30 rows, e.g. 20.0) beside other papers' r2 proportions. 170 pearson_r rows and 20 mae rows carry 'proportion', which is ignored.

- Before: (no scale column)
- After: model: Zero-shot Cross-Lingual (TOGA); ... metric: other; metric_name: Balanced Accuracy; score (percent): 0.5316; scale: proportion

This is what the config intends ('other' is left out of normalise.scales), but any synthesis of 'other' or r2 would mix scales. See decision d3.

### r23: 3 rows with an empty trait

Where: supplementary.md - card (Karanatsiou et al. 2020). Cause: 7. Recommendation: **look**.

Three rmse rows from 'Table 4. Single trait prediction' have no trait (and no dataset), although the column description says trait is never empty.

- Before: (no results table: the card was joined by cause 5)
- After: dataset: ; split: ; model: Independent Model; role: baseline; trait: ; metric: rmse; ... score (percent): 0.181

A row with no trait cannot be placed in any per-trait comparison; it slipped through the enum's null option. Check the paper's Table 4, or drop these rows.

### r24: Literal \u escapes in printed text grew from 64 to 204 (supplementary)

Where: supplementary.md and report.md - text cells. Cause: 7. Recommendation: **look**.

LLM output with JSON-escaped characters is printed verbatim: supplementary.md has 204 '\uXXXX' sequences (64 before), report.md 12 (10 before). Examples: metric_name 'R (square-root of R\u00b2)', quotes with 'Pearson\u2019s r', split 'word count \u2265100 filter'.

- Before: 64 occurrences
- After: 204 occurrences

The problem was already there; the growth comes from the new rows, metric_name and splits. They render as backslash text in the PDF too. Decision d5. Confirmed in tables.json: 58 values are stored with a literal backslash-u sequence (e.g. metric_name "R (square-root of R\u00b2)"), so they arrive from tabulate as written and the report prints them verbatim (decision d5).

### r25: Rows with no dataset rise from 432 to 1377

Where: supplementary.md - results rows. Cause: 1. Recommendation: **accept**.

Rows with an empty dataset go from 432 (28 papers) to 1377 (27 papers): roughly the same papers, each with more rows (Zhang et al. 2025 216, Yan et al. 2024 198, Singh et al. 2025 165, An et al. 2016 122).

- Before: 432 rows, 28 papers
- After: 1377 rows, 27 papers

No new papers lost their dataset; the growth tracks r20's extra variant rows. These rows cannot appear in any by-dataset comparison, which matters only once results rows are synthesised.

### r26: Duplicate rows within a card fall from 15 to 5

Where: supplementary.md - results rows. Cause: 1. Recommendation: **accept**.

Identical row cells within one card: 15 in 7 cards before, 5 in 3 cards now (Santos & Paraboni 2018 3, Hussain et al. 2026 1, Tan et al. 2026 1).

- Before: 15 duplicate rows in 7 cards
- After: 5 duplicate rows in 3 cards

e9c984a ('give duplicated results once') worked as intended. The remaining few may be the same value printed for two conditions.

### r27: Unchanged

Where: supplementary.md - Synthesis (Tables S1-S11) and Appendix A (Table S12). Cause: unexplained. Recommendation: **accept**.

The per-field synthesis tables and the full-text exclusions are byte-identical between the builds; the report's Characteristics sections, References and Appendices B-D change only in table numbers.

- Before: Table S1. Datasets ...
- After: Table S1. Datasets ...

Expected: none of the known causes touches the extract fields or screening. Listed so it is clear nothing disappeared.

### Needs attention

Unexplained changes: r4, r27 (both display-only: provenance paths, and a section confirmed unchanged). Items recommended for a look: r7, r9, r13, r16, r17, r18, r20, r21, r22, r23, r24.

## Decisions

### d1: Should the results rows (12771 rows, now on one scale for bounded metrics) be synthesised in the report, and which metrics go in?

**Background:** The builtin report shows tables.json only in the per-study cards. 'Results by dataset' lists headline_results prose, and there is no by-metric or by-trait section, so the new metrics change no synthesis table or chart. LitRev gained chart() for custom templates on 2026-10-11 (1bfe881a; README 'Charts in a template'), and the README's own example is a strip chart of macro-F1 for proposed systems on the main condition. Since 1bd911a, precision (582 rows) and recall (610) sit beside accuracy (4202) and the F1 family (2620).

**What it affects:** A custom report template in the review repo; the report's Results section; which rows a reader compares. It costs no LLM call.

**Options:**

- **Keep cards only for now.** No change; numbers are compared by hand from the supplementary. Nothing to re-check until d2-d3 are settled.
- **Add a custom template with charts for accuracy and the F1 family only (proposed, split empty).** One chart per metric; precision, recall and 'other' stay in the cards. Needs r20's role flips and r23's null-trait rows checked first, since they decide which rows a 'proposed' chart shows.
- **Chart every bounded metric, precision and recall included.** More coverage, but precision/recall are usually reported beside F1 for the same system, so a chart roughly doubles its points per paper and weights papers that print more metrics.

**Recommendation:** Add a custom template restricted to accuracy and the F1 family, after checking r20 and r23.

### d2: Should results.metric_name get a vocabulary?

**Background:** Since 1bd911a (2026-10-11), every 'other' row names its metric: 1107 rows, 45 distinct names, with spelling variants of one metric (Balanced Accuracy 173 / Balanced Accuracy (BA) 55; Zero-one loss / Zero-One Loss; two spellings of disattenuated Pearson r; weighted precision / Precision (weighted average)) and one non-metric ('Average', 19 rows, Li et al. 2022).

**What it affects:** config.py normalise.vocabularies; a normalise propose run (one LLM call over 45 names, so ask provider and cost first); a vocabulary review like the datasets/splits ones; Appendix E gains a section.

**Options:**

- **Bind a metric_names vocabulary on results.metric_name.** Variants merge under one label and Appendix E lists them, and an 'other' metric can then be named in a chart or in normalise.scales (d3). Costs one small propose call plus a review pass.
- **Leave metric_name as free text.** No work now. 'other' stays ungroupable and is left out of any synthesis.
- **Promote the frequent names to the metric enum (e.g. balanced_accuracy, uar) and re-send tabulate.** Cleanest data, but a full re-send of 171 papers costs about the last run (Batch API, roughly $16 on the 2026-10-07 estimate) and re-rolls every row (r20).

**Recommendation:** Bind a vocabulary; it is the cheap option and also settles d3.

### d3: Should bounded metrics filed under 'other' (and r2 printed as percent) be put on the percent scale?

**Background:** normalise.scales converts only accuracy, f1*, precision, recall and auc; 'other' was left out on purpose because it holds unbounded metrics too. 790 'other' rows carry a scale (548 proportion, 242 percent), so 'Balanced Accuracy' appears as both proportions (125 rows) and percentages (48 rows). One paper prints r2 as percent (30 rows).

**What it affects:** config.py normalise.scales; Table 53 and the Methods scale sentence; any chart of 'other' metrics.

**Options:**

- **Leave as is and exclude 'other' and r2 from any synthesis.** No change; the mixed scales stay in the cards only, with '(printed x)' absent for them.
- **After d2, add a second scale binding for the bounded metric_name labels.** Balanced accuracy and similar metrics read on one scale. First check that LitRev's where= can match on metric_name (or on metric and metric_name together).

**Recommendation:** Leave as is until d2 is settled, then add the binding.

### d4: File the 'score (percent)' heading on every card row as a LitRev defect?

**Background:** LitRev bf6d1239 (2026-10-11) labels the bound column with its scale. It does so on all 12771 rows, including the 4722 out-of-scope rows, e.g. 'score (percent): 0.166' for an rmse (item r18).

**What it affects:** LitRev report card rendering; supplementary.md; the PDF.

**Options:**

- **File it in LitRev's TODO.md.** Fixed later: the heading would read 'score' on rows the binding does not cover, or show '(percent)' only on rows it covers.
- **Accept.** Readers must know from the Methods sentence that only bounded metrics are percent.

**Recommendation:** File it in LitRev's TODO.md.

### d5: File the literal \uXXXX escapes as a LitRev defect?

**Background:** LLM answers sometimes double-escape non-ASCII characters, and LitRev stores and prints them verbatim. There are 204 in supplementary.md (64 on 2026-10-08) and 12 in report.md, including Appendix E's 'word count \u2265100 filter' (item r24).

**What it affects:** tabulate/extract storage or report rendering; every document; existing artefacts (a decode at report time fixes them without re-sending).

**Options:**

- **File it in LitRev's TODO.md (decode escapes at parse or report time).** The text renders as the real characters; no LLM cost if done at report time.
- **Accept.** Backslash sequences stay in the thesis appendix and PDF.

**Recommendation:** File it in LitRev's TODO.md.

### d6: Accept the re-appraised risk-of-bias judgements for the 12 studies whose per-study domains changed?

**Background:** On 2026-10-10 an appraise run re-appraised 25 papers after the datasets vocabulary renamed their units (appraisals.json stats changed 25). Per-study domains (Predictors, Analysis) changed for 12 studies even though units do not feed them: re-send variation. Example: Wang et al. 2023 some_concerns/some_concerns to low/high (item r9).

**What it affects:** Report Tables 43-47 and the risk-of-bias summary counts; card evidence for those 12 studies.

**Options:**

- **Accept the new judgements.** Report stands as built; the record shows the earlier judgements only in backup-pre-appraise-20261010-222652.
- **Human-check the 12 changed rows against their evidence quotes.** About 12 cards to read; any override is recorded per LitRev's appraise process, and the report is re-run.

**Recommendation:** Human-check the 12 rows; they are the reported judgements and the change is not explained by the units.

<!-- doc-counts: accept-end -->

## Answers

Answered 2026-10-11 on the page, no notes.

- **Items**: all 27 accepted, including the eleven recommended for a look.
- **d1**: keep cards only for now - no custom template or chart yet.
- **d2**: bind a `metric_names` vocabulary on `results.metric_name`.
- **d3**: leave as is; `other` and `r2` stay out of any synthesis.
- **d4**: file the `score (percent)` heading in LitRev's `TODO.md`.
- **d5**: file the literal `\u` escapes in LitRev's `TODO.md`.
- **d6**: accept the re-appraised risk-of-bias judgements.

**Done for d2, 2026-10-12**: `config.py` binds `metric_names` on
`results.metric_name`. `normalise` (anthropic `claude-sonnet-5`, 1364
input and 685 output tokens; backup
`output/backup-pre-normalise-20261012-061600`) proposed six clusters, none
merging two names from one paper. Answered in the session: all six
approved (Balanced Accuracy, Cohen's kappa, Disattenuated Pearson R,
Zero-One Loss, weighted precision, weighted recall), UAR added to Balanced
Accuracy since it is the same quantity, and the other 31 names kept as
written - "Average" (Li et al. 2022) among them, a row label rather than a
metric. `vocabularies/metric_names.json` holds 6 labels, 7 aliases and 31
kept names; `normalise` now sends nothing for any vocabulary.

**Done for d4 and d5**: filed in LitRev `TODO.md` as "A study card labels
every row's score `score (percent)`, rmse included" and "Literal `\u`
escapes in model answers are stored and printed as written".
