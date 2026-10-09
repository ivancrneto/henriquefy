# transform playbook

`transform` rewrites code in his style. The order is his method, not a lint list, and the
explanation of the diff is the deliverable. Every step cites the principle it applies.

## Order

1. **Check first.** Run `scripts/henriquefy.sh check <path> --json`, then the judgment pass
   (see SKILL.md). Sort findings by principle weight (`references/kb/rubric.md`).
2. **Fence the behavior before touching it** (execute-antes-de-ler). If the target has tests
   that cover it, run them and keep them green. If it has none, write characterization tests of
   the code as it is, warts included, using the project's runner; if there is no runner, add
   pytest under `tests/` and say so. Run the program when it is a program. Do not change a line
   of code before this step is green.
3. **One principle per change** (deixe-o-codigo-descansar, uma coisa de cada vez). Apply the
   highest-weight finding's fix, run the tests, then the next. Each change is small enough to
   describe in one sentence. Never commit, stage or branch unless asked; leave the working tree
   changed and say what a commit per principle would be.
4. **Explain the diff.** For each change: `path:line`, principle id, why in one sentence in his
   reasoning, citation (course, lesson, timestamp, or repo path and commit), and what the tests
   showed before and after.

## Stop rules

- **Public behavior stays.** A function that returns a boolean to its callers keeps returning
  a boolean; raising instead is a behavior change the caller did not ask for. Record it as a
  finding that remains, with the fix the caller would have to make.
- **Public names and signatures stay.** Renames and signature changes are proposals in the
  explanation, not edits.
- **Do not generalize** (nao-projete-a-generalizacao, deixe-o-codigo-descansar). No base
  classes, helpers or abstractions that the code did not ask for. If two things look alike,
  leave them alike.
- **Do not fix what is not a finding.** Style you dislike that no principle names stays.
- **Stop when the tests stop telling you anything.** If a change cannot be verified by a test
  that existed before it, undo it and say so.

## Evidence the run produces

- The test run before any change (green), the test run after each change (green).
- The `check` findings before and after, with the rule ids that disappeared and the ones that
  remain on purpose.
- The explanation, in the order the changes were made.
