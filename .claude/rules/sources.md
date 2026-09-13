---
paths:
  - content/sources/**
---

# Source Conventions

`content/sources/` holds the material the documentation's changes derive from, in two kinds:

- **Change requests** — every change applied through the change-request protocol is written down
  here first, and every artifact it creates or restructures cites it in `sources:`.
- **Assessments** — every run of `/okf-check` is filed here. An assessment changes nothing; it is
  the evidence a later change request cites for what it fixes.

Both are written once and never rewritten, so the folder reads as a history: what was found, what
was asked, what was decided.

## Files to produce
- `cr_{major}_{minor}.md` — one change request per version (e.g. `cr_1_3.md` for v1.3)
  - Auto-numbered: `CR-{major}.{minor}`, the version the change is released as
- `okf_assessment_{yyyy}_{mm}_{dd}.md` — one Open Knowledge Format assessment per run, named for the
  day it ran (e.g. `okf_assessment_2026_09_13.md`). A second run on the same day adds `_2`.
- `weight` continues the folder's sequence across both kinds, so the sidebar lists them in the order
  they were written.

## Change request — Markdown structure
```
# CR-{X.Y} – {Title}
## Request           → Who asked, when, and what — in the requester's terms
## Analysis          → The change restated, and which artifacts it touches (protocol step 1)
## Decisions         → What was clarified (step 2), and every assumption, marked **Assumption:**
## Impact Summary    → Table: Artifact | Impact (new / changed / none) | Details (step 3)
## User Stories      → Links to the stories drafted in step 5, or "None" with the reason
## Acceptance        → How to tell the change is done
## Status            → Proposed · Implemented in v{X.Y} on {date} · Approved (recorded with `make verify`)
```

## Change request — content rules
- A change request records a decision; it is **not rewritten** once implemented. If the change turns
  out wrong, the next change request says so.
- Use domain model entity names exactly, as everywhere else.
- Every assumption is written down and marked **Assumption:** — an unstated assumption is exactly
  what the Must-rule "Ask, don't assume" exists to prevent.
- The change log's version entry links its change request, and the change request links the change
  log.
- A change request that fixes assessment findings cites the assessment in `sources:`
  (`id: okf-assessment-2026-09-13`) and footnotes each check ID it addresses with that id.

## Assessment — frontmatter
- `title: "OKF v0.2 Conformance Assessment – {YYYY-MM-DD}"`, `linkTitle: "OKF Assessment {YYYY-MM-DD}"`
- `type: assessment`
- `description` — the result in one sentence: conformant or not, and the count per status. It is the
  line `content/log.md` shows for the run, so a reader of the log learns the result without opening
  the page.
- `generated` stamped when the run is filed. No `tags`: an assessment names no domain entity.

## Assessment — Markdown structure

A reader must learn what was checked without opening the register, and see the verdict before the
detail. So every check row carries its **name** from the register next to its ID, and the rows are
grouped: the three checks that decide conformance first, then one table per family.

```
# OKF v0.2 Conformance Assessment – {YYYY-MM-DD}
{One sentence: what was assessed, on which day, with what result.}

## Scope             → Two-column table with rows Bundle, Commit, Specification, Register, Validation
## Result            → Conformant or not, on the three mandatory checks alone. Then a table:
                       Family | meets | partial | not adopted | deviates | n/a, one row per family
                       in the order of the sections below, and a Total row
## Needs attention   → One bullet per `partial` or `deviates` check: ID, name, and the remediation in
                       one line. "Nothing." if there is none
## Mandatory checks  → OKF-CNF-01, OKF-CNF-02, OKF-CNF-03 — the §11 conformance criteria
## Bundle structure  → OKF-BUN-*
## Concept documents → OKF-CPT-*
## Provenance        → OKF-SRC-*
## Trust             → OKF-TRU-*
## Lifecycle         → OKF-LIF-*
## Cross-linking and paths → OKF-LNK-*
## Reserved files    → OKF-RSV-*
## Attested computations → OKF-CMP-*
## Consumer floor    → OKF-CNF-04
## Versioning        → OKF-VER-*
## Register notes    → Only when the run changed the register, or found something it has no ID for
```

Every check section is one table, with the rows in register order:

```
| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-BUN-01`](https://…/SPEC.md#3-bundle-structure) | Markdown directory tree | meets | … | |
```

- **Check** is the ID, linked to the clause of the specification the register links.
- **Name** is copied verbatim from the register.
- **Status** is one of the register's five words, and nothing else — decoration breaks the diff.
- **Remediation** is empty for `meets`, and precise for everything else.
- Every register ID appears exactly once in the page.

## Assessment — content rules
- **Never rewritten.** The next run is a new page; two pages are compared check by check, which is
  what the register's permanent IDs are for. A finding that turns out wrong is corrected by the next
  run, which says so under *Register notes*.
- **Not a change.** Filing an assessment gets no version and no change log entry. `make generate`
  lists it in `content/log.md` under the day it ran.
- **Links** to the specification use its URL; links to the register use the repository path in
  backticks, since the register lives outside the bundle.

## Approval
- `generated:` is stamped when Jarvis writes the page. `verified:` is recorded by the approver with
  `make verify`, never by Jarvis.
