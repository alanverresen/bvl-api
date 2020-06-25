#!/usr/bin/env sh

# This script cleans up most/all temporary files from repository.
# DO NOT RUN THIS SCRIPT DIRECTLY, USE 'make clean' INSTEAD!

# function used to find and remove files
find_and_remove()
{
  find . -name "$1" -exec rm -rf "{}" \; 2>/dev/null
}

# function used to find and remove directories
find_dir_and_remove()
{
  find . -type d -name "$1" -exec rm -rf "{}" \; 2>/dev/null
}

# remove following directories in root directory
rm -rf ".logs";
rm -rf ".venv";
rm -rf ".tox";
rm -rf "*.egg-info";
rm -rf "dist";
rm -rf "build";

# remove following file in root directory
rm ".coverage" 2>/dev/null
rm "MANIFEST" 2>/dev/null

# remove generated directories in all subdirectories
find_dir_and_remove "__pycache__";

# remove generated files in all subdirectories
find_and_remove "*~";
find_and_remove "*.pyc";
