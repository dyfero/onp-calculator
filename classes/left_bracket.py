from abc import ABC
from classes.bracket import Bracket, __increment_bracket__
from classes.constants.operator import OperatorEnum
from classes.input import Input
from classes.helpers.helper import is_numeric


class LeftBracket(Bracket, Input, ABC):
    def __init__(self):
        super().__init__()

    def append(self, output):
        if output.buffer and (is_numeric(output.buffer[-1]) or output.buffer[-1] == OperatorEnum.RBR):
            output.buffer.append(OperatorEnum.MUL)

        __increment_bracket__()
        output.buffer.append(OperatorEnum.LBR)
        output.refresh_label()
