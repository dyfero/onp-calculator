from abc import ABC

from classes.constants.operator import OperatorEnum
from classes.input import Input
from classes.helpers.helper import is_numeric


class Number(Input, ABC):
    def __init__(self, value):
        super().__init__()
        self.value = str(value)

    def append(self, output):
        if output.buffer and output.buffer[-1] == OperatorEnum.RBR:
            output.buffer.append(OperatorEnum.MUL)
            output.buffer.append(self.value)
        elif output.buffer and is_numeric(output.buffer[-1]):
            elem = output.buffer.pop()
            if elem == '0':
                elem = self.value
            else:
                elem += self.value
            output.buffer.append(elem)
        else:
            output.buffer.append(self.value)
        output.refresh_label()
