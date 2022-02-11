from kivy.uix.widget import Widget
from classes.output import Output
from kivy.core.window import Window


class CalculatorLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.output = Output(self)
        Window.clearcolor = (10 / 255, 10 / 255, 10 / 255, 0.9)

    def append(self, instance):
        instance.append(self.output)
