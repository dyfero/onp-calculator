from kivy.app import App
from layout.layout import CalculatorLayout


class Calculator(App):
    def build(self):
        return CalculatorLayout()
