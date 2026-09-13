---
title: "OKF v0.2 Conformance Assessment – 2026-09-13"
linkTitle: "OKF Assessment 2026-09-13"
type: assessment
description: "Conformant with OKF v0.2 on all three mandatory checks; of the 41 checks, 26 meets, 1 partial, 5 not adopted, 1 deviates, 8 n/a."
weight: 4
generated:
  by: jarvis/1.0
  at: 2026-09-13T10:00:11Z
---

# OKF v0.2 Conformance Assessment – 2026-09-13

The documentation in `content/`, as released in v1.5, assessed on 2026-09-13 against all 41 checks of
the Open Knowledge Format (OKF) v0.2 check register: **conformant**.

## Scope

| | |
|---|---|
| **Bundle** | `content/` — 58 Markdown files and 8 `.puml` diagram sources. The repository around it (scripts, instructions, the built site) is outside the bundle. |
| **Commit** | Branch `okf-assessments` at v1.5, based on `main` `d7eb052` |
| **Specification** | [OKF SPEC.md v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md), read at that URL on 2026-09-13 |
| **Register** | `.claude/skills/okf-check/okf-v0-2-checks.md`, version 2026-09-13 — all 41 IDs |
| **Validation** | `make lint` → 0 errors, 0 warnings, 58 files · `make build` → 18 tests OK, none skipped; Hugo 71 pages with `--panicOnWarning`, no warnings |

## Result

**Conformant with OKF v0.2 as of 2026-09-13**, on the three mandatory checks `OKF-CNF-01`,
`OKF-CNF-02` and `OKF-CNF-03` alone.

| Family | meets | partial | not adopted | deviates | n/a |
|---|---|---|---|---|---|
| Mandatory checks | 3 | 0 | 0 | 0 | 0 |
| Bundle structure | 2 | 0 | 0 | 0 | 0 |
| Concept documents | 9 | 0 | 0 | 0 | 2 |
| Provenance | 2 | 1 | 2 | 0 | 1 |
| Trust | 4 | 0 | 1 | 0 | 0 |
| Lifecycle | 1 | 0 | 1 | 0 | 0 |
| Cross-linking and paths | 3 | 0 | 0 | 1 | 1 |
| Reserved files | 1 | 0 | 0 | 0 | 1 |
| Attested computations | 0 | 0 | 0 | 0 | 2 |
| Consumer floor | 1 | 0 | 0 | 0 | 0 |
| Versioning | 0 | 0 | 1 | 0 | 1 |
| **Total** | **26** | **1** | **5** | **1** | **8** |

**Compared with the first run.** The first assessment, on 2026-09-12, was reported in the chat and
never filed; it found the documentation conformant but meeting only 12 checks
(12 meets, 6 partial, 8 not adopted, 1 deviates, 14 n/a). [CR-1.3](cr_1_3.md) acted on it. 17 checks have
changed status since:

- `OKF-CPT-02` One concept per file: partial → meets
- `OKF-CPT-05` Unknown type tolerated: partial → meets
- `OKF-CPT-09` `tags` is a list: not adopted → meets
- `OKF-CPT-10` Extra keys kept: partial → meets
- `OKF-SRC-01` Every source has `resource`: not adopted → meets
- `OKF-SRC-02` Footnotes cite source IDs: not adopted → partial
- `OKF-SRC-03` Source titles: n/a → not adopted
- `OKF-SRC-04` Credibility signals: n/a → not adopted
- `OKF-SRC-06` Lineage through links: partial → meets
- `OKF-TRU-01` `generated` well-formed: not adopted → meets
- `OKF-TRU-02` `verified` events: not adopted → meets
- `OKF-TRU-03` Bare `verified` read as a list: n/a → meets
- `OKF-TRU-05` Actor convention: n/a → meets
- `OKF-LNK-03` Broken links tolerated: partial → meets
- `OKF-LNK-04` Path-valued fields resolve: n/a → meets
- `OKF-RSV-02` `log.md` structure: n/a → meets
- `OKF-CNF-04` The consumer floor: partial → meets

## Needs attention

- `OKF-SRC-02` Footnotes cite source IDs — **partial.** Add a footnote labelled `business-process` to the "Corresponds to" sentence on `use_case/actors/customer.md`, `atmSystem.md` and `bankBackend.md`, with the footnote definition at the end of each. It edits artifacts, so it is a change request.
- `OKF-LNK-02` Bundle-absolute links preferred — **deviates.** Add the reason to the relative-paths rule in `AGENTS.md`, so the deviation is a recorded decision rather than an unexplained habit.

## Mandatory checks

The three §11 conformance criteria. Together they decide whether the bundle conforms; nothing else does.

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-CNF-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#11-conformance) | Parseable frontmatter everywhere | meets | All 58 Markdown files in `content/` open with a YAML frontmatter block that parses. `make lint` walks every `.md` file in the tree, not only the types it knows, and fails with E1 on one that does not parse. |  |
| [`OKF-CNF-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#11-conformance) | `type` everywhere | meets | `type` is non-empty on 58 of 58, generated `content/log.md` included. E2 fails on an empty or undeclared type. |  |
| [`OKF-CNF-03`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#11-conformance) | Reserved files well-formed | meets | The one reserved file present, `content/log.md`, follows §9 (`OKF-RSV-02`). There is no `index.md`, so §8 has nothing to apply to. |  |

## Bundle structure

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-BUN-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#3-bundle-structure) | Markdown directory tree | meets | `content/` is a directory tree of 58 Markdown files, one folder per artifact type, plus 8 `.puml` diagram sources that pages embed. |  |
| [`OKF-BUN-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#31-reserved-filenames) | Reserved names hold no concepts | meets | The only reserved name in use is `content/log.md`, and it is the history, generated from the change log and the assessments. No `index.md` exists; E3 rejects one anywhere, and a `log.md` anywhere but the root. |  |

## Concept documents

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-CPT-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#4-concept-documents) | Frontmatter, then body | meets | 58 of 58 parse as UTF-8 with a `---`-delimited frontmatter block followed by a body (E1). |  |
| [`OKF-CPT-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#2-terminology) | One concept per file | meets | One concept per file since v1.3: each of the 11 entities and 3 actors has its own page, and no link in the bundle points at an anchor inside another page. The story map keeps its 5 epics as columns, each realising one use case that has its own page — the map is one concept by design. |  |
| [`OKF-CPT-03`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#41-frontmatter) | Non-empty `type` | meets | Non-empty `type` on 58 of 58 (see `OKF-CNF-02`). |  |
| [`OKF-CPT-04`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#41-frontmatter) | Self-explanatory types | meets | 16 values in use — `entity`, `use-case`, `user-story`, `change-request`, `assessment`, … — each declared in `schema.yml` with a one-line `holds`, and each naming what the file is. E2 rejects an undeclared value. |  |
| [`OKF-CPT-05`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#41-frontmatter) | Unknown type tolerated | meets | Two consumers, two tests in `scripts/test_okf_consumer.py`: the Python reader (`test_unknown_type_is_consumed_and_unknown_key_kept`) and a real Hugo build (`test_unknown_type_renders_with_the_site_chrome`) both load `type: Future Concept`. |  |
| [`OKF-CPT-06`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#41-frontmatter) | `title` present | meets | `title` on 58 of 58; E4 requires it, W1 warns when it differs from the page's `# Heading`. |  |
| [`OKF-CPT-07`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#41-frontmatter) | One-sentence `description` | meets | `description` on 58 of 58, each a single line; E4 fails on a missing or multi-line one. |  |
| [`OKF-CPT-08`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#41-frontmatter) | `resource` on asset concepts | n/a | No concept describes an external asset with a URI of its own: the artifacts are the documentation itself. |  |
| [`OKF-CPT-09`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#41-frontmatter) | `tags` is a list | meets | `tags` on all 41 artifacts whose type requires them, each a YAML list of lowercase-kebab strings — the domain entities named, plus release row and KANO class on user stories. E8 validates the shape. |  |
| [`OKF-CPT-10`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#41-frontmatter) | Extra keys kept | meets | Producer keys `linkTitle` and `weight` are in use. Both consumers keep an unknown key: the Python reader returns `custom_extension` (`test_unknown_type_is_consumed_and_unknown_key_kept`), and Hugo builds the page carrying it. |  |
| [`OKF-CPT-11`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#42-body) | Conventional body headings | n/a | No concept has an asset schema, usage examples or a computation. An entity's `## Attributes` table describes a business concept, not an asset. |  |

## Provenance

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-SRC-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#51-provenance-sources) | Every source has `resource` | meets | 43 pages carry `sources`, 99 entries in all, every one a mapping with `id` and `resource`. E6 rejects a bare string, a missing `resource` and a resource that does not exist. |  |
| [`OKF-SRC-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#51-provenance-sources) | Footnotes cite source IDs | partial | 21 of 24 traceability references cite their source with a footnote labelled by its `sources[].id` — the use cases, the use-case diagram and all 16 user stories; E6 fails on a label that names no source. The 3 actor pages say "Corresponds to … in the Business Process" without one, though each lists `business-process` in `sources`. | Add a footnote labelled `business-process` to the "Corresponds to" sentence on `use_case/actors/customer.md`, `atmSystem.md` and `bankBackend.md`, with the footnote definition at the end of each. It edits artifacts, so it is a change request. |
| [`OKF-SRC-03`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#51-provenance-sources) | Source titles | not adopted | No `sources` entry has a `title`; ids such as `business-process` and `cr-1-4` name their source well enough. | Add `title` only where an id stops describing its source. |
| [`OKF-SRC-04`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#51-provenance-sources) | Credibility signals | not adopted | No `author`, `usage_count` or `last_modified` on any entry. | Record a signal only if it is measured. An invented one is worse than none. |
| [`OKF-SRC-05`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#51-provenance-sources) | `usage_window` frames usage counts | n/a | No `usage_count` exists to frame. |  |
| [`OKF-SRC-06`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#51-provenance-sources) | Lineage through links | meets | Every `sources` resource is a bundle path to another concept, so the derivation chain domain model → business process → use cases → state charts and story map → user stories is walkable from frontmatter alone, and each artifact a change request restructured cites it. |  |

## Trust

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-TRU-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#52-trust-generated-and-verified) | `generated` well-formed | meets | `generated` on all 47 pages whose type requires it: `by: jarvis/1.0`, `at` an explicit-UTC datetime stamped when the body last changed. E7 validates both. Sections and the log carry none. |  |
| [`OKF-TRU-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#52-trust-generated-and-verified) | `verified` events | meets | 55 `verified` events, each `by: human:owner` at a UTC datetime, recorded with `make verify` when the owner approved every page on 2026-09-13; E7 validates them. On the 18 pages v1.5 changed, that approval predates `generated.at`, which is the honest state until v1.5 is approved. |  |
| [`OKF-TRU-03`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#52-trust-generated-and-verified) | Bare `verified` read as a list | meets | Python reader: `Page.verified_events()` reads a bare mapping as one event, proven by `test_bare_verified_mapping_is_one_event`. The linter and `make verify` use the same function; `test_a_bare_mapping_becomes_a_list_and_survives` covers the writer. |  |
| [`OKF-TRU-04`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#53-trust-tiers) | Trust tiers derived | not adopted | Neither consumer derives or shows a trust tier. The site does not tell a reader whether a page is approved. | If readers need it, show the tier — and the latest approval — in the page footer, derived from `verified` in a layout partial. |
| [`OKF-TRU-05`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#7-actor-convention) | Actor convention | meets | Two actor values in the bundle: `jarvis/1.0` (`<producer>/<version>`) and `human:owner`. E7 enforces the convention on `generated.by` and `verified[].by`; `test_first_approval_is_a_valid_okf_event` checks `make verify` writes the `human:` form. |  |

## Lifecycle

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-LIF-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#54-lifecycle-status) | `status` values | meets | No page sets `status`, so every page reads as `stable`, which is true of released documentation. |  |
| [`OKF-LIF-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#55-lifecycle-stale_after) | `stale_after` is an instant | not adopted | No `stale_after`. Requirements do not expire on a date; they change through change requests. | Set it only on an artifact with a real review date. |

## Cross-linking and paths

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-LNK-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#61-links-between-concepts) | Standard Markdown links | meets | 258 standard relative Markdown links and 7 external URLs. None leaves the bundle. |  |
| [`OKF-LNK-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#61-links-between-concepts) | Bundle-absolute links preferred | deviates | Body links are relative, while `sources` resources are bundle-absolute. What is gained: a relative link works when the Markdown is browsed on GitHub, where `/use_case/…` would resolve from the repository root and fail. `AGENTS.md` prescribes relative links but does not say why. | Add the reason to the relative-paths rule in `AGENTS.md`, so the deviation is a recorded decision rather than an unexplained habit. |
| [`OKF-LNK-03`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#61-links-between-concepts) | Broken links tolerated | meets | Both consumers: the Python reader keeps `missing.md` as a link (`test_broken_link_is_read_without_rejection`) and Hugo passes it through (`test_broken_link_is_passed_through`). `make build` failing on a broken link is producer policy, not consumer rejection. |  |
| [`OKF-LNK-04`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#62-path-valued-fields) | Path-valued fields resolve | meets | All 99 `sources[].resource` values are bundle-absolute and resolve; E6 checks each one exists. No other path-valued field is used. |  |
| [`OKF-LNK-05`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#63-the-references-convention) | `references/` for external material | n/a | No external material, run instructions or code are mirrored into the bundle. |  |

## Reserved files

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-RSV-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#8-index-files) | `index.md` structure | n/a | No `index.md` exists; the owner excluded a generated root index in CR-1.3. `content/_index.md` is a concept of type `overview` and is checked as one. |  |
| [`OKF-RSV-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#9-log-files) | `log.md` structure | meets | `content/log.md` groups list entries under `## YYYY-MM-DD` headings, newest first — releases from the change log and, from v1.5, assessments. E3 checks heading form, order and list items; `scripts/test_generate.py` tests the generator. |  |

## Attested computations

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-CMP-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#102-contract-fields) | Attested computation contract | n/a | No concept has `type: Attested Computation`. |  |
| [`OKF-CMP-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#11-conformance) | Deterministic attester | n/a | No computations exist. |  |

## Consumer floor

What every consumer must tolerate — the promise that lets a bundle be partial and still useful.

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-CNF-04`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#11-conformance) | The consumer floor | meets | One test per clause against both consumers in `scripts/test_okf_consumer.py`: missing optional fields (`test_missing_optional_fields_are_not_an_error`, `test_concept_with_only_a_type_renders`), unknown type and unknown key (`OKF-CPT-05`, `OKF-CPT-10`), broken link (`OKF-LNK-03`), and a Hugo bundle without any `index.md` that builds (`test_the_bundle_builds`). |  |

## Versioning

| Check | Name | Status | Evidence | Remediation |
|---|---|---|---|---|
| [`OKF-VER-01`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#12-versioning) | `okf_version` declared | not adopted | No root `index.md` to declare `okf_version` in, by the owner's decision in CR-1.3. | Revisit together with `OKF-RSV-01` if an OKF consumer needs the declaration. |
| [`OKF-VER-02`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md#12-versioning) | Unknown version consumed best-effort | n/a | No consumer in scope reads `okf_version`. |  |

## Register notes

- **Names added.** This is the first run against register version 2026-09-13, which gives every check
  a short name. No ID and no check wording changed, so every row compares with the first run.
- **Diagrams.** The 8 `.puml` files are non-Markdown files inside the bundle. OKF says nothing about
  them and a consumer can read their text, so no check is proposed.
