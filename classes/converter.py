from classes.constants.operator import OperatorConst
from classes.helpers.helper import is_numeric


class Converter:
    priority = {
        OperatorConst.LBR: 0,
        OperatorConst.ADD: 1,
        OperatorConst.SUB: 1,
        OperatorConst.RBR: 1,
        OperatorConst.MUL: 2,
        OperatorConst.DIV: 2,
        OperatorConst.MOD: 2,
        OperatorConst.POW: 3
    }

    def convert(self, expression):
        expression = self.fix_expression(expression)

        stack = []
        out = []

        for item in expression:
            if item not in self.priority:
                out.append(item)
            elif item == OperatorConst.LBR:
                stack.append(item)
            elif item == OperatorConst.RBR and OperatorConst.LBR in stack:
                while stack[len(stack) - 1] != OperatorConst.LBR:
                    out.append(stack.pop())
                stack.pop()
            elif not stack or self.priority.get(item) > self.priority.get(stack[len(stack) - 1]):
                stack.append(item)
            else:
                while len(stack) > 0 and (self.priority.get(stack[len(stack) - 1]) >= self.priority.get(item)):
                    out.append(stack.pop())
                stack.append(item)

        while stack:
            out.append(stack.pop())

        return list(filter(lambda elem: elem != OperatorConst.LBR and elem != OperatorConst.RBR, out))

    def fix_expression(self, expression):
        if not expression:
            return []

        if not is_numeric(expression[-1]):
            expression = expression[:-1]

        return expression
