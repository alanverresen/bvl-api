#!/usr/bin/env sh

# This script is used by Makefile to run all automated tests.
# DO NOT RUN THIS SCRIPT DIRECTLY, USE 'make check' INSTEAD!

# Activate virtual environment with developer tools.
. .venv/bin/activate

# Execute all tests and checks using tox.
tox
