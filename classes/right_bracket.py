from abc import ABC

from classes.bracket import Bracket, __decrement_bracket__
from classes.constants.operator import OperatorConst
from classes.helpers.helper import is_numeric
from classes.input import Input


class RightBracket(Bracket, Input, ABC):
    def __init__(self):
        super().__init__()

    def append(self, output):
        if not output.buffer or self.brackets_counter <= 0:
            return

        last = output.buffer[-1]
        if is_numeric(last) or last == OperatorConst.RBR:
            __decrement_bracket__()
            output.buffer.append(OperatorConst.RBR)
            output.refresh_label()
