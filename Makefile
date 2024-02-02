all:
	@echo "#### functions implemented"
	@echo "make up ...................... runs main.py"
	@echo "make pc ...................... runs pre-commit on all files"
	@echo "make test .................... runs all tests (pytest)"

pc:
	@echo "[PRE-COMMIT] All files"
	pre-commit run --all-files

up:
	python3 -m src.main

test:
	python3 -m pytest

local_doc:
	@echo 'RUNNING DOCUMENTATION SCRIPTS'
	@for script in ./src/continuous_documentation/*.py; do \
		echo 'Running script:' $$script; \
		python3 -m src.continuous_documentation."$$(basename "$$script" .py)"; \
	done


build_doc:
	mkdocs build
	mkdocs serve
