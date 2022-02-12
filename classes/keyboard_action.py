from classes.constants.operator import OperatorConst
from classes.dot import Dot
from classes.equals import Equals
from classes.left_bracket import LeftBracket
from classes.number import Number
from classes.remove import Remove
from classes.right_bracket import RightBracket
from classes.sign import Sign


class KeyboardAction:
    MODIFIERS = {
        'numlock',
        'shift'
    }

    def __init__(self):
        self.shift_actions = {
            54: Sign(OperatorConst.POW),  # ^
            56: Sign(OperatorConst.MUL),  # *
            57: LeftBracket(),  # (
            48: RightBracket(),  # )
            61: Sign(OperatorConst.ADD)  # +
        }

        self.single_actions = {
            48: Number(0),
            256: Number(0),

            49: Number(1),
            257: Number(1),

            50: Number(2),
            258: Number(2),

            51: Number(3),
            259: Number(3),

            52: Number(4),
            260: Number(4),

            53: Number(5),
            261: Number(5),

            54: Number(6),
            262: Number(6),

            55: Number(7),
            263: Number(7),

            56: Number(8),
            264: Number(8),

            57: Number(9),
            265: Number(9),

            267: Sign(OperatorConst.DIV),
            47: Sign(OperatorConst.DIV),

            268: Sign(OperatorConst.MUL),

            269: Sign(OperatorConst.SUB),
            45: Sign(OperatorConst.SUB),

            270: Sign(OperatorConst.ADD),

            46: Dot(),
            44: Dot(),
            266: Dot(),

            271: Equals(),
            61: Equals(),
            13: Equals(),

            8: Remove()
        }

    def action(self, keycode, modifiers, output):
        if all(elem in modifiers for elem in self.MODIFIERS) and keycode[0] in self.shift_actions:
            ob = self.shift_actions[keycode[0]]
            ob.append(output)
            return

        if keycode[0] in self.single_actions:
            ob = self.single_actions[keycode[0]]
            ob.append(output)
            return
