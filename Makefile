GITBOOK = $(CURDIR)/gitbook
DOCS = $(CURDIR)/docs

.PHONY: clean pack upload install uninstall generate update test
uninstall:
	pip3 uninstall usocketgen || true

clean: uninstall
	rm -rf build dist *.egg-info __pycache__ usocketgen/__pycache__ app

pack:
	vim setup.py
	python3 setup.py sdist bdist_wheel

upload-to-test:
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

install-from-test:
	python3 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ --no-deps usocketgen

upload:
	python3 -m twine upload dist/*

install:
	pip3 install usocketgen

generate:
	python3 -m usocketgen.genapp --conf testconf.json --app app


dev-update: clean pack upload-to-test
prod-update: clean pack upload

dev-test: install-from-test generate
prod-test: install generate


.PHONY: mk-book clean-book
mk-book: gitbook
	gitbook build $(GITBOOK) $(DOCS)

clean-book: $(DOCS)
	rm -rf $(DOCS)/*
