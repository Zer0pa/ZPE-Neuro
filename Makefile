.PHONY: install test offline-verify download-dandi benchmark clean

PYTHON ?= python3.11
PIP ?= $(PYTHON) -m pip
PYTEST ?= $(PYTHON) -m pytest

install:
	$(PIP) install -e '.[dev,public,proof]'

test:
	$(PYTEST) tests -v

offline-verify:
	$(PYTEST) tests -v

download-dandi:
	$(PIP) install dandi
	mkdir -p data/dandi000034 data/dandi000055
	dandi download https://dandiarchive.org/dandiset/000034/draft --output-dir data/dandi000034/
	dandi download https://dandiarchive.org/dandiset/000055/draft --output-dir data/dandi000055/

benchmark:
	$(PYTHON) tools/run_public_corpus_benchmark.py --dandiset 000034 --artifact-root proofs/artifacts/dandi000034_benchmark --fixture-output tests/fixtures/dandi000034_extract.nwb

clean:
	rm -rf build dist *.egg-info .pytest_cache .coverage htmlcov
