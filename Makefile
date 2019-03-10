clean:
	rm -rf build dist *.egg-info __pycache__ usocketgen/__pycache__ app

pack:
	python3 setup.py sdist bdist_wheel

upload:
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

install:
	python3 -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ --no-deps usocketgen

uninstall:
	python3 -m pip uninstall usocketgen

generate:
	python3 -m usocketgen.genapp --conf conf.json --app app
