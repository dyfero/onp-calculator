from kivy.uix.widget import Widget

from classes.keyboard_action import KeyboardAction
from classes.output import Output
from kivy.core.window import Window


class CalculatorLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard_action = KeyboardAction()
        self.output = Output(self)
        self.init()

    def init(self):
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        Window.clearcolor = (10 / 255, 10 / 255, 10 / 255, 0.9)

    def append(self, instance):
        instance.append(self.output)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self._keyboard_action.action(keycode, modifiers, self.output)

