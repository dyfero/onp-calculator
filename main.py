from kivy.app import App
from layout import CalculatorLayout


class Calculator(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    Calculator().run()
