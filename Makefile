OUT := docs/assets/img

# Every .puml under docs/ is rendered — no hand-maintained list to drift out of sync.
# Each diagram's output name comes from its `@startuml <name>` directive, which the
# conventions require to equal the file basename. `make lint` (check L3) enforces that.
PUML_FILES := $(shell find docs -name '*.puml' | sort)

# Overridable so CI can point at a downloaded jar: make diagrams PLANTUML="java -jar plantuml.jar"
PLANTUML ?= plantuml

.PHONY: diagrams serve lint landing build clean

## Regenerate all PlantUML diagrams as SVG files into docs/assets/img/
diagrams:
	@echo "Generating PlantUML diagrams..."
	@for f in $(PUML_FILES); do \
		echo "  $$f"; \
		$(PLANTUML) -tsvg -o "$(CURDIR)/$(OUT)" "$$f" || exit 1; \
	done
	@echo "Done."

## Check documentation consistency (links, nav coverage, traceability, diagram naming)
lint:
	@python3 scripts/lint_docs.py
	@python3 scripts/build_landing.py --check

## Rebuild the embedded instructions in index.html from .github/instructions/
landing:
	@python3 scripts/build_landing.py

## Regenerate diagrams, then start mkdocs serve (live-reload)
serve: diagrams
	mkdocs serve

## Full local check: diagrams, lint, strict build — same order as CI
build: diagrams lint
	mkdocs build --strict

## Remove generated output
clean:
	rm -rf site
