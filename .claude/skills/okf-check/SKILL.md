---
name: okf-check
description: Assess content/ against every check in the Open Knowledge Format v0.2 register, file the result as an assessment in content/sources/, and report the conformance result.
---

# OKF check

Assess how far the documentation in `content/` conforms to the Open Knowledge Format (OKF) v0.2, and
file the result as an assessment in `content/sources/`. **Read-only for every artifact** — the one
file a run writes is its own assessment. Fixing a finding in the documentation is a change request,
and that change request cites the assessment.

Work through [okf-v0-2-checks.md](okf-v0-2-checks.md) — the register of numbered checks, each with a
short name and a link to the clause of the specification it comes from. Read it first. It also fixes
the vocabulary: the five statuses an assessment may use, and what `REQUIRED` means as against
everything else.

Do not restate the checks from memory and do not invent a numbering of your own. The register's IDs
are the join between one assessment and the next, and a re-run that renumbers them destroys the only
thing that makes two assessments comparable.

> Assess the bundle the user names — `content/` unless they say otherwise — against every check in
> `.claude/skills/okf-check/okf-v0-2-checks.md`. Read the normative specification at the URL the
> register names. Cover every ID in the register exactly once, and add no rows of your own — if
> something needs checking that the register has no ID for, say so under *Register notes* and
> propose the ID. Use only the register's five statuses. Do not record `meets` against a consumer
> requirement without naming the consumer and the acceptance test that proves it; `partial` is the
> honest status for a behaviour that is implemented but untested. Keep `not adopted` and `n/a` apart.
> Give a precise remediation for everything that is not `meets`, and none for what is. State the §11
> result — conformant or not, on the strength of the three mandatory checks alone. Run `make lint`
> and `make build` before filing, and record their results under *Scope*.

## Filing the result

1. Read `.claude/rules/sources.md` and write the assessment exactly as it describes: named for the day
   of the run, the verdict and the counts first, then the mandatory checks, then one table per family,
   every row carrying the check's name next to its ID.
2. Never edit an earlier assessment. Compare against the newest one instead, and name every check
   whose status changed under *Result*.
3. Run `make generate`, which lists the run in `content/log.md`, then `make build`.
4. Report the verdict, the counts and the *Needs attention* list in the chat, with a link to the file.
   The approval of the page is the user's, with `make verify` — never run it.

If the user asks for the result in the chat only, do not file it.

If a check turns out to be wrongly worded, or the specification gains a clause the register misses,
change the register and say so in the assessment. Adding a check is normal; renumbering is not.
