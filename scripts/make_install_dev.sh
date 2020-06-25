#!/usr/bin/env sh

# This script installs all developer tools needed for local development.
# DO NOT RUN THIS SCRIPT DIRECTLY, USE 'make install-dev' INSTEAD!

# Installs virtual python environment with pip.
if [ ! -d ".venv" ]; then
    python3 -m venv --without-pip .venv
    . .venv/bin/activate
    curl https://bootstrap.pypa.io/get-pip.py | python3
    deactivate
fi

# Activate virtual environment.
. .venv/bin/activate

# Install developer tools and package dependencies.
python3 -m pip install --upgrade twine tox bump2version
python3 -m pip install --upgrade -r requirements.txt
