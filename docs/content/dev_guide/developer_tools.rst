===============================================================================
Developer Tools
===============================================================================

Several developer tools are used to help produce high-quality code, and manage
efforts among developers. This document gives a brief overview of which tools
are used and their purposes.


-------------------------------------------------------------------------------
Git and GitHub
-------------------------------------------------------------------------------

**git** is a widely used version management tool that helps us track and share
code, and manage change. **GitHub** is an online platform that is used to host
git repositories.

For more information, check out:

* https://git-scm.com/
* https://github.com/

-------------------------------------------------------------------------------
GNU Make
-------------------------------------------------------------------------------

**GNU Make** is a widely available build system that can also be used as a
task runner. We use Make and shell scripts to automate some of the most
common tasks of software development.

Use the command `make help` for a descriptive list of supported commands.

For more information, check out:

* https://www.gnu.org/software/make/


-------------------------------------------------------------------------------
Tox
-------------------------------------------------------------------------------

**Tox** is an automated testing tool for Python that takes advantage of virtual
environments. We use Tox for the following reasons:

* easy to integrate into CI/CD pipelines without any extra boilerplate code
* can run tests for different versions of Python
* extra dependencies can be managed locally per test

For more information, check out:

* https://tox.readthedocs.io/en/latest/


-------------------------------------------------------------------------------
pytest
-------------------------------------------------------------------------------

**pytest** is a unit testing framework that we use in addition to Python STL's
unittest framework. We use pytest for the following reasons:

* is compatible with (most) features of Python STL's unittest framework
* ships with reporting capabilities for CI/CD pipeline

For more information, check out:

* https://docs.pytest.org/en/latest/


-------------------------------------------------------------------------------
coverage.py
-------------------------------------------------------------------------------

**coverage.py** is a tool for measuring code coverage. We use it to measure
the quality of our unit tests.

For more information, check out:

* https://coverage.readthedocs.io/en/latest/


-------------------------------------------------------------------------------
flake8
-------------------------------------------------------------------------------

**flake8** is a linter tool that helps us comply with Python's official
Style Guide (PEP-8). There are several alternative tools available, such as
pylint, pyflakes, prospector, pep8 or pycodestyle, but there are several
reasons for using flake8 instead:

* wraps around pyflakes and pycodestyle packages for linting
* calculates 'cyclomatic complexity' of code; complex code == difficult to test
* doesn't complain about personal style too much

For more information, check out:

* https://flake8.pycqa.org/en/latest/
* https://www.python.org/dev/peps/pep-0008/


-------------------------------------------------------------------------------
bandit
-------------------------------------------------------------------------------

**bandit** is a static analysis tool focused on security.

For more information:

* https://bandit.readthedocs.io/en/latest/


-------------------------------------------------------------------------------
EditorConfig
-------------------------------------------------------------------------------

**EditorConfig** is a widely supported tool that informs editors and IDEs about
certain text formatting settings, such as:

* character encoding
* indentation
* spaces or tabs
* ...

For more information, check out:

* https://editorconfig.org/


-------------------------------------------------------------------------------
Sphinx and Read The Docs
-------------------------------------------------------------------------------

**Sphinx** is a documentation tool for Python that uses reStructuredText
markup. It's intuitive, allows us to create beautiful documentation, lets us
automatically extract source code documentation. **Read The Docs** is an online
platform for hosting our documentation online.

For more information, check out:

* https://www.sphinx-doc.org/
* https://readthedocs.org/


-------------------------------------------------------------------------------
Twine
-------------------------------------------------------------------------------

**Twine** is used for publishing packages to PyPI, the Python Package Index.

For more information, check out:

* https://twine.readthedocs.io/en/latest/


-------------------------------------------------------------------------------
bump2version
-------------------------------------------------------------------------------

**bump2version** is a tool that helps us with increasing versions.

For more information, check out:

* https://pypi.org/project/bump2version/
