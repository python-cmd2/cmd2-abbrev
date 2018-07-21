#
# coding=utf-8
"""A cmd2 plugin which adds support for abbreviated commands."""

import cmd2

class AbbrevMixin:
    """A cmd2 plugin (mixin class) which adds support for abbreviated commands."""
    def __init__(self, *args, **kwargs):
        "Initialize this plugin."
        # code placed here runs before cmd2 initializes
        super().__init__(*args, **kwargs)
        # code placed here runs after cmd2 initializes
        # this is where you register any hook functions
        self.abbrev = False
        self.settable.update({'abbrev': 'Accept command abbreviations'})
        self.register_postparsing_hook(self.cmd2_abbrev_hook)

    def cmd2_abbrev_hook(self, data: cmd2.plugin.PostparsingData) -> cmd2.plugin.PostparsingData:
        """Postparsing hook which interprets abbreviated command names."""
        if self.abbrev:
            target = 'do_' + data.statement.command
            if target not in dir(self):
                # check if the entered command might be an abbreviation
                funcs = [func for func in self.keywords if func.startswith(data.statement.command)]
                if len(funcs) == 1:
                    raw = data.statement.raw.replace(data.statement.command, funcs[0], 1)
                    data.statement = self.statement_parser.parse(raw)
        return data
