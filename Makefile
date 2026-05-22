OUT := docs/assets/img

PUML_FILES := \
	docs/domain_model/domainModel.puml \
	docs/use_case/useCaseDiagram.puml \
	docs/use_case/authenticate/authenticate.puml \
	docs/use_case/withdraw_cash/withdrawCash.puml \
	docs/use_case/withdraw_foreign_currency/withdrawForeignCurrency.puml \
	docs/use_case/check_balance/checkBalance.puml \
	docs/use_case/transfer_funds/transferFunds.puml \
	docs/use_case/print_receipt/printReceipt.puml \
	docs/state_chart/transactionStateChart.puml

.PHONY: diagrams serve

## Regenerate all PlantUML diagrams as SVG files into docs/assets/img/
diagrams:
	@echo "Generating PlantUML diagrams..."
	@for f in $(PUML_FILES); do \
		echo "  $$f"; \
		plantuml -tsvg -o "$(CURDIR)/$(OUT)" "$$f"; \
	done
	@echo "Done."

## Regenerate diagrams, then start mkdocs serve (live-reload)
serve: diagrams
	mkdocs serve
