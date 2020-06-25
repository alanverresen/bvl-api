#!/usr/bin/env sh

# This script publishes a new version of package to PyPI.
# DO NOT RUN THIS SCRIPT DIRECTLY, USE 'make publish-*' INSTEAD!

#------------------------------------------------------------------------------
# U. UTILITY FUNCTIONS
#------------------------------------------------------------------------------

clean_build() {
    rm -rf dist/
    rm -rf build/
    rm -rf *.egg-info
}


#------------------------------------------------------------------------------
# 0. SCRIPT GUARDS
#------------------------------------------------------------------------------

# This script expects one and only one argument: major, minor, or patch
if [ "$#" -ne 1 ]; then
    exit 1
fi

# Check that argument is one of the following: major, minor, or patch
if [ "$1" != "major" ] && [ "$1" != "minor" ] && [ "$1" != "patch" ]; then
    exit 1
fi


#------------------------------------------------------------------------------
# 1. ACTIVATE VIRTUAL ENVIRONMENT
#------------------------------------------------------------------------------

# Activate virtual environment.
. .venv/bin/activate


#------------------------------------------------------------------------------
# 2. CHECK THAT THERE ARE NO PROBLEMS
#------------------------------------------------------------------------------

# Run automated tests locally to make sure that there will be no problems.
make check || exit 1


#------------------------------------------------------------------------------
# 3. BUMP VERSION
#------------------------------------------------------------------------------
# We have two main concerns for this section:
# - a version bump commit should be clean
#       --> all changes must be committed beforehand
# - we shouldn't bump a version more than once
#       --> use .version-already-bumped file as proof
#------------------------------------------------------------------------------

# Make sure that all development efforts have been committed.
nothing_staged=$(git status | grep 'nothing to commit')
if [ -z "${nothing_staged}" ]; then
    echo "Please commit all remaining changes first using git."
    exit 1
fi

# Increase version of Python package and add proof of this.
if [ -f ".version-already-bumped" ]; then
    echo "version was already bumped once"
else
    bumpversion "$1"
    touch .version-already-bumped
fi

# Check to make sure that bumping version did not fail.
if [ ! -f ".version-already-bumped" ]; then
    echo "something went wrong while trying to bump version"
    exit 1
fi


#------------------------------------------------------------------------------
# 4. PUBLISH NEW PACKAGE
#------------------------------------------------------------------------------

# Remove any previous builds.
clean_build

# Build package.
python setup.py sdist bdist_wheel || \
    (clean_build && echo "failed to build package" && exit 1)

# Check package.
twine check dist/* || \
    (clean_build && echo "something is wrong with package" && exit 1)

# Publish package.
twine upload dist/* || \
    (clean_build && echo "failed to publish" && exit 1)


#------------------------------------------------------------------------------
# 5. CLEAN UP
#------------------------------------------------------------------------------

# Clean up after publishing package.
clean_build
rm .version-already-bumped
