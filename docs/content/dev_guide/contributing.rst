===============================================================================
Contributing
===============================================================================

If you want to contribute to this project, please follow the steps as
described in this document:

1. fork this repository on github
2. clone repository
3. install tools and run tests
4. create a new branch
5. contribute
6. push your contribution(s)
7. send a pull request

After a pull request has been sent, one of the repository's maintainers can
review the pull request, and add your contributions.


-------------------------------------------------------------------------------
0. Preparations
-------------------------------------------------------------------------------

If you want to contribute to this project, we recommend that you do several
things first. The following conditions should be met before continuing. Most
of the listed tools are widely available, and are often already installed:

* You need to have a GitHub account.
* You need to have a recent version of curl installed.
* You need to have a recent version of git installed.
* You need to have a recent version of make installed.
* You need to have a recent version of python3 installed.

**If possible, you should try to install a recent version of each
major Python release that is supported by this package.**

Contributions are automatically tested for each supported version of Python,
and if any of the tests fail, the contribution will be rejected. You can run
these automated tests locally on your own machine by using the `make check`
command, but tests for specific versions of Python are skipped if those
versions of Python are not installed. That being said, if the automated tests
pass for one supported version of Python, then they typically pass for all
supported versions of Python.


-------------------------------------------------------------------------------
1. Fork This Repository On Github
-------------------------------------------------------------------------------

Log into github.com and fork this project's repository by pressing the 'fork'
button in the upper-right corner of the repository's main page.

A copy of this repository should've been added to your github account.


-------------------------------------------------------------------------------
2. Clone Repository
-------------------------------------------------------------------------------

You should now clone the repository that was added to your own github account
to your own local machine.

.. code-block:: sh

   $ git clone git@github.com:<your-username>/<repository-name>.git

You should now have a local copy of the repository on your machine.


-------------------------------------------------------------------------------
3. Install Tools and Run Tests
-------------------------------------------------------------------------------

Before you continue, you should make sure that everything will run smoothly on
your machine. First of all, run the following command in the repository's
root directory to install all required developer tools in a virtual
environment.

.. code-block:: sh

   $ make install-dev

After having installed all developer tools, we should be able to check if all
parts of our project pass all checks.

.. code-block:: sh

   $ make check

Tox should congratulate us, and report that everything went well. It is
recommended that you regularly run the `make check` command while working on
your contributions to detect any problems.


-------------------------------------------------------------------------------
4. Create A New Branch
-------------------------------------------------------------------------------

All contributions should be added in a new branch with a descriptive name.
To create a new branch, run the following command:

.. code-block:: sh

   $ git checkout master
   $ git pull upstream master && git push origin master
   $ git checkout -b my_contributions

You should now be working in a new branch.


-------------------------------------------------------------------------------
5. Contribute
-------------------------------------------------------------------------------

You can contribute in several ways:

- add extra functionality
- change the source code
- update or improve documentation
- ...

To uphold the code quality of this project, it is important to make sure that
your contributions do not cause any of our automated checks to fail. Again,
it's important that you rerun the `make check` command every so often.


-------------------------------------------------------------------------------
6. Commit and Push Your Contribution(s)
-------------------------------------------------------------------------------

After adding your contributions, and running the `make check` command one last
time to make sure that there aren't any problems, it is time to commit and
push your changes to your personal repository on GitHub. Make sure that your
commit message is clear and concise.

.. code-block:: sh

   $ git commit -m "A short description of my contribution(s)."
   $ git push -u origin my_contributions

Your own repository on GitHub should now have a new branch with your
contributions in it.


-------------------------------------------------------------------------------
7. Send A Pull Request
-------------------------------------------------------------------------------

GitHub should now give you the option for sending a pull request on your own
repository's main page. Click this button, and you will be presented with a
page where you can provide the maintainers of the project with more
information about your contributions.

Finally, click the 'Create pull request' button to submit your contributions
for further review by the project's maintainers.
