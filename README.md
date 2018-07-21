# cmd2-abbrev

## Description

Plugin for cmd2 to support previously deprecated abbreviation behavior.

Adds a setting `abbrev` which allows users to control whether commands
can be abbreviated. If an application has a `speak` command:
```
(Cmd) speak hello
hello
```
then any unique prefix of any command will run the command:
```
(Cmd) set abbrev True
abbrev - was: False
now: True
(Cmd) sp hello
hello
```

Non-unique abbreviations generate a syntax error:
```
(Cmd) s hello
*** Unknown syntax: s hello
(Cmd) help

Documented commands (type help <topic>):
========================================
alias  help     load  pyscript  set    shortcuts  unalias
edit   history  py    quit      shell  speak
```

## Installation

System requirements: works anywhere `cmd2` works. Requires `cmd2` version 0.9.4
or higher.

Install using pip:
```
$ pip install cmd2-abbrev
```

Add to your `cmd2` application by mixing in the `AbbrevMixin` class:
```python
import cmd2
import cmd2_abbrev

class AbbrevExample(cmd2_abbrev.AbbrevMixin, cmd2.Cmd):
    """A cmd2 program to demonstrate the use of the cmd2_abbrev plugin"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
```

You must mix in `AbbrevMixin` before `cmd2.Cmd` or it won't work properly.
