from abc import ABC

from classes.input import Input


class Clear(Input, ABC):
    def __init__(self):
        super().__init__()

    def append(self, output):
        output.clear()
