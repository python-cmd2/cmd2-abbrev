#
# coding=utf-8

import argparse

import cmd2
import cmd2_abbrev

class AbbrevExample(cmd2_abbrev.AbbrevMixin, cmd2.Cmd):
    """A cmd2 program to demonstrate the use of the cmd2_abbrev plugin"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxrepeats = 3
        # abbrev defaults to False, let's turn it on
        self.abbrev = True

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

if __name__ == '__main__':
    app = AbbrevExample()
    app.cmdloop()
