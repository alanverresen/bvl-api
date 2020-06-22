#!/usr/bin/env sh

# This script lets linter check code for problems.

# Activate virtual environment.
. .venv/bin/activate

# Use linter to check code.
flake8 --config=devs/flake8.ini --exit-zero .
