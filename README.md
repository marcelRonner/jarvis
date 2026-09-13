Meet Jarvis, the Business Analysis context and requirements engineering agent. 

This is an educational example. 

Details about how to build it for your own purpose (in < than 1 hour) and insights about where and how to run it can be experienced in the
[certificate of advanced studies in Business Analysis and Methods](https://www.zhaw.ch/de/sml/weiterbildung/detail/kurs/cas-business-analysis-and-methods) at the [ZHAW School of Management and Law](https://www.zhaw.ch/en/university). 

See you there! 🙋‍♂️

![AI Agents in 2026 - Trends you can't ignore](image.png)

---

## Where to start

| You want to… | Read |
|---|---|
| see the result | the documentation site — <https://www.wlrm.ch/jarvis/site/> |
| understand how the parts work together, in plain language | the landing page — <https://www.wlrm.ch/jarvis/> (`index.html`) |
| get oriented in the documentation, and see how its artifacts interlink | the documentation home — [`content/_index.md`](content/_index.md) |
| set the repository up, build it, deploy it, or change how it works | this README |
| know exactly what the agent is told | [`AGENTS.md`](AGENTS.md), [`.claude/rules/`](.claude/rules/), [`.claude/skills/`](.claude/skills/) |

## What is in here

The requirements documentation of an ATM example system, written and kept consistent by Jarvis, an
agent that runs in GitHub Copilot and Claude Code from the same instruction files, and published as
a Hugo site. The documentation is an [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
(OKF) v0.2 bundle, and follows the [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern: an agent compiles changes into linked, maintained pages, and a person approves them.

```
content/                  the documentation — the OKF bundle and the Hugo content directory
  _index.md               home page: what this is, the artifact list, how the artifacts interlink
  domain_model/           domainModel.md + .puml, and entities/ — one page per class
  business_process/       businessProcess.md, with an embedded Mermaid flowchart
  use_case/               useCaseDiagram, actorDescriptions, actors/, one folder per use case (.md + .puml)
  state_chart/            one state chart per entity with a status enum (.md + .puml)
  epics/                  the story map, and user_stories/ — one file per story
  change_log/             changeLog.md — every version, every artifact touched
  sources/                change requests, one per version, cited by the artifacts they changed
  log.md                  GENERATED — the OKF log, from the change log
AGENTS.md                 the always-on contract: identity, must-rules, frontmatter, checklist
CLAUDE.md                 one line, importing AGENTS.md for Claude Code
.claude/rules/            the conventions for each artifact type, loaded only for its folder
.claude/skills/           the operations: change-request, and okf-check with its 41-check register
.github/instructions/     GENERATED — the rules in Copilot's dialect
.github/prompts/          GENERATED — typed doors, so /change-request and /okf-check work in Copilot
.github/workflows/        deploy-docs.yml — build and FTP deploy on every push to main
schema.yml                the artifact types, and the metadata each type must carry
index.html                the landing page for students; its embedded instructions are GENERATED
hugo.yaml                 the site build: Docsy as a Hugo module, base URL, markup, Kroki
layouts/                  five theme overrides — each explains itself in a comment
assets/scss/              the version-marker styles and the diagram styles
scripts/                  checks, generator, verify command, acceptance tests
Makefile                  every command below
go.mod, go.sum            the Docsy module, pinned
package.json, packages/   Dart Sass and PostCSS, and Docsy's own npm dependencies (hugo mod npm pack)
requirements.txt          PyYAML, for the scripts
```

## Setting it up

| Tool | Version | Why |
|---|---|---|
| [Hugo](https://gohugo.io/installation/) **extended** | 0.166.0 (CI), at least 0.160.1 | builds the site |
| [Go](https://go.dev/dl/) | as in `go.mod` (1.27) | Hugo fetches the Docsy theme as a Hugo module |
| [Node.js](https://nodejs.org/) | current LTS | Dart Sass and PostCSS compile Docsy's stylesheets |
| Python | 3.13 | the checks, the generator and the tests (PyYAML) |
| network access to [kroki.io](https://kroki.io) | — | PlantUML diagrams render at build time |

```sh
git clone https://github.com/marcelRonner/jarvis.git && cd jarvis
npm install                       # Dart Sass, PostCSS, Bootstrap, Font Awesome
pip install -r requirements.txt   # PyYAML — a virtualenv is fine
make build                        # the same checks and build CI runs
make serve                        # http://localhost:1313/jarvis/site/
```

## Commands

| Command | What it does |
|---|---|
| `make serve` | Live-reload site at <http://localhost:1313/jarvis/site/>. Offline, a diagram shows as a link to its `.puml` source |
| `make generate` | Regenerate everything that restates something written elsewhere: `.github/instructions/`, `.github/prompts/`, the type table in `AGENTS.md`, the instructions embedded in `index.html`, and `content/log.md` |
| `make lint` | `make generate`, then check the documentation (codes below). `STRICT=1` makes warnings fail |
| `make test` | The OKF consumer acceptance tests — against the Python reader and a real Hugo build — and the script tests |
| `make build` | What CI runs: fail on a stale generated file, a lint error or a failing test, then `hugo --minify --panicOnWarning` into `site/` — which fails on a broken link or a diagram that did not render |
| `make stage` | `make build`, then assemble `deploy/` exactly as the server receives it |
| `make verify PAGES="content/a.md content/b.md" [WHO=owner]` | Record **your** approval of artifacts as an OKF `verified` event. Run by a person, never by the agent |
| `make clean` | Remove `site/` and `deploy/` |

## How a change is made

1. Ask Jarvis for the change — in Copilot or Claude Code, typed as `/change-request` or not.
2. Jarvis follows [`.claude/skills/change-request/SKILL.md`](.claude/skills/change-request/SKILL.md):
   analyse, clarify, impact summary, then write the change request to
   `content/sources/cr_{major}_{minor}.md`.
3. Jarvis updates the artifacts from the domain model outward, drafts user stories for any
   functional change, adds a version to the change log, stamps `generated` and `sources` on every
   artifact it touched, and runs `make generate` and `make build`.
4. You review and approve, and record the approval with `make verify PAGES="…"`.
5. Merge to `main`; CI builds and deploys.

## The documentation model

**Artifact types.** Every Markdown file in `content/` has one `type`, declared in
[`schema.yml`](schema.yml) with where it lives, which rules file governs it, and which metadata it
must carry. The table in `AGENTS.md` is generated from it. Adding a type means declaring it there,
writing `.claude/rules/<type>.md` with a `paths:` glob, adding a row to the routing table in
`AGENTS.md`, and running `make generate`.

**Frontmatter.** Every file carries `title`, `type` and `description`; artifacts also carry
`linkTitle` (the sidebar label), `weight` (the sidebar position), `tags` (the domain entities it
names, plus release and KANO class on a user story), `sources` (what it derives from, as
bundle-absolute paths with kebab-case ids) and `generated` (`jarvis/1.0`, and when). `verified` is
added only by `make verify`. The full contract is in [`AGENTS.md`](AGENTS.md).

**Derivation.** The artifacts form a chain — domain model → business process → use cases → state
charts and story map → user stories → change log — recorded in each artifact's `sources:` and
explained, with its join keys and review rules, on the [documentation home](content/_index.md).
Traceability references in the text ("Corresponds to **Business Process steps 4a.1 – 4a.7**") cite
their source with a footnote keyed to the source id.

**Versions.** `content/change_log/changeLog.md` is the only place a version is written:
`## v{X.Y} – {Title} ({YYYY-MM-DD})`, a summary sentence, and a row per artifact touched.
`make generate` restates it as `content/log.md` in OKF §9 form. Inline change markers use blockquote
alerts (`> [!NOTE] v1.4 – Added …`) and block attributes (`{.v-new}`), styled in
`assets/scss/_styles_project.scss`.

## The instructions

Jarvis runs on the same files in Claude Code and GitHub Copilot:

- **`AGENTS.md`** is read on every request — Copilot reads it natively, Claude Code through the
  one-line `CLAUDE.md`.
- **`.claude/rules/<type>.md`** holds the conventions for one artifact type, with a `paths:` glob so
  it loads only when that folder is touched. A rule attaches only after a file in its folder has been
  read, so `AGENTS.md` carries a routing table telling the agent which rules to open before a first
  write. Copilot reads project rules only from `.github/instructions/`, so `make generate` restates
  each one there, as `applyTo:`.
- **`.claude/skills/`** holds the operations: `change-request`, the protocol for changing the
  documentation, and `okf-check`, which assesses the bundle against the check register in
  `okf-v0-2-checks.md`. Both tools discover skills there; the generated `.github/prompts/*.prompt.md`
  files exist only so `/change-request` and `/okf-check` can be typed in Copilot.
- **`index.html`** shows the same instruction files to students, regenerated into the page on every
  `make generate`.

Edit the source files, never the generated ones — `make build` fails if they have drifted.

## Open Knowledge Format

`content/` is an OKF v0.2 bundle, so any agent that reads OKF can consume the documentation straight
from the repository. `/okf-check` assesses it against the 41 numbered checks of the register. The
conformance and quality rules are enforced by `make lint`:

| Code | Fails on |
|---|---|
| E1 | missing or unparseable frontmatter (OKF criterion 1) |
| E2 | empty `type`, or one not declared in `schema.yml` (OKF criterion 2) |
| E3 | any `index.md` (reserved, and a Hugo leaf bundle), or a `log.md` breaking OKF §9 (criterion 3) |
| E4 | missing `title` or `description`, or a multi-line description |
| E5 | a relative link or image pointing at nothing |
| E6 | malformed `sources`: no `resource` or `id`, duplicate ids, a missing resource, a footnote naming no source |
| E7 | malformed `generated` or `verified`: wrong actor form, datetime without a UTC offset |
| E8 | `tags` that are not lowercase-kebab strings |
| W1 | a page whose first `# Heading` differs from its `title` |
| W2 | a `.puml` diagram nothing embeds or links |
| W3 | an artifact missing metadata its type requires in `schema.yml` |

`scripts/test_okf_consumer.py` proves the consumer side: the Python reader in `scripts/okflib.py` and
a real Hugo build both accept an unknown type, an unknown key, a broken link, a concept with only a
type, and a bundle without `index.md`.

## How the site is built

Hugo renders `content/` with [Docsy](https://www.docsy.dev/) 0.17, pulled in as a Hugo module, into
`site/`. `baseURL` is `https://www.wlrm.ch/jarvis/site/`, because Hugo writes root-relative URLs.
There is no navigation list: the sidebar is the folder tree, ordered by `weight`, labelled by
`linkTitle`, with each folder's title and description in its `_index.md`.

The overrides in `layouts/`, each documented in place:

| File | Why |
|---|---|
| `_markup/render-link.html` | Resolves relative `.md` links, links to folders, and links to other files such as `.puml` sources, to their published URLs; warns on anything that resolves to nothing |
| `_markup/render-image.html` | Renders `![…](diagram.puml)` through Kroki at build time and publishes the SVG |
| `_partials/sidebar-args.html` | Roots the sidebar at the home page, so every artifact folder is reachable from every page |
| `_td-content.html`, `list.html` | Stop the page's own `# Heading` rendering twice under Docsy's title |

`hugo.yaml` also remounts Docsy's `layouts/docs` at the layout root: every page has an OKF `type`,
which Hugo would otherwise use to look for layouts and fall through to a page without the sidebar.
Re-check the mounts against Docsy's own `hugo.yaml` after `hugo mod get -u`.

## Diagrams

Business processes are Mermaid, embedded in the Markdown and drawn in the browser by Docsy.
Everything else is PlantUML, kept as `.puml` files beside the page, and embedded by pointing an image
at the source:

```markdown
![Activity Diagram – Withdraw Cash](withdrawCash.puml)
```

There is no PlantUML installation and no generated SVG in the repository. During the build,
`render-image.html` posts each `.puml` file to Kroki and publishes the SVG it returns — a diagram
cannot drift from its source, and a PlantUML syntax error fails the build. Hugo caches each response
by its source. To keep diagram source off the public service, run Kroki yourself
(`docker run -p 8000:8000 yuzutech/kroki`) and set `HUGO_PARAMS_KROKI_URL=http://localhost:8000`.
On GitHub, a page shows a broken image where its diagram would be; the site renders it.

## Deploy

[`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml) runs on every push to
`main`, and on demand from the Actions tab:

1. set up Go, Node LTS (with `npm ci`), Python 3.13 (with `requirements.txt`) and Hugo extended 0.166.0;
2. `make stage` — generated files current, lint, tests, Hugo build, then `deploy/`;
3. upload `deploy/` with [FTP-Deploy-Action](https://github.com/SamKirkland/FTP-Deploy-Action).

It needs three repository secrets: `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`. `deploy/` holds
exactly what the server serves — `index.html` at <https://www.wlrm.ch/jarvis/>, the documentation
under `site/` at <https://www.wlrm.ch/jarvis/site/>. The action keeps a sync-state file on the
server and deletes files it uploaded before that are no longer in `deploy/`. Uncomment `server-dir`
in the workflow if the target folder changes.

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| `npm dependencies are out of sync` | `package.json` changed without Hugo's pack step: run `hugo mod npm pack`, then `npm install` |
| Sass errors, or no stylesheet | Dart Sass is missing from `PATH`: run `npm install`, and build through `make` — it puts `node_modules/.bin` first |
| `render-image: … could not be rendered by https://kroki.io/…` | No network, or a PlantUML syntax error in that file. `make serve` falls back to a link; `make build` fails on purpose |
| `generate: STALE — run make generate` | A generated file was edited by hand, or its source changed: run `make generate` and commit the result |
| `render-link: … does not resolve` | A relative link inside `content/` points at nothing — fix the path; `make lint` reports it with a line number |
| A page has no sidebar | Its `type` is not reaching Docsy's docs layout: check the `layouts/docs` mount in `hugo.yaml` — `make test` catches this |
