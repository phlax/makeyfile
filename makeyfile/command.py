
import argparse

from .exceptions import UnrecognizedMakeyError


class Command(object):

    def __init__(self, makeyfile):
        self.makeyfile = makeyfile

    @property
    def commands(self):
        return self.resolver.commands

    @property
    def resolver(self):
        return self.makeyfile.resolver

    @property
    def parser_class(self):
        return argparse.ArgumentParser

    @property
    def parser(self):
        return self.add_args(self.parser_class())

    def add_args(self, parser):
        parser.add_argument(
            'command',
            action='store',
            choices=self.commands.keys(),
            help='Command to run')
        return parser

    def resolve(self, command):
        try:
            result = self.parser.parse_known_args([command])[0]
        except SystemExit as e:
            raise UnrecognizedMakeyError(e)
        return self.resolver.resolve(result.command)
