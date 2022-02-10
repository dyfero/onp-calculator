import operator

from classes.constants.operator import OperatorEnum
from classes.helpers.helper import is_numeric


class Onp:
    operators = {
        OperatorEnum.ADD: operator.add,
        OperatorEnum.SUB: operator.sub,
        OperatorEnum.MUL: operator.mul,
        OperatorEnum.DIV: operator.truediv,
        OperatorEnum.MOD: operator.mod,
        OperatorEnum.POW: operator.pow,
    }

    def calc(self, onp):
        stack = []
        while onp:
            item = float(onp.pop(0))

            if is_numeric(item):
                stack.append(item)
            else:
                a = float(stack.pop())
                b = float(stack.pop())
                res = self.operators[item](b, a)
                stack.append(res)

        return float(stack.pop())
