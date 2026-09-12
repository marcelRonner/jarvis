Meet Jarvis, the Business Analysis context and requirements engineering agent. 

This is an educational example. 

Details about how to build it for your own purpose (in < than 1 hour) and insights about where and how to run it can be experienced in the
[certificate of advanced studies in Business Analysis and Methods](https://www.zhaw.ch/de/sml/weiterbildung/detail/kurs/cas-business-analysis-and-methods) at the [ZHAW School of Management and Law](https://www.zhaw.ch/en/university). 

See you there! 🙋‍♂️

![AI Agents in 2026 - Trends you can't ignore](image.png)

---

## What is in here

The requirements documentation of an ATM example system, maintained by Jarvis, and published at
<https://www.wlrm.ch/jarvis/site/>.

```
content/            the documentation — Markdown and PlantUML, one folder per artifact type
AGENTS.md           Jarvis: the always-on contract — identity, must-rules, frontmatter, checklist
CLAUDE.md           one line, importing AGENTS.md for Claude Code
.claude/rules/      the conventions for each artifact type, loaded only for its folder
.claude/skills/     the change-request protocol, typable as /change-request
.github/            GENERATED Copilot copies of the rules and the prompt door, plus the deploy workflow
schema.yml          the artifact types
index.html          the landing page; its embedded instructions are GENERATED
layouts/, assets/   the site's theme overrides — each explains itself in a comment
scripts/            the documentation checks and the instruction generator
hugo.yaml           the site build: Docsy as a Hugo module
```

## Working on it

One-time setup: [Hugo](https://gohugo.io/installation/) (extended), Go, Node and Python 3, then

```sh
npm install
pip install -r requirements.txt
```

| Command | What it does |
|---|---|
| `make serve` | Live-reload site at <http://localhost:1313/jarvis/site/> |
| `make lint` | Regenerate the instructions, then check frontmatter, Open Knowledge Format conformance and links |
| `make instructions` | Regenerate `.github/`, the type table in `AGENTS.md`, and the instructions in `index.html` |
| `make build` | Everything CI checks, then build `site/` — fails on a stale generated file, a broken link, or a diagram that did not render |
| `make stage` | `make build`, then assemble `deploy/` exactly as the server receives it |

Every push to `main` runs `make stage` in GitHub Actions and uploads `deploy/` over FTP: the landing
page at the top, the docs under `site/`.

## The instructions

Jarvis runs on the same files in Claude Code and GitHub Copilot:

- **`AGENTS.md`** is read on every request — Copilot reads it natively, Claude Code through the
  one-line `CLAUDE.md`.
- **`.claude/rules/<type>.md`** holds the conventions for one artifact type, with a `paths:` glob so
  it loads only when that folder is touched. Copilot reads project rules only from
  `.github/instructions/`, so `make instructions` restates each one there, as `applyTo:`.
- **`.claude/skills/change-request/`** is the change-request protocol. Both tools discover the skill
  from `.claude/skills/`; the generated `.github/prompts/change-request.prompt.md` is only there so
  `/change-request` can be typed in Copilot.

Edit the source files, never the generated ones — `make build` fails if they have drifted.

## The documentation is an Open Knowledge Format bundle

`content/` conforms to the [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
v0.2: every Markdown file carries parseable frontmatter with a non-empty `type`, and no file uses
the reserved names `index.md` or `log.md`. `make lint` enforces both, so any agent that reads OKF
can consume the documentation as it is, straight from the repository.

## Diagrams

Business processes are Mermaid, embedded in the Markdown and drawn in the browser. Everything else
is PlantUML, kept as `.puml` files beside the page, and embedded by pointing an image at the
source:

```markdown
![Activity Diagram – Withdraw Cash](withdrawCash.puml)
```

There is no PlantUML installation and no generated SVG in the repository. During the build,
`layouts/_markup/render-image.html` sends each `.puml` file to [Kroki](https://kroki.io) and
publishes the SVG it returns — so a diagram can never drift from its source, and a PlantUML syntax
error fails the build. Point `HUGO_PARAMS_KROKI_URL` at a self-hosted Kroki to keep diagram source
off the public service.
