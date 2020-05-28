
from enum import Enum, auto

class UIKind(Enum):
    start = auto()
    win = auto()
    lose = auto()
    play = auto()


class UI():

    def __init__(self, kind):
        self.kind = kind
