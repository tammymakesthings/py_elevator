============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

All contributors must agree to abide by the `Contributor Covenant`_ Code of
Conduct. A copy of the Code of Conduct is provided in CODE_OF_CONDUCT.rst.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at <https://github.com/tammymakesthings/pyelevator/issues>.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Elevator Simulation could always use more documentation, whether as part of the
official Elevator Simulation docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
<https://github.com/tammymakesthings/pyelevator/issues>.

If you are proposing a feature:

* Explain in detail how it would work.

* Keep the scope as narrow as possible, to make it easier to implement.

* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `pyelevator`_ for local development.

1. Fork the `pyelevator`_ repo on GitHub.

2. Clone your fork locally::

   .. code-block: shell

       $ git clone git@github.com:your_name_here/pyelevator.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed,
   this is how you set up your fork for local development::

   .. code-block: shell

       $ mkvirtualenv pyelevator
       $ cd pyelevator/
       $ poetry update

4. Create a branch for local development::

   .. code-block: shell

       $ git checkout -b name-of-your-bugfix-or-feature

5. Now you can make your changes locally.

6. When you're done making changes, check that your changes pass flake8 and the
   tests::

   .. code-block: shell

       $ poetry run flake8 pyelevator tests
       $ poetry run pytest

7. Commit your changes and push your branch to GitHub::

   .. code-block: shell

       $ git add .
       $ git commit -m "Your detailed description of your changes."
       $ git push origin name-of-your-bugfix-or-feature

8. Submit a pull request through the GitHub website.


Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines::

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.

3. The pull request should work for Python 3.10.


Tips
----

To run a subset of tests::

.. code-block: shell

	$ poetry run pytest


Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

.. code-block: shell

	$ bump2version patch # possible: major / minor / patch
	$ git push
	$ git push --tags

.. _Contributor Covenant: https://contributor-covenant.org/
.. _pyelevator: https://github.com/tammymakesthings/pyelevator/
