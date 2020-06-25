#!/usr/bin/env sh

# This script checks that all tools for local development are installed.
# DO NOT RUN THIS SCRIPT DIRECTLY!

# Check that virtual environment with tools is installed yet.
if [ ! -d ".venv" ]; then
    echo "No virtual environment found; run 'make install-dev' first!"
    exit 1
fi

# Activate virtual environment.
. .venv/bin/activate

# Check that all required dev tools are installed.
if [ -z "$(command -v tox)" ]; then
    echo "Tool 'tox' not found; run 'make install-dev' first!"
    exit 1
fi
if [ -z "$(command -v twine)" ]; then
    echo "Tool 'twine' not found; run 'make install-dev' first!"
    exit 1
fi
if [ -z "$(command -v bumpversion)" ]; then
    echo "Tool 'bumpversion' not found; run 'make install-dev' first!"
    exit 1
fi
