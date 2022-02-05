from kivy.uix.widget import Widget
from helper import is_numeric
from onp import Onp
from converter import Converter


class CalculatorLayout(Widget):
    blocker = ['+', '-', '/', '*', '=', '^', ')', '.']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.onp = Onp()
        self.converter = Converter()
        self.input = ''
        self.buffer = []
        self.brackets_counter = 0

    def increment_bracket(self):
        self.brackets_counter = self.brackets_counter + 1

    def decrement_bracket(self):
        self.brackets_counter = self.brackets_counter - 1

    def block_input(self, value):
        return value in self.blocker

    def left_bracket(self, instance):
        if self.buffer and (is_numeric(self.buffer[-1]) or self.buffer[-1] == ')'):
            self.buffer.append('*')

        self.increment_bracket()
        self.buffer.append(instance.text)
        self.refresh_label()

    def right_bracket(self, instance):
        if not self.buffer or self.brackets_counter <= 0:
            return

        last = self.buffer[-1]
        if is_numeric(last) or last == ')':
            self.decrement_bracket()
            self.buffer.append(instance.text)
            self.refresh_label()

    def sign(self, instance):
        value = instance.text
        if not self.buffer and self.block_input(value):
            return

        last = self.buffer[-1]
        if is_numeric(last) or last == ')':
            self.buffer.append(value)
        else:
            self.buffer.pop()
            self.buffer.append(value)
        self.refresh_label()

    def number(self, instance):
        if self.buffer and self.buffer[-1] == ')':
            self.buffer.append('*')
            self.buffer.append(instance.text)
        elif self.buffer and is_numeric(self.buffer[-1]):
            elem = self.buffer.pop()
            if elem == '0':
                elem = instance.text
            else:
                elem += instance.text  # map from int to str
            self.buffer.append(elem)
        else:
            self.buffer.append(instance.text)
        self.refresh_label()

    def dot(self, instance):
        if not self.buffer:
            return
        elem = self.buffer[-1]
        if is_numeric(elem) and not '.' in elem:
            elem = self.buffer.pop()
            elem += '.'
            self.buffer.append(elem)
            self.refresh_label()

    def result(self):
        if not self.buffer:
            return
        converted = self.converter.convert(self.buffer)
        result = self.onp.calc(converted)
        self.ids['label_expression'].text = ' '.join(self.buffer)
        self.ids['label_input'].text = str(result)
        self.buffer = []

    def change_sign(self, instance):
        if self.buffer and not is_numeric(self.buffer[-1]):
            return

        elem = self.buffer.pop()
        if elem[0] == '-':
            elem = elem[1:]
        else:
            elem = '-' + elem

        self.buffer.append(elem)
        self.refresh_label()

    def refresh_label(self):
        if self.ids['label_expression'].text:
            self.ids['label_expression'].text = ''

        label = self.ids['label_input']
        label.text = ' '.join(self.buffer)

    def remove(self, instance):
        if not self.buffer:
            return

        last = self.buffer[-1]
        if is_numeric(last):
            elem = last[:-1]
            self.buffer.pop()
            if elem and elem != '-':
                self.buffer.append(elem)
        elif last == '(':
            self.decrement_bracket()
            self.buffer.pop()
        elif last == ')':
            self.increment_bracket()
            self.buffer.pop()
        else:
            self.buffer.pop()

        self.refresh_label()

    def clear(self, instance):
        self.buffer = []
        self.brackets_counter = 0
        self.refresh_label()
