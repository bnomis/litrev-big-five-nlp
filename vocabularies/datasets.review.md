# Review: `datasets` vocabulary proposal

## What is being reviewed and how

`litrev normalise` proposed a first `datasets` vocabulary on 2026-10-08 (anthropic `claude-sonnet-5`, effort `low`), from every dataset name in `extractions.json`'s `datasets` field and `tables.json`'s `results.dataset` column. No vocabulary existed, so every name was unmapped. The proposal is `vocabularies/datasets.proposed.json`.

For each proposed cluster: approve it, reject it, or rename its label. For each unassigned name: assign it to a label (existing or new), or leave it unassigned on purpose. Decide on the interactive page, <https://claude.ai/artifact/JxM5qvpyGSgNKMXMrGhN4t>; the answers are copied into the Answers section below, and then into `vocabularies/datasets.json`.

Counts below were taken on 2026-10-08 and are a record of this proposal, not of the review now.

## Automatic checks

| Check | Result |
|-------|--------|
| Every unmapped name is either in a cluster or unassigned | pass: 204 clustered + 153 unassigned = 357 names |
| No name in two clusters | pass after validation: the validator moved the three names below to unassigned |
| Names the model put in more than one cluster | fail: `PAN 2015 Author Profiling task dataset (English)`, `(Italian)`, `(Spanish)` |
| Names the model did not place | fail: `Essays test set (same 23 participants)`, `Personality` |
| Clusters holding only their own label | 19 - these merge nothing; approving them only fixes the spelling |

## The items

### Proposed clusters

Mentions sum each name's study count, so a study naming two aliases counts twice.

| Label | Names | Mentions | Model's rationale |
|-------|-------|----------|-------------------|
| AUG-Essays | 1 | 1 | Augmented essays dataset variant. |
| BIT Speaker Personality Corpus | 1 | 4 | Single dataset name. |
| CLPsych-2018 | 1 | 1 | Single consistent name. |
| CLPsych-2019 | 1 | 1 | Single consistent name. |
| CPED | 1 | 5 | Single dataset name. |
| CVs and free text responses | 4 | 4 | These refer to CV/free-text recruiting data from the same source context. |
| CXD (Columbia Deception Corpus) | 7 | 7 | These all reference the Columbia Cross-Cultural Deception corpus. |
| ChaLearn First Impressions Dataset | 11 | 16 | These all reference the ChaLearn First Impressions dataset and its V2 variants. |
| ContArgA | 1 | 2 | Single consistent name. |
| ConvAI | 1 | 2 | Single consistent name. |
| Cover Letters | 2 | 2 | Same dataset referring to cover letters. |
| DAIC-WOZ | 1 | 2 | Standard DAIC-WOZ dataset name. |
| Empathic Conversations | 3 | 3 | These all reference the Empathic/Empathetic Conversations dataset. |
| Essays | 17 | 94 | These all refer to the Pennebaker & King stream-of-consciousness essay corpus widely used for Big Five personality prediction. |
| Essays (GloVe) | 2 | 2 | GloVe embedding variant of essays dataset. |
| Essays (LIWC) | 2 | 2 | LIWC feature variant of essays dataset. |
| Essays (TF-IDF) | 2 | 2 | TF-IDF feature variant of essays dataset. |
| Essays (W2V) | 2 | 2 | Word2Vec feature variant of essays dataset. |
| Facebook | 13 | 20 | These refer to Facebook-based personality datasets, largely from Schwartz et al. and related studies. |
| Filipino Twitter Corpus | 2 | 2 | Same dataset, different casing. |
| Fisher dataset | 2 | 2 | Variant subsets of the Fisher dataset. |
| FriendsPersona | 1 | 7 | Single consistent dataset name. |
| GenBigFive | 2 | 2 | Same dataset variant. |
| HiTOP | 2 | 2 | Same dataset with segment variant. |
| Indonesian Twitter Personality Dataset | 3 | 3 | Refers to the same Indonesian-language Twitter personality dataset. |
| Kaggle (PersonalityCafe) | 11 | 18 | These refer to the Kaggle MBTI/PersonalityCafe forum dataset commonly used for MBTI classification. |
| LLM Personality | 1 | 2 | Single consistent name. |
| LinkedIn profiles | 2 | 3 | Same LinkedIn-based dataset variants. |
| MBTI9k | 1 | 2 | Single consistent name. |
| MSAPersonality | 1 | 6 | Single consistent name. |
| Mandarin Conversational Dialogue Corpus (MCDC) | 2 | 2 | Same dataset abbreviation and full name. |
| MultiWOZ | 1 | 2 | Single consistent name. |
| PAN-AP-2015 | 22 | 23 | These are all variants/subsets of the PAN 2015 Author Profiling dataset. |
| PANDORA | 4 | 12 | Variant capitalization/subset naming of the PANDORA Reddit personality dataset. |
| PersonaLLM | 2 | 2 | Same dataset naming variant. |
| Personality-1260 | 1 | 2 | Single consistent name. |
| PersonalityEvd | 3 | 3 | Variants/subsets of the PersonalityEvd dataset. |
| RealPersonaChat | 3 | 3 | Variants of the RealPersonaChat dataset. |
| Reddit | 1 | 2 | Single consistent name. |
| Reddit Calibration Data Set | 2 | 2 | Same Reddit calibration dataset. |
| SPADE | 2 | 3 | Variants of SPADE speech corpus. |
| SPAN (St. Louis Personality and Aging Network) | 5 | 8 | These refer to the same SPAN life narrative interview dataset. |
| Sample14 | 1 | 2 | Single consistent name. |
| Self-Descriptions | 2 | 2 | Same dataset naming variants. |
| Sentiment140 | 1 | 2 | Single consistent name. |
| Story2Personality | 2 | 2 | Same dataset with Big Five annotation noted. |
| TB5I | 1 | 2 | Single consistent name. |
| Twitter | 9 | 14 | These are general Twitter-based personality datasets without more specific distinguishing names. |
| WASSA 2022 | 3 | 3 | Variants naming the WASSA 2022 shared task dataset. |
| WASSA 2023 | 6 | 6 | Variants of the WASSA 2023 shared task dataset. |
| WTC | 2 | 2 | Same dataset with segment variant. |
| Weibo | 4 | 4 | These all reference Sina Weibo social media data. |
| Yelp | 2 | 2 | Same Yelp review dataset. |
| YouTube | 2 | 2 | Same platform name casing variants. |
| YouTube personality dataset | 8 | 10 | All refer to the YouTube vlogger personality dataset (Biel & Gatica-Perez/IDIAP). |
| b5-post | 1 | 4 | Single consistent name. |
| myPersonality | 9 | 40 | All refer to the myPersonality Facebook dataset. |
| myPersonality & DAIC-WOZ | 2 | 2 | Combined dataset name variants. |

### Unassigned names (needing attention)

Each needs a decision: none was explained by the model.

| Name | Studies | Flag |
|------|---------|------|
| Personality | 4 | not placed |
| Backstage | 2 |  |
| FriendFeed | 2 |  |
| PAN 2015 Author Profiling task dataset (English) | 2 | in two clusters |
| Abusive writing | 1 |  |
| Actions | 1 |  |
| Amazon movie reviews | 1 |  |
| AMT Psychometric Survey Data (Directed/Undirected Responses) | 1 |  |
| ASF developer email corpus (Phase 1 gold standard) | 1 |  |
| ASF ecosystem email/commit dataset (Calefato et al. 2019a replication) | 1 |  |
| ASF email corpus | 1 |  |
| BFI survey ground truth subset | 1 |  |
| Blog corpus (Nowson & Oberlander) | 1 |  |
| Blog posts from WordPress-hosted sites | 1 |  |
| ChatGPT interaction logs (new) | 1 |  |
| ChatGPT logs | 1 |  |
| Chinese data | 1 |  |
| CMU-MOSEI | 1 |  |
| Commonsense reasoning survey dataset | 1 |  |
| Conversation | 1 |  |
| Cornell Movie-Dialogs Corpus | 1 |  |
| counseling dialogues | 1 |  |
| Counseling dialogues corpus (new) | 1 |  |
| Crunchbase leaders dataset (this study) | 1 |  |
| D_HR (small high-reliability dataset) | 1 |  |
| D_LR (large low-reliability dataset) | 1 |  |
| Deceptive speech corpus (fake resume paradigm) | 1 |  |
| diary studies | 1 |  |
| Direct speech | 1 |  |
| Directed Responses | 1 |  |
| EAR corpus (Mehl, Golsing & Pennebaker) | 1 |  |
| EAR-Obs | 1 |  |
| EAR-Self | 1 |  |
| Emotions Dataset | 1 |  |
| English data | 1 |  |
| Essays test set (same 23 participants) | 1 | not placed |
| F2 | 1 |  |
| F2P | 1 |  |
| F3 | 1 |  |
| Facebook ego-network corpus (new) | 1 |  |
| Facebook posts + IPIP Big5 questionnaire responses (new) | 1 |  |
| Facebook profile dataset (Golbeck et al. 2011) | 1 |  |
| Facebook Wall Posts Dataset (new) | 1 |  |
| Fiction (Articles) | 1 |  |
| Fictional character personality dataset (from Personality Databank, characters from novels such as Harry Potter, Game of Thrones, Lord of the Rings, Star Wars, Twilight, classical literature) | 1 |  |
| Generated Data | 1 |  |
| geo-social media dataset | 1 |  |
| Geotagged social media dataset (Twitter, Instagram, Flickr, iNaturalist) | 1 |  |
| Gerrit (SentiCR, Ahmed et al.) | 1 |  |
| GitHub | 1 |  |
| GitHub comments (emotion corpus, 2.2 million comments across 406,600 pull requests) | 1 |  |
| GitHub communications data (GHTorrent, top 3% projects) | 1 |  |
| GitHub pull request comments (personality corpus) | 1 |  |
| GitHub pull-request/commit trace dataset (reconstructed for Iyer et al. replication) | 1 |  |
| GPT-3 generated dialogues (new) | 1 |  |
| Individual Text Corpora (ICs) | 1 |  |
| Individual text corpora (ICs) from Google search histories | 1 |  |
| Interview dataset of 555 U.S. adults (518 with complete BFI-10) | 1 |  |
| IPIP-NEO-300 | 1 |  |
| Ironic Corpus | 1 |  |
| ISEAR | 1 |  |
| JIRA (Ortu et al.) | 1 |  |
| Job recommendation dialogue (MBTI) | 1 |  |
| L | 1 |  |
| LLM Emotion | 1 |  |
| Long (>3,500 words) | 1 |  |
| MaSaC | 1 |  |
| MBTI | 1 |  |
| Medium (1,500-3,500 words) | 1 |  |
| MELD | 1 |  |
| Movie Script | 1 |  |
| Movie-Dialogs Corpus | 1 |  |
| Multi-PR GPA User Study Corpus (new) | 1 |  |
| MUStARD | 1 |  |
| NC | 1 |  |
| New conversational corpus (LLM-guided personality interviews) | 1 |  |
| New Corpus (NC) | 1 |  |
| Newly collected chatbot-conversation corpus (this study) | 1 |  |
| News (Articles) | 1 |  |
| News (Titles) | 1 |  |
| Nilsson et al. (2024) EMA dataset (service industry alcohol-use study) | 1 |  |
| Open Source Shakespeare (OSS) | 1 |  |
| Open-domain | 1 |  |
| Open-domain dialogue corpus (new) | 1 |  |
| OpenPsychometrics IPIP Big Five Survey | 1 |  |
| Ordinary World novel dialogues (Shaoping Sun and Shaoan Sun) | 1 |  |
| Original Corpus (OC) | 1 |  |
| Ours (BF-CC bilingual synthetic dialogue dataset) | 1 |  |
| PAN 2015 Author Profiling task dataset (Italian) | 1 | in two clusters |
| PAN 2015 Author Profiling task dataset (Spanish) | 1 | in two clusters |
| Pantheon 1.0 dataset | 1 |  |
| Participant-author's personal 16-year email archive | 1 |  |
| PER (Track3) | 1 |  |
| PIGA-augmented Essays (LLM-translated, personality-informed) | 1 |  |
| PIGA-augmented Kaggle (LLM-translated, personality-informed) | 1 |  |
| Predicatives | 1 |  |
| Private | 1 |  |
| Produced text (Reddit comments) | 1 |  |
| Prolific speech and personality dataset (new) | 1 |  |
| PTCD | 1 |  |
| PTCD-derived Personality Detection Dataset | 1 |  |
| Public figure personality perception dataset (new) | 1 |  |
| Real-world data | 1 |  |
| Real-World Interview | 1 |  |
| Real-world semi-structured interview dataset | 1 |  |
| Reddit Fiction Dataset | 1 |  |
| Reddit Founders Dataset (new) | 1 |  |
| Reddit music-fan corpus (new) | 1 |  |
| Reddit News Dataset | 1 |  |
| Reddit Online Communities Dataset (new) | 1 |  |
| Reddit Personality Descriptions | 1 |  |
| Rentfrow et al. (2013) state-level personality survey | 1 |  |
| Sarcasm Dataset | 1 |  |
| Semi-structured interview dataset | 1 |  |
| Short (<1,500 words) | 1 |  |
| SMP2020-EWECT | 1 |  |
| SOC writing | 1 |  |
| social media (meta-analysis) | 1 |  |
| Social Media Text | 1 |  |
| StackOverflow Java Lib (Lin et al.) | 1 |  |
| StackOverflow Sentiments (Senti4SD, Calefato et al.) | 1 |  |
| STORAL | 1 |  |
| Suicide and Depression (Reddit) | 1 |  |
| Suicide and depression dataset (Reddit, SuicideWatch/depression/teenagers subreddits) | 1 |  |
| Task-E2E dialogue corpus (new) | 1 |  |
| Task-pipeline | 1 |  |
| Task-pipeline dialogue corpus (new) | 1 |  |
| TEC | 1 |  |
| TED English-French (IWSLT 2014, gender-annotated) | 1 |  |
| TED61 en (matched subset of TED English-French) | 1 |  |
| TED61 fr-en (TEDx France) | 1 |  |
| Text Emotion | 1 |  |
| TOGA-augmented Essays and Kaggle (translation-only control) | 1 |  |
| Track 4 dataset | 1 |  |
| Turkish Texts | 1 |  |
| Twitter #SocialNetworks dataset | 1 |  |
| Twitter (manually collected, extended from Adi et al. and Ong et al.) | 1 |  |
| Twitter (state-level aggregated) | 1 |  |
| Twitter (Sumner et al. 2012 new corpus) | 1 |  |
| Twitter county-level corpus 2012-2014 (10% random sample) | 1 |  |
| Twitter+Instagram (new) | 1 |  |
| UM Corpus | 1 |  |
| Unconstrained use | 1 |  |
| Undirected Responses | 1 |  |
| United States Congressional Records (Congress) | 1 |  |
| Unnamed corpus (new) | 1 |  |
| User-Level | 1 |  |
| WASSA 2024 Track 4 PER dataset | 1 |  |
| Wave-Level | 1 |  |
| With Depressive Symptoms | 1 |  |
| Without Depressive Symptoms | 1 |  |
| X (Twitter) tweets dataset | 1 |  |
| YourMorals | 1 |  |

## Decisions

1. **`Essays (GloVe)`, `Essays (LIWC)`, `Essays (TF-IDF)`, `Essays (W2V)` are separate clusters.** These name a feature set, not a corpus. Options: rename each to `Essays` so they merge (one corpus), or keep them apart. Recommendation: rename to `Essays` - the report counts corpora, and the feature set is the modelling approach, not the data.
2. **Platform labels (`Facebook`, `Twitter`, `Reddit`, `YouTube`, `Weibo`, `Yelp`) beside named corpora (`myPersonality`, `PANDORA`, `YouTube personality dataset`).** Options: keep the platform as the label for self-collected data, or fold each into a named corpus where the aliases show one. Recommendation: keep platform labels for self-collected data, and move any alias that names a published corpus to that corpus.
3. **`myPersonality & DAIC-WOZ` is one cluster for two corpora.** Options: reject it and assign its names to each corpus, or keep it. Recommendation: reject - one label must name one corpus; a value naming both can stay unassigned.
4. **The PAN 2015 per-language names.** Options: assign all three to `PAN-AP-2015`, or keep languages apart. Recommendation: assign to `PAN-AP-2015`; the language is not a different corpus.
5. **Generic names (`Personality`, `diary studies`, `counseling dialogues` and similar).** Options: leave unassigned, or give each a descriptive label. Recommendation: leave unassigned - they name no corpus, and the report should not count them as one.

## Answers

Answered 2026-10-08 on the review page; read back from its store and applied to `vocabularies/datasets.json`.

- **Clusters:** all 58 approved as proposed; none rejected or renamed.
- **Decisions 1 and 3 (Essays feature variants, `myPersonality & DAIC-WOZ`):** not taken - those clusters were approved as they stand.
- **Decision 2 (platform labels):** kept; `Facebook profile dataset (Golbeck et al. 2011)` assigned to `myPersonality`.
- **Decision 4 (PAN 2015):** taken - the English, Italian and Spanish names assigned to `PAN-AP-2015`.
- **Decision 5 (generic names):** taken - left unassigned.
- **Other assignments:** `Essays test set (same 23 participants)` to `Essays`.
- **New labels**, from notes on names marked "Leave unassigned", confirmed in conversation as meant to be labels: `ASF` (three ASF email corpora), `ChatGPT` (two ChatGPT log sets), `EAR` (EAR corpus, EAR-Obs, EAR-Self), `F2` (F2, F2P), `NC` (NC, New Corpus (NC)).
- **Undecided on the page:** `PIGA-augmented Kaggle (LLM-translated, personality-informed)` - left unassigned, confirmed in conversation.
- **Everything else unassigned** was marked "Leave unassigned".
