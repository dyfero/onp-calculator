from abc import ABC

from classes.constants.operator import OperatorEnum
from classes.helpers.helper import is_numeric
from classes.input import Input


class Sign(Input, ABC):
    blocker = [
        OperatorEnum.ADD,
        OperatorEnum.SUB,
        OperatorEnum.DIV,
        OperatorEnum.MUL,
        OperatorEnum.EQL,
        OperatorEnum.POW,
        OperatorEnum.RBR,
        OperatorEnum.DOT
    ]

    def __init__(self, value):
        super().__init__()
        self.value = str(value)

    def append(self, output):
        if not output.buffer and self.block_input(self.value):
            return

        last = output.buffer[-1]
        if is_numeric(last) or last == OperatorEnum.RBR:
            output.buffer.append(self.value)
        else:
            output.buffer.pop()
            output.buffer.append(self.value)
        output.refresh_label()

    def block_input(self, value):
        return value in self.blocker
