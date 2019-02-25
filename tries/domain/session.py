from .domain_object import *


class Session(DomainObject):

    def __init__(self):
        super().__init__()

        self.start: int = None
        self.stop: int = None

        self.pipes = []