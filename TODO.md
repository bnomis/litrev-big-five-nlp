# Big-five review to do

Open work on this review. Defects in LitRev itself are filed in LitRev's own
`TODO.md`.

## Re-render the report after the 2026-10-29 report changes and the model families

Found 2026-10-30 by LitRev's `/todo-review`. `output/report/report.md` was
last rendered 2026-10-29 05:54. LitRev commit `fb5ab4c8` (2026-10-29,
"fix(report): resolve analysis rows to study keys") says "The big-five
review's report needs re-rendering to pick this up", and later report
changes landed after the render too: the risk-of-bias admission and the
corrections digest in Methods, and the placement of a not-fitted level's
reason. Commit `ec99897` (2026-10-30) then coded `model_architecture` into
model families, which changes the report's frequencies and normalisation
sections. The other half of that promise, `summary=True` in
`templates/report.md.j2`, is already in place.

Fix direction: back up `output/report`, re-run `litrev report` (no LLM
call), and review the diff against the backup before committing.
