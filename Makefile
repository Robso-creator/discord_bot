all:
	@echo "#### functions implemented"
	@echo "make up ...................... runs main.py"
	@echo "make pc ...................... runs pre-commit on all files"

pc:
	@echo "[PRE-COMMIT] All files"
	pre-commit run --all-files

up:
	python3 -m src.main
