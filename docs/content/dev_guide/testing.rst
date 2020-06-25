===============================================================================
Testing
===============================================================================

High-quality code is impossible without testing. Any contribution that does not
pass all tests and checks to ensure high-quality code, is outright rejected.


-------------------------------------------------------------------------------
Unit Tests
-------------------------------------------------------------------------------

Unit tests should be written for all code by its developers, if possible (see
'code coverage').

We use 'pytest' for test execution, which also supports tests written with
Python STL's unittest framework, and thus both can be used to write unit tests.

In addition, tox is used as a testing automation framework to run unit tests
for all supported versions of Python. However, tests are skipped for any
supported version of Python that is not installed. If tests succeed for one
recent version of Python, they typically succeed for all recent versions of
Python, but just to be sure, you should try to have all supported versions
of Python installed.


-------------------------------------------------------------------------------
Code Coverage
-------------------------------------------------------------------------------

Code coverage is a way to measure the quality of tests that we have written.
We should always strive to attain 100% statement and branch coverage, because
otherwise the reported number loses meaning, and becomes less helpful. For
example:

* what if the most important 5%-10% isn't covered?
* what if we forgot to test a statement/branch that we wanted to cover?

However, attaining 100% code coverage is almost impossible in real life. That's
why, instead of lowering the coverage threshold, we should explicitly exclude
parts of our code by:

* mark classes, functions, statements and branches from code coverage by
  adding '# pragma: no cover' inline comments
* also, add a comment that motivates the decision to exclude that specific
  part from code coverage.

Any contribution where code coverage is not 100%, or where no motivation is
given to exclude code from code coverage, will be rejected.


-------------------------------------------------------------------------------
Testing Other Stuff
-------------------------------------------------------------------------------

Testing should not be limited to just testing source code in the traditional
sense. We also used tox to orchestrate the following tests:

* does static code analysis using flake8 and bandit find any problems?
* does documentation build correctly?
* does package build correctly?

Any contribution that does not also pass all of these checks is rejected.


-------------------------------------------------------------------------------
Running All Tests
-------------------------------------------------------------------------------

This project comes with a Makefile that provides developers with shortcuts for
many common activities, including running all tests. After running
'make install-dev' to install all developer tools in a virtual environment, you
can run `make check` to run all tests.
