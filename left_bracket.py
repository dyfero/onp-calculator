from abc import ABC
from bracket import Bracket, __increment_bracket__
from input import Input
from helper import is_numeric


class LeftBracket(Bracket, Input, ABC):
    def __init__(self):
        super().__init__()

    def append(self, output):
        if output.buffer and (is_numeric(output.buffer[-1]) or output.buffer[-1] == ')'):
            output.buffer.append('*')

        __increment_bracket__()
        output.buffer.append('(')
        output.refresh_label()
