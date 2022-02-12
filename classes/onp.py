import operator

from classes.constants.operator import OperatorConst
from classes.helpers.helper import is_numeric


class Onp:
    operators = {
        OperatorConst.ADD: operator.add,
        OperatorConst.SUB: operator.sub,
        OperatorConst.MUL: operator.mul,
        OperatorConst.DIV: operator.truediv,
        OperatorConst.MOD: operator.mod,
        OperatorConst.POW: operator.pow,
    }

    def calc(self, onp):
        stack = []
        while onp:
            item = onp.pop(0)

            if is_numeric(item):
                stack.append(item)
            else:
                a = float(stack.pop())
                b = float(stack.pop())
                res = self.operators[item](b, a)
                stack.append(res)

        return stack.pop()
