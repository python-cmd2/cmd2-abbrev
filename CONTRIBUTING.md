# Contributing

## Get Source Code

Clone the repo from github:
```
$ git clone git@github.com:python-cmd2/cmd2-abbrev.git
```

## Install Dependencies

Install all the development dependencies:
```
$ pip install -e .[dev]
```

This command also installs `cmd2-abbrev` "in-place", so the package points to
the source code instead of copying files to the python `site-packages` folder.

All the dependencies now have been installed in the `cmd2-3.7`
virtualenv. If you want to work in other virtualenvs, you'll need to manually
select it, and install again::

   $ pyenv shell cmd2-3.4
   $ pip install -e .[dev]

## Common Development Tasks

This project uses many other python modules for various development tasks,
including testing, linting, building wheels, and distributing releases. These
modules can be configured many different ways, which can make it difficult to
learn the specific incantations required for each project you are familiar with.

This project uses [invoke](<http://www.pyinvoke.org>) to provide a clean,
high level interface for these development tasks. To see the full list of
functions available:
```
$ invoke -l
```

You can run multiple tasks in a single invocation, for example:
```
$ invoke clean docs sdist wheel
```

That one command will remove all superflous cache, testing, and build
files, render the documentation, and build a source distribution and a
wheel distribution.

For more information, read `tasks.py`.
