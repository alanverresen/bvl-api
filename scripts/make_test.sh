#!/usr/bin/env sh

# This script executes all tests.

# Activate virtual environment.
. .venv/bin/activate

# Executes tests for different environments.
tox
