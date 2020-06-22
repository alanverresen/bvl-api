#!/usr/bin/env sh

# This script builds all documentation locally.

# Activate virtual environment.
. .venv/bin/activate

# Builds documentation.
sphinx-build -W -b html docs docs/_build/html
