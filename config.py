"""Big Five personality detection from natural language: review configuration.

The review question: how has the Big Five (five-factor) personality model
been predicted from human language, written and spoken, and with what data,
methods and results?

Three things are extracted from every included paper, and they are the
reason this review exists rather than a reading list:

- which datasets were used,
- what accuracy, error or correlation was reported,
- how the modelling was done.

Everything below follows from those three. The `extract.fields` block is the
deliverable; the earlier stages exist to decide which papers reach it.

## Scope decisions, and why

`search.date_from` is 1999-01-01 rather than the more usual "last ten
years". Pennebaker and King's 1999 study is where the standard benchmark of
this field - the stream-of-consciousness essays corpus, labelled by
self-report Big Five scores - originates, and papers published in 2024 still
report accuracy on it. A review that started in 2015 would describe results
on a dataset whose construction it never saw.

`search.sources` leads with `acl_anthology` because that is where this
literature actually is: *ACL, EMNLP, COLING, and the WASSA and CLPsych
workshops between them hold most of the computational personality
recognition work, and none of it is indexed well by the general databases.
`arxiv` covers the LLM-era preprints that have not reached a venue yet.
`crossref` reaches the psychology side - Journal of Research in Personality,
JPSP, PLOS ONE - where the trait-validity arguments live, and `pubmed`
catches the clinical and psychiatric crossover. Papers on personality
prediction from language appear in all four and are the same literature;
`filter` deduplicates across them on title similarity.

`semantic_scholar` and `ieee` are left out rather than forgotten. Semantic
Scholar works without a key but is rate limited hard enough to slow a
200-per-source pass considerably; IEEE needs `IEEE_API_KEY` and covers
affective-computing venues (ACII, T-AFFC) that matter for the *spoken*
half of the question. Add either when the corpus shows a gap - both are one
line, see the commented entries below.

`search.max_results` is per source, not per run, so 200 here means up to 800
raw records before deduplication.

## Query grouping across sources

The query below is a three-clause AND of OR-groups. `arxiv` and `pubmed`
keep the parentheses; `crossref` is a relevance-ranked free-text search
where grouping does not apply.

`acl_anthology` is the one that had to be fixed before this review could
trust it. That source has no search endpoint - it re-parses the query and
evaluates it locally against each paper's title and abstract - so
translation and re-parsing form a round trip. It was mapped to a translator
that emits minimal parentheses, and because AND binds tighter than OR the
query came back as an OR-dominated one matching almost the whole anthology,
truncated at `max_results` in corpus order. Fixed on 2026-09-04 in
`searcher/query.py`, with the round trip now pinned by tests in
`src/tests/searcher/test_query.py::TestLocallyEvaluatedSourceRoundTrip`.

## The screening criteria, and the trap they exist to avoid

"Personality" and "prediction" are both far too common to screen on
mechanically, and this field has three specific ways of looking relevant
without being so. The criteria and `exclusion_reasons` below name each one:

- **Not the Big Five.** MBTI prediction is a large, adjacent and much
  noisier literature - the Kaggle MBTI corpus is self-labelled by forum
  users - and HEXACO and Dark Triad work uses the same methods. These are
  worth knowing about but answer a different question, so `not_big_five`
  excludes them. `personality_model` is extracted anyway, so a later
  decision to widen the review can find them again.
- **Personality as a predictor, not a target.** Studies that measure
  personality by questionnaire and then use it to predict something else
  (job performance, health outcomes, purchase behaviour) match every
  keyword and answer the opposite question. `personality_not_predicted`.
- **No language input.** Personality inferred from profile pictures,
  smartphone sensors, likes, or network structure alone.
  `not_language_input`. Multimodal work that includes a language channel
  stays in - the review question says "mostly written but could also be
  spoken", and a paper fusing text with audio is squarely inside it.

`assess` adds one more that only a full text can answer: a paper must
actually report a quantitative result against held-out data.
`no_quantitative_results` removes position papers, surveys and dataset
descriptions with no model. Surveys are worth reading and worth citing, but
they cannot be entered into a results table without double-counting the
studies they summarise.

## Reviewer protocol

`screen.require_dual` and `assess.require_dual` are both `False`, so the LLM
reviewer's verdict is final and every decision records `single_reviewer`.

Be clear about what that costs, because it is measured rather than
theoretical: over LitRev's own demonstration corpus on 2026-08-26, a
single-reviewer pass admitted 8 papers in 42 that the adjudicated review
excludes - 19% of its own included set. See
`agents/audit-reviews/cli-dual-review-2026-08-26.md` in the LitRev repo.

That is the right trade for a first pass whose purpose is to see the shape
of the corpus, and the wrong one for the review that goes in the thesis.
Turning it around is a two-line edit - set `assess.require_dual` to `True`,
re-run `assess`, and fill in `assessments/eligibility-worklist.md` - and
`projects/human-assess/config.py` in the LitRev repo is the worked example
of the dual protocol end to end.

## Cost

`llm.provider` is `anthropic` with `claude-sonnet-5`. Estimated at roughly
$8-15 for one full pass over a corpus of this size (about 450 abstracts
screened, 150 full texts assessed, 100 papers extracted), the paper text
dominating the input tokens. `claude-opus-5` is the same config with one
word changed and roughly $20-35 a pass; it is worth it for `extract`, where
the answers are buried in methods sections and results tables, more than for
`screen`, where an abstract usually settles it.

The key is never set here - see README: Secrets. Export
`LITREV_LLM_ANTHROPIC_API_KEY` instead.

## Running it

    export LITREV_LLM_ANTHROPIC_API_KEY=...
    export LITREV_PROJECT=/Users/simonb/src/phd/reviews/big-five-nlp

    bin/litrev.sh search
    bin/litrev.sh filter
    bin/litrev.sh screen
    bin/litrev.sh download
    bin/litrev.sh convert
    bin/litrev.sh assess
    bin/litrev.sh extract
    bin/litrev.sh store
    bin/litrev.sh cite
    bin/litrev.sh prisma
    bin/litrev.sh report

See README.md beside this file for what each stage produces and where the
pass is likely to need a decision from you.
"""

import typing

config: dict[str, typing.Any] = {
    'output': {'directory': 'output'},
    'logging': {'level': 'INFO'},
    'search': {
        # Recall-oriented rather than precise: three clauses - a trait
        # vocabulary, a language-data vocabulary, and a prediction-task
        # vocabulary - joined by AND, with the narrowing left to `filter`
        # and `screen`. A query tuned to return only relevant papers is
        # also a query that silently drops the ones phrased unusually,
        # and in a systematic review that loss is invisible.
        'query': (
            '("big five" OR "five factor" OR "personality trait" OR "personality traits" OR personality) '
            'AND (text OR language OR linguistic OR speech OR "social media" OR essays OR conversation) '
            'AND (prediction OR detection OR recognition OR classification OR inference OR profiling)'
        ),
        # acl_anthology is first because that is where this literature is.
        'sources': ['acl_anthology', 'arxiv', 'crossref', 'pubmed'],
        # 'sources': ['acl_anthology', 'arxiv', 'crossref', 'pubmed', 'semantic_scholar', 'ieee'],
        'max_results': 200,
        'date_from': '1999-01-01',
    },
    'filter': {
        # Deliberately weak. `filter` is a mechanical keyword and
        # duplicate pass, not a screening decision - anything cleverer
        # here removes papers without recording a PRISMA exclusion reason,
        # which is what `screen` is for. A record only has to mention
        # personality and some form of language data to survive.
        'include_keywords': ['personality', 'trait', 'big five', 'five factor'],
        # Deliberately empty. Matching here is case-insensitive *substring*
        # matching (see filterer/keywords.py), so a short exclusion term is
        # a trap: 'rat', intended to drop animal-model studies, also matches
        # generation, accurate, rating, literature and strategy. Measured on
        # 2026-09-04 over this project's own 715-record corpus, it rejected
        # 398 records - 56% of everything found - including "Learning to
        # Answer Psychological Questionnaire for Personality Detection" and
        # the PANDORA corpus paper, which are core to this review.
        #
        # Animal-model work is a small fraction of what this query returns
        # and `screen` excludes it on the criteria with a recorded PRISMA
        # reason, which is the right place for a judgement. If an exclusion
        # term is ever added back, it must be long enough not to appear
        # inside an unrelated word: 'zebrafish' is safe, 'rat' is not.
        'exclude_keywords': [],
        'required_fields': ['abstract', 'issued', 'title'],
        'similarity_threshold': 0.85,
    },
    'llm': {
        'provider': 'anthropic',
        'anthropic': {'model': 'claude-sonnet-5'},
    },
    'screen': {
        'criteria': (
            'Studies that predict, detect or infer Big Five (five-factor) personality traits - '
            'openness, conscientiousness, extraversion, agreeableness, neuroticism - from human '
            'language, whether written text or transcribed or acoustic speech. Include multimodal '
            'studies where language is one of the input channels. Include work on any language, '
            'any population and any text genre. Published 1999 or later, reported in English.'
        ),
        'exclusion_reasons': [
            'not_big_five',
            'personality_not_predicted',
            'not_language_input',
            'not_english',
        ],
        'require_dual': False,
        # Batch dispatch: the same model at half the per-token price, on
        # Anthropic's Message Batches endpoint. Scoped to this stage rather
        # than set globally, so `assess`, `extract` and `appraise` keep
        # immediate dispatch and stay interactive.
        #
        # The trade is latency, not quality: a batch is promised within 24
        # hours and usually returns far sooner. Screening a snowball round's
        # candidates is not interactive work - nothing waits on it but the
        # next stage - so the wait costs nothing and the discount is real.
        'dispatch': 'batch',
    },
    'download': {
        # `screen` sits between `filter` and `download`, so retrieval is
        # attempted only for records that survived title/abstract
        # screening. Without this the default `filtered.json` would send
        # the resolver chain after several hundred PDFs this review has
        # already decided it does not want.
        'input_path': 'output/assessments/screened.json',
        # `unpaywall` is deliberately absent. It is the one resolver that
        # needs configuring - the Unpaywall API requires an email address
        # as a courtesy identifier - and without `download.unpaywall_email`
        # it raises a ResolverError for every item it is handed rather than
        # reporting a clean miss, so listing it unconfigured buys nothing
        # but noise in the manifest. Much of this literature is in the ACL
        # Anthology and on arXiv, both fully open access, so `direct` and
        # `arxiv` carry most of the corpus without it.
        #
        # To enable it, set `unpaywall_email` and add 'unpaywall' back to
        # the end of the chain. That address is sent to a third party on
        # every request, which is why it is not filled in here by default.
        #
        # `semantic_scholar` was dropped from the default chain alongside
        # `unpaywall` with no reason recorded, which on this corpus was a
        # mistake. Most records here were built from Semantic Scholar
        # papers, and every such record carried that service's landing page
        # as its URL - a page rather than a file - so `direct` was handed a
        # question it could not answer and won nothing. This resolver asks
        # the same API for the record's `openAccessPdf` instead, and nearly
        # every one of those records has the DOI it needs. Restoring it on
        # 2026-09-22 retrieved 16 papers the chain had given up on.
        #
        # LitRev now prefers `openAccessPdf` when it builds the record, so
        # records created from here on carry a file URL and `direct` can
        # win them. Keep this resolver anyway: it still covers the records
        # already stored with a landing page, and any record whose
        # open-access copy was not known at search time but is now.
        #
        # It needs no configuring - unlike `unpaywall` - and it shares one
        # rate limiter with the searcher's semantic_scholar source, so it
        # cannot race that stage against the same host. It is not free:
        # that shared limiter took the stage from 5m27s to 26m.
        'resolvers': ['direct', 'arxiv', 'semantic_scholar', 'doi'],
        # 'unpaywall_email': '<your-email>',
        'max_concurrent': 5,
    },
    'convert': {
        # Results in this field live in tables - per-trait accuracy or
        # F1 across five columns - so table structure recovery is what
        # makes `extract` able to answer the metrics question at all.
        'table_structure': True,
        # 'auto' is already the default and is stated here because the
        # date range makes it load-bearing: scanned pre-2005 psychology
        # PDFs are common enough to need the fallback, which reconverts
        # with OCR only when the text layer yields fewer than
        # `convert.ocr_min_chars` characters. 'always' would put every
        # born-digital ACL paper through OCR for nothing.
        'ocr': 'auto',
    },
    'assess': {
        'criteria': (
            'Full-text studies that build or evaluate a computational model predicting Big Five '
            'personality traits from language data, and report at least one quantitative result '
            'on held-out data - accuracy, F1, precision/recall, RMSE, MAE or correlation. The '
            'paper must identify the dataset it used and describe its modelling approach in '
            'enough detail to be summarised. Exclude surveys and reviews that report only results '
            'obtained by others, and dataset or resource papers that introduce no model.'
        ),
        'exclusion_reasons': [
            'not_big_five',
            'personality_not_predicted',
            'not_language_input',
            'no_quantitative_results',
            'survey_or_review',
            'full_text_unavailable',
        ],
        'require_dual': False,
        # Batch dispatch, as `screen` uses and for the same reason: nothing
        # is waiting on a full-text pass but the next stage. It matters more
        # here than there - a full-text assessment sends the whole paper, so
        # the measured cost is roughly 20,000 input tokens each against
        # screening's 1,300, and half of a larger number is a larger saving.
        'dispatch': 'batch',
    },
    'extract': {
        # One LLM call per paper answers this whole block as a single
        # JSON object, each field carrying a verbatim supporting quote,
        # so a richer field set costs output tokens rather than input
        # ones - the paper text dominates either way.
        #
        # But a field set is bounded by the provider, not only by cost.
        # This block held seventeen fields on 2026-09-04 and every call
        # failed with HTTP 400:
        #
        #   Schemas contains too many parameters with union types (30
        #   parameters with type arrays or anyOf) ... limit: 16 parameters
        #   with unions
        #
        # Each field is nullable so a paper can honestly answer "not
        # reported", and each carries a nullable quote, so seventeen
        # fields generate about thirty union-typed parameters against a
        # ceiling of sixteen. The rejection happens at schema compilation,
        # before any inference, so it is fast and free - but total.
        #
        # The arithmetic is worth stating, because it is not one union
        # per field. build_field_schema() gives every field a nullable
        # `value` and a nullable `quote`, so a field costs two unions -
        # except an enum, whose value is rendered as {'enum': [...]} and
        # costs nothing. The budget is therefore
        #
        #     2 * (non-enum fields) + 1 * (enum fields) <= 16
        #
        # Seventeen fields cost 30. This block now holds five non-enum and
        # five enum fields: 2*5 + 5 = 15, one under the ceiling.
        #
        # Seven fields were folded into their neighbours rather than
        # dropped - dataset_is_new, sample_size, data_language and
        # text_genre into `datasets`; traits_modelled_jointly into
        # `model_architecture`; reports_per_trait_results and
        # baseline_comparison into `headline_results` - and
        # code_or_data_available became an enum to buy back a union.
        # Nothing the review asks went away; several answers are now
        # structured prose inside a field rather than a field of their
        # own. Adding a non-enum field back means removing another, or
        # turning one into an enum.
        'fields': {
            # --- Datasets -------------------------------------------------
            'datasets': {
                'type': 'list[str]',
                'description': (
                    'Named datasets or corpora the study trains or evaluates on, as the paper '
                    'names them (for example "Essays", "myPersonality", "PAN-2015", "First '
                    'Impressions V2", "Friends Persona"). Include a newly collected corpus, '
                    'named or described.\n'
                    'Give one entry per dataset, each in the form '
                    '"<name> | <genre> | <language> | <n> subjects", where genre is the '
                    'provenance of the language data (stream-of-consciousness essays, Facebook '
                    'status updates, tweets, interview transcripts, YouTube vlogs, novels), '
                    'language is the natural language of the data, and n is the number of '
                    'individual people whose personality is labelled - people, not documents. '
                    'Write "unclear" for any part the paper does not report, and append " (new)" '
                    'to any corpus the study itself collects or releases.'
                ),
            },
            'modality': {
                'type': 'enum',
                'choices': ['written_text', 'transcribed_speech', 'acoustic_speech', 'multimodal', 'other'],
                'description': 'Form of the language input. Use multimodal where a non-language channel such as audio prosody, video or images is fused with language.',
            },
            'ground_truth_method': {
                'type': 'enum',
                'choices': [
                    'self_report_questionnaire',
                    'observer_rated',
                    'expert_annotated',
                    'crowd_annotated',
                    'derived_from_user_profile',
                    'llm_annotated',
                    'not_reported',
                    'other',
                ],
                # litrev warns that this asks the quote for a second fact.
                # Checked against the 2026-09-04 run and kept: 36 of the 58
                # judged quotes name an instrument, because a sentence
                # supporting 'self_report_questionnaire' usually says which
                # questionnaire. Partial rather than reliable, but nothing
                # downstream derives a judgement from the instrument - unlike
                # the split unit, which the appraiser's Analysis domain turns
                # on - so a partial answer costs nothing and a field of its
                # own is unaffordable: the schema is at its 16-union ceiling.
                'description': 'How the personality labels were obtained. Name the specific instrument in the quote where the paper gives one (BFI-44, NEO-PI-R, IPIP, TIPI, BFI-2).',
            },
            # --- Modelling ------------------------------------------------
            'task_formulation': {
                'type': 'enum',
                'choices': ['binary_classification', 'multiclass_classification', 'regression', 'ranking', 'generation', 'other'],
                'description': 'How trait prediction is posed. Binary usually means a median split per trait; regression means predicting the continuous score.',
            },
            'features_or_representation': {
                'type': 'list[str]',
                'description': 'Input representations, for example LIWC categories, n-grams, TF-IDF, Mairesse features, word2vec, GloVe, BERT embeddings, prosodic features, raw prompting.',
            },
            'model_architecture': {
                'type': 'list[str]',
                'description': (
                    'Learning methods or model families evaluated, for example SVM, logistic '
                    'regression, random forest, CNN, BiLSTM, BERT, RoBERTa, GPT-4, LLaMA. '
                    'Include the fine-tuning or prompting strategy where the paper names one. '
                    'Add "multi-output" or "per-trait models" as a final entry to record '
                    'whether the five traits are predicted jointly or by five separate models.'
                ),
            },
            # --- Results --------------------------------------------------
            'evaluation_metrics': {
                'type': 'list[str]',
                'description': 'Metrics reported, for example accuracy, macro F1, weighted F1, RMSE, MAE, Pearson r, concordance correlation coefficient.',
            },
            'headline_results': {
                'type': 'str',
                'description': (
                    'The best reported result, with its metric, its dataset and the trait it belongs to. '
                    'Give per-trait figures where the paper reports them (for example "accuracy: O .621, '
                    'C .570, E .590, A .578, N .588 on Essays") rather than only an average across traits; '
                    'if only an average over the five traits is reported, say so explicitly. '
                    'End with what the result is compared against - a majority-class baseline, a named '
                    'prior system, an ablation, or nothing.'
                ),
            },
            'validation_scheme': {
                'type': 'enum',
                'choices': [
                    'train_test_split',
                    'k_fold_cross_validation',
                    'nested_cross_validation',
                    'leave_one_out',
                    'held_out_benchmark_split',
                    'not_reported',
                    'other',
                ],
                'description': 'How held-out evaluation was done.',
            },
            # Split off validation_scheme's description, which used to ask the
            # quote to note whether the split was by subject or by document.
            # That never happened: a quote must support its own value, and a
            # sentence supporting 'train_test_split' is generally not one that
            # names what the split is by. Of the 64 quotes the 2026-09-04 run
            # produced, none stated the unit, which left the appraiser's
            # Analysis domain - 39 of 70 studies judged high, largely on
            # leakage - with nothing on disk to check it against.
            #
            # An enum rather than a str by arithmetic, not taste: the schema
            # ceiling below allows 2*(non-enum) + 1*(enum) <= 16, and this
            # review sits at 2*5 + 5 = 15. An enum lands on 16 exactly; a str
            # would land on 17 and every call would fail at compilation.
            'validation_split_unit': {
                'type': 'enum',
                'choices': [
                    'by_subject',
                    'by_document',
                    'mixed',
                    'not_applicable',
                    'not_reported',
                ],
                'description': (
                    'Whether the held-out evaluation separates subjects or only documents. by_subject means no '
                    'person appears in both training and test; by_document means the split is over texts and one '
                    'person may appear on both sides, which leaks. not_applicable where the paper does no '
                    'held-out evaluation at all.'
                ),
            },
            'code_or_data_available': {
                'type': 'enum',
                'choices': ['code_and_data', 'code_only', 'data_only', 'none', 'not_stated'],
                # Same warning, same decision: 20 of the 36 releasing studies'
                # quotes carry a URL, since a sentence announcing a release
                # often gives one. Additive, with no derived claim resting on
                # it.
                'description': 'What the paper states is publicly released. The quote should carry the URL or repository name if one is given.',
            },
        },
        'instructions': (
            'Answer from the study itself, not from related work it cites or compares against. '
            'Where a paper reports several models, the headline result is its own best system, '
            'not the strongest number in any table. Where a paper reports several datasets, list '
            'all of them and make the headline result say which dataset it came from. Report '
            'metrics exactly as scaled in the paper - do not convert a correlation to a '
            'percentage or an F1 to accuracy.'
        ),
    },
    # Risk-of-bias appraisal. PROBAST's four domains - the established
    # instrument for appraising prediction-model studies, which is what
    # these papers are - with the concern for each written against this
    # literature's own failure modes rather than PROBAST's generic
    # wording. The names are the instrument's so a reviewer recognises
    # them; the prose is this review's.
    #
    # LitRev supplies the answers (low / some_concerns / high /
    # no_information); this file supplies only the question. Editing a
    # concern re-appraises without re-extracting - that decoupling is why
    # `appraise` is a stage of its own rather than extra extract fields.
    'appraise': {
        'domains': {
            'Participants': (
                'Were the people whose language was analysed an appropriate sample for the '
                'target population, and is that population stated? Judge high where a '
                'convenience sample - students, crowdworkers, or self-selected social media '
                'users - is presented as a general population without qualification.'
            ),
            'Predictors': (
                'Were the language features defined and computed without knowledge of the '
                'personality scores? Judge high where feature selection, prompt design or '
                'hyperparameters were tuned against the test labels.'
            ),
            'Outcome': (
                'Were personality scores obtained with a validated instrument, and is it '
                'named? Judge low for a full inventory such as NEO-PI-R or BFI-44, some '
                'concerns for a brief scale such as TIPI or BFI-10, and high where labels are '
                'inferred from a user profile, annotated by a model, or the instrument is not '
                'reported.'
            ),
            'Analysis': (
                'Does the held-out evaluation support the claim? Judge high where the split is '
                'by document rather than by subject, so one person contributes to both '
                'training and test; where the sample is too small for the number of '
                'parameters; or where results are reported for some traits only, or against no '
                'baseline.'
            ),
        },
        # Participants and Outcome are properties of a corpus, not of a paper:
        # who was sampled and how their labels were obtained belong to the
        # dataset. Judging them once per study forced the model to pick one
        # corpus unprompted when a paper used several, and it always picked
        # the weakest - 21 of the 36 studies judged high on Outcome in the
        # 2026-09-16 run were multi-dataset, with Vu et al. judged on YouTube
        # impression scores while its Essays results, scored against
        # self-report BFI, sat in the same results table.
        #
        # Predictors and Analysis stay per study: feature construction and the
        # evaluation scheme are what the authors did, not what the corpus is.
        'unit_field': 'datasets',
        'unit_domains': ['Participants', 'Outcome'],
    },
    'store': {
        'path': 'output/litrev.db',
    },
    'cite': {
        'style': 'harvard1',
        'format': 'markdown',
        # BibTeX for the thesis itself, CSL JSON as the reference-manager
        # interchange format. Both land under output/citations/.
        'exports': ['bibtex', 'csl-json'],
    },
    'prisma': {
        'title': 'Big Five personality detection from natural language',
        'format': 'mermaid',
    },
    'report': {
        # Markdown is written whether it is listed or not - the PDF is a
        # pandoc conversion of it, so asking for `pdf` alone would still
        # leave the markdown behind. Listing both says so out loud, and
        # keeps the two files in step: with markdown alone, a rerun
        # refreshes report.md and leaves a stale report.pdf beside it.
        # Needs `pandoc` and the `typst` engine on PATH.
        'formats': ['markdown', 'latex', 'pdf'],
        # `title` is deliberately unset: it falls back to prisma.title,
        # which is the name this review already goes by. Setting it here
        # would be a second copy of that string, free to drift from it.
        #
        # `strict` stays False while the review is still moving. Turn it
        # to True before the document goes into the thesis: it makes an
        # unexplained discrepancy in the PRISMA counts fail the run
        # instead of rendering it into a table nobody re-checks.
        'strict': False,
        # `datasets` entries are written "<name> | <genre> | <language> |
        # <n> subjects" (see extract.fields above), so counting them
        # verbatim makes almost every row a singleton: "Essays | ... |
        # 2468 subjects", "... | 2,468 subjects" and "... | 2467
        # subjects" are three rows for one corpus, because three papers
        # reported its size three ways. Keying on the separator counts
        # the name alone, which is the thing the frequency table is
        # asking about.
        #
        # This is lexical, not semantic: "Essays", "Essays Dataset" and
        # "Stream-of-consciousness essays" stay three rows. That is the
        # honest answer - the table shows what the extraction said, and
        # seeing the variants is itself useful - but it means the counts
        # are a floor, not a total.
        'frequency_key_separator': '|',
        # Fold the singleton tail into one generated row. With the
        # separator above, `datasets` still has a long tail of corpora
        # used by one study each; a table whose every row reads "1" is
        # not a finding. Raise this if a table is still unreadable, and
        # lower it to 1 to see every value again - it applies to every
        # list[str] field, not just `datasets`.
        'frequency_min_count': 2,
        # Group the results section by the corpus a study evaluated on,
        # so work on the same dataset sits together and can be compared.
        # Unset, the section renders a placeholder rather than guessing
        # a field.
        'results_group_field': 'datasets',
        # Fold the singleton tail of the results section. A group holding one
        # study compares nothing, and keyed on the separator above this
        # review has a long tail of corpora used once. The gathered studies
        # keep their result text - they are relisted under one heading, not
        # summarised away.
        #
        # Separate from `frequency_min_count` on purpose: that one governs
        # every list[str] field's frequency table, this one only the field
        # `results_group_field` names.
        'results_min_group_size': 2,
        # `synthesis` joins the default supplementary set. It is the
        # per-field transpose - one table per field, one row per study -
        # which was the only synthesis available before `characteristics`
        # and `frequencies` existed, and those two now cover the same
        # ground in the shape a paper uses: one row per study, and a
        # count per value. Keeping all three in the manuscript spends
        # about a third of its length restating the same data a third
        # way.
        #
        # Routed rather than dropped from `sections`: the per-field
        # tables are the audit trail for every extracted value, and a
        # reviewer asking where a number came from should still be able
        # to find it. Dropping it would also mean listing every section
        # that survives, which is a hand-maintained copy of the `Section`
        # literal - a later phase's new section would go missing from
        # this review silently.
        'supplementary_sections': ['synthesis', 'studies', 'exclusions'],
    },
    'scan': {
        # Where `download` writes, so a hand-collected PDF dropped into
        # the same directory is identified and renamed by the same rules.
        'directory': 'output/downloads',
    },
    'snowball': {
        # Citation searching, PRISMA's "other methods" column: follow the
        # references and citers of the papers this review already included,
        # to find records the database search missed.
        #
        # Every path is left at its default (included.json in, and
        # snowball-candidates.json / snowball.json out, all under
        # output.directory), because the defaults are exactly where this
        # review's files already are. Only the parameters that are a
        # judgement are stated here.
        #
        # One round. depth records the intent rather than enforcing it -
        # the stage runs one round per invocation, because a further round
        # is only meaningful after this one's candidates have been
        # screened, and that is a human step in between.
        'depth': 1,
        # Both directions. Backward finds the foundations this field builds
        # on, which a keyword search misses whenever the vocabulary has
        # moved; forward finds work that cites an included paper, which is
        # where anything published after the search date lives. Dropping
        # forward would halve the requests, and would also drop the half
        # that covers the gap between the search and today.
        'directions': ['backward', 'forward'],
        # A heavily cited paper would otherwise dominate the round: the cap
        # is per seed per direction, so a single well-known benchmark paper
        # cannot supply most of a round's candidates on its own.
        'max_per_seed': 200,
        # Off: a seed already followed is not followed again, so a repeated
        # run costs nothing for the seeds it has already done. Turn it on
        # for a forward search repeated months later, when papers citing a
        # seed exist that did not before - backward references do not
        # change, so re-following them buys nothing.
        'refollow': False,
    },
}
