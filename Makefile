GITBOOK = $(CURDIR)/gitbook
DOCS = $(CURDIR)/docs
PKG = unixsocketcs

.PHONY: install-deps
install-deps:
	python3 -m pip install --upgrade setuptools wheel twine

.PHONY: uninstall clean
uninstall:
	pip3 uninstall $(PKG) || true

clean: uninstall
	rm -rf build dist *.egg-info __pycache__ $(PKG)/__pycache__ example/__pycache__ example/uds_server

.PHONY: dev-config config
dev-config:
	vim setup.py

config:
	sed -i '/^V/c\V="${VERSION}"' setup.py 

.PHONY: pack
pack:
	python3 setup.py sdist bdist_wheel

.PHONY: dev-upload dev-install upload install
dev-upload:
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

dev-install:
	python3 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ --no-deps $(PKG) 

upload:
	python3 -m twine upload dist/*

install:
	pip3 install $(PKG) 

.PHONY: dev-build dev-update build update dev-test test
dev-build: clean dev-config pack
dev-update:  dev-build dev-upload

build: clean config pack
update: build upload

dev-test: dev-install
test: install

.PHONY: mk-book clean-book
mk-book: gitbook
	gitbook build $(GITBOOK) $(DOCS)

clean-book: $(DOCS)
	rm -rf $(DOCS)/*
