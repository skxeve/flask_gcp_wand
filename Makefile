
all: clean build upload-test upload

build:
	python setup.py bdist_wheel
	tree dist

clean:
	rm -rf flask_gcp_wand.egg-info dist build

upload-test:
	twine upload --repository pypitest dist/*

install:
	pip --no-cache-dir install --upgrade --index-url https://test.pypi.org/simple/ flask_gcp_wand

upload:
	twine upload --repository pypi dist/*

