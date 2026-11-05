# Big-five review to do

Open work on this review. Defects in LitRev itself are filed in LitRev's own
`TODO.md`.

## Give each result row its model family

<!-- doc-counts: accept-start figures from the 2026-10-27 tabulate run - a record, not a claim about the present -->
Found 2026-10-30 by LitRev's `/todo-review`. On 2026-10-30, commit
`ec99897` coded the paper-level field `model_architecture` into 13 model
families, which is step 1 of the plan to explore which models papers use.
Step 2 was agreed in the same session but is recorded nowhere else: a
family for each row of the `results` table, so the explorer and `analyse`
can filter or subgroup results by model family, not only count papers.
Today the table's `model` column holds only the paper's own label for the
system. The 2026-10-27 `tabulate` run (`tabulate-run-20261027.log`) re-sent
every result and recorded 4305963 input and 3823832 output tokens, which is
$23.43 at Sonnet 5 Batch rates ($1 in, $5 out per million). That sets the
estimate for a full re-send at about $23 to $30.
<!-- doc-counts: accept-end -->

Cause: model families exist only at paper level, and a paper often reports
several models, so a paper's families cannot be pushed down to its rows.

Fix direction, with a provider choice and cost confirmation before any run:

- **Option A:** add a `model_family` column to the `results` table in
  `config.py`, taking the families in `vocabularies/model_architecture.json`,
  and re-send `tabulate`. Changing the prompt re-sends every result.
- **Option B (unconfirmed, cheaper):** first try a `categories` vocabulary
  bound to the `model` column with `normalise`, which costs cents. This may
  fail on labels that name no system, such as "Ours".

Rehearse on an APFS clone either way, then re-run `analyse`, `explore` and
`report`.
