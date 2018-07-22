#
# coding=utf-8

import argparse

import cmd2
import cmd2_abbrev

class AbbrevApp(cmd2_abbrev.AbbrevMixin, cmd2.Cmd):
    """Simple subclass of cmd2.Cmd with the AbbrevMixin plugin included."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxrepeats = 3

    speak_parser = argparse.ArgumentParser()
    speak_parser.add_argument('-p', '--piglatin', action='store_true', help='atinLay')
    speak_parser.add_argument('-s', '--shout', action='store_true', help='N00B EMULATION MODE')
    speak_parser.add_argument('-r', '--repeat', type=int, help='output [n] times')
    speak_parser.add_argument('words', nargs='+', help='words to say')

    @cmd2.with_argparser(speak_parser)
    def do_speak(self, args):
        """Repeats what you tell me to."""
        words = []
        for word in args.words:
            if args.piglatin:
                word = '%s%say' % (word[1:], word[0])
            if args.shout:
                word = word.upper()
            words.append(word)
        repetitions = args.repeat or 1
        for i in range(min(repetitions, self.maxrepeats)):
            # .poutput handles newlines, and accommodates output redirection too
            self.poutput(' '.join(words))


#
# You can't use a fixture to instantiate your app if you want to use
# to use the capsys fixture to capture the output. cmd2.Cmd sets
# internal variables to sys.stdout and sys.stderr on initialization
# and then uses those internal variables instead of sys.stdout. It does
# this so you can redirect output from within the app. The capsys fixture
# can't capture the output properly in this scenario.
#
# If you have extensive initialization needs, create a function
# to initialize your cmd2 application.
def init_app():
    app = AbbrevApp()
    return app


#####
#
# unit tests
#
#####
def test_normal_command_abbrev_true(capsys):
    app = init_app()
    app.abbrev = True
    app.onecmd_plus_hooks('speak hello')
    out, err = capsys.readouterr()
    assert out == 'hello\n'
    assert not err

def test_normal_command_abbrev_false(capsys):
    app = init_app()
    app.abbrev = False
    app.onecmd_plus_hooks('speak hello')
    out, err = capsys.readouterr()
    assert out == 'hello\n'
    assert not err

def test_short_command_abbrev_true(capsys):
    app = init_app()
    app.abbrev = True
    app.onecmd_plus_hooks('sp hello')
    out, err = capsys.readouterr()
    assert out == 'hello\n'
    assert not err

def test_short_command_abbrev_false(capsys):
    app = init_app()
    app.abbrev = False
    app.onecmd_plus_hooks('sp hello')
    out, err = capsys.readouterr()
    assert "Unknown syntax" in out
    assert not err

def test_not_unique_abbrev(capsys):
    app = init_app()
    app.abbrev = True
    app.onecmd_plus_hooks('s hello')
    out, err = capsys.readouterr()
    assert "Unknown syntax" in out
    assert not err
