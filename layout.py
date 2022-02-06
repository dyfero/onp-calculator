from kivy.uix.widget import Widget
from output import Output


class CalculatorLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output = Output(self)

    def append(self, instance):
        instance.append(self.output)
