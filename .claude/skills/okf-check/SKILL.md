---
name: okf-check
description: Assess content/ against every check in the Open Knowledge Format v0.2 register, with one finding per check ID, and report the conformance result.
---

# OKF check

Assess how far the documentation in `content/` conforms to the Open Knowledge Format (OKF) v0.2.
**Read-only** unless the user names a destination for the result — never change an artifact as part
of an assessment. Fixing a finding in the documentation is a change request.

Work through [okf-v0-2-checks.md](okf-v0-2-checks.md) — the register of numbered checks, each linked
to the clause of the specification it comes from. Read it first. It also fixes the vocabulary: the
five statuses an assessment may use, and what `REQUIRED` means as against everything else.

Do not restate the checks from memory and do not invent a numbering of your own. The register's IDs
are the join between one assessment and the next, and a re-run that renumbers them destroys the only
thing that makes two assessments comparable.

> Assess the bundle the user names — `content/` unless they say otherwise — against every check in
> `.claude/skills/okf-check/okf-v0-2-checks.md`. State the scope and the date. Read the normative
> specification at the URL the register names. Produce one table: check ID, status, evidence,
> remediation. Cover every ID in the register, in register order, and add no rows of your own — if
> something needs checking that the register has no ID for, say so under the table and propose the
> ID. Use only the register's five statuses. Do not record `meets` against a consumer requirement
> without naming the consumer and the acceptance test that proves it; `partial` is the honest status
> for a behaviour that is implemented but untested. Keep `not adopted` and `n/a` apart. Give a
> precise remediation for everything that is not `meets`, and none for what is. Then state the §11
> result — conformant or not, on the strength of the three REQUIRED checks alone — and run
> `make lint` and `make build` before reporting it.

Write the result to the destination the user names. If none is named, report it in the chat.

If a check turns out to be wrongly worded, or the specification gains a clause the register misses,
change the register and say so in the assessment. Adding a check is normal; renumbering is not.
