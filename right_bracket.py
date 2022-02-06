from abc import ABC

from bracket import Bracket, __decrement_bracket__
from helper import is_numeric
from input import Input


class RightBracket(Bracket, Input, ABC):
    def __init__(self):
        super().__init__()

    def append(self, output):
        if not output.buffer or self.brackets_counter <= 0:
            return

        last = output.buffer[-1]
        if is_numeric(last) or last == ')':
            __decrement_bracket__()
            output.buffer.append(')')
            output.refresh_label()
