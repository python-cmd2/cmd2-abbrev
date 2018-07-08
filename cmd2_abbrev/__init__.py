#
# coding=utf-8
"""An abbreviation plugin for cmd2

Adds a user setting `abbrev` which defaults to false. When set to True
any command can be abbreviated by typing the shortest unique prefix
of that command.

See examples/example.py
"""

from .abbrev import AbbrevMixin