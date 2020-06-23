#!/usr/bin/env sh

# This script publishes package to PyPI.

# Activate virtual environment.
. .venv/bin/activate

# Publish package.
rm -rf dist/*
python setup.py sdist bdist_wheel
twine check dist/*
twine upload dist/*
