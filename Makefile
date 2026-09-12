PY := python3
S  := scripts

# Hugo needs Dart Sass on PATH to compile Docsy's stylesheets. It is a project-local npm dependency
# rather than a global install, so `npm install` is all the setup there is.
HUGO := PATH="$(CURDIR)/node_modules/.bin:$$PATH" hugo

.PHONY: help instructions lint serve build stage clean

## Show the available commands
help:
	@echo "make instructions  regenerate the Copilot copies in .github/, the type table in AGENTS.md, and index.html"
	@echo "make lint          check frontmatter, Open Knowledge Format conformance and links (errors fail)"
	@echo "make serve         live-reload site at http://localhost:1313/jarvis/site/"
	@echo "make build         check nothing is stale or broken, render every diagram, build site/"
	@echo "make stage         build, then assemble deploy/ exactly as the server receives it"
	@echo "make clean         remove site/ and deploy/"

## Regenerate everything that restates the instructions
instructions:
	@$(PY) $(S)/build_instructions.py

## Regenerate, then check
lint: instructions
	@$(PY) $(S)/lint_docs.py $(if $(STRICT),--strict,)

## Live-reload the site while writing. Diagrams render through Kroki, so this needs network access;
## offline, a diagram shows as a link to its .puml source instead.
serve:
	$(HUGO) server --buildDrafts

## Full check plus a build — what CI runs. Nothing is regenerated: a stale generated file is a failure,
## not a fixup. Hugo warnings fail the build, because the two things that warn are a link that
## resolves to nothing and a diagram that did not render, and neither should ever deploy.
build:
	@$(PY) $(S)/build_instructions.py --check
	@$(PY) $(S)/lint_docs.py $(if $(STRICT),--strict,)
	$(HUGO) --minify --panicOnWarning

## The deploy uploads deploy/ to the server: the landing page at the top, the docs under site/.
stage: build
	@rm -rf deploy && mkdir -p deploy
	@cp index.html deploy/
	@cp -R site deploy/site
	@echo "stage: deploy/ holds index.html and site/"

clean:
	rm -rf site deploy
