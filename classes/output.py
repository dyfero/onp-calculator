from classes.bracket import __decrement_bracket__, __increment_bracket__, __clear_bracket_counter__
from classes.converter import Converter
from classes.constants.operator import OperatorEnum
from classes.helpers.helper import is_numeric
from classes.onp import Onp


class Output:
    def __init__(self, layout):
        self.onp = Onp()
        self.converter = Converter()
        self.buffer = []
        self.layout = layout

    def refresh_label(self):
        if self.layout.ids['label_expression'].text:
            self.layout.ids['label_expression'].text = ''

        label = self.layout.ids['label_input']
        label.text = ' '.join(self.buffer)

    def remove(self):
        if not self.buffer:
            __clear_bracket_counter__()
            return

        last = self.buffer[-1]
        if is_numeric(last):
            elem = last[:-1]
            self.buffer.pop()
            if elem and elem != OperatorEnum.SUB:
                self.buffer.append(elem)
        elif last == OperatorEnum.LBR:
            __decrement_bracket__()
            self.buffer.pop()
        elif last == OperatorEnum.RBR:
            __increment_bracket__()
            self.buffer.pop()
        else:
            self.buffer.pop()

        self.refresh_label()

    def change_sign(self):
        if not self.buffer:
            return

        if self.buffer and not is_numeric(self.buffer[-1]):
            return

        elem = self.buffer.pop()
        if elem[0] == OperatorEnum.SUB:
            elem = elem[1:]
        else:
            elem = OperatorEnum.SUB + elem

        self.buffer.append(elem)
        self.refresh_label()

    def clear(self):
        self.clear_variables()
        self.refresh_label()

    def clear_variables(self):
        self.buffer = []
        __clear_bracket_counter__()

    def result(self):
        if not self.buffer:
            return

        converted = self.converter.convert(self.buffer)
        result = self.onp.calc(converted)
        result = self.map_result(result)

        self.layout.ids['label_expression'].text = ' '.join(self.buffer)
        self.layout.ids['label_input'].text = str(result)
        self.clear_variables()

    def map_result(self, result):
        if result.is_integer():
            return int(result)
        return result
