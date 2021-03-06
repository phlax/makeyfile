
from . import registry
from .discovery import Discovery
from .loader import Loader
from .resolver import Resolver
from .runners import Runners


class Makeyfile(object):

    def __init__(self):
        self.registry = registry
        self.runners = Runners(self)
        self.discovery = Discovery()
        self.loader = Loader()
        self.makey = self.loader.load(self.filepath)
        self.resolver = Resolver(self)

    @property
    def filepath(self):
        return self.discovery.find()
