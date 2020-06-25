#!/usr/bin/env sh

# This script prints out information about all available make commands.
# DO NOT RUN THIS SCRIPT DIRECTLY, USE 'make help' INSTEAD!

echo "------------------------------------------------------------------------"
echo ""
echo "This makefile provides the following targets:"
echo ""
echo "help"
echo "    prints list of all targets (default target)"
echo "install-dev"
echo "    install/upgrade all tools and dependencies for local development"
echo "publish-major"
echo "    publishes a new major release of package to PyPI"
echo "publish-minor"
echo "    publishes a new minor release of package to PyPI"
echo "publish-patch"
echo "    publishes a new patch release of package to PyPI"
echo "check"
echo "    checks whether or not all automated tests pass"
echo "clean"
echo "    removes all temporary and generated files"
echo ""
echo "------------------------------------------------------------------------"
