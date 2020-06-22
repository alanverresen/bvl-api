#!/usr/bin/env sh

# This script installs all tools for local development.

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
python3 -m pip install --upgrade -r devs/requirements.txt
python3 -m pip install --upgrade -r requirements.txt
