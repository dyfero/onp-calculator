from abc import ABC

from classes.constants.operator import OperatorConst
from classes.input import Input
from classes.helpers.helper import is_numeric


class Dot(Input, ABC):
    def __init__(self):
        super().__init__()

    def append(self, output):
        if not output.buffer:
            return
        elem = output.buffer[-1]
        if is_numeric(elem) and not OperatorConst.DOT in elem:
            elem = output.buffer.pop()
            elem += '.'
            output.buffer.append(elem)
            output.refresh_label()
