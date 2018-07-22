# Contributing

## Get Source Code

Clone the repo from github:
```
$ git clone git@github.com:python-cmd2/cmd2-abbrev.git
```

## Create Python Environments

This project uses [tox](https://tox.readthedocs.io/en/latest/) to run the test
suite against multiple python versions. I recommend
[pyenv](https://github.com/pyenv/pyenv) with the
[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv>) plugin to manage
these various versions. If you are a Windows user, `pyenv` won't work for you,
but [conda](https://conda.io/) can also be used to solve this problem.

This distribution includes a shell script `build-pyenvs.sh` which
automates the creation of these environments.

If you prefer to create these virtual envs by hand, do the following:
```
$ cd cmd2_abbrev
$ pyenv install 3.7.0
$ pyenv virtualenv -p python3.7 3.7.0 cmd2-3.7
$ pyenv install 3.6.5
$ pyenv virtualenv -p python3.6 3.6.5 cmd2-3.6
$ pyenv install 3.5.5
$ pyenv virtualenv -p python3.5 3.5.5 cmd2-3.5
$ pyenv install 3.4.8
$ pyenv virtualenv -p python3.4 3.4.8 cmd2-3.4
```

Now set pyenv to make all three of those available at the same time:
```
$ pyenv local cmd2-3.7 cmd2-3.6 cmd2-3.5 cmd2-3.4
```

Whether you ran the script, or did it by hand, you now have isolated
virtualenvs for each of the major python
versions. This table shows various python commands, the version of
python which will be executed, and the virtualenv it will utilize.

| Command     | python | virtualenv |
| ----------- | ------ | ---------- |
| `python`    | 3.7.0  | cmd2-3.6   |
| `python3`   | 3.7.0  | cmd2-3.6   |
| `python3.7` | 3.7.0  | cmd2-3.7   |
| `python3.6` | 3.6.5  | cmd2-3.6   |
| `python3.5` | 3.5.5  | cmd2-3.5   |
| `python3.4` | 3.4.8  | cmd2-3.4   |
| `pip`       | 3.7.0  | cmd2-3.6   |
| `pip3`      | 3.7.0  | cmd2-3.6   |
| `pip3.7`    | 3.7.0  | cmd2-3.7   |
| `pip3.6`    | 3.6.5  | cmd2-3.6   |
| `pip3.5`    | 3.5.5  | cmd2-3.5   |
| `pip3.4`    | 3.4.8  | cmd2-3.4   |


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

## Make a Release

To make a release and deploy it to [PyPI](https://pypi.python.org/pypi), do the
following:

1. Merge everything to be included in the release into the **master** branch.

2. Run `tox` to make sure the tests pass in all the supported python versions.

3. Review and update `CHANGELOG.md`.

4. Push the **master** branch to github.

5. Tag the **master** branch with the new version number, and push the tag.

6. Build source distribution, wheel distribution, and upload them to Test PyPI:
   ```
   $ invoke pypi-test
   ```
   Check on [test.pypi.org](https://test.pypi.org) to make sure the package looks
good.

7. Build source distribution, wheel distribution, and upload them to PyPI:
   ```
   $ invoke pypi
   ```
