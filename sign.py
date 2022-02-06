from abc import ABC

from helper import is_numeric
from input import Input


class Sign(Input, ABC):
    blocker = ['+', '-', '/', '*', '=', '^', ')', '.']

    def __init__(self, value):
        super().__init__()
        self.value = str(value)

    def append(self, output):
        if not output.buffer and self.block_input(self.value):
            return

        last = output.buffer[-1]
        if is_numeric(last) or last == ')':
            output.buffer.append(self.value)
        else:
            output.buffer.pop()
            output.buffer.append(self.value)
        output.refresh_label()

    def block_input(self, value):
        return value in self.blocker
